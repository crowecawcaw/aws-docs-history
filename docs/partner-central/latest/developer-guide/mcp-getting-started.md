The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Getting Started with the Partner Central Agent MCP Server

This guide walks you through setting up programmatic access to the Partner Central Agent MCP Server
using a custom MCP client. The server uses direct HTTPS with SigV4 authentication — no proxy
or IDE plugin required.

## Prerequisites

Before you begin, make sure you have:

- An active Partner Central account (migrated to the AWS console)
- An AWS account with IAM permissions for Partner Central
- AWS CLI installed and configured with credentials
- Access to the us-east-1 (N. Virginia) region
- HTTPS connectivity to
  `partnercentral-agents-mcp.us-east-1.api.aws`
- TLS 1.2+ support in your HTTP client
- An MCP-compatible client that supports JSON-RPC 2.0 and SigV4 request
  signing

## Step 1: Set up IAM permissions

The Partner Central Agent MCP Server requires IAM permissions at two levels: protocol access
(to communicate with the MCP endpoint) and data access (to perform Partner Central
operations).

### Attaching IAM policies

To attach a policy to your IAM identity using the AWS Management Console:

1. Open the [IAM
   console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Users**,
   **User groups**, or
   **Roles** depending on the identity you want to attach the
   policy to, then choose the name of the specific user, group, or role.
3. Choose the **Permissions**
   tab.
4. Choose **Attach policies** (or
   **Add permissions** if it's the first
   time).
5. In the policy list, search for and select the managed policy you want to
   attach (for example, a custom policy you created from the JSON blocks
   below).
6. Choose **Attach policies** (or
   **Next** and then
   **Add permissions**) to confirm.

The permissions take effect immediately. You can attach multiple policies to the same
identity.

### Recommended: Use the managed policy

The simplest way to grant MCP protocol access is to attach the
`AWSMcpServiceActionsFullAccess` managed policy to your IAM identity. This
policy includes all permissions needed to interact with the MCP server.

For fine-grained control, you can use the `aws:IsMcpServiceAction`
condition key in your IAM policies to scope permissions specifically to MCP service
actions.

### Minimum permissions for MCP protocol access

At minimum, your IAM identity needs this action to interact with the MCP
server:

| Action                      | Description                                                    |
| --------------------------- | -------------------------------------------------------------- |
| `partnercentral:UseSession` | Required to create, update, and retrieve conversation sessions |

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "partnercentral:UseSession"
            ],
            "Resource": "*",
			"Condition": {
                "Bool": {
                    "aws:IsMcpServiceAction": "true"
                }
            }
        }
    ]


}
```

### Data access permissions

To actually perform Partner Central operations through the agent, you need additional
permissions based on your use case.

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

For development and testing, you can combine all permissions into a single
policy:

```
aws iam create-policy \
    --policy-name PartnerCentralAgentsFullAccess \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "partnercentral:UseSession",
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

For production environments or read-only use cases, restrict permissions to read
operations:

```
aws iam create-policy \
    --policy-name PartnerCentralAgentReadOnly \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "partnercentral:UseSession",
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

## Step 2: Connect your MCP client

The Partner Central Agent MCP Server uses direct HTTPS with SigV4 request signing. There is no
proxy layer — your MCP client sends JSON-RPC 2.0 requests directly to the
endpoint.

### Endpoint

```
https://partnercentral-agents-mcp.us-east-1.api.aws/mcp
```

### Authentication

All requests must be signed with [AWS
Signature Version 4](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") using:

- Service name: `partnercentral-agents-mcp`
- Region: `us-east-1`

### Initialize the MCP connection

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

```
{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/list",
    "params": {}
}
```

## Signing your calls with MCP header

When making requests to Partner Central agents MCP, we recommend including the custom MCP header
using the following methods to help AWS identify the source of the client application,
monitor usage, and audit performance. AWS uses this header to distinguish the type of
client application making the call and to gather insights about the success rate of
different client implementations.

### Method 1: \_meta field (programmatic/stateless MCP)

For code that directly constructs MCP `tools/call` requests, provide the
`_meta` field on requests.

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

For custom MCP clients establishing sessions, provide MCP header info inside the
`clientInfo` field:

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

- `integrator` — Company name or "Direct" for partners

Example: `AWS`

- `sourceProduct` — Product/agent name

Example: `AWS CRM Connector`

### Method 3: URL parameter (hosted MCP only)

Only for hosted MCP clients where the integrator cannot modify protocol fields. Use
the URL parameter:

Server URL:
`https://mcp.partnercentral.aws?appId=<Integrator's Company Name / Direct>`

## Step 3: Verify your setup

Send a simple message to confirm everything is working. Use the
`Sandbox` catalog for testing:

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

If you receive a response with `"status": "complete"` and a text reply from
the agent, your setup is working correctly. The response will also include a
`sessionId` that you can use for follow-up messages.

## Step 4: Run your first tasks

### Query your opportunities

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

- "Guide me through the tax interview process"
- "Can you look at my website and fill in my partner profile?"
- "What do I still need to do to be ready to sell on Marketplace?"

## Security considerations

- Do not pass AWS credentials through MCP tool parameters. Authentication is
  handled by SigV4 request signing at the transport layer.
- Use the Sandbox catalog for testing and development. The
  `"Sandbox"` catalog provides an isolated environment that does not affect
  production partner data.
- Apply least-privilege IAM policies in production. Use the read-only policy
  for monitoring and reporting use cases. Only grant write permissions when the user needs to
  update opportunities or submit funding applications.
- Review write operations carefully. The server uses human-in-the-loop approval
  for all write operations. When a write action is proposed, review the parameters before
  approving.
- Session data is transient. Sessions expire 48 hours after creation. Do not
  rely on sessions for long-term data storage.
- File uploads go to an ephemeral S3 bucket. Uploaded files are stored
  temporarily and are not retained permanently. Do not upload files containing credentials,
  secrets, or other sensitive information.

## Next steps

- [**Configuration Reference**](../APIReference/mcp-configuration-reference.md "../APIReference/mcp-configuration-reference.md") — Full reference
  for endpoint, IAM actions, session management, and error codes
- [**Tools Reference**](../APIReference/mcp-tools-reference.md "../APIReference/mcp-tools-reference.md") — Detailed documentation
  for `sendMessage` and `getSession` tools
