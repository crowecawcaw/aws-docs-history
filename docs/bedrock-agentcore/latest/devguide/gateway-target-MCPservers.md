# MCP servers targets

MCP servers provide local tools, data access, or custom functions for your interactions with
models and agents in Bedrock AgentCore. In Bedrock AgentCore, you can define a preconfigured MCP
server as a target when creating a gateway.

MCP servers host tools which agents can discover and invoke. In Bedrock AgentCore, you use a
gateway to associate targets to tools to connect to your agent runtime. You connect with
external MCP servers through the `SynchronizeGatewayTargets` API that performs
protocol handshakes and indexes available tools. For more information about installing and using
MCP servers, see [Amazon Bedrock AgentCore MCP Server: Vibe coding with your coding assistant](mcp-getting-started.md "mcp-getting-started.md").

###### Topics

- [Key considerations and limitations](#gateway-target-MCPservers-considerations "#gateway-target-MCPservers-considerations")
- [Configuring permissions](#gateway-target-MCPservers-permissions "#gateway-target-MCPservers-permissions")

## Key considerations and limitations

Tool discovery is managed through the synchronization operation provided by the
`SynchronizeGatewayTargets` API as follows.

**Implicit Synchronization**

Implicity synchronization is the automatic tool discovery and indexing that occurs during
`CreateGatewayTarget` and `UpdateGatewayTarget` operations. Gateway
immediately calls the MCP server's tools/list capability to fetch available tools and make
tools available in the unified catalog without requiring separate user action.

**Explicit Synchronization**

Manual tool catalog refresh triggered by calling the
`SynchronizeGatewayTargets` API. Invoke this when the MCP server has changed its
tool definitions. The API performs discovery process on-demand operation, allowing users to
control when Gateway updates its view of available tools.

Synchronization is a critical mechanisms for maintaining accurate tool catalogs when
integrating MCP servers. Implicit synchronization occurs automatically during target creation
and updates, where Gateway immediately discovers and indexes tools from the MCP server to
ensure tools are available for semantic search and unified listing. Explicit synchronization
is performed on-demand through the `SynchronizeGatewayTargets` API, allowing
discovery of MCP tool catalog when MCP servers independently modify their capabilities.

**When to call
`SynchronizeGatewayTargets`**

Use this API whenever your MCP server's tools change - whether adding new tools, modifying
existing tool schemas, or removing deprecated tools. Since Gateway pre-computes vector
embeddings for semantic search and maintains normalized tool catalogs, synchronization ensures
users can discover and invoke the latest available tools across all target types.

**How to call the API**

Make a PUT request to /gateways/{gatewayIdentifier}/synchronize with the target ID in the
request body. The API returns a 202 response immediately and processes synchronization
asynchronously. Monitor the target status through GetGatewayTarget to track synchronization
progress, as the operation can take several minutes for large tool sets.

**Authorization strategy**

Two types of the authorization strategy are supported.

- NoAuth - Gateway will invoke the MCP server's tool capabilities without preconfigured
  Auth. This is not the recommended approach.
- OAuth2 - Gateway supports two-legged OAuth. You configure the authorization provider
  in AgentCore Identity in the same account and Region for the Gateway to be able to make
  calls to the MCP server.

**Configuration considerations** For the MCP servers target
type, the following must be configured.

1. The MCP server must have tool capabilities.
2. Supported MCP protocol versions are - **2025-06-18** and
   **2025-03-26**.
3. For the provided URL/endpoint of the server, the URL should be encoded. The Gateway
   will use the same URL to invoke the server.
4. JSON Schema reference keywords such as `$ref`, `$defs`,
   `$anchor`, `$dynamicRef`, and `$dynamicAnchor` are not
   supported in the tool definitions returned by the MCP server's `tools/list`
   response. If your MCP server returns tool schemas containing these keywords, the target
   creation or synchronization will fail. Ensure your MCP server returns fully resolved,
   self-contained JSON schemas without reference keywords.

## Configuring permissions

The IAM role which you use to create, update or synchronize MCP servers targets should
have the permissions shown in the following example.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:CreateGateway",
                "bedrock-agentcore:GetGateway",
                "bedrock-agentcore:CreateGatewayTarget",
                "bedrock-agentcore:GetGatewayTarget",
                "bedrock-agentcore:SynchronizeGatewayTargets",
                "bedrock-agentcore:UpdateGatewayTarget"
            ],
            "Resource": "arn:aws:bedrock-agentcore:*:*:*gateway*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:CreateWorkloadIdentity",
                "bedrock-agentcore:GetWorkloadAccessToken",
                "bedrock-agentcore:GetResourceOauth2Token",
                "secretsmanager:GetSecretValue"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:EnableKeyRotation",
                "kms:Decrypt",
                "kms:Encrypt",
                "kms:GenerateDataKey*",
                "kms:ReEncrypt*",
                "kms:CreateAlias",
                "kms:DisableKey",
                "kms:*"
            ],
            "Resource": "arn:aws:kms:*:123456789012:key/*"
        }
    ]
}
```
