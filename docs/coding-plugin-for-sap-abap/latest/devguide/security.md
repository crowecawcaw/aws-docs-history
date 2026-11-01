

# Security
<a name="security"></a>

 AWS Coding Plugin for SAP ABAP ("Coding Plugin") runs on your machine, inside your own Eclipse installation. Its security model is a set of trust boundaries between the parts it connects. These boundaries are: the plug-in and Eclipse, the plug-in and Kiro, Kiro and the Model Context Protocol (MCP) servers, and the path to your SAP system. This chapter describes each boundary and what crosses it.

**Topics**
+ [The plug-in and Eclipse](#security-eclipse)
+ [The plug-in and Kiro](#security-kiro)
+ [Kiro and the MCP servers](#security-mcp)
+ [Reaching your SAP system](#security-sap)
+ [Credential and token handling](#security-credentials)

## The plug-in and Eclipse
<a name="security-eclipse"></a>

Coding Plugin is an OSGi bundle that runs inside your Eclipse installation. It runs with the permissions of your Eclipse session and can read and modify files in your Eclipse workspace. It holds no permission that you do not already have as the developer running Eclipse.

## The plug-in and Kiro
<a name="security-kiro"></a>

On your machine, Coding Plugin launches Kiro CLI as a child process and communicates with it over a local stdio pipe. Communication between Coding Plugin and Kiro does not cross the network.

Kiro CLI handles sign-in to the backend service, using any sign-in option that Kiro supports, such as AWS Builder ID or AWS IAM Identity Center. For more information about sign-in options, see [Authentication](https://kiro.dev/docs/getting-started/authentication/) on the Kiro website.

### What data leaves your machine
<a name="security-data"></a>

Your prompts, and the code context the agent gathers, are sent by Kiro CLI to the Kiro backend service, which runs the model. How that data is handled is governed by Kiro. See [Privacy and security](https://kiro.dev/docs/privacy-and-security/) in the Kiro documentation. Coding Plugin adds no separate data collection of its own.

## Kiro and the MCP servers
<a name="security-mcp"></a>

Kiro CLI connects to MCP servers configured in `mcp.json`.

The two ADT-related MCP servers (the SAP ADT MCP server, and Coding Plugin’s MCP server) are a special case:

The Coding Plugin MCP server is reachable only by your Kiro CLI:
+ It binds to `localhost` (`127.0.0.1`) only and is never exposed on the network.
+ It listens on an ephemeral port chosen when it starts.
+ Its URL paths are randomized.
+ Access requires a bearer token that is regenerated each time the server starts.

The connection from Kiro to the MCP server is configured through `stdio`, outside of `mcp.json`, so that the bearer token is never written to persistent storage.

Coding Plugin also automatically configures the connection from Kiro to SAP’s ADT MCP server using the `stdio` channel instead of `mcp.json`. The plug-in never writes SAP’s bearer token to persistent storage.

## Reaching your SAP system
<a name="security-sap"></a>

The agent reaches your SAP system only through the SAP ADT connection you have already defined in Eclipse. This connection is authenticated to SAP by the SAP ADT plugin, and Coding Plugin never gains access to these credentials. The plug-in stores no SAP credentials of its own.

Every read and write runs as your SAP user. The agent can do nothing on the system that your user cannot do, and SAP’s own authority checks apply to its actions exactly as they apply to yours. Your SAP authorizations such as `S_DEVELOP` and the transport layer remain the fundamental control.

Developers often have powerful permissions in the development system, and so does Coding Plugin. You can constrain the agent’s actions through steering and prompts. For example, your steering files can contain instructions such as "never modify code in the `Z_HCM` package". However, steering is not a security measure. A large language model (LLM) can ignore steering because of context rot, conflicting instructions, or misunderstanding it. Your SAP authorizations remain the fundamental control.

Every tool call the agent makes is gated by Kiro Permissions, Kiro’s mechanism for approving the agent’s actions. See [Kiro Permissions](kiro-permissions.md).

## Credential and token handling
<a name="security-credentials"></a>
+  **Kiro sign-in** is managed by Kiro CLI. The plug-in does not have access to Kiro’s credentials to the backend service.
+  **Your SAP logon** is your existing ADT connection. The plug-in does not have access to your SAP credentials.
+  **SAP ADT’s MCP server token**: SAP mints it and persists it in its own Eclipse preference store. Coding Plugin reads it from there and keeps no copy of its own.
+  **The plug-in’s MCP server bearer token**: Coding Plugin holds it in memory, regenerates it each time the server starts, and never persists it.