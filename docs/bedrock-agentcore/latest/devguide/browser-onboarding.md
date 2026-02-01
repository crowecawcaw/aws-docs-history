# Get started with AgentCore Browser

AgentCore Browser enables your agents to interact with web pages through a managed Chrome browser.
The agent can navigate websites, search for information, extract content, and interact with
web elements in a secure, managed environment.

This page covers the prerequisites and helps you get started using _AWS
Strands_. Strands provides a high-level agent framework that simplifies building
AI agents with built-in tool integration, conversation management, and automatic session
handling.

###### Topics

- [Step 0:Prerequisites](#browser-prerequisites "#browser-prerequisites")
- [Step 1: Install dependencies](#browser-strands-install "#browser-strands-install")
- [Step 2: Create your agent with AgentCore Browser](#browser-strands-create "#browser-strands-create")
- [Step 3: Run the agent](#browser-strands-run "#browser-strands-run")
- [Step 4: View the browser session live](#browser-strands-live-view "#browser-strands-live-view")
- [Find your resources](#browser-find-resources "#browser-find-resources")
- [Next steps](#browser-next-steps "#browser-next-steps")

## Step 0:Prerequisites

Before you start, ensure you have:

- Python version 3.10 or newer. You can check your version using the below command. If you need to update Python, visit [python.org/downloads](python.org/downloads.md "python.org/downloads.md").

```
python3 --version
```

- Boto3 installed. See [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html").
- Model access: Anthropic Claude Sonnet 4.0 [enabled](../../../bedrock/latest/userguide/model-access-modify.md "../../../bedrock/latest/userguide/model-access-modify.md") in the Amazon Bedrock console. For information about using a different model
  with the Strands Agents see the _Model Providers_ section in the
  [Strands Agents SDK
  documentation](https://strandsagents.com/latest/documentation/docs/ "https://strandsagents.com/latest/documentation/docs/").
- AWS Region where Amazon Bedrock AgentCore is available. See [Supported AWS Regions](agentcore-regions.md "agentcore-regions.md").
- Your network allows secure WebSocket connections
- Verify your AWS account using the below command. Take note of the user or credentials returned, as you'll be attaching
  permissions to this identity in the next step. If this command fails, configure your credentials. For more information, see
  [Configuration and credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") in the AWS CLI
  documentation.

```
aws sts get-caller-identity
```

- Attach IAM execution role with the required permissions. Attach this policy to
  your IAM identity. To attach this policy in Console: Navigate to the IAM Console, Find your user or role (the one returned in previous step), Click Add permissions → Create inline policy, Switch to JSON view and paste the policy above, Name it AgentCoreBrowserAccess , and Save.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "BedrockAgentCoreBrowserFullAccess",
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:CreateBrowser",
                "bedrock-agentcore:ListBrowsers",
                "bedrock-agentcore:GetBrowser",
                "bedrock-agentcore:DeleteBrowser",
                "bedrock-agentcore:StartBrowserSession",
                "bedrock-agentcore:ListBrowserSessions",
                "bedrock-agentcore:GetBrowserSession",
                "bedrock-agentcore:StopBrowserSession",
                "bedrock-agentcore:UpdateBrowserStream",
                "bedrock-agentcore:ConnectBrowserAutomationStream",
                "bedrock-agentcore:ConnectBrowserLiveViewStream"
            ],
            "Resource": "arn:aws:bedrock-agentcore:<Region>:<account_id>:browser/*"
        },
        {
            "Sid": "BedrockModelAccess",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

###### Note

Replace `<Region>` with your actual AWS Region and
`<account_id>` with your AWS account ID.

## Step 1: Install dependencies

Before you start, make sure you have installed the required packages:

```
pip install bedrock-agentcore strands-agents strands-agents-tools playwright nest-asyncio
```

These packages provide:

- `bedrock-agentcore`: The SDK for Amazon Bedrock AgentCore tools including
  AgentCore Browser
- `strands-agents`: The Strands agent framework
- `strands-agents-tools`: The tools that the Strands agent framework
  offers including Browser tool
- `playwright`: Python library for browser automation. Strands uses
  playwright for browser automation
- `nest-asyncio`: Allows running asyncio event loops within existing
  event loops

If you face issues with pip install , review the instructions [here](https://packaging.python.org/en/latest/tutorials/installing-packages/ "https://packaging.python.org/en/latest/tutorials/installing-packages/"). Amazon Bedrock AgentCore requires requires Python version 3.10 or
newer.

## Step 2: Create your agent with AgentCore Browser

Create a file named `browser_agent.py` and add the following code:

###### Note

Replace `<Region>` with your actual AWS Region (for example,
`us-west-2` or `us-east-1`).

```
from strands import Agent
from strands_tools.browser import AgentCoreBrowser

# Initialize the Browser tool
browser_tool = AgentCoreBrowser(region="<Region>")

# Create an agent with the Browser tool
agent = Agent(tools=[browser_tool.browser])

# Test the agent with a web search prompt
prompt = "what are the services offered by Bedrock AgentCore? Use the documentation link if needed: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html"
print(f"\\n\\nPrompt: {prompt}\\n\\n")

response = agent(prompt)
print("\\n\\nAgent Response:")
print(response.message["content"][0]["text"])

```

This code:

- Initializes the Browser tool for your region
- Creates an agent that can use the browser to interact with websites
- Sends a prompt asking the agent to search AgentCore documentation and answer
  question
- Prints the agent's response with the information found

## Step 3: Run the agent

Execute the following command:

```
python browser_agent.py
```

###### Expected output

You should see the agent's response containing details about AgentCore services from
the documentation. The agent navigates the website and extracts the requested
information.

If you encounter errors, verify:

- Your IAM role/user has the correct permissions
- You have model access enabled in the Amazon Bedrock console
- Your AWS credentials are properly configured

## Step 4: View the browser session live

While your browser script is running, you can view the session in real-time through
the AWS Console:

1. Open the [AgentCore Browser Console](https://us-west-2.console.aws.amazon.com/bedrock-agentcore/builtInTools "https://us-west-2.console.aws.amazon.com/bedrock-agentcore/builtInTools")
2. Navigate to **Built-in tools** in the left
   navigation
3. Select the Browser tool (for example, `AgentCore Browser Tool`, or your
   custom browser)
4. In the **Browser sessions** section, find your active
   session with status **Ready**
5. In the **Live view / recording** column, click the
   provided "View live session" URL
6. The live view opens in a new browser window, displaying the real-time browser
   session

The live view interface provides:

- Real-time video stream of the browser session
- Interactive controls to take over or release control from automation
- Ability to terminate the session

## Find your resources

After using AgentCore Browser, view your resources in the AWS Console:

| #   | Resource           | Location                                                                         |
| --- | ------------------ | -------------------------------------------------------------------------------- |
| 1   | Live View          | Browser Console > Tool Name > **View live<br>session**                           |
| 2   | Session Recordings | Browser Console > Tool Name > **View recording**                                 |
| 3   | Browser Logs       | **CloudWatch\*<br>• > **Log groups\*<br>• ><br>`/aws/bedrock-agentcore/browser/` |
| 4   | Recording Files    | \*_S3_<br>• > Your bucket > `browser-recordings/`<br>prefix                      |
| 5   | Custom Browsers    | **AgentCore Console\*<br>• > **Built-in<br>tools\*<br>• > Your custom browser    |
| 6   | IAM Roles          | **IAM\*<br>• > **Roles\*<br>• > Search for<br>your execution role                |

## Next steps

Now that you have AgentCore Browser working, explore these advanced features:

- [Browser session recording and replay](browser-session-replay.md "browser-session-replay.md") -
  Record and replay sessions for debugging
- [Using AgentCore Browser with other Browser libraries and
  tools](browser-building-agents.md "browser-building-agents.md") -
  Use other frameworks like Nova Act or Playwright
- [Resource and session management](browser-resource-session-management.md "browser-resource-session-management.md") - Learn about API operations and
  custom browsers
