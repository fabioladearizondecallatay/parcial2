"""Este archivo opcional permite ejecutar todo el sistema distribuido en una sola terminal, incluyendo:
El servidor central.
El sistema local que genera y procesa noticias.
Los subscriptores remotos.
Es útil para probar el flujo completo desde un solo lugar."""

import asyncio
from sistema_local import main as sistema_main
from servidor_central import iniciar_servidor_central
from subscriptores_remotos import main as subscriptores_main

async def main():
    await asyncio.gather(
        iniciar_servidor_central(),
        sistema_main(),
        subscriptores_main()
    )

if __name__ == "__main__":
    asyncio.run(main())
