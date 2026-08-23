# Configure OAuth access to AWS MCP Server

## Overview

AWS MCP Server supports OAuth authorization through AWS Sign-In. With OAuth
authorization, agents can access AWS using the same identities, permissions, and
governance model that you already use with the AWS Management Console and AWS CLI.
When you authorize an agent, it can access AWS MCP Server on your behalf.
Authorization does not grant the agent additional AWS permissions.

Use this guide to configure OAuth access to AWS MCP Server. It covers
supported authorization models, required IAM permissions, and how to govern and
monitor OAuth access.

For more information about OAuth support in AWS Sign-In, see [Sign-In with OAuth 2.0](oauth-sign-in-overview.md "oauth-sign-in-overview.md").

## Prerequisites

Before connecting an agent to AWS MCP Server, make sure that:

- Your IAM identity has the required permissions for OAuth
  authorization.
- Your agent supports the Model Context Protocol (MCP).
- Your agent supports OAuth 2.1 authorization.

Grant the required permissions by attaching the [AWS
managed policy](../../../aws-managed-policy/latest/reference/AWSMCPSignInOAuthAccessPolicy.md "../../../aws-managed-policy/latest/reference/AWSMCPSignInOAuthAccessPolicy.md"):

```
aws iam attach-role-policy \
  --role-name `MyRole` \
  --policy-arn arn:aws:iam::aws:policy/AWSMCPSignInOAuthAccessPolicy
```

This managed policy grants:

- `signin:AuthorizeOAuth2Access`
- `signin:CreateOAuth2Token`

If you authenticate as the AWS account root user, no additional IAM permissions are
required.

## Supported Redirect URIs for DCR

Agents can register with AWS Sign-In and use one or more
approved redirect URIs during the OAuth authorization process.

| OAuth client             | Redirect URI(s)                                         |
| ------------------------ | ------------------------------------------------------- |
| Localhost                | `localhost`, `127.0.0.1`                                |
| Claude                   | `https://claude.ai/*`                                   |
| Cursor Desktop           | `cursor://anysphere.cursor-mcp/oauth/callback`          |
| Cursor Web               | `https://www.cursor.com/agents/mcp/oauth/callback`      |
| Visual Studio Code       | `vscode://*`                                            |
| Visual Studio Code (Web) | `https://vscode.dev/*`                                  |
| ChatGPT                  | `https://chatgpt.com/*`                                 |
| ChatGPT Connectors       | `https://chatgpt.com/connector_platform_oauth_redirect` |
| Replit                   | `https://replit.com/`                                   |
| Lovable                  | `https://lovable.app/*`                                 |
| Lovable Developer        | `https://lovable.dev/*`                                 |
| Vercel v0                | `https://api.v0.dev/v1/mcp-servers/oauth/callback`      |

## Connect an agent to AWS MCP Server

The steps to configure an OAuth-compatible agent vary depending on the
application. For instructions for supported agents, see the [AWS MCP Server Guide](../../../agent-toolkit/latest/userguide/getting-started-aws-mcp-server.md "../../../agent-toolkit/latest/userguide/getting-started-aws-mcp-server.md").

The general workflow is:

1. Configure the AWS MCP Server endpoint.
2. Authenticate through AWS Sign-In or obtain an OAuth access token
   programmatically.
3. Approve the authorization request (interactive flow only).
4. Begin invoking tools provided by AWS MCP Server.

## Authorization models

AWS MCP Server supports the authorization models provided by AWS Sign-In.

### Interactive authorization

Interactive authorization is intended for developers using agents on local
workstations.

When an agent requires authorization:

1. The agent redirects the user to AWS Sign-In.
2. The user authenticates using their AWS identity.
3. The user reviews and approves the authorization request.
4. AWS Sign-In issues OAuth access and refresh tokens.
5. The agent accesses AWS MCP Server on the user's behalf.

Required IAM permissions:

- `signin:AuthorizeOAuth2Access`
- `signin:CreateOAuth2Token`

### Non-interactive authorization

Non-interactive authorization uses the OAuth 2.0 client credentials grant. It is
intended for agents and applications that already possess AWS credentials and
cannot perform browser-based authentication.

