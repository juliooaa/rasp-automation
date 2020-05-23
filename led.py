import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

import time, datetime # Creates a date from a timestamp

from flask import Flask # Import flask

from flask import request # Import request

from flask import abort # Import abort

from flask import jsonify # Import jsonify

import time # Import Time

now = datetime.datetime.now() # Create a timestamp

app = Flask('_name_') # Creates a Flask instance

GPIO.setwarnings(False) # Ignore warning for now

GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(5, GPIO.OUT) # Define pin 5 as output

GPIO.setup(40, GPIO.OUT) # Define pin 40 as output

pwm = GPIO.PWM(40, 100) # Configure PWM in pin 40 with 100Hz 

pwm.start(100) # Start DC = 100%

@app.route('/on', methods=['GET']) # Creates route /on

# View for route /on
def on():

	GPIO.output(5, True)
	return jsonify({'on':'done'}), 201

@app.route('/off', methods=['GET']) # Creates route /off

# View for route /off
def off():

        GPIO.output(5, False)
        return jsonify({'off':'done'}), 201

@app.route('/pwm', methods=['GET']) # Creates route /pwm

# View for route /pwm
def pwm():

	dc = 100
	while(dc != 0):
		pwm.ChangeDutyCycle(dc)
		time.sleep(0.05)
		dc = dc - 1
	return jsonify({'pwm':'off'})



app.run(debug=True)
