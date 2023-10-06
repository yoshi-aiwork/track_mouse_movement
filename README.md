# Mouse Movement Tracker
This Python script allows users to track their mouse movements over a specified duration and records the positions, mouse clicks, and the title of the active window. The data is then exported to a CSV file.

## Features
- Track mouse position at millisecond intervals.
- Record mouse clicks (left, right, middle, etc.).
- Capture the title of the currently active window.
- Export the recorded data to a CSV file named in the format "mouse_data_YYYYMMDD_HHMMSS.csv".
- Visualize mouse movements, clicks, and active window trajectories in a PNG image.

## Prerequisites
Ensure you have Python installed on your machine. This script was developed using Python 3.x.

## Installation
1. Clone the repository:
git clone https://github.com/your_username/track_mouse_movement.git
2. Navigate to the project directory:
cd track_mouse_movement/scripts
3. Install the required libraries:

## Usage
1. Run the script:
python mouse_movement_tracking.py
2. When prompted, enter the recording duration in seconds.
3. The script will then start recording the mouse data for the specified duration.
4. Once the recording is complete, you can find the CSV file in the `scripts` directory.

### Visualizing Mouse Movements
1. After generating the CSV file using the tracking script, run the visualization script:
python visualize_movemovement.py --csv_path <path_to_your_csv_file.csv>
2. The script will create a PNG image visualization of the mouse movements, clicks, and active window trajectories in the same directory with the same base name as the CSV.

## Caution
Always be cautious when using mouse and keyboard listeners, as they can capture sensitive information. Ensure you're aware of the data being recorded and stored.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT] (https://choosealicense.com/licenses/mit/)
