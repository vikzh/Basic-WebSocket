import asyncio
import websockets
import json


async def client():
    uri = 'ws://localhost:6789'
    async with websockets.connect(uri) as websocket:
        # Prepare data
        phrase = input('Enter your text: ')
        data = json.dumps({"phrase": phrase})

        # Send data to server
        await websocket.send(data)

        response = await websocket.recv()
        print(response)

asyncio.get_event_loop().run_until_complete(client())