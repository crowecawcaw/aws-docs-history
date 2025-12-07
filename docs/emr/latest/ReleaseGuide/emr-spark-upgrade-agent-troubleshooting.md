# Troubleshooting and Q&A

## Troubleshooting

The error message from the upgrade process is available in different ways for different MCP clients. In this page, we list some general guidance for common issues you may see using Apache Spark Upgrade Agent for Amazon EMR.

###### Topics

- [Error: SMUS Managed MCP server failed to load](#spark-upgrade-agent-mcp-server-failed "#spark-upgrade-agent-mcp-server-failed")
- [Observation : Slow Tool Loading](#spark-upgrade-agent-slow-tool-loading "#spark-upgrade-agent-slow-tool-loading")
- [Error: Tool Invocation Failed with Throttling Error](#spark-upgrade-agent-throttling-error "#spark-upgrade-agent-throttling-error")
- [Error: Tool Responds With User Error](#spark-upgrade-agent-user-error "#spark-upgrade-agent-user-error")
- [Error: Tool Responds With Internal Error](#spark-upgrade-agent-internal-error "#spark-upgrade-agent-internal-error")

### Error: SMUS Managed MCP server failed to load

- Verify your MCP configuration are properly configured.
- **Validate JSON syntax**:
  - Ensure your JSON is valid with no syntax errors
  - Check for missing commas, quotes, or brackets

- Verify your local AWS credentials and verify the policy for the MCP IAM role are properly configured.
- Run /mcp to verify MCP server availability for `Kiro-CLI` case

### Observation : Slow Tool Loading

- Tools may take a few seconds to be loaded on first attempt of launching the server.
- If tools don't appear, try restarting the chat,
- Run `/tools` command to verify tool availability.
- Run `/mcp` if the server is launched without error.

### Error: Tool Invocation Failed with Throttling Error

If you hit your service limit, please wait for a few seconds to issue a tool invocation if you see the throttling exception.

### Error: Tool Responds With User Error

- AccessDeniedException - check the error message and fix the permission issue.
- InvalidInputException - check the error message and correct the tool input parameters.
- ResourceNotFoundException - check the error message and fix the input parameter for resource reference.

### Error: Tool Responds With Internal Error

- If you see `The service is handling high-volume requests` please retry the tool invocation in a few seconds.
- If you see `INTERNAL SERVICE EXCEPTION` please document the analysis id, tool name, any error message available from the mcp log or tool response and optional sanitized conversation history and reach out to the AWS support.

## Q&A

### 1. Should I enable "trust" setting for the tools by default?

Do not turn on "trust" setting by default for all tool calls initially and operate on git-versioned build environment. Review each tool execution to understand what changes are being made, for example review the upgrade plan before providing consent. Never trust the Kiro or your Agent's `fs_write` tool - this tool modifies your project files and you should always review changes before they are saved/committed. In general, examine all proposed file changes before allowing them to be written. Use git to version changes and create checkpoints throughout the upgrade process. Build confidence gradually - If you are repeatedly using the system for multiple upgrades and have gained confidence in the tools, you can selectively trust certain tools.

### 2. What are the common example prompts to leverage the upgrade tools?

Please refer to [Prompt Examples for the Spark Upgrade Agent](emr-spark-upgrade-agent-prompt-examples.md "emr-spark-upgrade-agent-prompt-examples.md") for the prompt examples about leveraging upgrade tools.
