# Get started with AgentCore Browser

AgentCore Browser enables your agents to interact with web pages through a managed Chrome browser.
The agent can navigate websites, search for information, extract content, and interact with
web elements in a secure, managed environment.

This page covers the prerequisites and helps you get started using _AWS
Strands_. Strands provides a high-level agent framework that simplifies building
AI agents with built-in tool integration, conversation management, and automatic session
handling.

###### Topics

- [Prerequisites](#browser-prerequisites "#browser-prerequisites")
- [Using AgentCore Browser via AWS Strands](#browser-using-strands "#browser-using-strands")
- [Find your resources](#browser-find-resources "#browser-find-resources")
- [Next steps](#browser-next-steps "#browser-next-steps")

## Prerequisites

Before you start, ensure you have:

- AWS account with credentials configured. See [Configuring your credentials](#browser-credentials-config "#browser-credentials-config").
- Python 3.10+ installed
- Boto3 installed. See [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html").
- IAM execution role with the required permissions. See [Configuring your credentials](#browser-credentials-config "#browser-credentials-config").
- Model access: Anthropic Claude Sonnet 4.0 [enabled](../../../bedrock/latest/userguide/model-access-modify.md "../../../bedrock/latest/userguide/model-access-modify.md") in the Amazon Bedrock console. For information about using a different model
  with the Strands Agents see the _Model Providers_ section in the
  [Strands Agents SDK
  documentation](https://strandsagents.com/latest/documentation/docs/ "https://strandsagents.com/latest/documentation/docs/").
- AWS Region where Amazon Bedrock AgentCore is available. See [AWS Regions](agentcore-regions.md "agentcore-regions.md").
- Your network allows secure WebSocket connections

### Configuring your credentials

Perform the following steps to configure your AWS credentials and attach the
required permissions to use AgentCore Browser.

1. ###### Verify your AWS credentials

Confirm your AWS credentials are configured:

```
aws sts get-caller-identity
```

Take note of the user or credentials returned here, as you'll be attaching
permissions to this identity in the next step.

If this command fails, configure your credentials. For more information, see
[Configuration and credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") in the AWS CLI
documentation. 2. ###### Attach required permissions

Your IAM user or role needs permissions to use AgentCore Browser. Attach this policy to
your IAM identity:

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

**To attach this policy**:

    * Navigate to the IAM Console
    * Find your user or role (the one returned by `aws sts
     get-caller-identity`)
    * Click **Add permissions** → **Create inline policy**
    * Switch to JSON view and paste the policy above
    * Name it `AgentCoreBrowserAccess` and save

###### Note

Replace `<Region>` with your actual AWS Region and
`<account_id>` with your AWS account ID. 3. ###### Verify your setup

Confirm your setup is correct by checking:

    * Your AWS credentials are properly configured
    * The IAM policy is attached to your user or role
    * Model access is enabled in the Amazon Bedrock console

The following sections show you how to use the Amazon Bedrock AgentCore Browser with and without the agent
framework. Using the Browser directly without an agent framework is especially useful when you
want to execute specific browser automation tasks programmatically.

## Using AgentCore Browser via AWS Strands

The following sections show you how to use the Amazon Bedrock AgentCore Browser with the Strands SDK.
Before you go through the examples in this section, see [Prerequisites](#browser-prerequisites "#browser-prerequisites").

###### Topics

- [Step 1: Install dependencies](#browser-strands-install "#browser-strands-install")
- [Step 2: Create your agent with AgentCore Browser](#browser-strands-create "#browser-strands-create")
- [Step 3: Run the agent](#browser-strands-run "#browser-strands-run")
- [Step 4: View the browser session live](#browser-strands-live-view "#browser-strands-live-view")

### Step 1: Install dependencies

Create a project folder and install the required packages:

###### Note

On Windows, use: `.venv\Scripts\activate`

```
mkdir agentcore-browser-quickstart
cd agentcore-browser-quickstart
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

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

### Step 2: Create your agent with AgentCore Browser

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

### Step 3: Run the agent

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

### Step 4: View the browser session live

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

This example:

- Creates a browser session using the browser_session client
- Retrieve the WebSocket connection details required for automation and live
  view.
- Start the viewer server, which launches a browser window to display the remote browser
  session via Live View.
- Connect Playwright to the remote browser via automation endpoint and navigate to
  Amazon.com.
- Keep the session alive until manually interrupted.
- Handle cleanup gracefully by terminating the session and releasing resources when the
  program exits.
  The BrowserViewerServer component provides a local web server that connects to the remote
  browser session and displays it in a browser window, allowing you to see and interact with the
  browser in real-time.

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
- [Use cases](browser-tool.md#browser-use-cases "browser-tool.md#browser-use-cases") - See
  real-world implementation examples
- [Resource and session management](browser-resource-session-management.md "browser-resource-session-management.md") - Learn about API operations and
  custom browsers
