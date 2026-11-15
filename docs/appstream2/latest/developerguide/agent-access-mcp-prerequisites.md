

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

For image builders, agent access supports Windows Server and Windows 11 (BYOL). Linux image builders aren't supported.

## Account, fleet, and image builder requirements
<a name="agent-access-before-you-begin"></a>

To set up agent access on a stack, you need the following:
+ An AWS account with permissions to create and manage WorkSpaces Applications stacks.
+ An active WorkSpaces Applications fleet (Always-On or On-Demand). If you haven't created a fleet, see [Get Started with Amazon WorkSpaces Applications: Set Up With Sample Applications](getting-started.md).
+ A stack associated with a fleet. Agents cannot connect to a stack without an associated fleet.
+ If you plan to enable screenshot storage, an Amazon S3 bucket. The bucket policy must grant the AppStream service principal access to list buckets. The agent that connects to the Model Context Protocol (MCP) server must have the `s3:PutObject` permission on the bucket.
+ A fleet running the latest version of the WorkSpaces Applications Agent. This is the streaming software on the image, not the AI agent you build. For more information about updating it, see [Keep Your Amazon WorkSpaces Applications Image Up-to-Date](keep-image-updated.md). For information about managing agent versions, see [Managing agent versions](https://docs.aws.amazon.com/appstream2/latest/developerguide/base-images-agent.html).

To use agent access on an image builder, you need the following:
+ An AWS account with permissions to create and manage WorkSpaces Applications images.
+ An image builder in the `RUNNING` state. An agent can't connect to an image builder that isn't running.
+ If you plan to enable screenshot storage, an Amazon S3 bucket. The bucket policy must grant the AppStream service principal access to list buckets. The agent that connects to the Model Context Protocol (MCP) server must have the `s3:PutObject` permission on the bucket.
+ An image builder whose image uses a WorkSpaces Applications agent released on or after October 25, 2026. If you create the image builder from a WorkSpaces Applications base image, use a base image released on or after November 4, 2026. If the image uses an earlier version, the request to enable agent access fails with an `IncompatibleImageException` error.

  To check an image, run the following command. In the response, `AppstreamAgentVersion` shows the agent version and `PublicBaseImageReleasedDate` shows when the base image was released.

  ```
  aws appstream describe-images --names {{your-image-name}}
  ```

  If the image is older, use a newer base image, or update the agent on your image. For more information, see [WorkSpaces Applications Agent Release Notes](agent-software-versions.md), [WorkSpaces Applications Base Image and Managed Image Update Release Notes](base-image-version-history.md), and [Update an Image by Using Managed WorkSpaces Applications Image Updates](keep-image-updated-managed-image-updates.md).

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
      "Action": ["appstream:CreateStreamingURL", "appstream:DescribeFleets", "appstream:CreateImageBuilderStreamingURL"],
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
  + `agentaccess-mcp:SwitchUser`: On an image builder, disconnect the current built-in user and log in as another built-in user (`ADMINISTRATOR`, `TEMPLATE_USER`, or `TEST_USER`)
  + `agentaccess-mcp:GetCurrentUser`: Return the built-in user that's logged in to an image builder

  The `agentaccess-mcp:*` wildcard also allows `SwitchUser` and `GetCurrentUser` on every image builder, as any of the three built-in users. To limit an agent on image builders, name the actions and use the condition keys, as in the example policy later in this topic.

  The agent needs the same `agentaccess-mcp` permissions whether it connects to an image builder with a streaming URL or with the image builder name.
+ An MCP-compatible agent framework that can send Streamable HTTP requests to the MCP endpoint, authorized in one of two ways:
  + **Signature Version 4 (SigV4) signing** – The agent signs each request to the MCP server with its AWS credentials.
  + **OAuth bearer token** – The agent uses OAuth 2.1 authorization through AWS Sign-In to retrieve a short-lived access token, and passes it as a bearer token on each request.

  For more information about both authorization methods, see [Request authorization](agent-access-mcp-server-endpoint.md#agent-access-mcp-server-authorization). The [Strands Agents SDK](https://strandsagents.com/docs/user-guide/concepts/tools/mcp-tools/) provides native MCP client support, or you can use any framework with the `mcp-proxy-for-aws` transport.
+ Python 3.10 or later on the machine where your agent runs. Your agent can run on any operating system, independent of the streamed desktop.

To enable or disable agent access, or change its settings on an existing image builder, you need the `appstream:UpdateImageBuilder` permission. This permission is separate from the agent's permissions.

On an image builder, the agent logs in as one of three built-in Windows users: `ADMINISTRATOR`, `TEMPLATE_USER`, or `TEST_USER`. For more information about these users, see [Built-in users on image builders](getting-started-agent-access.md#getting-started-agent-access-built-in-users). To control which image builders an agent can use and which built-in users it can log in as, use the following IAM condition keys:
+ `agentaccess-mcp:ImageBuilderArn`: The ARN of the image builder.
+ `agentaccess-mcp:LocalUser`: The built-in user that the agent logs in as.

The `LocalUser` condition key is present only on requests that log a user in. Use the `StringEqualsIfExists` operator with it, as in the example policy later in this topic. With `StringEquals`, other requests, such as `tools/list`, are denied.

We recommend that you restrict the agent to the least-privileged built-in user that its tasks need. For example, an agent that only tests applications can log in as `TEST_USER`.

The following example policy allows an agent to use one image builder and to log in only as `TEST_USER`. The second statement lists the tools that the agent can use on that image builder. Add the other actions that your agent needs.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ConnectAndSwitchOnlyAsTestUser",
            "Effect": "Allow",
            "Action": ["agentaccess-mcp:InvokeMcp", "agentaccess-mcp:SwitchUser"],
            "Resource": "*",
            "Condition": {
                "ArnEquals": { "agentaccess-mcp:ImageBuilderArn": "arn:aws:appstream:{{region}}:{{account-id}}:image-builder/{{image-builder-name}}" },
                "StringEqualsIfExists": { "agentaccess-mcp:LocalUser": "TEST_USER" }
            }
        },
        {
            "Sid": "DriveTheDesktopOnThatBuilder",
            "Effect": "Allow",
            "Action": [
                "agentaccess-mcp:GetCurrentUser",
                "agentaccess-mcp:CheckConnectionStatus",
                "agentaccess-mcp:GetScreenshot",
                "agentaccess-mcp:LeftClick",
                "agentaccess-mcp:TypeText",
                "agentaccess-mcp:KeyPress"
            ],
            "Resource": "*",
            "Condition": {
                "ArnEquals": { "agentaccess-mcp:ImageBuilderArn": "arn:aws:appstream:{{region}}:{{account-id}}:image-builder/{{image-builder-name}}" }
            }
        }
    ]
}
```

## Limitations
<a name="agent-access-limitations"></a>

WorkSpaces Applications agent access configurations have the following limitations:
+ VPC endpoints are not supported.
+ Multi-session fleets are not supported.
+ Elastic fleets are not supported.
+ A single session supports only a single AI agent connection.

Agent access on image builders has the following additional limitations:
+ Domain-joined image builders are not supported.
+ App block builders, which you use with elastic fleets, aren't supported.
+ An image builder supports only one AI agent connection at a time.
+ Changes to agent access settings on the image builder cannot be made while the image builder is running. Stop the image builder first to make an update, and it takes effect on the next session.
+ Either the AI agent or a human can provide input on an image builder, but not both at the same time. To switch between agent and human input, stop the image builder, change the setting to enable or disable agent access, and restart the image builder.