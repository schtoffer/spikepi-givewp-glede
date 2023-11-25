from buildhat import Motor, ForceSensor
from buildhat.exc import BuildHATError
import time

motor_tower = Motor("A")
# motor_gauge = Motor("B")

sales_goal = 58200000

# first_postion_gauge = motor_gauge.get_position()
first_position_tower = motor_tower.get_position()

def main():
    show_on_tower(19)

# def show_on_gauge(degrees):

#     global first_postion_gauge
#     one_degree = 2440 / 30    
#     last_position = motor_gauge.get_position()
#     target_degrees = first_postion_gauge - last_position - ( degrees * one_degree )
#     motor_gauge.run_for_degrees(target_degrees, 25)

def show_on_tower(per_cent):

    global sales_goal
    global first_position_tower
    
    one_per_cent = 8500 / 100 # 11700 to the very top of the tower
    last_position = motor_tower.get_position()
    target_degrees = first_position_tower - last_position - ( per_cent * one_per_cent )
    motor_tower.run_for_degrees(target_degrees, 35)

def initialize_sensor(port, attempts=5, delay=5):
    while attempts > 0:
        try:
            sensor = ForceSensor(port)
            return sensor
        except BuildHATError:
            attempts -= 1
            time.sleep(delay)  # Wait for 5 seconds before retrying
    raise  # Re-raise the last exception after all attempts fail

# def initialize_motor(port, attempts=5, delay=5):
#     while attempts > 0:
#         try:
#             motor = Motor(port)
#             return motor
#         except BuildHATError:
#             attempts -= 1
#             time.sleep(delay)  # Wait for 5 seconds before retrying
#     raise  # Re-raise the last exception after all attempts fail

if __name__ == '__main__':
    main()
