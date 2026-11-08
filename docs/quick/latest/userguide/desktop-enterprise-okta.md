

# Set up enterprise sign-in with Okta for Amazon Quick on desktop
<a name="desktop-enterprise-okta"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

Use these steps only if you choose **Configure Identity Provider** when you add the desktop connector. Most organizations don't need a separate identity provider configuration for the desktop application. For the default setup, see [Turning on desktop access](desktop-enterprise-setup.md#desktop-enterprise-turn-on).

This page walks you through the three steps to set up enterprise sign-in with Okta:

1. Create an OpenID Connect (OIDC) application in Okta and record its values.

1. Add the desktop connector with your identity provider configuration.

1. Download, verify, and distribute the desktop application.

Before you begin, review the prerequisites in [Setting up Amazon Quick on desktop for enterprise deployments](desktop-enterprise-setup.md) and [Using a dedicated identity provider configuration (advanced)](desktop-enterprise-advanced-idp.md).

**Note**  
To sign in, users need an active Amazon Quick web session in their browser. The email address in Okta must exactly match the user's email address in Quick, and Okta must not mark that email address as unverified. For more information, see [How sign-in works with a dedicated identity provider](desktop-enterprise-advanced-idp.md#desktop-enterprise-how-it-works).

## Step 1: Create an OIDC application in Okta
<a name="desktop-enterprise-okta-step1"></a>

Register an OIDC native application in Okta. The Amazon Quick desktop application uses this client to authenticate users through the authorization code flow with PKCE, and requests the `openid`, `profile`, `email`, and `offline_access` scopes at sign-in.

For more information, see [Create OpenID Connect app integrations](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm) in the Okta documentation.

**To create the Okta OIDC Native Application**

1. In the Okta Admin Console, navigate to **Applications → Applications → Create App Integration**.

1. Select **OIDC - OpenID Connect** as the sign-in method.

1. Select **Native Application** as the application type, then choose **Next**.

1. Configure the following settings:


<table>
<thead>
  <tr><th>Setting</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td>App integration name</td><td><code>Amazon Quick Desktop</code></td></tr>
  <tr><td>Grant type</td><td>Authorization Code and Refresh Token</td></tr>
  <tr><td>Sign-in redirect URIs</td><td><code>http://localhost:18080</code></td></tr>
  <tr><td>Assignments</td><td>Assign to the appropriate users or groups</td></tr>
</tbody>
</table>


1. Choose **Save**.

1. On the **General** tab, note the **Client ID**.

Okta enforces PKCE (S256) automatically for native applications.

**To verify authentication settings**

1. In the app integration, go to the **General** tab.

1. Under **General Settings**, confirm that the application type is **Native**, client authentication is **None** (public client), and PKCE is **Required**.

1. Under **LOGIN**, confirm that `http://localhost:18080` is listed as a redirect URI.

1. Choose **Save** if you made any changes.

Record the following OIDC endpoints. You enter these values, together with the **Client ID** you noted earlier, in Step 2. Replace `<OKTA_DOMAIN>` with your Okta domain (for example, `your-org.okta.com`). For the endpoint reference, see [Authorization Code with PKCE](https://developer.okta.com/docs/guides/implement-grant-type/authcodepkce/main/) in the Okta documentation.


| Field | Value | 
| --- | --- | 
| Client ID | The Client ID from the General tab | 
| Issuer URL | https://<OKTA\_DOMAIN> | 
| Authorization endpoint | https://<OKTA\_DOMAIN>/oauth2/v1/authorize | 
| Token endpoint | https://<OKTA\_DOMAIN>/oauth2/v1/token | 
| JWKS URI | https://<OKTA\_DOMAIN>/oauth2/v1/keys | 

**Use the standard Okta domain, not the admin subdomain**  
Use your standard Okta domain (for example, `your-org.okta.com`) in these endpoints, not the `-admin` subdomain (`your-org-admin.okta.com`) shown in the address bar of the admin console. The `-admin` subdomain does not host the OAuth endpoints, so using it causes sign-in to fail with an HTTP 404 error.

## Step 2: Add the desktop connector with your identity provider configuration
<a name="w2aac51c53c15c27c27c19"></a>

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
<a name="w2aac51c53c15c27c27c21"></a>

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