Applications authenticate using existing AWS Signature Version 4 (SigV4)
credentials and obtain OAuth access tokens through the
`CreateOAuth2TokenWithIAM` API.

Unlike the interactive flow, only access tokens are issued. Applications request
a new access token when the current token expires.

Required IAM permission:

- `signin:CreateOAuth2Token`

The following example shows how to obtain an access token using the AWS CLI:

```
aws signin create-oauth2-token-with-iam \
    --grant-type client_credentials \
    --resource aws-mcp.amazonaws.com \
    --region us-east-1
```

## OAuth resource types

AWS Sign-In represents OAuth authorization targets and public OAuth clients as IAM
resources. You reference these resources in IAM policies to grant or control OAuth
authorization.

The following resource types are currently supported.

| Resource type                      | ARN format                                                                     | Description                                                                                                                                                                           |
| ---------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS MCP Server                     | `arn:aws:signin:`region`:`account-id`:service-principal/aws-mcp.amazonaws.com` | Represents the AWS MCP Server. Use this resource to grant or<br>control OAuth authorization for applications that access AWS MCP<br>Server.                                           |
| OAuth public client (same-device)  | `arn:aws:signin:`region`:`account-id`:oauth2/public-client/localhost`          | Represents the AWS CLI public OAuth client for same-device<br>authorization. Use this resource with `aws login`, where<br>the browser and AWS CLI run on the same device.             |
| OAuth public client (cross-device) | `arn:aws:signin:`region`:`account-id`:oauth2/public-client/remote`             | Represents the AWS CLI public OAuth client for cross-device<br>authorization. Use this resource with `aws login --remote`,<br>where authentication is completed on a separate device. |

## Token lifecycle

AWS Sign-In manages the lifecycle of OAuth tokens issued for AWS MCP Server.

| Token                        | Description                                                                                                                                                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Interactive access token     | Valid for up to one hour. Automatically refreshed while the<br>refresh token remains valid.                                                                                              |
| Non-interactive access token | Valid for the shorter of one hour or the remaining AWS session<br>duration. Applications request a new token after expiration.                                                           |
| Refresh token                | Issued only for interactive authorization. Allows applications to<br>obtain new access tokens without requiring the user to sign in<br>again. Refresh tokens are rotated and single-use. |

## Managing OAuth tokens

AWS Sign-In provides APIs for validating and managing OAuth authorizations.

| API                                                                                                                                                                    | Purpose                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| [`IntrospectOAuth2Token`](../APIReference/API_dataplane-signin_IntrospectOAuth2TokenWithIAM.md "../APIReference/API_dataplane-signin_IntrospectOAuth2TokenWithIAM.md") | Returns metadata describing an OAuth token. |
| [`RevokeOAuth2Token`](../APIReference/API_dataplane-signin_RevokeOAuth2TokenWithIAM.md "../APIReference/API_dataplane-signin_RevokeOAuth2TokenWithIAM.md")             | Revokes a refresh token.                    |

## Monitoring OAuth activity

OAuth-related activities are recorded in AWS CloudTrail.

CloudTrail records events including:

- OAuth authorization requests
- OAuth token issuance
- Token introspection
- Token revocation

CloudTrail also records the OAuth client, redirect URI, authorization flow, AWS MCP
Server resource, and associated AWS Sign-In session, allowing administrators to correlate
AWS API activity with the originating OAuth authorization.

Example CloudTrail events are available for:

- `AuthorizeOAuth2Access`
- `CreateOAuth2Token`

