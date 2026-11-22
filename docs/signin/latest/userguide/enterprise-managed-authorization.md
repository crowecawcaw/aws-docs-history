

# Configure enterprise-managed authorization for MCP servers

## Overview
<a name="ema-overview"></a>

With enterprise-managed authorization (EMA), your enterprise's identity provider (IdP) decides which MCP servers each employee can access. Employees sign in to their agent once through the IdP. The agent then connects to every MCP server that uses AWS Sign-In without a browser sign-in or consent page for each server. EMA is the Model Context Protocol (MCP) Enterprise-Managed Authorization extension, which Okta calls Cross App Access (XAA).

AWS Sign-In implements EMA with the OAuth 2.0 JWT bearer grant (RFC 7523) and the Identity Assertion JSON Web Token (JWT) Authorization Grant (ID-JAG). The IdP issues the agent an ID-JAG for AWS Sign-In. The agent exchanges it for a short-lived AWS Sign-In access token. AWS STS validates the ID-JAG against an IAM OIDC identity provider in your account and assumes the IAM role that you choose. For the ID-JAG specification, see [Identity Assertion JWT Authorization Grant](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/) on the IETF Datatracker website.

The agent can perform only the actions that the role allows, and IAM policies, service control policies (SCPs), resource control policies (RCPs), and permission boundaries still apply.

This page uses AWS MCP Server as the example. The same setup applies to any MCP server that uses AWS Sign-In as its authorization server. For another server, use its MCP server URL and its service principal.

## How enterprise-managed authorization works
<a name="ema-how-it-works"></a>

1. The employee signs in to the agent through the enterprise's IdP.

1. The agent reads the MCP server's protected resource metadata to find its authorization server. For AWS MCP Server in US West (Oregon), the authorization server is `https://us-west-2.oauth.signin.aws`.

1. The agent exchanges the ID token or refresh token at the IdP for an ID-JAG. The IdP checks that the employee is assigned access, and sets the ID-JAG audience to the AWS Sign-In issuer and its resource to the MCP server URL.

1. The agent sends the ID-JAG to the AWS Sign-In token endpoint using the JWT bearer grant.

1. AWS STS validates the ID-JAG signature, issuer, and audience against your IAM OIDC identity provider. It then evaluates the role trust policy and assumes the role that the ID-JAG names.

1. AWS Sign-In checks that the role allows `signin:CreateOAuth2Token` and issues an access token that is valid for up to one hour.

1. The agent calls the MCP server with the access token.

AWS Sign-In does not issue a refresh token for this grant. When the access token expires, the agent requests a new ID-JAG from the IdP and exchanges it again, so the employee does not sign in again while their IdP session is active.

