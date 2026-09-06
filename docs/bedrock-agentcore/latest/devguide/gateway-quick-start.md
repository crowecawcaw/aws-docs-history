

# Get started with AgentCore Gateway
<a name="gateway-quick-start"></a>

In this quick start guide you’ll learn how to set up a gateway and integrate it into your agents using the AgentCore CLI. For more comprehensive guides and examples, see the [Amazon Bedrock AgentCore Gateway GitHub repository](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-features/07-centralize-and-govern-your-ai-infrastructure/01-gateway).

**Note**  
The AgentCore CLI provides both commands and an interactive TUI wizard for managing AgentCore Gateway resources. For the full AWS SDK API reference, see [AgentCore Control Plane operations](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control.html).

**Topics**
+ [Prerequisites](#gateway-quick-start-prereqs)
+ [Step 1: Setup and install](#gateway-quick-start-setup)
+ [Step 2: Create gateway](#gateway-quick-start-create-gateway-setup)
+ [Step 3: Run the setup](#gateway-quick-start-run-setup)
+ [Step 4: Use the gateway with an agent](#gateway-quick-start-use-gateway-with-agents)
+ [What you’ve built](#gateway-quick-start-what-youve-built)
+ [Troubleshooting](#gateway-quick-start-troubleshooting)
+ [Quick validation](#gateway-quick-start-quick-validation)
+ [Cleanup](#gateway-quick-start-cleanup)
+ [Next steps](#gateway-quick-start-next-steps)

## Prerequisites
<a name="gateway-quick-start-prereqs"></a>

Before starting, make sure you have the following:
+  ** AWS Account** with credentials configured. To configure credentials, you can install and use the AWS Command Line Interface by following the steps at [Getting started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).
+  **Node.js 20\+** installed (for the AgentCore CLI).
+  **Python 3.10\+** installed (for the agent script).
+  **IAM permissions** for creating roles, Lambda functions, and using Amazon Bedrock AgentCore.
+  **Model access.** Amazon Bedrock enables access to foundation models by default. To use a non-foundation model, follow the [model access steps](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html#model-access-sdk-step4).

## Step 1: Setup and install
<a name="gateway-quick-start-setup"></a>

Install the AgentCore CLI globally:

```
npm install -g @aws/agentcore
```

Create a new AgentCore project with an agent and a gateway:

**Example**  

1. 

   ```
   agentcore create --project-name MyGatewayProject --name MyGatewayAgent \
     --language Python --framework Strands --model-provider Bedrock --memory none
   cd MyGatewayProject
   ```

   These options create a Python Strands agent that uses Amazon Bedrock and no memory. Alternatively, run `agentcore create` without options and select **Agent** in the interactive wizard.

1. You can also run `agentcore create` without flags to use the interactive wizard. The wizard guides you through selecting a project name, agent framework, model provider, and other options.

## Step 2: Create gateway
<a name="gateway-quick-start-create-gateway-setup"></a>

Add a gateway and a target to your project using the AgentCore CLI:

**Example**  

1. 

   ```
   # Add a gateway with no inbound auth (simplest for getting started)
   agentcore add gateway --name TestGateway --authorizer-type NONE --runtimes MyGatewayAgent
   
   # Add a Lambda function target
   agentcore add gateway-target --name TestLambdaTarget --type lambda-function-arn \
     --lambda-arn <YOUR_LAMBDA_ARN> \
     --tool-schema-file tools.json \
     --gateway TestGateway
   ```

1. Run `agentcore` to open the TUI, then select **add** and choose **Gateway** :

1. Enter the gateway name:  
![Gateway wizard: enter name](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/gateway-add-name.png)

1. Select the authorizer type. For this quickstart, choose **NONE** :  
![Gateway wizard: select NONE authorizer](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/gateway-add-auth-none.png)

1. Configure advanced options or accept the defaults:  
![Gateway wizard: advanced configuration](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/gateway-add-advanced.png)

1. Review the configuration and press **Enter** to confirm:  
![Gateway wizard: review configuration](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/gateway-add-confirm.png)

   Next, select **add** again and choose **Gateway Target** to add a Lambda function target:

1. Enter the target name.

1. Select **Lambda function** as the target type:  
![Gateway target wizard: select Lambda function](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/gateway-target-type-lambda.png)

1. Enter the Lambda ARN and tool schema file path, then confirm.

To use JWT-based authorization instead, specify `--authorizer-type CUSTOM_JWT` with your OAuth discovery URL:

**Example**  

1. 

   ```
   agentcore add gateway --name TestGateway \
     --authorizer-type CUSTOM_JWT \
     --discovery-url https://cognito-idp.us-east-1.amazonaws.com/<POOL_ID>/.well-known/openid-configuration \
     --allowed-audience <CLIENT_ID> \
     --runtimes MyGatewayAgent
   ```

1. Run `agentcore` to open the TUI, then select **add** and choose **Gateway** . When prompted for the authorizer type, select **Custom JWT** :

1. Enter the gateway name:  
![Gateway wizard: enter name](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/gateway-add-name.png)

1. Select **Custom JWT** as the authorizer type:  
![Gateway wizard: select Custom JWT authorizer](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/gateway-add-auth-jwt.png)

1. Enter the OAuth discovery URL and allowed audience when prompted.

1. Configure advanced options or accept the defaults:  
![Gateway wizard: advanced configuration](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/gateway-add-advanced.png)

1. Review the configuration and press **Enter** to confirm:  
![Gateway wizard: review configuration](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/gateway-add-confirm.png)

## Step 3: Run the setup
<a name="gateway-quick-start-run-setup"></a>

Deploy your project to AWS:

```
agentcore deploy
```

The CLI synthesizes a AWS CDK stack and deploys your gateway, targets, and agent to Amazon Bedrock AgentCore. This takes about 2-3 minutes.

## Step 4: Use the gateway with an agent
<a name="gateway-quick-start-use-gateway-with-agents"></a>

Retrieve your gateway URL using the AgentCore CLI:

```
agentcore status
```

Create a new file called `run_agent.py` and insert the following code. Install the Python dependencies first:

```
pip install strands-agents mcp
```

```
"""
Agent script to test the Gateway
Run this after setup: python run_agent.py
"""

from strands import Agent
from strands.models import BedrockModel
from strands.tools.mcp.mcp_client import MCPClient
from mcp.client.streamable_http import streamablehttp_client
import json
import sys

def create_streamable_http_transport(mcp_url: str):
    return streamablehttp_client(mcp_url)

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
    # Get the gateway URL from agentcore status
    gateway_url = "<YOUR_GATEWAY_URL>"  # Replace with URL from 'agentcore status'

    # Model configuration - change if needed
    model_id = "anthropic.claude-3-7-sonnet-20250219-v1:0"

    print("Starting AgentCore Gateway Test Agent")
    print(f"Gateway URL: {gateway_url}")
    print(f"Model: {model_id}")
    print("-" * 60)

    # Setup Bedrock model
    bedrockmodel = BedrockModel(
        model_id=model_id,
        streaming=True,
    )

    # Setup MCP client (no auth token needed for NONE authorizer)
    mcp_client = MCPClient(lambda: create_streamable_http_transport(gateway_url))

    with mcp_client:
        # List available tools
        tools = get_full_tools_list(mcp_client)
        print(f"\nAvailable tools: {[tool.tool_name for tool in tools]}")
        print("-" * 60)

        # Create agent
        agent = Agent(model=bedrockmodel, tools=tools)

        # Interactive loop
        print("\nInteractive Agent Ready!")
        print("Try asking: 'What's the weather in Seattle?'")
        print("Type 'exit', 'quit', or 'bye' to end.\n")

        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Goodbye!")
                break

            print("\nThinking...\n")
            response = agent(user_input)
            print(f"\nAgent: {response.message.get('content', response)}\n")

if __name__ == "__main__":
    run_agent()
```

### Run your agent
<a name="gateway-quick-start-run-agent"></a>

Test your gateway by running the agent and interacting with the tools.

```
python run_agent.py
```

That’s it\! The agent will start and you can ask questions like:
+ "What’s the weather in Seattle?"
+ "What time is it in New York?"

## What you’ve built
<a name="gateway-quick-start-what-youve-built"></a>

Through this getting started tutorial, you’ve created the following resources:
+  **MCP Server (Gateway)** : A managed endpoint at `https://gateway-id.gateway.bedrock-agentcore.region.amazonaws.com/mcp` 
+  **Lambda tools** : Mock functions that return test data (weather: "72°F, Sunny", time: "2:30 PM")
+  **AI agent** : Claude-powered assistant that can discover and use your tools

## Troubleshooting
<a name="gateway-quick-start-troubleshooting"></a>

The following table shows some possible issues and their solutions:


| Issue | Solution | 
| --- | --- | 
| "No module named 'strands'" | Run: `pip install strands-agents`  | 
| "Model access denied" | Amazon Bedrock enables access to foundation models by default. For a non-foundation model, follow the [model access steps](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html#model-access-sdk-step4). | 
| "AccessDeniedException" | Check IAM permissions for bedrock-agentcore:\* | 
| Gateway not responding | Wait 30-60 seconds after creation for DNS propagation | 

## Quick validation
<a name="gateway-quick-start-quick-validation"></a>

Run the following commands in a terminal to check that your gateway is working.

```
# Check your Gateway is working
curl -X POST YOUR_GATEWAY_URL \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'

# Watch live logs
aws logs tail /aws/bedrock-agentcore/gateways/YOUR_GATEWAY_ID --follow
```

## Cleanup
<a name="gateway-quick-start-cleanup"></a>

To remove the gateway and its targets from your project:

```
agentcore remove gateway --name TestGateway
```

To remove all resources and redeploy:

```
agentcore remove all
agentcore deploy
```

## Next steps
<a name="gateway-quick-start-next-steps"></a>
+  **Custom Lambda Tools** : Create Lambda functions with your business logic
+  **Add Your Own APIs** : Extend your Gateway with OpenAPI specifications for real services
+  **Production Setup** : Configure VPC endpoints, custom domains, and monitoring