# QuantumFlow

QuantumFlow is a Python-based tool designed to generate detailed reports about system processes and application activity on Windows systems. This tool utilizes the `psutil` library to gather data on currently running processes and generates a comprehensive report in CSV format.

## Features

- **Process Monitoring**: Collects information about active system processes, including PID, process name, CPU usage, memory usage, and the user who initiated the process.
- **CSV Report Generation**: Outputs a detailed report in CSV format, which can be opened with any spreadsheet application for further analysis.
- **Extensible Design**: Designed with future enhancements in mind, allowing for easy integration of additional application activity tracking features.

## Requirements

- Python 3.x
- psutil library

## Installation

Before running QuantumFlow, ensure you have the required Python package by installing it via pip:

```bash
pip install psutil
```

## Usage

To generate a system process report, simply run the `quantumflow.py` script:

```bash
python quantumflow.py
```

The script will generate a CSV file in the same directory with a timestamped filename indicating when the report was created.

## Future Enhancements

- Integration of application-specific activity tracking features.
- Advanced filtering options for process data.
- Real-time monitoring with a graphical user interface (GUI).

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Contact

For any questions or feature requests, please open an issue on the GitHub repository.