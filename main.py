pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)
x = 2
y = 2
def on_forever():
    led.plot(x, y) 
forever(on_forever)
def on_button_pressed_a():
    global x
    if x <= 0:
        pass
    else:
        basic.clear_screen()
        x -= 1
        led.plot(x, y)
        
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    global x
    if x >= 4:
        pass
    else:
        basic.clear_screen()
        x += 1
        led.plot(x, y)
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_pin_pressed_p2():
    global y
    if y >= 4:
        pass
    else:
        basic.clear_screen()
        y += 1
        led.plot(x, y)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)
def on_button_pressed_ab():
    global x, y
    x = 2
    y = 2
    basic.clear_screen()
    led.plot(x, y)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
def on_logo_event_pressed():
    global y
    if y <= 0:
        pass
    else:
        basic.clear_screen()
        y -= 1
        led.plot(x, y)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)