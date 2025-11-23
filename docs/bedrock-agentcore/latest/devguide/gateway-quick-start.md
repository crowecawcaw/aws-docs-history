# Get started with AgentCore Gateway

In this quick start guide you'll learn how to set up a gateway and integrate it into your agents using the AgentCore starter toolkit. For more comprehensive guides and examples, see the [Amazon Bedrock AgentCore Gateway GitHub repository](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway").

###### Note

The AgentCore starter toolkit abstracts the AWS Python SDK (Boto3) into simplified methods and is intended to help developers get started quickly. For a more comprehensive set of operations, you should use an AWS SDK such as Boto3. For more information on Boto3 operations for AgentCore, see [AgentCore Control Plane operations](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control.html").

###### Topics

- [Prerequisites](#gateway-quick-start-prereqs "#gateway-quick-start-prereqs")
- [Step 1: Setup and install](#gateway-quick-start-setup "#gateway-quick-start-setup")
- [Step 2: Create gateway setup script](#gateway-quick-start-create-gateway-setup "#gateway-quick-start-create-gateway-setup")
- [Step 3: Run the setup](#gateway-quick-start-run-setup "#gateway-quick-start-run-setup")
- [Step 4: Use the gateway with an agent](#gateway-quick-start-use-gateway-with-agents "#gateway-quick-start-use-gateway-with-agents")
- [What you've built](#gateway-quick-start-what-youve-built "#gateway-quick-start-what-youve-built")
- [Troubleshooting](#gateway-quick-start-troubleshooting "#gateway-quick-start-troubleshooting")
- [Quick validation](#gateway-quick-start-quick-validation "#gateway-quick-start-quick-validation")
- [Cleanup](#gateway-quick-start-cleanup "#gateway-quick-start-cleanup")
- [Next steps](#gateway-quick-start-next-steps "#gateway-quick-start-next-steps")

## Prerequisites

Before starting, make sure you have the following:

- **AWS Account** with credentials configured. To configure credentials, you can install and use the AWS Command Line Interface by following the steps at [Getting started with the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md").
- **Python 3.10+** installed.
- **IAM permissions** for creating roles, Lambda functions, and using Amazon Bedrock AgentCore.
- **Model Access** – Enable Anthropic's Claude Sonnet 3.7 in the Amazon Bedrock console (or another model for the demo agent)

## Step 1: Setup and install

Run the following in a terminal to set up the virtual environment in which to install the dependencies.

```
mkdir agentcore-gateway-quickstart
cd agentcore-gateway-quickstart
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Then, run the following to install the dependencies

```
pip install boto3
pip install bedrock-agentcore-starter-toolkit
pip install strands-agents
```

## Step 2: Create gateway setup script

Create a new file called `setup_gateway.py` and insert the following complete code into it:

```
"""
Setup script to create Gateway with Lambda target and save configuration
Run this first: python setup_gateway.py
"""

from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient
import json
import logging
import time

def setup_gateway():
    # Configuration
    region = "us-east-1"  # Change to your preferred region

    print("🚀 Setting up AgentCore Gateway...")
    print(f"Region: {region}\n")

    # Initialize client
    client = GatewayClient(region_name=region)
    client.logger.setLevel(logging.INFO)

    # Step 2.1: Create OAuth authorizer
    print("Step 2.1: Creating OAuth authorization server...")
    cognito_response = client.create_oauth_authorizer_with_cognito("TestGateway")
    print("✓ Authorization server created\n")

    # Step 2.2: Create Gateway
    print("Step 2.2: Creating Gateway...")
    gateway = client.create_mcp_gateway(
        # the name of the Gateway - if you don't set one, one will be generated.
        name=None,
        # the role arn that the Gateway will use - if you don't set one, one will be created.
        # NOTE: if you are using your own role make sure it has a trust policy that trusts bedrock-agentcore.amazonaws.com
        role_arn=None,
        # the OAuth authorization server details. If you are providing your own authorization server,
        # then pass an input of the following form: {"customJWTAuthorizer": {"allowedClients": ["<INSERT CLIENT ID>"], "discoveryUrl": "<INSERT DISCOVERY URL>"}}
        authorizer_config=cognito_response["authorizer_config"],
        # enable semantic search
        enable_semantic_search=True,
    )
    print(f"✓ Gateway created: {gateway['gatewayUrl']}\n")

    # If role_arn was not provided, fix IAM permissions
    # NOTE: This is handled internally by the toolkit when no role is provided
    client.fix_iam_permissions(gateway)
    print("⏳ Waiting 30s for IAM propagation...")
    time.sleep(30)
    print("✓ IAM permissions configured\n")

    # Step 2.3: Add Lambda target
    print("Step 2.3: Adding Lambda target...")
    lambda_target = client.create_mcp_gateway_target(
        # the gateway created in the previous step
        gateway=gateway,
        # the name of the Target - if you don't set one, one will be generated.
        name=None,
        # the type of the Target
        target_type="lambda",
        # the target details - set this to define your own lambda if you pre-created one.
        # Otherwise leave this None and one will be created for you.
        target_payload=None,
        # you will see later in the tutorial how to use this to connect to APIs using API keys and OAuth credentials.
        credentials=None,
    )
    print("✓ Lambda target added\n")

    # Step 2.4: Save configuration for agent
    config = {
        "gateway_url": gateway["gatewayUrl"],
        "gateway_id": gateway["gatewayId"],
        "region": region,
        "client_info": cognito_response["client_info"]
    }

    with open("gateway_config.json", "w") as f:
        json.dump(config, f, indent=2)

    print("=" * 60)
    print("✅ Gateway setup complete!")
    print(f"Gateway URL: {gateway['gatewayUrl']}")
    print(f"Gateway ID: {gateway['gatewayId']}")
    print("\nConfiguration saved to: gateway_config.json")
    print("\nNext step: Run 'python run_agent.py' to test your Gateway")
    print("=" * 60)

    return config

if __name__ == "__main__":
    setup_gateway()
```

Expand the following section for a step-by-step understanding of each component.

The following topics explain what happns in each part of the setup script:

###### Topics

- [Import required libraries](#setup-script-import-libraries "#setup-script-import-libraries")
- [Create the Setup Function](#setup-script-create-setup-function "#setup-script-create-setup-function")
- [Create an OAuth Authorization Server](#setup-script-create-oauth "#setup-script-create-oauth")
- [Create a Gateway](#setup-script-create-gateway "#setup-script-create-gateway")
- [Adding Lambda Targets](#setup-script-add-lambda-target "#setup-script-add-lambda-target")
- [Save the gateway configuration](#setup-script-save-config "#setup-script-save-config")

#### Import required libraries

First, import the necessary libraries for gateway creation and configuration.

```
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient
import json
import logging
import time
```

#### Create the Setup Function

Initialize the setup function with your AWSs region configuration.

```
def setup_gateway():
    # Configuration
    region = "us-east-1"  # Change to your preferred region

    print("🚀 Setting up AgentCore Gateway...")
    print(f"Region: {region}\n")

    # Initialize client
    client = GatewayClient(region_name=region)
    client.logger.setLevel(logging.INFO)
```

#### Create an OAuth Authorization Server

Gateways are secured by OAuth authorization servers which ensure that only allowed users can access your Gateway. Let's create an OAuth authorization server using Amazon Cognito.

```
# Step 2.1: Create OAuth authorizer
    print("Step 2.1: Creating OAuth authorization server...")
    cognito_response = client.create_oauth_authorizer_with_cognito("TestGateway")
    print("✓ Authorization server created\n")
```

**What happens here**: This creates an Amazon Cognito user pool with an OAuth 2.0 client credentials flow configured. You'll get a client ID and secret that can be used to obtain access tokens.

#### Create a Gateway

Now, let's create a gateway. The gateway acts as your MCP server endpoint that agents will connect to.

```
# Step 2.2: Create Gateway
    print("Step 2.2: Creating Gateway...")
    gateway = client.create_mcp_gateway(
        # the name of the Gateway - if you don't set one, one will be generated.
        name=None,
        # the role arn that the Gateway will use - if you don't set one, one will be created.
        # NOTE: if you are using your own role make sure it has a trust policy that trusts bedrock-agentcore.amazonaws.com
        role_arn=None,
        # the OAuth authorization server details. If you are providing your own authorization server,
        # then pass an input of the following form: {"customJWTAuthorizer": {"allowedClients": ["<INSERT CLIENT ID>"], "discoveryUrl": "<INSERT DISCOVERY URL>"}}
        authorizer_config=cognito_response["authorizer_config"],
        # enable semantic search
        enable_semantic_search=True,
    )
    print(f"✓ Gateway created: {gateway['gatewayUrl']}\n")

    # If role_arn was not provided, fix IAM permissions
    # NOTE: This is handled internally by the toolkit when no role is provided
    client.fix_iam_permissions(gateway)
    print("⏳ Waiting 30s for IAM propagation...")
    time.sleep(30)
    print("✓ IAM permissions configured\n")
```

**What happens here**: Creates a gateway with MCP protocol support, configures OAuth authorization, and enables semantic search for tool discovery. If you don't provide a role, one is created and configured automatically.

#### Adding Lambda Targets

Let's add a Lambda function target. This code will automatically create a Lambda function with weather and time tools.

```
# Step 2.3: Add Lambda target
    print("Step 2.3: Adding Lambda target...")
    lambda_target = client.create_mcp_gateway_target(
        # the gateway created in the previous step
        gateway=gateway,
        # the name of the Target - if you don't set one, one will be generated.
        name=None,
        # the type of the Target
        target_type="lambda",
        # the target details - set this to define your own lambda if you pre-created one.
        # Otherwise leave this None and one will be created for you.
        target_payload=None,
        # you will see later in the tutorial how to use this to connect to APIs using API keys and OAuth credentials.
        credentials=None,
    )
    print("✓ Lambda target added\n")
```

**What happens here**: Creates a test Lambda function with two tools (`get_weather` and `get_time`) and registers it as a target in your gateway.

#### Save the gateway configuration

Save the gateway configuration to a file for use by the agent.

```
# Step 2.4: Save configuration for agent
    config = {
        "gateway_url": gateway["gatewayUrl"],
        "gateway_id": gateway["gatewayId"],
        "region": region,
        "client_info": cognito_response["client_info"]
    }

    with open("gateway_config.json", "w") as f:
        json.dump(config, f, indent=2)

    print("=" * 60)
    print("✅ Gateway setup complete!")
    print(f"Gateway URL: {gateway['gatewayUrl']}")
    print(f"Gateway ID: {gateway['gatewayId']}")
    print("\nConfiguration saved to: gateway_config.json")
    print("\nNext step: Run 'python run_agent.py' to test your Gateway")
    print("=" * 60)

    return config

if __name__ == "__main__":
    setup_gateway()
```

## Step 3: Run the setup

Execute the setup script to create your gateway and invoke the Lambda target.

```
python setup_gateway.py
```

**What to expect**: The script will take about 2-3 minutes to complete. You'll see progress messages for each step.

## Step 4: Use the gateway with an agent

Create a new file called `run_agent.py` and insert the following code:

```
"""
Agent script to test the Gateway
Run this after setup: python run_agent.py
"""

from strands import Agent
from strands.models import BedrockModel
from strands.tools.mcp.mcp_client import MCPClient
from mcp.client.streamable_http import streamablehttp_client
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient
import json
import sys

def create_streamable_http_transport(mcp_url: str, access_token: str):
    return streamablehttp_client(mcp_url, headers={"Authorization": f"Bearer {access_token}"})

def get_full_tools_list(client):
    """Get all tools with pagination support"""
    more_tools = True
    tools = []
    pagination_token = None
    while more_tools:
        tmp_tools = client.list_tools_sync(pagination_token=pagination_token)
        tools.extend(tmp_tools)
        if tmp_tools.pagination_token is None:
            more_tools = False
        else:
            more_tools = True
            pagination_token = tmp_tools.pagination_token
    return tools

def run_agent():
    # Load configuration
    try:
        with open("gateway_config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("❌ Error: gateway_config.json not found!")
        print("Please run 'python setup_gateway.py' first to create the Gateway.")
        sys.exit(1)

    gateway_url = config["gateway_url"]
    client_info = config["client_info"]

    # Get access token for the agent
    print("Getting access token...")
    client = GatewayClient(region_name=config["region"])
    access_token = client.get_access_token_for_cognito(client_info)
    print("✓ Access token obtained\n")

    # Model configuration - change if needed
    model_id = "anthropic.claude-3-7-sonnet-20250219-v1:0"

    print("🤖 Starting AgentCore Gateway Test Agent")
    print(f"Gateway URL: {gateway_url}")
    print(f"Model: {model_id}")
    print("-" * 60)

    # Setup Bedrock model
    bedrockmodel = BedrockModel(
        inference_profile_id=model_id,
        streaming=True,
    )

    # Setup MCP client
    mcp_client = MCPClient(lambda: create_streamable_http_transport(gateway_url, access_token))

    with mcp_client:
        # List available tools
        tools = get_full_tools_list(mcp_client)
        print(f"\n📋 Available tools: {[tool.tool_name for tool in tools]}")
        print("-" * 60)

        # Create agent
        agent = Agent(model=bedrockmodel, tools=tools)

        # Interactive loop
        print("\n💬 Interactive Agent Ready!")
        print("Try asking: 'What's the weather in Seattle?'")
        print("Type 'exit', 'quit', or 'bye' to end.\n")

        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("👋 Goodbye!")
                break

            print("\n🤔 Thinking...\n")
            response = agent(user_input)
            print(f"\nAgent: {response.message.get('content', response)}\n")

if __name__ == "__main__":
    run_agent()
```

### Run your agent

Test your gateway by running the agent and interacting with the tools.

```
python run_agent.py
```

That's it! The agent will start and you can ask questions like:

- "What's the weather in Seattle?"
- "What time is it in New York?"

## What you've built

Through this getting started tutorial, you've created the following resources:

- **MCP Server (Gateway)**: A managed endpoint at `https://gateway-id.gateway.bedrock-agentcore.region.amazonaws.com/mcp`
- **Lambda tools**: Mock functions that return test data (weather: "72°F, Sunny", time: "2:30 PM")
- **OAuth authentication**: Secure access using Cognito tokens
- **AI agent**: Claude-powered assistant that can discover and use your tools

## Troubleshooting

The following table shows some possible issues and their solutions:

| Issue                       | Solution                                                                      |
| --------------------------- | ----------------------------------------------------------------------------- |
| "No module named 'strands'" | Run: `pip install strands-agents`                                             |
| "Model not enabled"         | Enable Claude Sonnet 3.7 in Bedrock console → Model access                    |
| "AccessDeniedException"     | Check IAM permissions for `bedrock-agentcore:*`                               |
| Gateway not responding      | Wait 30-60 seconds after creation for DNS propagation                         |
| OAuth token expired         | Tokens expire after 1 hour, get new one with `get_access_token_for_cognito()` |

## Quick validation

Run the following commands in a terminal to check that your gateway is working.

```
# Check your Gateway is working
curl -X POST YOUR_GATEWAY_URL \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'

# Watch live logs
aws logs tail /aws/bedrock-agentcore/gateways/YOUR_GATEWAY_ID --follow
```

## Cleanup

Create a `cleanup_gateway.py` file and insert the following contents:

```
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient
import json

with open("gateway_config.json", "r") as f:
    config = json.load(f)

client = GatewayClient(region_name=config["region"])
client.cleanup_gateway(config["gateway_id"], config["client_info"])
print("✅ Cleanup complete!")
```

Run the following in a terminal:

```
python cleanup_gateway.py
```

## Next steps

- **Custom Lambda Tools**: Create Lambda functions with your business logic
- **Add Your Own APIs**: Extend your Gateway with OpenAPI specifications for real services
- **Production Setup**: Configure VPC endpoints, custom domains, and monitoring
