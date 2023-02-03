import logging

from telegram import Update

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Add your questions and answers here

questions = {

    "what's your name?": "I am a chatbot created by OpenAI, so I don't have a name!",

    "what can you do?": "I can chat with you and answer some basic questions!",

    "what's your purpose?": "I was created to demonstrate how to build a chatbot with Telegram and OpenAI."

}

def start(update: Update, context):

    update.message.reply_text("Hello! This is a simple Q&A bot. Ask me a question and I'll do my best to answer it.")

def answer(update: Update, context):

    message = update.message.text.lower()

    for question in questions:

        if question.lower() == message:

            update.message.reply_text(questions[question])

            return

    update.message.reply_text("Sorry, I don't know the answer to that question. Please ask another question.")

def error(update: Update, context):

    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():

    # replace this with your own token

    token = "5648103386:AAGb2tlYazkxTI3OVJp5khtTFOq6DVWL8eU"  

    updater = Updater(token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.text, answer))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':

    main()

