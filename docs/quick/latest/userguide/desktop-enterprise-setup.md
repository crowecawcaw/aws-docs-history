# Setting up Amazon Quick on desktop for enterprise deployments

|                                           |
| ----------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition |

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
2. Configure the extension access in the Amazon Quick management console.
3. Distribute the desktop application to your users.
   This guide provides IdP-specific instructions for Microsoft Entra ID, Google
   Workspace, Okta, and Ping Identity (PingFederate and PingOne). See instructions for
   your specific identity provider below.

## How enterprise sign-in works

The Amazon Quick desktop application uses the OIDC protocol to authenticate users.
When a user chooses **Continue with SSO**, the application
opens a browser window and redirects to your IdP's authorization endpoint. The
application then exchanges the resulting authorization code for tokens using Proof Key
for Code Exchange (PKCE).

Amazon Quick validates the token and maps the user to an identity in your account.
The email address in your IdP must exactly match the email address of the user
in Amazon Quick.

## Prerequisites

Before you begin, verify that you have the following:

- An AWS account with an active Amazon Quick subscription. The
  Amazon Quick account's home region (identity region) must be in a
  supported AWS Region. For a list of supported Regions, see
  [Supported AWS Regions for Amazon Quick](regions.md#regions-qs "regions.md#regions-qs"). All identity
  types are supported, including IAM Identity Center, IAM federation, and native Amazon Quick
  (username/password) users.
- Administrator access to your Amazon Quick account.
- Access to your IdP with permissions to create OIDC application
  registrations.

###### Important

Amazon Quick on desktop is available for Enterprise accounts in
AWS Regions that support the full Amazon Quick feature set. Regions
that support Amazon Quick Sight capabilities only do not include desktop. For
the full list, see [Supported AWS Regions for Amazon Quick](regions.md#regions-qs "regions.md#regions-qs").

## Step 1: Create an OIDC application in your identity provider

Register a public OIDC client application in your IdP. The Amazon Quick desktop
application uses this client to authenticate users through the authorization code flow
with PKCE. No client secret is required.

The desktop application requires refresh tokens to maintain long-lived sessions.
How refresh tokens are configured depends on your IdP:

- **Microsoft Entra ID** – The
  `offline_access` scope must be granted. Without it, users must
  re-authenticate frequently.
- **Google Workspace** – Include the
  `access_type=offline` parameter in the authorization request.
  Google issues a refresh token on the first authorization. No additional
  scope or grant type configuration is required.
- **Okta** – The Refresh Token grant
  type must be enabled on the application, and the
  `offline_access` scope must be granted.
- **Ping Identity** – The Refresh Token
  grant type must be enabled, and the `offline_access` scope must
  be granted. For PingFederate, the **Return ID Token On
  Refresh Grant** setting must also be enabled in the OIDC
  policy.

Choose the instructions for your identity provider.

### Microsoft Entra ID

For detailed instructions, see [Register an application](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app "https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app") in the Microsoft Entra
documentation.

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

###### To configure token claims

1. In the app registration, navigate to **Token configuration**.
2. Choose **Add optional claim**.
3. Select token type: **ID**.
4. Select the `email` claim and choose
   **Add**.

###### Important

This step is required. Without the `email` optional claim,
Microsoft Entra ID does not include the user's email address in the ID
token, and Amazon Quick cannot map the token to a user. Additionally,
each user who signs in must have their **Mail** attribute populated in their Entra ID profile (under
**Contact Information**). The User Principal
Name (UPN) alone is not sufficient — the Mail attribute must contain
a value.

Your OIDC endpoints use the following format. Replace
`<TENANT_ID>` with your Directory (tenant) ID.

###### Important

The Issuer URL must include the `/v2.0` path suffix. Do not
use the "Authority URL" shown in the Entra ID Endpoints panel, which omits
this suffix. If the `/v2.0` suffix is missing, token validation
fails with an "Invalid issuer" error at sign-in time.

| Field                  | Value                                                                 |
| ---------------------- | --------------------------------------------------------------------- |
| Issuer URL             | `https://login.microsoftonline.com/<TENANT_ID>/v2.0`                  |
| Authorization endpoint | `https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/authorize` |
| Token endpoint         | `https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/token`     |
| JWKS URI               | `https://login.microsoftonline.com/<TENANT_ID>/discovery/v2.0/keys`   |

###### Tip

The JWKS URI is not displayed in the Microsoft Entra ID
**Endpoints** panel. You can find it by
opening the **OpenID Connect metadata
document** URL from the Endpoints panel and locating the
`jwks_uri` field in the JSON response. Alternatively,
construct it using the format shown in the preceding table.

### Google Workspace

For detailed instructions, see [OAuth 2.0 for Mobile & Desktop Apps](https://developers.google.com/identity/protocols/oauth2/native-app "https://developers.google.com/identity/protocols/oauth2/native-app") in the Google for
Developers documentation.

###### To create the Google OAuth client

1. In the Google Cloud Console, navigate to **APIs & Services → Credentials → Create
   Credentials → OAuth client ID**.
2. Configure the following settings:

| Setting          | Value                  |
| ---------------- | ---------------------- |
| Application type | Desktop app            |
| Name             | `Amazon Quick Desktop` |

3. Choose **Create**.
4. Note the **Client ID** and
   **Client secret**. You need these
   values in later steps.

###### To configure the OAuth consent screen

1. In the Google Cloud Console, navigate to **Google Auth Platform → Branding**.
2. Set the **User type** to **Internal**. This restricts sign-in to users
   in your Google Workspace organization.
3. Fill in the required app information and choose **Save**.

###### To configure scopes

1. In the Google Cloud Console, navigate to **Google Auth Platform → Data Access**.
2. Add the following scopes: `openid`,
   `email`, `profile`.
3. Choose **Save**.

Google supports PKCE for desktop applications. Refresh tokens are issued
automatically when the `access_type=offline` parameter is
included in the authorization request. No additional configuration is
required.

Your OIDC endpoints are as follows:

| Field                  | Value                                                               |
| ---------------------- | ------------------------------------------------------------------- |
| Issuer URL             | `https://accounts.google.com`                                       |
| Authorization endpoint | `https://accounts.google.com/o/oauth2/v2/auth`                      |
| Token endpoint         | `https://oauth2.googleapis.com/token?client_secret=<CLIENT_SECRET>` |
| JWKS URI               | `https://www.googleapis.com/oauth2/v3/certs`                        |

###### Note

Append your client secret to the token endpoint as a
`client_secret` query parameter so that token exchange
succeeds—for example,
`https://oauth2.googleapis.com/token?client_secret=<CLIENT_SECRET>`.
Replace `<CLIENT_SECRET>` with the client secret
generated for your OAuth client.

### Okta

For detailed instructions, see [Create OpenID Connect app integrations](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm "https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm") in the Okta
documentation.

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

1. In the Okta Admin Console, navigate to **Security → API → Authorization Servers** and
   select your authorization server (for example, **default**).
2. On the **Scopes** tab, verify that
   the following scopes are enabled: `openid`,
   `email`, `profile`,
   `offline_access`.
3. On the **Access Policies** tab,
   verify that the policy assigned to this application allows the
   `Authorization Code` and `Refresh Token`
   grant types.

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

### Ping Identity

Choose the instructions for your Ping Identity product.

#### PingFederate

For detailed instructions, see [Setting up an OIDC application in PingFederate](https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_oidc_app_setup_pf.html "https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_oidc_app_setup_pf.html") in the Ping
Identity documentation.

###### To create the PingFederate OIDC client

1. In the PingFederate administrative console, go to
   **Applications → OAuth →
   Clients**, and choose **Add
   Client**.
2. In the **Client ID** field, enter
   a unique identifier for this client.
3. In the **Name** field, enter
   `Amazon Quick Desktop`.
4. For **Client Authentication**,
   select **None**.
5. In the **Redirection URI**
   section, enter `http://localhost:18080` and choose
   **Add**.
6. In the **Allowed Grant Types**
   list, select **Authorization Code**
   and **Refresh Token**.
7. Select the **Require Proof Key for Code
   Exchange (PKCE)** checkbox.
8. Under **Common Scopes**, grant
   the following: `openid`, `email`,
   `profile`, `offline_access`.
9. Choose **Save**.
10. Note the **Client ID**. You need
    this value in later steps.

###### To configure the OIDC policy

1. In the PingFederate administrative console, go to
   **Applications → OAuth → OpenID
   Connect Policy Management**.
2. Select the OIDC policy associated with this client, or choose
   **Add Policy** to create
   one.
3. Select the **Return ID Token On Refresh
   Grant** checkbox. This ensures that the desktop
   application receives a fresh ID token with current claims when
   refreshing the session.
4. Under **Attribute Contract**,
   verify that the `email` claim is included and mapped
   to the corresponding user attribute in your authentication
   source. The `email` claim must be present in tokens
   issued during both initial authentication and refresh token
   grants.
5. Choose **Save**.

Your OIDC endpoints use the following format. Replace
`<PINGFEDERATE_HOST>` with your PingFederate server
hostname.

| Field                  | Value                                                 |
| ---------------------- | ----------------------------------------------------- |
| Issuer URL             | `https://<PINGFEDERATE_HOST>`                         |
| Authorization endpoint | `https://<PINGFEDERATE_HOST>/as/authorization.oauth2` |
| Token endpoint         | `https://<PINGFEDERATE_HOST>/as/token.oauth2`         |
| JWKS URI               | `https://<PINGFEDERATE_HOST>/pf/JWKS`                 |

#### PingOne

For detailed instructions, see [Editing an application – Native](https://docs.pingidentity.com/pingone/applications/p1_edit_application_native.html "https://docs.pingidentity.com/pingone/applications/p1_edit_application_native.html") in the Ping Identity
documentation.

###### To create the PingOne OIDC native application

1. In the PingOne admin console, go to **Applications → Applications** and choose the
   **+** icon.
2. Enter `Amazon Quick Desktop` as the application
   name.
3. In the **Application Type**
   section, select **Native**, then
   choose **Save**.
4. On the **Configuration** tab,
   choose **Edit** and configure the
   following settings:

| Setting                              | Value                                |
| ------------------------------------ | ------------------------------------ |
| Response Type                        | Code                                 |
| Grant Type                           | Authorization Code and Refresh Token |
| PKCE Enforcement                     | S256                                 |
| Redirect URIs                        | `http://localhost:18080`             |
| Token Endpoint Authentication Method | None                                 |

5. Choose **Save**.
6. On the **Resources** tab, add the
   following scopes: `openid`, `email`,
   `profile`, `offline_access`.
7. On the **Attribute Mappings** tab,
   verify that the `email` attribute is mapped to the
   user's email address.
8. Toggle the application to **Enabled**.
9. Note the **Client ID** and
   **Environment ID** from the
   **Configuration** tab.

###### Note

The PingOne domain varies by region. The examples below use
`.com`. Replace the domain with the one for your
environment (for example, `.ca`, `.eu`, or
`.asia`).

Your OIDC endpoints use the following format. Replace
`<ENV_ID>` with your PingOne environment ID.

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| Issuer URL             | `https://auth.pingone.com/<ENV_ID>/as`           |
| Authorization endpoint | `https://auth.pingone.com/<ENV_ID>/as/authorize` |
| Token endpoint         | `https://auth.pingone.com/<ENV_ID>/as/token`     |
| JWKS URI               | `https://auth.pingone.com/<ENV_ID>/as/jwks`      |

## Step 2: Configure the extension access in the Amazon Quick management console

###### To add the extension access

1. Sign in to the Amazon Quick management console and choose
   **Manage account**.
2. In the left navigation pane, under **Permissions**,
   choose **Extension access**.
3. Choose **Add extension access**.
4. Under **Select Service**, select
   **Amazon Quick (Desktop application for
   Quick)** and choose **Next**.
5. Enter the Amazon Quick extension details:

| Field                  | Value                                                                    | Notes                                                                                                             |
| ---------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Name                   | A name for this extension access (for example,<br>`QuickDesktop-access`) | Internal reference only. This name is not<br>configured in your IdP. Alphanumeric and hyphens<br>only, no spaces. |
| Description            | (Optional) A description of this extension<br>access                     | Optional. For your reference only.                                                                                |
| Issuer URL             | The OIDC issuer URL from Step 1                                          | Must include the `/v2.0` suffix for<br>Entra ID.                                                                  |
| Authorization Endpoint | The OIDC authorization endpoint URL from<br>Step 1                       |                                                                                                                   |
| Token Endpoint         | The OIDC token endpoint URL from Step 1                                  |                                                                                                                   |
| JWKS URI               | The JSON Web Key Set URI from Step 1                                     |                                                                                                                   |
| Client ID              | The OIDC client identifier from Step 1                                   |                                                                                                                   |

6. Choose **Add**.

###### Important

Verify that all values are correct before choosing
**Add**. The extension access
configuration cannot be edited after creation. If any value is
incorrect, you must delete the extension access and create a new
one.

###### To create the extension

1. In the Amazon Quick management console, in the left navigation pane, choose
   **Quick**, then under **Connect apps and data**, choose **Extensions**.
2. Choose **Add extension**.
3. Select the **Desktop application for
   Quick** extension access you previously created. Choose
   **Next**.
4. Choose **Create**.

###### Important

Both steps are required. If you only configure the extension access
without creating the extension, enterprise sign-in will not be available and
users will see the error: "Enterprise sign-in for Quick Desktop has not been
configured for this account."

###### Note

Creating the extension is a one-time, account-level action. Once an
administrator creates the extension, enterprise sign-in is available
for all users in the account. Individual users do not need to enable
the extension themselves — they only need to download the desktop
application and sign in.

## Step 3: Download and distribute the desktop application

After you configure enterprise sign-in, verify the setup by downloading and
installing the desktop application yourself. Choose **Enterprise
login** on the sign-in screen and authenticate with your corporate
credentials to confirm the configuration is working. For download and installation
steps, see [Getting started](getting-started-desktop.md "getting-started-desktop.md").

If the sign-in fails, verify the values you entered in Step 2 against the OIDC
endpoints from Step 1. If any value is incorrect, delete the extension access under
**Permissions → Extension access**, and repeat
Step 2 with the correct values.

After you verify the setup, direct your users to [Getting started](getting-started-desktop.md "getting-started-desktop.md") for
download, installation, and sign-in instructions.

## Troubleshooting

`redirect_mismatch` error

Verify that the redirect URI in your IdP is exactly
`http://localhost:18080` and is configured as a public
client or native platform.

User not found after sign-in

This error has two common causes:

1. **The email claim is not being returned
   in the token.** For Microsoft Entra ID, you must add
   the `email` optional claim to the ID token under
   Token configuration (see Step 1). Additionally, the user's
   **Mail** attribute must be
   populated in their Entra ID profile. The User Principal Name
   (UPN) alone is not sufficient.
2. **No matching user exists in
   Amazon Quick.** The email in the token must exactly
   match the email of a provisioned user. For IAM Identity
   Center accounts, verify the user's email in Identity Center
   matches. Email matching is case-sensitive.

Token validation failure

Verify that the issuer URL in the extension access configuration
matches the issuer URL in your IdP's OIDC configuration exactly.

Invalid issuer error (Microsoft Entra ID)

If sign-in fails with "Invalid issuer:
https://login.microsoftonline.com/TENANT\_ID/v2.0", verify that the
Issuer URL in your extension access configuration includes the
`/v2.0` path suffix. The Entra ID v2.0 endpoint issues
tokens with an `iss` claim that includes
`/v2.0`. If the suffix is missing, delete the extension
access and recreate it with the correct Issuer URL.

Enterprise sign-in not configured for this account

This error means the extension access was created but the extension
itself was not. Navigate to **Connect apps and data
→ Extensions** in the management console and create the
extension, selecting the extension access you previously
configured.

User info request failed (HTTP 504)

This is a transient backend timeout. Sign in to your Amazon Quick
account via the web browser first, then retry the desktop sign-in.
If the error persists, verify network connectivity to the Amazon Quick
service endpoint.

Consent or permission errors (Microsoft Entra ID)

Grant admin consent for the required API permissions in the Azure
portal. Navigate to the app registration's **API
permissions** page and choose **Grant admin
consent for [your organization]**.

Session expires frequently

Verify that your IdP is configured to issue refresh tokens. For
Microsoft Entra ID, the `offline_access` scope is required.
For Google Workspace, include `access_type=offline` in the
authorization request (handled automatically by Quick).
For Okta, the Refresh Token grant type must be enabled and the
`offline_access` scope must be granted. For Ping Identity,
the Refresh Token grant type must be enabled and the
`offline_access` scope must be granted. For PingFederate,
also verify that **Return ID Token On Refresh
Grant** is selected in the OIDC policy.

`invalid_scope` error (Okta)

Verify that `offline_access` is enabled on your
authorization server. Navigate to **Security
→ API → Authorization Servers → default →
Scopes** and confirm the scope is present. Also verify
that the access policy for the application allows the Refresh Token
grant type.

Application not enabled (PingOne)

If authentication fails immediately without reaching the PingOne
login page, verify that the application toggle is set to
**Enabled** in the PingOne admin
console.

Missing email claim after refresh (PingFederate)

Verify that the `email` claim is included in the OIDC
policy **Attribute Contract** and mapped
to the correct user attribute. The mapping must produce the
`email` claim for both initial authentication and refresh
token grants.
