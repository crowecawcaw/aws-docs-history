# Deploy MCP servers in AgentCore Runtime

Amazon Bedrock AgentCore Runtime lets you deploy and run Model Context Protocol (MCP) servers in the
AgentCore Runtime. This guide walks you through creating, testing, and deploying your first MCP
server.

For an example, see [https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/02-hosting-MCP-server](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/02-hosting-MCP-server "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/02-hosting-MCP-server").

In this section, you learn:

- How to create an MCP server with tools
- How to test your server locally
- How to deploy your server to AWS
- How to invoke your deployed server
  For more information about MCP, see [MCP protocol contract](runtime-mcp-protocol-contract.md "runtime-mcp-protocol-contract.md").

###### Topics

- [How Amazon Bedrock AgentCore supports MCP](#runtime-mcp-how-it-works "#runtime-mcp-how-it-works")
- [Prerequisites](#runtime-mcp-prerequisites "#runtime-mcp-prerequisites")
- [Step 1: Create your MCP server](#runtime-mcp-create-server "#runtime-mcp-create-server")
- [Step 2: Test your MCP server locally](#runtime-mcp-test-locally "#runtime-mcp-test-locally")
- [Step 3: Deploy your MCP server to AWS](#runtime-mcp-deploy-aws "#runtime-mcp-deploy-aws")
- [Step 4: Invoke your deployed MCP server](#runtime-mcp-invoke-server "#runtime-mcp-invoke-server")
- [Appendix](#runtime-mcp-appendix "#runtime-mcp-appendix")

## How Amazon Bedrock AgentCore supports MCP

When you configure a Amazon Bedrock AgentCore Runtime with the MCP protocol, the service
expects MCP server containers to be available at the path `0.0.0.0:8000/mcp`,
which is the default path supported by most official MCP server SDKs.

Amazon Bedrock AgentCore requires stateless streamable-HTTP servers because the Runtime
provides session isolation by default. The platform automatically adds a
`Mcp-Session-Id` header for any request without it, so MCP clients can
maintain connection continuity to the same Amazon Bedrock AgentCore Runtime session.

The payload of the [InvokeAgentRuntime](../APIReference/API_InvokeAgentRuntime.md "../APIReference/API_InvokeAgentRuntime.md") API is passed through directly,
allowing RPC messages of protocols like MCP to be easily proxied.

## Prerequisites

- Python 3.10 or higher installed and basic understanding of Python
- An AWS account with appropriate permissions and local credentials
  configured

## Step 1: Create your MCP server

### Install required packages

First, install the MCP package:

```
pip install mcp
```

### Create your first MCP

server

Create a new file called `my_mcp_server.py`:

```
# my_mcp_server.py

from mcp.server.fastmcp import FastMCP
from starlette.responses import JSONResponse

mcp = FastMCP(host="0.0.0.0", stateless_http=True)

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers together"""
    return a * b

@mcp.tool()
def greet_user(name: str) -> str:
    """Greet a user by name"""
    return f"Hello, {name}! Nice to meet you."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

### Understanding the code

- **FastMCP**: Creates an MCP server that can
  host your tools
- **@mcp.tool()**: Decorator that turns your
  Python functions into MCP tools
- **Tools**: Three simple tools that
  demonstrate different types of operations

## Step 2: Test your MCP server locally

### Start your MCP server

Run your MCP server locally:

```
python my_mcp_server.py
```

You should see output indicating the server is running on port
`8000`.

### Test with MCP client

From a new terminal, create a new file `my_mcp_client.py` and
execute it using `python my_mcp_client.py`

```
# my_mcp_client.py

import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    mcp_url = "http://localhost:8000/mcp"
    headers = {}

    async with streamablehttp_client(mcp_url, headers, timeout=120, terminate_on_close=False) as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tool_result = await session.list_tools()
            print(tool_result)

asyncio.run(main())
```

You can also test your server using the MCP Inspector as described in [Local testing with MCP inspector](#runtime-mcp-appendix-b "#runtime-mcp-appendix-b").

## Step 3: Deploy your MCP server to AWS

### Install deployment

tools

Install the AgentCore starter toolkit:

```
pip install bedrock-agentcore-starter-toolkit
```

You use the starter toolkit to deploy your agent to AgentCore Runtime.

Create a project folder with the following structure:

```
## Project Folder Structure

your_project_directory/
├── mcp_server.py # Your main agent code
├── requirements.txt # Dependencies for your agent
└── __init__.py # Makes the directory a Python package
```

Create a new file called `requirements.txt`, add the following
to it:

```
mcp
```

`requirements.txt` specifies the requirements that the agent needs for deployment to AgentCore Runtime.

### Configure your MCP server for

deployment

Before configuring your deployment, you need to set up a Cognito user pool for
authentication as described in [Set up Cognito user pool for
authentication](#runtime-mcp-appendix-a "#runtime-mcp-appendix-a"). This
provides the OAuth tokens required for secure access to your deployed server.

###### Service-Linked Role for Authentication

Starting **October 7, 2025**, Amazon Bedrock AgentCore uses a Service-Linked Role for workload identity permissions when using OAuth authentication. For detailed information about this change, see [Identity service-linked role](service-linked-roles.md#identity-service-linked-role "service-linked-roles.md#identity-service-linked-role").

After setting up authentication, create the deployment configuration:

```
agentcore configure -e my_mcp_server.py --protocol MCP
```

This will start a guided prompt workflow:

- For execution role, you need to have an IAM execution role with
  appropriate permissions
- For ECR, just press `enter` to skip and it will
  auto-create
- For dependency file, the CLI will auto-detect from current
  directory
- For OAuth, type `yes` and provide the discovery URL
  and client ID token

### Deploy to AWS

Deploy your agent:

```
agentcore launch
```

This command will:

1. Build a Docker container with your agent
2. Push it to Amazon ECR
3. Create a Amazon Bedrock AgentCore runtime
4. Deploy your agent to AWS

After deployment, you'll receive an agent runtime ARN that looks like:

```
arn:aws:bedrock-agentcore:us-west-2:`accountId`:runtime/my_mcp_server-xyz123
```

## Step 4: Invoke your deployed MCP server

### Test with MCP client (remote)

Before testing, set the following environment variables:

- Export agent ARN as an environment variable: `export
AGENT_ARN="`agent_arn`"`
- Export bearer token as an environment variable: `export
BEARER_TOKEN="`bearer_token`"`

if you pass in an `Accept` header, it must follow the [MCP](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#sending-messages-to-the-server "https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#sending-messages-to-the-server") standard. Acceptable media types are `application/json` and `text/event-stream`.

Create a new file `my_mcp_client_remote.py` and execute it
using `python my_mcp_client_remote.py`

```
import asyncio
import os
import sys

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    agent_arn = os.getenv('AGENT_ARN')
    bearer_token = os.getenv('BEARER_TOKEN')
    if not agent_arn or not bearer_token:
        print("Error: AGENT_ARN or BEARER_TOKEN environment variable is not set")
        sys.exit(1)

    encoded_arn = agent_arn.replace(':', '%3A').replace('/', '%2F')
    mcp_url = f"https://bedrock-agentcore.us-west-2.amazonaws.com/runtimes/{encoded_arn}/invocations?qualifier=DEFAULT"
    headers = {"authorization": f"Bearer {bearer_token}","Content-Type":"application/json"}
    print(f"Invoking: {mcp_url}, \nwith headers: {headers}\n")

    async with streamablehttp_client(mcp_url, headers, timeout=120, terminate_on_close=False) as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tool_result = await session.list_tools()
            print(tool_result)

asyncio.run(main())
```

You can also test your deployed server using the MCP Inspector as described in
[Remote testing with MCP inspector](#runtime-mcp-appendix-c "#runtime-mcp-appendix-c").

## Appendix

### Set up Cognito user pool for

authentication

Create a new file `setup_cognito.sh` and add the following
content.

```
#!/bin/bash

# Create User Pool and capture Pool ID directly
export POOL_ID=$(aws cognito-idp create-user-pool \
  --pool-name "MyUserPool" \
  --policies '{"PasswordPolicy":{"MinimumLength":8}}' \
  --region $REGION | jq -r '.UserPool.Id')

# Create App Client and capture Client ID directly
export CLIENT_ID=$(aws cognito-idp create-user-pool-client \
  --user-pool-id $POOL_ID \
  --client-name "MyClient" \
  --no-generate-secret \
  --explicit-auth-flows "ALLOW_USER_PASSWORD_AUTH" "ALLOW_REFRESH_TOKEN_AUTH" \
  --region $REGION | jq -r '.UserPoolClient.ClientId')

# Create User
aws cognito-idp admin-create-user \
  --user-pool-id $POOL_ID \
  --username $USERNAME \
  --region $REGION \
  --message-action SUPPRESS > /dev/null

# Set Permanent Password
aws cognito-idp admin-set-user-password \
  --user-pool-id $POOL_ID \
  --username $USERNAME \
  --password $PASSWORD \
  --region $REGION \
  --permanent > /dev/null

# Authenticate User and capture Access Token
export BEARER_TOKEN=$(aws cognito-idp initiate-auth \
  --client-id "$CLIENT_ID" \
  --auth-flow USER_PASSWORD_AUTH \
  --auth-parameters USERNAME=$USERNAME,PASSWORD=$PASSWORD \
  --region $REGION | jq -r '.AuthenticationResult.AccessToken')

# Output the required values
echo "Pool id: $POOL_ID"
echo "Discovery URL: https://cognito-idp.$REGION.amazonaws.com/$POOL_ID/.well-known/openid-configuration"
echo "Client ID: $CLIENT_ID"
echo "Bearer Token: $BEARER_TOKEN"
```

Open a terminal window and set the following environment variables:

- `REGION` – the AWS Region that you want to use
- `USERNAME` – the user name for the new user
- `PASSWORD` – the password for the new user

```
export REGION=`us-east-1` // set your desired Region
export USERNAME=`USER NAME`
export PASSWORD=`PASSWORD`
```

Run the script using the command `source
 setup_cognito.sh`.

###### Note

For detailed OAuth authentication setup and Service-Linked Role information, see [Authenticate and authorize with Inbound Auth and Outbound Auth](runtime-oauth.md "runtime-oauth.md").

After running this script, note the following values for use in the deployment
configuration:

- Discovery URL: Used during the `agentcore configure`
  step
- Client ID: Used during the `agentcore configure` step
- Bearer Token: Used when invoking your deployed server

### Local testing with MCP inspector

The MCP Inspector is a visual tool for testing MCP servers. To use it, you
need:

- Node.js and npm installed

Install and run the MCP Inspector:

```
npx @modelcontextprotocol/inspector
```

This will:

- Start the MCP Inspector server
- Display a URL in your terminal (typically
  `http://localhost:6274`)

To use the Inspector:

1. Navigate to `http://localhost:6274` in your browser
2. Paste the MCP server URL (`http://localhost:8000/mcp`) into the
   MCP Inspector connection field
3. You'll see your tools listed in the sidebar
4. Click on any tool to test it
5. Fill in the parameters (e.g., for `add_numbers`, enter values
   for `a` and `b`)
6. Click "Call Tool" to see the result

### Remote testing with MCP inspector

You can also test your deployed server using the MCP Inspector:

1. Open the MCP Inspector: `npx
@modelcontextprotocol/inspector`
2. In the web interface:
   - Select "Streamable HTTP" as the transport
   - Enter your agent's endpoint URL, which will look like:
     `https://bedrock-agentcore.us-west-2.amazonaws.com/runtimes/arn%3Aaws%3Abedrock-agentcore%3Aus-west-2%3A`accountId`%3Aruntime%2F`runtimeName`/invocations?qualifier=DEFAULT`
   - Make sure to URL-encode your agent runtime ARN when constructing
     the endpoint URL. The colon (:) characters become %3A and forward
     slashes (/) become %2F in the encoded URL.
   - Add your Bearer token under authentication
   - Click "Connect"

3. Test your tools just like you did locally
