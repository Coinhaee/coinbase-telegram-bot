from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "7959225593:AAEFtB2MOijObph9Znieeveq4isDc6T1G7E"
FORWARD_TO_USERNAME = "@coinbaseeuropesupport"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛠 Jag behöver teknisk support", callback_data="tech")],
        [InlineKeyboardButton("💸 Jag har frågor om en betalning", callback_data="payment")],
        [InlineKeyboardButton("🔐 Jag misstänker bedrägeri", callback_data="fraud")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Hej! Vad gäller ditt ärende?", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    response_map = {
        "tech": "🛠 Teknisk support",
        "payment": "💸 Betalningsfråga",
        "fraud": "🔐 Misstänkt bedrägeri"
    }

    choice = response_map.get(query.data, "Support")

    link = f"https://t.me/{FORWARD_TO_USERNAME.lstrip('@')}"
    text = f"{choice} registrerad.\n\n➡️ Klicka här för att chatta med support: {link}"
    await query.edit_message_text(text=text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot is running...")
    app.run_polling()
