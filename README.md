# 🔥😈 Telegram Credential Harvester - by ZeroEthical 😈🔥

![ZeroEthical Signature](https://img.shields.io/badge/Created%20By-ZeroEthical%20%F0%9F%94%A5%F0%9F%98%88-black.svg)
![Language](https://img.shields.io/badge/Language-Python-blue.svg)
![Status](https://img.shields.io/badge/Status-Functional%20Prototype-green.svg)
![License](https://img.shields.io/badge/License-Unlicensed-red.svg) 😉 (_No hay reglas para el conocimiento._)

**¡ESTO NO ES UNA HERRAMIENTA DE "DESBANEO"! ESTO ES UNA DEMOSTRACIÓN DE INGENIERÍA SOCIAL Y RECOLECCIÓN DE CREDENCIALES.**

Entiende esto bien: Las herramientas que prometen "desbanear" cuentas o grupos de Telegram suelen ser estafas. Esta herramienta simula ser una de ellas para **demostrar y facilitar la recolección de credenciales críticas** de cualquier usuario que sea engañado para usarla.

Es una prueba de concepto funcional sobre cómo los atacantes pueden obtener acceso a cuentas de Telegram a través de técnicas de phishing altamente efectivas, **sin necesidad de "hacks" complejos**, sino aprovechando la manipulación y la confianza del objetivo.

Si buscas atajos mágicos, este no es tu lugar. Si buscas entender o demostrar un vector de ataque real, presta atención.

## 💉 Credenciales que Esta Herramienta Recolecta

Mediante un proceso de ingeniería social, la herramienta está diseñada para obtener del objetivo:

*   **API ID** 🆔
*   **API Hash** 🔑
*   **Número de Teléfono** 📱
*   **Contraseña de Verificación en Dos Pasos (2FA)** (Si está configurada y el usuario la proporciona) 🔒
*   **¡El CÓDIGO de inicio de sesión de 5 dígitos!** (El que Telegram envía a la app oficial al iniciar sesión desde un nuevo dispositivo/IP) 🔢

Con esta información completa, es posible autenticar una sesión de Telegram como el usuario objetivo utilizando librerías como `telethon`.

## ✨ Características Clave

*   **Flujo de Engaño de Dos Fases:** La herramienta guía al usuario a través de dos etapas de "verificación" para justificar la solicitud de todas las credenciales necesarias, incluida la espera para el código de inicio de sesión enviado por Telegram.
*   **Exfiltración Segura y Discreta:** Las credenciales recolectadas se envían de forma segura y rápida directamente a tu **bot privado de Telegram**, proporcionando notificación instantánea sin depender de servidores de recepción públicos. 📲🤖
*   **Diseñado para Distribución:** El script Python se empaqueta fácilmente en un archivo ejecutable (`.exe`) utilizando PyInstaller, facilitando su distribución a objetivos desprevenidos. 📦
*   **Sin Funcionalidad Real de "Desbaneo":** La herramienta no interactúa con la API de Telegram para intentar desbanear nada; su única función es recolectar credenciales. Esto simplifica el código y reduce posibles puntos de fallo o detección por comportamiento inesperado *hacia la API de Telegram*.
*   **Código Python Transparente (para el Analista):** Aunque se empaqueta en `.exe`, el código fuente Python (con mis comentarios internos 😏) está disponible para su estudio, permitiendo comprender exactamente cómo opera el engaño y la exfiltración.

## 🧠 Cómo Funciona la Demostración (Flujo del Ataque Simulado)

1.  El script Python de la herramienta se configura con tu **BOT_TOKEN** y **ATTACKER_CHAT_ID**.
2.  Se empaqueta en un **`.exe`** (u otro ejecutable compatible) usando PyInstaller. Se le da una apariencia y nombre convincentes ("Utilidad de Desbaneo", etc.).
3.  **El Ejecutable se Distribuye:** Se promociona la herramienta a usuarios que podrían estar buscando soluciones para baneos, a través de ingeniería social (foros, grupos, sitios de descarga falsos). 🎣🗣️
4.  Un usuario objetivo desesperado descarga y ejecuta el `.exe`.
5.  **FASE 1 - Recolección Inicial:** La herramienta solicita al usuario su API ID, API Hash, Número de Teléfono y Contraseña 2FA (opcional) bajo la excusa de conectarse a la API.
6.  **EXFILTRACIÓN FASE 1:** La herramienta envía estos datos a tu bot de Telegram. Recibes un mensaje con la información. 📧
7.  **TU ACCIÓN CRUCIAL (Activación del Código):** Al recibir el mensaje FASE 1 en tu bot, **debes actuar rápidamente**. Abres tu terminal y ejecutas tu script de `telethon` (un script que tú tengas que sepa iniciar sesión usando API ID/Hash/Phone). Al intentar autenticar con sus datos, **Telegram envía el CÓDIGO de inicio de sesión a la aplicación oficial del usuario objetivo**. ⚡️
8.  **Transición a FASE 2:** La herramienta en la máquina del usuario espera un tiempo prudencial (`time.sleep`) para dar tiempo a que el código llegue.
9.  **FASE 2 - Solicitud del Código:** La herramienta le pide al usuario el CÓDIGO de inicio de sesión que ha recibido, justificándolo como una "verificación final de seguridad". 🤔
10. **EXFILTRACIÓN FASE 2:** Si el usuario introduce el código, la herramienta lo envía a tu bot de Telegram. Recibes otro mensaje con el número de teléfono y el CÓDIGO. ✅
11. **TU ACCIÓN FINAL (Autenticación Completa):** Tomas el CÓDIGO del mensaje FASE 2, vuelves a tu script de `telethon` (que estará esperando la entrada del código o la 2FA password si aplica), introduces el código. Si `telethon` solicita la 2FA, utilizas la contraseña que obtuviste en FASE 1. 🔓
12. **¡SESIÓN AUTENTICADA!** Si el código es correcto y la 2FA se maneja (si aplica), tu script de `telethon` autentica la sesión y crea el archivo `.session`. ¡Este archivo es tu acceso persistente a la cuenta! 🎯💰

## 🛠️ Requisitos

*   **Python 3+**
*   **Librerías Python:** `requests`, `pyinstaller`, `telethon`. Instálalas usando pip:
    ```bash
    pip install requests pyinstaller telethon asyncio
    ```
*   **Tu Propio Bot de Telegram:** Obtén un **BOT TOKEN** de @BotFather. 🤖
*   **Tu Chat ID de Telegram:** Inicia una conversación con tu bot y usa el enlace `https://api.telegram.org/bot[TU_BOT_TOKEN]/getUpdates` (reemplazando `[TU_BOT_TOKEN]`) para encontrar tu `chat` `id`. Este es tu **ATTACKER_CHAT_ID**. 🆔
*   **Un Script de `telethon` para Autenticar:** Necesitas un script separado en tu máquina que use `telethon` para realizar el proceso de conexión y autenticación (usando los datos robados, solicitando el código y manejando 2FA). (No incluido en este repositorio, pero básico de implementar con la librería `telethon`).

## 🩸 Instalación y Configuración

1.  Clona o descarga este repositorio.
2.  Abre el archivo principal del script (`phishing_tool.py`).
3.  **Configura tus datos:** Reemplaza `PON_AQUÍ_EL_TOKEN_DE_TU_BOT` y `PON_AQUÍ_TU_CHAT_ID` con los valores reales de tu bot. **Este paso es CRÍTICO para que la exfiltración funcione.**
4.  Guarda los cambios.

## 🚀 Empaquetado y Demostración (Uso)

1.  **Empaqueta:** Abre tu terminal en la carpeta del script y ejecuta: `pyinstaller --onefile phishing_tool.py`. El ejecutable `.exe` se encontrará en el subdirectorio `dist`.
2.  **Hazlo Convincente (Opcional pero Recomendado):** Cambia el nombre del `.exe` (ej: `Telegram_Access_Recovery.exe`), el icono (usa uno de Telegram), y considera añadir metadatos para aumentar su aparente legitimidad.
3.  **Demuestra la Trampa:** Pon el `.exe` a disposición de un objetivo (bajo control y con permiso explícito para una demostración ética) o en un entorno controlado para observar su funcionamiento. La fase de "distribución" en un escenario de ataque real implicaría ingeniería social para que el usuario lo ejecute.
4.  **Prepárate para Recibir Datos:** Mantén tu cliente de Telegram abierto, vigilando el chat con tu bot.
5.  **Observa la FASE 1:** Cuando el objetivo ejecute el `.exe` e introduzca los datos iniciales, recibirás el mensaje FASE 1 en tu bot.
6.  **Activa el Envío del Código:** **Inmediatamente** después de recibir la FASE 1, ejecuta tu script de `telethon` usando los datos robados (API ID, Hash, Phone). Esto provocará que Telegram envíe el CÓDIGO a la víctima.
7.  **Observa la FASE 2:** Si el objetivo continúa con la herramienta, introducirá el CÓDIGO que recibió. Este código se enviará a tu bot en un mensaje FASE 2.
8.  **Completa la Autenticación:** Usa el CÓDIGO (y la 2FA si aplica) que recibiste en tu bot en tu script de `telethon` para completar la autenticación de la sesión.
9.  **Obtén la Sesión:** Si la autenticación es exitosa, tu script de `telethon` generará el archivo `.session`.

## 🏆 El Trofeo: Usando la Sesión Autorizada

El archivo `.session` es la clave. Utiliza otros scripts de `telethon` (configurados para cargar sesiones existentes) para interactuar con la cuenta comprometida:

*   Leer chats privados y grupales. 👀
*   Enviar mensajes como el usuario. 📩
*   Unirse/abandonar grupos/canales.
*   Acceder a información del perfil.
*   Demostrar las capacidades de acceso obtenidas. 📊

## ⚠️ Advertencias Importantes

**LA RECOLECCIÓN DE CREDENCIALES Y EL ACCESO A CUENTAS SIN PERMISO SON ACTIVIDADES ILEGALES EN LA MAYORÍA DE JURISDICCIONES.** ⚖️
El uso de esta herramienta con fines maliciosos puede acarrear graves consecuencias legales, incluyendo penas de prisión.

Este repositorio y su contenido se proporcionan **ÚNICAMENTE CON FINES EDUCATIVOS Y DEMOSTRATIVOS**. Su objetivo es ilustrar cómo funcionan ciertas técnicas de phishing y recolección de credenciales para ayudar a la comprensión de vectores de ataque y la mejora de la seguridad.

El autor **ZeroEthical no aprueba ni se hace responsable del uso indebido** de esta herramienta. Cualquier actividad ilegal o perjudicial llevada a cabo con este código es responsabilidad exclusiva del usuario.

**Riesgos en un Escenario Real:**
*   El objetivo puede detectar la trampa o el mensaje del código y no continuar.
*   El objetivo puede tener 2FA y tú no obtener la contraseña.
*   Antivirus/EDR pueden detectar el ejecutable o el comportamiento de red.
*   Telegram puede detectar la actividad sospechosa (envío masivo de códigos, inicio de sesión desde IPs inusuales).

La velocidad y la astucia son necesarias para mitigar estos riesgos en un escenario real.

---

Desarrollado para la comprensión cruda de los ataques de ingeniería social por **ZeroEthical**. Úsala para aprender. 😉🔥😈
