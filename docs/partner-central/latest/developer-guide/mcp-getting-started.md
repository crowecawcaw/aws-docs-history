

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Getting Started with the Partner Central Agent MCP Server
<a name="mcp-getting-started"></a>

This guide walks you through setting up access to the Partner Central Agent MCP Server. The server supports two authentication methods: OAuth for browser-based sign-in and SigV4 for direct HTTPS access — no proxy or IDE plugin required.

## Prerequisites
<a name="mcp-prerequisites"></a>

Before you begin, make sure you have:
+ An active Partner Central account (migrated to the AWS console)
+ An AWS account linked to your Partner Central organization, with IAM permissions for Partner Central
+ An MCP-compatible client (Claude Code, Kiro, Claude Desktop, or any client that supports Model Context Protocol)

**For SigV4 authentication only**  
The following prerequisites apply only to SigV4 authentication.
+ AWS CLI installed and configured with credentials
+ An MCP-compatible client that supports JSON-RPC 2.0 and SigV4 request signing

## Step 1: Configure authentication and connect
<a name="mcp-step1-connect"></a>

With the Partner Central Agent MCP Server, you can authenticate using OAuth for browser-based sign-in or SigV4 for direct HTTPS access. Choose the method that best fits your workflow. Your MCP client connects directly to the endpoint — no proxy layer or IDE plugin required.

### Endpoint
<a name="mcp-endpoint"></a>

```
https://partnercentral-agents-mcp.us-east-1.api.aws/mcp
```

The Partner Central Agent MCP Server is currently available in US East (N. Virginia) only. You can connect to this endpoint from any location.

### Choosing an authentication method
<a name="mcp-choosing-auth"></a>


| Question | Use | 
| --- | --- | 
| Do you want to get started without installing AWS CLI or configuring local credentials? | OAuth | 
| Does your client support remote MCP servers with browser-based login? | OAuth | 
| Does your agent run without a browser (CI/CD, automation scripts)? | SigV4 | 
| Does your organization restrict signin:AuthorizeOAuth2Access and signin:CreateOAuth2Token permissions? | SigV4 | 

### Connect your MCP client
<a name="mcp-connect-client"></a>

Choose a tab to view setup instructions for your preferred authentication method.

------
#### [ OAuth (simple) ]

With OAuth, you sign in using the same credentials you use for the AWS Management Console. When you first connect, your MCP client opens a browser window to AWS Sign-In. After you authenticate and authorize access, tokens refresh automatically in the background.

**Note**  
Authorizing an agent does not grant it any additional AWS permissions. AWS evaluates every request against your IAM policies, service control policies, resource control policies, and permission boundaries.

