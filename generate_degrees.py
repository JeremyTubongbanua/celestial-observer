import argparse
import csv
from datetime import datetime
from typing import List, Tuple

# Constants
SIDEREAL_ROTATION_PERIOD_HOURS: float = 24.622962  # Sidereal rotation period of Mars in hours

def parse_horizons_file(file_path: str) -> Tuple[List[datetime], List[float]]:
    """
    Parses the Horizons data file to extract timestamps and Sun-Observer-Target (S-O-T) angles.

    Args:
        file_path (str): Path to the Horizons data file.

    Returns:
        Tuple[List[datetime], List[float]]: A tuple containing two lists:
            - List of datetime objects representing the timestamps.
            - List of floats representing the Mars-Sun angles (S-O-T angles).
    """
    timestamps: List[datetime] = []
    s_o_t_angles: List[float] = []
    with open(file_path, 'r') as file:
        in_data_section: bool = False
        for line in file:
            if "$$SOE" in line:
                in_data_section = True
                continue
            if "$$EOE" in line:
                break
            if in_data_section:
                parts: List[str] = line.split()
                if len(parts) < 10:
                    continue
                date_str: str = f"{parts[0]} {parts[1]}"
                try:
                    timestamp: datetime = datetime.strptime(date_str, "%Y-%b-%d %H:%M")
                    s_o_t_angle: float = float(parts[9])  # The S-O-T angle column
                    timestamps.append(timestamp)
                    s_o_t_angles.append(s_o_t_angle)
                except (ValueError, IndexError):
                    continue
    return timestamps, s_o_t_angles

def calculate_rotation_degrees(timestamps: List[datetime]) -> List[float]:
    """
    Calculates the rotation degrees of Mars based on its sidereal rotation period.

    Args:
        timestamps (List[datetime]): List of datetime objects representing the timestamps.

    Returns:
        List[float]: List of floats representing the rotation degrees (0-360) of Mars.
    """
    degrees_list: List[float] = []
    initial_time: datetime = timestamps[0]

    for timestamp in timestamps:
        elapsed_time: float = (timestamp - initial_time).total_seconds() / 3600
        rotation_fraction: float = (elapsed_time % SIDEREAL_ROTATION_PERIOD_HOURS) / SIDEREAL_ROTATION_PERIOD_HOURS
        rotation_degrees: float = rotation_fraction * 360
        degrees_list.append(round(rotation_degrees, 2))

    return degrees_list

def write_to_csv(output_path: str, timestamps: List[datetime], rotation_degrees: List[float], s_o_t_angles: List[float]) -> None:
    """
    Writes the timestamps, rotation degrees, and Mars-Sun angles to a CSV file.

    Args:
        output_path (str): Path to the output CSV file.
        timestamps (List[datetime]): List of datetime objects representing the timestamps.
        rotation_degrees (List[float]): List of floats representing the rotation degrees of Mars.
        s_o_t_angles (List[float]): List of floats representing the Mars-Sun angles.
    """
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "Rotation (Degrees)", "Mars-Sun Angle (Degrees)"])
        for timestamp, rotation_degree, s_o_t_angle in zip(timestamps, rotation_degrees, s_o_t_angles):
            writer.writerow([timestamp.strftime("%Y-%m-%d %H:%M"), rotation_degree, s_o_t_angle])

def main() -> None:
    """
    Main function to parse arguments, process the Horizons data file, and generate the output CSV file.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Generate rotation degrees of Mars and Mars-Sun angle from Horizons data.")
    parser.add_argument("--data", required=True, help="Path to the Horizons data file.")
    parser.add_argument("--output", required=True, help="Output CSV file path.")
    args: argparse.Namespace = parser.parse_args()

    timestamps, s_o_t_angles = parse_horizons_file(args.data)
    rotation_degrees = calculate_rotation_degrees(timestamps)
    write_to_csv(args.output, timestamps, rotation_degrees, s_o_t_angles)

if __name__ == "__main__":
    main()
