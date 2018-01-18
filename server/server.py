import asyncio
import websockets

async def hello(websocket, path):
    print('waiting')
    name = await websocket.recv()
    print("< {}".format(name))

    greeting = "Hello {}!".format(name)
    await websocket.send(greeting)
    print("> {}".format(greeting))

start_server = websockets.serve(hello, '127.0.0.1', 8123)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
