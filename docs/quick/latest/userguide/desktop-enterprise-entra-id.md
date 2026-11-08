

# Set up enterprise sign-in with Microsoft Entra ID for Amazon Quick on desktop
<a name="desktop-enterprise-entra-id"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

Use these steps only if you choose **Configure Identity Provider** when you add the desktop connector. Most organizations don't need a separate identity provider configuration for the desktop application. For the default setup, see [Turning on desktop access](desktop-enterprise-setup.md#desktop-enterprise-turn-on).

This page walks you through the three steps to set up enterprise sign-in with Microsoft Entra ID:

1. Create an OpenID Connect (OIDC) application in Microsoft Entra ID and record its values.

1. Add the desktop connector with your identity provider configuration.

1. Download, verify, and distribute the desktop application.

Before you begin, review the prerequisites in [Setting up Amazon Quick on desktop for enterprise deployments](desktop-enterprise-setup.md) and [Using a dedicated identity provider configuration (advanced)](desktop-enterprise-advanced-idp.md).

**Note**  
To sign in, users need an active Amazon Quick web session in their browser. The email address in Microsoft Entra ID must exactly match the user's email address in Quick, and Microsoft Entra ID must not mark that email address as unverified. For more information, see [How sign-in works with a dedicated identity provider](desktop-enterprise-advanced-idp.md#desktop-enterprise-how-it-works).

## Step 1: Create an OIDC application in Microsoft Entra ID
<a name="desktop-enterprise-entra-id-step1"></a>

Register a public OIDC client application in Microsoft Entra ID. The Amazon Quick desktop application uses this client to authenticate users through the authorization code flow with PKCE. This client requires no client secret. Grant the `offline_access` scope so that the application can issue refresh tokens. Without it, users must re-authenticate frequently.

For more information, see [Register an application](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) in the Microsoft Entra documentation.

**To create the Entra ID app registration**

1. In the Azure portal, navigate to **Microsoft Entra ID → App registrations → New registration**.

1. Configure the following settings:


<table>
<thead>
  <tr><th>Setting</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td>Name</td><td><code>Amazon Quick Desktop</code></td></tr>
  <tr><td>Supported account types</td><td>Accounts in this organizational directory only (Single tenant)</td></tr>
  <tr><td>Redirect URI platform</td><td>Public client/native (mobile &amp; desktop)</td></tr>
  <tr><td>Redirect URI</td><td><code>http://localhost:18080</code></td></tr>
</tbody>
</table>


1. Choose **Register**.

1. On the **Overview** page, note the **Application (client) ID** and **Directory (tenant) ID**. You need these values in later steps.

This is a public client registration. Entra ID enforces PKCE automatically for public clients.

**To configure API permissions**

1. In the app registration, navigate to **API permissions → Add a permission → Microsoft Graph → Delegated permissions**.

1. Add the following permissions: `openid`, `email`, `profile`, `offline_access`.

1. Choose **Add permissions**.

1. If your organization requires it, choose **Grant admin consent for [your organization]**.

**To configure authentication settings**

1. In the app registration, navigate to **Authentication**.

1. Under **Advanced settings**, leave **Allow public client flows** set to **No**.

1. Verify that `http://localhost:18080` is listed under **Mobile and desktop applications**.

1. Choose **Save**.

**To configure token claims**

1. In the app registration, navigate to **Token configuration**.

1. Choose **Add optional claim**.

1. Select token type: **ID**.

1. Select the `email` claim and choose **Add**.

**Important**  
This step is required. Without the `email` optional claim, Microsoft Entra ID does not include the user's email address in the ID token, and Amazon Quick cannot map the token to a user. Additionally, each user who signs in must have their **Mail** attribute populated in their Entra ID profile (under **Contact Information**). The User Principal Name (UPN) alone is not sufficient. The Mail attribute must contain a value.

Record the following OIDC endpoints. You enter these values, together with the **Application (client) ID** you noted earlier, in Step 2. Replace `<TENANT_ID>` with your Directory (tenant) ID.

**Important**  
The Issuer URL must include the `/v2.0` path suffix. Do not use the **Authority URL** shown in the Entra ID Endpoints panel, which omits this suffix. If the `/v2.0` suffix is missing, token validation fails with an "Invalid issuer" error at sign-in time.


