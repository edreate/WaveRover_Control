# WaveRover Control

This repository contains code to control the Waveshare WaveRover using various techniques, both hardware and software.
## Introduction

The WaveRover Control project provides a way to control the Waveshare WaveRover using a Python script and a keyboard. The script uses the `pynput` library to capture keyboard inputs and send movement commands to the rover.

## Requirements
- Python 3.6+ 
- `requests` library 
- `pynput` library
## Installation

To get started, you'll need to install the required Python libraries. Use the following commands to install them:

```bash
pip install requests pynput
```


## Keyboard Control

The keyboard control script allows you to move the WaveRover using the WASD keys. Additionally, you can switch between different speed modes using the number keys 1, 2, and 3.
### Controls: 
- **W** : Move forward 
- **S** : Move backward 
- **A** : Turn left 
- **D** : Turn right 
- **1** : Switch to slow mode 
- **2** : Switch to medium mode 
- **3** : Switch to fast mode 
- **ESC** : Exit the control program


## Usage 
1. Clone this repository to your local machine.

```bash
git clone [https://github.com/yourusername/waverrover-control.git](https://github.com/edreate/WaveRover_Control)
cd WaveRover_Control
```

2. Ensure that your WaveRover is connected to the same network as your computer. 
3. Open the `keyboard_control.py` script and modify the `WAVER_ROVER_IP` variable to match the IP address of your WaveRover. 
4. Run the script:

```bash
python control.py
```

You should see the message "Rover control started. Use WASD to move. Press 1 for slow, 2 for medium, 3 for fast. Press ESC to exit."

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any improvements or bug fixes.
## License

This project is licensed under the MIT License. See the [LICENSE]()  file for details.

