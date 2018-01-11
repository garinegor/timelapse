from time import sleep
from picamera import PiCamera
import config,telebot
from telebot import types

bot = telebot.TeleBot(config.token)

camera = PiCamera()
camera.vflip = True
camera.hflip = True

@bot.message_handler(commands=["start"])
def start(message):
	camera.capture('./test.jpg')
	bot.send_photo(chat_id=202226598, photo=open('./test.jpg', 'rb'))
@bot.message_handler(commands=["photo"])
def start(message):
	for i in range(3000):
		camera.capture('./photos/'+i+'.jpg')
		bot.send_photo(chat_id=202226598, photo=open('./photos/'+i+'.jpg', 'rb'))
		sleep(20)