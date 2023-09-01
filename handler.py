from telegram import Update
from telegram.ext import Updater, filters, ContextTypes
from createMMD import *
from analyzeTx import get_tx_info
import os


async def tx_to_graph(tx_id: str):
    print(f"transfer tx {tx_id} to graph...")
    try:
        tx_info: any = get_tx_info(tx_id)
        if tx_info is not None:
            mermaid_code = generate_mmd(*tx_info)
            await mmd_to_png(mermaid_code)
        else:
            print("the tx is not valid here!")
    except Exception as e:
        print(f"can't generate mermaid code from tx_id")


# Response
async def handle_response(tx_id: str):
    print("handle response...")
    await tx_to_graph(tx_id)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tx_id: str = update.message.text

    await handle_response(tx_id)
    if os.path.exists("out.png"):
        await update.message.reply_photo(
            photo=open("out.png", "rb"), caption="Graph generated !!"
        )
    else:
        await update.message.reply_text("out.png does not exist.")
    # await update.message.reply_text(response)


# Error
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update{update} caused error {context.error}")
