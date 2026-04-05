# MCP servers targets

MCP servers provide local tools, data access, or custom functions for your interactions with
models and agents in Bedrock AgentCore. In Bedrock AgentCore, you can define a preconfigured MCP
server as a target when creating a gateway.

MCP servers host tools that agents can discover and invoke. In Bedrock AgentCore, you use a
gateway to associate targets with tools and connect them to your agent runtime. You connect with
external MCP servers through the `SynchronizeGatewayTargets` API that performs
protocol handshakes and indexes available tools. For more information about installing and using
MCP servers, see [Amazon Bedrock AgentCore MCP Server: Vibe coding with your coding assistant](mcp-getting-started.md "mcp-getting-started.md").

###### Topics

- [Key considerations and limitations](#gateway-target-MCPservers-considerations "#gateway-target-MCPservers-considerations")
- [Connecting to an OAuth-protected MCP server using Authorization Code flow](#gateway-target-MCPservers-auth-code-grant-flow "#gateway-target-MCPservers-auth-code-grant-flow")
- [Configuring permissions](#gateway-target-MCPservers-permissions "#gateway-target-MCPservers-permissions")

## Key considerations and limitations

Tool discovery is managed through the synchronization operation provided by the
`SynchronizeGatewayTargets` API as follows.

**Implicit Synchronization**

Implicit synchronization is the automatic tool discovery and indexing that occurs during
`CreateGatewayTarget` and `UpdateGatewayTarget` operations. Gateway
immediately calls the MCP server's tools/list capability to fetch available tools and make
tools available in the unified catalog without requiring separate user action.

**Explicit Synchronization**

Manual tool catalog refresh triggered by calling the
`SynchronizeGatewayTargets` API. Invoke this when the MCP server has changed its
tool definitions. The API performs the discovery process on-demand, allowing users to
control when Gateway updates its view of available tools.

Synchronization is a critical mechanism for maintaining accurate tool catalogs when
integrating MCP servers. Implicit synchronization occurs automatically during target creation
and updates, where Gateway immediately discovers and indexes tools from the MCP server to
ensure tools are available for semantic search and unified listing. Explicit synchronization
is performed on-demand through the `SynchronizeGatewayTargets` API, allowing
discovery of the MCP tool catalog when MCP servers independently modify their capabilities.

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

The following types of the authorization strategy are supported.

- No authorization – The gateway invokes the MCP server without preconfigured
  authorization. This approach is not recommended.
- OAuth – The gateway supports both two-legged OAuth (Client Credentials grant
  type) and three-legged OAuth (Authorization Code grant type). You configure the
  authorization provider in Amazon Bedrock AgentCore Identity in the same account and Region for
  the gateway to make calls to the MCP server.
- IAM ([AWS Signature Version 4 (Sig V4)](../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md")) – The gateway signs requests to the MCP server using SigV4
  with the gateway service role credentials. You configure an
  `IamCredentialProvider` with a required service name for SigV4 signing and
  an optional Region (defaults to the gateway Region).

###### Important

IAM (SigV4) outbound authorization requires that the MCP server is hosted behind an AWS service that natively supports IAM authentication. The gateway signs outbound requests with SigV4 but does not modify the authentication configuration on the target. The target service must be able to verify SigV4 signatures.

The following AWS services natively support IAM authentication and are compatible with IAM outbound authorization for MCP server targets:

- Amazon Bedrock AgentCore Gateway
- Amazon Bedrock AgentCore Runtime (see [Deploy MCP servers in AgentCore Runtime](runtime-mcp.md "runtime-mcp.md"))
- Amazon API Gateway
- Lambda Function URLs
  Services that do not natively verify SigV4 signatures, such as Application Load Balancer or direct Amazon EC2 endpoints, are not compatible with IAM outbound authorization. If your MCP server is hosted behind one of these services, use OAuth or API key authorization instead.

**Configuration considerations for MCP server targets**

The following must be configured.

1. The MCP server must have tool capabilities.
2. Supported MCP protocol versions are - **2025-06-18**,
   **2025-03-26**, and **2025-11-25**.
3. For the provided URL/endpoint of the server, the URL should be encoded. The Gateway
   will use the same URL to invoke the server.
4. JSON Schema reference keywords such as `$ref`, `$defs`,
   `$anchor`, `$dynamicRef`, and `$dynamicAnchor` are not
   supported in the tool definitions returned by the MCP server's `tools/list`
   response. If your MCP server returns tool schemas containing these keywords, the target
   creation or synchronization will fail. Ensure your MCP server returns fully resolved,
   self-contained JSON schemas without reference keywords.

## Connecting to an OAuth-protected MCP server using Authorization Code flow

To support the Authorization Code grant type (three-legged OAuth) with MCP server targets,
Amazon Bedrock AgentCore Gateway provides two methods for target creation.

**Implicit sync during MCP server target creation**

With this method, the admin user completes the authorization code flow during
`CreateGatewayTarget`, `UpdateGatewayTarget`, or
`SynchronizeGatewayTargets` operations using the authorization URL returned in
the response. This allows Amazon Bedrock AgentCore Gateway to discover and cache the MCP server's
tools upfront.

###### Note

You cannot delete, update, or synchronize a target that is in a pending authorization
state (`CREATE_PENDING_AUTH`, `UPDATE_PENDING_AUTH`, or
`SYNCHRONIZE_PENDING_AUTH`). Wait for the authorization to complete or fail
before performing further operations on the target.

**Provide schema upfront during MCP server target creation**

With this method, admin users provide the tool schema directly during
`CreateGatewayTarget` or `UpdateGatewayTarget` operations using the
`mcpToolSchema` field, rather than Amazon Bedrock AgentCore Gateway fetching them
dynamically from the MCP server. Amazon Bedrock AgentCore Gateway parses the provided schema and
caches the tool definitions.

###### Note

You cannot synchronize a target that has a static tool schema
(`mcpToolSchema`) configured. Remove the static schema through an
`UpdateGatewayTarget` call to enable dynamic tool synchronization.

**URL Session Binding**

[OAuth 2.0 authorization URL session binding](oauth2-authorization-url-session-binding.md "oauth2-authorization-url-session-binding.md") verifies that the user who
initiated the OAuth authorization request
is the same user who granted consent. After the user completes consent, the browser redirects
back to a return URL configured on the target with a unique session URI. The application is
then responsible for calling the [CompleteResourceTokenAuth](../APIReference/API_CompleteResourceTokenAuth.md "../APIReference/API_CompleteResourceTokenAuth.md") API, presenting both
the user's identity and the session URI. Amazon Bedrock AgentCore Identity validates that the user
who started the flow is the same user who completed it before exchanging the authorization
code for an access token.

This prevents a scenario where a user accidentally shares the authorization URL and
someone else completes the consent, which would grant access tokens to the wrong party. The
authorization URL and session URI are only valid for 10 minutes, further limiting the window
for misuse. Session binding applies during target creation (implicit sync) and during tool
invocation.

###### Note

When performing target operations (Create, Update, or Synchronize) and authorization
through the AWS Management Console, the [CompleteResourceTokenAuth](../APIReference/API_CompleteResourceTokenAuth.md "../APIReference/API_CompleteResourceTokenAuth.md") call is
made on behalf of the resource owner, requiring no further action after
authorization.

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
                "bedrock-agentcore:GetWorkloadAccessTokenForUserId",
                "bedrock-agentcore:GetResourceOauth2Token",
                "bedrock-agentcore:CompleteResourceTokenAuth",
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