## Prerequisites
<a name="ema-prereqs"></a>
+ An IdP that issues ID-JAGs.
+ Administrator access to the IdP and to IAM in the AWS account whose roles employees use.
+ An agent that supports EMA. For the agents covered on this page and their minimum versions, see [Step 4: Configure your agent](#ema-step4).

## Step 1: Create an IAM OIDC identity provider
<a name="ema-step1"></a>

In the IAM console, open the **Identity providers** page and choose **Add provider** to create an OpenID Connect provider that trusts the ID-JAGs your IdP issues.

The following table lists the settings for the OIDC identity provider.


| Setting | Value | 
| --- | --- | 
| Provider type | OpenID Connect | 
| Provider URL | The issuer of the ID-JAGs. For Okta, this is your Okta org URL, for example https://example.okta.com. | 
| Audience | https://{{region}}.oauth.signin.aws. Add one audience for each Region that employees use. | 

For more information, see [Create an OpenID Connect (OIDC) identity provider in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html).

## Step 2: Create an IAM role for employees
<a name="ema-step2"></a>

Create an IAM role that employees assume through the IdP. In the IAM console, select the identity provider from Step 1 and choose **Assign role**, then choose **Web identity** as the trusted entity type. Confirm that the role trust policy looks similar to the following example.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::{{123456789012}}:oidc-provider/{{example.okta.com}}"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "{{example.okta.com}}:aud": "https://{{region}}.oauth.signin.aws"
        }
      }
    }
  ]
}
```

Replace {{example.okta.com}} with your Okta org domain and {{region}} with the Region of your MCP server.

To allow the role to obtain access tokens for AWS MCP Server, attach the [AWSMCPSignInOAuthAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMCPSignInOAuthAccessPolicy.html) AWS managed policy. For another MCP server, allow `signin:CreateOAuth2Token` on that server's service principal.

Also attach the permissions that employees need for the AWS actions they call through the MCP server. Access tokens carry the role's permissions and nothing more.

## Step 3: Configure your identity provider
<a name="ema-step3"></a>

Configure the IdP so that it issues ID-JAGs for AWS Sign-In to each agent. Every IdP needs the settings in the following table, although each IdP names them differently. For Okta field names and steps, see [Configure Okta](#ema-step3-okta).


| Setting | Value | 
| --- | --- | 
| Agent sign-in application | An OIDC application for the agent with the authorization code and refresh token grants, the agent's redirect URI, and the employees who can use the agent. | 
| Authorization server issuer | https://{{region}}.oauth.signin.aws | 
| Resource identifier | The MCP server URL, for example https://aws-mcp.{{region}}.api.aws/mcp for AWS MCP Server. | 
| Agent client ID | A client ID that you choose for the agent, for example anthropic-claude. Configure the same value in the agent in [Step 4: Configure your agent](#ema-step4). | 
| Role | The ARN of the role from Step 2. | 

### Configure Okta
<a name="ema-step3-okta"></a>

In Okta, the agent's sign-in application is the requesting app, and the AWS MCP resource app is a resource app that you create once for each Region. A resource connection on the agent links the two. For more information, see [Cross App Access](https://developer.okta.com/docs/guides/xaa-agent-to-app/main/) on the Okta Developer website.

1. Set up the agent's sign-in application. Use an OIDC application with the **Authorization Code** and **Refresh Token** grant types, and assign the employees who can use the agent. The application settings and the sign-in redirect URI depend on the agent:
   + For Kiro, follow [Create the OIDC Okta application](https://kiro.dev/docs/enterprise/identity-provider/okta/#step-1-create-oidc-application) on the Kiro website.
   + For Codex CLI, add `http://localhost:43123/callback/{{callback-id}}` as the sign-in redirect URI. To find {{callback-id}}, see [Codex CLI](#ema-step4-codex).
   + For Claude, follow the Okta setup that Claude links to from its single sign-on (SSO) setting.

1. Register the AI agent. Go to **Directory**, **AI Agents**, and choose **Register AI agent**. Under **User access**, choose **Select an existing app** and pick the agent's sign-in application. If the agent doesn't use a client secret, such as Kiro, choose **Client ID only** for **Client registration**.

1. Create the AWS MCP resource app. Create an OIDC web application, for example `AWS MCP (us-west-2)`. Okta never uses its sign-in redirect URI for this flow, so you can keep the default value. On the **Machine Assignments** tab, edit the access method and enable Cross App Access, set **Issuer URL** to the AWS Sign-In issuer for your Region, for example `https://us-west-2.oauth.signin.aws`, and set **Audience/tenant ID** to the role ARN from Step 2. Assign the same employees.

1. Connect the agent. Open the AI agent and add a resource connection. Set **Application instance** to the AWS MCP resource app, the AI agent's client ID registered in this app to the agent client ID from the table above, and **Resource identifier** to the MCP server URL.

Repeat steps 1, 2, and 4 for each agent, and repeat steps 3 and 4 for each Region. Okta records each issued ID-JAG in the System Log as `OAuth 2.0 Identity Assertion Authorization Grant is granted`.

## Step 4: Configure your agent
<a name="ema-step4"></a>

The examples use AWS MCP Server in US West (Oregon). Replace {{idp-issuer-url}} with your IdP issuer, for example `https://example.okta.com`, {{idp-client-id}} with the client ID of the agent's sign-in application at the IdP, and {{agent-client-id}} with the agent client ID from Step 3.

### Kiro
<a name="ema-step4-kiro"></a>

Requires Kiro CLI 3.5.0 or later in a V3 session, or Kiro IDE 1.4.236 or later.

