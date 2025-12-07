# Create an AgentCore gateway using the CLI

You can use the Amazon Bedrock AgentCore starter toolkit CLI to create gateways with simplified commands. The CLI handles common configurations automatically, including IAM role creation and OAuth setup.

Basic gateway

```
bedrock-agentcore-starter-toolkit gateway create-mcp-gateway \
  --name MyGateway \
  --region us-east-1
```

With semantic search

```
bedrock-agentcore-starter-toolkit gateway create-mcp-gateway \
  --name MyGateway \
  --region us-east-1 \
  --enable_semantic_search
```

With custom IAM role

```
bedrock-agentcore-starter-toolkit gateway create-mcp-gateway \
  --name MyGateway \
  --region us-east-1 \
  --role-arn arn:aws:iam::123456789012:role/MyGatewayRole
```

After creating the gateway, you can add targets using the `create-mcp-gateway-target` command. For more information about CLI commands, see the [Get started with AgentCore Gateway](gateway-quick-start.md "gateway-quick-start.md").
