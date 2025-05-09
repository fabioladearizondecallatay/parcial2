"""Este archivo lanza tres subscriptores remotos, uno en cada ciudad: Madrid, Londres y São Paulo.
Cada uno escucha en un puerto diferente y recibe las noticias reenviadas por el servidor central.
Al recibir una noticia, simplemente la muestra por consola."""

import asyncio
import json

async def iniciar_subscriptor(ciudad, puerto):
    async def handler(reader, writer):
        data = await reader.read(4096)
        articulo = json.loads(data.decode())
        print(f"🟢 [{ciudad.upper()}] Noticia recibida: {articulo['titulo']}")
        writer.close()
        await writer.wait_closed()

    server = await asyncio.start_server(handler, 'localhost', puerto)
    print(f"🟢 [{ciudad.upper()}] Esperando noticias en puerto {puerto}...")
    async with server:
        await server.serve_forever()

async def main():
    await asyncio.gather(
        iniciar_subscriptor("Madrid", 9001),
        iniciar_subscriptor("Londres", 9002),
        iniciar_subscriptor("SaoPaulo", 9003)
    )

if __name__ == "__main__":
    asyncio.run(main())
