import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# 1. Comando /start che mostra il pulsante "Utility"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Utility", callback_data="menu_utility")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Ciao! Clicca qui sotto per accedere alle utility:", reply_markup=reply_markup)

# 2. Menu "Utility" che mostra Contatore e Roulette
async def utility_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton(
                "Contatore", 
                web_app=WebAppInfo(url="https://1cdp-debug.github.io/contatore/index.html")
            ),
            InlineKeyboardButton(
                "Roulette", 
                web_app=WebAppInfo(url="https://1cdp-debug.github.io/contatore/ruota_magica_telegram_mini_app.html")
            )
        ],
        [InlineKeyboardButton("🔙 Indietro", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Scegli una utility:", reply_markup=reply_markup)

# 3. Torna al menu principale
async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    keyboard = [[InlineKeyboardButton("Utility", callback_data="menu_utility")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Menu principale:", reply_markup=reply_markup)

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(utility_menu, pattern="^menu_utility$"))
    application.add_handler(CallbackQueryHandler(main_menu, pattern="^main_menu$"))

    application.run_polling()

if __name__ == "__main__":
    main()
