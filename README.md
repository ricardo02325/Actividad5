# Actividad 5

Este repositorio contiene el desarrollo, archivos y documentación correspondiente a la **Actividad 5**, incluyendo su descripción, desarrollo, conclusiones y cualquier material complementario necesario para su entrega.

---

## 📌 Descripción General

En esta actividad se realiza el análisis, desarrollo y documentación de un ejercicio práctico asignado.  
El repositorio tiene como objetivo mantener organizado el contenido y facilitar la revisión del trabajo.

---

## 📂 Contenido del Repositorio

- `detectar` — Archivos principal del proyecto.
- `README.md` — Descripción principal del proyecto.  

---

## 📝 Instrucciones de Uso

1. Clonar el repositorio:

```bash
git clone https://github.com/ricardo02325/Actividad5.git
Entrar a la carpeta:

cd Actividad5
Explorar los archivos según la estructura del proyecto.

# Detector de Gestos – Actividad 5

Este repositorio contiene un único archivo principal: `detectar.py`, que implementa un sistema básico de detección de gestos usando visión por computadora.

---

## 📌 Descripción del Proyecto

El programa detecta manos mediante MediaPipe y reconoce gestos simples basados en el conteo de dedos, por ejemplo: pulgar arriba/abajo, mano abierta, OK, etc.

---

## 📁 Archivo principal

### `detectar.py`
Contiene:

- Inicialización de MediaPipe Hands
- Función para contar dedos levantados
- Función para interpretar el gesto
- Lectura de la cámara y bucle principal
- Dibujo de landmarks y visualización en tiempo real

---

## ▶️ Ejecución

1. Instalar dependencias (si aún no están instaladas):

```powershell
pip install opencv-python mediapipe
```

2. Ejecutar el programa:

```powershell
python detectar.py
```

La ventana mostrará la cámara y los gestos detectados en tiempo real.

---

## 📝 Requisitos

- Python 3.x
- OpenCV
- MediaPipe
- Cámara web

---

## 👤 Autor

Ricardo Gregorio

Universidad de Colima