

# Troubleshooting AWS Coding Plugin for SAP ABAP
<a name="troubleshooting"></a>

Most problems with AWS Coding Plugin for SAP ABAP ("Coding Plugin") surface as a banner in the chat panel that names the problem and offers an action. The following list covers the problems you are most likely to encounter, most common first.

## Common issues
<a name="troubleshooting-common-issues"></a>

 **The agent cannot reach your SAP ADT MCP server**   
You enable SAP’s ABAP Development Tools (ADT) Model Context Protocol (MCP) server under **Preferences**, **ABAP Development**, **MCP Server**. The server requires a port and a token, both of which the preferences page generates when you enable it.  
The most common causes are:  
+ The ADT MCP server is not running. Toggle it off and on.
+ No token is defined. Open the preferences page and enable the server again to generate one.

 **An MCP server failed to connect**   
When a session starts, the plug-in connects the agent’s MCP servers. If one does not answer, the agent runs without it, and a banner lists the servers that failed.  
+ A server can exceed Kiro’s MCP launch timeout.
+ A failure of the plug-in’s own server is a problem in the plug-in.
+ A failure of a server you defined in `mcp.json` points at that entry.

  In the banner, choose **Reconnect** for a single failed server or **Reconnect all** when several failed. A reconnect can take up to a minute.

 **Kiro CLI is missing, out of date, or signed out**   
The plug-in launches `kiro-cli` to run Kiro. If `kiro-cli` is not installed, is older than the version the plug-in requires, or you are signed out, the plug-in shows a **Fix setup…​** banner. Choose it to open the setup wizard at the step that is not satisfied.  
+ If `kiro-cli` is not installed, install it from [Kiro CLI](https://kiro.dev/cli/) on the Kiro website, then choose **Check Again**.
+ If it is out of date, update it and choose **Check Again**.
+ If you are signed out, follow the wizard to sign in.

 **A chat stops responding**   
A chat can stop because the agent is still working on a long turn, is waiting for you to answer a question or approve a tool call, the connection to `kiro-cli` has dropped, or the plug-in itself is at fault. The plug-in reports which of these it found.  
+ If the agent is still working, let it run, or stop it.
+ If the agent is waiting on you, answer the question or approve or deny the tool call.
+ If Kiro exits, the plug-in attempts to restart it (the tab shows **Reconnecting…​**).
+ A stopped turn shows **Response stopped**, with **Resend** and **Continue**.

## Additional help
<a name="troubleshooting-additional-help"></a>

If the agent is responsive, ask it to diagnose itself. In many cases it can report its own state and read its own logs, and offer an explanation of an error.

If the agent cannot chat with you, a common cause is an expired Kiro login or license. Try running `kiro-cli` directly from the command line to confirm whether the underlying Kiro tool is working.

If you cannot resolve an issue, open a technical support case in the AWS Support Center and attach a diagnostics bundle. Choose **Kiro** as the service and **IDE** as the category. For instructions on collecting a bundle, see [Collecting diagnostics for a support request](#troubleshooting-diagnostics).

## Logging
<a name="troubleshooting-logging"></a>

 AWS Coding Plugin for SAP ABAP writes detailed diagnostic information to a log file on your local machine. You set the log verbosity level in **Preferences**, AWS Coding Plugin for SAP ABAP, **Diagnostics**.

### What is recorded at INFO level
<a name="troubleshooting-logging-info"></a>

At the default INFO level, the main log (`~/.aws_cp4sa/aws_cp4sa.log`) records major lifecycle events: startup steps, the Kiro CLI path and version, the MCP bridge starting and its port, SAP ADT MCP discovery, session create, load, and close events, connection state changes and the reason for any restart, the names of the built-in MCP servers offered to each session, and model selection. It records no chat content — neither your prompts nor the agent’s replies. Two entries do reflect your work: the full path of any file or folder you pin into chat context, and a size estimate, in bytes, of each request sent to the agent.

### What is recorded at DEBUG level
<a name="troubleshooting-logging-debug"></a>

DEBUG level records the same information as the INFO level, and the following additional diagnostic trace: every path checked while locating the CLI, the command used to start it, every protocol message by name and size, every file read, file write, and shell command the agent performs together with your approval decision, every ADT tool call and its timing, hook evaluation including your configured file patterns, and the resolved workspace and project paths. Large values are recorded as a length rather than their contents, so prompt and file text still does not appear. The log level propagates to the Kiro CLI, which writes its own log, `kiro-cli.log`.

### Additional logging settings
<a name="troubleshooting-logging-settings"></a>

Three more checkboxes appear on the **Diagnostics** page when the log verbosity level is DEBUG.
+  **Capture KRS request payloads** (off by default) — Makes the Kiro CLI write the full model-request payloads, the prompts and context actually sent to the model, to `~/.aws_cp4sa/krs-dumps/`, from its next start.
+  **Capture ACP frames** (off by default) — Writes every Agent Client Protocol message exchanged with the CLI, one JSON object per line, to `~/.aws_cp4sa/acp-frames.log`, taking effect on the next message.
+  **Remove chat content from captured frames** (on by default, available only while capture is enabled) — Replaces prompts, replies, file contents, and tool-call titles in that file with a size marker, keeping paths, tool names, and MCP server names. Clearing it records that content as written.

## Collecting diagnostics for a support request
<a name="troubleshooting-diagnostics"></a>

When you contact support, attach a diagnostics bundle.

1. Open **Preferences**, AWS Coding Plugin for SAP ABAP, **Diagnostics**.

1. Choose **Collect Diagnostics**. The plug-in writes a ZIP file.

1. Attach the ZIP file to your support request.

The ZIP file contains the plug-in’s logs, your configuration, a snapshot of the plug-in’s state, and the result of its self-diagnosis.

**Note**  
The bundle includes your chat transcripts (prompts and replies). At the DEBUG log level with **Capture ACP frames** on, raw messages exchanged with Kiro CLI are also captured. Secrets such as tokens are stripped automatically from ACP frames. Review an archive before you share it.