| Field | Value | 
| --- | --- | 
| Client ID | The Application (client) ID from the app registration Overview page | 
| Issuer URL | https://login.microsoftonline.com/<TENANT\_ID>/v2.0 | 
| Authorization endpoint | https://login.microsoftonline.com/<TENANT\_ID>/oauth2/v2.0/authorize | 
| Token endpoint | https://login.microsoftonline.com/<TENANT\_ID>/oauth2/v2.0/token | 
| JWKS URI | https://login.microsoftonline.com/<TENANT\_ID>/discovery/v2.0/keys | 

**Tip**  
The JWKS URI is not displayed in the Microsoft Entra ID **Endpoints** panel. You can find it by opening the **OpenID Connect metadata document** URL from the Endpoints panel and locating the `jwks_uri` field in the JSON response. Alternatively, construct it using the format shown in the preceding table.

**Important**  
If your application has custom signing keys because of the claims-mapping feature, you must append an `appid` query parameter containing the **Application (client) ID** to the JWKS URI. Otherwise, token validation fails because the default keys endpoint does not return the application's custom signing key. For example:  
`https://login.microsoftonline.com/<TENANT_ID>/discovery/v2.0/keys?appid=<CLIENT_ID>`  
To confirm the correct value, open the OpenID Connect metadata document with the same `appid` parameter appended (`https://login.microsoftonline.com/<TENANT_ID>/.well-known/openid-configuration?appid=<CLIENT_ID>`) and use the `jwks_uri` it returns. For more information, see [Validate the signature](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens#validate-the-signature) in the Microsoft Entra documentation.

## Step 2: Add the desktop connector with your identity provider configuration
<a name="w2aac51c53c15c27c23c19"></a>

In the Amazon Quick console, add the desktop connector and enter the values that you recorded in Step 1.

**Important**  
Adding the desktop connector turns on desktop access for all users in your account right away. To roll out desktop in stages, restrict the **Quick desktop** capability in a custom permissions profile before you add the connector. For more information, see [Turning on desktop access](desktop-enterprise-setup.md#desktop-enterprise-turn-on). You can also restrict the capability after you add the connector.

**To add the desktop connector**

1. Sign in to the Amazon Quick console as an administrator.

1. Choose your profile icon, and then choose **Manage account**.

1. In the navigation pane, choose **Inbound connectors**, and then choose the **Quick Desktop** tab.

1. Choose **Add desktop connector**.

1. For the identity setup, choose **Configure Identity Provider**, and then enter the values that you recorded in Step 1:


**Identity provider configuration values**  

<table>
<thead>
  <tr><th>Field</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td>Issuer URL</td><td>The exact OIDC issuer URL from Step 1, including any required path suffix.</td></tr>
  <tr><td>Authorization endpoint</td><td>The OIDC authorization endpoint URL from Step 1.</td></tr>
  <tr><td>Token endpoint</td><td>The OIDC token endpoint URL from Step 1.</td></tr>
  <tr><td>JWKS URI</td><td>The JSON Web Key Set URI from Step 1.</td></tr>
  <tr><td>Client ID</td><td>The OIDC client identifier (Client ID or Application (client) ID) that you recorded in Step 1.</td></tr>
</tbody>
</table>


1. Choose **Confirm**.

1. Verify that the connector card shows the name **Quick Desktop** and the status **Enabled**.

**Note**  
Adding the desktop connector is a one-time, account-level action. After the connector is enabled, all users in your account can sign in with your identity provider. Users don't need to turn anything on themselves.

## Step 3: Download, verify, and distribute the desktop application
<a name="w2aac51c53c15c27c23c21"></a>

In this step, you install the desktop application, verify that enterprise sign-in works, and then distribute the application to your users.

First, download and install the application. For download locations and installation steps, see [Downloading and installing](getting-started-desktop.md#desktop-download-install).

Then, verify that enterprise sign-in works.

**To verify enterprise sign-in**

1. Open the Amazon Quick desktop application.

1. On the sign-in screen, choose **Continue with SSO**.

1. (Optional) Select your AWS Region, or choose **Dynamic** to detect your Region automatically.

1. Sign in with your corporate credentials. The application redirects to your identity provider, and then opens the Home screen after sign-in succeeds.

**Tip**  
If sign-in fails, check the values that you entered in Step 2 against the values from Step 1. For more information, see [Troubleshooting enterprise sign-in for Amazon Quick on desktop](desktop-enterprise-setup-troubleshooting.md).

Finally, distribute the application to your users. Direct them to [Getting started with the Amazon Quick desktop application](getting-started-desktop.md) for download, installation, and sign-in instructions. Users choose **Continue with SSO** and sign in with their corporate credentials. They don't need any other setup.