In Kiro CLI, store the IdP details once, and then add each MCP server with enterprise mode.

```bash
kiro-cli mcp idp setup --issuer {{idp-issuer-url}} --client-id {{idp-client-id}}

kiro-cli mcp add --name aws-mcp --url https://aws-mcp.us-west-2.api.aws/mcp --scope global \
    --oauth-mode enterprise --oauth-client-id {{agent-client-id}}
```

Kiro IDE and Kiro CLI read the same user-level `~/.kiro/settings/mcp.json` file, so you can make the same change there instead.

```json
{
  "identityProvider": {
    "issuer": "{{idp-issuer-url}}",
    "clientId": "{{idp-client-id}}"
  },
  "mcpServers": {
    "aws-mcp": {
      "url": "https://aws-mcp.us-west-2.api.aws/mcp",
      "oauth": {
        "mode": "enterprise",
        "clientId": "{{agent-client-id}}"
      }
    }
  }
}
```

To sign in from Kiro CLI, type `/mcp` on its own, not `/mcp list`, which prints a table that you can't navigate. The first row is the organization sign-in, which shows as not signed in, and each server that uses it says that it needs organization sign-in. Select the first row and press Enter, then finish signing in through your browser. In Kiro IDE, choose **Sign in** on the Organization sign-in row. For more information, see [MCP configuration](https://kiro.dev/docs/mcp/configuration/) on the Kiro website.

### Codex CLI
<a name="ema-step4-codex"></a>

Requires Codex CLI 0.156.0 or later.

Add the following to `~/.codex/config.toml`. Codex reads these settings only from that file, not from project configuration. Keep the two callback settings above the first table header.

```toml
mcp_oauth_callback_url = "http://localhost:43123/callback"
mcp_oauth_callback_port = 43123

[features]
use_xaa = true

[mcp_enterprise_managed_auth.idp]
issuer = "{{idp-issuer-url}}"
client_id = "{{idp-client-id}}"

[mcp_servers.aws-mcp]
url = "https://aws-mcp.us-west-2.api.aws/mcp"
auth = "ema_auth"

[mcp_servers.aws-mcp.oauth]
client_id = "{{agent-client-id}}"
```

Codex adds an identifier to the end of the callback URL, so the redirect URI to register has the form `http://localhost:43123/callback/{{callback-id}}`. To find it, start Codex and run `/mcp login aws-mcp`. When Okta rejects the redirect URI, copy the `redirect_uri` value from the address bar of the browser, register it on the Codex sign-in application, and sign in again. The identifier depends only on the IdP issuer, so one registered URI works for every employee.

### Claude
<a name="ema-step4-claude"></a>

An administrator of your Claude organization adds the MCP server as a custom connector. The OAuth client that you choose for the connector decides how members sign in. The following table describes the sign-in modes.


| Mode | OAuth client | Managed authorization | 
| --- | --- | --- | 
| EMA only | Use your own OAuth client with the agent client ID from Step 3 | Set up for all roles | 
| Split mode, for EMA-testing purposes | Use your own OAuth client with a client ID that you register in each Region | Set up for a test role. Other members sign in through the browser. | 

Browser sign-in requires a client registered with AWS Sign-In. EMA accepts any client ID. That is why split mode needs a registered client, and EMA only does not. To register a client for split mode, call the [CreateOAuth2PublicClient](https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_CreateOAuth2PublicClient.html) API in each Region with the Claude redirect URI. Use the returned client ID in the connector and in that Region's resource connection in the IdP.

1. In Claude, open **Admin settings**, **Connectors**, and choose **Add**, **Custom connector**. Enter a name and the MCP server URL, for example `https://aws-mcp.us-west-2.api.aws/mcp`.

1. For **Authentication**, choose **Sign in when needed**. For **OAuth client**, choose **Use your own OAuth client**, enter the client ID for your mode, and leave the client secret blank.

