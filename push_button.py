import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

import time, datetime 

import telepot # Communicate with Telegram API

from telepot.loop import MessageLoop

chat_id = 0

button = 10

now = datetime.datetime.now()

GPIO.setmode (GPIO.BOARD) # Use physical pin numbering

GPIO.setwarnings(False) # Ignore warning for now


GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(button,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

# Send a message when button is click
def button_callback(channel):

    global chat_id

    message_button = "Sua campanhia ta tocando"

    telegram_bot.sendMessage (chat_id, message_button)

# Get the chat_id
def action(msg):

    global  chat_id

    chat_id = msg['chat']['id']
    
GPIO.cleanup() # Clean up
