# CamJam EduKit 3 - Robotics
# Worksheet 9 – Obstacle Avoidance

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7
# Define GPIO pins for the ultrasound to use on the Pi
# We will use two ultrasound modules to determine proximity
pinLeftTrigger = 17
pinLeftEcho = 18
pinRightTrigger = ############### need to set this value
pinRightEcho = ################## need to set this value

# Define GPIO pins for the LEDs and buzzer
########################################################
########################################################
############### Need to set these values ###############
########################################################
########################################################
pinLeftLED =
pinRightLED =
pinFrontLED =
pinBackLED =
pinBuzzer = 

# How many times to turn the pin on and off each second
Frequency = 20
# How long the pin stays on each cycle, as a percent
DutyCycleA = 33
DutyCycleB = 32
# Settng the duty cycle to 0 means the motors will not turn
Stop = 0

# Set the GPIO Pin mode to be Output for the motors
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Set pins as output and input for the ultrasonic sensor
GPIO.setup(pinTrigger, GPIO.OUT)  # Trigger
GPIO.setup(pinEcho, GPIO.IN)      # Echo

# Set up the pins as output for the LEDs and Buzzer
GPIO.setup(pinLeftLED, GPIO.OUT)
GPIO.setup(pinRightLED, GPIO.OUT)
GPIO.setup(pinFrontLED, GPIO.OUT)
GPIO.setup(pinBackLED, GPIO.OUT)
GPIO.setup(pinBuzzer, GPIO.OUT)
# Distance Variables
HowNear = 25.0
ReverseTime = 0.75
TurnTime = 0.3

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

# Turn all motors off
def StopMotors():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
    GPIO.output(pinLeftLED, GPIO.LOW)
    GPIO.output(pinRightLED, GPIO.LOW)
    GPIO.output(pinFrontLED, GPIO.LOW)
    GPIO.output(pinBackLED, GPIO.HIGH)
    GPIO.output(pinBuzzer, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pinBackLED, GPIO.LOW)

# Turn both motors forwards
def Forwards():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
    GPIO.output(pinLeftLED, GPIO.LOW)
    GPIO.output(pinRightLED, GPIO.LOW)
    GPIO.output(pinFrontLED, GPIO.HIGH)
    GPIO.output(pinBackLED, GPIO.LOW)
    GPIO.output(pinBuzzer, GPIO.LOW)

# Turn both motors backwards
def Backwards():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
    GPIO.output(pinLeftLED, GPIO.LOW)
    GPIO.output(pinRightLED, GPIO.LOW)
    GPIO.output(pinFrontLED, GPIO.LOW)
    GPIO.output(pinBackLED, GPIO.HIGH)
    GPIO.output(pinBuzzer, GPIO.HIGH)
                
# Turn left
def Left():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
    GPIO.output(pinLeftLED, GPIO.LOW)
    GPIO.output(pinRightLED, GPIO.LOW)
    GPIO.output(pinFrontLED, GPIO.LOW)
    GPIO.output(pinBackLED, GPIO.LOW)
    GPIO.output(pinBuzzer, GPIO.LOW)
    For i =(0,3):
        GPIO.output(pinLeftLED, GPIO.HIGH)
        sleep(ReverseTime/6)
        GPIO.output(pinLeftLED, GPIO.LOW)
        sleep(ReverseTime/6)
        i +=1

# Turn Right
def Right():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
    GPIO.output(pinLeftLED, GPIO.LOW)
    GPIO.output(pinRightLED, GPIO.LOW)
    GPIO.output(pinFrontLED, GPIO.LOW)
    GPIO.output(pinBackLED, GPIO.LOW)
    GPIO.output(pinBuzzer, GPIO.LOW)
    For i =(0,3):
        GPIO.output(pinRightLED, GPIO.HIGH)
        sleep(ReverseTime/6)
        GPIO.output(pinRightLED, GPIO.LOW)
        sleep(ReverseTime/6)
        i +=1
        
# Take distance measurements
def Measure():
    GPIO.output(pinLeftTrigger, True)
    GPIO.output(pinRightTrigger, True)
    time.sleep(0.00001)
    GPIO.output(pinLeftTrigger, False)
    GPIO.output(pinRightTrigger, False)
    LeftStartTime = time.time()
    LeftStopTime = StartTime
    RightStopTime = LeftStopTime

    while GPIO.input(pinLeftEcho)==0:
        LeftStartTime = time.time()
        LeftStopTime = LeftStartTime

    while GPIO.input(pinLeftEcho)==1:
        StopTime = time.time()
        # If the sensor is too close to an object, the Pi cannot
        # see the echo quickly enough, so we have to detect that
        # problem and say what has happened.
        if StopTime-StartTime >= 0.04:
            print("Hold on there!  You're too close for me to see.")
            StopTime = StartTime
            break

    ElapsedTime = StopTime - StartTime
    Distance = (ElapsedTime * 34300)/2

    return Distance

# Return True if the ultrasonic sensor sees an obstacle
def IsNearObstacle(localHowNear):
    Distance = Measure()

    print("IsNearObstacle: "+str(Distance))
    if Distance < localHowNear:
        return True
    else:
        return False

# Move back a little, then turn right
def AvoidObstacle():
    # Back off a little
    print("Backwards")
    Backwards()
    time.sleep(ReverseTime)
    StopMotors()

    # Turn right
    print("Checking distance of obstacle to the right")
    Right()
    time.sleep(TurnTime)
    StopMotors()
    RightDistance = Measure()
    print("Obstacle to right in:",RightDistance,"cm")

    #Turn left (twice right)
    print("Checking distance of obstacle to the left")
    Left()
    time.sleep(2*TurnTime)
    StopMotors()
    LeftDistance = Measure()
    print("Obstacle to left in:",LeftDistance,"cm")

    if LeftDistance > RightDistance:
        print("Going Left")
    else:
        print("Going Right")
        Right()
        time.sleep(2*TurnTime)
        StopMotors()

# Your code to control the robot goes below this line
try:
    # Set trigger to False (Low)
    GPIO.output(pinTrigger, False)

    # Allow module to settle
    time.sleep(0.1)

    #repeat the next indented block forever
    while True:
        Forwards()
        time.sleep(0.1)
        if IsNearObstacle(HowNear):
            StopMotors()
            AvoidObstacle()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    GPIO.cleanup()
