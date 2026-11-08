

# MCP tool forwarding
<a name="agent-access-mcp-tool-forwarding-details"></a>

With Model Context Protocol (MCP) tool forwarding, agents can work directly with the applications and operating system running on the desktop. They make direct MCP calls instead of using computer-use tools. When you turn on tool forwarding, the MCP server forwards the tools set up on the WorkSpaces Applications session to your agent.

## Setting up tool forwarding
<a name="agent-access-tool-forwarding-setup"></a>

To set up MCP tool forwarding:

**Step 1: Enable tool forwarding**

Turn on the `FORWARD_MCP_TOOLS` agent action through the API or console settings.

**Step 2: Add the configuration file to the fleet's image**

WorkSpaces Applications creates each streaming instance from the fleet's image, so the configuration file must be part of that image. Add it when you build or update the image. A file placed on a running instance does not carry over to new sessions. The service looks for the file at the following location, which depends on the platform:


| Platform | Configuration file path | 
| --- | --- | 
| Windows instances | C:\\ProgramData\\NICE\\dcv\\mcp\_server\_redirection\_config.json | 
| Linux instances | /etc/dcv/mcp\_server\_redirection\_config.json | 

**Step 3: Define the MCP servers in the configuration file**

The configuration file is JSON with a single top-level `mcpServers` object. Each key is a unique name that you choose for a server. Each value specifies how to launch that server.

The following example is for a Windows instance:

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


| Field | Required | Type | Description | 
| --- | --- | --- | --- | 
| command | Yes | String | Absolute path to the executable to launch. | 
| args | No | Array of strings | Arguments passed to the executable. | 

**Step 4: Verify tool availability**

If the configuration file is present, the service connects to the MCP servers it lists and forwards their tools. Forwarded tools appear when the agent lists its available tools.

**Step 5: Test the configuration**

To confirm that tool forwarding works, run the `mcpforwardingtester` script. You can find it in the [sample-code-for-workspaces-agent-access](https://github.com/aws-samples/sample-code-for-workspaces-agent-access/tree/main/utils/mcpforwardingtester) repository on GitHub. The script tests the MCP setup on your WorkSpace. It reports which tools are ready and flags any issues.

**Note**  
Both IAM access and the service setting must be enabled for tool forwarding to work. IAM permissions do not override the service setting.

## MCP tool forwarding considerations
<a name="agent-access-tool-forwarding-considerations"></a>

Note the following considerations when you configure MCP tool forwarding:
+ **Transport is standard I/O (stdio) only.** Each entry must launch a process that speaks MCP over its standard input and output. Remote HTTP or SSE MCP endpoints are not supported. To use a remote endpoint, wrap it in a local stdio server.
+ **Only `command` and `args` are supported.** There is no field for environment variables or working directory. Each server inherits the environment of the streaming session and runs as the session user. Use absolute paths for `command` and for any path arguments.
+ **On Windows instances, use forward slashes in paths.** For example, use `C:/Program Files/my-mcp/server.exe`. JSON treats the backslash as an escape character, so a Windows-style path written with single backslashes is invalid. Windows accepts forward slashes for absolute paths, which avoids the need to escape every separator as `\\`.

## How forwarded tools appear to the agent
<a name="agent-access-tool-forwarding-naming"></a>

To prevent collisions between servers, the MCP server renames each forwarded tool in the agent's tool list using the following pattern:

```
forwarded___{{server-name}}___{{original-tool-name}}
```

The {{server-name}} is the key from your configuration file. For example, a `get_forecast` tool from the `weather` server is listed as `forwarded___weather___get_forecast`. When the agent calls the forwarded name, the MCP server routes the request to the original tool on the owning server. Agent code that matches on tool names must expect this prefix.

## IAM permissions for tool forwarding
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