**Prerequisites**  
Grant OAuth sign-in permissions to your IAM role or user. You can attach the `AWSMcpServiceActionsFullAccess` managed policy, or add the `signin:AuthorizeOAuth2Access` and `signin:CreateOAuth2Token` actions to your IAM policy.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "signin:AuthorizeOAuth2Access",
                "signin:CreateOAuth2Token"
            ],
            "Resource": "*"
        }
    ]
}
```

**Note**  
No explicit Allow for `partnercentral:*` actions is required for MCP protocol access. The MCP server grants protocol access by default to all authenticated AWS identities. The `signin:*` permissions above are only needed to enable the browser-based OAuth flow.

**Configure your MCP client**  
Use one of the following clients to connect.

**Claude Code CLI**  
Run the following command:

```
claude mcp add partnercentral --transport http https://partnercentral-agents-mcp.us-east-1.api.aws/mcp
```

**Claude Desktop**  
Add as a remote MCP server with the following URL:

```
https://partnercentral-agents-mcp.us-east-1.api.aws/mcp
```

**Kiro CLI (v3 or later)**  
Run the following command:

```
kiro-cli --v3 mcp add --name partnercentral --url https://partnercentral-agents-mcp.us-east-1.api.aws/mcp
```

**Note**  
OAuth with the Partner Central Agent MCP Server requires Kiro CLI version 3 or later. Earlier versions do not support this flow.

**Kiro IDE**  
Add as a remote MCP server with the following URL:

```
https://partnercentral-agents-mcp.us-east-1.api.aws/mcp
```

**Amazon Quick**  
Create a connector and install it in Quick Desktop.

**Part 1: Create the connector**  
Complete the following steps in Amazon Quick.

1. In the left panel of Amazon Quick, open **Capabilities** → **Connectors**.

1. Choose **Create** → **Web Connectors**. Quick web opens in your default browser.

1. Select the **Create for your team** tab, then choose **Model Context Protocol**.

1. Choose **No, Create New** and enter the following:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/partner-central/latest/developer-guide/mcp-getting-started.html)

1. Choose **Next**.

1. For **Auth configuration**, select **Default OAuth app**.

1. Choose **Create and Continue**. A browser popup opens to sign in with your Partner Central account — select your existing signed-in account.

1. After the popup closes, choose **Next** to reach the review section.

1. In the **Publish** section, select the aliases you want to share the connector with (including your own), or share with your entire organization.

**Part 2: Connect in Quick Desktop**  
Install the connector in your desktop application.

1. In Quick Desktop, open **Capabilities**.

1. On the **Connectors** tab, choose **Browse More** and search for **Partner Central Agents**. It might take a few minutes to appear.

1. Choose **Install**.

**Note**  
If your client is not listed, use the endpoint URL above. If tool calls fail due to credential errors, append `?oauth=initialize` to the URL to explicitly trigger the OAuth sign-in flow.

------
#### [ SigV4 (advanced) ]

Use SigV4 to authenticate requests for custom MCP clients, headless agents, CI/CD pipelines, or automation scripts.

**Prerequisites**  
Complete the following steps before connecting.

1. Install the AWS CLI.

1. Sign in and configure credentials: `aws configure`

1. Verify access: `aws sts get-caller-identity`

**Note**  
No explicit IAM Allow is required for MCP protocol access. The MCP server grants access by default to all authenticated AWS identities. You only need valid AWS credentials that can sign requests.

**Configure**  
Sign requests using AWS Signature Version 4 with the following parameters:
+ Service name: `partnercentral-agents-mcp`
+ Region: `us-east-1`

Example using `awscurl`:

```
awscurl --service partnercentral-agents-mcp --region us-east-1 \
  -X POST -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}' \
  "https://partnercentral-agents-mcp.us-east-1.api.aws/mcp"
