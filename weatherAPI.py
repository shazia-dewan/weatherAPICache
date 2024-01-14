import requests
from multiprocessing import Pool, Manager, freeze_support
import time

weather = {}

# Get weather data from api single processing
def get_weather(api_key, city):
    global weather
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            # Update the global dictionary with temperature data
            weather[city] = data['main']['temp']
            # Simulate a delay for testing parallelism
            time.sleep(3)
            return data
        else:
            print("Error")
    except Exception as e:
        print("There was an exception")
        return None

# Get weather data using multiprocessing
def get_multi_city(api_key, cities):
    with Pool() as pool:
        # Use starmap to pass multiple arguments to the function
        results = pool.starmap(get_weather, [(api_key, city) for city in cities])

    return results

# Get weather data sequentially
def get_sequential(api_key, cities):
    results = []
    for city in cities:
        data = get_weather(api_key, city)
        results.append(data)
    return results

# Display weather data from api
def display_weather(weather_data):
    if weather_data:
        print("Weather Information:")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("Failed to fetch weather information.")

def main():
    cities = ["london", "paris", "ottawa", "toronto"]
    api_key = "97acacc9c48e4ae723d8b3921c9fcc5d"

    # Measure time for parallel execution
    start_time_parallel = time.time()
    weather_data_parallel = get_multi_city(api_key, cities)
    end_time_parallel = time.time()

    # Display results for parallel execution
    for city, data in zip(cities, weather_data_parallel):
        if data:
            print(f"Weather in {city}: {data['weather'][0]['description']}")
        else:
            print(f"Failed to fetch weather data for {city}")

    total_time_parallel = end_time_parallel - start_time_parallel
    print(f"Total Execution Time (Parallel): {total_time_parallel:.2f} seconds")

    # Measure time for sequential execution
    start_time_sequential = time.time()
    weather_data_sequential = get_sequential(api_key, cities)
    end_time_sequential = time.time()

    # Display results for sequential execution
    for city, data in zip(cities, weather_data_sequential):
        if data:
            print(f"Weather in {city}: {data['weather'][0]['description']}")
        else:
            print(f"Failed to fetch weather data for {city}")

    total_time_sequential = end_time_sequential - start_time_sequential
    print(f"Total Execution Time (Sequential): {total_time_sequential:.2f} seconds")

    # Display the global dictionary
    print("Weather Information:")
    for city, temperature in weather.items():
        print(f"{city}: {temperature}°C")

if __name__ == "__main__":
    main()
