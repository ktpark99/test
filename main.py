def on_iot_switch_kids_state_off():
    pins.servo_write_pin(AnalogPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P0, 1)
ESP8266_IoT.iot_switch_event(ESP8266_IoT.KidsIotSwitchState.OFF,
    on_iot_switch_kids_state_off)

def on_iot_switch_kids_state():
    pins.servo_write_pin(AnalogPin.P0, 35)
    pins.digital_write_pin(DigitalPin.P0, 0)
ESP8266_IoT.iot_switch_event(ESP8266_IoT.KidsIotSwitchState.ON, on_iot_switch_kids_state)

ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)

def on_forever():
    if ESP8266_IoT.wifi_state(True):
        basic.show_icon(IconNames.HEART)
    else:
        ESP8266_IoT.connect_wifi("iptime5G", "01092611378")
        if ESP8266_IoT.kidsiot_state(True):
            basic.show_icon(IconNames.SMALL_HEART)
        else:
            ESP8266_IoT.connect_kidsiot("", "")
basic.forever(on_forever)

def on_forever2():
    ESP8266_IoT.upload_kidsiot(input.light_level())
    basic.pause(2000)
basic.forever(on_forever2)
