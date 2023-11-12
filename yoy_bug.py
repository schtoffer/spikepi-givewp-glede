from buildhat import Motor
from time import sleep

api_result = [0, -30]
motor = Motor("B")
start_position = motor.get_position()

def main():
    pass

    # for i in range(50):
    #     for i in range(len(api_result)):
    #         show_on_dial(api_result[i])
    #         i += 1
    #         sleep(1)
 
def show_on_dial(degrees):
    one_degree = 800 / 30 * -1
    last_position = motor.get_position() - start_position
    motor.run_for_degrees(degrees * one_degree - last_position, 20)
    print(f"last_position: {last_position} degrees_to_turn: {(degrees * one_degree - last_position)}")

if __name__ == '__main__':
    main()