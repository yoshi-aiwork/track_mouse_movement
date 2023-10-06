import pandas as pd
import matplotlib.pyplot as plt
import textwrap
import argparse
import pyautogui
import numpy as np

def str2bool(v):
    """
    Convert string representation of boolean to a boolean type.
    """
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def visualize_and_export_mouse_data(filename, include_clicks=True, include_active_windows=True):
    # Fetch screen resolution
    screen_width, screen_height = pyautogui.size()

    # Adjust the figure size based on the screen resolution
    fig_width = screen_width / 100
    fig_height = screen_height / 100

    # Load the data
    mouse_data = pd.read_csv(filename)
    unique_windows = mouse_data['active_window_title'].unique()
    # Plotting setup
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    
    if include_active_windows:
        # Get unique active windows and assign a unique color to each
        colors = plt.cm.jet(np.linspace(0, 1, len(unique_windows)))
        window_to_color = dict(zip(unique_windows, colors))
        
        for window, color in window_to_color.items():
            subset = mouse_data[mouse_data['active_window_title'] == window]
            ax.plot(subset['x'], subset['y'], color=color, alpha=0.5)
    else:
        ax.plot(mouse_data['x'], mouse_data['y'], color='blue', alpha=0.5) # Using a single color

    if include_clicks:
               
        # Highlight mouse clicks
        left_clicks = mouse_data[mouse_data['mouse_click'] == 'left']
        right_clicks = mouse_data[mouse_data['mouse_click'] == 'right']
        middle_clicks = mouse_data[mouse_data['mouse_click'] == 'middle']
        scroll_clicks = mouse_data[mouse_data['mouse_click'] == 'scroll']
        other_clicks = mouse_data[~mouse_data['mouse_click'].isin(['left', 'right', 'middle', 'scroll']) & ~mouse_data['mouse_click'].isna()]

        ax.scatter(left_clicks['x'], left_clicks['y'], color='red', s=100, marker='o', edgecolors='black', label='Left Clicks')
        ax.scatter(right_clicks['x'], right_clicks['y'], color='blue', s=100, marker='o', edgecolors='black', label='Right Clicks')
        ax.scatter(middle_clicks['x'], middle_clicks['y'], color='green', s=100, marker='o', edgecolors='black', label='Middle Clicks')
        ax.scatter(scroll_clicks['x'], scroll_clicks['y'], color='purple', s=100, marker='o', edgecolors='black', label='Scroll Clicks')
        ax.scatter(other_clicks['x'], other_clicks['y'], color='orange', s=100, marker='o', edgecolors='black', label='Other Clicks')

    # Setting the plot aesthetics
    ax.set_xlim(0, screen_width)
    ax.set_ylim(0, screen_height)
    ax.set_title('Mouse Movements and Clicks')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.grid(True)

    # Adjusting legend size and placement
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])

    # Wrapping the window title if it's too long
    wrapped_windows = ['\n'.join(textwrap.wrap(str(window), 30)) for window in unique_windows]

    # Increasing the font size and wrapping the text
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 10}, labels=wrapped_windows)

    plt.tight_layout()

    # Export to PNG
    export_filename = filename.replace('.csv', '.png')
    plt.savefig(export_filename, bbox_inches='tight')
    plt.close()

    print(f"Visualization exported to: {export_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize mouse movement data from a CSV file.")
    parser.add_argument("--csv_path", type=str, required=True, help="Path to the CSV file containing mouse movement data.")
    parser.add_argument("--include_clicks", type=str2bool, default=True, help="Include mouse movement trajectories in the visualization. Default is True.")
    parser.add_argument("--include_active_windows", type=str2bool, default=True, help="Differentiate mouse trajectories based on active windows. Default is True.")
    
    args = parser.parse_args()
    visualize_and_export_mouse_data(args.csv_path, args.include_clicks, args.include_active_windows)