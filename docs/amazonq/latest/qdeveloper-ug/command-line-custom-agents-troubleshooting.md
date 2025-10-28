# Troubleshooting

This section covers common issues you might encounter when working with custom agents and how to resolve them.

## Configuration errors

### Invalid JSON syntax

**Problem:** Custom agent fails to load with JSON parsing errors.

**Symptoms:**

- Error messages mentioning "invalid JSON" or "syntax error"
- Custom agent not appearing in `/agent list`
- Fallback to default agent behavior

**Solutions:**

- Validate your JSON using a JSON validator or linter
- Check for common JSON errors:
  - Missing commas between array elements or object properties
  - Trailing commas after the last element
  - Unmatched brackets or braces
  - Unescaped quotes in string values

- Use `/agent schema` to verify your configuration structure

### Schema validation errors

**Problem:** Custom agent configuration doesn't match the expected schema.

**Symptoms:**

- Warnings about unknown configuration fields
- Custom agent behavior not matching configuration
- Missing required fields errors

**Solutions:**

- Compare your configuration against the schema using `/agent schema`
- Check field names for typos (e.g., `allowedTools` vs `allowedTool`)
- Verify data types match schema requirements (arrays vs strings, booleans vs strings)
- Review the [agent format documentation](https://github.com/aws/amazon-q-developer-cli/blob/main/docs/agent-format.md "https://github.com/aws/amazon-q-developer-cli/blob/main/docs/agent-format.md") in the supplementary Amazon Q Developer CLI documentation for correct syntax

## Custom agent loading issues

### Custom agent not found

**Problem:** Custom agent doesn't appear in the list or can't be used.

**Symptoms:**

- `/agent list` doesn't show your custom agent
- `/agent use [name]` fails with "agent not found"
- Fallback to default agent without warning

**Solutions:**

- Verify the custom agent file is in the correct location:
  - Global: `~/.aws/amazonq/cli-agents/[name].json`
  - Local: `amazonq/cli-agents/[name].json`

- Check file permissions - ensure the file is readable
- Verify the filename matches the custom agent name you're trying to use
- Ensure the file has a `.json` extension

### Wrong custom agent version loading

**Problem:** A different version of your custom agent is loading than expected.

**Symptoms:**

- Custom agent behavior doesn't match your recent configuration changes
- Warning message about custom agent conflicts
- Unexpected tool availability or permissions

**Solutions:**

- Check for custom agent name conflicts between local and global directories
- Remember that local custom agents take precedence over global custom agents
- Use `/agent list` to see which version is being loaded
- Remove or rename conflicting custom agent files if necessary

## Tool permission problems

### Tool not available

**Problem:** Custom agent can't access a tool you've configured.

**Symptoms:**

- Error messages about unknown or unavailable tools
- Custom agent asking for permission for tools in `allowedTools`
- MCP server tools not working

**Solutions:**

- Verify tool names are spelled correctly in the `tools` array
- For MCP tools, ensure the server is properly configured in `mcpServers`
- Check that MCP servers are running and accessible
- Use correct syntax for MCP tools: `@server_name/tool_name`
- Verify built-in tool names against the [built-in tools documentation](https://github.com/aws/amazon-q-developer-cli/blob/main/docs/built-in-tools.md "https://github.com/aws/amazon-q-developer-cli/blob/main/docs/built-in-tools.md") in the supplementary Amazon Q Developer CLI documentation

### /tools command returns empty list

**Problem:** The `/tools` command shows no available tools or fewer tools than expected.

**Symptoms:**

- `/tools` returns an empty list
- Expected tools are missing from the tools list
- Custom agent appears to have no capabilities

**Common causes:**

- Empty `tools` array in the custom agent configuration
- Typos in tool names within the `tools` array
- Incorrect MCP server tool names (missing server prefix)
- MCP server configuration issues preventing tool loading

**Solutions:**

- Check that your custom agent configuration includes a `tools` array with valid tool names
- Verify tool names are spelled correctly (case-sensitive)
- For MCP tools, ensure you're using the correct server-prefixed format: `server-name___tool-name`
- Test with the default agent to confirm tools are available: `q chat` then `/tools`
- Check MCP server status if using external tools

### Unexpected permission prompts

**Problem:** Custom agent prompts for permission for tools you thought were pre-approved.

**Symptoms:**

- Permission prompts for tools listed in `allowedTools`
- Workflow interruptions despite custom agent configuration

**Solutions:**

- Ensure tools are listed in both `tools` and `allowedTools` arrays
- Check for typos in tool names between the two arrays
- For MCP tools, use the full server-prefixed name in `allowedTools`
- Verify that `toolAliases` are correctly applied

## Debugging custom agent behavior

### Missing context or resources

**Problem:** Custom agent doesn't seem to have access to expected files or context.

**Solutions:**

- Verify file paths in the `resources` array are correct and files exist
- Check that glob patterns in resources are matching the intended files
- Ensure hook commands are executing successfully and producing output
- Test hook commands manually to verify they work in your environment
- Check hook timeout settings if commands are being cut off

### MCP server issues

**Problem:** MCP servers aren't working or tools aren't available.

**Solutions:**

- Verify MCP server commands are correct and executables are in your PATH
- Check that required environment variables are set
- Test MCP servers independently to ensure they're working
- Review MCP server logs for error messages
- Increase timeout values if servers are slow to start
- For more MCP troubleshooting, see [Using MCP with Amazon Q Developer](qdev-mcp.md "qdev-mcp.md")

### Testing custom agent configurations

To systematically test your custom agent configuration:

1. Validate JSON syntax using a JSON validator
2. Check configuration against schema using `/agent schema`
3. Test custom agent loading with `/agent list`
4. Switch to the custom agent with `/agent use [name]`
5. Test each tool individually to verify access and permissions
6. Verify that resources and hooks are providing expected context
7. Test common workflows to ensure the custom agent behaves as expected

## Getting additional help

If you continue to experience issues with agents:

- Review the complete [agent configuration documentation](https://github.com/aws/amazon-q-developer-cli/blob/main/docs/agent-format.md "https://github.com/aws/amazon-q-developer-cli/blob/main/docs/agent-format.md") in the supplementary Amazon Q Developer CLI documentation
- Check the [built-in tools reference](https://github.com/aws/amazon-q-developer-cli/blob/main/docs/built-in-tools.md "https://github.com/aws/amazon-q-developer-cli/blob/main/docs/built-in-tools.md") for tool-specific configuration
- Consult the [MCP documentation](qdev-mcp.md "qdev-mcp.md") for MCP-related issues
- Start with simpler agent configurations and gradually add complexity
- Compare your configuration with the examples in [Agent examples and use cases](command-line-custom-agents-examples.md "command-line-custom-agents-examples.md")
- Remember that agent switching and editing requires starting new chat sessions rather than using in-session commands
