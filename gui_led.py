import tkinter as tk
from gpiozero import LED

# Define LEDs connected to GPIO pins
led1 = LED(26)  # LED 1 on GPIO 26
led2 = LED(3)  # LED 2 on GPIO 3
led3 = LED(2)  # LED 3 on GPIO 2

# Function to turn off all the LED
def reset_led():
    led1.off()
    led2.off()
    led3.off()
    
# Initialize LEDs
reset_led()

# Function to turn on the selected LED and turn off the others
def turn_on_led(led):
    led1.off()
    led2.off()
    led3.off()
    if led == 1:
        led1.on()
    elif led == 2:
        led2.on()
    elif led == 3:
        led3.on()

# Function to handle radio button selection
def led_select():
    selected_led = led_var.get()
    turn_on_led(selected_led)
    
def quit_app():
    led1.off()
    led2.off()
    led3.off()
    root.quit()

# Create the GUI window
root = tk.Tk()
root.title("LED Control")

# Variable to store the radio button selection
led_var = tk.IntVar()

# Create a heading
heading = tk.Label(root, text="Toggle lights", font=("Helvetica", 24))
heading.pack()


# Create radio buttons
radio1 = tk.Radiobutton(root, text="LED 1", variable=led_var, value=1, command=led_select)
radio2 = tk.Radiobutton(root, text="LED 2", variable=led_var, value=2, command=led_select)
radio3 = tk.Radiobutton(root, text="LED 3", variable=led_var, value=3, command=led_select)

# Pack the radio buttons
radio1.pack(anchor=tk.W)
radio2.pack(anchor=tk.W)
radio3.pack(anchor=tk.W)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset_led)
reset_button.pack()

# Exit button
exit_button = tk.Button(root, text="Exit", command=quit_app)
exit_button.pack()

# Run the GUI event loop
root.mainloop()
