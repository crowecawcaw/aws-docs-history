

# Authentication and security
<a name="connecting-to-devops-agent-remote-servers-authentication-and-security"></a>

Two authentication methods are available for both MCP and A2A endpoints:
+ **Access token (Bearer)** – A single token scoped to one Agent Space. Simplest setup for individual use.
+ **AWS SigV4** – AWS credential-based authentication. Supports multiple Agent Spaces and integrates with existing AWS identity governance. Handled automatically by [mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws), a local proxy that signs requests using your AWS credentials.

## Create an access token
<a name="create-an-access-token"></a>

### Prerequisites
<a name="prerequisites"></a>
+ The access tokens feature must be enabled on your Agent Space.
+ You must have IAM permissions to manage access tokens (`aidevops:CreateAccessToken`, `aidevops:RevokeAccessToken`, `aidevops:RotateAccessToken`). For the full list, see [DevOps Agent IAM permissions](aws-devops-agent-security-devops-agent-iam-permissions.md).

### Enable access tokens
<a name="enable-access-tokens"></a>

1. Sign in to the AWS Management Console and open the AWS DevOps Agent console.

1. Choose your Agent Space.

1. Choose the **Configuration** tab.

1. In the **Access tokens** section, choose **Enable**.

1. Confirm the action.

### Create a token
<a name="create-a-token"></a>

1. Open the DevOps Agent web app for your Agent Space, then from the navigation menu, choose **Settings**, then choose **Access Tokens**.

1. Choose **Generate token**.

1. Enter a name for the token.

1. Choose a scope:
   + `read` – View investigations, recommendations, chats, and Agent Space resources.
   + `operate` – Full access. Includes everything in `read`, plus send messages, create chats, and manage backlog tasks and recommendations.

1. Choose a client type:
   + `human` – For IDE and CLI usage (Kiro, Claude Code, Cursor, and other interactive tools).
   + `agent` – For autonomous A2A integrations and programmatic agents.

1. Set an expiration (1 to 60 days).

1. Copy the token value and store it in a safe, secure location, such as [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html). You cannot retrieve it again.

After creating a token, the web app displays a configuration example that you can copy directly into your client.

## Use SigV4 authentication
<a name="use-sigv4-authentication"></a>

SigV4 authentication uses your AWS credentials instead of an access token. The Kiro power and Claude Code plugin include built-in SigV4 support through `mcp-proxy-for-aws`, which signs requests using your local AWS credentials.

### When SigV4 is used
<a name="when-sigv4-is-used"></a>
+ As a **fallback** when the access token is not configured or fails (expired, invalid).
+ As the **primary** auth when you have multiple Agent Spaces and need to route by `agent_space_id` per tool call.
+ As a **user choice** – in Claude Code, run the setup skill to switch from Bearer token to SigV4 auth.

### Prerequisites
<a name="prerequisites"></a>
+ AWS credentials available in the environment (through SSO, environment variables, or credential file).
+ Your credentials must have permission to invoke AWS DevOps Agent actions. For the required permissions, see [DevOps Agent IAM permissions](aws-devops-agent-security-devops-agent-iam-permissions.md).
+ `uvx` installed (the proxy runs through `uvx mcp-proxy-for-aws@latest`).

### Example configuration
<a name="example-configuration"></a>

To configure an MCP client to use SigV4 instead of an access token, run the server through `mcp-proxy-for-aws`. Replace `{region}` with your Agent Space's Region (for example, `us-east-1`):

```
{
  "mcpServers": {
    "aws-devops-agent": {
      "command": "uvx",
      "timeout": 120000,
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://connect.aidevops.{region}.api.aws/mcp",
        "--service", "aidevops",
        "--region", "{region}"
      ]
    }
  }
}
```

The proxy signs each request with your local AWS credentials, so no access token is required.

### Multi-Agent-Space routing
<a name="multi-agent-space-routing"></a>

In SigV4 mode, pass `agent_space_id` on each tool call to specify which Agent Space to use. This makes it possible to route across multiple Agent Spaces from a single client.

## Security considerations
<a name="security-considerations"></a>

### Token scoping
<a name="token-scoping"></a>
+ Use least privilege: choose `read` for read-only integrations, `operate` only when the client needs to send messages or manage tasks.
+ Rotate tokens periodically. Tokens expire after the configured duration (maximum 60 days).
+ Store tokens in environment variables or secrets managers. Do not hardcode tokens in source code.
+ Do not auto-execute agent responses without human review.

