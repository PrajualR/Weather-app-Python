import json
import os
from dotenv import load_dotenv
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt5.QtCore import Qt
import  sys

class Weather(QWidget):
    def __init__(self):
        super().__init__()

        self.cityLabel = QLabel(self)
        self.cityInput = QLineEdit(self)
        self.cityInput.setPlaceholderText("Enter the City:")
        self.getWeatherButton = QPushButton("Search", self)
        self.temperature = QLabel(self)
        self.description = QLabel(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(600, 400, 400, 200)


        vbox = QVBoxLayout()
        vbox.addWidget(self.cityInput)
        vbox.addWidget(self.getWeatherButton)
        vbox.addWidget(self.cityLabel)
        vbox.addWidget(self.temperature)
        vbox.addWidget(self.description)
        vbox.setSpacing(20)

        self.setLayout(vbox)

        self.cityLabel.setAlignment(Qt.AlignCenter)
        self.temperature.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)

        self.cityLabel.setObjectName("cityLabel")
        self.cityInput.setObjectName("cityInput")
        self.getWeatherButton.setObjectName("getWeatherButton")
        self.temperature.setObjectName("temperature")
        self.description.setObjectName("description")
        self.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                font-size: 18px;
                font-family: 'Roboto';
                font-weight: bold;
                color: white;
                padding: 10px;
                border-radius: 15px;
            }
            QLineEdit#cityInput {
                font-size: 20px;
                padding: 10px;
                border-radius: 15px;
            }
            QLabel {
                font-size: 32px;
                font-weight: bold;
                font-family: 'Helvetica';
                color: #FF6347;
            }
            QLabel#description {
                font-size: 32px;
                font-weight: bold;
                font-family: 'Helvetica';
                color: blue; 
            }
        """)
        # self.setStyleSheet("background-color : green;")
        self.getWeatherButton.setStyleSheet("background-color : green;")

        self.getWeatherButton.clicked.connect(self.getWeatherData)



    def getWeatherData(self):
        # Load environment variables from the .env file
        load_dotenv()
        apiKey = os.getenv('API_KEY')

        city = self.cityInput.text()
        url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"
        if not city:
            self.displayError("City name cannot be empty.")
            return

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
						
            if data.get("cod") == 200:
                self.displayWeather(data) 
            else:
                self.displayError(data.get("message", "An error occurred."))
        except requests.exceptions.HTTPError as httpError:
            match response.status_code:
                case 400:
                    self.displayError("Bad request.\nPlease check your input.")
                case 401:
                    self.displayError("Unauthorized error.\nInvalid API key.")
                case 403:
                    self.displayError("Forbidden error.\nAccess denied.")
                case 404:
                    self.displayError("Not found error.\nCity not found.")
                case 500:
                   self.displayError("Internal server error.\nPlease try again.")
                case 502:
                    self.displayError("Bad gateway error.\nInvalid response from the server.")
                case 503:
                    self.displayError("Service unavailable error.\nServer down.")
                case 504:
                    self.displayError("Gateway timeout error.\nNo response.")
                case _:
                    self.displayError(f"HTTP error: {httpError}")
        except requests.exceptions.ConnectionError:
            self.displayError("Connection error. Please check you internet.")
        except requests.exceptions.TooManyRedirects:
            self.displayError("Timeout error. The request timed out.")
        except requests.exceptions.Timeout:
            self.displayError("Too many redirects. Please check the URL.")
        except requests.exceptions.RequestException as reqException:
            self.displayError(f"Request error. {reqException}")

    def displayError(self, message):
        self.temperature.setStyleSheet("font-size: 30px; font-style: italic; color: red;")								
        self.temperature.setText(message)
        self.cityLabel.clear()
        self.description.clear()


    def displayWeather(self, data):
        # self.temperature.setStyleSheet("font-size: 100px;")
        # temp_k = data["main"]["temp"]
        # temp_c = temp_k - 273.15
        # cityName = self.cityInput.text()
        # self.cityLabel.setStyleSheet("font-size: 60px;")
        # self.cityLabel.setText(cityName)
        # self.temperature.setText(f"{temp_c:.0f}°C")
        # weatherDescription = data["weather"][0]["description"]
        # self.description.setStyleSheet("font-size: 60px;")
        # self.description.setText(weatherDescription.capitalize())
        # Extract temperature
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15
        # unit_symbol = "°C" if self.unitComboBox.currentText() == "Celsius" else "°F"
        cityName = data["name"]
        weatherDescription = data["weather"][0]["description"]

        # Update UI
        self.cityLabel.setStyleSheet("font-size: 40px;")
        self.cityLabel.setText(cityName)
        self.temperature.setStyleSheet("font-size: 100px;")
									 
								
										
														
										
        self.temperature.setText(f"{temp_c:.0f}°C")
															  
        self.description.setStyleSheet("font-size: 60px;")
        self.description.setText(weatherDescription.capitalize())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weatherApp = Weather()
    weatherApp.show()
    sys.exit(app.exec_())