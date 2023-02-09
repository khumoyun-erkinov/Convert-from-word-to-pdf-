import os
import telegram
from telegram.ext import Updater, MessageHandler, Filters
from docx import Document
TOKEN = "5633752095:AAGhkBTQzi7VCnaHfXlyp6b7G23iLkfqpCc"

def convert_to_pdf(word_file):
    # Open the Word file using python-docx
    document = Document(word_file)

    # Save the document as a PDF
    pdf_file = word_file.replace('.docx', '.pdf')
    document.save(pdf_file)

    return pdf_file

def handle_word_file(bot, update, **kwargs):
    # Get the file ID
    file_id = update.message.document.file_id

    # Get the file from Telegram
    newFile = bot.get_file(file_id)
    newFile.download('word_file.docx')

    # Convert the Word file to PDF
    pdf_file = convert_to_pdf('word_file.docx')

    # Send the PDF file back to the user
    with open(pdf_file, 'rb') as f:
        bot.send_document(chat_id=update.message.chat_id, document=f)

def main():
    # Get the Telegram Bot API token
    token = os.environ.get(TOKEN)

    # Create the Telegram Bot
    bot = telegram.Bot(token)

    # Create the Updater
    updater = Updater(token)

    # Get the dispatcher
    dp = updater.dispatcher

    # Add the message handler
    dp.add_handler(MessageHandler(Filters.document, handle_word_file))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
