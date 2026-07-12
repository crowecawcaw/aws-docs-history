# Sign-In with OAuth 2.0

## OAuth overview

With AWS Sign-In industry-standard OAuth 2.0 support, agents and applications can
access supported AWS services using OAuth authorization.

OAuth integrates with your existing AWS identities and authorization model.
Applications obtain short-lived OAuth tokens through AWS Sign-In. OAuth tokens work
with your existing IAM identities, policies, service control policies (SCPs),
resource control policies (RCPs), and other AWS authorization controls. OAuth
introduces a standards-based authorization model without changing how access to AWS
resources is governed.

With AWS Sign-In, you can authorize applications through a browser (interactive),
or applications with existing AWS credentials can obtain OAuth access tokens
programmatically (non-interactive).

## Supported capabilities

AWS Sign-In provides the following OAuth capabilities.

| Capability                                                                                                                                                         | Description                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| [Interactive authorization](#oauth-sign-in-interactive "#oauth-sign-in-interactive")                                                                               | Browser-based OAuth authorization for users.                                                                   |
| [Non-interactive authorization](#oauth-sign-in-non-interactive "#oauth-sign-in-non-interactive")                                                                   | OAuth authorization for agents and applications using existing<br>AWS credentials without requiring a browser. |
| [Token management](aws-mcp-server.md#aws-mcp-server-token-management "aws-mcp-server.md#aws-mcp-server-token-management")                                          | Issue and introspect access and refresh tokens, and<br>revoke refresh tokens.                                  |
| [Dynamic client registration](../APIReference/API_dataplane-signin_CreateOAuth2PublicClient.md "../APIReference/API_dataplane-signin_CreateOAuth2PublicClient.md") | Register approved OAuth-compatible applications with<br>AWS Sign-In.                                           |
| [IAM integration](../../../service-authorization/latest/reference/list_signin.md "../../../service-authorization/latest/reference/list_signin.md")                 | Govern OAuth authorization using IAM permissions, resources,<br>and condition keys.                            |
| [CloudTrail integration](aws-mcp-server.md#aws-mcp-server-monitoring "aws-mcp-server.md#aws-mcp-server-monitoring")                                                | Audit OAuth authorization and token lifecycle events using<br>AWS CloudTrail.                                  |

## How OAuth works

OAuth authorization in AWS Sign-In follows the OAuth 2.0 standard.

1. An agent or application requests authorization to access a supported AWS
   service.
2. AWS Sign-In authenticates the user.
3. AWS Sign-In issues OAuth tokens that authorize the application to access the
   requested AWS service on behalf of the user.
4. The AWS service evaluates every request using the existing AWS
   authorization model, including IAM policies, service control policies (SCPs),
   resource control policies (RCPs), permission boundaries, and other applicable
   controls.

OAuth tokens authorize an application to access a supported AWS service. They do
not grant additional AWS permissions. Applications can perform only the actions
already permitted by the authenticated IAM identity.

## Authorization models

AWS Sign-In supports two OAuth authorization models.

### Interactive authorization

Interactive authorization is intended for developers using browser-based
authentication.

AWS Sign-In enforces the OAuth 2.1 Authorization Code Grant with Proof Key for
Code Exchange (PKCE). When an application requires authorization, it redirects the
user to AWS Sign-In, where the user authenticates, reviews the authorization request,
and grants consent.

After successful authorization, AWS Sign-In issues:

- **Access tokens** – Short-lived OAuth
  tokens (up to one hour) that authorize applications to access supported
  AWS services.
- **Refresh tokens** – Used to obtain
  new access tokens without requiring the user to authenticate again.
  AWS Sign-In automatically manages token refresh for authorized
  applications.

Interactive authorization supports:

- IAM users
- AWS account root users
- IAM Identity Center users
- SAML and Custom Identity broker users

For a walkthrough of connecting an agent using interactive authorization, see
[AWS MCP Server](aws-mcp-server.md "aws-mcp-server.md").

### Non-interactive authorization

Non-interactive authorization is intended for agents and applications that
already possess AWS credentials and cannot perform browser-based
authentication.

AWS Sign-In implements the OAuth 2.0 Client Credentials Grant using AWS
Signature Version 4 (SigV4) credentials instead of a static OAuth client secret.
Applications authenticate to the AWS Sign-In token endpoint using existing AWS
credentials and receive a short-lived OAuth access token that can be used to access
supported AWS services.

The client credentials grant issues only access tokens (no refresh tokens).
Request a new access token when the current token expires.

For a walkthrough of connecting an application using non-interactive
authorization, see [AWS MCP Server](aws-mcp-server.md "aws-mcp-server.md").

## Security model

OAuth authorization integrates with the existing AWS security model.
AWS Sign-In extends this authorization model with OAuth-specific capabilities,
including:

- IAM actions for OAuth authorization and token management. See [Actions,
  resources, and condition keys for AWS Sign-In](../../../service-authorization/latest/reference/list_signin.md "../../../service-authorization/latest/reference/list_signin.md").
- OAuth authorization grant resources. See [Actions,
  resources, and condition keys for AWS Sign-In](../../../service-authorization/latest/reference/list_signin.md "../../../service-authorization/latest/reference/list_signin.md").
- OAuth-specific IAM condition keys. See [OAuth condition keys](reference-signin-condition-keys.md#reference-signin-condition-keys-oauth "reference-signin-condition-keys.md#reference-signin-condition-keys-oauth").
- Token [introspection](../APIReference/API_dataplane-signin_IntrospectOAuth2TokenWithIAM.md "../APIReference/API_dataplane-signin_IntrospectOAuth2TokenWithIAM.md") and [revocation](../APIReference/API_dataplane-signin_RevokeOAuth2TokenWithIAM.md "../APIReference/API_dataplane-signin_RevokeOAuth2TokenWithIAM.md") APIs.
- AWS CloudTrail auditing for OAuth authorization and token lifecycle
  events. See [Monitoring OAuth activity](aws-mcp-server.md#aws-mcp-server-monitoring "aws-mcp-server.md#aws-mcp-server-monitoring").
- Required PKCE (Proof Key for Code Exchange) with OAuth 2.1 for interactive
  authorization flows.
- Single-use authorization codes and rotating single-use refresh tokens to
  prevent replay attacks.
- VPCE support for OAuth APIs. See [AWS PrivateLink](oauth-privatelink.md "oauth-privatelink.md").
- Support trusted redirect URIs in DCR.

These capabilities allow administrators to govern OAuth authorization using the same
IAM authorization model they already use across AWS.

## OAuth endpoints

AWS Sign-In provides the following OAuth endpoints.

| Endpoint                    | Path             | Description                                                                                        |
| --------------------------- | ---------------- | -------------------------------------------------------------------------------------------------- |
| Authorization               | `/v1/authorize`  | Initiates the interactive authorization flow.                                                      |
| Token                       | `/v1/token`      | Exchanges authorization codes, refresh tokens, or client<br>credentials for OAuth tokens.          |
| Introspection               | `/v1/introspect` | Returns metadata about an OAuth token.                                                             |
| Revocation                  | `/v1/revoke`     | Revokes a refresh token.                                                                           |
| Dynamic Client Registration | `/v1/register`   | Registers approved OAuth clients with AWS Sign-In. Only<br>allowlisted redirect URIs are accepted. |

Use this regional endpoint for the OAuth flow at
`https://{region}.oauth.signin.aws`. For a list of possible region values,
see the Region column in [AWS Sign-In
endpoints](../../../general/latest/gr/signin-service.md "../../../general/latest/gr/signin-service.md").

## Related topics

- [AWS MCP Server](aws-mcp-server.md "aws-mcp-server.md")
- [OAuth condition keys](reference-signin-condition-keys.md#reference-signin-condition-keys-oauth "reference-signin-condition-keys.md#reference-signin-condition-keys-oauth")
- [AWS Sign-In API
  Reference](../APIReference/API_Operations.md "../APIReference/API_Operations.md")
- [Actions,
  resources, and condition keys for AWS Sign-In](../../../service-authorization/latest/reference/list_signin.md "../../../service-authorization/latest/reference/list_signin.md")
