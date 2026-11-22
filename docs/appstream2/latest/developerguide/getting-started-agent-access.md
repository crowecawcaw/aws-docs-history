

# Get started providing agents with access to WorkSpaces Applications

To enable AI agents to operate desktop applications through Amazon WorkSpaces Applications, you create a stack with access enabled for agents, generate a streaming URL, and connect your agent to the managed MCP server. You can also enable agent access on an image builder, so that an agent can install and test applications before you create an image.

If you are setting up agent access for the first time, you can use the Build Your First Agent quick-start experience. You can also follow the steps in this topic to configure agent access manually. The quick-start experience is available in the GitHub repository — [sample-code-for-workspaces-agent-access](https://github.com/aws-samples/sample-code-for-workspaces-agent-access).

This tutorial takes approximately 15 minutes to complete.

**Important**  
The resources you create in this tutorial might result in charges to your AWS account. Delete the stack and stop the fleet when you are done to avoid ongoing charges.

In this tutorial, you complete the following tasks:
+ Step 1: Create a stack or image builder with agent access enabled
+ Step 2: Generate a streaming URL
+ Step 3: Connect your agent to the MCP server
+ Step 4: Verify agent activity
+ Step 5: Change agent access settings or disable agent access
+ Step 6: Clean up resources

## Write agent code with the Agent Toolkit for AWS
<a name="getting-started-agent-access-toolkit"></a>

If you build your agent with an AI coding assistant, you can use the [Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/what-is-agent-toolkit.html). It helps you set up agent access and build your first agent.

The toolkit uses the [AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/mcp-server.html). This managed server gives agents safe access to AWS through the Model Context Protocol (MCP). Agents can run AWS CLI commands, search AWS docs, and follow ready-made skills. They connect through one secure endpoint. You also get CloudWatch metrics and IAM access controls. To set up the server for your agent, see [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html) in the *Agent Toolkit for AWS User Guide*.

The toolkit includes the following skills for WorkSpaces Applications:

`setting-up-workspaces-applications`  
Sets up a WorkSpaces Applications desktop for an AI agent or for people. Your agent asks about your workflow one question at a time. It then recommends image, fleet, and stack settings, and shows you a plan that you can approve to create the resources. It can also build a custom image with an image builder.

`amazon-workspaces-agent-access`  
Connects your agent to the MCP server and helps it operate the desktop, following best practices for agent access. It also helps you fix connection errors. The skill includes three sample workflows that you can run in your own AWS account to see agent access working.

After you set up the AWS MCP Server, your agent can find and load these skills when it needs them. To install the skills for the AI coding agents on your system instead, run the following commands. The `add-skill` command requires AWS CLI version 2.35.0 or later.

```bash
aws agent-toolkit add-skill \
    --skill-name setting-up-workspaces-applications

aws agent-toolkit add-skill \
    --skill-name amazon-workspaces-agent-access
```

To get started, ask your agent "Help me complete the getting started WorkSpaces agent access tutorial".

## Prerequisites
<a name="getting-started-agent-access-prereqs"></a>

Before you begin, review the agent access requirements. For the account, fleet, permissions, and agent prerequisites, see [Prerequisites](agent-access-mcp-prerequisites.md).

## Step 1: Create a stack or image builder with agent access enabled
<a name="getting-started-agent-access-create-stack"></a>

Create a WorkSpaces Applications stack or image builder with agent access enabled to allow AI agents to interact with desktop applications.

### Create a stack using the AWS Management Console
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
   + **Application settings persistence** — Optionally enable this to save your agent's application customizations and Windows settings between sessions. Settings are saved to an Amazon S3 bucket in your AWS account. This setting is available on Windows and is not supported on Linux.
   + **Enable MCP tool forwarding** — Allow agents to interact with applications and the desktop operating system through direct MCP calls rather than using computer use tools. When enabled, MCP tools configured on the WorkSpaces application session are forwarded to the agent. Tool forwarding also requires a configuration file on the image. For the platform-specific path and setup steps, see [Setting up tool forwarding](agent-access-mcp-tool-forwarding-details.md#agent-access-tool-forwarding-setup).
   + **Enable user control mode** — Allow users to observe agent sessions in real time through their browser. Observers see a live view of the desktop as the agent works. In VIEW\_STOP mode, observers can stop the agent using a button at the top of the screen. After the agent stops, it must start a new session to resume.
**Note**  
You must enable at least one of computer input or computer vision.

   Choose **Next**.

1. On the **Review and Create** page (step 4 of 4), review your settings and choose **Create Stack**.

### Create a stack using the AWS CLI
<a name="getting-started-agent-access-create-stack-cli"></a>

Run the following command to create a stack with agent access enabled:

```bash
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

```bash
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

```bash
aws appstream associate-fleet \
    --stack-name {{your-stack-name}} \
    --fleet-name {{your-fleet-name}}
```

### Enable agent access on an image builder using the AWS CLI
<a name="getting-started-agent-access-create-image-builder-cli"></a>

With agent access on an image builder, an agent can install, configure, and test applications on the image builder. You then create an image from the image builder and use that image for the fleet that you associate with your stack. If you don't have an image for your fleet yet, you can complete this step first.

You enable agent access when you create the image builder. Domain-joined image builders aren't supported. For more information, see [Limitations](agent-access-mcp-prerequisites.md#agent-access-limitations).

Run the following command to create an image builder with agent access enabled:

```bash
aws appstream create-image-builder \
    --name {{your-image-builder-name}} \
    --instance-type {{your-instance-type}} \
    --image-name {{your-base-image-name}} \
    --agent-access-config '{
        "Settings": [
            {"AgentAction": "COMPUTER_VISION", "Permission": "ENABLED"},
            {"AgentAction": "COMPUTER_INPUT", "Permission": "ENABLED"},
            {"AgentAction": "FORWARD_MCP_TOOLS", "Permission": "ENABLED"}
        ],
        "ScreenResolution": "W_1280xH_720",
        "ScreenImageFormat": "PNG",
        "UserControlMode": "VIEW_ONLY",
        "ScreenshotsUploadEnabled": false
    }'
```

Instead of `--image-name`, you can specify the base image with `--image-arn`.

The `Settings`, `ScreenResolution`, and `ScreenImageFormat` members are required, and at least one action in `Settings` must be `ENABLED`. `UserControlMode` is optional. For a description of each setting, see [Session behavior](agent-access-mcp-session-behavior.md).

To confirm that agent access is enabled, run the following command. The response includes an `AgentAccessConfig` object with your settings.

```bash
aws appstream describe-image-builders \
    --names {{your-image-builder-name}}
```

## Step 2: Generate a streaming URL
<a name="getting-started-agent-access-streaming-url"></a>

Generate a streaming URL for your stack or image builder. You don't need agent-specific parameters. The stack's or image builder's agent access configuration determines the agent-specific behavior.

### Stack using the AWS Management Console
<a name="getting-started-agent-access-streaming-url-console"></a>

**To generate a streaming URL using the console**

1. Open the [WorkSpaces Applications console](https://console.aws.amazon.com/appstream2/home).

1. In the left navigation pane, choose **Stacks**, then choose the stack you created with agent access enabled.

1. Choose the **Actions** button, and in the dropdown, select **Create Streaming URL**. Your stack must be selected for this option to be available.

1. In the **UserID** section, enter a user. You can enter `TestUser` if you are testing.

1. In the **URL expiration** section, select the time you want the URL to be valid. A shorter time is recommended. The default is 30 minutes, which is recommended for testing.

1. Choose **GetURL** and copy the URL generated.

### Stack using the AWS CLI
<a name="getting-started-agent-access-streaming-url-cli"></a>

Create a streaming URL using the standard WorkSpaces Applications `CreateStreamingURL` API. Run the following command to generate a streaming URL:

```bash
aws appstream create-streaming-url \
    --stack-name {{your-stack-name}} \
    --fleet-name {{your-fleet-name}} \
    --user-id {{your-agent-id}} \
    --validity 3600
```

The response includes a `StreamingURL` that you pass to your agent in the next step. The URL is valid for the duration specified by the `--validity` parameter.

**Note**  
At any given time, only one agent can connect to a unique session. Named users, specified through the `UserId` parameter, can have only one active session per fleet at a time. To run multiple agents concurrently, each agent must connect to its own unique session.

### Image builder using the AWS CLI
<a name="getting-started-agent-access-streaming-url-image-builder-cli"></a>

If you use an image builder, you can generate a streaming URL with the following command. Or you can skip this step and connect with the image builder name. For both options, see [Connecting with image builders](agent-access-mcp-server-endpoint.md#agent-access-mcp-server-connect-image-builder).

```bash
aws appstream create-image-builder-streaming-url \
    --name {{your-image-builder-name}}
```

## Step 3: Connect your agent to the MCP server
<a name="getting-started-agent-access-connect"></a>

Your agent connects to the managed MCP server at the following fixed endpoint:

`https://agentaccess-mcp.{{region}}.api.aws/mcp`

Replace {{region}} with your Region code. For the supported Regions and their endpoints, see [WorkSpaces Applications MCP endpoints](allowed-domains.md#allowed-domains-mcp-endpoints).

The connection uses SigV4 signing with the service name `agentaccess-mcp`. Your agent signs each request using the AWS credentials configured in the prerequisites with the `agentaccess-mcp:*` permissions. You pass the streaming URL from Step 2 as a header on every MCP request.

The following example shows how to establish the connection using mcp-proxy-for-aws:

```python
aws_iam_streamablehttp_client(
    endpoint="https://agentaccess-mcp.{{region}}.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region="{{region}}",
    headers={
        "x-amzn-agentaccess-streaming-session-url": streaming_url,
    },
)
```

After the agent connects, it can use the MCP tools to enter text, choose buttons, and take screenshots of the desktop.

If you connect to an image builder, you must also pass the `x-amzn-agentaccess-local-user` header with the built-in user that the agent logs in as. For the headers and examples, see [Connecting with image builders](agent-access-mcp-server-endpoint.md#agent-access-mcp-server-connect-image-builder).

### Built-in users on image builders
<a name="getting-started-agent-access-built-in-users"></a>

An image builder has three built-in Windows users. The agent works as one of them:
+ `ADMINISTRATOR`: The local administrator. Use this user to install software and create the image.
+ `TEMPLATE_USER`: A standard user whose profile becomes the default profile for your users.
+ `TEST_USER`: A standard user for testing applications.

An image builder doesn't log in a user automatically. The agent chooses the user when it connects, and it can switch to another user with the `switch_user` tool. For more information, see [User tools](agent-access-mcp-server-tools.md#agent-access-mcp-tools-user).

For example, an agent can prepare and test an application as follows:

1. Connect as `ADMINISTRATOR`.

1. Install the application.

1. Call `switch_user` to switch to `TEST_USER`.

1. Open the application and check that it works.

## Step 4: Verify agent activity
<a name="getting-started-agent-access-verify"></a>

You can verify agent activity using the following AWS services:
+ **AWS CloudTrail** — AWS CloudTrail logs agent session events. Open the AWS CloudTrail console to view agent activity. Tool calls are logged as data events, which requires a trail configured to [log data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html).
+ **CloudWatch** — CloudWatch provides operational metrics for agent sessions. Open the CloudWatch console to view metrics.
+ **Amazon S3** — If you enabled screenshot storage, Amazon S3 stores the screenshots in the bucket you specified during stack configuration.

## Step 5: Change agent access settings or disable agent access
<a name="getting-started-agent-access-update"></a>

This step changes the saved agent access settings on a stack or an image builder. To switch the Windows user that is logged in to an image builder, the agent uses the `switch_user` tool instead. For more information, see [User tools](agent-access-mcp-server-tools.md#agent-access-mcp-tools-user).

**To change agent access settings on a stack**

1. Run the following command with only the fields that you want to change. This example changes the user control mode.

   ```bash
   aws appstream update-stack \
       --name {{your-stack-name}} \
       --agent-access-config '{
           "UserControlMode": "VIEW_STOP"
       }'
   ```

   Fields that you don't include keep their current values. After the update, at least one action must be enabled.

1. Start a new streaming session. The changes apply to new sessions, not to sessions that are already running.

To disable agent access on a stack, run the following command:

```bash
aws appstream update-stack \
    --name {{your-stack-name}} \
    --attributes-to-delete AGENT_ACCESS_CONFIG
```

You can change agent access settings on an image builder only while it is stopped.

**To change agent access settings on an image builder**

1. Stop the image builder.

   ```bash
   aws appstream stop-image-builder \
       --name {{your-image-builder-name}}
   ```

1. Run the following command until the `State` value in the response is `STOPPED`.

   ```bash
   aws appstream describe-image-builders \
       --names {{your-image-builder-name}}
   ```

1. Run the following command with only the fields that you want to change. This example enables MCP tool forwarding.

   ```bash
   aws appstream update-image-builder \
       --name {{your-image-builder-name}} \
       --agent-access-config '{
           "Settings": [
               {"AgentAction": "FORWARD_MCP_TOOLS", "Permission": "ENABLED"}
           ]
       }'
   ```

   The same rules apply as for stacks. If you set `ScreenshotsUploadEnabled` to `false`, the `S3BucketArn` value is also removed.

1. Start the image builder. The changes apply at the next session.

   ```bash
   aws appstream start-image-builder \
       --name {{your-image-builder-name}}
   ```

To disable agent access on an image builder, stop the image builder as described in the previous procedure, and then run the following command. After you start the image builder again, you can work on it yourself in a browser.

```bash
aws appstream update-image-builder \
    --name {{your-image-builder-name}} \
    --attributes-to-delete AGENT_ACCESS_CONFIG
```

## Step 6: Clean up resources
<a name="getting-started-agent-access-cleanup"></a>

To avoid ongoing charges, delete the stack you created in this tutorial. You must stop the fleet and disassociate it from the stack before you can delete the stack. Optionally, you can also delete the fleet.

If you created an image builder, stop it when you are done to avoid ongoing charges. You can also delete it. For the commands, see [Using the AWS CLI](#getting-started-agent-access-cleanup-cli).

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

```bash
aws appstream stop-fleet \
    --name {{your-fleet-name}}

aws appstream disassociate-fleet \
    --stack-name {{your-stack-name}} \
    --fleet-name {{your-fleet-name}}

aws appstream delete-stack \
    --name {{your-stack-name}}
```

(Optional) To also delete the fleet after it has stopped:

```bash
aws appstream delete-fleet \
    --name {{your-fleet-name}}
```

If you created an image builder, stop it when you are done. A stopped image builder isn't billed for the instance.

```bash
aws appstream stop-image-builder \
    --name {{your-image-builder-name}}
```

(Optional) To delete the image builder:

```bash
aws appstream delete-image-builder \
    --name {{your-image-builder-name}}
```