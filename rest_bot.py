from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Welcome to the restaurant bot, {user.first_name}!"
    )

# Handler for regular messages
def echo(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm sorry, I can only respond to commands."
    )

# Handler for the /menu command
def menu(update: Update, context: CallbackContext) -> None:
    menu_text = "Today's Menu:\n- Pizza\n- Pasta\n- Salad\n- Dessert"
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=menu_text
    )

# Handler for the /reservation command
def reservation(update: Update, context: CallbackContext) -> None:
    # Logic for making a reservation
    # You can prompt the user for input using context.bot.send_message()
    # and retrieve the user's response from update.message.text

# Main function to run the bot
def main() -> None:
    # Set up the updater and dispatcher
    updater = Updater("5788817056:AAHnRe7odeTipRRm7B0e7eKdZd0LwTNMoEE")
    dispatcher = updater.dispatcher

    # Set up the command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("menu", menu))
    dispatcher.add_handler(CommandHandler("reservation", reservation))

    # Set up the message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
