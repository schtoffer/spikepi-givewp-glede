from buildhat import Motor
from time import sleep

api_result = [0]
motor = Motor("B")

one_degree = 800 / 30 * -1

def main():
    last_position = motor.get_position()
    print(last_position)
    sleep(1)

    for i in range(len(api_result)):
        show_on_dial(api_result[i])
        
        print(f"api result: {api_result[i]} last_position:{last_position} run_to: {api_result[i] - last_position * -1}")
        print(print(one_degree * i))
        sleep(2)
        i += 1
 

def show_on_dial(degrees):
    last_position = motor.get_position()
    motor.run_for_degrees(one_degree * degrees - last_position, 100)
    print(one_degree * degrees)



if __name__ == '__main__':
    main()