# Setting up Amazon Quick on desktop for enterprise deployments

|                                                                 |
| --------------------------------------------------------------- |
| \*_Applies<br>to:_<br>• Enterprise Edition and Standard Edition |

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

To use Amazon Quick on desktop for enterprise deployments, administrators must
configure enterprise single sign-on (SSO) so that users in the organization can sign in
with their corporate credentials. This setup connects your organization's OpenID Connect
(OIDC) compatible identity provider (IdP) to Amazon Quick.

###### Note

If you are using a Free or Plus account, this section does not apply to you.
Continue to [Getting started](getting-started-desktop.md "getting-started-desktop.md").

The setup involves the following steps, in order:

1. Create an OIDC application in your IdP.
2. Create a Trusted Token Issuer (TTI) in IAM Identity Center (only
   required for accounts that use IAM Identity Center for
   authentication).
3. Configure the extension access in the Amazon Quick management console.
4. Distribute the desktop application to your users.
   This guide provides IdP-specific instructions for Microsoft Entra ID, Okta, PingOne,
   and Google Workspace. See instructions for your specific identity provider below.

## How enterprise sign-in works

The Amazon Quick desktop application uses the OIDC protocol to authenticate users.
When a user chooses **Enterprise login**, the application
opens a browser window and redirects to your IdP's authorization endpoint. The
application then exchanges the resulting authorization code for tokens using Proof Key
for Code Exchange (PKCE).

Amazon Quick validates the token and maps the user to an identity in your account.
For accounts that use IAM Identity Center, the TTI maps the
`email` claim in the OIDC token to the `emails.value` attribute
in the identity store. For accounts that use IAM federation, Amazon Quick maps the
user by email directly. In both cases, the email address in your IdP must exactly
match the email address of the user in Amazon Quick.

## Prerequisites

Before you begin, verify that you have the following:

- An AWS account with an active Amazon Quick subscription that uses
  IAM Identity Center or IAM federation for authentication. The
  Amazon Quick account's home region (identity region) must be US East
  (N. Virginia) (us-east-1).
- Administrator access to your Amazon Quick account.
- Access to your IdP with permissions to create OIDC application
  registrations.

###### Important

The Amazon Quick account's home region (identity region) must be US East
(N. Virginia) (us-east-1). All inference for the desktop application also
uses this Region. While Amazon Quick on the web can be used in other Regions,
the desktop application connects to us-east-1 for both authentication and
inference.

## Step 1: Create an OIDC application in your identity provider

Register a public OIDC client application in your IdP. The Amazon Quick desktop
application uses this client to authenticate users through the authorization code flow
with PKCE. No client secret is required.

The desktop application requires refresh tokens to maintain long-lived sessions.
How refresh tokens are configured depends on your IdP:

- **Microsoft Entra ID** – The
  `offline_access` scope must be granted. Without it, users must
  re-authenticate frequently.
- **Okta** – The Refresh Token grant
  type must be enabled on the application, and the
  `offline_access` scope must be granted.
- **PingOne** – The Refresh Token grant
  type must be enabled. The `offline_access` scope is optional
  but recommended.
- **Google Workspace** – Refresh tokens
  are returned automatically for desktop applications. No additional
  configuration is required.

Choose the instructions for your identity provider.

### Microsoft Entra ID

###### To create the Entra ID app registration

1. In the Azure portal, navigate to **Microsoft Entra
   ID → App registrations → New registration**.
2. Configure the following settings:

| Setting                 | Value                                                             |
| ----------------------- | ----------------------------------------------------------------- |
| Name                    | `Amazon Quick Desktop`                                            |
| Supported account types | Accounts in this organizational directory only<br>(Single tenant) |
| Redirect URI platform   | Public client/native (mobile & desktop)                           |
| Redirect URI            | `http://localhost:18080`                                          |

3. Choose **Register**.
4. On the **Overview** page, note the
   **Application (client) ID** and
   **Directory (tenant) ID**. You need these
   values in later steps.

This is a public client registration. PKCE
is enforced automatically by Entra ID for public clients.

###### To configure API permissions

1. In the app registration, navigate to **API
   permissions → Add a permission → Microsoft Graph →
   Delegated permissions**.
