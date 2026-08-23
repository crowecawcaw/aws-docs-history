The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Configuration Reference

This page provides the complete reference for connecting to and configuring the Partner Central
Agent MCP Server.

## Endpoint

| Property           | Value                                                     |
| ------------------ | --------------------------------------------------------- |
| URL                | `https://partnercentral-agents-mcp.us-east-1.api.aws/mcp` |
| Region             | `us-east-1` (N. Virginia) only                            |
| Protocol           | JSON-RPC 2.0 over HTTPS                                   |
| Streaming          | Server-Sent Events (SSE)                                  |
| Authentication     | AWS Signature Version 4                                   |
| SigV4 service name | `partnercentral-agents-mcp`                               |
| TLS requirement    | TLS 1.2 or higher                                         |

## IAM permissions

All IAM actions use the `partnercentral:` prefix unless otherwise
noted.

### MCP protocol access

As an authenticated AWS identity, you have protocol access to the MCP server by
default. You do not need an explicit IAM Allow for protocol access.

For OAuth authentication, the following sign-in permissions are required:

| Action                         | Description                              |
| ------------------------------ | ---------------------------------------- |
| `signin:AuthorizeOAuth2Access` | Authorizes the browser-based OAuth flow  |
| `signin:CreateOAuth2Token`     | Issues and refreshes OAuth access tokens |

To restrict MCP access, apply an explicit Deny on
`partnercentral:InvokeMcp`.

### Opportunity management

| Action                                              | Description                                                        |
| --------------------------------------------------- | ------------------------------------------------------------------ |
| `partnercentral:List*`                              | List opportunities, solutions, and other Partner Central resources |
| `partnercentral:Get*`                               | Retrieve details for individual opportunities and other resources  |
| `partnercentral:CreateOpportunity`                  | Create an opportunity                                              |
| `partnercentral:UpdateOpportunity`                  | Modify opportunity fields (stage, close date, revenue, etc.)       |
| `partnercentral:SubmitOpportunity`                  | Submit an opportunity for AWS review                               |
| `partnercentral:AssignOpportunity`                  | Assign an opportunity to a partner representative                  |
| `partnercentral:AssociateOpportunity`               | Link an opportunity to another resource (solution, etc.)           |
| `partnercentral:DisassociateOpportunity`            | Remove a link between an opportunity and another resource          |
| `partnercentral:StartEngagementFromOpportunityTask` | Submit opportunities to start an engagement from an opportunity    |

### Funding programs

| Action                                                  | Description                                         |
| ------------------------------------------------------- | --------------------------------------------------- |
| `partnercentral:ListBenefitAllocations`                 | List available benefit allocations for your account |
| `partnercentral:ListBenefitApplications`                | List submitted benefit applications                 |
| `partnercentral:CreateBenefitApplication`               | Create a new benefit application (MAP, POC, WMP)    |
| `partnercentral:GetBenefitApplication`                  | Retrieve details of a specific benefit application  |
| `partnercentral:UpdateBenefitApplication`               | Update a pending benefit application                |
| `partnercentral:AssociateBenefitApplicationResource`    | Link a resource to a benefit application            |
| `partnercentral:DisassociateBenefitApplicationResource` | Remove a resource link from a benefit application   |

### Marketplace access

| Action                             | Description                              |
| ---------------------------------- | ---------------------------------------- |
| `aws-marketplace:DescribeEntity`   | Retrieve details of a marketplace entity |
| `aws-marketplace:SearchAgreements` | Search marketplace agreements            |
| `aws-marketplace:ListEntities`     | List marketplace entities                |

### Onboarding Agent

**Partner account management
(`partnercentral`):**

| Action                                                           | Description                                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------------- |
| `partnercentral:ListPartners`                                    | List partner registrations for the account                      |
| `partnercentral:GetPartner`                                      | Retrieve partner registration and profile details               |
| `partnercentral:GetProfileVisibility`                            | Retrieve current profile visibility (PUBLIC/PRIVATE)            |
| `partnercentral:GetAllianceLeadContact`                          | Retrieve alliance lead contact information                      |
| `partnercentral:GetProfileUpdateTask`                            | Check status of a pending async profile update                  |
| `partnercentral:StartProfileUpdateTask`                          | Submit a partner profile update (async)                         |
| `partnercentral:CancelProfileUpdateTask`                         | Cancel a pending profile update task                            |
| `partnercentral:PutProfileVisibility`                            | Change profile visibility to PUBLIC or PRIVATE                  |
| `partnercentral:PutAllianceLeadContact`                          | Update alliance lead contact (name, title, email)               |
| `partnercentral:SendEmailVerificationCode`                       | Send a verification code for email-based domain/contact changes |
| `partnercentral:AssociateAwsTrainingCertificationEmailDomain`    | Link an email domain for training certification tracking        |
| `partnercentral:DisassociateAwsTrainingCertificationEmailDomain` | Remove a linked training certification email domain             |
| `partnercentral:GetAccountConnections`                           | List active account connections (e.g., subsidiary links)        |
| `partnercentral:GetConnectionInvitations`                        | List pending sent and received connection invitations           |
| `partnercentral:CreateConnectionInvitation`                      | Send a connection invitation to another AWS account             |
| `partnercentral:CancelConnectionInvitation`                      | Cancel a pending outgoing connection invitation                 |
| `partnercentral:RespondConnectionInvitation`                     | Accept or reject an incoming connection invitation              |
| `partnercentral:CancelConnection`                                | Cancel an active account connection                             |
| `partnercentral:ManageConnectionPreferences`                     | Get or update sharing preferences between connected accounts    |

