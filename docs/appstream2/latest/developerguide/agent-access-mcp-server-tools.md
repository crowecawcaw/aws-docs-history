

# Available tools
<a name="agent-access-mcp-server-tools"></a>

The Model Context Protocol (MCP) server provides the following tools, grouped into mouse, keyboard, screen, application, and session tools. Agents use them to operate the desktop during a streaming session. All tool names use the `agentaccess___` prefix.

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

**Note**  
These application tools appear in the agent's tool list only when applications are registered in the fleet image's catalog. If the image has no registered applications, these tools are not available.

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

## Session tools
<a name="agent-access-mcp-tools-session"></a>

The `close_session` tool is part of the stateless MCP protocol (version 2026-07-28). With the earlier MCP protocol versions, you end the session by closing the MCP client in your agent code, which sends an HTTP `DELETE` request instead. For more information, see [Session cleanup](agent-access-mcp-server-session-cleanup.md).

**Note**  
To watch an agent while it works, code the agent to open a streaming URL in a browser. Keep the URL out of the model's context, because it grants session access. You can create the URL in one of two ways:  
Call the `CreateStreamingURL` API with the `stack`, `fleet`, and `userId` values from `get_session_info`, then open the returned URL in a browser.
Read the `streaming_url` value from the `_meta` field of the `get_session_info` response, then open it in a browser.
In both cases, the agent's own code handles the URL, so it never exposes the session credentials to the model.

`get_session_info`  
Return information about the current session.  
Parameters: none.  
Returns the following identifier fields as the tool result: `mcpSessionId`, `stack`, `userId`, `workSpacesSessionId`, and `fleet`.

`close_session`  
The agent calls this tool to end the current session. This closes the MCP session. By default, it does not expire the WorkSpaces Applications streaming session, and the streaming instance is preserved for reuse.  
Parameters: `expire_streaming_session` (optional, Boolean, default `false`). Set it to `true` to also expire the WorkSpaces Applications streaming session, which terminates the streaming instance and triggers the fleet's configured autoscaling policy. For more information about autoscaling, see [Fleet Auto Scaling for Amazon WorkSpaces Applications](autoscaling.md).