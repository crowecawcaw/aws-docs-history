

# Available tools

The Model Context Protocol (MCP) server provides the following tools, grouped into mouse, keyboard, screen, application, sequencing, session, and user tools. Agents use them to operate the desktop during a streaming session. All tool names use the `agentaccess___` prefix.

The tools available to an agent depend on whether the session is on a stack or on an image builder. Application tools are available only on stacks, and user tools are available only on image builders.

## Mouse tools
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
Parameters: `x` (required), `y` (required), `scroll_direction` (required, one of `Up`, `Down`, `Left`, or `Right`), `scroll_amount` (required, in ticks, where 120 ticks equals one wheel notch), `modifiers` (optional).

## Keyboard tools
<a name="agent-access-mcp-tools-keyboard"></a>

`type_text`  
Type text by simulating keyboard events for each character.  
Parameters: `text` (required, up to 10,000 characters).

`key`  
Press a key or key combination.  
Parameters: `keys` (required, a single key or combination joined by `+`, for example `a`, `ctrl+c`, or `ctrl+shift+s`).

`hold_key`  
Hold a key or key combination for a specified duration.  
Parameters: `keys` (required), `duration` (required, 1 to 30 seconds).

## Screen tools
<a name="agent-access-mcp-tools-screen"></a>

`screenshot`  
Capture a screenshot of the desktop. The returned image dimensions define the coordinate space for all mouse tools.  
Parameters: `include_cursor` (optional, defaults to `false`).

## Application tools
<a name="agent-access-mcp-tools-application"></a>

Application tools appear in the agent's tool list only when applications are registered in the fleet image's catalog. If the image has no registered applications, these tools are not available.

`launch_application`  
Launch an application from the ones available in the fleet image's catalog.  
Parameters: `id` (required). The application identifier.  
The tool's own description lists the identifiers of the available applications. The MCP server populates this description from the fleet image's catalog (for example, `firefox`, `notepad++`, or `eclipse`). Use one of the listed identifiers. An `id` that is not in the catalog returns `isError: true` with `SERVER_ERROR: Invalid input`. IDs are set when the image is built. You cannot determine an ID from the application name.  
Launching an application does not replace what is already running. The previously launched application stays open. That is why the app switcher exists.

`toggle_app_switcher`  
Open or close the app-switcher overlay.  
Parameters: none.  
This tool only toggles the overlay. To bring a particular application to the foreground, follow up with a `left_click` on its thumbnail, using coordinates read from a screenshot. No tool reports which application is currently in the foreground, so an agent that needs to know must capture a screenshot and look.  
The app switcher is available only when the fleet's **Stream view** is set to **Application**, which displays only the windows of applications that users open. It is not available when **Stream view** is set to **Desktop**, because WorkSpaces Applications then provides the standard desktop and taskbar for the operating system.

## Sequencing tools
<a name="agent-access-mcp-tools-sequencing"></a>

Use these tools to run several actions in one call, and to pace them, instead of making a separate tool call for each step.

`execute_sequence`  
Run several tool calls in one call, in order. Each item in the `actions` list is an object with a `type` that names the tool to run. Write the `type` the same way the tool appears in `tools/list`, for example `agentaccess___left_click` or `agentaccess___wait`. Include that tool's own arguments as sibling keys, not nested. For example:  

```
[{"type": "agentaccess___type_text", "text": "hello"},
 {"type": "agentaccess___key", "keys": "Tab"}]
```
The sequence stops at the first failure. You cannot use `screenshot` or `execute_sequence` inside a sequence. If the sequence succeeds, the MCP server pauses briefly and returns a final screenshot. If the last action in the sequence is a `wait`, the server skips this pause. You can end a sequence with a `wait` to set your own delay after a slow action, such as opening a window. If an action fails or the sequence reaches the time limit, the MCP server returns text only. It includes guidance to take a screenshot before the next action.  
A sequence has the following limits. If a sequence exceeds any limit, the MCP server rejects it before any action runs:  
+ A sequence can include at most 20 actions.
+ Each `wait` lasts 0.001 to 5 seconds, and all waits together last at most 10 seconds.
+ All `type_text` text together totals at most 10,000 characters.
+ The entire sequence stops after 60 seconds.
Parameters: `actions` (required, a list of action objects).  
The following example request fills in a form and submits it. It enters text in three fields, presses Enter to submit, and ends with a `wait` so the page has time to update:  

