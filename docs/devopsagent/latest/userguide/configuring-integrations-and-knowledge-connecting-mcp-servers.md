

# Connecting MCP Servers
<a name="configuring-integrations-and-knowledge-connecting-mcp-servers"></a>

Model Context Protocol (MCP) servers extend AWS DevOps Agent's investigation capabilities by providing access to data from your external observability tools, custom monitoring systems, and operational data sources. This guide explains how to connect an MCP server to AWS DevOps Agent.

## Requirements
<a name="requirements"></a>

Before connecting an MCP server, ensure your server meets these requirements:
+ **Streamable HTTP transport protocol** – Only MCP servers that implement the Streamable HTTP transport protocol are supported.
+ **Authentication support** – Your MCP server must support one of the following authentication methods: OAuth 2.0 (Client Credentials or 3LO), API key/token-based authentication, or AWS Signature Version 4 (SigV4).

## Security considerations
<a name="security-considerations"></a>

When connecting MCP servers to AWS DevOps Agent, consider these security aspects:
+ **Tool allowlisting – ** You should allowlist only the specific tools your Agent Space needs, rather than exposing all tools from your MCP server. See [Configuring MCP tools in an Agent Space](#configuring-integrations-and-knowledge-connecting-mcp-servers) for how to allow list tools per Agent Space.

Please note that the maximum tool name length of any MCP tool is 64 characters. For the maximum number of MCP tools allowed per agent space, see [Quotas](quotas.md).
+ **Prompt injection risks** – Custom MCP servers can introduce additional risk of prompt injection attacks. See [Prompt injection protection: AWS DevOps Agent Security](aws-devops-agent-security.md) for more information.
+ **Read-only tools and access –** Only allowlist read-only MCP tools and ensure that authentication credentials are only permitted read-only access.

See [AWS DevOps Agent Security](aws-devops-agent-security.md) for more information on prompt injection and the shared responsibility model.

**Note**  
If your MCP server is on a private network, see [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md)

## Community MCP servers
<a name="community-mcp-servers"></a>

The [AWS DevOps Agent Tools repository](https://github.com/aws/tools-for-devops-agent) includes deployable MCP servers that give the agent custom tools for deep infrastructure diagnostics such as Amazon Elastic Kubernetes Service (Amazon EKS) node log collection, Amazon Virtual Private Cloud (Amazon VPC) DNS resolution probing, and Amazon Relational Database Service (Amazon RDS) database health checks. The repository is maintained by the AWS DevOps Agent service team, and all contributions go through the same security review bar before being added. To browse what's available, see the [MCP servers catalog](https://aws.github.io/tools-for-devops-agent/mcp-servers/) on the GitHub website.

To use a community MCP server:

1. Deploy the MCP server to your AWS account by following the deployment instructions in the server's README.

1. Register the deployed server with your Agent Space as a capability provider by following the steps in [Registering an MCP server](#registering-an-mcp-server-account-level) below.

## Registering an MCP server (account-level)
<a name="registering-an-mcp-server-account-level"></a>

MCP servers are registered at the AWS account level and shared among all Agent Spaces in that account. Individual Agent Spaces can then choose which specific tools they need from each MCP server.

### Step 1: MCP server details
<a name="step-1-mcp-server-details"></a>

1. Sign in to the AWS Management Console

1. Navigate to the AWS DevOps Agent console

1. Go to the **Capability Providers** page (accessible from the side navigation)

1. Find **MCP Server** in the **Available** providers section and choose **Register**

1. On the **MCP server details** page, enter the following information:
   + **Name** – Enter a descriptive name for your MCP server
   + **Endpoint URL** – Enter the full HTTPS URL of your MCP server endpoint
   + **Description** (optional) – Add a description to help identify the server's purpose
   + **Enable Dynamic Client Registration** – Select this checkbox if you want to allow AWS DevOps Agent to automatically register with your MCP server's authorization server
   + **Connect to endpoint using private connection** – Select this checkbox if you want AWS DevOps Agent to make requests to your MCP server privately. You may select an existing private connection or create a new one. If you use OAuth authentication, the private connection applies to both the MCP server endpoint and the token exchange endpoint. Ensure the private connection is configured with a host address that can route traffic to both endpoints. The connection's host address and this endpoint URL are two different values, and the connection's port ranges must include the endpoint URL's port. For more information about host addresses and endpoint URLs, see [Host address and endpoint URL](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md) and [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md).

1. Choose **Next**

**Note**  
** The MCP server endpoint URL will be displayed in AWS CloudTrail logs in your account.

### Step 2: Authorization flow
<a name="step-2-authorization-flow"></a>

Select the authentication method for your MCP server:

**OAuth Client Credentials** – If your MCP server uses OAuth Client Credentials flow:

1. Select **OAuth Client Credentials**

1. Choose **Next**

**OAuth 3LO (Three-Legged OAuth)** – If your MCP server uses OAuth 3LO for authentication:

1. Select **OAuth 3LO**

1. Choose **Next**

**API Key** – If your MCP server uses API key authentication:

1. Select **API Key**

1. Choose **Next**

**AWS SigV4** – If your MCP server uses AWS Signature Version 4 authentication:

1. Select **AWS SigV4**

1. Choose **Next**

### Step 3: Authorization configuration
<a name="step-3-authorization-configuration"></a>

Configure additional authorization parameters based on the selected authentication method:

**For OAuth Client Credentials:**

1. **Client ID** – Enter the client ID of the OAuth client

1. **Client Secret** – Enter the client secret of the OAuth client

1. **Exchange URL** – Enter the OAuth token exchange endpoint URL

1. **Exchange Parameters** – Enter OAuth token exchange parameters for authenticating with the service

1. **Add Scope** – Add OAuth scopes for authentication

1. Choose **Next**

**For OAuth 3LO:**

1. **Client ID** – Enter the client ID of the OAuth client

1. **Client Secret** – Enter the client secret of the OAuth client if it’s required by your OAuth client

1. **Exchange URL** – Enter the OAuth token exchange endpoint URL

1. **Authorization URL ** - Enter the OAuth authorization endpoint URL

1. **Code Challenge Support ** - Select this checkbox if your OAuth client supports code challenge

1. **Add Scope** – Add OAuth scopes for authentication

1. Choose **Next**

**For API Key:**

1. Enter an API key name

1. Enter the the name of the header that will contain the API key in the request

1. Enter your API key value

1. Choose **Next**

**For AWS SigV4:**

AWS SigV4 authentication allows AWS DevOps Agent to connect to MCP servers that use AWS Signature Version 4 for request signing. This is useful for MCP servers hosted behind Amazon API Gateway or other AWS services that support SigV4 authentication.

**Note:** Private connections are not supported for MCP servers using SigV4 authentication. Your MCP server endpoint must be publicly accessible. For MCP servers on private networks using other authentication methods, see [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md).

1. **Configure IAM role** – Choose one of the following options:
   + **Use an existing role** – Select an existing IAM role from the dropdown. The role must have a trust policy that allows the AWS DevOps Agent service principal to assume it (see [Creating an IAM role for SigV4 authentication](configuring-integrations-and-knowledge-connecting-mcp-servers.html#creating-an-iam-role-for-sigv4-authentication)).
   + **Create a new role manually** – Follow the step-by-step instructions displayed in the console to create a new IAM role with the correct trust policy.
   + **Register without a dedicated role** – Register the MCP server without providing an IAM role. AWS DevOps Agent instead signs requests using an IAM role from an AWS account associated with your Agent Space, and defers connection validation until you associate the server. Choose this for cross-account access across the AWS accounts connected to your Agent Space. For details, see [Cross-account access without a dedicated role](configuring-integrations-and-knowledge-connecting-mcp-servers.html#cross-account-access-without-a-dedicated-role).

1. **AWS Region** – Enter the AWS Region for SigV4 signing (for example, `us-east-1`). To use SigV4a multi-region signing, enter `*`.

1. **Service Name** – Enter the AWS service name for SigV4 signing (for example, `execute-api` for API Gateway).

1. **Custom Headers** (optional) – Add up to 10 custom key-value header pairs to include with each signed request.

1. Choose **Next**

### Step 4: Review and submit
<a name="step-4-review-and-submit"></a>

1. Review all the MCP server configuration details

1. Choose **Submit** to complete the registration

1. AWS DevOps Agent will validate the connection to your MCP server

1. Upon successful validation, your MCP server will be registered at the account level

**Note:** For a server registered without a dedicated role, AWS DevOps Agent defers connection validation to association time, using the primary AWS account role. If validation fails then, you might need to correct the MCP server configuration (such as the endpoint, Region, or service) you provided during registration. For details, see [Cross-account access without a dedicated role](configuring-integrations-and-knowledge-connecting-mcp-servers.html#cross-account-access-without-a-dedicated-role).

## Configuring MCP tools in an Agent Space
<a name="configuring-mcp-tools-in-an-agent-space"></a>

After registering an MCP server at the account level, you can configure which tools from that server are available to specific Agent Spaces:

1. In the AWS DevOps Agent console, select your Agent Space

1. Go to the **Capabilities** tab

1. In the **MCP Servers** section, choose **Add**

1. Select the registered MCP server you want to connect to this Agent Space

1. Configure which tools from this MCP server should be available to the Agent Space:
   + **Allow all tools** – Makes all tools from the MCP server available
   + **Select specific tools** – Allows you to choose which tools to allowlist

1. Choose **Add** to connect the MCP server to your Agent Space

AWS DevOps Agent will now be able to use the allowlisted tools from your MCP server during investigations in this Agent Space.

To control whether the agent can invoke an MCP tool as a read-only or mutating action, you classify each tool. Tools you register programmatically without supplying `toolDetails` default to read-only, and the agent runs them without requesting approval. For more information about classifying MCP tools as read-only or mutating, see [Working with directed actions](working-with-devops-agent-working-with-directed-actions.md).

## Managing MCP server connections
<a name="managing-mcp-server-connections"></a>

**Updating authentication credentials** – You can update the authentication credentials of a registered MCP server without deregistering it. Navigate to the **Capability Providers** page in the AWS DevOps Agent console, select your MCP server, and choose **Update** from the **Actions** menu. Your Agent Space associations are preserved. What you can update depends on the authentication method:
+ **API key** – Enter a new API key value and header name to rotate the credential. The endpoint can't be changed during an update.
+ **OAuth 3LO (Three-Legged OAuth)** – Re-run the authorization flow to refresh the stored token. You don't re-enter the client credentials. When you submit, AWS DevOps Agent redirects you to the provider's consent page to complete the re-authorization. Optionally, you can override the authorization URL. If you leave it blank, AWS DevOps Agent discovers it from your MCP server's metadata.
+ **AWS SigV4** – Update the server name, endpoint, description, AWS Region, service, IAM role, and custom headers.

MCP servers that use OAuth Client Credentials can't be updated in place. To change those credentials, remove any active associations, deregister the MCP server, and re-register it with the new values.

**Viewing connected MCP servers** – To see all MCP servers connected to your Agent Space, select your Agent Space, go to the **Capabilities** tab, and check the **MCP Servers** section. You can also update selected tools here.

**Removing MCP server connections** – To disconnect an MCP server from an Agent Space, select the server in the **MCP Servers** section and choose **Remove**. To completely delete an MCP server registration, remove it from all Agent Spaces first, then delete the account-level registration.

## Creating an IAM role for SigV4 authentication
<a name="creating-an-iam-role-for-sigv4-authentication"></a>

When using AWS SigV4 authentication, AWS DevOps Agent assumes an IAM role in your account to sign requests to your MCP server. This role must have a trust policy that allows the AWS DevOps Agent service principal (`aidevops.amazonaws.com`) to assume it, with confused deputy protection.

### Trust policy
<a name="trust-policy"></a>

Create an IAM role with the following trust policy. Replace `REGION` with your AWS Region (for example, `us-east-1`) and `ACCOUNT_ID` with your AWS account ID.

```
{
  "Version": "2012-10-17",		 	 	 		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "aidevops.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "ACCOUNT_ID"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:aidevops:REGION:ACCOUNT_ID:service/*"
        }
      }
    }
  ]
}
```

The trust policy includes the following conditions to prevent the [confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) :
+ `aws:SourceAccount` – Restricts role assumption to requests originating from your AWS account.
+ `aws:SourceArn` – Restricts role assumption to requests originating from AWS DevOps Agent service resources in your account.

### Permissions policy
<a name="permissions-policy"></a>

Attach a permissions policy to the role that grants the minimum permissions required to invoke your MCP server. For example, if your MCP server is hosted behind Amazon API Gateway, the role should have `execute-api:Invoke` permission on the API Gateway resource.

### Multi-region signing (SigV4a)
<a name="multi-region-signing-sigv4a"></a>

If your MCP server is deployed across multiple AWS Regions, you can use [SigV4a (Signature Version 4a)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) for multi-region signing. To enable this, enter `*` as the AWS Region when configuring the SigV4 authorization. SigV4a uses asymmetric signing, which allows a single signed request to be valid across multiple Regions.

## Cross-account access without a dedicated role
<a name="cross-account-access-without-a-dedicated-role"></a>

Instead of registering a dedicated IAM role for your MCP server, you can use **role-less registration**: register the server without a role and have AWS DevOps Agent sign requests using an IAM role from an AWS account already associated with your Agent Space. This is useful when your MCP server needs to access resources spanning the primary and secondary AWS accounts connected to an Agent Space, rather than a single role scoped to one account.

### How it works
<a name="how-it-works"></a>

Cross-account access without a dedicated role works as follows:

1. **Register the MCP server without a role** – On the SigV4 authorization configuration step, choose **Register without a dedicated role**. AWS DevOps Agent registers the server but does not validate the connection yet, because there is no role to sign a validation request with.

1. **Associate the MCP server with an Agent Space** – When you add the MCP server to an Agent Space, AWS DevOps Agent validates it using the **primary AWS account (monitor) role**. It assumes that role and calls `listTools` to confirm the server is reachable and the configuration is valid. The Agent Space must have a primary AWS account associated with it. That account's role must be able to invoke your MCP server.

1. **During investigations** – When the agent uses the MCP server while operating on a specific account, it signs requests with that account's role, the **primary account role** for the primary account, and the corresponding **secondary account role** for each secondary account. Each primary or secondary account role that the agent will use with this MCP server must be able to invoke it.

### Requirements
<a name="requirements"></a>

Before you associate a role-less SigV4 MCP server with an Agent Space:
+ The Agent Space must have a **primary AWS account** associated with it. Without a primary account, association fails because the primary account role performs the `listTools` validation. The error message is: *"SigV4 MCP server registered without a dedicated role requires a primary account association in the Agent Space."*
+ The **primary account role** must grant permission to invoke your MCP server (for example, `execute-api:Invoke` for an API Gateway-hosted server). Every **secondary account role** you expect the agent to use with this MCP server must also grant this permission. For more information, see [Permissions policy](configuring-integrations-and-knowledge-connecting-mcp-servers.html#permissions-policy). AWS DevOps Agent uses the primary role at association time, and secondary roles during investigations of those accounts.

## Troubleshooting
<a name="troubleshooting"></a>

### Associating a role-less MCP server fails: "requires a primary account association"
<a name="associating-a-role-less-mcp-server-fails-requires-a-primary-account-association"></a>

If you registered an MCP server without a dedicated role and association fails, check the error message. If the error states that the server *requires a primary account association in the Agent Space*, the Agent Space does not have a primary AWS account connected to it.

AWS DevOps Agent validates a role-less SigV4 MCP server when you associate it, using the IAM role of the primary AWS account of the Agent Space. To resolve this:

1. Add a primary AWS account to the Agent Space, if it does not already have one.

1. Make sure that account's IAM role has permission to invoke your MCP server (for example, `execute-api:Invoke` for a server hosted behind Amazon API Gateway).

1. Associate the MCP server again.

## Related topics
<a name="related-topics"></a>
+ Security in AWS DevOps Agent
+ Setting up an Agent Space
+ Prompt Injection Protection