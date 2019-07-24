import time
import RPi.GPIO as GPIO


class FIDOMove:
    def __init__(self):
        self.Motor_A_EN = 7
        self.Motor_B_EN = 11

        self.Motor_A_Pin1 = 8
        self.Motor_A_Pin2 = 10
        self.Motor_B_Pin1 = 13
        self.Motor_B_Pin2 = 12

        self.Dir_forward = 0
        self.Dir_backward = 1

        self.left_forward = 1
        self.left_backward = 0

        self.right_forward = 0
        self.right_backward = 1

        self.pwn_A = 0
        self.pwm_B = 0

    def motorStop(self):  # Motor stops
        GPIO.output(self.Motor_A_Pin1, GPIO.LOW)
        GPIO.output(self.Motor_A_Pin2, GPIO.LOW)
        GPIO.output(self.Motor_B_Pin1, GPIO.LOW)
        GPIO.output(self.Motor_B_Pin2, GPIO.LOW)
        GPIO.output(self.Motor_A_EN, GPIO.LOW)
        GPIO.output(self.Motor_B_EN, GPIO.LOW)

    def setup(self):  # Motor initialization
        global pwm_A, pwm_B
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.Motor_A_EN, GPIO.OUT)
        GPIO.setup(self.Motor_B_EN, GPIO.OUT)
        GPIO.setup(self.Motor_A_Pin1, GPIO.OUT)
        GPIO.setup(self.Motor_A_Pin2, GPIO.OUT)
        GPIO.setup(self.Motor_B_Pin1, GPIO.OUT)
        GPIO.setup(self.Motor_B_Pin2, GPIO.OUT)

        self.motorStop()
        try:
            pwm_A = GPIO.PWM(self.Motor_A_EN, 1000)
            pwm_B = GPIO.PWM(self.Motor_B_EN, 1000)
        except:
            pass

    def motor_left(self, status, direction, speed):  # Motor 2 positive and negative rotation
        if status == 0:  # stop
            GPIO.output(self.Motor_B_Pin1, GPIO.LOW)
            GPIO.output(self.Motor_B_Pin2, GPIO.LOW)
            GPIO.output(self.Motor_B_EN, GPIO.LOW)
        else:
            if direction == self.Dir_backward:
                GPIO.output(self.Motor_B_Pin1, GPIO.HIGH)
                GPIO.output(self.Motor_B_Pin2, GPIO.LOW)
                pwm_B.start(100)
                pwm_B.ChangeDutyCycle(speed)
            elif direction == self.Dir_forward:
                GPIO.output(self.Motor_B_Pin1, GPIO.LOW)
                GPIO.output(self.Motor_B_Pin2, GPIO.HIGH)
                pwm_B.start(0)
                pwm_B.ChangeDutyCycle(speed)

    def motor_right(self, status, direction, speed):  # Motor 1 positive and negative rotation
        if status == 0:  # stop
            GPIO.output(self.Motor_A_Pin1, GPIO.LOW)
            GPIO.output(self.Motor_A_Pin2, GPIO.LOW)
            GPIO.output(self.Motor_A_EN, GPIO.LOW)
        else:
            if direction == self.Dir_forward:  #
                GPIO.output(self.Motor_A_Pin1, GPIO.HIGH)
                GPIO.output(self.Motor_A_Pin2, GPIO.LOW)
                pwm_A.start(100)
                pwm_A.ChangeDutyCycle(speed)
            elif direction == self.Dir_backward:
                GPIO.output(self.Motor_A_Pin1, GPIO.LOW)
                GPIO.output(self.Motor_A_Pin2, GPIO.HIGH)
                pwm_A.start(0)
                pwm_A.ChangeDutyCycle(speed)
        return direction

    def move(self, direction, turn, radius=0.6):  # 0 < radius <= 1
        speed = 100
        if direction == 'forward':
            if turn == 'left':
                self.motor_left(0, self.left_backward, int(speed * radius))
                self.motor_right(1, self.right_forward, speed)
            elif turn == 'right':
                self.motor_left(1, self.left_forward, speed)
                self.motor_right(0, self.right_backward, int(speed * radius))
            else:
                self.motor_left(1, self.left_forward, 100)
                self.motor_right(1, self.right_forward, 100)
        elif direction == 'backward':
            if turn == 'left':
                self.motor_left(0, self.left_forward, int(speed * radius))
                self.motor_right(1, self.right_backward, speed)
            elif turn == 'right':
                self.motor_left(1, self.left_backward, speed)
                self.motor_right(0, self.right_forward, int(speed * radius))
            else:
                self.motor_left(1, self.left_backward, speed)
                self.motor_right(1, self.right_backward, speed)
        elif direction == 'no':
            if turn == 'left':
                self.motor_left(1, self.left_backward, 100)
                self.motor_right(1, self.right_forward, 100)
            elif turn == 'right':
                self.motor_left(1, self.left_forward, 100)
                self.motor_right(1, self.right_backward, 100)
            else:
                self.motorStop()
        else:
            pass

    def destroy(self):
        self.motorStop()
        GPIO.cleanup()  # Release resource
