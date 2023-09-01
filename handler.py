from telegram import Update
from telegram.ext import Updater, filters, ContextTypes
from createMMD import *
from analyzeTx import get_tx_info


def tx_to_graph(tx_id: str):
    print(f"tx {tx_id} to graph...")
    mermaid_code = generate_mmd(*get_tx_info(tx_id))
    mmd_to_png(mermaid_code)


# Response
def handle_response(tx_id: str):
    print("handle response...")
    tx_to_graph(tx_id)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text

    response: str = handle_response(text)
    await update.message.reply_photo(
        photo=open("out.png", "rb"), caption="Graph generated !!"
    )
    # await update.message.reply_text(response)


# Error
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update{update} caused error {context.error}")
