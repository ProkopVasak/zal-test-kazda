let up = false
let down = false
let right = false
let left = false
let x = 2
let y = 2
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (x <= 0) {
        
    } else {
        left = true
        basic.pause(20)
        left = false
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (x >= 4) {
        
    } else {
        right = true
        basic.pause(20)
        right = false
    }
    
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    if (y >= 4) {
        
    } else {
        down = true
        basic.pause(20)
        down = false
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    
    if (y <= 0) {
        
    } else {
        up = true
        basic.pause(20)
        up = false
    }
    
})
forever(function start() {
    
    led.plot(x, y)
    if (up == true) {
        basic.clearScreen()
        y -= 1
    }
    
    if (down == true) {
        basic.clearScreen()
        y += 1
    }
    
    if (right == true) {
        basic.clearScreen()
        x += 1
    }
    
    if (left == true) {
        basic.clearScreen()
        x -= 1
    }
    
})
