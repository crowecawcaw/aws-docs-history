

# WorkSpaces Applications MCP server
<a name="agent-access-mcp-server"></a>

The WorkSpaces Applications MCP server is a fully managed service that provides AI agents with Model Context Protocol (MCP) tools to interact with desktop applications during streaming sessions. Agents can click buttons, enter text, scroll, and take screenshots of the desktop.

## Overview
<a name="agent-access-mcp-server-overview"></a>

When you enable agent access on a stack, agents can connect to the managed MCP server to interact with desktop applications. The MCP server handles the communication between your agent and the streaming session. Your agent sends MCP tool requests, and the server executes them on the desktop.

Agent access supports both non-domain-joined and domain-joined fleets. The connection method differs by fleet type. For non-domain-joined fleets, you can connect in either of two ways. In the first, you provide the stack and user ID as two headers: `x-amzn-agentaccess-workspaces-applications-stack` and `x-amzn-agentaccess-workspaces-applications-user-id`. The MCP server then creates the streaming session for you. In the second, you generate a streaming URL yourself and pass it as a header. For domain-joined fleets, authenticate through SAML federation. For the path that matches your fleet, see [Connecting to the MCP server](#agent-access-mcp-server-endpoint).

## Connecting to the MCP server
<a name="agent-access-mcp-server-endpoint"></a>

Agents connect to the MCP server at the following endpoint:

```
https://agentaccess-mcp.{{region}}.api.aws/mcp
```

Replace {{region}} with your Region code. For the supported Regions and their endpoints, see [WorkSpaces Applications MCP endpoints](allowed-domains.md#allowed-domains-mcp-endpoints).

The MCP server is hosted in the AWS cloud and uses Streamable HTTP as its transport protocol. You don't need to install or maintain any server components.

**Note**  
Before an agent can connect, the fleet associated with your stack must be running and have available capacity.

To connect an agent, you make two choices: how the agent authorizes its requests, and how it identifies the streaming session.

### Request authorization
<a name="agent-access-mcp-server-authorization"></a>

You can authorize requests in one of two ways: SigV4 signing or OAuth 2.1 authorization through AWS Sign-In.

#### SigV4 signing
<a name="agent-access-mcp-server-authorization-sigv4"></a>

To use SigV4, sign each request using IAM credentials with the service name `agentaccess-mcp`. The following Python example shows the general connection pattern using `mcp-proxy-for-aws`:

```
from mcp_proxy_for_aws import aws_iam_streamablehttp_client

async with aws_iam_streamablehttp_client(
    endpoint="https://agentaccess-mcp.{{region}}.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region="{{region}}",
    headers={
        # Fleet-type-specific headers (see the following subsections)
    },
    metadata={
        # Fleet-type-specific metadata (see the following subsections)
    },
) as (read, write, _):
    # Use read/write streams with your MCP client
    ...
```

For other languages, write your own SigV4 signing logic for outgoing MCP requests or use a library that supports SigV4 signing. For more information about `mcp-proxy-for-aws`, see [mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws) on GitHub.

#### OAuth 2.1 authorization
<a name="agent-access-mcp-server-connect-oauth"></a>

As an alternative to signing requests with IAM credentials, the MCP server supports OAuth 2.1 authorization through AWS Sign-In, the same way as the AWS MCP Server. AWS Sign-In acts as the authorization server. It issues short-lived, scoped access tokens. The MCP server accepts these tokens as bearer tokens. OAuth uses your existing IAM identities, permissions, and organizational controls. When you authorize an agent, it can access the MCP server on your behalf. It does not get extra permissions. AWS still checks every request against your IAM policies.

OAuth-compatible MCP clients — such as Kiro, Claude Code, Cursor, Codex, and Gemini — can connect directly to the MCP server endpoint without local proxy software. AWS Sign-In supports two authorization models:
+ **Interactive authorization** — For agents that can open a browser. The client registers through dynamic client registration, redirects you to an AWS Sign-In page to authenticate and approve access, and AWS Sign-In then issues and refreshes the access tokens.
+ **Non-interactive authorization** — For agents that already have AWS credentials and run without a browser (sometimes called headless authorization). The agent uses the OAuth client credentials grant to exchange SigV4-signed credentials for a short-lived access token.

OAuth authorization for the MCP server works the same way as it does for the AWS MCP Server, using the MCP server endpoint (`https://agentaccess-mcp.{{region}}.api.aws/mcp`). For setup, required IAM permissions, and governance and monitoring options, see [OAuth 2.1 authentication for AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/oauth-authentication.html) in the *Agent Toolkit for AWS User Guide* and [Sign-In with OAuth 2.0](https://docs.aws.amazon.com/signin/latest/userguide/oauth-sign-in-overview.html) in the *AWS Sign-In User Guide*.

### Session identification
<a name="agent-access-mcp-server-session-id"></a>

How you identify the streaming session depends on your fleet type.

**Note**  
At any given time, only one agent can connect to a unique session. Named users, specified through the `UserId` parameter, can have only one active session per fleet at a time. To run multiple agents concurrently, each agent must connect to its own unique session.

#### Connecting with non-domain-joined fleets
<a name="agent-access-mcp-server-connect-ndj"></a>

For non-domain-joined fleets, you can connect in either of two ways. Provide the stack and user ID as headers, and the MCP server creates the streaming session for you. This suits MCP clients that you configure statically, because such a client can hold a fixed pair of headers but cannot generate a streaming URL or replace one when it expires. Alternatively, generate a streaming URL yourself and pass it as a header. Use this approach when you need control over session creation, such as setting the validity period.

To connect with the stack and user ID, pass the following headers on every request:
+ `x-amzn-agentaccess-workspaces-applications-stack` — the stack name or ARN.
+ `x-amzn-agentaccess-workspaces-applications-user-id` — the user ID for the session.

**Note**  
The `x-amzn-agentaccess-workspaces-applications-user-id` header is optional. If you omit it, the MCP server derives the user identity from the authenticated session. It uses the AWS `SourceIdentity` when one is present, and the caller's IAM principal otherwise. `SourceIdentity` preserves a user's original corporate identity when they assume an IAM role. This holds even when roles are chained through an external identity provider (IdP).

```
from mcp_proxy_for_aws import aws_iam_streamablehttp_client

# Connect to the MCP server with the stack and user ID
async with aws_iam_streamablehttp_client(
    endpoint="https://agentaccess-mcp.{{region}}.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region="{{region}}",
    headers={
        "x-amzn-agentaccess-workspaces-applications-stack": "{{stack-name-or-arn}}",
        "x-amzn-agentaccess-workspaces-applications-user-id": "{{user-id}}",
    },
) as (read, write, _):
    ...
```

To connect with a streaming URL instead, generate one using the `CreateStreamingURL` API and pass it as the `x-amzn-agentaccess-streaming-session-url` header on every request. No agent-specific parameters are required. The agent behavior is determined by the stack's agent access configuration.

```
import boto3
from mcp_proxy_for_aws import aws_iam_streamablehttp_client

# Generate streaming URL
appstream = boto3.client("appstream", region_name="{{region}}")
response = appstream.create_streaming_url(
    StackName="{{stack-name}}",
    FleetName="{{fleet-name}}",
    UserId="{{user-id}}",
)
streaming_url = response["StreamingURL"]

# Connect to MCP server
async with aws_iam_streamablehttp_client(
    endpoint="https://agentaccess-mcp.{{region}}.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region="{{region}}",
    headers={
        "x-amzn-agentaccess-streaming-session-url": streaming_url,
    },
) as (read, write, _):
    ...
```

For more information about the `CreateStreamingURL` API, see [CreateStreamingURL](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html) in the *Amazon WorkSpaces Applications 2.0 API Reference*.

#### Connecting with domain-joined fleets
<a name="agent-access-mcp-server-connect-dj"></a>

When agents access domain-joined streaming instances, the connection must be federated through a SAML provider. This requirement applies to both traditional and agent sessions. For agent sessions, [Certificate-Based Authentication](certificate-based-authentication.md) is required.

Because domain-joined streaming instances require access through SAML, your MCP client must provide a signed SAML assertion instead of a streaming URL. Encoded SAML assertions exceed HTTP header size limits. To avoid this, use the `metadata` field in `mcp-proxy-for-aws`:

```
from mcp_proxy_for_aws import aws_iam_streamablehttp_client

# saml_response: your signed, base64-encoded SAML assertion
# stack_arn: the ARN of the AppStream stack for the AD user

async with aws_iam_streamablehttp_client(
    endpoint="https://agentaccess-mcp.{{region}}.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region="{{region}}",
    metadata={
        "saml_response": saml_response,
        "stack_arn": stack_arn,
    },
) as (read, write, _):
    ...
```

**Note**  
The `metadata` parameter was added in `mcp-proxy-for-aws` version 1.6.1. Earlier versions cannot inject the `_meta` field without additional development. To upgrade, run `pip install -U mcp-proxy-for-aws`.

For more information about setting up SAML federation with WorkSpaces Applications, see [Setting up SAML](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-overview.html) in the *Amazon WorkSpaces Applications Administration Guide*. For more information and a complete working example, see the [sample-code-for-workspaces-agent-access](https://github.com/aws-samples/sample-code-for-workspaces-agent-access/tree/main) repository in AWS Samples on GitHub.

## Connection modes
<a name="agent-access-mcp-server-connect-mode"></a>

You can control how your agent waits for the desktop session to become available by setting the `x-amzn-agentaccess-connect-mode` header on your MCP requests.

**Note**  
Connection modes apply to both non-domain-joined and domain-joined fleets. Set the `x-amzn-agentaccess-connect-mode` header alongside whichever authentication mechanism your fleet type uses. For non-domain-joined fleets, that is either the stack and user ID headers or a streaming-URL header. For domain-joined fleets, it is the SAML assertion metadata.

The following modes are available:
+ **BLOCKING** (default) — The MCP server waits until the desktop connection is fully established before responding. When `tools/list` returns, all tools are immediately available.
+ **POLLING** — The MCP server responds immediately without waiting for the desktop connection. Initially, only the `connection_status` tool is available. Your agent polls this tool until the connection is established, at which point the full tool set becomes available.

Use POLLING mode when you want your agent to perform other work while waiting for the desktop connection, or when you need more control over connection timeout behavior.

The following example shows how to use POLLING mode:

```
# Pass the header when creating the MCP connection
headers = {
    "x-amzn-agentaccess-streaming-session-url": streaming_url,  # non-domain-joined fleets
    "x-amzn-agentaccess-connect-mode": "POLLING",
}

# After initialize, tools/list returns immediately with connection_status
tools = await session.list_tools()
# tools = [connection_status]

# Poll connection_status until the desktop is ready
while True:
    result = await session.call_tool("connection_status", {})
    status = json.loads(result.content[0].text)
    if status["state"] == "CONNECTED":
        break
    time.sleep(2)

# Now tools/list returns the full set (screenshot, left_click, type_text, etc.)
tools = await session.list_tools()
```

## Session cleanup
<a name="agent-access-mcp-server-session-cleanup"></a>

You can control whether the streaming session is expired when your agent ends its connection by setting the `x-amzn-agentaccess-expire-streaming-session-on-delete` header on your MCP requests. The following values are available:
+ **true** — When your agent sends an explicit HTTP `DELETE` request, the MCP server expires the WorkSpaces Applications streaming session as part of cleanup. Expiring the session terminates the underlying streaming instance and triggers the fleet's configured autoscaling policy. For more information, see [Fleet Auto Scaling for Amazon WorkSpaces Applications](autoscaling.md).
+ **false** (default) — The streaming session continues running until the disconnect timeout is reached. For more information about the disconnect timeout, see [Create a Fleet in Amazon WorkSpaces Applications](set-up-stacks-fleets-create.md).

**Note**  
By default, an `mcp-proxy-for-aws` MCP client automatically handles the `DELETE` request when you properly end the client lifecycle.

## Available tools
<a name="agent-access-mcp-server-tools"></a>

The MCP server provides the following tools. Agents use them to interact with the desktop during a streaming session. All tool names use the `agentaccess___` prefix.

### Mouse tools
<a name="agent-access-mcp-tools-mouse"></a>

`left_click`  
Perform a left click at the given coordinates.  
Parameters: `x` (required), `y` (required), `modifiers` (optional, for example `ctrl` or `ctrl+shift`).

`double_click`  
Perform a double click at the given coordinates.  
Parameters: `x` (required), `y` (required), `modifiers` (optional).

`triple_click`  
Perform a triple click at the given coordinates.  
Parameters: `x` (required), `y` (required), `modifiers` (optional).

`right_click`  
Perform a right click at the given coordinates.  
Parameters: `x` (required), `y` (required), `modifiers` (optional).

`middle_click`  
Perform a middle click at the given coordinates.  
Parameters: `x` (required), `y` (required), `modifiers` (optional).

`left_click_drag`  
Perform a left click drag from start coordinates to end coordinates.  
Parameters: `start_x` (required), `start_y` (required), `end_x` (required), `end_y` (required).

`left_mouse_down`  
Press and hold the left mouse button at the given coordinates.  
Parameters: `x` (required), `y` (required), `modifiers` (optional).

`left_mouse_up`  
Release the left mouse button at the given coordinates.  
Parameters: `x` (required), `y` (required), `modifiers` (optional).

`move_pointer`  
Move the pointer to the given coordinates.  
Parameters: `x` (required), `y` (required).

`scroll`  
Scroll the mouse wheel at the given coordinates.  
Parameters: `x` (required), `y` (required), `scroll_direction` (required — `Up`, `Down`, `Left`, or `Right`), `scroll_amount` (required — in ticks, where 120 ticks equals one wheel notch), `modifiers` (optional).

### Keyboard tools
<a name="agent-access-mcp-tools-keyboard"></a>

`type_text`  
Type text by simulating keyboard events for each character.  
Parameters: `text` (required — up to 10,000 characters).

`key`  
Press a key or key combination.  
Parameters: `keys` (required — a single key or combination joined by `+`, for example `a`, `ctrl+c`, or `ctrl+shift+s`).

`hold_key`  
Hold a key or key combination for a specified duration.  
Parameters: `keys` (required), `duration` (required — 1 to 30 seconds).

### Screen tools
<a name="agent-access-mcp-tools-screen"></a>

`screenshot`  
Capture a screenshot of the desktop. The returned image dimensions define the coordinate space for all mouse tools.  
Parameters: `include_cursor` (optional — defaults to `false`).

### Application tools
<a name="agent-access-mcp-tools-application"></a>

**Note**  
These application tools appear in the agent's tool list only when applications are registered in the fleet image's catalog. If the image has no registered applications, these tools are not available.

`launch_application`  
Launch an application from the ones available in the fleet image's catalog.  
Parameters: `id` (required) — the application identifier.  
The tool's own description lists the identifiers of the available applications. The MCP server populates this description from the fleet image's catalog (for example, `firefox`, `notepad++`, or `eclipse`). Use one of the listed identifiers. An `id` that is not in the catalog returns `isError: true` with `SERVER_ERROR: Invalid input`. IDs are set when the image is built. You cannot work out an ID from the application name.  
Launching an application does not replace what is already running. The previously launched application stays open. That is why the app switcher exists.

`toggle_app_switcher`  
Open or close the app-switcher overlay.  
Parameters: none.  
This tool only toggles the overlay. To bring a particular application to the foreground, follow up with a `left_click` on its thumbnail, using coordinates read from a screenshot. No tool reports which application is currently in the foreground, so an agent that needs to know must capture a screenshot and look.  
The app switcher is available only when the fleet's **Stream view** is set to **Application**, which displays only the windows of applications that users open. It is not available when **Stream view** is set to **Desktop**, because WorkSpaces Applications then provides the standard desktop and taskbar for the operating system.

### Session tools
<a name="agent-access-mcp-tools-session"></a>

**Note**  
To watch an agent while it works, code the agent to open a streaming URL in a browser. Keep the URL out of the model's context, because it grants session access. You can create the URL in one of two ways:  
Call the `CreateStreamingURL` API with the `stack`, `fleet`, and `userId` values from `get_session_info`, then open the returned URL in a browser.
Read the `streaming_url` value from the `_meta` field of the `get_session_info` response, then open it in a browser.
In both cases, the agent's own code handles the URL, so it never exposes the session credentials to the model.

`get_session_info`  
Return information about the current session.  
Parameters: none.  
Returns the following identifier fields as the tool result: `mcpSessionId`, `stack`, `userId`, `workSpacesSessionId`, and `fleet`.

## MCP tool forwarding
<a name="agent-access-mcp-tool-forwarding-details"></a>

With MCP tool forwarding, agents can work directly with applications and the operating system. They make direct MCP calls instead of using computer use tools. When you turn on tool forwarding, the MCP server sends your agent the tools set up on the WorkSpaces application session.

### Setting up tool forwarding
<a name="agent-access-tool-forwarding-setup"></a>

To set up MCP tool forwarding:

1. **Enable tool forwarding** — Turn on the `FORWARD_MCP_TOOLS` agent action through the API or console settings.

1. **Verify that the MCP server configuration file is present** — The service looks for a configuration file at the following path:

   ```
   C:\ProgramData\NICE\dcv\mcp_server_redirection_config.json
   ```

1. **Configure the MCP server on the WorkSpace image** — The configuration file is JSON with a single top-level `mcpServers` object. Each key is a unique name that you choose for a server. Each value specifies how to launch that server.

   ```
   {
       "mcpServers": {
           "filesystem": {
               "command": "C:/path/to/python.exe",
               "args": ["C:/mcpServerPath/filesystem.py", "C:/UserName/Documents"]
           },
           "weather": {
               "command": "C:/Program Files/my-mcp/weather.exe"
           }
       }
   }
   ```


<table>
<thead>
  <tr><th>Field</th><th>Required</th><th>Type</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><code>command</code></td><td>Yes</td><td>String</td><td>Absolute path to the executable to launch.</td></tr>
  <tr><td><code>args</code></td><td>No</td><td>Array of strings</td><td>Arguments passed to the executable.</td></tr>
</tbody>
</table>


1. **Verify tool availability** — If the file is present, the service connects to the MCP servers listed in the file and forwards their tools. The forwarded tools appear when the agent lists its available tools.

1. **Test the configuration** — To confirm that tool forwarding works, run the `mcpforwardingtester` script. You can find it in the [sample-code-for-workspaces-agent-access](https://github.com/aws-samples/sample-code-for-workspaces-agent-access/tree/main/utils/mcpforwardingtester) repository on GitHub. The script tests the MCP setup on your WorkSpace. It reports which tools are ready and flags any issues.

**Note**  
Both IAM access and the service setting must be enabled for tool forwarding to work. IAM permissions do not override the service setting.

### MCP tool forwarding considerations
<a name="agent-access-tool-forwarding-considerations"></a>

Note the following considerations when you configure MCP tool forwarding:
+ **Transport is standard I/O (stdio) only.** Each entry must launch a process that speaks MCP over its standard input and output. Remote HTTP or SSE MCP endpoints are not supported. To use a remote endpoint, wrap it in a local stdio server.
+ **Only `command` and `args` are supported.** There is no field for environment variables or working directory. Each server inherits the environment of the streaming session and runs as the session user. Use absolute paths for `command` and for any path arguments.
+ **Use forward slashes in paths** (for example, `C:/Program Files/my-mcp/server.exe`). JSON treats the backslash as an escape character, so a Windows-style path written with single backslashes is invalid. Windows accepts forward slashes for absolute paths, which avoids the need to escape every separator as `\\`.
+ **Tool-call timeout.** Each forwarded tool call must complete within 5 seconds. The MCP server cancels calls that take longer and returns an error to the agent. Design forwarded tools to return quickly.

### How forwarded tools appear to the agent
<a name="agent-access-tool-forwarding-naming"></a>

To prevent collisions between servers, the MCP server renames each forwarded tool in the agent's tool list using the following pattern:

```
forwarded___{{server-name}}___{{original-tool-name}}
```

The {{server-name}} is the key from your configuration file. For example, a `get_forecast` tool from the `weather` server is listed as `forwarded___weather___get_forecast`. When the agent calls the forwarded name, the MCP server routes the request to the original tool on the owning server. Agent code that matches on tool names must expect this prefix.

### IAM permissions for tool forwarding
<a name="agent-access-tool-forwarding-iam"></a>

The IAM action for calling forwarded tools is `CallForwardedTool`. To limit access to specific stacks, use the `StackArn` condition key:

```
{
  "Action": "agentaccess-mcp:*",
  "Resource": "*",
  "Condition": {
    "ArnLike": {
      "agentaccess-mcp:StackArn": "arn:aws:appstream:{{region}}:{{account-id}}:stack/{{stack-name}}"
    }
  }
}
```

## Compatible frameworks
<a name="agent-access-mcp-server-frameworks"></a>

You can connect to the WorkSpaces Applications MCP server from any MCP-compatible agent framework that supports Streamable HTTP and SigV4 signing. The following frameworks have been tested:
+ [Strands Agents SDK](https://strandsagents.com/docs/user-guide/concepts/tools/mcp-tools/) — Provides native MCP client support.
+ [mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws) — A lightweight transport that handles SigV4 signing for MCP requests in Python.

## Monitoring
<a name="agent-access-mcp-server-monitoring"></a>

You can monitor agent activity through the following services:
+ **AWS CloudTrail** — Agent session events are logged in CloudTrail. You can view when agents connect, which tools they use, and when sessions end. Tool calls are data events and require that you set up a trail to log data events. For more information, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *CloudTrail User Guide*.
+ **CloudWatch** — Operational metrics for agent sessions are available in CloudWatch.
+ **Amazon S3** — If you configure screenshot storage, screenshots captured during agent sessions are available in the Amazon S3 bucket that you specify. Screenshots are stored with the following key format:

  ```
  agentaccess/screenshots/year={{YYYY}}/month={{MM}}/day={{DD}}/{{session-id}}/{{timestamp}}.png
  ```

  The UUID in the path is the WorkSpaces Applications streaming session ID.

## Get started
<a name="agent-access-mcp-server-get-started"></a>

To get started with the WorkSpaces Applications MCP server, see [Get started providing agents with access to WorkSpaces Applications](getting-started-agent-access.md).