import validators
import os ,re , requests
from os import environ
from telegram.ext import *

API_KEY = environ['API_KEY']
print("Bot Started....")
def userinfo(update,context):
    messager_id = update.message.chat.id
    messager_Fname = update.message.chat.first_name
    messager_Lname = update.message.chat.last_name
    messager_Username = update.message.chat.username
    info = """
          _______________________________________
          id = {}
          First Name = {}
          Last Name = {}
          UserName = {}
          _______________________________________
          """.format(messager_id,messager_Fname,messager_Lname,messager_Username)
    return info
def start_command(update,context):
    update.message.reply_text(' Hello {}\n, Send Facebook Video Link to start Downloading !'.format(update.message.chat.first_name))
def help_command(update,context):
    update.message.reply_text('This Bot can Bring you Download Link for facebook Video \n ,if url was given ')
def suggestions_command(update,context):
    userinfo(update,context)

def error_Functiuon(update,context):
    print("update {} caused error {}".format(update,context.error))


def message_handler(update,context):
    message_text = update.message.text
    print('-' * 30)
    print(userinfo(update,context))
    print(message_text)
    print('-' * 30)
    isvalid = validators.url(message_text.strip())
    if isvalid == True:
        req = requests.get(message_text.strip()).text
        sd_video_Link = re.search('sd_src:"(.+?)"',req)
        update.message.reply_text(sd_video_Link)
    else:
        update.message.reply_text('Link is not Valid or the requested video is private !')
    

        
def main():
    Bot_updater = Updater(API_KEY,use_context=True)
    Bot_dispatcher = Bot_updater.dispatcher
    Bot_dispatcher.add_handler(CommandHandler('start',start_command))
    Bot_dispatcher.add_handler(CommandHandler('help',help_command))
    Bot_dispatcher.add_handler(CommandHandler('userinfo',suggestions_command))
    Bot_dispatcher.add_handler(MessageHandler(Filters.text,message_handler))
    Bot_dispatcher.add_error_handler(error_Functiuon)
    Bot_updater.start_polling()
    Bot_updater.idle()
main()
