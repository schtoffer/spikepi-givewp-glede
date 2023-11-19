import time
from buildhat import ForceSensor, Motor

# def initialize_sensor(port, attempts=5, delay=5):
#     while attempts > 0:
#         try:
#             sensor = ForceSensor(port)
#             return sensor
#         except buildhat.exc.BuildHATError:
#             attempts -= 1
#             time.sleep(delay)  # Wait for 5 seconds before retrying
#     raise  # Re-raise the last exception after all attempts fail

def initialize_spike_module(type, port, attempts=5, delay=5):
    while attempts > 0:
        try:
            module = type(port)
            return module
        except buildhat.exc.BuildHATError:
            attempts -= 1
            time.sleep(delay)  # Wait for 5 seconds before retrying
    raise  # Re-raise the last exception after all attempts fail

button_left = initialize_spike_module(ForceSensor, 'C')
print(button_left)

while True:
        
    if button_left.is_pressed():
        print('Hei')
        break