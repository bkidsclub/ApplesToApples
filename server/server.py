import asyncio
import websockets
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

players = {}

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

clients = set()

green = 'green'
hand = ['a', 'b']
round = 0
toJudge = []
judge = ''

async def hello(websocket, path):
    global players
    global judge
    global green
    global clients
    global hand
    global round
    global toJudge


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
                    


            if id in players:
                response = {
                    'player': id,
                    'name': players[id]['name'],
                    'serverError': "",
                    'green': green,
                    'hand': hand,
                    'submitted': players[id]['submitted'],
                    'winner': '',
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


start_server = websockets.serve(hello, '127.0.0.1', 8123)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
