ESP8266_IoT.iotSwitchEvent(ESP8266_IoT.KidsIotSwitchState.off, function () {
    pins.servoWritePin(AnalogPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P0, 1)
})
ESP8266_IoT.iotSwitchEvent(ESP8266_IoT.KidsIotSwitchState.on, function () {
    pins.servoWritePin(AnalogPin.P0, 35)
    pins.digitalWritePin(DigitalPin.P0, 0)
})
ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
basic.forever(function () {
    if (ESP8266_IoT.wifiState(true)) {
        basic.showIcon(IconNames.Heart)
    } else {
        ESP8266_IoT.connectWifi("iptime5G", "01092611378")
        if (ESP8266_IoT.kidsiotState(true)) {
            basic.showIcon(IconNames.SmallHeart)
        } else {
            ESP8266_IoT.connectKidsiot("62c2KpcyPvKT6Piq", "1")
        }
    }
})
basic.forever(function () {
    ESP8266_IoT.uploadKidsiot(input.lightLevel())
    basic.pause(2000)
})
