screen_width = 10
screen_height = 20

buttons = [
	[screen_width * 0.85, screen_height * 0.05, "Instructions"],
	[screen_width * 0.86, screen_height * 0.15, "Sound"],
	[screen_width * 0.4, screen_height * 0.7, "Yes"],
	[screen_width * 0.53, screen_height * 0.7, "No"],
	[20, screen_height * 0.3, "Pause"],
	[20, screen_height * 0.2, "Quit"],
]

buttons = [
    [screen_width * 0.85, screen_height * 0.05, "Instructions"],
    [screen_width * 0.86, screen_height * 0.15, "Sound"],
    [screen_width * 0.4, screen_height * 0.7, "Yes"],
    [screen_width * 0.53, screen_height * 0.7, "No"],
    [20, screen_height * 0.3, "Pause"],
    [20, screen_height * 0.2, "Quit"],
]

buttons = [
    [screen_width * 0.85, screen_height * 0.05, "Instructions"],
    [screen_width * 0.86, screen_height * 0.15, "Sound"],
    [screen_width * 0.4, screen_height * 0.7, "Yes"],
    [screen_width * 0.53, screen_height * 0.7, "No"],
    [20, screen_height * 0.3, "Pause"],
    [20, screen_height * 0.2, "Quit"],
]

for button in buttons:
    # Set default color (black)
    button.append(40)   # Height attribute
    button.append(160)  # Width attribute
    if button[2] == "Quit": button.append((255, 0, 0))  # Red color for "Quit" button
    else: button.append((0, 0, 0))  # Black color for other buttons
    button.append(button.pop(2))  # Move label to the end of the button sublist

    print(button)  # Print the modified button sublist