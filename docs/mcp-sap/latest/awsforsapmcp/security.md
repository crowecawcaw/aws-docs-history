

# Security
<a name="security"></a>

Learn about the security features of the Model Context Protocol (MCP) Server, including its network configuration, create, read, update, and delete (CRUD) default read-only mode, credential management, and authentication and authorization mechanisms.

## Network security
<a name="network-security"></a>

The AWS for SAP MCP Server runs in virtual private cloud (VPC) mode on Amazon Bedrock AgentCore Runtime. Network access is controlled through VPC security groups and subnets that you configure during deployment. You can manage network access to Amazon Bedrock AgentCore by using [resource-based policies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/resource-based-policies.html).

## Create, Read, Update, Delete (CRUD) operations
<a name="crud-operations"></a>

The MCP Server runs in read-only mode by default. All write-related configuration flags are set to `false` out of the box. No write tool is registered with the MCP Server unless you explicitly opt in. This granular model helps you grant only the specific write capabilities that your use case requires.

## Authentication
<a name="authentication-security"></a>

The server enforces access control at two layers: inbound and outbound.
+  **Inbound access control:** Amazon Bedrock AgentCore runtime validates all incoming requests before they reach the MCP Server. When configured with JSON Web Token (JWT) based authentication, the runtime verifies the token signature, issuer, audience, and expiration against the configured identity provider’s discovery endpoint. Requests with missing, expired, or invalid tokens are rejected with a 401 response.
+  **Outbound access control:** The MCP Server authenticates to SAP using the configured authentication flow (Basic, M2M, or User Federation). Credentials are never hardcoded in the MCP server or its configuration. For Basic authentication, credentials are retrieved from AWS Secrets Manager on each request. For OAuth flows, tokens are obtained via Amazon Bedrock AgentCore Identity at runtime. The MCP Server does not store or cache outbound credentials.

## Authorization
<a name="authorization"></a>

When you use OAuth authentication flows, the OAuth scopes that you configure through the CloudFormation template determine which SAP OData services the server is authorized to access. Configure scopes to grant access only to the specific services required, following the principle of least privilege. Assign the SAP user associated with the authentication flow only the minimum necessary roles and authorizations in SAP.

## Credential management
<a name="credential-management"></a>

The MCP Server is designed to never store credentials on disk. Sensitive values, such as authentication or cross-site request forgery (CSRF) tokens, are automatically redacted from logs.
+  **OAuth 2.0** — Access tokens are held in-memory only via the TokenStore dataclass. Tokens are not persisted to disk or written to any external store.
+  **BASIC** — When using the BASIC authentication flow, SAP system credentials are retrieved from AWS Secrets Manager at runtime on each request. The credentials exist only in memory for the duration of the request.