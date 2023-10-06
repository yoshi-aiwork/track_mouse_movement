import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse
import pyautogui
import textwrap

def visualize_and_export_mouse_data(filename):
    # Fetch screen resolution
    screen_width, screen_height = pyautogui.size()

    # Adjust the figure size based on the screen resolution
    fig_width = screen_width / 100  # Assuming 100 DPI, can be adjusted
    fig_height = screen_height / 100

    # Load the data
    mouse_data = pd.read_csv(filename)

    # Get unique active windows and assign a unique color to each
    unique_windows = mouse_data['active_window_title'].unique()
    colors = plt.cm.jet(np.linspace(0, 1, len(unique_windows)))
    window_to_color = dict(zip(unique_windows, colors))

    # Plot the trajectories
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    for window, color in window_to_color.items():
        subset = mouse_data[mouse_data['active_window_title'] == window]
        ax.plot(subset['x'], subset['y'], label=window, color=color)

    # Highlight mouse clicks
    clicks = mouse_data.dropna(subset=['mouse_click'])
    ax.scatter(clicks['x'], clicks['y'], color='red', s=100, marker='o', edgecolors='black', label='Mouse Clicks')

    # Setting the plot aesthetics
    ax.set_xlim(0, screen_width)
    ax.set_ylim(0, screen_height)
    ax.set_title('Mouse Movements and Clicks')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.grid(True)

    # Adjusting legend size and placement for 90-10 ratio
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])

    # Wrapping the window title if it's too long, ensuring each title is a string
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
    
    args = parser.parse_args()
    visualize_and_export_mouse_data(args.csv_path)