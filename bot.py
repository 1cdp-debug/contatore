import os
import threading
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# 1. Creiamo un mini server Flask per mantenere sveglio Render tramite i ping
app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "Bot Telegram attivo e operativo!"

def run_web():
    port = int(os.getenv("PORT", 10000))
    app_web.run(host="0.0.0.0", port=port)

# 2. Mostra i tre pulsanti non appena si avvia il bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "Contatore", 
                web_app=WebAppInfo(url="https://1cdp-debug.github.io/contatore/index.html")
            ),
            InlineKeyboardButton(
                "Ruota SM", 
                web_app=WebAppInfo(url="https://1cdp-debug.github.io/contatore/ruota_magica_telegram_mini_app.html")
            )
        ],
        [
            InlineKeyboardButton(
                "Performance", 
                web_app=WebAppInfo(url="https://1cdp-debug.github.io/contatore/utilizzo_cesso.html")
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Benvenuto! Scegli quale utility aprire:", reply_markup=reply_markup)

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    
    # Avviamo il mini server web in background su un thread separato
    t = threading.Thread(target=run_web)
    t.daemon = True
    t.start()

    # Avviamo il bot di Telegram normalmente
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
