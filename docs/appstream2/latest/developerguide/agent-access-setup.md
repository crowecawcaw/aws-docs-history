

# Learn more about agents accessing WorkSpaces
<a name="agent-access-setup"></a>

Amazon WorkSpaces Applications enables agents to connect to streaming sessions and interact with desktop applications through a managed Model Context Protocol (MCP) service. This topic explains how agents access WorkSpaces Applications and the capabilities you can configure.

## Prerequisites
<a name="agent-access-before-you-begin"></a>

To use agent access, you need the following:
+ An active Amazon WorkSpaces Applications fleet (Always-On or On-Demand). If you haven't created a fleet, see [Get Started with Amazon WorkSpaces Applications: Set Up With Sample Applications](getting-started.md).
+ A stack associated with a fleet. Agents cannot connect to a stack without an associated fleet.
+ An AWS account with permissions to create and manage Amazon WorkSpaces Applications stacks.
+ If you plan to enable screenshot storage, an Amazon S3 bucket. The bucket policy must grant the AppStream service principal access to list buckets. The agent that connects to the MCP service must have the `s3:PutObject` permission on the bucket.
+ A fleet running the latest WorkSpaces Applications Agent. To read more on updating your WorkSpaces Applications Agent, see [Keep Your Amazon WorkSpaces Applications Image Up-to-Date](keep-image-updated.md). For information about managing agent versions, see [Managing agent versions](https://docs.aws.amazon.com/appstream2/latest/developerguide/base-images-agent.html).

**Limitations**

WorkSpaces agent access configurations have the following limitations:
+ Only Windows Server images are supported.
+ VPC endpoints are not supported.
+ Multi-session fleets are not supported.
+ Elastic fleets are not supported.
+ A single session supports only a single agent connection.

## How agent access works
<a name="agent-access-how-it-works"></a>

You enable agent access when you create a stack. When agent access is enabled, the stack is configured with agent-specific settings instead of the Amazon WorkSpaces Applications configuration for human users. You can enable agent access through the Amazon WorkSpaces Applications console, AWS CLI, or API.

## Computer input and vision
<a name="agent-access-input-vision"></a>

Agent access provides two interaction capabilities that you configure at the stack level:
+ **Computer input** — Allows agents to click buttons, enter text, and scroll on the desktop during a streaming session.
+ **Computer vision** — Allows agents to see the desktop by taking screenshots during a streaming session.

You must enable at least one of these capabilities.

## Screenshot storage
<a name="agent-access-screenshots"></a>

You can optionally configure screenshot storage for agent sessions. When screenshot storage is enabled, screenshots captured during agent sessions are stored in an Amazon S3 bucket. The MCP service uses the connecting agent's credentials to upload screenshots to the bucket. The agent must have the `s3:PutObject` permission on the bucket.

## Desktop screen layout
<a name="agent-access-screen-layout"></a>

You configure the screen resolution and image format for the agent streaming environment:
+ **Screen resolution** — The display resolution for the agent streaming environment. The supported resolution is 1280x720.
+ **Screen image type** — The image format for agent screen captures. You can choose PNG or JPEG.

## Home folder storage
<a name="agent-access-home-folders"></a>

You can enable home folders so that agent files are saved to an Amazon S3 bucket in your AWS account. The Amazon WorkSpaces Applications fleet associated with the stack must allow access to Amazon S3 through the internet or an Amazon S3 VPC endpoint. For more information, see [Enable and administer home folders for your users](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders.html).

## Application settings persistence
<a name="agent-access-app-persistence"></a>

You can optionally enable application settings persistence. When enabled, your agent's application customizations and Windows settings are saved after each streaming session and applied during the next session. These settings are saved to an Amazon S3 bucket in your AWS account. The Amazon WorkSpaces Applications fleet associated with the stack must allow access to Amazon S3 through the internet or an Amazon S3 VPC endpoint. For more information, see [Enable application settings persistence for your users](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-settings-persistence.html).

## MCP tool forwarding
<a name="agent-access-mcp-tool-forwarding"></a>

You can enable MCP tool forwarding to allow agents to interact with applications and the desktop operating system through direct MCP calls rather than using computer use tools. When enabled, MCP tools available on your WorkSpaces application session are forwarded to the agent. The forwarded tools appear when the agent lists its available tools.

## User control mode
<a name="agent-access-user-control-mode"></a>

You can enable user control mode to allow users to observe and interact with agent sessions in real time. When user control mode is enabled, observers connect to the session through their browser using a streaming URL. They see a real-time view of the desktop as the agent interacts with it.

In `VIEW_STOP` mode, a stop button appears at the top of the observer's screen. The observer can use this button to stop the agent if needed. Once an agent is stopped, it must start a new session to resume work.

Set the `UserControlMode` attribute in the `AgentAccessConfig` to one of the following values:
+ `VIEW_ONLY` — Users can view and observe agent actions as they happen.
+ `VIEW_STOP` — Users can view agent actions and stop the agent if needed.
+ `DISABLED` — Users cannot view or stop the agent session.

## Streaming URLs
<a name="agent-access-streaming-url"></a>

Agents connect to WorkSpaces Applications through a streaming URL. You generate a streaming URL by using the `CreateStreamingURL` API. No agent-specific parameters are required. The agent-specific behavior is determined by the stack's agent access configuration. The streaming URL is passed to the MCP service as a header on each request.

For more information about the `CreateStreamingURL` API, see [CreateStreamingURL](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html) in the *Amazon AppStream 2.0 API Reference*.

## MCP proxy for AWS
<a name="agent-access-mcp-proxy"></a>

To connect your agent to the managed MCP service, you can use the `mcp-proxy-for-aws` transport to create an MCP client that supports SigV4 signing of MCP requests in Python. If you are building an agent in another language, you need to write the signing logic yourself or find an available library.

For more information, see [mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws) on GitHub.

## Monitoring
<a name="agent-access-monitoring"></a>

You can monitor agent activity through the following services:
+ **AWS CloudTrail** — Agent session events are logged in CloudTrail. You can view when agents connect, which tools they use, and when sessions end. Tool calls are data events and require that you set up a trail to log data events. For more information, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *CloudTrail User Guide*.
+ **CloudWatch** — The following operational metrics are available in CloudWatch for agent sessions:
  + `Invocations`
  + `Latency`
  + `ClientErrors`
  + `ServerErrors`
  + `McpSessionStart`
  + `McpSessionDuration`
+ **Amazon S3** — If you configure screenshot storage, screenshots captured during agent sessions are available in the Amazon S3 bucket that you specify.