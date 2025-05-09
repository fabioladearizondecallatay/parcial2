# 📰 Sistema Distribuido de Noticias – Publisher-Subscriber + Cliente-Servidor

Este proyecto simula un sistema de adquisición, procesamiento y distribución de noticias utilizando una combinación de arquitecturas `Publisher-Subscriber` y `Cliente-Servidor`.

---

## 📦 Estructura de ficheros

- `sistema_local.py` → Publica y procesa artículos desde Asia, África y América, y los envía al servidor central.
- `servidor_central.py` → Almacena y analiza los artículos, y los reenvía a servidores remotos.
- `subscriptores_remotos.py` → Simula servidores remotos en Madrid, Londres y São Paulo.
- `comunicacion.py` → Módulo compartido con funciones de conexión TCP.
- `main.py` → Ejecuta todo el sistema en una única terminal (opcional).

---

## 🚀 Ejecución en 3 terminales (modo distribuido real)

### 🟢 Terminal 1 – Sistema Local
```bash
cd noticias_system
python3 sistema_local.py
```
Simula fuentes de noticias, procesa los datos y los envía al servidor central.

### 🟣 Terminal 2 – Servidor Central
```bash
cd noticias_system
python3 servidor_central.py
```
Recibe, almacena, analiza y reenvía artículos a los servidores remotos.

### 🟢 Terminal 3 – Subscriptores Remotos
```bash
cd noticias_system
python3 subscriptores_remotos.py
```
Reciben y muestran las noticias reenviadas por el servidor central.

---

## 💡 Ejecución alternativa (todo en una terminal)

```bash
cd noticias_system
python3 main.py
```
Ejecuta automáticamente todos los componentes (ideal para demostraciones rápidas o desarrollo).
