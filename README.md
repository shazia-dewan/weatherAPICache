Description: This program to collects weather data for multiple cities using the OpenWeatherMap API. It uses python requests library to send HTTP requests. 
I have Incorporated multiprocessing to be able to fetch weather data for multiple cities in parallel. Used the concept of a worker pool with multiple threads to distribute the workload.
Created a python webserver to display the data collected in the global shared dictionary. Tested the retrieval of weather functions using PyTest.

To run the webserver type in terminal: python3 weatherServer.py
To see the data in the server type in new terminal: curl http://localhost:8080

To run the pytests navigate to test directory and type: pytest test_weather.py
