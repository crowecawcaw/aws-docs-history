

# Session behavior
<a name="agent-access-mcp-session-behavior"></a>

When you enable agent access on a stack, you configure how the agent's desktop session behaves, including how the agent sees and controls the desktop, where screenshots and files are stored, the screen layout, and whether people can watch and stop the agent. You set these options at the stack level.

## Computer input and vision
<a name="agent-access-input-vision"></a>

Agent access gives you two options for computer use. You set them up at the stack level. For other agent options, see [MCP tool forwarding](agent-access-mcp-tool-forwarding-details.md) and [User control mode](#agent-access-user-control-mode).
+ **Computer input**: during a streaming session, agents click buttons, enter text, and scroll on the desktop.
+ **Computer vision**: during a streaming session, agents take screenshots to see the desktop.

Use these rules to choose what to turn on:
+ For your agent to use computer input, computer vision must be turned on. The agent must see the desktop to use the keyboard and mouse.
+ You can leave computer input and vision off if you only use tool forwarding. For details, see [MCP tool forwarding](agent-access-mcp-tool-forwarding-details.md).

## Screenshot storage
<a name="agent-access-screenshots"></a>

You can optionally configure screenshot storage. When you enable it, the Model Context Protocol (MCP) server stores the screenshots captured during agent sessions in an Amazon S3 bucket. The MCP server uses the connecting agent's credentials to upload screenshots to the bucket, so the agent must have the `s3:PutObject` permission on the bucket. To encrypt screenshots in your bucket, see [Configuring default encryption for an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html).

## Desktop screen layout
<a name="agent-access-screen-layout"></a>

You configure the screen resolution and image format for the agent's desktop session:
+ **Screen resolution**: the display resolution for the agent's desktop session. The supported resolution is 1280x720.
+ **Screen image type**: the image format for agent screen captures. You can choose PNG or JPEG.

## Home folder storage
<a name="agent-access-home-folders"></a>

You can enable home folders so that agent files are saved to an Amazon S3 bucket in your AWS account. The Amazon WorkSpaces Applications fleet associated with the stack must allow access to Amazon S3 through the internet or an Amazon S3 VPC endpoint. For more information, see [Enable and administer home folders for your users](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders.html).

## Application settings persistence
<a name="agent-access-app-persistence"></a>

You can optionally enable application settings persistence. This setting is available on Windows and is not supported on Linux. When enabled, your agent's application customizations and Windows settings are saved after each streaming session and applied during the next session. These settings are saved to an Amazon S3 bucket in your AWS account. The Amazon WorkSpaces Applications fleet associated with the stack must allow access to Amazon S3 through the internet or an Amazon S3 VPC endpoint. For more information, see [Enable application settings persistence for your users](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-settings-persistence.html).

## User control mode
<a name="agent-access-user-control-mode"></a>

You can enable user control mode to allow users to observe and interact with agent sessions in real time. When user control mode is enabled, observers connect to the session through their browser using a streaming URL. They see a real-time view of the desktop as the agent interacts with it.

In `VIEW_STOP` mode, a stop button appears at the top of the observer's screen. The observer can use this button to stop the agent if needed. After an agent is stopped, it must start a new session to resume work.

Set the `UserControlMode` attribute in the `AgentAccessConfig` to one of the following values:
+ `VIEW_ONLY`: users can view and observe agent actions as they happen.
+ `VIEW_STOP`: users can view agent actions and stop the agent if needed.
+ `DISABLED`: users cannot view or stop the agent session.