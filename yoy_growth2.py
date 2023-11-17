from buildhat import Motor
from time import sleep


motor_tower = Motor("A")
motor_gauge = Motor("B")

first_postion_gauge = motor_gauge.get_position() # Get position from motor, say -1000
first_position_tower = motor_tower.get_position()

def main():
    for i in range(1):
        show_on_gauge(90)
        show_on_gauge(-90)
        sleep(1)
        i += 1

def show_on_gauge(degrees):

    global first_postion_gauge
    one_degree = 2440 / 90    
    last_position = motor_gauge.get_position()
    target_degrees = first_postion_gauge - last_position - ( degrees * one_degree )
    motor_gauge.run_for_degrees(target_degrees, 40)

def show_on_tower(degrees):

    global first_position_tower
    one_degree = 2440 / 90    
    last_position = motor_gauge.get_position()
    target_degrees = first_position_tower - last_position - ( degrees * one_degree )
    motor_gauge.run_for_degrees(target_degrees, 40)


if __name__ == '__main__':
    main()