### IP allowlist
<a name="ip-allowlist"></a>

When creating an access token, you can optionally specify an IP allowlist. When configured, the token can only be used from the specified IP addresses or CIDR ranges. Requests from other IPs are rejected with an access denied error.

### Token rotation and revocation
<a name="token-rotation-and-revocation"></a>
+ **Rotation** – Rotate a token to generate a new token value while preserving the token's name, scopes, and IP allowlist. The old token is immediately invalidated. Update your client configuration with the new token value. Rotation also starts a fresh chat history—see the following section.
+ **Revocation** – If a token is compromised, revoke it immediately. Revoked tokens cannot be used and cannot be restored.

#### Chat history and token rotation
<a name="chat-history-and-token-rotation"></a>

Each token has its own chat history. When you rotate a token, AWS DevOps Agent treats the new token value as a new identity. Chats that you created with the previous token no longer appear through the remote server.

#### Responding to a compromised token
<a name="responding-to-a-compromised-token"></a>

If you suspect a token has been compromised, follow these steps:

1. **Block all token access** – In the AWS DevOps Agent console, open your Agent Space, choose the **Configuration** tab, and choose **Disable** in the Access tokens section. This immediately blocks all token-based access to the Agent Space.

1. **Revoke compromised tokens** – In the web app, go to **Settings** > **Access Tokens**, choose the compromised token, and choose **Revoke**. You can revoke tokens even while access tokens are disabled.

1. **Re-enable access tokens** – After revoking the compromised tokens, re-enable access tokens from the **Configuration** tab if you still need token-based access.

#### Revoking tokens programmatically
<a name="revoking-tokens-programmatically"></a>

You can also revoke tokens programmatically using `awscurl`. The following commands use SigV4 authentication. Replace the Region (`us-east-1`) with the Region where your Agent Space is created.

