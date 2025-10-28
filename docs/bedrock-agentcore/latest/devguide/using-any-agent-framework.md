# Use any agent framework

You can use open source AI frameworks to create an agent or tool.
This topic shows examples for a variety of frameworks, including Strands Agents, LangGraph, and Google ADK.

###### Topics

- [Strands Agents](#agent-runtime-frameworks-strands "#agent-runtime-frameworks-strands")
- [LangGraph](#agent-runtime-frameworks-langgraph "#agent-runtime-frameworks-langgraph")
- [Google Agent Development Kit (ADK)](#agent-runtime-frameworks-google-adk "#agent-runtime-frameworks-google-adk")
- [OpenAI Agents SDK](#agent-runtime-frameworks-open-ai-agents-sdk "#agent-runtime-frameworks-open-ai-agents-sdk")
- [Microsoft AutoGen](#agent-runtime-frameworks-microsoft-autogen "#agent-runtime-frameworks-microsoft-autogen")
- [CrewAI](#agent-runtime-frameworks-crewai "#agent-runtime-frameworks-crewai")

## Strands Agents

For the full example, see [https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/strands-agents](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/strands-agents "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/strands-agents").

```
import os
from strands import Agent
from strands_tools import file_read, file_write, editor

agent = Agent(tools=[file_read, file_write, editor])


from bedrock_agentcore.runtime import BedrockAgentCoreApp
app = BedrockAgentCoreApp()
@app.entrypoint
def agent_invocation(payload, context):
    """Handler for agent invocation"""
    user_message = payload.get("prompt", "No prompt found in input, please guide customer to create a json payload with prompt key")
    result = agent(user_message)
    print("context:\n-------\n", context)
    print("result:\n*******\n", result)
    return {"result": result.message}
app.run()
```

## LangGraph

For the full example, see [https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/langgraph](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/langgraph "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/langgraph").

```
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
#------------------------------------------------
from bedrock_agentcore.runtime import BedrockAgentCoreApp
app = BedrockAgentCoreApp()
#------------------------------------------------

llm = init_chat_model(
    "us.anthropic.claude-3-5-haiku-20241022-v1:0",
    model_provider="bedrock_converse",
)

# Create graph
graph_builder = StateGraph(State)
...
# Add nodes and edges
...
graph = graph_builder.compile()

# Finally write your entrypoint
@app.entrypoint
def agent_invocation(payload, context):

    print("received payload")
    print(payload)

    tmp_msg = {"messages": [{"role": "user", "content": payload.get("prompt", "No prompt found in input, please guide customer as to what tools can be used")}]}
    tmp_output = graph.invoke(tmp_msg)
    print(tmp_output)

    return {"result": tmp_output['messages'][-1].content}

app.run()
```

## Google Agent Development Kit (ADK)

For the full example, see [https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/adk](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/adk "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/adk").

```
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types
import asyncio
import os

# adapted form https://google.github.io/adk-docs/tools/built-in-tools/#google-search

APP_NAME="google_search_agent"
USER_ID="user1234"

# Agent Definition
# Add your GEMINI_API_KEY
root_agent = Agent(
    model="gemini-2.0-flash",
    name="openai_agent",
    description="Agent to answer questions using Google Search.",
    instruction="I can answer your questions by searching the internet. Just ask me anything!",
    # google_search is a pre-built tool which allows the agent to perform Google searches.
    tools=[google_search]
)

# Session and Runner
async def setup_session_and_runner(user_id, session_id):
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME, user_id=user_id, session_id=session_id)
    runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)
    return session, runner

# Agent Interaction
async def call_agent_async(query, user_id, session_id):
    content = types.Content(role='user', parts=[types.Part(text=query)])
    session, runner = await setup_session_and_runner(user_id, session_id)
    events = runner.run_async(user_id=user_id, session_id=session_id, new_message=content)

    async for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print("Agent Response: ", final_response)

    return final_response


from bedrock_agentcore.runtime import BedrockAgentCoreApp
app = BedrockAgentCoreApp()

@app.entrypoint
def agent_invocation(payload, context):
    return asyncio.run(call_agent_async(payload.get("prompt", "what is Bedrock Agentcore Runtime?"), payload.get("user_id",USER_ID), context.session_id))

app.run()
```

## OpenAI Agents SDK

For the full example, see [https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/openai-agents](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/openai-agents "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/openai-agents").

```
from agents import Agent, Runner, WebSearchTool
import logging
import asyncio
import sys

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("openai_agents")

# Configure OpenAI library logging
logging.getLogger("openai").setLevel(logging.DEBUG)

logger.debug("Initializing OpenAI agent with tools")
agent = Agent(
    name="Assistant",
    tools=[
        WebSearchTool(),
    ],
)

async def main(query=None):
    if query is None:
        query = "Which coffee shop should I go to, taking into account my preferences and the weather today in SF?"

    logger.debug(f"Running agent with query: {query}")

    try:
        logger.debug("Starting agent execution")
        result = await Runner.run(agent, query)
        logger.debug(f"Agent execution completed with result type: {type(result)}")
        return result
    except Exception as e:
        logger.error(f"Error during agent execution: {e}", exc_info=True)
        raise

# Integration with Bedrock AgentCore
from bedrock_agentcore.runtime import BedrockAgentCoreApp
app = BedrockAgentCoreApp()

@app.entrypoint
async def agent_invocation(payload, context):
    logger.debug(f"Received payload: {payload}")
    query = payload.get("prompt", "How can I help you today?")

    try:
        result = await main(query)
        logger.debug("Agent execution completed successfully")
        return {"result": result.final_output}
    except Exception as e:
        logger.error(f"Error during agent execution: {e}", exc_info=True)
        return {"result": f"Error: {str(e)}"}

# Run the app when imported
if __name__== "__main__":
    app.run()

```

## Microsoft AutoGen

For the full example, see [https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/autogen](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/autogen "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/agentic-frameworks/autogen").

```
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio
import logging

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("autogen_agent")

# Initialize the model client
model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
)

# Define a simple function tool that the agent can use
async def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return f"The weather in {city} is 73 degrees and Sunny."

# Define an AssistantAgent with the model and tool
agent = AssistantAgent(
    name="weather_agent",
    model_client=model_client,
    tools=[get_weather],
    system_message="You are a helpful assistant.",
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens
)

# Integrate with Bedrock AgentCore
from bedrock_agentcore.runtime import BedrockAgentCoreApp
app = BedrockAgentCoreApp()

@app.entrypoint
async def main(payload):
    # Process the user prompt
    prompt = payload.get("prompt", "Hello! What can you help me with?")

    # Run the agent
    result = await Console(agent.run_stream(task=prompt))

    # Extract the response content for JSON serialization
    if result and hasattr(result, 'messages') and result.messages:
        last_message = result.messages[-1]
        if hasattr(last_message, 'content'):
            return {"result": last_message.content}

    return {"result": "No response generated"}

app.run()

```

## CrewAI

For the full example, see [https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/01-AgentCore-runtime/01-hosting-agent/04-crewai-with-bedrock-model/runtime-with-crewai-and-bedrock-models.ipynb](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/01-AgentCore-runtime/01-hosting-agent/04-crewai-with-bedrock-model/runtime-with-crewai-and-bedrock-models.ipynb "https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/01-AgentCore-runtime/01-hosting-agent/04-crewai-with-bedrock-model/runtime-with-crewai-and-bedrock-models.ipynb").

```
from crewai import Agent, Crew, Process, Task
from crewai_tools import MathTool, WeatherTool
from bedrock_agentcore.runtime import BedrockAgentCoreApp
import argparse
import json
app = BedrockAgentCoreApp()

# Define CrewAI agent
def create_researcher():
    """Create a researcher agent"""
    from langchain_aws import ChatBedrock

    # Initialize LLM
    llm = ChatBedrock(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",
        model_kwargs={"temperature": 0.1}
    )

    # Create researcher agent
    return Agent(
        role="Senior Research Specialist",
        goal="Find comprehensive and accurate information about the topic",
        backstory="You are an experienced research specialist with a talent for finding relevant information.",
        verbose=True,
        llm=llm,
        tools=[MathTool(), WeatherTool()]
    )

# Define the analyst agent
def create_analyst():
....

# Create the crew
def create_crew():
    """Create and configure the CrewAI crew"""
    # Create agents
    researcher = create_researcher()
    analyst = create_analyst()

    # Create research task with fields like description filled in as per crewAI docs
    research_task = Task(
        description="...",
        agent=researcher,
        expected_output="..."
    )

    analysis_task = Task(
    ...
    )

    # Create crew
    return Crew(
        agents=[researcher, analyst],
        tasks=[research_task, analysis_task],
        process=Process.sequential,
        verbose=True
    )

# Initialize the crew
crew = create_crew()

# Finally write your entrypoint
@app.entrypoint
def crewai_bedrock(payload):
    """
    Invoke the crew with a payload
    """
    user_input = payload.get("prompt")

    # Run the crew
    result = crew.kickoff(inputs={"topic": user_input})

    # Return the result
    return result.raw

if __name__ == "__main__":
    app.run()
```
