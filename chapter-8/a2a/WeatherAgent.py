# uv run simple_agent.py from the parent directory

from python_a2a import A2AServer, skill, agent, run_server, TaskStatus, TaskState

import os
import requests
import logging


@agent(
    name="Weather Agent",
    description="Provides weather information",
    version="1.0.0",
    url="https://zzz.example.com"
)
class WeatherAgent(A2AServer):
    
    @skill(
        name="Get Weather",
        description="Get current weather for a location",
        tags=["weather", "forecast"],
        examples="I am a weather agent for getting weather forecast from Open weather"
    )
    def get_weather(self, location):

        """Get real weather for a location using OpenWeatherMap API."""
        api_key = os.getenv("OPENWEATHER_API_KEY")

        if not api_key:
            return "Weather service not available (missing API key)."
        
        try:
            url = (
                f"https://api.openweathermap.org/data/2.5/weather?"
                f"q={location}&units=imperial&appid={api_key}"
            )
            logging.debug(f"Request URL: {url}")  # Log the full request URL

            response = requests.get(url, timeout=5)
            response.raise_for_status()
            logging.debug(f"Response Status Code: {response.status_code}")  # Log status code
            logging.debug(f"Response Text: {response.text}")  # Log raw response text
            
            data = response.json()
            
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            city_name = data["name"]

            logging.debug(f"Parsed Data: Temp = {temp}, Description = {description}, City = {city_name}")
            
            return f"The weather in {city_name} is {description} with a temperature of {temp}°F."
        
        except requests.RequestException as e:
            return f"Error fetching weather: {e}"
        except (KeyError, TypeError):
            return "Could not parse weather data."
    
    def handle_task(self, task):
        # Extract location from message
        message_data = task.message or {}
        content = message_data.get("content", {})
        text = content.get("text", "") if isinstance(content, dict) else ""
        
        if "weather" in text.lower() and "in" in text.lower():
            location = text.split("in", 1)[1].strip().rstrip("?.")
            
            # Get weather and create response
            weather_text = self.get_weather(location)
            task.artifacts = [{
                "parts": [{"type": "text", "text": weather_text}]
            }]
            task.status = TaskStatus(state=TaskState.COMPLETED)
        else:
            task.status = TaskStatus(
                state=TaskState.INPUT_REQUIRED,
                message={"role": "agent", "content": {"type": "text", 
                         "text": "Please ask about weather in a specific location."}}
            )
        return task

# Run the server
if __name__ == "__main__":
    agent = WeatherAgent(google_a2a_compatible=True)
    run_server(agent, port=8000, debug=True)
