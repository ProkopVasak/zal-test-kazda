pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
let x = 2
let y = 2
forever(function on_forever() {
    led.plot(x, y)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (x <= 0) {
        
    } else {
        basic.clearScreen()
        x -= 1
        led.plot(x, y)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (x >= 4) {
        
    } else {
        basic.clearScreen()
        x += 1
        led.plot(x, y)
    }
    
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    if (y >= 4) {
        
    } else {
        basic.clearScreen()
        y += 1
        led.plot(x, y)
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    x = 2
    y = 2
    basic.clearScreen()
    led.plot(x, y)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    
    if (y <= 0) {
        
    } else {
        basic.clearScreen()
        y -= 1
        led.plot(x, y)
    }
    
})