```

------

**Important**  
When you connect to the MCP server, you have protocol access only. To perform Partner Central operations such as querying opportunities or managing funding, you must also grant data access permissions. See [Step 2: Grant data access permissions](#mcp-step2-data-permissions).

**Restricting MCP access**  
By default, all authenticated AWS identities have protocol access to the MCP server. To block MCP access for specific users or accounts, apply an explicit Deny on `partnercentral:InvokeMcp`:

```
{
    "Effect": "Deny",
    "Action": "partnercentral:InvokeMcp",
    "Resource": "*"
}
```

### MCP protocol reference
<a name="mcp-protocol-reference"></a>

This section describes the JSON-RPC protocol for custom MCP client implementations. If you are using Claude Code, Kiro, or Claude Desktop, your client handles these requests automatically.

The request and response format is identical for both OAuth and SigV4 authentication. The only difference is the HTTP authentication header: OAuth uses `Authorization: Bearer <token>`, while SigV4 uses AWS signature headers.

### Initialize the MCP connection
<a name="mcp-initialize-connection"></a>

Send an `initialize` request to establish the protocol:

```
{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2025-03-26",
        "capabilities": {},
        "clientInfo": {
            "name": "my-partner-client",
            "version": "1.0.0"
        }
    }
}
```

Expected response:

```
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "protocolVersion": "2025-03-26",
        "capabilities": {
            "tools": {
                "listChanged": false
            }
        },
        "serverInfo": {
            "name": "PartnerCentralAgentMCPServer",
            "version": "1.0.0"
        }
    }
}
```

### List available tools
<a name="mcp-list-tools"></a>

```
{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/list",
    "params": {}
}
```

## Step 2: Grant data access permissions
<a name="mcp-step2-data-permissions"></a>

When you connect to the MCP server, you have protocol access only. To perform Partner Central operations such as querying opportunities or managing funding, you need additional IAM permissions. The following sections describe how to attach policies and the available permission levels.

### Attaching IAM policies
<a name="mcp-attaching-iam-policies"></a>

To attach a policy to your IAM identity using the AWS Management Console:

1. Open the [IAM console](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, choose **Users**, **User groups**, or **Roles** depending on the identity you want to attach the policy to, then choose the name of the specific user, group, or role.

1. Choose the **Permissions** tab.

1. Choose **Attach policies** (or **Add permissions** if it's the first time).

1. In the policy list, search for and select the managed policy you want to attach (for example, a custom policy you created from the JSON blocks below).

1. Choose **Attach policies** (or **Next** and then **Add permissions**) to confirm.

The permissions take effect immediately. You can attach multiple policies to the same identity.

### Recommended: Use the managed policy
<a name="mcp-managed-policy"></a>

The simplest way to grant data access permissions is to attach the `AWSPartnerCentralFullAccess` managed policy to your IAM identity. This policy includes permissions for all Partner Central operations available through the MCP server.

For fine-grained control, use the custom policies in the following sections to grant only the specific actions your use case requires.

### Data access permissions
<a name="mcp-data-access-permissions"></a>

To actually perform Partner Central operations through the agent, you need additional permissions based on your use case.

**Opportunity management:**

```
{
    "Effect": "Allow",
    "Action": [
        "partnercentral:List*",
        "partnercentral:Get*",
        "partnercentral:CreateOpportunity",
        "partnercentral:UpdateOpportunity",
        "partnercentral:SubmitOpportunity",
        "partnercentral:AssignOpportunity",
        "partnercentral:AssociateOpportunity",
        "partnercentral:DisassociateOpportunity"
    ],
    "Resource": "*"
}
```

**Funding programs:**

```
{
    "Effect": "Allow",
    "Action": [
        "partnercentral:ListBenefitAllocations",
        "partnercentral:ListBenefitApplications",
        "partnercentral:CreateBenefitApplication",
        "partnercentral:GetBenefitApplication",
        "partnercentral:UpdateBenefitApplication",
        "partnercentral:SubmitBenefitApplication",
        "partnercentral:AmendBenefitApplication",
        "partnercentral:CancelBenefitApplication",
        "partnercentral:RecallBenefitApplication",
        "partnercentral:AssociateBenefitApplicationResource",
        "partnercentral:DisassociateBenefitApplicationResource"
    ],
    "Resource": "*"
}
```

**Marketplace access:**

```
{
    "Effect": "Allow",
    "Action": [
        "aws-marketplace:DescribeEntity",
        "aws-marketplace:DescribeAgreement",
        "aws-marketplace:SearchAgreements",
        "aws-marketplace:ListEntities"
    ],
    "Resource": "*"
}
```

**Partner Central Onboarding:**

```
{
    "Effect": "Allow",
    "Action": [
        "partnercentral:ListPartners",
        "partnercentral:GetPartner",
        "partnercentral:GetProfileVisibility",
        "partnercentral:GetAllianceLeadContact",
        "partnercentral:GetProfileUpdateTask",
        "partnercentral:StartProfileUpdateTask",
        "partnercentral:CancelProfileUpdateTask",
        "partnercentral:PutProfileVisibility",
        "partnercentral:PutAllianceLeadContact",
        "partnercentral:SendEmailVerificationCode",
        "partnercentral:AssociateAwsTrainingCertificationEmailDomain",
        "partnercentral:DisassociateAwsTrainingCertificationEmailDomain",
        "partnercentral:GetAccountConnections",
        "partnercentral:GetConnectionInvitations",
        "partnercentral:CreateConnectionInvitation",
        "partnercentral:CancelConnectionInvitation",
        "partnercentral:RespondConnectionInvitation",
        "partnercentral:CancelConnection",
        "partnercentral:ManageConnectionPreferences"
    ],
    "Resource": "*"
}
```

For Marketplace seller setup, also add:

```
{
    "Effect": "Allow",
    "Action": [
        "aws-marketplace:ListEntities",
        "aws-marketplace:DescribeEntity",
        "aws-marketplace:DescribeChangeSet",
        "aws-marketplace:StartChangeSet"
    ],
    "Resource": "*"
}
```

For service-linked role management (Resale Authorizations/CPPO):

```
{
    "Effect": "Allow",
    "Action": [
        "iam:GetRole",
        "iam:CreateServiceLinkedRole"
    ],
    "Resource": "*"
}
```

### Full access policy
<a name="mcp-full-access-policy"></a>

For development and testing, you can combine all permissions into a single policy:

```
aws iam create-policy \
    --policy-name PartnerCentralAgentsFullAccess \
    --policy-document '{
        "Version": "2012-10-17",		 	 	 
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "partnercentral:List*",
                    "partnercentral:Get*",
                    "partnercentral:CreateOpportunity",
                    "partnercentral:UpdateOpportunity",
                    "partnercentral:SubmitOpportunity",
                    "partnercentral:AssignOpportunity",
                    "partnercentral:AssociateOpportunity",
                    "partnercentral:DisassociateOpportunity",
                    "partnercentral:CreateResourceSnapshot",
                    "partnercentral:CreateResourceSnapshotJob",
                    "partnercentral:StartResourceSnapshotJob",
                    "partnercentral:CreateEngagement",
                    "partnercentral:CreateEngagementInvitation",
                    "partnercentral:RejectEngagementInvitation",
                    "partnercentral:StartEngagementByAcceptingInvitationTask",
                    "partnercentral:StartEngagementFromOpportunityTask",
                    "partnercentral:CreateBenefitApplication",
                    "partnercentral:UpdateBenefitApplication",
                    "partnercentral:SubmitBenefitApplication",
                    "partnercentral:AmendBenefitApplication",
                    "partnercentral:CancelBenefitApplication",
                    "partnercentral:RecallBenefitApplication",
                    "partnercentral:AssociateBenefitApplicationResource",
                    "partnercentral:DisassociateBenefitApplicationResource",
                    "partnercentral:ListPartners",
                    "partnercentral:StartProfileUpdateTask",
                    "partnercentral:CancelProfileUpdateTask",
                    "partnercentral:PutProfileVisibility",
                    "partnercentral:PutAllianceLeadContact",
                    "partnercentral:SendEmailVerificationCode",
                    "partnercentral:AssociateAwsTrainingCertificationEmailDomain",
                    "partnercentral:DisassociateAwsTrainingCertificationEmailDomain",
                    "partnercentral:CreateConnectionInvitation",
                    "partnercentral:CancelConnectionInvitation",
                    "partnercentral:RespondConnectionInvitation",
                    "partnercentral:CancelConnection",
                    "partnercentral:ManageConnectionPreferences"
                ],
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "aws-marketplace:DescribeEntity",
                    "aws-marketplace:DescribeAgreement",
                    "aws-marketplace:SearchAgreements",
                    "aws-marketplace:ListEntities",
                    "aws-marketplace:DescribeChangeSet",
                    "aws-marketplace:StartChangeSet"
                ],
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "iam:GetRole",
                    "iam:CreateServiceLinkedRole"
                ],
                "Resource": "*"
            }
        ]
    }'
