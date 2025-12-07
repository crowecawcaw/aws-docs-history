# Add a target using the CLI

You can use the Amazon Bedrock AgentCore starter toolkit CLI to add targets to an existing gateway with simplified commands.

Lambda target

```
bedrock-agentcore-starter-toolkit gateway create-mcp-gateway-target \
  --gateway-arn arn:aws:bedrock-agentcore:us-east-1:123456789012:gateway/abc123 \
  --gateway-url https://abc123.execute-api.us-east-1.amazonaws.com \
  --role-arn arn:aws:iam::123456789012:role/MyGatewayRole \
  --name MyLambdaTarget \
  --target-type lambda
```

OpenAPI target with credentials

```
bedrock-agentcore-starter-toolkit gateway create-mcp-gateway-target \
  --gateway-arn arn:aws:bedrock-agentcore:us-east-1:123456789012:gateway/abc123 \
  --gateway-url https://abc123.execute-api.us-east-1.amazonaws.com \
  --role-arn arn:aws:iam::123456789012:role/MyGatewayRole \
  --name MyAPITarget \
  --target-type openApiSchema \
  --target-payload '{"s3":{"uri":"s3://my-bucket/api-spec.json"}}' \
  --credentials '{"api_key":"my-key","credential_location":"HEADER","credential_parameter_name":"X-API-Key"}'
```

MCP server target

```
bedrock-agentcore-starter-toolkit gateway create-mcp-gateway-target \
  --gateway-arn arn:aws:bedrock-agentcore:us-east-1:123456789012:gateway/abc123 \
  --gateway-url https://abc123.execute-api.us-east-1.amazonaws.com \
  --role-arn arn:aws:iam::123456789012:role/MyGatewayRole \
  --name MyMCPTarget \
  --target-type mcpServer
```

Replace the gateway ARN, URL, and role ARN with the values from your gateway. For more CLI examples, see the [Get started with AgentCore Gateway](gateway-quick-start.md "gateway-quick-start.md").
