import asyncio
import websockets


async def main():
    uri = "wss://www.seismicportal.eu/standing_order/websocket"
    async with websockets.connect(uri) as websocket:
        seismic_event = await websocket.recv()
        print(f"< {seismic_event}")

asyncio.get_event_loop().run_until_complete(main())
