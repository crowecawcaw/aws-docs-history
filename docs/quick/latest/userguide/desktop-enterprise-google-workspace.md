

# Set up enterprise sign-in with Google Workspace for Amazon Quick on desktop
<a name="desktop-enterprise-google-workspace"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

Use these steps only if you choose **Configure Identity Provider** when you add the desktop connector. Most organizations don't need a separate identity provider configuration for the desktop application. For the default setup, see [Turning on desktop access](desktop-enterprise-setup.md#desktop-enterprise-turn-on).

This page walks you through the three steps to set up enterprise sign-in with Google Workspace:

1. Create an OpenID Connect (OIDC) application in Google Workspace and record its values.

1. Add the desktop connector with your identity provider configuration.

1. Download, verify, and distribute the desktop application.

Before you begin, review the prerequisites in [Setting up Amazon Quick on desktop for enterprise deployments](desktop-enterprise-setup.md) and [Using a dedicated identity provider configuration (advanced)](desktop-enterprise-advanced-idp.md).

**Note**  
To sign in, users need an active Amazon Quick web session in their browser. The email address in Google Workspace must exactly match the user's email address in Quick, and Google Workspace must not mark that email address as unverified. For more information, see [How sign-in works with a dedicated identity provider](desktop-enterprise-advanced-idp.md#desktop-enterprise-how-it-works).

## Step 1: Create an OIDC application in Google Workspace
<a name="desktop-enterprise-google-workspace-step1"></a>

Register an OAuth client in the Google Cloud Console. The Amazon Quick desktop application uses this client to authenticate users through the authorization code flow with PKCE. Google issues a refresh token automatically when the authorization request includes the `access_type=offline` parameter. Quick includes this parameter automatically. No additional scope or grant type configuration is required.

For more information, see [OAuth 2.0 for Mobile & Desktop Apps](https://developers.google.com/identity/protocols/oauth2/native-app) in the Google for Developers documentation.

**To create the Google OAuth client**

1. In the Google Cloud Console, navigate to **APIs & Services → Credentials → Create Credentials → OAuth client ID**.

1. Configure the following settings:


**OAuth client settings**  

<table>
<thead>
  <tr><th>Setting</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td>Application type</td><td>Desktop app</td></tr>
  <tr><td>Name</td><td><code>Amazon Quick Desktop</code></td></tr>
</tbody>
</table>


1. Choose **Create**.

1. Note the **Client ID** and **Client secret**. You need these values in later steps.

**To configure the OAuth consent screen**

1. In the Google Cloud Console, navigate to **Google Auth Platform → Branding**.

1. Set the **User type** to **Internal**. This restricts sign-in to users in your Google Workspace organization.

1. Fill in the required app information and choose **Save**.

**To configure scopes**

1. In the Google Cloud Console, navigate to **Google Auth Platform → Data Access**.

1. Add the following scopes: `openid`, `email`, `profile`.

1. Choose **Save**.

Record the following OIDC endpoints. You enter these values, together with the **Client ID** you noted earlier, in Step 2.


**OIDC endpoint values**  

| Field | Value | 
| --- | --- | 
| Client ID | The Client ID from your OAuth client | 
| Issuer URL | https://accounts.google.com | 
| Authorization endpoint | https://accounts.google.com/o/oauth2/v2/auth | 
| Token endpoint | https://oauth2.googleapis.com/token?client\_secret=<CLIENT\_SECRET> | 
| JWKS URI | https://www.googleapis.com/oauth2/v3/certs | 

**Note**  
Append your client secret to the token endpoint as a `client_secret` query parameter so that token exchange succeeds. For example, `https://oauth2.googleapis.com/token?client_secret=<CLIENT_SECRET>`. Replace `<CLIENT_SECRET>` with the client secret generated for your OAuth client.

## Step 2: Add the desktop connector with your identity provider configuration
<a name="w2aac51c53c15c27c25c19"></a>

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
<a name="w2aac51c53c15c27c25c21"></a>

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