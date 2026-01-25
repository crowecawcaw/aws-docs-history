**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EKS MCP Server Configuration Reference

This guide shows all the configurations available for the [_mcp-proxy-for-aws_](https://github.com/aws/mcp-proxy-for-aws "https://github.com/aws/mcp-proxy-for-aws") client-side tool that allows you to connect to the fully managed Amazon EKS MCP Server from your IDE.

###### Note

The Amazon EKS MCP Server is in preview release for Amazon EKS and is subject to change.

## Example

```
{
  "mcpServers": {
    "eks-mcp": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://eks-mcp.us-west-2.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "default",
        "--region",
        "us-east-1",
        "--read-only"
      ]
    }
  }
}
```

## IAM permissions

The role used for connecting to the MCP server requires **`eks-mcp:InvokeMcp`** permissions for initialization and retrieving information about available tools. **`eks-mcp:CallReadOnlyTool`** is required for usage of read only tools and **`eks-mcp:CallPrivilegedTool`** is required for usage of full access (write) tools.

## Environment variables

**`AWS_PROFILE`** (optional)
AWS credentials profile name to use; can be overridden by the `--profile` command-line argument.

- Example: `export AWS_PROFILE=production`

**`AWS_REGION`** (optional)
AWS region for SigV4 signing; defaults to `us-west-2` if not set.

- Example: `export AWS_REGION=us-east-1`

## Arguments

**SigV4 MCP endpoint URL** (required)
The MCP endpoint URL to connect to.

- Example: `https://eks-mcp.us-west-2.api.aws/mcp`

**`--service`** (optional)
AWS service name for SigV4 signing; auto-detected from the endpoint hostname if not provided.

- Example: `--service eks-mcp`

**`--profile`** (optional)
AWS credentials profile to use. Defaults to the `AWS_PROFILE` environment variable if not specified.

- Example: `--profile production`

**`--region`**
AWS region to use. Uses `AWS_REGION` environment variable if not set, defaults to `us-east-1`.

- Example: `--region us-west-2`

**`--read-only`** (optional)
Disable tools which may require write permissions (tools which DO NOT require write permissions are annotated with readOnlyHint=true). By default, all tools are enabled.

- Example: `--read-only`

For more configuration options, see [Configuration parameters](https://github.com/aws/mcp-proxy-for-aws?tab=readme-ov-file#configuration-parameters "https://github.com/aws/mcp-proxy-for-aws?tab=readme-ov-file#configuration-parameters").

## Tools

For detailed information about all available tools, including parameters and usage examples, see [Amazon EKS MCP Server Tools Reference](eks-mcp-tools.md "eks-mcp-tools.md").
