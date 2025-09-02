import logging
from livekit.agents import function_tool, RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun

@function_tool()
async def get_weather(
        context: RunContext,
        city: str) -> str:
    """
    Get the current weather for a given city.
    """
    try:
        response = requests.get(
            f"http://wttr.in/{city}?format=3"
        )
        if response.status_code == 200:
            logging.info(f"Weather in {city}: {response.text.strip()}")
            return response.text.strip()
        else:
            logging.error(f"Error fetching weather data: {response.status_code}")
            return f"Sorry, I couldn't fetch the weather for {city}."
    except Exception as e:
        logging.error(f"Error retrieving weather for {city}: {e}")
        return f"Sorry, an error occurred while fetching the weather for {city}."

@function_tool()
async def web_search(
        context: RunContext,
        query: str) -> str:
    """
    Perform a web search using DuckDuckGo and return the top result.
    """
    try:
        results = DuckDuckGoSearchRun().run(tool_input=query)
        logging.info(f"Search results for '{query}': {results}")
        return results
    except Exception as e:
        logging.error(f"Error performing web search for '{query}': {e}")
        return f"Sorry, an error occurred while searching for '{query}'."