1. Open the connector, and on the **Configuration** tab choose **Set up** next to **Managed authorization**. Choose **IdP-managed** as the identity source, complete [Step 3: Configure your identity provider](#ema-step3) if you haven't already, and confirm that the connection checks pass.

1. Choose the roles that connect through managed authorization, and then choose **Save**.

**Note**  
If the connector doesn't have a **Managed authorization** setting, add the connector again with an AWS MCP Server endpoint in a Region other than US East (N. Virginia) (`us-east-1`) or Europe (Frankfurt) (`eu-central-1`), for example `https://aws-mcp.us-west-2.api.aws/mcp`.

Use the same client ID in the IdP's resource connection for Claude. For more information, see [Auto-connect your organization's apps to Claude](https://support.claude.com/en/articles/15537633-authorize-mcp-connectors-for-your-entire-organization) on the Claude Help Center website.

## Monitoring enterprise-managed authorization
<a name="ema-monitoring"></a>

AWS CloudTrail records each token request as a `CreateOAuth2Token` event, as in the following example.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROA1234567890EXAMPLE:IDAAG.nM5xzagNal2jb_tdJucKeDBJHAU6XtsjXoSpIzOqvoE",
        "arn": "arn:aws:sts::123456789012:assumed-role/OktaXAA/IDAAG.nM5xzagNal2jb_tdJucKeDBJHAU6XtsjXoSpIzOqvoE",
        "accountId": "123456789012",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROA1234567890EXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/OktaXAA",
                "accountId": "123456789012",
                "userName": "OktaXAA"
            },
            "webIdFederationData": {
                "federatedProvider": "arn:aws:iam::123456789012:oidc-provider/example.okta.com",
                "attributes": {}
            },
            "attributes": {
                "creationDate": "2026-11-12T00:10:30Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2026-11-12T00:10:31Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "CreateOAuth2Token",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "10.0.0.25",
    "userAgent": "python-httpx/0.28.1",
    "requestParameters": {
        "resource": "https://aws-mcp.us-west-2.api.aws/mcp",
        "client_id": "arn:aws:signin:::external-client/jwt-bearer/anthropic-claude"
    },
    "responseElements": null,
    "additionalEventData": {
        "signInSessionArn": "arn:aws:signin:us-west-2:123456789012:session/318c7829-2be1-4c7d-b693-538685cc1d49",
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "success": "true"
    },
    "requestID": "0a475993-9f25-4198-9ed6-a8a141a05e99",
    "eventID": "21a99293-1659-49de-ad69-143c81c3e7a6",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "us-west-2.oauth.signin.aws"
    }
}
```
+ `userIdentity` – The role session that AWS STS created. `webIdFederationData` names your OIDC identity provider.
+ `client_id` – The agent client ID, recorded as `arn:aws:signin:::external-client/jwt-bearer/{{agent-client-id}}`.
+ `grant_type` – `urn:ietf:params:oauth:grant-type:jwt-bearer` for every EMA token request.
+ `signInSessionArn` – The same value appears on the calls that the agent makes through the MCP server, so you can link them to this request.

## Troubleshooting enterprise-managed authorization
<a name="ema-troubleshooting"></a>

The following table lists common problems and how to fix them.


| Problem | Solution | 
| --- | --- | 
| Employees can't sign in to the IdP | Verify the following:+  The redirect URI on the agent's sign-in application exactly matches the one the agent sends, including the host and path. <br />+  The employee is assigned to the agent's sign-in application. <br />+  The agent authenticates to the sign-in application the way the application expects.  | 
| Employees sign in, but the agent can't connect to the MCP server | Verify the following:+  The resource app's issuer is `https://{{region}}.oauth.signin.aws`. <br />+  The resource connection's resource identifier is the MCP server URL. <br />+  The agent and the IdP use the same agent client ID. <br />+  The OIDC identity provider has the Region's audience.  | 
| The agent asks employees to sign in again every hour | The agent's sign-in application does not issue refresh tokens. Turn on the refresh token grant, and have employees sign in again. | 

## Related topics
<a name="ema-related"></a>
+ [Sign-In with OAuth 2.0](oauth-sign-in-overview.md)
+ [AWS MCP Server](aws-mcp-server.md)
+ [OAuth condition keys](reference-signin-condition-keys.md#reference-signin-condition-keys-oauth)