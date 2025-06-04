import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('请发送便当照片')

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    photo_file = await update.message.photo[-1].get_file()
    photos_dir = 'photos'
    os.makedirs(photos_dir, exist_ok=True)
    file_path = os.path.join(photos_dir, f"{photo_file.file_id}.jpg")
    await photo_file.download_to_drive(file_path)
    await update.message.reply_text('图片已收到')

def main() -> None:
    if not TOKEN:
        print('Please set TELEGRAM_TOKEN environment variable.')
        return
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.run_polling()

if __name__ == '__main__':
    main()