```

### Read-only policy
<a name="mcp-read-only-policy"></a>

For production environments or read-only use cases, restrict permissions to read operations:

```
aws iam create-policy \
    --policy-name PartnerCentralAgentReadOnly \
    --policy-document '{
        "Version": "2012-10-17",		 	 	 
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "partnercentral:List*",
                    "partnercentral:Get*",
                    "partnercentral:ListPartners",
                    "partnercentral:GetPartner",
                    "partnercentral:GetProfileVisibility",
                    "partnercentral:GetAllianceLeadContact",
                    "partnercentral:GetProfileUpdateTask",
                    "partnercentral:GetAccountConnections",
                    "partnercentral:GetConnectionInvitations"
                ],
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "aws-marketplace:DescribeEntity",
                    "aws-marketplace:DescribeAgreement",
                    "aws-marketplace:SearchAgreements",
                    "aws-marketplace:ListEntities",
                    "aws-marketplace:DescribeChangeSet"
                ],
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "iam:GetRole"
                ],
                "Resource": "*"
            }
        ]
    }'
```

## Signing your calls with MCP header
<a name="mcp-signing-calls-header"></a>

When making requests to Partner Central agents MCP, we recommend including the custom MCP header using the following methods to help AWS identify the source of the client application, monitor usage, and audit performance. AWS uses this header to distinguish the type of client application making the call and to gather insights about the success rate of different client implementations.

### Method 1: \_meta field (programmatic/stateless MCP)
<a name="mcp-header-meta-field"></a>

For code that directly constructs MCP `tools/call` requests, provide the `_meta` field on requests.

```
{
    "method": "tools/call",
    "params": {
        "name": "sendMessage",
        "arguments": {
            "content": [
                {
                    "type": "text",
                    "text": "List my open opportunities with expected close date in Q1 2026"
                }
            ],
            "catalog": "AWS"
        },
        "_meta": {
            "integrator": "<Integrator's Company Name / Direct>",
            "sourceProduct": "<Integrator's Application Name>"
        }
    }
}
```

### Method 2: clientInfo (session-based custom agents)
<a name="mcp-header-client-info"></a>

For custom MCP clients establishing sessions, provide MCP header info inside the `clientInfo` field:

```
{
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "clientInfo": {
            "integrator": "<Integrator's Company Name / Direct>",
            "sourceProduct": "<Integrator's Application Name>"
        }
    }
}
```

Fields in `clientInfo`:
+ `integrator` — Company name or "Direct" for partners

  Example: `AWS`
+ `sourceProduct` — Product/agent name

  Example: `AWS CRM Connector`

### Method 3: URL parameter (hosted MCP only)
<a name="mcp-header-url-parameter"></a>

Only for hosted MCP clients where the integrator cannot modify protocol fields. Use the URL parameter:

Server URL: `https://partnercentral-agents-mcp.us-east-1.api.aws/mcp?appId=<Integrator's Company Name / Direct>`

