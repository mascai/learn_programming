import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info("peername")
    print(f"Received {message} from {addr}")
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(
    handle_echo, 
    "127.0.0.1", # listen host
    10001, # port
    loop=loop
)


server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
