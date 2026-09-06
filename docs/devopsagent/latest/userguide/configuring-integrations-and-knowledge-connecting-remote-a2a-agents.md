

# Connecting Remote A2A Agents
<a name="configuring-integrations-and-knowledge-connecting-remote-a2a-agents"></a>

Remote agents extend AWS DevOps Agent's investigation capabilities by delegating tasks to external agents that implement the Agent-to-Agent (A2A) protocol. When you connect a remote agent, AWS DevOps Agent can assign investigation subtasks to it and incorporate its findings into the overall investigation. This guide explains how to connect a remote agent to AWS DevOps Agent.

**Note:** Remote A2A agents are currently supported for incident investigations only.

## Requirements
<a name="requirements"></a>

Before connecting a remote agent, ensure your agent meets these requirements:
+ **A2A protocol support** – Your agent must implement the [Agent-to-Agent (A2A) protocol](https://a2a-protocol.org/latest/specification/) (JSONRPC or HTTP\+JSON binding) and serve a valid agent card at an accessible URL. The agent card tells AWS DevOps Agent how to communicate with your agent. The same authentication credentials used to invoke the agent are used to fetch the agent card. The following agent card fields are required:
  + **name** – A unique name identifying your agent
  + **description** – A description of your agent's capabilities. AWS DevOps Agent uses this to determine which remote agent is best suited for a given subtask
  + **supportedInterfaces** – Declares the invoke endpoint URL, protocol binding (`JSONRPC` or `HTTP+JSON`), and protocol version
  + **capabilities** – An object indicating whether your agent supports streaming responses
  + **skills** – An array describing the specific capabilities of your agent. AWS DevOps Agent uses skills to route tasks to the most appropriate remote agent
+ **Authentication support** – Your remote agent must support one of the following authentication methods: Bearer token, OAuth Client Credentials, API key, or AWS Signature Version 4 (SigV4).
+ **Idle timeout** – AWS DevOps Agent closes the connection if the remote A2A agent sends no data for 1 minute. This applies to both single and streaming responses, so a streaming agent must send data at least once per minute to keep the connection open.

## Security considerations
<a name="security-considerations"></a>

When connecting remote agents to AWS DevOps Agent, consider these security aspects:
+ **Read-only agents** – Remote agents should be designed for investigation and data gathering only. Ensure that remote agents do not perform write operations or modifications to production systems.
+ **Prompt injection risks** – Remote agents can introduce additional risk of prompt injection attacks. See [Prompt injection protection: AWS DevOps Agent Security](aws-devops-agent-security.md) for more information.

See [AWS DevOps Agent Security](aws-devops-agent-security.md) for more information on prompt injection and the shared responsibility model.

**Note**  
** If your remote agent is on a private network, see [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md).

## Registering a remote agent (account-level)
<a name="registering-a-remote-agent-account-level"></a>

Remote agents are registered at the AWS account level and shared among all Agent Spaces in that account.

### Step 1: Configure remote agent
<a name="step-1-configure-remote-agent"></a>

1. Sign in to the AWS Management Console

1. Navigate to the AWS DevOps Agent console

1. Go to the **Capability Providers** page (accessible from the side navigation)

1. Find **Remote Agent** in the **Available** providers section and click **Register**

1. On the **Configure remote agent** page, enter the agent details:
   + **Name** – A unique name for this remote agent
   + **Agent card endpoint** – HTTPS URL for the remote agent's agent card. AWS DevOps Agent fetches this URL to discover the agent's capabilities and invoke endpoint.
   + **Description** (optional) – Add a description to help identify the agent's purpose

1. Select an authentication method and enter its details:
   + **API key** – Authenticate using a static API key sent in a custom header:
     + **API Key Name** – A user-friendly name for the API key
     + **API Key Header** – The header name expected by the service (for example, `x-api-key`)
     + **API Key Value** – The API key value for authenticating with the service
   + **Bearer token** – Authenticate using a bearer token (RFC 6750):
     + **Token** – The bearer token value
   + **OAuth Client Credentials** – Authenticate using OAuth 2.0 client credentials grant flow:
     + **Client ID** – Enter the client ID of the OAuth client
     + **Client Secret** – Enter the client secret of the OAuth client
     + **Exchange URL** – Enter the OAuth token exchange endpoint URL
     + **Add Scope** – Add OAuth scopes for authentication
   + **AWS SigV4** – Authenticate using AWS Signature Version 4:
     + **Configure IAM role** – Choose either **Use an existing role** (select an existing IAM role with a trust policy that allows the AWS DevOps Agent service principal to assume it, as described in [Creating an IAM role for SigV4 authentication](configuring-integrations-and-knowledge-connecting-mcp-servers.html#creating-an-iam-role-for-sigv4-authentication)) or **Create a new role manually** (follow the instructions displayed in the console).
     + **AWS Region** – Enter the AWS Region for SigV4 signing (for example, `us-east-1`)
     + **Service Name** – Enter the AWS service name for SigV4 signing (for example, `execute-api` for API Gateway, `bedrock-agentcore` for Amazon Bedrock AgentCore)

1. (Optional) If you use API key, Bearer token, or OAuth Client Credentials authentication, select **Connect to endpoint using a private connection** to make requests to your remote agent privately. If you don't select it, the connection is made over the public internet. This option is not available for AWS SigV4 authentication, which requires a publicly accessible endpoint. The private connection applies to both the agent card endpoint and the invoke endpoint declared in your agent card. If you use OAuth Client Credentials authentication, it also applies to the token exchange endpoint. Ensure the private connection is configured with a host address that can route traffic to these endpoints. For more information, see [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md). When selected, choose one of the following:
   + **Use an existing private connection** – Select one of your existing private connections.
   + **Create a new private connection** – Create a new VPC connection using Amazon VPC Lattice.

1. Choose **Next**

### Step 2: Review and register
<a name="step-2-review-and-register"></a>

1. Review all the remote agent configuration details

1. Click **Register** to complete the registration

1. AWS DevOps Agent will validate the connection by fetching your agent card

1. Upon successful validation, your remote agent will be registered at the account level

## Associating remote agents with an Agent Space
<a name="associating-remote-agents-with-an-agent-space"></a>

After registering a remote agent at the account level, you can associate it with specific Agent Spaces:

1. In the AWS DevOps Agent console, select your Agent Space

1. Go to the **Capabilities** tab

1. In the **Remote Agents** section, click **Add**

1. Select the registered remote agent you want to connect to this Agent Space

1. Click **Add** to associate the remote agent with your Agent Space

AWS DevOps Agent will now be able to delegate investigation subtasks to your remote agent in this Agent Space.

## Managing remote agent connections
<a name="managing-remote-agent-connections"></a>

**Viewing connected agents** – To see all remote agents connected to your Agent Space, select your Agent Space, go to the **Capabilities** tab, and check the **Remote Agents** section.

**Removing remote agent connections** – To disconnect a remote agent from an Agent Space, select the agent in the **Remote Agents** section and choose **Remove**. To completely delete a remote agent registration, remove it from all Agent Spaces first, then navigate to **Capability Providers**, select the remote agent, and choose **Deregister** from the **Actions** menu.

**Updating authentication credentials** – If your authentication credentials need to be updated, you need to re-register your remote agent. Navigate to the **Capability Providers** page in the AWS DevOps Agent console, locate your remote agent, remove any active associations, and choose **Deregister** from the **Actions** menu. Next, register your remote agent with the new authentication credentials and re-create any necessary associations with your Agent Space.

## Related topics
<a name="related-topics"></a>
+ [Connecting MCP Servers](configuring-integrations-and-knowledge-connecting-mcp-servers.md)
+ [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md)
+ [AWS DevOps Agent Security](aws-devops-agent-security.md)
+ [Creating an Agent Space](getting-started-with-aws-devops-agent-creating-an-agent-space.md)