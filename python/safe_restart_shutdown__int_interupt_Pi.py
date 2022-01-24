# safe_restart_shutdown_interrupt_Pi.py
#
# Raspberry Pi Safe Restart and Shutdown Python Script
# WRITTEN BY: Matthew Miller @ CHS
# MODIFIED: 11/30/2021
# DESCRIPTION: This python script uses a button to safely
# reboot/shutdown your RPi. A momentary press reboots the pi,
# holding the button shuts the RPi down. 
#
# Based on code from the following tutorial:
#https://learn.sparkfun.com/tutorials/
#raspberry-pi-safe-reboot-and-shutdown-button/all
#-------------------------------------------------
import time
import RPi.GPIO as GPIO 
# Pin definition
reset_shutdown_pin = 26
# Suppress warnings
GPIO.setwarnings(False)
# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)
# Use built-in pullup resistor so the pin is not floating
GPIO.setup(reset_shutdown_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# modular function to restart Pi
def restart():
    print("restarting Pi")
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)
# modular function to shutdown Pi
def shut_down():
    print("shutting down")
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)
while True:
    #short delay, to reduce computational requirements
    time.sleep(0.5)
    # wait for a button press with switch debounce
    channel = GPIO.wait_for_edge(reset_shutdown_pin, GPIO.FALLING, bouncetime=200)
    if channel is None:
        print('Timeout occurred')
    else:
        print('Edge detected on channel', channel)
        # For troubleshooting, uncomment this line
        #print('GPIO state is = ', GPIO.input(reset_shutdown_pin))
        counter = 0
        while GPIO.input(reset_shutdown_pin) == False:
            # For troubleshooting, uncomment this line to view the counter
            #print(counter)
            counter += 1
            time.sleep(0.5)
            # long button press
            if counter > 4:
                shut_down()
        #if short button press, restart!
        restart()
