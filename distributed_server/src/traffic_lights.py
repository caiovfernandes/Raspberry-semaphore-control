import gpio
from time import sleep, time
from pedestrian_sensor import button_is_pressed_event
from utils import get_gpio_port_mapping, get_traffic_lights_states, get_traffic_lights_timers, get_traffic_lights_timers_debug


SLEEP_TIME = 2
SLEEP_TIME_DEBUG = 2
gpio_port_mapping = get_gpio_port_mapping()

def config_light_output():
    for crossing in gpio_port_mapping.values():
        for light in crossing.values():
            main = light['light2']
            aux = light['light1']
            gpio.gpio_setup_out(main)
            gpio.gpio_setup_out(aux)
            gpio.output_low(main)
            gpio.output_low(aux)

def init_traffic_control():
    traffic_lights_states = get_traffic_lights_states()
    traffic_lights_timers = get_traffic_lights_timers()
    timers =  {
        "green_main": traffic_lights_timers["green_maximum"]["main"],
        "green_aux": traffic_lights_timers["green_maximum"]["aux"],
        "yellow": traffic_lights_timers["yellow"]["main"],
        "red_main": traffic_lights_timers["red_maximum"]["main"],
        "red_aux": traffic_lights_timers["red_maximum"]["aux"]
    }
    reset_traffic_lights()
    button_is_pressed_event(pedestrian_button_was_pressed)



    gpio.output_high(gpio_port_mapping["cruzamento1"]["red"]['light2'])
    gpio.output_high(gpio_port_mapping["cruzamento2"]["red"]['light2'])

    gpio.output_high(gpio_port_mapping["cruzamento1"]["red"]['light1'])
    gpio.output_high(gpio_port_mapping["cruzamento2"]["red"]['light1'])
    
    while True:
        run_traffic_lights_main(timers)
        run_traffic_lights_aux(timers)


def pedestrian_button_was_pressed(channel):
    print("Button was pressed")
    if current_execution == "light2":
        if (time() -  main_start) >= timers[str(main_current_light) + "_aux"]:
            if main_current_light == "red":
                main_current_light = "green"
            elif main_current_light == "green":
                main_current_light = "yellow"
                print("Go to yellow main")
            elif main_current_light == "yellow":
                main_current_light = "red"
    if current_execution == "light1":
        if (time() -  aux_start) >= timers[str(aux_current_light) + "_aux"]:
            if aux_current_light == "red":
                aux_current_light = "green"
            elif aux_current_light == "green":
                aux_current_light = "yellow"
                print("Go to yellow aux")
            elif aux_current_light == "yellow":
                aux_current_light = "red"



def run_traffic_lights_main(timers):
    ## Main street traffic lights setup
    main_current_light = "red"
    current_execution = "light2"
    main_start = time()
    while 1:
        if(main_current_light == "red" and (time() -  main_start) >= timers["red_main"] ):
            gpio.output_low(gpio_port_mapping["cruzamento1"][main_current_light]['light2'])
            gpio.output_low(gpio_port_mapping["cruzamento2"][main_current_light]['light2'])
            main_current_light = "green"
            gpio.output_high(gpio_port_mapping["cruzamento1"][main_current_light]['light2'])
            gpio.output_high(gpio_port_mapping["cruzamento2"][main_current_light]['light2'])
            main_start = time()
            

        elif(main_current_light == "green" and (time() -  main_start) >= timers["green_main"] ):
            gpio.output_low(gpio_port_mapping["cruzamento1"][main_current_light]['light2'])
            gpio.output_low(gpio_port_mapping["cruzamento2"][main_current_light]['light2'])
            main_current_light = "yellow"
            gpio.output_high(gpio_port_mapping["cruzamento1"][main_current_light]['light2'])
            gpio.output_high(gpio_port_mapping["cruzamento2"][main_current_light]['light2'])
            main_start = time()

        elif(main_current_light == "yellow" and (time() -  main_start) >= timers["yellow"] ):
            gpio.output_low(gpio_port_mapping["cruzamento1"][main_current_light]['light2'])
            gpio.output_low(gpio_port_mapping["cruzamento2"][main_current_light]['light2'])
            main_current_light = "red"
            gpio.output_high(gpio_port_mapping["cruzamento1"][main_current_light]['light2'])
            gpio.output_high(gpio_port_mapping["cruzamento2"][main_current_light]['light2'])
            main_start = time()
            break
        
