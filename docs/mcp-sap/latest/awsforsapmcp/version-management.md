

# Version management
<a name="version-management"></a>

You access the AWS for SAP Model Context Protocol (MCP) Server as a container image distributed through AgentCore Runtime. There are two ways to consume the image, each offering a different trade-off between convenience and control.

## Image tags
<a name="image-tags"></a>

 ** `latest` tag (auto-updating)** 

If your container configuration references `aws-sap-mcp:latest`, you automatically receive the newest version the next time your container runtime pulls the image. No action is required — the `latest` tag is re-pointed atomically to the new image during each deployment.

 **Version-specific tags (pinned, immutable)** 

Each deployment also produces a version-specific tag derived from the server version (for example, `1.0.0-200`). Version-specific tags are immutable — once pushed, they cannot be overwritten. Use version-specific tags when you need deterministic deployments or want to control exactly when version changes are applied.

To update to a newer version, update the image URI in your AgentCore Runtime configuration to reference the desired version tag and update the runtime hosting.

## Rollback procedure
<a name="rollback-procedure"></a>

To roll back to a previous version, change your Amazon Bedrock AgentCore Runtime to reference an older version-specific tag. Then, create a new version of the AgentCore Runtime endpoint. For instructions on creating a new version of the AgentCore Runtime endpoint, see the [AgentCore Runtime documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html).