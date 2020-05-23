
import time, datetime

import RPi.GPIO as GPIO

import telepot

from telepot.loop import MessageLoop



chat_id = 0

led = 5

button = 10

light = 40

now = datetime.datetime.now()

GPIO.setmode (GPIO.BOARD)

GPIO.setwarnings(False)

 #LED

GPIO.setup(led, GPIO.OUT)

GPIO.output(led, 0) #Off initially

 #Button

def button_callback(channel):

    global chat_id

    message_button = "Sua campanhia ta tocando"

    telegram_bot.sendMessage (chat_id, message_button)



GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(button, GPIO.RISING, callback=button_callback)

 #Light

GPIO.setup(light, GPIO.OUT)

pwm = GPIO.PWM(light, 100)

pwm.start(100)


def action(msg):

    global  chat_id

    chat_id = msg['chat']['id'] 

    command = msg['text']

    dc = 100

    print 'Received: %s' % command

    if 'on' in command:

        message = "Turned on "

        if 'led' in command:

            message = message + "led"

            GPIO.output(led, 1)

            telegram_bot.sendMessage (chat_id, message)



    if 'off' in command:

        message = "Turned off "

        if 'led' in command:

            message = message + "led "

            GPIO.output(led, 0)

            telegram_bot.sendMessage (chat_id, message)

    if 'luz' in command:

        message = "teste"

        telegram_bot.sendMessage (chat_id, message)

        while(dc != 0):

	    pwm.ChangeDutyCycle(dc)
	    time.sleep(0.05)
	    dc = dc - 1


telegram_bot = telepot.Bot('1179446601:AAE_hah4h3dANL0Vr0LNEWylik2DShKU8tA')

print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()

print 'Up and Running....'



while 1:

   time.sleep(10) 
