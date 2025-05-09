"""Este archivo representa el sistema local distribuido que simula tres fuentes de noticias: Asia, África y América.
Cada fuente (publisher) genera noticias en formatos variados (JSON, XML, HTML).
Estas noticias son procesadas (normalizadas) por el sistema local y enviadas al servidor central a través de una conexión TCP."""

import asyncio
import random
import time
from comunicacion import enviar_al_servidor_central

async def publisher(nombre, queue):
    formatos = ["JSON", "XML", "HTML"]
    while True:
        await asyncio.sleep(random.randint(1, 4))
        articulo = {
            "source": nombre,
            "format": random.choice(formatos),
            "content": f"<{random.choice(['xml','html',''])}>Artículo de {nombre} a las {time.strftime('%X')}</>"
        }
        await queue.put(articulo)
        print(f"✅ [SISTEMA] Fuente {nombre} publicó un nuevo artículo.")

def normalizar_articulo(articulo):
    formato = articulo["format"]
    contenido = articulo["content"]
    if formato == "XML":
        contenido = contenido.replace("<xml>", "").replace("</>", "")
    elif formato == "HTML":
        contenido = contenido.replace("<html>", "").replace("</>", "")
    return {
        "titulo": f"{articulo['source']} - Noticia procesada",
        "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
        "contenido": contenido
    }


async def procesador(queue):
    while True:
        articulo = await queue.get()
        normalizado = normalizar_articulo(articulo)
        print(f"✅ [SISTEMA] Enviando al servidor central: {normalizado['titulo']}")
        await enviar_al_servidor_central(normalizado)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    publishers = [
        publisher("Asia_News", queue),
        publisher("Africa_Times", queue),
        publisher("America_Reports", queue)
    ]
    await asyncio.gather(*(asyncio.create_task(p) for p in publishers), procesador(queue))

if __name__ == "__main__":
    asyncio.run(main())
