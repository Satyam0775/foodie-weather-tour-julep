from julep import Julep
import streamlit as st
from utils.utils import clean_response_text  # Make sure this path matches your utils structure

class AgentServices:
    def __init__(self, api_key):
        """
        Initialize the AgentServices class with Julep API key.
        """
        self.api_key = api_key
        self.client = None
        self.agents = {}

    def initialize_client(self):
        """
        Initialize the Julep client using the API key.
        Returns True if successful, False otherwise.
        """
        try:
            self.client = Julep(api_key=self.api_key)
            return True
        except Exception as e:
            st.error(f"❌ Could not initialize Julep client: {e}")
            return False

    def create_agents(self):
        """
        Create all required agents and store them in a dictionary.
        Each agent serves a specific role in the food tour generation process.
        """
        try:
            with st.spinner("🤖 Initializing AI agents..."):
                roles = {
                    "weather": {
                        "name": "Weather Oracle",
                        "about": "A weather expert giving location-specific dining tips."
                    },
                    "culinary": {
                        "name": "Food Culture Guru",
                        "about": "Local cuisine expert suggesting iconic dishes."
                    },
                    "restaurant": {
                        "name": "Restaurant Detective",
                        "about": "Finds authentic, highly-rated restaurants."
                    },
                    "tour": {
                        "name": "Storytelling Tour Guide",
                        "about": "Designs engaging and weather-aware day tours."
                    },
                    "coordinator": {
                        "name": "Experience Coordinator",
                        "about": "Combines weather, food, and travel insights into one cohesive guide."
                    }
                }

                for key, config in roles.items():
                    agent = self.client.agents.create(
                        name=config["name"],
                        model="claude-3.5-sonnet",
                        about=config["about"]
                    )
                    self.agents[key] = agent

            return True
        except Exception as e:
            st.error(f"❌ Agent creation failed: {e}")
            return False

    def chat_with_agent(self, agent_key, prompt):
        """
        Sends a prompt to a specific agent and returns the AI-generated response.
        """
        if agent_key not in self.agents:
            return f"⚠️ Agent '{agent_key}' not found."

        agent = self.agents[agent_key]

        try:
            session = self.client.sessions.create(agent=agent.id)

            reply = self.client.sessions.chat(
                session_id=session.id,
                messages=[{"role": "user", "content": prompt}]
            )

            if reply.messages and hasattr(reply.messages[-1], "content"):
                content = reply.messages[-1].content
                if isinstance(content, list):
                    for item in content:
                        if isinstance(item, dict) and "text" in item:
                            return clean_response_text(item["text"])
                        elif isinstance(item, str):
                            return clean_response_text(item)
                elif isinstance(content, str):
                    return clean_response_text(content)

            return "⚠️ No response available."

        except Exception as e:
            st.warning(f"⚠️ Failed to communicate with {agent.name}: {e}")
            return f"❌ Could not get a reply from {agent.name}. Try again later."
