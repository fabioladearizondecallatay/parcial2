"""Este fichero representa el servidor central.
Recibe los artículos procesados del sistema local, los almacena en memoria y los analiza (por ejemplo, buscando palabras clave como "crisis").
Posteriormente, reenvía cada artículo a tres servidores remotos simulados: Madrid, Londres y São Paulo."""

import asyncio
import json
from comunicacion import reenviar_a_suscriptores

almacen = []

async def manejar_sistema(reader, writer):
    data = await reader.read(4096)
    articulo = json.loads(data.decode())
    almacen.append(articulo)
    print(f"🟣 [CENTRAL] Artículo recibido: {articulo['titulo']} (Total: {len(almacen)})")

    # Simular análisis
    if "crisis" in articulo["contenido"].lower():
        print(f"🟣 [CENTRAL] ALERTA: '{articulo['titulo']}' contiene palabra clave 'crisis'")

    # Reenviar a suscriptores
    await reenviar_a_suscriptores(articulo)
    writer.close()
    await writer.wait_closed()

async def iniciar_servidor_central():
    server = await asyncio.start_server(manejar_sistema, 'localhost', 8888)
    print("🟣 [CENTRAL] Servidor central en marcha en puerto 8888...")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(iniciar_servidor_central())
