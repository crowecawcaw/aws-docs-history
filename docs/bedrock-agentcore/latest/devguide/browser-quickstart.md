

# Get started with AgentCore Browser
<a name="browser-quickstart"></a>

AgentCore Browser enables your agents to interact with web pages through a managed Chrome browser. In this guide, you’ll create an AI agent that navigates a website and extracts information — in under 5 minutes.

**Topics**
+ [Prerequisites](#browser-prerequisites)
+ [Step 1: Install dependencies](#browser-strands-install)
+ [Step 2: Create your agent](#browser-strands-create)
+ [Step 3: Run the agent](#browser-strands-run)
+ [Step 4: View the browser session live](#browser-strands-live-view)
+ [Find your resources](#browser-find-resources)
+ [Next steps](#browser-next-steps)
+ [Using AgentCore Browser with Nova Act](browser-quickstart-nova-act.md)
+ [Using AgentCore Browser with Playwright](browser-quickstart-playwright.md)

## Prerequisites
<a name="browser-prerequisites"></a>

Before you start, ensure you have:
+ Python 3.10 or newer ( [python.org/downloads](https://www.python.org/downloads/) )
+ Boto3 installed ( [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) )
+  AWS credentials configured — verify with:

  ```
  aws sts get-caller-identity
  ```

  If this command fails, see [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) in the AWS CLI documentation.
+ Anthropic Claude Sonnet 4.0 model access [enabled](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-modify.html) in the Amazon Bedrock console
+  AWS Region where Amazon Bedrock AgentCore is available (see [Supported AWS Regions](agentcore-regions.md) )

 **IAM permissions** 

Attach this policy to your IAM identity. In the IAM Console, find your user or role, choose **Add permissions** > **Create inline policy** , switch to JSON view, and paste:

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
            "Resource": "arn:aws:bedrock-agentcore:<Region>:++<account_id>++:browser/*"
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

**Note**  
Replace `<Region>` with your actual AWS Region and `<account_id>` with your AWS account ID.

## Step 1: Install dependencies
<a name="browser-strands-install"></a>

```
pip install bedrock-agentcore strands-agents strands-agents-tools playwright nest-asyncio
```

## Step 2: Create your agent
<a name="browser-strands-create"></a>

Create a file named `browser_agent.py` :

**Note**  
Replace `<Region>` with your AWS Region (for example, `us-west-2` ).

```
from strands import Agent
from strands_tools.browser import AgentCoreBrowser

# Initialize the Browser tool
browser_tool = AgentCoreBrowser(region="<Region>")

# Create an agent with the Browser tool
agent = Agent(tools=[browser_tool.browser])

# Test the agent with a web search prompt
prompt = "what are the services offered by Bedrock AgentCore? Use the documentation link if needed: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html"
print(f"\n\nPrompt: {prompt}\n\n")

response = agent(prompt)
print("\n\nAgent Response:")
print(response.message["content"][0]["text"])
```

## Step 3: Run the agent
<a name="browser-strands-run"></a>

```
python browser_agent.py
```

You should see the agent navigate the website and return details about AgentCore services. If you encounter errors, verify your IAM permissions, model access, and AWS credentials.

## Step 4: View the browser session live
<a name="browser-strands-live-view"></a>

While your agent is running, you can watch it in real-time through the AWS Console:

1. Open the [AgentCore Browser Console](https://us-west-2.console.aws.amazon.com/bedrock-agentcore/builtInTools) 

1. Navigate to **Built-in tools** in the left navigation

1. Select the Browser tool (for example, `AgentCore Browser Tool` , or your custom browser)

1. In the **Browser sessions** section, find your active session with status **Ready** 

1. In the **Live view / recording** column, click the provided "View live session" URL

The live view provides a real-time video stream with interactive controls to take over or release control from automation.

## Find your resources
<a name="browser-find-resources"></a>

After using AgentCore Browser, view your resources in the AWS Console:


| \# | Resource | Location | 
| --- | --- | --- | 
| 1 | Live View | Browser Console > Tool Name > **View live session**  | 
| 2 | Session Recordings and Replay | Browser Console > Tool Name > **View recording**  | 
| 3 | Browser Logs |  **CloudWatch** > **Log groups** > `/aws/bedrock-agentcore/browser/`  | 
| 4 | Recording Files |  **S3** > Your bucket > `browser-recordings/` prefix | 
| 5 | Custom Browsers |  **AgentCore Console** > **Built-in tools** > Your custom browser | 
| 6 | IAM Roles |  **IAM** > **Roles** > Search for your execution role | 

## Next steps
<a name="browser-next-steps"></a>

Now that you have AgentCore Browser working, explore these advanced features:
+  [Session Recording and Replay](browser-session-recording.md) - Record and replay sessions for debugging
+  [Using AgentCore Browser with Nova Act](browser-quickstart-nova-act.md) and [Using AgentCore Browser with Playwright](browser-quickstart-playwright.md) - Use other frameworks like Nova Act or Playwright
+  [Fundamentals](browser-resource-session-management.md) - Learn about API operations and custom browsers