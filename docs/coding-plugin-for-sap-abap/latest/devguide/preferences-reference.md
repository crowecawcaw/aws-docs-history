

# AWS Coding Plugin for SAP ABAP preferences reference
<a name="preferences-reference"></a>

 AWS Coding Plugin for SAP ABAP ("Coding Plugin") adds its own preferences to Eclipse, separate from Kiro’s configuration.

## AWS Coding Plugin for SAP ABAP preferences
<a name="preferences-reference-settings"></a>

Open the preferences from **Preferences**, AWS Coding Plugin for SAP ABAP. The page you land on holds the connection to Kiro and to SAP. The rest of the settings are grouped by task on four subpages. Eclipse lists them in this order: **Onboarding**, **Behavior**, **MCP Servers**, and **Diagnostics**.

### Main page
<a name="preferences-reference-main"></a>
+  **Kiro CLI location** shows the status of the `kiro-cli` binary and holds the path to it. Edit the path directly, choose **Browse** to pick the file, or choose **Test** to check the path you entered. A blank path means Coding Plugin detects `kiro-cli` on your `PATH`.
+  **Log in to Kiro** starts the Kiro CLI authentication flow, so you can sign in without leaving Eclipse.
+  **ADT Status** reports whether SAP ABAP Development Tools (ADT) is installed, and links to the installation if it is not.

### Onboarding
<a name="preferences-reference-onboarding"></a>
+  **Show Welcome on startup** opens the Welcome wizard the next time Eclipse starts.
+ The **Onboarding nudges** checkboxes each suppress one of the one-time offers: to take the guided tour of the chat panel, to set up steering for the workspace, or to set up steering for a connected SAP system. The SAP setting applies to every SAP system you connect to.
+  **Run Welcome Wizard** opens the onboarding wizard now, without restarting Eclipse.

### Behavior
<a name="preferences-reference-behavior"></a>
+  **Terminal command timeout (seconds)** is how long a command may run before Coding Plugin stops it. The timeout is not a gate on whether a command runs at all: the agent asks you to approve each command first, and does not run it if you decline. See [Kiro Permissions](kiro-permissions.md).
+  **Session/prompt timeout (seconds)** is how long a prompt may run before it times out.
+  **Recent conversations to list** is how many past conversations the chat panel’s recent-conversations selector offers, newest first. Set it to `0` to list every conversation the agent remembers.
+  **Warning threshold (%)** and **Critical threshold (%)** are percentages of the context window. When usage crosses the warning threshold, Kiro compacts the conversation automatically. Crossing the critical threshold escalates the warning and fires a safety-net compaction if one is not already in progress. For more about the context window, see [Using the chat](using-chat.md).
+  **Detect spec-building prompts and offer to switch to Spec mode** offers to switch to Spec mode when a prompt looks like it is describing a feature to build.

### MCP Servers
<a name="preferences-reference-mcp-servers"></a>

This page covers your Model Context Protocol (MCP) servers, and which of the plug-in’s own tools the agent can reach.
+  **User MCP servers** and **Workspace MCP servers** give the path of each `mcp.json` file, with a link that opens it, or creates it from a starter template if it does not exist yet. The workspace row becomes available once a Coding Plugin project is open. Kiro reads these files itself, so an entry you add takes effect on your next session.
+  **Bridge Tool Categories** selects which categories of the plug-in’s own tools the agent can see and call: **Coding Plugin Introspection**, **Eclipse tools**, and **Additional SAP ADT functions**. Clearing a category hides its tools from the agent. Changes take effect after a session restart.

### Diagnostics
<a name="preferences-reference-diagnostics"></a>

Use these settings to capture logs when you report a problem.
+  **Log verbosity level** sets how much detail the plug-in records: `ERROR`, `WARN`, `INFO`, or `DEBUG`.
+  **Capture KRS request payloads (requires restart)** and **Capture ACP frames** record the full model requests, and the Agent Client Protocol (ACP) messages exchanged with Kiro CLI. Both are available only at the `DEBUG` verbosity level. **Remove chat content from captured frames**, available while frame capture is on, replaces prompts, replies, and file contents in the frame log with a size marker.
+  **Collect Diagnostics** bundles the logs, your chat transcripts, and the plug-in’s configuration into a single archive you can attach to a support case.
+  **Record usage metrics in the log** writes each turn’s token counts, credit usage, duration, and context usage to the log file on your own machine. Nothing is sent off your machine.
+  **Read `mcp.json` files for diagnostics** gives Coding Plugin read-only access to your user-level and workspace-level `mcp.json` files. The read serves diagnostics alone: it warns you when one of your entries targets SAP’s built-in ADT MCP endpoint, and it records an entry count in a diagnostics archive. Kiro reads and honors your `mcp.json` files regardless of this setting; see [Architecture](architecture.md) in How AWS Coding Plugin for SAP ABAP works.

**Warning**  
At the `DEBUG` verbosity level, and when **Capture ACP frames** is on, the captured logs can include your prompts and chat transcripts. A diagnostics archive also bundles your chat transcripts. If you share an archive without reviewing it first, you can expose the contents of your prompts and transcripts to whoever receives it.

For when and how to collect diagnostics while troubleshooting, see [Troubleshooting](troubleshooting.md).

## Theme, fonts, and colors
<a name="preferences-reference-appearance"></a>

The chat panel follows Eclipse’s own appearance settings, so it matches the rest of your IDE and changes live when you adjust them.
+  **Theme.** The chat panel supports both light and dark themes. Choose a theme under **Preferences**, **General**, **Appearance**. The panel repaints to match.
+  **Fonts and text size.** Set the chat text under **Preferences**, **General**, **Appearance**, **Colors and Fonts**, in the AWS Coding Plugin category. **Content Font** sets the transcript and input text (the size of headings scales with it). **Chrome Font** sets the tab strip, buttons, and status areas.
+  **Colors.** The same AWS Coding Plugin category lets you override the chat card, code block, and accent colors. If you do not override them, the panel derives its colors from your current theme.