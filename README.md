# Public Equity Exploratory Data Analysis Tool

This tool provides a comprehensive platform for performing exploratory data analysis on public equity data. It is designed to facilitate quick insights and visualization, leveraging the power of Python's Pandas and Streamlit libraries alongside the Pygwalker API.

## Features

- **Interactive Data Visualization**: Utilize Streamlit's dynamic capabilities to interact with data visualizations in real time.
- **Memory Efficiency**: Built-in caching of data and configurations to optimize performance and reduce memory usage.
- **Flexible Configuration**: Ability to save and retrieve chart configurations through a JSON file.

## Installation

To run this tool, you will need Python installed on your system. You can install the required packages using pip:

```bash
pip install streamlit pandas pygwalker
```

## Usage

1. **Prepare Your Data**:
   - Ensure your financial data is in CSV format and includes the necessary columns for analysis.
   - Save the data in the same directory as your script or adjust the path in the script accordingly.

2. **Configuration**:
   - Modify `gw_config.json` to match your specific visualization needs. This file controls the appearance and functionality of the generated plots.

3. **Launch the Application**:
   - Run the Streamlit application by navigating to your project directory and running:
     ```bash
     streamlit run <your_script_name>.py
     ```

## Example Data Format

Your CSV file (ex: `ATD.TO.csv`) should follow a structured format, e.g., Date, Open, High, Low, Close, Volume. Ensure the correct formatting for optimal performance.

## Citation

This app is powered by streamlit https://docs.streamlit.io/get-started and pygwalker https://github.com/Kanaries/pygwalker

## License

The project is open-sourced under Apache-2.0.