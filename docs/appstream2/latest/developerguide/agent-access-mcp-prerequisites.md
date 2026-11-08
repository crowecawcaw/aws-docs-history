

# Prerequisites
<a name="agent-access-mcp-prerequisites"></a>

This topic covers what you need in place before an agent can connect: the AWS account and Amazon WorkSpaces Applications fleet that host the desktop session, and the permissions and software your agent uses to reach it. Setting these up first lets your agent authenticate and operate the desktop without interruption.

## Supported operating systems
<a name="agent-access-supported-os"></a>

Agent access supports the same operating systems as WorkSpaces Applications. How you get an image depends on the operating system.


| Operating system | Image source | More information | 
| --- | --- | --- | 
| Windows Server | AWS-provided base images, or bring your own image | [WorkSpaces Applications Base Image and Managed Image Update Release Notes](base-image-version-history.md)<br />[Import Image](import-image.md) | 
| Linux | AWS-provided base images | [WorkSpaces Applications Base Image and Managed Image Update Release Notes](base-image-version-history.md) | 
| Windows 11 | Bring Your Own License (BYOL): you supply the image | [Bring Your Own Windows Desktop Licenses for Amazon WorkSpaces Applications](byol-windows-images.md) | 

Windows 11 requires additional BYOL setup. For requirements, see [Bring Your Own Windows Desktop Licenses for Amazon WorkSpaces Applications](byol-windows-images.md).

## Account and fleet requirements
<a name="agent-access-before-you-begin"></a>

To set up agent access, you need the following:
+ An active WorkSpaces Applications fleet (Always-On or On-Demand). If you haven't created a fleet, see [Get Started with Amazon WorkSpaces Applications: Set Up With Sample Applications](getting-started.md).
+ A stack associated with a fleet. Agents cannot connect to a stack without an associated fleet.
+ An AWS account with permissions to create and manage WorkSpaces Applications stacks.
+ If you plan to enable screenshot storage, an Amazon S3 bucket. The bucket policy must grant the AppStream service principal access to list buckets. The agent that connects to the Model Context Protocol (MCP) server must have the `s3:PutObject` permission on the bucket.
+ A fleet running the latest version of the WorkSpaces Applications Agent. This is the streaming software on the image, not the AI agent you build. For more information about updating it, see [Keep Your Amazon WorkSpaces Applications Image Up-to-Date](keep-image-updated.md). For information about managing agent versions, see [Managing agent versions](https://docs.aws.amazon.com/appstream2/latest/developerguide/base-images-agent.html).

## Agent and permissions requirements
<a name="agent-access-prereqs-agent"></a>

To build and connect your agent, you need the following:
+ AWS credentials (environment variables, AWS profile, EC2 instance role, or Lambda execution role) with the following IAM permissions. The agent uses these credentials directly to sign requests to the MCP server:

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
  + `agentaccess-mcp:InvokeMcp`: Initialize sessions and discover tools
  + `agentaccess-mcp:GetScreenshot`: Capture screen state
  + `agentaccess-mcp:LeftClick`: Perform left mouse click
  + `agentaccess-mcp:DoubleClick`: Perform double click
  + `agentaccess-mcp:TripleClick`: Perform triple click
  + `agentaccess-mcp:RightClick`: Perform right mouse click
  + `agentaccess-mcp:MiddleClick`: Perform middle mouse click
  + `agentaccess-mcp:TypeText`: Type text string
  + `agentaccess-mcp:KeyPress`: Press key or key combination
  + `agentaccess-mcp:HoldKey`: Hold key for duration
  + `agentaccess-mcp:Scroll`: Scroll at coordinates
  + `agentaccess-mcp:MovePointer`: Move pointer to coordinates
  + `agentaccess-mcp:LeftClickDrag`: Perform left click drag
  + `agentaccess-mcp:LeftMouseDown`: Press and hold left mouse button
  + `agentaccess-mcp:LeftMouseUp`: Release left mouse button
  + `agentaccess-mcp:CheckConnectionStatus`: Check connection status of a streaming session
  + `agentaccess-mcp:CallForwardedTool`: Invoke a forwarded tool on a remote instance
  + `agentaccess-mcp:LaunchApplication`: Launch a cataloged application in the current session
  + `agentaccess-mcp:ToggleAppSwitcher`: Open or close the app-switcher overlay
+ An MCP-compatible agent framework that can send Streamable HTTP requests to the MCP endpoint, authorized in one of two ways:
  + **Signature Version 4 (SigV4) signing** – The agent signs each request to the MCP server with its AWS credentials.
  + **OAuth bearer token** – The agent uses OAuth 2.1 authorization through AWS Sign-In to retrieve a short-lived access token, and passes it as a bearer token on each request.

  For more information about both authorization methods, see [Request authorization](agent-access-mcp-server-endpoint.md#agent-access-mcp-server-authorization). The [Strands Agents SDK](https://strandsagents.com/docs/user-guide/concepts/tools/mcp-tools/) provides native MCP client support, or you can use any framework with the `mcp-proxy-for-aws` transport.
+ Python 3.10 or later on the machine where your agent runs. Your agent can run on any operating system, independent of the streamed desktop.

## Limitations
<a name="agent-access-limitations"></a>

WorkSpaces Applications agent access configurations have the following limitations:
+ VPC endpoints are not supported.
+ Multi-session fleets are not supported.
+ Elastic fleets are not supported.
+ A single session supports only a single agent connection.