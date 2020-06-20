import telebot
import config
import random
import pdfkit

from urllib.parse import urlsplit
from telebot import types
from Screenshot import Screenshot_Clipping
from selenium import webdriver

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('images/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keybord
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Random")
    button2 = types.KeyboardButton("what's up")
    markup.add(button1, button2)

    bot.send_message(message.chat.id, "Hi, {0.first_name}!\nI - <b>{1.first_name}</b>, I was made to serve you, my lord.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_backe(message):
    if message.chat.type == 'private':
        if message.text == 'Random':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == "what's up":
            bot.send_message(message.chat.id, 'fine, and you?')
        else:
            par = urlsplit(message.text)
            if not par.scheme or not par.netloc:
                bot.send_message(message.chat.id, " Try sending me the URL")
            else:
                try:
                    chromedriver = 'C:/DRIVERS/chromedriver_win32/chromedriver.exe'

                    '''driver = webdriver.Chrome(executable_path=chromedriver)
                    driver.get_screenshot_as_file('Page.png')'''

                    #For Full Page ScreenShot :
                    '''ob = Screenshot_Clipping.Screenshot()
                    driver = webdriver.Chrome(executable_path=chromedriver)
                    driver.get(message.text)
                    img_url = ob.full_Screenshot(driver, save_path=r'.', image_name='Page.png')
                    print(img_url)
                    driver.close()
                    driver.quit()'''

                    #For Html Element Clipping :
                    '''ob = Screenshot_Clipping.Screenshot()
                    driver = webdriver.Chrome(executable_path=chromedriver)
                    driver.get(message.text)
                    element = driver.find_element_by_class_name('signup-prompt')
                    img_url = ob.get_element(driver, element, r'.')
                    print(img_url)
                    driver.close()
                    driver.quit()'''

                    #For Html Element Clipping with Hiding Element :
                    '''ob = Screenshot_Clipping.Screenshot()
                    driver = webdriver.Chrome(executable_path=chromedriver)
                    driver.get(message.text)
                    Hide_elements = [
                        'class=avatar width-full height-full avatar-before-user-status'] 
                    img_url = ob.full_Screenshot(driver, save_path=r'.', elements=Hide_elements,
                                                 image_name='Page.png')
                    print(img_url)
                    driver.close()
                    driver.quit()'''

                    '''page = open('Page.png', 'rb')
                    bot.send_document(message.chat.id, page)'''

                    #For Page in PDF
                    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
                    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
                    pdfkit.from_url(message.text, 'pdf1.pdf', configuration=config)
                    pdf = open('pdf1.pdf', 'rb')
                    bot.send_document(message.chat.id, pdf)
                except Exception as e:
                    print(repr(e))
                    bot.send_message(message.chat.id, e)

# RUN
bot.polling(none_stop=True)