## Step 3: Verify your setup
<a name="mcp-step3-verify"></a>

Send a simple message to confirm everything is working. Use the `Sandbox` catalog for testing:

```
{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
        "name": "sendMessage",
        "arguments": {
            "content": [
                {
                    "type": "text",
                    "text": "Hello, what can you help me with?"
                }
            ],
            "catalog": "Sandbox"
        }
    }
}
```

If you receive a response with `"status": "complete"` and a text reply from the agent, your setup is working correctly. The response will also include a `sessionId` that you can use for follow-up messages.

## Step 4: Run your first tasks
<a name="mcp-step4-tasks"></a>

### Query your opportunities
<a name="mcp-query-opportunities"></a>

```
{
    "jsonrpc": "2.0",
    "id": 4,
    "method": "tools/call",
    "params": {
        "name": "sendMessage",
        "arguments": {
            "sessionId": "session-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "content": [
                {
                    "type": "text",
                    "text": "List my open opportunities with expected revenue over $50K"
                }
            ],
            "catalog": "AWS"
        }
    }
}
```

### Check funding eligibility
<a name="mcp-check-funding"></a>

```
{
    "jsonrpc": "2.0",
    "id": 5,
    "method": "tools/call",
    "params": {
        "name": "sendMessage",
        "arguments": {
            "sessionId": "session-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "content": [
                {
                    "type": "text",
                    "text": "Am I eligible for MAP funding for opportunity O1234567890?"
                }
            ],
            "catalog": "AWS"
        }
    }
}
```

