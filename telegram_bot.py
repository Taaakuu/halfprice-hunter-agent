import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes



TOKEN = "7853503988:AAHlF5odHI7aXZecyKjD40HWvBewjLtmXGQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('请发送便当照片')

from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='japan')

def ocr_image(image_path):
    result = ocr.ocr(image_path, cls=True)
    lines = []
    for line in result:
        for box in line:
            text = box[1][0]
            if any(keyword in text for keyword in ['半額', '円', '牛', '肉', '豚', '割']):
                lines.append(text)
    return lines 

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    photo_file = await update.message.photo[-1].get_file()
    photos_dir = 'photos'
    os.makedirs(photos_dir, exist_ok=True)
    file_path = os.path.join(photos_dir, f"{photo_file.file_id}.jpg")
    await photo_file.download_to_drive(file_path)
    # 加入 OCR 分析
    texts = ocr_image(file_path)
    recognized_text = '\n'.join(texts)
    print('识别结果:\n', recognized_text) 

    await update.message.reply_text('图片已收到,我识别到以下内容:\n' + recognized_text)




def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.run_polling()

if __name__ == '__main__':
    main()