2. Add the following permissions: `openid`,
   `email`, `profile`,
   `offline_access`.
3. Choose **Add permissions**.
4. If your organization requires it, choose **Grant
   admin consent for [your organization]**.

###### To configure authentication settings

1. In the app registration, navigate to **Authentication**.
2. Under **Advanced settings**, set
   **Allow public client flows** to
   **Yes**.
3. Verify that `http://localhost:18080` is listed under
   **Mobile and desktop applications**.
4. Choose **Save**.

Your OIDC endpoints use the following format. Replace
`<TENANT_ID>` with your Directory (tenant) ID.

| Field                  | Value                                                                 |
| ---------------------- | --------------------------------------------------------------------- |
| Issuer URL             | `https://login.microsoftonline.com/<TENANT_ID>/v2.0`                  |
| Authorization endpoint | `https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/authorize` |
| Token endpoint         | `https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/token`     |
| JWKS URI               | `https://login.microsoftonline.com/<TENANT_ID>/discovery/v2.0/keys`   |

### Okta

###### To create the Okta OIDC Native Application

1. In the Okta Admin Console, navigate to **Applications → Applications → Create App
   Integration**.
2. Select **OIDC - OpenID Connect** as the
   sign-in method.
3. Select **Native Application** as the
   application type, then choose **Next**.
4. Configure the following settings:

| Setting               | Value                                     |
| --------------------- | ----------------------------------------- |
| App integration name  | `Amazon Quick Desktop`                    |
| Grant type            | Authorization Code and Refresh Token      |
| Sign-in redirect URIs | `http://localhost:18080`                  |
| Assignments           | Assign to the appropriate users or groups |

5. Choose **Save**.
6. On the **General** tab, note the
   **Client ID**.

PKCE (S256) is enforced automatically by Okta for native
applications.

###### To configure scopes

1. In the app integration, go to the **Okta API
   Scopes** tab.
2. Grant the following scopes: `openid`, `email`,
   `profile`, `offline_access`.

###### Note

If you are using a custom authorization server, verify that these scopes
are also enabled under **Security → API →
Authorization Servers → default → Scopes**.

###### To verify authentication settings

1. In the app integration, go to the **General** tab.
2. Under **General Settings**, confirm that
   the application type is **Native**, client
   authentication is **None** (public client),
   and PKCE is **Required**.
3. Under **LOGIN**, confirm that
   `http://localhost:18080` is listed as a redirect URI.
4. Choose **Save** if you made any
   changes.

Your OIDC endpoints use the following format. Replace
`<OKTA_DOMAIN>` with your Okta domain (for example,
`your-org.okta.com`).

| Field                  | Value                                               |
| ---------------------- | --------------------------------------------------- |
| Issuer URL             | `https://<OKTA_DOMAIN>/oauth2/default`              |
| Authorization endpoint | `https://<OKTA_DOMAIN>/oauth2/default/v1/authorize` |
| Token endpoint         | `https://<OKTA_DOMAIN>/oauth2/default/v1/token`     |
| JWKS URI               | `https://<OKTA_DOMAIN>/oauth2/default/v1/keys`      |

### PingOne

###### To create the PingOne OIDC Native Application

1. In the PingOne Admin Console, navigate to **Applications → Applications → +** (Add
   Application).
2. Enter `Amazon Quick Desktop` as the application
   name.
3. Select **OIDC Native App** as the
   application type, then choose **Save**.
4. On the **Configuration** tab, choose
   **Edit** and configure the following
   settings:

| Setting                              | Value                                |
| ------------------------------------ | ------------------------------------ |
| Response Type                        | Code                                 |
| Grant Types                          | Authorization Code and Refresh Token |
| PKCE Enforcement                     | S256                                 |
| Redirect URIs                        | `http://localhost:18080`             |
| Token Endpoint Authentication Method | None                                 |

5. Choose **Save**.
6. On the **Resources** tab, add the
   following scopes: `openid`, `email`,
   `profile`.
7. Toggle the application to **Enabled**.
8. Note the **Client ID** and
   **Environment ID** from the
   **Configuration** tab.

###### To verify authentication settings

1. In the PingOne Admin Console, navigate to **Applications → Applications** and select the Amazon Quick
   Desktop application.