def run_traffic_lights_aux(timers):
    ## Auxiliar street traffic lights setup

    aux_current_light = "red"
    current_execution = "light1"
    aux_start = time()
    while 1:
        if(aux_current_light == "red" and (time() -  aux_start) >= timers["red_aux"] ):
            gpio.output_low(gpio_port_mapping["cruzamento1"][aux_current_light]['light1'])
            gpio.output_low(gpio_port_mapping["cruzamento2"][aux_current_light]['light1'])
            aux_current_light = "green"
            gpio.output_high(gpio_port_mapping["cruzamento1"][aux_current_light]['light1'])
            gpio.output_high(gpio_port_mapping["cruzamento2"][aux_current_light]['light1'])
            aux_start = time()

        elif(aux_current_light == "green" and (time() -  aux_start) >= timers["green_aux"] ):
            gpio.output_low(gpio_port_mapping["cruzamento1"][aux_current_light]['light1'])
            gpio.output_low(gpio_port_mapping["cruzamento2"][aux_current_light]['light1'])
            aux_current_light = "yellow"
            gpio.output_high(gpio_port_mapping["cruzamento1"][aux_current_light]['light1'])
            gpio.output_high(gpio_port_mapping["cruzamento2"][aux_current_light]['light1'])
            aux_start = time()

        elif(aux_current_light == "yellow" and (time() -  aux_start) >= timers["yellow"] ):
            gpio.output_low(gpio_port_mapping["cruzamento1"][aux_current_light]['light1'])
            gpio.output_low(gpio_port_mapping["cruzamento2"][aux_current_light]['light1'])
            aux_current_light = "red"
            gpio.output_high(gpio_port_mapping["cruzamento1"][aux_current_light]['light1'])
            gpio.output_high(gpio_port_mapping["cruzamento2"][aux_current_light]['light1'])
            aux_start = time()
            break




def reset_traffic_lights():
    gpio.output_low(gpio_port_mapping["cruzamento2"]['green']['light2'])
    gpio.output_low(gpio_port_mapping["cruzamento2"]['yellow']['light2'])
    gpio.output_low(gpio_port_mapping["cruzamento2"]['red']['light2'])
    gpio.output_low(gpio_port_mapping["cruzamento1"]['green']['light2'])
    gpio.output_low(gpio_port_mapping["cruzamento1"]['yellow']['light2'])
    gpio.output_low(gpio_port_mapping["cruzamento1"]['red']['light2'])
    gpio.output_low(gpio_port_mapping["cruzamento2"]['green']['light1'])
    gpio.output_low(gpio_port_mapping["cruzamento2"]['yellow']['light1'])
    gpio.output_low(gpio_port_mapping["cruzamento2"]['red']['light1'])
    gpio.output_low(gpio_port_mapping["cruzamento1"]['green']['light1'])
    gpio.output_low(gpio_port_mapping["cruzamento1"]['yellow']['light1'])
    gpio.output_low(gpio_port_mapping["cruzamento1"]['red']['light1'])