**Example – AuthorizeOAuth2Access
event:**

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAEXAMPLE:testuser",
        "arn": "arn:aws:sts::111111111111:assumed-role/Admin/testuser",
        "accountId": "111111111111",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAEXAMPLE",
                "arn": "arn:aws:iam::111111111111:role/Admin",
                "accountId": "111111111111",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2026-06-09T05:06:39Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2026-06-09T05:09:00Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "AuthorizeOAuth2Access",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.1",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ...",
    "requestParameters": {
        "resource": "https://aws-mcp.us-west-2.api.aws/mcp",
        "redirect_uri": "http://127.0.0.1:60432/oauth/callback",
        "code_challenge_method": "S256",
        "client_id": "arn:aws:signin:us-west-2::external-client/dcr/b3f2c8a1-9d4e-4f7a-8c6b-2e1f5a3d9b7c"
    },
    "responseElements": null,
    "additionalEventData": {
        "success": "true"
    },
    "requestID": "4fb4ff7b-6yu7-9090-78i9-9c0088a65134",
    "eventID": "bb05b222-31ec-4237-b8e7-8eb26d4fd48b",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111111111111",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "us-west-2.oauth.signin.aws"
    }
}
```

**Example – CreateOAuth2Token event:**

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAEXAMPLE:testuser",
        "arn": "arn:aws:sts::111111111111:assumed-role/Admin/testuser",
        "accountId": "111111111111",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAEXAMPLE",
                "arn": "arn:aws:iam::111111111111:role/Admin",
                "accountId": "111111111111",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2026-06-09T05:06:39Z",
                "mfaAuthenticated": "false"
            },
            "signInSessionArn": "arn:aws:signin:us-west-2:111111111111:session/daff060f-7871-4ab6-92cd-a07bbdabe61a"
        }
    },
    "eventTime": "2026-06-09T05:10:04Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "CreateOAuth2Token",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.1",
    "userAgent": "curl/8.7.1",
    "requestParameters": {
        "resource": "https://aws-mcp.us-west-2.api.aws/mcp",
        "client_id": "arn:aws:signin:us-west-2::external-client/dcr/b3f2c8a1-9d4e-4f7a-8c6b-2e1f5a3d9b7c"
    },
    "responseElements": null,
    "additionalEventData": {
        "signInSessionArn": "arn:aws:signin:us-west-2:111111111111:session/daff060f-7871-4ab6-92cd-a07bbdabe61a",
        "grant_type": "refresh_token",
        "success": "true"
    },
    "requestID": "44d6d7ce-e4r5-4cbf-0909-bfb8a8295a76",
    "eventID": "f79cc63f-b383-4e3c-a1e5-97c7db1ab833",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111111111111",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "us-west-2.oauth.signin.aws"
    }
}
```

Additional audit events and logging details for calls made using OAuth access tokens
to the AWS MCP Server can be found in the [AWS MCP Server CloudTrail logging guide](../../../agent-toolkit/latest/userguide/logging-using-cloudtrail.md "../../../agent-toolkit/latest/userguide/logging-using-cloudtrail.md").

## Troubleshooting

### Permission denied when connecting to AWS MCP Server

Verify that your IAM identity has the
`signin:AuthorizeOAuth2Access` and
`signin:CreateOAuth2Token` permissions for the AWS MCP Server
authorization grant resource.

### Access token expired

Interactive authorization automatically refreshes access tokens while the
associated refresh token remains valid. If the refresh token has expired or been
revoked, authenticate again through your agent.

For non-interactive authorization, you can request a new access token from
the token endpoint.

### Invalid target resource

When calling `CreateOAuth2TokenWithIAM`, verify that the
`resource` parameter identifies a supported target service. For AWS
MCP Server, use the AWS MCP Server service principal.

### Agent cannot register as an OAuth client

Only approved agents can register through Dynamic Client Registration (DCR). If
you are developing an MCP-compatible agent, contact AWS support.

### OAuth condition key policy is not taking effect

Verify that the condition key applies to the IAM action being evaluated. Some
condition keys are supported only by specific OAuth actions. For more information,
see [Sign-In with OAuth 2.0](oauth-sign-in-overview.md "oauth-sign-in-overview.md").

### Session revoked but the agent still has access

Revoking a refresh token immediately prevents new access tokens from being
issued. Existing access tokens remain valid until they expire (up to one
hour).

For immediate containment, apply an IAM policy using the
`aws:SignInSessionArn` global condition key to deny requests associated
with the affected sign-in session.

## Related topics

- [Sign-In with OAuth 2.0](oauth-sign-in-overview.md "oauth-sign-in-overview.md")
- [AWS Sign-In condition keys reference](reference-signin-condition-keys.md "reference-signin-condition-keys.md")
- [Connect an agent to AWS MCP Server](../../../agent-toolkit/latest/userguide/getting-started-aws-mcp-server.md "../../../agent-toolkit/latest/userguide/getting-started-aws-mcp-server.md")
