# Building AI agents with Amazon Nova

###### Note

This documentation is for Amazon Nova Version 1. For information about how to build AI agents with Amazon Nova 2, visit [Building AI agents](../nova2-userguide/building-ai-agents.md "../nova2-userguide/building-ai-agents.md").

An AI agent helps your end-users complete actions based on organization data and user
input. Agents orchestrate interactions between foundation models (FMs), data sources,
software applications, and user conversations. In addition, agents automatically call APIs
to take actions and invoke knowledge bases to supplement information for these actions.
Developers can save weeks of development effort by integrating agents to accelerate the
delivery of generative artificial intelligence (generative AI) applications .

With agents, you can automate tasks for your customers and answer questions for them. For
example, you can create an agent that helps customers process insurance claims or an agent
that helps customers make travel reservations. You don't have to provision capacity, manage
infrastructure, or write custom code. Amazon Nova manages prompt engineering, memory,
monitoring, encryption, user permissions, and API invocation.

For information on building AI agents in Amazon Bedrock, see [Bedrock
Agents](../../../bedrock/latest/userguide/agents.md "../../../bedrock/latest/userguide/agents.md").

Agents perform the following tasks:

- Extend foundation models to understand user requests and break down the tasks that
  the agent must perform into smaller steps.
- Collect additional information from a user through natural conversation.
- Take actions to fulfill a customer's request by making API calls to your company
  systems.
- Augment performance and accuracy by querying data sources.

###### Topics

- [Using Amazon Nova as a foundation model in an AI
  agent](agents-use-nova.md "agents-use-nova.md")
- [Using Amazon Nova with AgentCore](#agents-agentcore "#agents-agentcore")
- [Using Amazon Nova with Strands](#agents-strands "#agents-strands")
- [Additional Resources](#agents-resources "#agents-resources")

## Using Amazon Nova with AgentCore

Amazon Nova models can be used with all Bedrock AgentCore services, enabling you to deploy
and operate highly effective agents securely, at scale. Key Services include Runtime, Identity,
Memory, Gateway, and Observability. See Amazon Bedrock AgentCore for additional details and
{placeholder} for sample code.

The following is an example of using Amazon Nova with AgentCore:

```

import boto3
from strands.models import BedrockModel

# Create a Bedrock model with the custom session
bedrock_model = BedrockModel(
model_id="model_id",
boto_session=session
)

```

## Using Amazon Nova with Strands

Strands provides native support for Amazon Bedrock, allowing you to use these
Nova models in your agents with minimal configuration. See Strands Amazon Bedrock
for more details.

The following is a code example showing how to use Strands with Amazon Nova:

```

from strands import Agent
from strands.models import BedrockModel

# Create a Bedrock model instance
bedrock_model = BedrockModel(
    model_id="us.amazon.nova-premier-v1:0",
    temperature=0.3,
    top_p=0.8,
)

# Create an agent using the BedrockModel instance
agent = Agent(model=bedrock_model)

# Use the agent
response = agent("Tell me about Amazon Bedrock.")

```

## Additional Resources

1. [Automate tasks in your application using agents](../../../bedrock/latest/userguide/agents.md "../../../bedrock/latest/userguide/agents.md")
2. [Tool use (function calling) with Amazon Nova](tool-use.md "tool-use.md")
3. [Text understanding prompting best
   practices](prompting-text-understanding.md "prompting-text-understanding.md")
