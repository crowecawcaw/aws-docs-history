# Connect to DevOps Agent remote servers

AWS DevOps Agent provides dedicated remote servers for the Model Context Protocol (MCP) and Agent-to-Agent (A2A) protocol. Use these servers to connect your IDE, CLI, or custom agent integrations to an Agent Space.

## Supported protocols

- **MCP (Model Context Protocol)** – Connect IDE and CLI clients such as Kiro, Claude Code, Cursor, and other MCP-compatible tools.
- **A2A (Agent-to-Agent) v1.0** – Connect autonomous agents for agent-to-agent communication.

## Endpoints

Remote servers are available at a regional URL:

```
https://connect.aidevops.{region}.api.aws
```

| Protocol       | Path                           | Method |
| -------------- | ------------------------------ | ------ |
| MCP            | `/mcp`                         | POST   |
| A2A            | `/a2a/*`                       | POST   |
| A2A agent card | `/.well-known/agent-card.json` | GET    |

For the list of available Regions, see [Supported Regions](about-aws-devops-agent-supported-regions.md "about-aws-devops-agent-supported-regions.md").

## Authentication

Two authentication methods are available for both MCP and A2A endpoints:

- **Access token (Bearer)** – A single token scoped to one Agent Space. Simplest setup for individual use.
- **AWS SigV4** – AWS credential-based authentication. Supports multiple Agent Spaces and integrates with existing AWS identity governance. Handled automatically by [mcp-proxy-for-aws](https://github.com/awslabs/mcp-proxy-for-aws "https://github.com/awslabs/mcp-proxy-for-aws"), a local proxy that signs requests using your AWS credentials.

## Create an access token

### Prerequisites

- The access tokens feature must be enabled on your Agent Space.
- You must have IAM permissions to manage access tokens (`aidevops:CreateAccessToken`, `aidevops:RevokeAccessToken`, `aidevops:RotateAccessToken`). For the full list, see [DevOps Agent IAM permissions](aws-devops-agent-security-devops-agent-iam-permissions.md "aws-devops-agent-security-devops-agent-iam-permissions.md").

### Enable access tokens

1. Sign in to the AWS Management Console and open the AWS DevOps Agent console.
2. Choose your Agent Space.
3. Choose the **Configuration** tab.
4. In the **Access tokens** section, choose **Enable**.
5. Confirm the action.

### Create a token

1. Open the DevOps Agent web app for your Agent Space, then from the navigation menu, choose **Settings**, then choose **Access Tokens**.
2. Choose **Create access token**.
3. Enter a name for the token.
4. Choose a scope:

   - `read` – View investigations, recommendations, chats, and Agent Space resources.
   - `operate` – Full access. Includes everything in `read`, plus send messages, create chats, and manage backlog tasks and recommendations.

5. Set an expiration (1 to 60 days).
6. Copy the token value and store it in a safe, secure location. You cannot retrieve it again.

After creating a token, the web app displays a configuration example that you can copy directly into your client.

## Connect with Kiro

1. Install the **aws-devops-agent** power from the Powers marketplace.
2. Set the following environment variables to configure the connection:

`DEVOPS_AGENT_TOKEN=<your-token> DEVOPS_AGENT_REGION=<your-agent-space-region>`

1. Approve the environment variable prompt when it appears.
2. Restart the IDE when necessary.

The Kiro power includes `aws-mcp` as a fallback, which provides direct AWS API access when the remote server endpoint is unavailable.

## Connect with Claude Code

1. Install the **aws-devops-agent** plugin.
2. Set the following environment variables to configure the connection:

`DEVOPS_AGENT_TOKEN=<your-token> DEVOPS_AGENT_REGION=<your-agent-space-region>`

The Claude Code plugin includes `aws-mcp` as a fallback, which provides direct AWS API access when the remote server endpoint is unavailable.

## Connect with other MCP clients

For any MCP-compatible client, configure the server with:

- **URL** – `https://connect.aidevops.{region}.api.aws/mcp`
- **Authorization header** – `Bearer <your-token>`
- **Timeout** – 120 seconds minimum (initial responses can take 5–30 seconds; ongoing chat sessions may take longer)

## Use SigV4 authentication

SigV4 authentication uses your AWS credentials instead of an access token. The Kiro power and Claude Code plugin include built-in SigV4 support through `mcp-proxy-for-aws`, which signs requests using your local AWS credentials.

### When SigV4 is used

- As a **fallback** when the access token is not configured or fails (expired, invalid).
- As the **primary** auth when you have multiple Agent Spaces and need to route by `agent_space_id` per tool call.
- As a **user choice** – in Claude Code, run the setup skill to switch from Bearer token to SigV4 auth.

### Prerequisites

- AWS credentials available in the environment (through SSO, environment variables, or credential file).
- Your credentials must have permission to invoke AWS DevOps Agent actions. For the required permissions, see [DevOps Agent IAM permissions](aws-devops-agent-security-devops-agent-iam-permissions.md "aws-devops-agent-security-devops-agent-iam-permissions.md").
- `uvx` installed (the proxy runs through `uvx mcp-proxy-for-aws@latest`).

### Multi-Agent-Space routing

In SigV4 mode, pass `agent_space_id` on each tool call to specify which Agent Space to use. This makes it possible to route across multiple Agent Spaces from a single client.

## A2A integration

The A2A endpoint implements the [A2A v1.0 specification](https://a2a-protocol.org/latest/specification/ "https://a2a-protocol.org/latest/specification/") using HTTP+JSON binding.

### Agent card discovery

Retrieve the agent card at:

```
GET https://connect.aidevops.{region}.api.aws/.well-known/agent-card.json
```

### Supported operations

- `SendMessage` – Send a message and receive a response.
- `SendStreamingMessage` – Stream responses as they are generated.
- `GetTask` – Check the status of an asynchronous task.
- `ListTasks` – List tasks for an Agent Space.
- `CancelTask` – Cancel a running task.
- `SubscribeToTask` – Subscribe to task updates through server-sent events.

### Skills

- **investigate** – Deep asynchronous analysis of operational issues (5–8 minutes).
- **chat** – Instant answers to operational questions.

## Security considerations

### Token scoping

- Use least privilege: choose `read` for read-only integrations, `operate` only when the client needs to send messages or manage tasks.
- Rotate tokens periodically. Tokens expire after the configured duration (maximum 60 days).
- Store tokens in environment variables or secrets managers. Do not hardcode tokens in source code.
- Do not auto-execute agent responses without human review.

### IP allowlist

When creating an access token, you can optionally specify an IP allowlist. When configured, the token can only be used from the specified IP addresses or CIDR ranges. Requests from other IPs are rejected with an access denied error.

### Token rotation and revocation

- **Rotation** – Rotate a token to generate a new token value while preserving the token's name, scopes, and IP allowlist. The old token is immediately invalidated. Update your client configuration with the new token value.
- **Revocation** – If a token is compromised, revoke it immediately. Revoked tokens cannot be used and cannot be restored.

#### Responding to a compromised token

If you suspect a token has been compromised, follow these steps:

1. **Block all token access** – In the AWS DevOps Agent console, open your Agent Space, choose the **Configuration** tab, and choose **Disable** in the Access tokens section. This immediately blocks all token-based access to the Agent Space.
2. **Revoke compromised tokens** – In the web app, go to **Settings** > **Access Tokens**, choose the compromised token, and choose **Revoke**. You can revoke tokens even while access tokens are disabled.
3. **Re-enable access tokens** – After revoking the compromised tokens, re-enable access tokens from the **Configuration** tab if you still need token-based access.

#### Revoking tokens programmatically

You can also revoke tokens programmatically using `awscurl`. The following commands use SigV4 authentication. Replace the Region (`us-east-1`) with the Region where your Agent Space is created.

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

When an access token is used, AWS DevOps Agent assumes a role on your behalf to perform actions. This `AssumeRole` call is logged in AWS CloudTrail with session tags that identify the token and caller:

- `AgentSpaceId` – Identifier of the Agent Space.
- `UserId` – Identity of the token creator.
- `AccessTokenId` – Unique identifier of the token.
- `TokenName` – Name of the access token used.
- `ClientType` – The protocol used (MCP, A2A).
- `SourceIp` – IP address of the client.
- `UserAgent` – Client User-Agent string (when available).

Direct MCP and A2A endpoint invocations are not logged in CloudTrail for either authentication method. Each invocation has a corresponding downstream AWS API call logged in CloudTrail, with an identifiable role session name in the format `token_{spaceId}_{timestamp}_{tokenName}`.

### VPC endpoint policy limitation

The remote server endpoints do not support VPC endpoint policies. Calls using either access tokens or SigV4 authentication cannot be restricted by VPC endpoint policies.

### Disabling access tokens

The access tokens feature is off by default. To disable it after enabling:

1. Open the **Configuration** tab of your Agent Space.
2. In the **Access tokens** section, choose **Disable**.

Disabling immediately blocks all token-based access. Existing tokens are not deleted but cannot be used until the feature is re-enabled.

To prevent users in your organization from enabling access tokens, create a Service Control Policy (SCP) that denies the access token API actions and the `UpdateAgentSpace` action (which controls the access tokens toggle):

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

| Symptom                                | Cause                                                                 | Resolution                                                         |
| -------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------ |
| HTTP 401 Unauthorized                  | Token is invalid or expired.                                          | Create a new token or rotate the existing token in the web app.    |
| HTTP 400 "A2A-Version header required" | Missing protocol version header. Only A2A v1.0 is supported.          | Add `A2A-Version: 1.0` header to A2A requests.                     |
| Request timeout                        | Initial responses take 5–30 seconds. Investigations take 5–8 minutes. | Set client timeout to at least 120 seconds.                        |
| Connection refused                     | Incorrect endpoint URL or Region.                                     | Verify the URL format: `https://connect.aidevops.{region}.api.aws` |
