

# Get started providing agents with access to WorkSpaces Applications
<a name="getting-started-agent-access"></a>

To enable AI agents to operate desktop applications through Amazon WorkSpaces Applications, you create a stack with access enabled for agents, generate a streaming URL, and connect your agent to the managed MCP service.

If you are setting up agent access for the first time, you can use the Build Your First Agent quick-start experience. You can also follow the steps in this topic to configure agent access manually. The quick-start experience is available in the GitHub repository — [sample-code-for-workspaces-agent-access](https://github.com/aws-samples/sample-code-for-workspaces-agent-access).

This tutorial takes approximately 15 minutes to complete.

**Important**  
The resources you create in this tutorial might result in charges to your AWS account. Delete the stack and stop the fleet when you are done to avoid ongoing charges.

In this tutorial, you complete the following tasks:
+ Step 1: Create a stack with agent access enabled
+ Step 2: Generate a streaming URL
+ Step 3: Connect your agent to the MCP service
+ Step 4: Verify agent activity
+ Step 5: Clean up resources

## Prerequisites
<a name="getting-started-agent-access-prereqs"></a>

Before you begin, make sure you have the following:
+ An active Amazon WorkSpaces Applications fleet. If you haven't set one up yet, see [Get Started with Amazon WorkSpaces Applications: Set Up With Sample Applications](getting-started.md).
+ AWS credentials (environment variables, AWS profile, EC2 instance role, or Lambda execution role) with the following IAM permissions. The agent uses these credentials directly to sign requests to the MCP service:

  ```
  {
      "Sid": "MCP",
      "Effect": "Allow",
      "Action": ["agentaccess-mcp:*"],
      "Resource": "*"
  },
  {
      "Sid": "AppStream",
      "Effect": "Allow",
      "Action": ["appstream:CreateStreamingURL", "appstream:DescribeFleets"],
      "Resource": "*"
  }
  ```

  The `agentaccess-mcp:*` wildcard includes the following actions:
  + `agentaccess-mcp:InvokeMcp` — Initialize sessions and discover tools
  + `agentaccess-mcp:GetScreenshot` — Capture screen state
  + `agentaccess-mcp:LeftClick` — Perform left mouse click
  + `agentaccess-mcp:DoubleClick` — Perform double click
  + `agentaccess-mcp:TripleClick` — Perform triple click
  + `agentaccess-mcp:RightClick` — Perform right mouse click
  + `agentaccess-mcp:MiddleClick` — Perform middle mouse click
  + `agentaccess-mcp:TypeText` — Type text string
  + `agentaccess-mcp:KeyPress` — Press key or key combination
  + `agentaccess-mcp:HoldKey` — Hold key for duration
  + `agentaccess-mcp:Scroll` — Scroll at coordinates
  + `agentaccess-mcp:MovePointer` — Move pointer to coordinates
  + `agentaccess-mcp:LeftClickDrag` — Perform left click drag
  + `agentaccess-mcp:LeftMouseDown` — Press and hold left mouse button
  + `agentaccess-mcp:LeftMouseUp` — Release left mouse button
  + `agentaccess-mcp:CheckConnectionStatus` — Check connection status of a streaming session
  + `agentaccess-mcp:CallForwardedTool` — Invoke a forwarded tool on a remote instance
+ An MCP-compatible agent framework. The agent must be able to make SigV4-signed Streamable HTTP requests to the MCP endpoint. The [Strands Agents SDK](https://strandsagents.com/docs/user-guide/concepts/tools/mcp-tools/) provides native MCP client support, or you can use any framework with the mcp-proxy-for-aws transport.
+ Python 3.10 or later. No specific operating system is required.

## Step 1: Create a stack with agent access enabled
<a name="getting-started-agent-access-create-stack"></a>

Create a WorkSpaces Applications stack with agent access enabled to allow AI agents to interact with desktop applications.

### Using the AWS Management Console
<a name="getting-started-agent-access-create-stack-console"></a>

**To create a stack with agent access**

1. Open the [WorkSpaces Applications console](https://console.aws.amazon.com/appstream2/home).

1. In the left navigation pane, choose **Stacks**, then choose **Create Stack**.

1. On the **Stack details** page (step 1 of 4), under **AI agent access**, select **Enable AI agent access**. Choose **Next**.

1. On the **Enable storage** page (step 2 of 4), optionally enable **Home folders** to allow your agent to save files to an Amazon S3 bucket in your AWS account. The fleet associated with this stack must allow access to Amazon S3 through the internet or a Amazon VPC endpoint for Amazon S3. Choose **Next**.

1. On the **Edit agent settings** page (step 3 of 4), configure the following:
   + **Enable computer input** — Allow agents to choose buttons, enter text, and scroll on the desktop. If you enable computer input, you must also enable computer vision.
   + **Enable computer vision** — Allow agents to see the desktop.
   + **Screenshot storage** — Configure where agent screenshots are stored during streaming sessions. If enabled, provide an Amazon S3 bucket that you have permissions to write to.
   + **Screen resolution** — Select the display resolution for the agent streaming environment (1280x720).
   + **Screen image type** — Select the image format for agent screen captures (PNG or JPEG).
   + **Application settings persistence** — Optionally enable this to save your agent's application customizations and Windows settings between sessions. Settings are saved to an Amazon S3 bucket in your AWS account.
   + **Enable MCP tool forwarding** — Allow agents to interact with applications and the desktop operating system through direct MCP calls rather than using computer use tools. When enabled, MCP tools configured on the WorkSpaces application session are forwarded to the agent.
   + **Enable user control mode** — Allow users to observe agent sessions in real time through their browser. Observers see a live view of the desktop as the agent works. In VIEW\_STOP mode, observers can stop the agent using a button at the top of the screen. Once stopped, the agent must start a new session to resume.
**Note**  
You must enable at least one of computer input or computer vision.

   Choose **Next**.

1. On the **Review and Create** page (step 4 of 4), review your settings and choose **Create Stack**.

### Using the AWS CLI
<a name="getting-started-agent-access-create-stack-cli"></a>

Run the following command to create a stack with agent access enabled:

```
aws appstream create-stack \
    --name {{your-stack-name}} \
    --agent-access-config '{
        "Settings": [
            {"AgentAction": "COMPUTER_VISION", "Permission": "ENABLED"},
            {"AgentAction": "COMPUTER_INPUT", "Permission": "ENABLED"},
            {"AgentAction": "FORWARD_MCP_TOOLS", "Permission": "ENABLED"}
        ],
        "ScreenResolution": "W_1280xH_720",
        "ScreenImageFormat": "PNG"
    }'
```

To also enable screenshot storage, add the `S3BucketArn` and `ScreenshotsUploadEnabled` parameters:

```
aws appstream create-stack \
    --name {{your-stack-name}} \
    --agent-access-config '{
        "Settings": [
            {"AgentAction": "COMPUTER_VISION", "Permission": "ENABLED"},
            {"AgentAction": "COMPUTER_INPUT", "Permission": "ENABLED"},
            {"AgentAction": "FORWARD_MCP_TOOLS", "Permission": "ENABLED"}
        ],
        "ScreenResolution": "W_1280xH_720",
        "ScreenImageFormat": "PNG",
        "S3BucketArn": "{{arn:aws:s3:::your-bucket-name}}",
        "ScreenshotsUploadEnabled": true
    }'
```

After you create the stack, associate it with a fleet. Agents cannot connect to a stack that does not have an associated fleet.

```
aws appstream associate-fleet \
    --stack-name {{your-stack-name}} \
    --fleet-name {{your-fleet-name}}
```

## Step 2: Generate a streaming URL
<a name="getting-started-agent-access-streaming-url"></a>

Create a streaming URL using the standard WorkSpaces Applications `CreateStreamingURL` API. You don't need agent-specific parameters. The stack's agent access configuration determines the agent-specific behavior.

### Using the AWS Management Console
<a name="getting-started-agent-access-streaming-url-console"></a>

**To generate a streaming URL using the console**

1. Open the [WorkSpaces Applications console](https://console.aws.amazon.com/appstream2/home).

1. In the left navigation pane, choose **Stacks**, then choose the stack you created with agent access enabled.

1. Choose the **Actions** button, and in the dropdown, select **Create Streaming URL**. Your stack must be selected for this option to be available.

1. In the **UserID** section, enter a user. You can enter `TestUser` if you are testing.

1. In the **URL expiration** section, select the time you want the URL to be valid. A shorter time is recommended. 30 minutes is the default and recommended for testing.

1. Choose **GetURL** and copy the URL generated.

### Using the AWS CLI
<a name="getting-started-agent-access-streaming-url-cli"></a>

Run the following command to generate a streaming URL:

```
aws appstream create-streaming-url \
    --stack-name {{your-stack-name}} \
    --fleet-name {{your-fleet-name}} \
    --user-id {{your-agent-id}} \
    --validity 3600
```

The response includes a `StreamingURL` that you pass to your agent in the next step. The URL is valid for the duration specified by the `--validity` parameter.

**Note**  
At any given time, only one agent can connect to a unique session. Named users, specified through the `UserId` parameter, can have only one active session per fleet at a time. To run multiple agents concurrently, each agent must connect to its own unique session.

## Step 3: Connect your agent to the MCP service
<a name="getting-started-agent-access-connect"></a>

Your agent connects to the managed MCP service at the following fixed endpoint:

`https://agentaccess-mcp.{{region}}.api.aws/mcp`

The connection uses SigV4 signing with the service name `agentaccess-mcp`. Your agent signs each request using the AWS credentials configured in the prerequisites with the `agentaccess-mcp:*` permissions. You pass the streaming URL from Step 2 as a header on every MCP request.

The following example shows how to establish the connection using mcp-proxy-for-aws:

```
aws_iam_streamablehttp_client(
    endpoint="https://agentaccess-mcp.{{region}}.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region="{{region}}",
    headers={
        "X-Amzn-AgentAccess-Streaming-Session-Url": streaming_url,
    },
)
```

After the agent connects, it can use the MCP tools to enter text, choose buttons, and take screenshots of the desktop.

## Step 4: Verify agent activity
<a name="getting-started-agent-access-verify"></a>

You can verify agent activity using the following AWS services:
+ **AWS CloudTrail** — AWS CloudTrail logs agent session events. Open the AWS CloudTrail console to view agent activity.
+ **CloudWatch** — CloudWatch provides operational metrics for agent sessions. Open the CloudWatch console to view metrics.
+ **Amazon S3** — If you enabled screenshot storage, Amazon S3 stores the screenshots in the bucket you specified during stack configuration.

## Step 5: Clean up resources
<a name="getting-started-agent-access-cleanup"></a>

To avoid ongoing charges, delete the stack you created in this tutorial. You must stop the fleet and disassociate it from the stack before you can delete the stack. Optionally, you can also delete the fleet.

### Using the AWS Management Console
<a name="getting-started-agent-access-cleanup-console"></a>

**To clean up resources**

1. Open the [WorkSpaces Applications console](https://console.aws.amazon.com/appstream2/home).

1. In the left navigation pane, choose **Fleets**.

1. Select the fleet associated with the stack. Choose **Actions**, **Stop**. Wait for the fleet to stop.

1. In the left navigation pane, choose **Stacks**.

1. Select the stack you created, and choose **Actions**, **Disassociate Fleet**.

1. With the stack still selected, choose **Actions**, **Delete**.

1. (Optional) To delete the fleet, in the left navigation pane, choose **Fleets**. Select the fleet and choose **Actions**, **Delete**.

### Using the AWS CLI
<a name="getting-started-agent-access-cleanup-cli"></a>

Run the following commands to clean up resources:

```
aws appstream stop-fleet \
    --name {{your-fleet-name}}

aws appstream disassociate-fleet \
    --stack-name {{your-stack-name}} \
    --fleet-name {{your-fleet-name}}

aws appstream delete-stack \
    --name {{your-stack-name}}
```

(Optional) To also delete the fleet after it has stopped:

```
aws appstream delete-fleet \
    --name {{your-fleet-name}}
```