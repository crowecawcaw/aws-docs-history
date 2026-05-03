# WorkSpaces Applications MCP server

The WorkSpaces Applications MCP server is a fully managed service that provides
AI agents with Model Context Protocol (MCP) tools to interact with desktop
applications during streaming sessions. Agents can click buttons, enter text,
scroll, and take screenshots of the desktop.

## Overview

When you enable agent access on a stack, agents can connect to the managed
MCP server to interact with desktop applications. The MCP server handles the
communication between your agent and the streaming session. Your agent sends
MCP tool requests, and the server executes them on the desktop.

The MCP server is hosted in the AWS cloud. You don't need to install or
maintain any server components. The server uses Streamable HTTP as its
transport protocol.

## Connecting to the MCP server

Agents connect to the MCP server at the following endpoint:

```
https://agentaccess-mcp.`region`.api.aws/mcp
```

Each request must include the following:

- **SigV4 signing** — All requests
  must be signed using IAM credentials with the service name
  `agentaccess-mcp`.
- **Streaming URL header** — The
  streaming URL from the `CreateStreamingURL` API must be
  passed as the
  `X-Amzn-AgentAccess-Streaming-Session-Url`
  header on every request.

The following Python example shows how to connect using
`mcp-proxy-for-aws`:

```
aws_iam_streamablehttp_client(
    endpoint="https://agentaccess-mcp.`region`.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region="`region`",
    headers={
        "X-Amzn-AgentAccess-Streaming-Session-Url": streaming_url,
    },
)
```

For other languages, you need to write your own signing logic for
outgoing MCP requests or find an available library that supports SigV4
signing.

For more information about `mcp-proxy-for-aws`, see
[mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws "https://github.com/aws/mcp-proxy-for-aws")
on GitHub.

## Available tools

The MCP server provides the following tools for agents to interact with
the desktop during a streaming session. All tool names use the
`agentaccess___` prefix.

### Mouse tools

`left_click`

Perform a left click at the given coordinates.

Parameters: `x` (required), `y` (required),
`modifiers` (optional, for example `ctrl` or
`ctrl+shift`).

`double_click`

Perform a double click at the given coordinates.

Parameters: `x` (required), `y` (required),
`modifiers` (optional).

`triple_click`

Perform a triple click at the given coordinates.

Parameters: `x` (required), `y` (required),
`modifiers` (optional).

`right_click`

Perform a right click at the given coordinates.

Parameters: `x` (required), `y` (required),
`modifiers` (optional).

`middle_click`

Perform a middle click at the given coordinates.

Parameters: `x` (required), `y` (required),
`modifiers` (optional).

`left_click_drag`

Perform a left click drag from start coordinates to end
coordinates.

Parameters: `start_x` (required),
`start_y` (required), `end_x` (required),
`end_y` (required).

`left_mouse_down`

Press and hold the left mouse button at the given
coordinates.

Parameters: `x` (required), `y` (required),
`modifiers` (optional).

`left_mouse_up`

Release the left mouse button at the given coordinates.

Parameters: `x` (required), `y` (required),
`modifiers` (optional).

`move_pointer`

Move the pointer to the given coordinates.

Parameters: `x` (required),
`y` (required).

`scroll`

Scroll the mouse wheel at the given coordinates.

Parameters: `x` (required), `y` (required),
`scroll_direction` (required — `Up`,
`Down`, `Left`, or `Right`),
`scroll_amount` (required — in ticks, where
120 ticks equals one wheel notch),
`modifiers` (optional).

### Keyboard tools

`type_text`

Type text by simulating keyboard events for each
character.

Parameters: `text` (required — up to
10,000 characters).

`key`

Press a key or key combination.

Parameters: `keys` (required — a single key
or combination joined by `+`, for example
`a`, `ctrl+c`, or
`ctrl+shift+s`).

`hold_key`

Hold a key or key combination for a specified duration.

Parameters: `keys` (required),
`duration` (required — 1 to 30 seconds).

### Screen tools

`screenshot`

Capture a screenshot of the desktop. The returned image
dimensions define the coordinate space for all mouse tools.

Parameters: `include_cursor` (optional —
defaults to `false`).

## Compatible frameworks

You can connect to the WorkSpaces Applications MCP server from any
MCP-compatible agent framework that supports Streamable HTTP and SigV4
signing. The following frameworks have been tested:

- [Strands
  Agents SDK](https://strandsagents.com/docs/user-guide/concepts/tools/mcp-tools/ "https://strandsagents.com/docs/user-guide/concepts/tools/mcp-tools/") — Provides native MCP client support.
- [mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws "https://github.com/aws/mcp-proxy-for-aws")
  — A lightweight transport that handles SigV4 signing for
  MCP requests in Python.

## Monitoring

You can monitor agent activity through the following services:

- **AWS CloudTrail** — Agent session
  events are logged in CloudTrail. You can view when agents connect, which
  tools they use, and when sessions end. Tool calls are data events
  and require that you set up a trail to log data events. For more
  information, see [Logging
  data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") in the _CloudTrail User Guide_.
- **CloudWatch** — Operational metrics
  for agent sessions are available in CloudWatch.
- **Amazon S3** — If you configure
  screenshot storage, screenshots captured during agent sessions are
  available in the Amazon S3 bucket that you specify. Screenshots are stored
  with the following key format:

```
agentaccess/screenshots/year=`YYYY`/month=`MM`/day=`DD`/`session-id`/`timestamp`.png
```

The UUID in the path is the WorkSpaces Applications streaming session ID.

## Get started

To get started with the WorkSpaces Applications MCP server, see
[Get started providing agents with access to WorkSpaces Applications](getting-started-agent-access.md "getting-started-agent-access.md").
