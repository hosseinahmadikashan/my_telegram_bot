import telebot
from telebot import types 


TOKEN="8811643477:AAENFLbDZPOZvfZS59UuTYjjutpIy9lCxEY"
CHANNEL_ID="pooshaksartapa"
ADMIN_ID=7409762657

bot=telebot.TeleBot(TOKEN)

main_menu=types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False,row_width=2)
btn_products=types.KeyboardButton("product🛒") 
btn_tele=types.KeyboardButton("contact",request_contact=True) 
btn_contactUs=types.KeyboardButton("about us👩")
main_menu.add(btn_products,btn_contactUs,btn_tele)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(chat_id=message.chat.id,text="hoho",reply_markup=main_menu)

@bot.message_handler(content_types=["contact"])
def contact_message(message):
    contact=message.contact.phone_number
    bot.send_message(chat_id=message.chat.id,text="get phone")
    print("{contact}")

@bot.message_handler(func=lambda message:message.text=="product🛒")
def show_product(message):
    bot.send_message(message.chat.id,
                     "\n my product:"
                     "\n jorab"
                     "\n kafsh")

print("running....")
bot.infinity_polling()
    

    
