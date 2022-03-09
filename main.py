pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)
up = False
down = False
right = False
left = False
x = 2
y = 2

def on_button_pressed_a():
    global left
    if x <= 0:
        pass
    else:
        left = True
        basic.pause(20)
        left = False
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global right
    if x >= 4:
        pass
    else:
        right = True
        basic.pause(20)
        right = False
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p2():
    global down
    if y >= 4:
        pass
    else:
        down = True
        basic.pause(20)
        down = False
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_logo_event_pressed():
    global up
    if y <= 0:
        pass
    else:
        up = True
        basic.pause(20)
        up = False
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)

def start():
    global up, down, right, left, x, y
    led.plot(x, y)
    if up == True:
        basic.clear_screen()
        y -= 1
    if down == True:
        basic.clear_screen()
        y += 1
    if right == True:
        basic.clear_screen()
        x += 1
    if left == True:
        basic.clear_screen()
        x -= 1
forever(start)