2. On the **Configuration** tab,
   confirm that the Response Type is **Code**, Grant Types include **Authorization Code** and **Refresh
   Token**, PKCE Enforcement is **S256**, and Token Endpoint Authentication Method is
   **None**.
3. Confirm that `http://localhost:18080` is listed as a
   redirect URI.
4. Confirm that the application toggle is set to **Enabled**.

Your OIDC endpoints use the following format. Replace
`<ENV_ID>` with your PingOne environment ID.

###### Note

The PingOne domain varies by region. The examples below use
`.com`. Replace the domain with the one for your environment
(for example, `.ca`, `.eu`, or
`.asia`).

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| Issuer URL             | `https://auth.pingone.com/<ENV_ID>/as`           |
| Authorization endpoint | `https://auth.pingone.com/<ENV_ID>/as/authorize` |
| Token endpoint         | `https://auth.pingone.com/<ENV_ID>/as/token`     |
| JWKS URI               | `https://auth.pingone.com/<ENV_ID>/as/jwks`      |

### Google Workspace

###### To create the Google OAuth 2.0 Desktop client

1. In the Google Cloud Console, navigate to **APIs
   & Services → Credentials → Create credentials →
   OAuth client ID**.
2. Select **Desktop app** as the application
   type.
3. Set the name to `Amazon Quick Desktop`.
4. Choose **Create**.
5. Note the **Client ID** from the
   confirmation dialog.

###### Note

Google issues a client secret for desktop apps, but it is not treated as
confidential for installed applications. The desktop app uses the
authorization code flow with PKCE — the client secret is optional in
the token exchange.

###### To configure the OAuth consent screen

1. In the Google Cloud Console, navigate to **APIs
   & Services → OAuth consent screen**.
2. Select **Internal** as the user type.
   This restricts authentication to users within your Google Workspace
   organization.
3. Configure the following settings:

| Setting            | Value                       |
| ------------------ | --------------------------- |
| App name           | `Amazon Quick Desktop`      |
| User support email | Your admin or support email |
| Authorized domains | Your organization's domain  |

4. Under **Scopes**, add the following:
   `openid`, `email`,
   `profile`.
5. Choose **Save and Continue**.

###### To verify authentication settings

1. Navigate to **APIs & Services →
   Credentials**.
2. Select the **Amazon Quick Desktop**
   OAuth client.
3. Confirm that the application type is **Desktop
   app** and that the Client ID is present.
4. Under **Authorized redirect URIs**,
   confirm that `http://localhost:18080` is listed. If it is
   missing, add it manually.

The OIDC endpoints are the same for all Google Workspace tenants:

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| Issuer URL             | `https://accounts.google.com`                                  |
| Authorization endpoint | `https://accounts.google.com/o/oauth2/v2/auth`                 |
| Token endpoint         | `https://oauth2.googleapis.com/token`                          |
| JWKS URI               | `https://www.googleapis.com/oauth2/v3/certs`                   |
| Discovery document     | `https://accounts.google.com/.well-known/openid-configuration` |

## Step 2: Create a Trusted Token Issuer in IAM Identity Center

###### Note

This step is only required if your Amazon Quick account uses AWS Identity and Access Management
Identity Center for authentication. If your account uses IAM federation,
skip this step and proceed to Step 3.

The TTI tells IAM Identity Center to trust tokens from your IdP and how to
map them to IAM Identity Center users. You can create the TTI in the AWS Identity and Access Management
Identity Center console or with the AWS CLI.

To create the TTI with the AWS CLI, run the following command. Replace
`<IDC_INSTANCE_ARN>` with your IAM Identity Center instance
Amazon Resource Name (ARN) and `<ISSUER_URL>` with the issuer URL
from Step 1.

```
aws sso-admin create-trusted-token-issuer \
  --instance-arn <IDC_INSTANCE_ARN> \
  --name "AmazonQuickDesktop" \
  --trusted-token-issuer-type OIDC_JWT \
  --trusted-token-issuer-configuration '{
    "OidcJwtConfiguration": {
      "IssuerUrl": "<ISSUER_URL>",
      "ClaimAttributePath": "email",
      "IdentityStoreAttributePath": "emails.value",
      "JwksRetrievalOption": "OPEN_ID_DISCOVERY"
    }
  }'
```