def debug_lights():
    button_is_pressed_event(callback = pedestrian_button_was_pressed_DEBUG)
    while 1:
        gpio.output_high(gpio_port_mapping["cruzamento2"]['green']['light2'])
        gpio.output_high(gpio_port_mapping["cruzamento2"]['yellow']['light2'])
        gpio.output_high(gpio_port_mapping["cruzamento2"]['red']['light2'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_high(gpio_port_mapping["cruzamento2"]['green']['light2'])
        gpio.output_high(gpio_port_mapping["cruzamento2"]['yellow']['light2'])
        gpio.output_high(gpio_port_mapping["cruzamento2"]['red']['light2'])

        gpio.output_high(gpio_port_mapping["cruzamento1"]['green']['light2'])
        gpio.output_high(gpio_port_mapping["cruzamento1"]['yellow']['light2'])
        gpio.output_high(gpio_port_mapping["cruzamento1"]['red']['light2'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_high(gpio_port_mapping["cruzamento1"]['green']['light2'])
        gpio.output_high(gpio_port_mapping["cruzamento1"]['yellow']['light2'])
        gpio.output_high(gpio_port_mapping["cruzamento1"]['red']['light2'])
        gpio.output_high(gpio_port_mapping["cruzamento2"]['green']['light1'])
        gpio.output_high(gpio_port_mapping["cruzamento2"]['yellow']['light1'])
        gpio.output_high(gpio_port_mapping["cruzamento2"]['red']['light1'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_high(gpio_port_mapping["cruzamento2"]['green']['light1'])
        gpio.output_high(gpio_port_mapping["cruzamento2"]['yellow']['light1'])
        gpio.output_high(gpio_port_mapping["cruzamento2"]['red']['light1'])

        gpio.output_high(gpio_port_mapping["cruzamento1"]['green']['light1'])
        gpio.output_high(gpio_port_mapping["cruzamento1"]['yellow']['light1'])
        gpio.output_high(gpio_port_mapping["cruzamento1"]['red']['light1'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_high(gpio_port_mapping["cruzamento1"]['green']['light1'])
        gpio.output_high(gpio_port_mapping["cruzamento1"]['yellow']['light1'])
        gpio.output_high(gpio_port_mapping["cruzamento1"]['red']['light1'])
    
    # gpio.output_high(gpio_port_mapping["cruzamento2"]['green']['light2'])
    # gpio.output_high(gpio_port_mapping["cruzamento2"]['yellow']['light2'])
    # gpio.output_high(gpio_port_mapping["cruzamento2"]['red']['light2'])
    # # sleep(SLEEP_TIME_DEBUG)
    # gpio.output_high(gpio_port_mapping["cruzamento2"]['green']['light1'])
    # gpio.output_high(gpio_port_mapping["cruzamento2"]['yellow']['light1'])
    # gpio.output_high(gpio_port_mapping["cruzamento2"]['red']['light1'])

    # gpio.output_high(gpio_port_mapping["cruzamento1"]['green']['light2'])
    # gpio.output_high(gpio_port_mapping["cruzamento1"]['yellow']['light2'])
    # gpio.output_high(gpio_port_mapping["cruzamento1"]['red']['light2'])
    # # sleep(SLEEP_TIME_DEBUG)
    # gpio.output_high(gpio_port_mapping["cruzamento1"]['green']['light1'])
    # gpio.output_high(gpio_port_mapping["cruzamento1"]['yellow']['light1'])
    # gpio.output_high(gpio_port_mapping["cruzamento1"]['red']['light1'])
    while 1:
        pass



def pedestrian_button_was_pressed_DEBUG(channel):
    while 1:
        gpio.output_low(gpio_port_mapping["cruzamento2"]['green']['light2'])
        gpio.output_low(gpio_port_mapping["cruzamento2"]['yellow']['light2'])
        gpio.output_low(gpio_port_mapping["cruzamento2"]['red']['light2'])
        gpio.output_low(gpio_port_mapping["cruzamento1"]['green']['light2'])
        gpio.output_low(gpio_port_mapping["cruzamento1"]['yellow']['light2'])
        gpio.output_low(gpio_port_mapping["cruzamento1"]['red']['light2'])
        gpio.output_low(gpio_port_mapping["cruzamento2"]['green']['light1'])
        gpio.output_low(gpio_port_mapping["cruzamento2"]['yellow']['light1'])
        gpio.output_low(gpio_port_mapping["cruzamento2"]['red']['light1'])
        gpio.output_low(gpio_port_mapping["cruzamento1"]['green']['light1'])
        gpio.output_low(gpio_port_mapping["cruzamento1"]['yellow']['light1'])
        gpio.output_low(gpio_port_mapping["cruzamento1"]['red']['light1'])
    # gpio.output_low(gpio_port_mapping["cruzamento2"]['green']['light2'])
    # gpio.output_low(gpio_port_mapping["cruzamento2"]['yellow']['light2'])
    # gpio.output_low(gpio_port_mapping["cruzamento2"]['red']['light2'])
    # gpio.output_low(gpio_port_mapping["cruzamento1"]['green']['light2'])
    # gpio.output_low(gpio_port_mapping["cruzamento1"]['yellow']['light2'])
    # gpio.output_low(gpio_port_mapping["cruzamento1"]['red']['light2'])
    # gpio.output_low(gpio_port_mapping["cruzamento2"]['green']['light1'])
    # gpio.output_low(gpio_port_mapping["cruzamento2"]['yellow']['light1'])
    # gpio.output_low(gpio_port_mapping["cruzamento2"]['red']['light1'])
    # gpio.output_low(gpio_port_mapping["cruzamento1"]['green']['light1'])
    # gpio.output_low(gpio_port_mapping["cruzamento1"]['yellow']['light1'])
    # gpio.output_low(gpio_port_mapping["cruzamento1"]['red']['light1'])


def activate_nocturnal_mode():
    reset_traffic_lights()
    while 1:
        gpio.output_high(gpio_port_mapping["cruzamento2"]['yellow']['light2'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_high(gpio_port_mapping["cruzamento2"]['yellow']['light2'])

        gpio.output_high(gpio_port_mapping["cruzamento1"]['yellow']['light2'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_high(gpio_port_mapping["cruzamento1"]['yellow']['light2'])
        gpio.output_high(gpio_port_mapping["cruzamento2"]['yellow']['light1'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_high(gpio_port_mapping["cruzamento2"]['yellow']['light1'])

        gpio.output_high(gpio_port_mapping["cruzamento1"]['yellow']['light1'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_high(gpio_port_mapping["cruzamento1"]['yellow']['light1'])
        sleep(1)
        gpio.output_low(gpio_port_mapping["cruzamento2"]['yellow']['light2'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_low(gpio_port_mapping["cruzamento2"]['yellow']['light2'])

        gpio.output_low(gpio_port_mapping["cruzamento1"]['yellow']['light2'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_low(gpio_port_mapping["cruzamento1"]['yellow']['light2'])
        gpio.output_low(gpio_port_mapping["cruzamento2"]['yellow']['light1'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_low(gpio_port_mapping["cruzamento2"]['yellow']['light1'])

        gpio.output_low(gpio_port_mapping["cruzamento1"]['yellow']['light1'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_low(gpio_port_mapping["cruzamento1"]['yellow']['light1'])
        sleep(1)


def activate_emergency_mode():
    reset_traffic_lights()
    while 1:
        gpio.output_high(gpio_port_mapping["cruzamento2"]['green']['light2'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_high(gpio_port_mapping["cruzamento2"]['green']['light2'])

        gpio.output_high(gpio_port_mapping["cruzamento1"]['green']['light2'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_high(gpio_port_mapping["cruzamento1"]['green']['light2'])

        gpio.output_high(gpio_port_mapping["cruzamento2"]['red']['light1'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_high(gpio_port_mapping["cruzamento2"]['red']['light1'])

        gpio.output_high(gpio_port_mapping["cruzamento1"]['red']['light1'])
        # sleep(SLEEP_TIME_DEBUG)
        gpio.output_high(gpio_port_mapping["cruzamento1"]['red']['light1'])

