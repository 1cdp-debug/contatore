import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Mostra i tre pulsanti non appena si avvia il bot
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
    
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == "__main__":
    main()
