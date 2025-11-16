# Using Strands Agents in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio now supports Strands Agents integration, streamlining AI agent development for users. This integration enables you to immediately begin building AI agents using Strands SDK's powerful capabilities without the complexity of dependency management or environment configuration.

By making Strands SDK a native component of the Amazon SageMaker ecosystem, developers can focus on creating innovative AI solutions while leveraging Amazon SageMaker's enterprise-grade infrastructure and scaling capabilities.

The Amazon BedrockModel provider is used by default when creating a basic Agent with the provided Amazon Bedrock model. You can specify which Amazon Bedrock model to use by passing in the model_id string directly to the Agent constructor. You must use the application inference profile ARN as the model_id, like in the following example:

```

import boto3
from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import calculator, current_time

# Create a Bedrock model with the custom session
bedrock_model = BedrockModel(
model_id="arn:aws:bedrock:us-west-2:123456789321:application-inference-profile/ab788q84ey7z"
)

# Create an agent with the model and tools
agent = Agent(
model=bedrock_model,
tools=[calculator, current_time]
)
# First request will cache the tools
response1 = agent("What time is it?")

# Second request will reuse the cached tools
response2 = agent("What is the square root of 1764?")

```

You can obtain the application inference profile ARN by performing the following
procedure:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to your project.
3. Navigate to your chat agents under the **Build** menu.
4. In the left-hand navigation pane, choose **Models** in order to
   see all the enabled Amazon Bedrock models for the project.
5. Choose a model and then on the model details page, locate the application
   inference profile ARN.