```
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 5,
  "params": {
    "name": "agentaccess___execute_sequence",
    "arguments": {
      "actions": [
        {"type": "agentaccess___left_click", "x": 450, "y": 320},
        {"type": "agentaccess___type_text", "text": "Jane Doe"},
        {"type": "agentaccess___key", "keys": "Tab"},
        {"type": "agentaccess___type_text", "text": "Seattle"},
        {"type": "agentaccess___key", "keys": "Tab"},
        {"type": "agentaccess___type_text", "text": "Please add me to the newsletter."},
        {"type": "agentaccess___key", "keys": "Enter"},
        {"type": "agentaccess___wait", "duration": 2}
      ]
    }
  }
}
```

`wait`  
Pause for `duration` seconds without interacting with the desktop. Use `wait` on its own, or as an action inside `execute_sequence` to pace actions that need time to settle.  
Parameters: `duration` (required, 0.001 to 5 seconds).

## Session tools
<a name="agent-access-mcp-tools-session"></a>

The `close_session` tool is part of the stateless MCP protocol (version 2026-07-28). With the earlier MCP protocol versions, you end the session by closing the MCP client in your agent code, which sends an HTTP `DELETE` request instead. For more information, see [Session cleanup](agent-access-mcp-server-session-cleanup.md).

**Note**  
To watch an agent while it works, code the agent to open a streaming URL in a browser. The `get_session_info` tool doesn't return a streaming URL, but its values let your agent's code create one:  
On a stack, call the `CreateStreamingURL` API with the `stack`, `fleet`, and `userId` values from `get_session_info`.
On an image builder, call the `CreateImageBuilderStreamingURL` API with the image builder name. The name is the last part of the `imageBuilder` ARN from `get_session_info`.
Then read the `streaming_url` value from the `_meta` field of your MCP client, and open it in a browser. The full URL contains session credentials, so keeping it in `_meta` keeps it out of the model's context.

`get_session_info`  
Return information about the current session.  
Parameters: none.  
Returns the following identifier fields as the tool result: `mcpSessionId`, `stack`, `userId`, `workSpacesSessionId`, and `fleet`.  
On an image builder session, returns `mcpSessionId`, `workSpacesSessionId`, and `imageBuilder` (the ARN of the image builder).

`close_session`  
The agent calls this tool to end the current session. This closes the MCP session. By default, it does not expire the WorkSpaces Applications streaming session, and the streaming instance is preserved for reuse.  
Parameters: `expire_streaming_session` (optional, Boolean, default `false`). The following values are available:  
+ `true` – The MCP server also expires the WorkSpaces Applications streaming session.
  + On a fleet, this terminates the streaming instance and triggers the fleet's configured autoscaling policy. For more information, see [Fleet Auto Scaling for Amazon WorkSpaces Applications](autoscaling.md).
  + On an image builder, this doesn't end the streaming session. The streaming session and the built-in users that the agent logged in keep running until you stop the image builder. Stopping the image builder ends its streaming session and logs out all users.
+ `false` (default) – The streaming session continues running.
  + On a fleet, the session runs until the disconnect timeout is reached. For more information about the disconnect timeout, see [Create a Fleet in Amazon WorkSpaces Applications](set-up-stacks-fleets-create.md).
  + On an image builder, the session runs until you stop the image builder. For more information, see [Image Builder Actions](managing-image-builders-actions.md).

## User tools
<a name="agent-access-mcp-tools-user"></a>

User tools control which built-in user is logged in to the image builder. The logged-in built-in user determines which actions the agent can perform, because each built-in user has different permissions on the image builder. These tools are available only on image builders. For more information about connecting as a built-in user, see [Connecting with image builders](agent-access-mcp-server-endpoint.md#agent-access-mcp-server-connect-image-builder).

`switch_user`  
Disconnect the current built-in user's Windows session and log in another built-in user. The previous user's session keeps running.  
Parameters: `user` (required, one of `ADMINISTRATOR`, `TEMPLATE_USER`, or `TEST_USER`). These are the same values as the `x-amzn-agentaccess-local-user` header.

`get_current_user`  
Return the built-in user that is logged in to the image builder.  
Parameters: none.  
Returns the logged-in built-in user.