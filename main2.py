#!/usr/bin/env python3

### Function and Class Definitions

    # These are valid keys:
    # 'i_antall_i_aar', Value: 16 782
    # 'm_sum_i_aar'
    # 'm_max_i_aar'
    # 'i_antall_i_fjor'
    # 'm_sum_i_fjor'
    # 'm_max_i_fjor'
    # 'n_prosent_sum'
    # 'n_prosent_antall'
    # 'i_antall'

### Standard library imports
import time


### Related third-party imports.
from buildhat import Motor, ForceSensor
# import schedule

### Local application/library specific imports
from api_profundo import get_profundo_key_value

### GLOBAL_CONSTANTS
motor = Motor('A')

class MotorController:
    def __init__(self, motor):
        self.motor = motor
        self.initial_position = motor.get_position()
        self.deviation = 0

    def move_motor_by_degrees(self, degrees):
        # Calculate target position considering the initial position and deviation
        target_position = self.initial_position + degrees + self.deviation

        # Run the motor
        run = self.deviation - degrees
        self.motor.run_for_degrees(run, 100)
        

        # Calculate actual position and update deviation
        actual_position = self.motor.get_position()
        self.deviation += (target_position - actual_position) - degrees

        print(target_position, actual_position, self.deviation, degrees, run)

    def get_current_deviation(self):
        return self.deviation

# Example usage
motor_controller = MotorController(motor)

for i in range(3):
    motor_controller.move_motor_by_degrees(500)
    time.sleep(1)
    i += 1

# MAX_RANGE_OF_MOTER = -11700
# start_position = motor.get_position()


# while True:
#     current_position = motor.get_position()
#     target_position = ( 300 - current_position ) * -1
#     degrees_to_adjust = target_position - start_position
    
#     # motor.run_for_degrees(degrees_to_adjust, 100)
    
#     print(current_position, target_position, start_position, degrees_to_adjust)


#     time.sleep(.5)



# def go_to(position=300):
#     current_position = motor.get_position()
#     target_position = position - current_position
#     degrees_to_adjust = current_position - target_position - start_position
    
#     motor.run_for_degrees(degrees_to_adjust, 100)
    
#     print(current_position, target_position, start_position, degrees_to_adjust)


#     time.sleep(.5)



# def go_to(target_position):

#     off_set = motor.get_position() - target_position
#     degrees_to_adjust = target_position - off_set
#     motor.run_for_degrees(degrees_to_adjust, 100)
#     print(target_position, degrees_to_adjust, off_set)

# go_to(0)

# for i in range(1, 10):
#     go_to(200)
#     time.sleep(.5)