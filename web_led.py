#!/user/bin/env python
import RPi.GPIO as GPIO
import entitis
from sakshat import SAKSHAT 
from flask import Flask, render_template, request

app = Flask(__name__)
SAKS = SAKSHAT()

leds = {
    0 : {'name' : 'led0', 'state' : GPIO.LOW},
    1 : {'name' : 'led1', 'state' : GPIO.LOW},
    2 : {'name' : 'led2', 'state' : GPIO.LOW},
    3 : {'name' : 'led3', 'state' : GPIO.LOW},
    4 : {'name' : 'led4', 'state' : GPIO.LOW},
    5 : {'name' : 'led5', 'state' : GPIO.LOW},
    6 : {'name' : 'led6', 'state' : GPIO.LOW},
    7 : {'name' : 'led7', 'state' : GPIO.LOW}
}
@app.route("/")
def main():
    for i in range(0,8):
	leds[i]['state'] = SAKS.ledrow.is_on(i)
    templateData = {
            'leds' : leds
        }
    return render_template('main.html', **templateData)

@app.route("/<changeLed>/<action>")
def led_action(changeLed,action):
    ledx = int(changeLed)
    deviceName = leds[ledx]['name']
    if action == 'on':
        SAKS.ledrow.on_for_index(ledx)
        message = "turned"+deviceName+"on."
    if action == 'off':
        SAKS.ledrow.off_for_index(ledx)
        message = "turned"+deviceName+"off."
    for i in range(0,8):
        leds[i]['state'] = SAKS.ledrow.is_on(i)
    templateData = {
            'message' : message,
            'leds' : leds
        }
    return render_template('main.html', **templateData)

if __name__ == '__main__':
    SAKS.ledrow.on_for_index(2)    
    app.run(host='0.0.0.0', port = 80, debug=True)
