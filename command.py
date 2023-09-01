from telegram import Update
from telegram.ext import ContextTypes
from createMMD import *

img_path = r"X:\Vscode\TelegramBot\test.jpg"


# Command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi Im a temporary test bot. I can repeat any thing you send in chat."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi Nothing I can help you now :( ")


async def swear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("FucK You")


async def pic_commnad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await mmd_to_png("test", "si8a1.mmd")
    await update.message.reply_photo(photo=open("out.png", "rb"), caption="这是你要的图片！")