Note the `TrustedTokenIssuerArn` from the output. You need it in the
next step.

The following table lists the issuer URL for each identity provider.

| Identity provider  | Issuer URL                                           |
| ------------------ | ---------------------------------------------------- |
| Microsoft Entra ID | `https://login.microsoftonline.com/<TENANT_ID>/v2.0` |
| Okta               | `https://<OKTA_DOMAIN>/oauth2/default`               |
| PingOne            | `https://auth.pingone.com/<ENV_ID>/as`               |
| Google Workspace   | `https://accounts.google.com`                        |

## Step 3: Configure the extension access in the Amazon Quick management console

###### To add the extension access

1. Sign in to the Amazon Quick management console.
2. Under **Permissions**, choose
   **Extension access**.
3. Choose **Add extension access**.
4. (Optional) If your account uses IAM Identity Center, the
   **Trusted Token Issuer Setup** step appears.
   Enter the following:

| Field                    | Value                                      |
| ------------------------ | ------------------------------------------ |
| Trusted Token Issuer ARN | The `TrustedTokenIssuerArn` from<br>Step 2 |
| Aud claim                | The Client ID from Step 1                  |

This step does not appear for accounts that use IAM federation. 5. Select the **Desktop application for
Quick** extension and choose **Next**. 6. Enter the Amazon Quick extension details:

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| Name                   | A name for this extension access                   |
| Description            | (Optional) A description                           |
| Issuer URL             | The OIDC issuer URL from Step 1                    |
| Authorization Endpoint | The OIDC authorization endpoint URL from<br>Step 1 |
| Token Endpoint         | The OIDC token endpoint URL from Step 1            |
| JWKS URI               | The JSON Web Key Set URI from Step 1               |
| Client ID              | The OIDC client identifier from Step 1             |

7. Choose **Add**.

###### To create the extension

1. In the Amazon Quick console, in the left navigation under
   **Connect apps and data**, choose
   **Extensions**.
2. Choose **Add extension**.
3. Select the **Desktop application for
   Quick** extension access you previously created. Choose
   **Next**.
4. Choose **Create**.

## Step 4: Download and distribute the desktop application

After you configure enterprise sign-in, verify the setup by downloading and
installing the desktop application yourself. Choose **Enterprise
login** on the sign-in screen and authenticate with your corporate
credentials to confirm the configuration is working. For download and installation
steps, see [Getting started](getting-started-desktop.md "getting-started-desktop.md").

After you verify the setup, direct your users to [Getting started](getting-started-desktop.md "getting-started-desktop.md") for
download, installation, and sign-in instructions.

## Troubleshooting

`redirect_mismatch` error

Verify that the redirect URI in your IdP is exactly
`http://localhost:18080` and is configured as a public
client or native platform.

User not found after sign-in

The email in the IdP token must exactly match the email of a user in
IAM Identity Center. Verify that the user is provisioned and that
the email addresses are identical in both systems.

Token validation failure

Verify that the issuer URL in the TTI matches the issuer URL in your
IdP's OIDC configuration exactly.

Consent or permission errors (Microsoft Entra ID)

Grant admin consent for the required API permissions in the Azure
portal. Navigate to the app registration's **API
permissions** page and choose **Grant admin
consent for [your organization]**.

Session expires frequently

Verify that your IdP is configured to issue refresh tokens. For
Microsoft Entra ID, the `offline_access` scope is required.
For Okta, the Refresh Token grant type must be enabled and the
`offline_access` scope must be granted. For PingOne, the
Refresh Token grant type must be enabled.

`invalid_scope` error (Okta)

Verify that `offline_access` is granted in the
**Okta API Scopes** tab. If you are using
a custom authorization server, verify that the scope is enabled under
**Security → API → Authorization Servers
→ default → Scopes**.

Application not enabled (PingOne)

If authentication fails immediately without reaching the PingOne login
page, verify that the application toggle is set to **Enabled** in the PingOne Admin Console.

`access_denied` error (Google Workspace)

This typically means the OAuth consent screen is set to
**Internal** and the user is not a member
of your Google Workspace organization. Verify that the user's Google
account belongs to your organization's domain.