### Retrieve session history
<a name="mcp-retrieve-session"></a>

```
{
    "jsonrpc": "2.0",
    "id": 6,
    "method": "tools/call",
    "params": {
        "name": "getSession",
        "arguments": {
            "sessionId": "session-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "catalog": "AWS"
        }
    }
}
```

### Partner onboarding
<a name="mcp-partner-onboarding-task"></a>

```
{
    "jsonrpc": "2.0",
    "id": 7,
    "method": "tools/call",
    "params": {
        "name": "sendMessage",
        "arguments": {
            "sessionId": "session-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "content": [
                {
                    "type": "text",
                    "text": "Help me onboard to Partner Central"
                }
            ],
            "catalog": "AWS"
        }
    }
}
```

Other onboarding tasks to try:
+ "Guide me through the tax interview process"
+ "Can you look at my website and fill in my partner profile?"
+ "What do I still need to do to be ready to sell on Marketplace?"

## Security considerations
<a name="mcp-security-considerations"></a>
+ Do not pass AWS credentials through MCP tool parameters. SigV4 request signing or OAuth tokens handle authentication at the transport layer.
+ Use the Sandbox catalog for testing and development. The `"Sandbox"` catalog provides an isolated environment that does not affect production partner data.
+ Apply least-privilege IAM policies in production. Use the read-only policy for monitoring and reporting use cases. Only grant write permissions when the user needs to update opportunities or submit funding applications.
+ Review write operations carefully. The server uses human-in-the-loop approval for all write operations. When a write action is proposed, review the parameters before approving.
+ Session data is transient. Sessions expire 48 hours after creation. Do not rely on sessions for long-term data storage.
+ File uploads go to an ephemeral S3 bucket. Uploaded files are stored temporarily and are not retained permanently. Do not upload files containing credentials, secrets, or other sensitive information.
+ OAuth tokens refresh automatically for up to 12 hours. After the session expires, re-authenticate through the browser.
+ Authorizing an agent does not grant additional AWS permissions beyond your existing IAM policies, service control policies, resource control policies, and permission boundaries.

## Troubleshooting
<a name="mcp-troubleshooting"></a>

The following table lists common errors and their resolutions.


| Error | Cause | Resolution | 
| --- | --- | --- | 
| The security token included in the request is invalid | Expired credentials | Run aws sso login to refresh credentials | 
| Access denied: User is not authorized to perform signin:AuthorizeOAuth2Access | Missing OAuth permissions | Attach AWSMcpServiceActionsFullAccess or add signin permissions | 
| 400 error after OAuth sign-in | IAM principal lacks OAuth permissions | Verify signin:AuthorizeOAuth2Access and signin:CreateOAuth2Token are allowed | 
| Access denied or implicit deny on partnercentral:InvokeMcp or signin:\* actions | Organization uses allowlist-based Service Control Policies (SCPs) that block services not explicitly permitted | Ask your AWS administrator to add partnercentral and signin (for OAuth only) to the allowed services in your organization's SCPs. The SCP must permit these services at the account level before identity policies can take effect. The only action that controls MCP protocol access is partnercentral:InvokeMcp — an explicit Deny on this action blocks all MCP requests. | 

## Next steps
<a name="mcp-next-steps"></a>
+ [**Configuration Reference**](https://docs.aws.amazon.com/partner-central/latest/APIReference/mcp-configuration-reference.html) — Full reference for endpoint, IAM actions, session management, and error codes
+ [**Tools Reference**](https://docs.aws.amazon.com/partner-central/latest/APIReference/mcp-tools-reference.html) — Detailed documentation for `sendMessage` and `getSession` tools