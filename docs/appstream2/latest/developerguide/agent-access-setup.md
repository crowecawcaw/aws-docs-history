# Learn more about agents accessing WorkSpaces

Amazon WorkSpaces Applications enables agents to connect to streaming sessions and interact
with desktop applications through a managed Model Context Protocol (MCP) service.
This topic explains how agents access WorkSpaces Applications and the capabilities
you can configure.

## Prerequisites

To use agent access, you need the following:

- An active Amazon WorkSpaces Applications fleet (Always-On or On-Demand). If you haven't
  created a fleet,
  see [Get Started with Amazon WorkSpaces Applications: Set Up With Sample Applications](getting-started.md "getting-started.md").
- A stack associated with a fleet. Agents cannot connect to a stack
  without an associated fleet.
- An AWS account with permissions to create and manage Amazon WorkSpaces Applications
  stacks.
- If you plan to enable screenshot storage, an Amazon S3 bucket. The bucket
  policy must grant the AppStream service principal access to list buckets.
  The agent that connects to the MCP service must have the
  `s3:PutObject` permission on the bucket.
- If you plan to enable home folders, the same Amazon S3 access requirement
  applies.
- A fleet running the latest WorkSpaces Applications Agent. To read more
  on updating your WorkSpaces Applications Agent, see [Keep Your Amazon WorkSpaces Applications Image Up-to-Date](keep-image-updated.md "keep-image-updated.md").

**Limitations**

WorkSpaces agent access configurations have the following limitations:

- Only Windows Server images are supported.
- Domain-joined fleets are not supported.
- VPC endpoints are not supported.
- Multi-session fleets are not supported.
- Elastic fleets are not supported.

## How agent access works

You enable agent access when you create a stack. When agent access is enabled,
the stack is configured with agent-specific settings instead of the standard
Amazon WorkSpaces Applications configuration for human users. You can enable agent access through
the Amazon WorkSpaces Applications console, AWS CLI, or API.

## Computer input and vision

Agent access provides two interaction capabilities that you configure at the
stack level:

- **Computer input** — Allows agents
  to click buttons, enter text, and scroll on the desktop during a streaming
  session.
- **Computer vision** — Allows agents
  to see the desktop by taking screenshots during a streaming session.

You must enable at least one of these capabilities.

## Screenshot storage

You can optionally configure screenshot storage for agent sessions. When
screenshot storage is enabled, screenshots captured during agent sessions are
stored in an Amazon S3 bucket. The MCP service uses the connecting agent's credentials
to upload screenshots to the bucket. The agent must have the
`s3:PutObject` permission on the bucket.

## Desktop screen layout

You configure the screen resolution and image format for the agent streaming
environment:

- **Screen resolution** — The display
  resolution for the agent streaming environment. The supported resolution
  is 1280x720.
- **Screen image type** — The image
  format for agent screen captures. You can choose PNG or JPEG.

## Home folder storage

You can enable home folders so that agent files are saved to an Amazon S3 bucket
in your AWS account. The Amazon WorkSpaces Applications fleet associated with the stack must
allow access to Amazon S3 through the internet.

## Application settings persistence

You can optionally enable application settings persistence. When enabled,
your agent's application customizations and Windows settings are saved after
each streaming session and applied during the next session. These settings are
saved to an Amazon S3 bucket in your AWS account. The Amazon WorkSpaces Applications fleet associated
with the stack must allow access to Amazon S3 through the internet.

## Streaming URLs

Agents connect to WorkSpaces Applications through a streaming URL. You generate
a streaming URL by using the `CreateStreamingURL` API. No agent-specific
parameters are required. The agent-specific behavior is determined by the stack's
agent access configuration. The streaming URL is passed to the MCP service as a
header on each request.

For more information about the `CreateStreamingURL` API, see
[CreateStreamingURL](../APIReference/API_CreateStreamingURL.md "../APIReference/API_CreateStreamingURL.md")
in the _Amazon AppStream 2.0 API Reference_.

## MCP proxy for AWS

To connect your agent to the managed MCP service, you can use the
`mcp-proxy-for-aws` transport to create an MCP client that supports
SigV4 signing of MCP requests in Python. If you are building an agent in another
language, you need to write the signing logic yourself or find an available
library.

For more information, see
[mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws "https://github.com/aws/mcp-proxy-for-aws")
on GitHub.

## Monitoring

You can monitor agent activity through the following services:

- **AWS CloudTrail** — Agent session
  events are logged in CloudTrail. You can view when agents connect, which
  tools they use, and when sessions end. Tool calls are data events
  and require that you set up a trail to log data events. For more
  information, see [Logging
  data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") in the _CloudTrail User Guide_.
- **CloudWatch** — The following
  operational metrics are available in CloudWatch for agent sessions:

  - `Invocations`
  - `Latency`
  - `ClientErrors`
  - `ServerErrors`
  - `SessionStart`
  - `SessionEnd`

- **Amazon S3** — If you configure
  screenshot storage, screenshots captured during agent sessions are
  available in the Amazon S3 bucket that you specify.
