import asyncio
import websockets
import json
import pprint
import collections
import random
import load

pp = pprint.PrettyPrinter(indent=4)

players = collections.OrderedDict()

"""
type alias Model =
  { player : Int
  , name : String
  , serverError : String
  , green : String
  , hand : List String
  , submitted : String
  , winner : String
  , score : Int
  , round : Int
  , toJudge : List String
  , judgeName : String
  }
"""
gapple = []
rapple = []
clients = set()
green = ''
round = 0
toJudge = []
judge = ''
winner = ''

def generate_green():
    return gapple.pop()

def generate_hand(hand):
    for i in range(7 - len(hand)):
        hand.append(rapple.pop())
    return hand

def reload_game():
    global gapple
    global rapple
    global judge
    global green
    global clients
    global round
    global toJudge
    global winner
    gapple = load.loadCards('GAPPLE')
    rapple = load.loadCards('RAPPLE')
    clients = set()
    green = generate_green()
    round = 0
    toJudge = []
    judge = ''
    winner = ''




async def hello(websocket, path):
    global players
    global judge
    global green
    global clients
    global round
    global toJudge
    global winner

    id = None

    clients.add(websocket)

    try:
        while True:
            broadcast = False
            message = await websocket.recv()
            if len(message) > 0:
                request = json.loads(message)

                pp.pprint(request)

                if 'name' in request:
                    print('sign up request')
                    if id is None:
                        if request['id'] not in players:
                            id = request['id']
                            players[request['id']] = {
                                'name': request['name'],
                                'score': 0,
                                'hand': generate_hand([]),
                                'submitted': ""
                            }
                            broadcast = True
                            if len(players) == 1:
                                # first person is the judge
                                judge = players[id]['name']
                                print('judge = ' + judge)

                        else:
                            raise RuntimeError("ID already exists")
                    else:
                        raise RuntimeError('player already signed up!')
                elif 'red' in request:
                    print('player selected a card')
                    if players[id]['name'] != judge:
                        players[id]['submitted'] = request['red']
                    if len(players) > 1 and all([players[id]['submitted'] != "" for id in players if players[id]['name'] != judge]):
                        print("judging time")
                        broadcast = True
                        toJudge = [players[id]['submitted'] for id in players if players[id]['name'] != judge]
                elif 'winner' in request:
                    print('judge submitted winner, round over')
                    winner = request['winner']
                    for tid in players:
                        if players[tid]['submitted'] == winner:
                            players[tid]['score'] += 1
                            break
                    broadcast = True
                elif 'nextRound' in request:
                    print("next round request received")
                    if request['nextRound'] == True:
                        print("next round is true")
                        judgeID = 0
                        for tid in players:
                            if players[tid]['name'] == judge:
                                judgeID = tid
                                break
                        if judgeID == request['id']:
                            print("next round")
                            # Go to next round
                            round += 1
                            for tid in players:
                                if players[tid]['submitted'] in players[tid]['hand']:
                                    players[tid]['hand'].remove(players[tid]['submitted'])
                                players[tid]['hand'] = generate_hand(players[tid]['hand'])
                                players[tid]['submitted'] = ''
                            toJudge = []
                            for i, tid in enumerate(players):
                                if i == round % len(players):
                                    judge = players[tid]['name']
                                    break
                            broadcast = True
                            winner = ''
                            # new green apple
                            green = generate_green()



            if id in players:
                response = {
                    'player': id,
                    'name': players[id]['name'],
                    'serverError': "",
                    'green': green,
                    'hand': players[id]['hand'],
                    'submitted': players[id]['submitted'],
                    'winner': winner,
                    'score': players[id]['score'],
                    'round': round,
                    'toJudge': toJudge,
                    'judgeName': judge,
                    'allPlayers': [players[id]['name'] for id in players]
                }

                if not broadcast:
                    await websocket.send(json.dumps(response))
                else:
                    await asyncio.wait([ws.send('') for ws in clients])
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        if id is not None:
            del players[id]
        clients.remove(websocket)
        print("client disconnected")
        print("number of players: " + str(len(players)))
        if len(players) == 0:
            reload_game()


reload_game()
start_server = websockets.serve(hello, '127.0.0.1', 8123)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
