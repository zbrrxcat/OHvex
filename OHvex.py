
#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# define vars

speed=75

# Robot configuration code
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)
controller_1 = Controller(PRIMARY)
motor_group_9_motor_a = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
motor_group_9_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
motor_group_9 = MotorGroup(motor_group_9_motor_a, motor_group_9_motor_b)
controller_1 = Controller(PRIMARY)

# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")



# define variables used for controlling motors based on controller inputs
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, remote_control_code_enabled, speed
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            
            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis3
            # right = axis2
            drivetrain_left_side_speed = controller_1.axis3.position()*(speed/100)
            drivetrain_right_side_speed = controller_1.axis2.position()*(speed/100)

            # check if the value is inside of the deadband range
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_needs_to_be_stopped_controller_1:
                    
                    # stop the left drive motor
                    left_drive_smart.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:

                # check if the right motor has already been stopped
                if drivetrain_r_needs_to_be_stopped_controller_1:

                    #quickstop
                    controller_1.screen.clear_screen()
                    controller_1.screen.set_cursor(1, 1)
                    controller_1.screen.print("qs")

                    if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                        # check if the left motor has already been stopped
                        #if drivetrain_l_needs_to_be_stopped_controller_1:

                        '''
                        left_drive_smart.set_velocity(speed * -1 , PERCENT)
                        left_drive_smart.spin(FORWARD)

                        right_drive_smart.set_velocity(speed * -1.25 , PERCENT)
                        right_drive_smart.spin(FORWARD)

                        wait(50, MSEC)

                        right_drive_smart.stop()
                        left_drive_smart.stop()

                        drivetrain_r_needs_to_be_stopped_controller_1 = False
                        drivetrain_l_needs_to_be_stopped_controller_1 = False

                        controller_1.screen.clear_screen()
                        controller_1.screen.set_cursor(1, 1)
                        controller_1.screen.print("1")
                        '''
                        drivetrain.set_stopping(HOLD)
                        right_drive_smart.stop()
                        left_drive_smart.stop()

                    # stop the right drive motor
                    right_drive_smart.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_needs_to_be_stopped_controller_1 = True
            
            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_l_needs_to_be_stopped_controller_1:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller_1:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)
                # wait before repeating the process
                wait(100, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

#endregion VEXcode Generated Robot Configuration
#reon VEXcode Generated Robot Configuration



# Brain should be defined by default
brain=Brain()


# Robot configuration code


# wait for rotation sensor to fully initialize
wait(30, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *
#UI code

# Function to run when the event occurs
def speedup():
    global speed
    speed += 5
    controller_1.screen.clear_screen()
    controller_1.screen.set_cursor(1, 1)
    controller_1.screen.print("speed: "+ str(speed))

# Function to run when the event occurs
def speedDown():
    global speed
    speed -= 5
    controller_1.screen.clear_screen()
    controller_1.screen.set_cursor(1, 1)
    controller_1.screen.print("speed: " + str(speed))

controller_1.buttonUp.pressed(speedup)
controller_1.buttonDown.pressed(speedDown)

def when_started1():
    global myVariable, is_extended
    is_extended = 1
    motor_group_9.set_position(0, DEGREES)

def onevent_controller_1buttonR1_pressed_0():
    global myVariable, is_extended
    is_extended = is_extended * -1
    if is_extended == -1:
        motor_group_9.spin_to_position(-135, DEGREES)
    else:
        motor_group_9.spin_to_position(0, DEGREES)

# system event handlers
controller_1.buttonR1.pressed(onevent_controller_1buttonR1_pressed_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()
# Begin project code
