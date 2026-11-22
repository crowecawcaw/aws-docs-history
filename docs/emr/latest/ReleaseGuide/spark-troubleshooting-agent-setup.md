

# Set up the Apache Spark agents

**Note**  
The Apache Spark agents use cross-Region inference to process natural language requests and generate responses. For more information, see [Cross-Region processing for the Apache Spark agents](spark-troubleshooting-cross-region-processing.md).

**Note**  
Both agents use the `sagemaker-unified-studio-mcp-troubleshooting` server and the `/spark-troubleshooting/mcp` endpoint, despite "troubleshooting" in the names. Both agents use the same setup. If you've already set up one agent, you can use the other on the same platforms without additional setup. Only the troubleshooting agent uses the code recommendation server, `sagemaker-unified-studio-mcp-code-rec` (`/spark-code-recommendation/mcp`). If you use only the optimization agent, you can skip it.

## Prerequisites
<a name="spark-troubleshooting-agent-prerequisites"></a>

Before you begin the setup for integration with Kiro CLI, make sure that you have the following installed on your workstation:
+ [Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
+ [Install Python 3.10\+](https://www.python.org/downloads/release/python-3100/)
+ [Install the `uv` package manager](https://docs.astral.sh/uv/getting-started/installation/) for [MCP Proxy for AWS](https://github.com/aws/mcp-proxy-for-aws?tab=readme-ov-file)
+ [Install Kiro CLI](https://kiro.dev/docs/cli/)
+ AWS local credentials configured (through the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html), environment variables, or IAM roles). The MCP Proxy for AWS uses these credentials to authenticate the agents' requests to AWS services as your IAM identity.

## How the agents access your resources
<a name="spark-agents-setup-access"></a>

The MCP server authorizes operations at the AWS service level using the IAM identity that your MCP client is configured with. The agents act as that identity, so they can only access what that identity is permitted to access. No separate MCP-specific permissions are required.

Point the MCP client at an AWS profile for a role that you already use to analyze your Spark jobs today. The agents' access then matches your own. Make sure that role carries the permissions described in [IAM permissions for the Apache Spark agents](spark-troubleshooting-agent-iam-setup.md) so the agents can read all the signals from your Spark jobs.

If you want tighter, scoped control over what the agents can access, see [How can I get more fine-grained control over the agents' permissions?](spark-troubleshooting-agent-iam-setup.md#qa-fine-grained-permissions). To give the agents their own role, see [How do I create a dedicated IAM role for the agents?](spark-troubleshooting-agent-iam-setup.md#qa-dedicated-role).

## Add the Apache Spark agents to your MCP client
<a name="spark-agents-setup-add-servers"></a>

The agents use the AWS profile that you pass to the MCP servers. Use a profile for a role you already have. If your default profile already uses that role, use it. Otherwise, create a profile that assumes the role, replacing `your-role-name` with your role's name:

```
aws configure set profile.smus-mcp-profile.role_arn arn:aws:iam::111122223333:role/your-role-name
aws configure set profile.smus-mcp-profile.source_profile default
aws configure set profile.smus-mcp-profile.region <your mcp server launch region>
```

For the permissions the role needs, see [IAM permissions for the Apache Spark agents](spark-troubleshooting-agent-iam-setup.md).

To set your Region and add the MCP servers, run the following commands. Point `--profile` at the profile for the role you use. This example uses the `smus-mcp-profile` profile from the previous step. If you use a different profile, replace it.

```
export SMUS_MCP_REGION=<your mcp server launch region>

# Add Spark Troubleshooting and Optimization MCP Server
kiro-cli-chat mcp add \
    --name "sagemaker-unified-studio-mcp-troubleshooting" \
    --command "uvx" \
    --args "[\"mcp-proxy-for-aws@latest\",\"https://sagemaker-unified-studio-mcp.${SMUS_MCP_REGION}.api.aws/spark-troubleshooting/mcp\", \"--service\", \"sagemaker-unified-studio-mcp\", \"--profile\", \"smus-mcp-profile\", \"--region\", \"${SMUS_MCP_REGION}\", \"--read-timeout\", \"180\"]" \
    --timeout 180000 \
    --scope global

# If you use Claude Code, use the following command instead
# claude mcp add --scope user \
#     sagemaker-unified-studio-mcp-troubleshooting \
#  -- uvx mcp-proxy-for-aws@latest \
#     https://sagemaker-unified-studio-mcp.${SMUS_MCP_REGION}.api.aws/spark-troubleshooting/mcp \
#     --service sagemaker-unified-studio-mcp \
#     --profile smus-mcp-profile \
#     --region ${SMUS_MCP_REGION} \
#     --read-timeout 180

# Add Spark Code Recommendation MCP Server
kiro-cli-chat mcp add \
    --name "sagemaker-unified-studio-mcp-code-rec" \
    --command "uvx" \
    --args "[\"mcp-proxy-for-aws@latest\",\"https://sagemaker-unified-studio-mcp.${SMUS_MCP_REGION}.api.aws/spark-code-recommendation/mcp\", \"--service\", \"sagemaker-unified-studio-mcp\", \"--profile\", \"smus-mcp-profile\", \"--region\", \"${SMUS_MCP_REGION}\", \"--read-timeout\", \"180\"]" \
    --timeout 180000 \
    --scope global

# If you use Claude Code, use the following command instead
# claude mcp add --scope user \
#     sagemaker-unified-studio-mcp-code-rec \
#  -- uvx mcp-proxy-for-aws@latest \
#     https://sagemaker-unified-studio-mcp.${SMUS_MCP_REGION}.api.aws/spark-code-recommendation/mcp \
#     --service sagemaker-unified-studio-mcp \
#     --profile smus-mcp-profile \
#     --region ${SMUS_MCP_REGION} \
#     --read-timeout 180
```

This updates `~/.kiro/settings/mcp.json` to include the MCP server configuration as follows. If you use Claude Code, the command updates `~/.claude.json` instead.

```
{
  "mcpServers": {
    "sagemaker-unified-studio-mcp-troubleshooting": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://sagemaker-unified-studio-mcp.us-east-1.api.aws/spark-troubleshooting/mcp",
        "--service",
        "sagemaker-unified-studio-mcp",
        "--profile",
        "smus-mcp-profile",
        "--region",
        "us-east-1",
        "--read-timeout",
        "180"
      ],
      "timeout": 180000,
      "disabled": false
    },
    "sagemaker-unified-studio-mcp-code-rec": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://sagemaker-unified-studio-mcp.us-east-1.api.aws/spark-code-recommendation/mcp",
        "--service",
        "sagemaker-unified-studio-mcp",
        "--profile",
        "smus-mcp-profile",
        "--region",
        "us-east-1",
        "--read-timeout",
        "180"
      ],
      "timeout": 180000,
      "disabled": false
    }
  }
}
```

## Configure your MCP client
<a name="integration-other-mcp-clients"></a>

You can also use the preceding configuration in other MCP clients and IDEs to connect to the managed MCP server:
+ **Integration with Claude Code** – To use the MCP server with Claude Code, modify the configuration file to include the MCP configuration. The file path varies depending on your operating system. For detailed setup, see [https://code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp).
+ **Integration with Codex** – To use the MCP server with Codex, add the MCP server configuration shown earlier to your Codex configuration file (`~/.codex/config.toml`), in Codex's TOML format. For more information, see [Model Context Protocol](https://developers.openai.com/codex/mcp) in the Codex documentation.
+ **Integration with Cline** – To use the MCP server with Cline, modify `cline_mcp_settings.json` and add the MCP server configuration shown earlier. For more information about how to manage MCP configuration, see the [Cline documentation](https://docs.cline.bot/mcp/configuring-mcp-servers).
+ **Integration with GitHub Copilot** – To use the MCP server with GitHub Copilot, follow the instructions in [Extending Copilot Chat with MCP](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp) to modify the corresponding configuration file, and follow the instructions for each IDE to activate the setup.