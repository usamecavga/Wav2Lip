import asyncio
import websockets
import subprocess
import sys

async def handle_connection(websocket, path):
    try:
        # Receive parameters from the WebSocket connection
        parameters = await websocket.recv()

        # Run the interface.py script with the received parameters
        subprocess.run(["python3", "/workspace/Wav2Lip/interface.py"] + parameters.split(), check=True)
    except Exception as e:
        print(f"Error: {e}")

# Start the WebSocket server
start_server = websockets.serve(handle_connection, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()