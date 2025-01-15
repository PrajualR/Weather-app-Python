
# Weather App

This is a simple **Weather App** built with **Python** and **PyQt5**, which allows users to search for current weather information by entering a city name. It retrieves weather data from the **OpenWeatherMap API** and displays the temperature and weather description in an interactive GUI.

## Features
- Search for weather by city name.
- Displays the current temperature (in Celsius or Fahrenheit).
- Displays the weather description (e.g., "clear sky", "light rain").
- Option to switch between Celsius and Fahrenheit.
- Error handling for various API responses (e.g., city not found, incorrect API key).
- Responsive and user-friendly interface.

## Requirements
- Python 3.x
- PyQt5
- Requests library

### Installation

1. Clone the repository or download the project files.
2. Install the required libraries using `pip`:
   ```bash
   pip install PyQt5 requests
   ```
3. Get your **OpenWeatherMap API key** from [OpenWeatherMap](https://openweathermap.org/).
4. Set your API key as an environment variable:
   ```bash
   export API_KEY="your_api_key_here"
   ```
   Or alternatively, you can replace `os.getenv('API_KEY')` in the code with your API key directly (not recommended for production).

## Usage

1. Run the `Weather_app.py` script:
   ```bash
   python Weather_app.py
   ```
2. Enter a city name in the input field and click "Search".
3. The weather information (temperature and description) will be displayed.


## Code Explanation

- **PyQt5 GUI:** The GUI is built using PyQt5, which provides an easy way to create graphical applications in Python.
- **OpenWeatherMap API:** The app uses the OpenWeatherMap API to fetch weather data for the entered city.
- **Error Handling:** The app gracefully handles various errors, such as missing city name, invalid API key, or server issues.
- **Unit Conversion:** You can choose between Celsius and Fahrenheit units for temperature using a dropdown menu.


## Acknowledgments
- **OpenWeatherMap API** for providing free weather data.
- **PyQt5** for the graphical user interface framework.
