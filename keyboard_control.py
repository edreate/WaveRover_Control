import requests
from pynput import keyboard


# --- Configuration ---
WAVER_ROVER_IP = "192.168.179.3"

# Speed rates for different modes
FORWARD_BACKWARD_SPEED_RATES = {"fast": 1.0, "medium": 0.6, "slow": 0.45}

TURNING_SPEED_RATES = {"fast": 1.0, "medium": 0.8, "slow": 0.6}

CURRENT_MODE = "slow"

# --- Rover Communication ---


def send_request_to_rover(command: str) -> bool:
    """
    Sends a movement command to the Waver Rover.

    Args:
        command: JSON string representing the desired movement.

    Returns:
        True if the request was successful (status code 200), False otherwise.
    """
    url = f"http://{WAVER_ROVER_IP}/js?json={command}"
    response = requests.get(url)
    return response.status_code == 200


def movement_string(speed_l: float, speed_r: float, turning: bool = False) -> str:
    """
    Creates a JSON string for controlling the Waver Rover's movement.

    Args:
        speed_l: Speed for the left motor (-0.5 to 0.5).
        speed_r: Speed for the right motor (-0.5 to 0.5).
        turning: Whether the movement is a turn or not.

    Source:
        L is the speed of the left wheel, R is the speed of the right wheel,
        and the speed range is -0.5 ~ +0.5, positive value forward,
        negative value backward.

        The speed of 0.5 represents 100% of the PWM of the motor on that side,
        and 0.25 represents 50% of the PWM of the motor on that side.

        It is recommended to use this command to control the product.

        https://www.waveshare.com/wiki/WAVE_ROVER

    Returns:
        JSON string representing the movement command.
    """
    speed_rate = (
        TURNING_SPEED_RATES[CURRENT_MODE]
        if turning
        else FORWARD_BACKWARD_SPEED_RATES[CURRENT_MODE]
    )
    return str(
        {
            "T": 1,
            "L": speed_l * speed_rate,
            "R": speed_r * speed_rate,
        }
    )


# --- Movement Commands ---


def move_forward():
    """Moves the Rover forward."""
    send_request_to_rover(movement_string(0.5, 0.5))


def move_backward():
    """Moves the Rover backward."""
    send_request_to_rover(movement_string(-0.5, -0.5))


def move_right():
    """Turns the Rover right."""
    send_request_to_rover(movement_string(0.5, -0.5, turning=True))


def move_left():
    """Turns the Rover left."""
    send_request_to_rover(movement_string(-0.5, 0.5, turning=True))


def stop():
    """Stops the Rover."""
    send_request_to_rover(movement_string(0.0, 0.0))


# --- Keyboard Control ---


def on_press(key):
    """Handles key presses for Rover control."""
    global CURRENT_MODE
    try:
        if key.char == "w":
            move_forward()
        elif key.char == "s":
            move_backward()
        elif key.char == "a":
            move_left()
        elif key.char == "d":
            move_right()
        elif key.char == "1":
            CURRENT_MODE = "slow"
            print("\nMode changed to slow")
        elif key.char == "2":
            CURRENT_MODE = "medium"
            print("\nMode changed to medium")
        elif key.char == "3":
            CURRENT_MODE = "fast"
            print("\nMode changed to fast")
    except AttributeError:
        pass  # Ignore non-character keys


def on_release(_):
    """Stops the Rover when a key is released."""
    stop()


# --- Main Program ---


def main():
    """Starts the Rover control program."""
    print(
        "Rover control started. Use WASD to move. Press 1 for slow, 2 for medium, 3 for fast. Press ESC to exit."
    )

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    import os  # Better to import modules at the top

    os.system("cls" if os.name == "nt" else "clear")  # Cross-platform screen clear

    main()