**Marketplace seller setup
(`aws-marketplace`):**

| Action                              | Description                                                   |
| ----------------------------------- | ------------------------------------------------------------- |
| `aws-marketplace:ListEntities`      | List Marketplace entities (e.g., seller entities)             |
| `aws-marketplace:DescribeEntity`    | Retrieve full details of a Marketplace entity                 |
| `aws-marketplace:DescribeChangeSet` | Check status of a submitted change set                        |
| `aws-marketplace:StartChangeSet`    | Submit a Marketplace change set (e.g., seller profile update) |

**IAM — service-linked role
(`iam`):**

| Action                        | Description                                                                      |
| ----------------------------- | -------------------------------------------------------------------------------- |
| `iam:GetRole`                 | Check whether the Marketplace Resale Authorization service-linked role<br>exists |
| `iam:CreateServiceLinkedRole` | Create the `AWSServiceRoleForMarketplaceResaleAuthorization`<br>role             |

## Catalog environments

| Catalog     | Description                                                                                        |
| ----------- | -------------------------------------------------------------------------------------------------- |
| `"AWS"`     | Production environment. All operations affect live partner data.                                   |
| `"Sandbox"` | Isolated testing environment. No impact on production data. Use for development<br>and validation. |

## Session management

| Property          | Value                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------- |
| Session ID format | UUID v4 with `session-` prefix (e.g.,<br>`session-550e8400-e29b-41d4-a716-446655440000`) |
| Session creation  | Automatic on first `sendMessage` call without a<br>`sessionId`                           |
| Session expiry    | 48 hours from session creation (absolute expiry, not<br>inactivity-based)                |

## File upload

| Property               | Value                                                           |
| ---------------------- | --------------------------------------------------------------- |
| Max files per message  | 3                                                               |
| Image size limit       | 3.75 MB                                                         |
| Document size limit    | 4.5 MB                                                          |
| Allowed extensions     | `doc`, `docx`, `pdf`, `png`,<br>`jpeg`, `xlsx`, `csv`,<br>`txt` |
| S3 bucket (production) | aws-partner-central-marketplace-ephemeral-writeonly-files       |
| Upload path            | s3://{bucket}/{aws-account-id}/                                 |
| S3 URI requirement     | Must include `versionId` query parameter                        |

### Upload workflow

1. Upload your file to the appropriate S3 bucket under your AWS account ID
   prefix.
2. Note the S3 URI including the `versionId` returned by the
   upload.
3. Include the file as a `document` content block in your
   `sendMessage` call.

Example S3 URI format:

```
s3://aws-partner-central-marketplace-ephemeral-writeonly-files/123456789012/my-document.pdf?versionId=abc123
```

## Error codes

| Code     | Name                     | Description                                                                    |
| -------- | ------------------------ | ------------------------------------------------------------------------------ |
| `-32001` | `AUTHENTICATION_FAILURE` | SigV4 signature is invalid or credentials have expired                         |
| `-31004` | `TOOL_PERMISSION_DENIED` | IAM identity lacks the required `partnercentral:` action for this<br>operation |
| `-32002` | `ACCESS_DENIED`          | General access denied (account not enrolled, region mismatch, etc.)            |
| `-32004` | `LIMIT_EXCEEDED`         | Rate limit or quota exceeded. Retry with exponential backoff.                  |
| `-30001` | `RESOURCE_NOT_FOUND`     | Requested resource (session, opportunity, etc.) does not exist                 |
| `-32600` | `INVALID_REQUEST`        | Malformed JSON-RPC request or invalid parameters                               |
| `-32603` | `INTERNAL_ERROR`         | Server-side error. Retry the request.                                          |

## Rate limits

The server enforces per-account rate limits:

| Operation            | Sustained rate         | Burst |
| -------------------- | ---------------------- | ----- |
| `sendMessage`        | 2 requests per minute  | 10    |
| All other operations | 10 requests per minute | 20    |

If you exceed these limits, the server returns error code `-32004`
(LIMIT\_EXCEEDED). Implement exponential backoff with jitter in your client to handle rate
limiting gracefully.

## Streaming (SSE) event types

When `stream` is set to `true` in a `sendMessage`
call, the server returns Server-Sent Events with these event types:

| Event Type                     | Description                                              |
| ------------------------------ | -------------------------------------------------------- |
| `stream_start`                 | Stream connection established                            |
| `assistant-response.start`     | Agent has begun generating a response                    |
| `assistant-response.delta`     | Incremental text chunk of the agent's response           |
| `assistant-response.completed` | Agent has finished generating the response               |
| `server-tool-use`              | Agent is invoking an internal tool (read operation)      |
| `server-tool-response`         | Result of an internal tool invocation                    |
| `tool_approval_request`        | Agent is requesting human approval for a write operation |
| `stream_end`                   | Stream connection closing                                |
| `done`                         | Final event indicating the SSE stream is complete        |

## Next steps

- [**Tools Reference**](../APIReference/mcp-tools-reference.md "../APIReference/mcp-tools-reference.md") — Detailed documentation
  for `sendMessage` and `getSession` tools
