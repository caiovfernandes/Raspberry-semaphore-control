
def get_gpio_port_mapping():

    gpio_port_mapping = {
        "cruzamento1": 
            {
                'green': {
                    'light2': 20,
                    'light1': 1,
                },
                'yellow': {
                    'light2': 16,
                    'light1': 26,
                },
                'red': {
                    'light2': 12,
                    'light1': 21,
                },
            },
        "cruzamento2":
            {
                'green': {
                    'light2': 0,
                    'light1': 2,
                },
                'yellow': {
                    'light2': 5,
                    'light1': 3,
                },
                'red': {
                    'light2': 6,
                    'light1': 11,
                }
            }
    }   
    return gpio_port_mapping


def get_traffic_lights_timers():
    traffic_lights_timers = {
        "green_minimum": {
            "main": 10,
            "aux": 5
        },
        "green_maximum": {
            "main": 20,
            "aux": 10
        },
        "yellow": {
            "main": 3,
            "aux": 3
        },
        "red_minimum": {
            "main": 5,
            "aux": 10
        },
        "red_maximum": {
            "main": 10,
            "aux": 20
        },
        "red_total": {
            "main": 1,
            "aux": 1
        }
    }
    return traffic_lights_timers

def get_traffic_lights_timers_debug():
    traffic_lights_timers = {
        "green_minimum": {
            "main": 5,
            "aux": 2.5
        },
        "green_maximum": {
            "main": 10,
            "aux": 5
        },
        "yellow": {
            "main": 1.5,
            "aux": 1.5
        },
        "red_minimum": {
            "main": 2.5,
            "aux": 5
        },
        "red_maximum": {
            "main": 5,
            "aux": 10
        },
        "red_total": {
            "main": 1,
            "aux": 1
        }
    }
    return traffic_lights_timers

def get_traffic_lights_states():
    traffic_lights_states = ["green", "yellow", "red"]
    return  traffic_lights_states

def handle_message(message):
    nocturnal_mode = True if message["modo_noturno"] == "True" else False
    emergency_mode = True if message["modo_emergencia"] == "True" else False
    normal_mode = True if message["modo_normal"] == "True" else False
    debug_mode = True if message["modo_debug"] == "True" else False

    return nocturnal_mode, emergency_mode, normal_mode, debug_mode

def get_pedestrian_sensors_pinout():
    pedestrian_sensors_pinout = {
        "pedestrian1":{
            "1": 8,
            "2": 10
        },
        "pedestrian2":{
            "1": 7,
            "2": 9
        }
    }
    return pedestrian_sensors_pinout