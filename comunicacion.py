"""Contiene funciones de comunicación TCP:
enviar_al_servidor_central: cliente que conecta con el servidor central para enviar noticias.
reenviar_a_suscriptores: el servidor central usa esta función para reenviar artículos a los servidores de Madrid, Londres y São Paulo."""

import asyncio
import json

# Cliente que envía al servidor central
async def enviar_al_servidor_central(articulo, host='localhost', puerto=8888):
    reader, writer = await asyncio.open_connection(host, puerto)
    writer.write(json.dumps(articulo).encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()

# Reenvío del servidor central a los suscriptores remotos
PUERTOS_SUBSCRIPTORES = {
    "Madrid": 9001,
    "Londres": 9002,
    "SaoPaulo": 9003
}

async def reenviar_a_suscriptores(articulo):
    for ciudad, puerto in PUERTOS_SUBSCRIPTORES.items():
        try:
            reader, writer = await asyncio.open_connection('localhost', puerto)
            writer.write(json.dumps(articulo).encode())
            await writer.drain()
            writer.close()
            await writer.wait_closed()
            print(f"🔁 [CENTRAL] Reenviado a {ciudad}: {articulo['titulo']}")
        except:
            print(f"⚠️ [CENTRAL] No se pudo conectar con {ciudad}")
