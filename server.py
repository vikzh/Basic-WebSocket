import asyncio
import websockets


async def server(websocket, path):
    # Get received data from websocket
    data = await websocket.recv()

    # Send response back to client
    await websocket.send("Your message is: " + data)

# Create websocket server
start_server = websockets.serve(server, "localhost", 6789)

# Start and run websocket server forever
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

