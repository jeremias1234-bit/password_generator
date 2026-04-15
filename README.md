# 🔐 Generador de Contraseñas CLI

Aplicación desarrollada en Python que permite generar contraseñas seguras de forma interactiva desde la terminal.

---

## 🚀 Funcionalidades

- Generación de contraseñas seguras
- Opciones de generación:
  - Solo números
  - Solo letras
  - Completa (letras, números y símbolos)
- Validación de longitud:
  - Bloqueo para contraseñas inseguras (≤ 4 caracteres)
  - Advertencia para contraseñas débiles (< 8 caracteres)
- Historial de contraseñas generadas en la sesión
- Manejo de errores en entrada de datos

---

## 🛠 Tecnologías utilizadas

- Python
- Librerías estándar:
  - `string`
  - `secrets` (generación segura de caracteres)

---

## ▶️ Uso

Ejecutar el programa desde la terminal:

```bash
python main.py

Luego:
Ingresar la longitud de la contraseña
Elegir el tipo de contraseña
Visualizar la contraseña generada

📌 Objetivo del proyecto
Este proyecto fue desarrollado como práctica para:
mejorar la lógica de programación
trabajar con estructuras de control
aplicar validaciones y manejo de errores
construir herramientas funcionales desde consola

👨‍💻 Autor
Jeremías

🧠 Nota
Proyecto inicial enfocado en práctica y aprendizaje, con mejoras progresivas hacia estándares más profesionales.
