# brave_search_agent.py

from python_a2a import A2AServer, skill, agent, run_server, TaskStatus, TaskState
import os
import requests
import logging


@agent(
    name="Brave Search Agent",
    description="Performs internet search using Brave Search API",
    version="1.0.0",
    url="https://yourdomain.com"
)
class BraveSearchAgent(A2AServer):

    @skill(
        name="Search Internet",
        description="Perform a web search using Brave Search API",
        tags=["search", "internet", "brave"],
        examples="Search 'must visit places in utah in may'"
    )
    def search(self, query: str):
        """Perform search using Brave Search API"""
        api_key = os.getenv("BRAVE_API_KEY")
        if not api_key:
            return "Search service not available (missing Brave API key)."

        headers = {
            "Accept": "application/json",
            "X-Subscription-Token": api_key,
        }

        url = "https://api.search.brave.com/res/v1/web/search"
        params = {"q": query, "count": 5}

        try:
            response = requests.get(url, headers=headers, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            results = data.get("web", {}).get("results", [])
            if not results:
                return "No search results found."

            summary = "\n".join(
                [f"- {r.get('title')}: {r.get('url')}" for r in results]
            )
            return f"Top results for '{query}':\n{summary}"

        except requests.RequestException as e:
            logging.error(f"Error during Brave search: {e}")
            return f"Search failed: {e}"
        except Exception as e:
            return f"Unexpected error: {e}"

    def handle_task(self, task):
        message_data = task.message or {}
        content = message_data.get("content", {})
        text = content.get("text", "") if isinstance(content, dict) else ""

        if text.strip():
            query = text.strip()
            result = self.search(query)
            task.artifacts = [{
                "parts": [{"type": "text", "text": result}]
            }]
            task.status = TaskStatus(state=TaskState.COMPLETED)
        else:
            task.status = TaskStatus(
                state=TaskState.INPUT_REQUIRED,
                message={"role": "agent", "content": {"type": "text", 
                         "text": "Please provide a search query."}}
            )
        return task


if __name__ == "__main__":
    agent = BraveSearchAgent(google_a2a_compatible=True)
    run_server(agent, port=8002, debug=True)