**Note:** Step 1 uses the AWS CLI. Steps 2 and 3 use [awscurl](https://github.com/okigan/awscurl), a command-line tool that signs HTTP requests with SigV4, because access token operations do not yet have dedicated AWS CLI commands.

**Step 1: List your Agent Spaces**

```
aws aidevops list-agent-spaces --region us-east-1
```

**Step 2: List access tokens for an Agent Space**

```
awscurl --service aidevops --region us-east-1 \
  -H "Accept: application/json" \
  "https://cp.aidevops.us-east-1.api.aws/v1/agentspaces/{agentSpaceId}/access-tokens"
```

**Step 3: Revoke a token**

```
awscurl --service aidevops --region us-east-1 -X POST \
  -H "Accept: application/json" \
  "https://cp.aidevops.us-east-1.api.aws/v1/agentspaces/{agentSpaceId}/access-tokens/{accessTokenId}/revoke"
```

Replace `{agentSpaceId}` and `{accessTokenId}` with the values from the previous responses.

### Traceability
<a name="traceability"></a>

AWS DevOps Agent records remote server activity in AWS CloudTrail. Use these records to trace who invoked a remote server and what the agent did as a result. AWS DevOps Agent delivers CloudTrail events to the AWS account that hosts the Agent Space.

#### Access token authentication events
<a name="access-token-authentication-events"></a>

Each time AWS DevOps Agent authenticates an access token for an MCP or A2A endpoint, it emits an `AuthenticateAccessToken` event to CloudTrail. AWS DevOps Agent records both successful and failed authentications. Use these records to audit legitimate use and detect rejected attempts. Examples include expired or revoked tokens, and requests blocked by an IP allowlist.

The event has the following characteristics:
+ **Event source** – `aidevops.amazonaws.com`
+ **Event name** – `AuthenticateAccessToken`
+ **Management event** – The event is a management event and is not read-only, so it remains visible when you filter out read-only events.

The event includes the following key fields:


| Field | Description | 
| --- | --- | 
| userIdentity.principalId | The ID of the access token that was presented. | 
| userName | The name of the access token. | 
| requestParameters.agentSpaceId | The Agent Space the token authenticates against. | 
| requestParameters.accessTokenId | The access token ID. | 
| requestParameters.tokenName | The access token name. | 
| requestParameters.protocol | The protocol that was used—MCP or A2A. | 
| responseElements.AuthenticateAccessToken | The outcome—Success or Failure. | 
| resources | The Agent Space resource (AWS::AIDevOps::AgentSpace) the token authenticates against, identified by its ARN. | 
| additionalEventData.roleSessionName | For successful authentications, the downstream role session name, in the format token\_{spaceId}\_{timestamp}\_{tokenName}. Use it to correlate the authentication with the actions the agent performs. | 
| sourceIPAddress | The IP address of the client. | 
| userAgent | The client User-Agent string, when available. | 
| errorCode, errorMessage | For failed authentications, the reason the authentication was rejected. | 

**Note**  
** AWS DevOps Agent never records the raw bearer token value. Only the opaque access token ID appears in the event.

#### Downstream action events
<a name="downstream-action-events"></a>

When you use an access token, AWS DevOps Agent assumes a role on your behalf to perform actions. AWS DevOps Agent logs this `AssumeRole` call in CloudTrail with session tags that identify the token and caller:
+ `AgentSpaceId` – Identifier of the Agent Space.
+ `UserId` – Identity of the token creator.
+ `AccessTokenId` – Unique identifier of the token.
+ `TokenName` – Name of the access token used.
+ `ClientType` – The protocol used (MCP, A2A).
+ `SourceIp` – IP address of the client.
+ `UserAgent` – Client User-Agent string (when available).

Each action that the agent takes on your behalf has a corresponding downstream AWS API call that CloudTrail logs. The role session name uses the format `token_{spaceId}_{timestamp}_{tokenName}`. This session name matches the `roleSessionName` in the `AuthenticateAccessToken` event. Use it to trace from an authentication to the specific actions that followed it.

#### SigV4 invocations
<a name="sigv4-invocations"></a>

Invocations that use AWS SigV4 authentication instead of an access token do not produce `AuthenticateAccessToken` events. AWS DevOps Agent attributes SigV4 requests to your AWS Identity and Access Management (IAM) identity. You can trace the actions the agent performs through the downstream AWS API calls they trigger.

### VPC endpoint policy limitation
<a name="vpc-endpoint-policy-limitation"></a>

The remote server endpoints do not support VPC endpoint policies. Calls using either access tokens or SigV4 authentication cannot be restricted by VPC endpoint policies.

### Disabling access tokens
<a name="disabling-access-tokens"></a>

The access tokens feature is off by default. To disable it after enabling:

1. Open the **Configuration** tab of your Agent Space.

1. In the **Access tokens** section, choose **Disable**.

Disabling immediately blocks all token-based access. Existing tokens are not deleted but cannot be used until the feature is re-enabled.

To prevent users in your organization from enabling access tokens, create a Service Control Policy (SCP) that denies the access token API actions and the `UpdateAgentSpace` action (which controls the access tokens toggle):

**Note:** Denying `aidevops:UpdateAgentSpace` also prevents other Agent Space updates (name, description, locale). If this is too broad, omit it from the SCP — the remaining denies still prevent token creation and use, even if someone enables the feature.

```
{
  "Version": "2012-10-17",		 	 	 		 	 	 
  "Statement": [
    {
      "Sid": "DenyAccessTokenOperations",
      "Effect": "Deny",
      "Action": [
        "aidevops:UpdateAgentSpace",
        "aidevops:CreateAccessToken",
        "aidevops:GetAccessToken",
        "aidevops:ListAccessTokens",
        "aidevops:RotateAccessToken",
        "aidevops:RevokeAccessToken"
      ],
      "Resource": "*"
    }
  ]
}
```

## Troubleshooting
<a name="troubleshooting"></a>


| Symptom | Cause | Resolution | 
| --- | --- | --- | 
| HTTP 401 Unauthorized | Token is invalid or expired. | Create a new token or rotate the existing token in the web app. | 
| HTTP 400 "A2A-Version header required" | Missing protocol version header. Only A2A v1.0 is supported. | Add A2A-Version: 1.0 header to A2A requests. | 
| HTTP 400 "Agent space not resolved from credentials" | An A2A \+ SigV4 request does not include the X-Agent-Space-Id header. | Add X-Agent-Space-Id: <agentSpaceId> to the request. | 
| Request timeout | Initial responses take 5–30 seconds. Investigations take 5–8 minutes. | Set client timeout to at least 120 seconds. | 
| Connection refused | Incorrect endpoint URL or Region. | Verify the URL format: https://connect.aidevops.{region}.api.aws | 