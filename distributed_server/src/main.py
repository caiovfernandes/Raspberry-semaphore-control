from traffic_lights import config_light_output, init_traffic_control, debug_lights, activate_nocturnal_mode, activate_emergency_mode
from gpio import config_gpio
from tcp_server import start_tcp_server
from utils import handle_message


def main():
    message = start_tcp_server()
    config_gpio()
    config_light_output()

    nocturnal_mode, emergency_mode, normal_mode, debug_mode = handle_message(message)
    if(nocturnal_mode):
        activate_nocturnal_mode()
    elif(emergency_mode):
        activate_emergency_mode()
    elif(normal_mode):
        init_traffic_control()
    elif(debug_mode):
        debug_lights()

if __name__ == "__main__":
    main()