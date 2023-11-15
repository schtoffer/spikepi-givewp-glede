#!/usr/bin/env python3

### Standard library imports


### Related third-party imports.
from buildhat import Motor, ForceSensor
# import schedule

### Local application/library specific imports
from api_profundo import get_profundo_key_value

### GLOBAL_CONSTANTS
motor = Motor('A')

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

def main():
    
    
    motor.run_for_degrees(get_profundo_key_value('n_prosent_antall'))




if __name__ == '__main__':
    main()
