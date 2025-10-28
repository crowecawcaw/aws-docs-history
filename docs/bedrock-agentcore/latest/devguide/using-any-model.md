# Use any foundation model

You can use any foundation model with AgentCore Runtime The following are examples for
Amazon Bedrock, Open AI, and Gemini:

###### Topics

- [Amazon Bedrock](#agent-runtime-model-bedrock "#agent-runtime-model-bedrock")
- [Open AI](#agent-runtime-model-open-ai "#agent-runtime-model-open-ai")
- [Gemini](#agent-runtime-model-gemini "#agent-runtime-model-gemini")

## Amazon Bedrock

```
import boto3
from strands.models import BedrockModel

# Create a Bedrock model with the custom session
bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    boto_session=session
)
```

## Open AI

```
from strands.models.openai import OpenAIModel
model = OpenAIModel(
    client_args={
        "api_key": "<our_OPENAI_API_KEY>",
    # **model_config
    model_id="gpt-4o",
    params={
        "max_tokens": 1000,
        "temperature": 0.7,
    }
)


from strands import Agent
from strands_tools import python_repl
agent = Agent(model=model,tools=[python_repl])
```

## Gemini

```
import os
from langchain.chat_models import init_chat_model

# Use your Google API key to initialize the chat model
os.environ["GOOGLE_API_KEY"] = "..."

llm = init_chat_model("google_genai:gemini-2.0-flash")
```
