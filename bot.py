from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
from downloader import download_video


TOKEN = "[Credentials]"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Envie o link do vídeo da Shopee 📥"
    )


async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    msg = await update.message.reply_text("Baixando vídeo... ⏳")


    try:
        video_path = download_video(url)
        await update.message.reply_video(video=open(video_path, "rb"))
    except Exception as e:
        await update.message.reply_text("Erro ao baixar o vídeo ❌")


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
app.run_polling()

