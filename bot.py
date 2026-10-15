import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Appena l'utente avvia il bot, compaiono SUBITO Contatore e Roulette
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "Contatore", 
                web_app=WebAppInfo(url="https://1cdp-debug.github.io/contatore/index.html")
            ),
            InlineKeyboardButton(
                "Ruota S&M", 
                web_app=WebAppInfo(url="https://1cdp-debug.github.io/contatore/ruota_magica_telegram_mini_app.html")
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Benvenuto! Scegli quale utility aprire:", reply_markup=reply_markup)

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    
    application = Application.builder().token(token).build()

    # Si attiva direttamente con il comando di avvio
    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == "__main__":
    main()
