

# Set up enterprise sign-in with Ping Identity for Amazon Quick on desktop
<a name="desktop-enterprise-ping-identity"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

Use these steps only if you choose **Configure Identity Provider** when you add the desktop connector. Most organizations don't need a separate identity provider configuration for the desktop application. For the default setup, see [Turning on desktop access](desktop-enterprise-setup.md#desktop-enterprise-turn-on).

This page walks you through the three steps to set up enterprise sign-in with Ping Identity:

1. Create an OpenID Connect (OIDC) application in your Ping Identity product (PingFederate or PingOne) and record its values.

1. Add the desktop connector with your identity provider configuration.

1. Download, verify, and distribute the desktop application.

Before you begin, review the prerequisites in [Setting up Amazon Quick on desktop for enterprise deployments](desktop-enterprise-setup.md) and [Using a dedicated identity provider configuration (advanced)](desktop-enterprise-advanced-idp.md).

**Note**  
To sign in, users need an active Amazon Quick web session in their browser. The email address in Ping Identity must exactly match the user's email address in Quick, and Ping Identity must not mark that email address as unverified. For more information, see [How sign-in works with a dedicated identity provider](desktop-enterprise-advanced-idp.md#desktop-enterprise-how-it-works).

## Step 1: Create an OIDC application in Ping Identity
<a name="desktop-enterprise-ping-identity-step1"></a>

Register a public OIDC client in your Ping Identity product. The Amazon Quick desktop application uses this client to authenticate users through the authorization code flow with PKCE. This client requires no client secret. Enable the Refresh Token grant type and grant the `offline_access` scope. Choose the instructions for your Ping Identity product.

### PingFederate
<a name="desktop-enterprise-pingfederate"></a>

For more information, see [Setting up an OIDC application in PingFederate](https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_oidc_app_setup_pf.html) in the Ping Identity documentation.

**To create the PingFederate OIDC client**

1. In the PingFederate administrative console, go to **Applications → OAuth → Clients**, and choose **Add Client**.

1. In the **Client ID** field, enter a unique identifier for this client.

1. In the **Name** field, enter `Amazon Quick Desktop`.

1. For **Client Authentication**, select **None**.

1. In the **Redirection URI** section, enter `http://localhost:18080` and choose **Add**.

1. In the **Allowed Grant Types** list, select **Authorization Code** and **Refresh Token**.

1. Select the **Require Proof Key for Code Exchange (PKCE)** checkbox.

1. Under **Common Scopes**, grant the following: `openid`, `email`, `profile`, `offline_access`.

1. Choose **Save**.

1. Note the **Client ID**. You need this value in later steps.

**To configure the OIDC policy**

1. In the PingFederate administrative console, go to **Applications → OAuth → OpenID Connect Policy Management**.

1. Select the OIDC policy associated with this client, or choose **Add Policy** to create one.

1. Select the **Return ID Token On Refresh Grant** checkbox. This ensures that the desktop application receives a fresh ID token with current claims when refreshing the session.

1. Under **Attribute Contract**, verify that the `email` claim is included and mapped to the corresponding user attribute in your authentication source. The `email` claim must be present in tokens issued during both initial authentication and refresh token grants.

1. Choose **Save**.

Record the following OIDC endpoints. You enter these values, together with the **Client ID** you noted earlier, in Step 2. Replace `<PINGFEDERATE_HOST>` with your PingFederate server hostname.


| Field | Value | 
| --- | --- | 
| Client ID | The Client ID you entered when you created the client | 
| Issuer URL | https://<PINGFEDERATE\_HOST> | 
| Authorization endpoint | https://<PINGFEDERATE\_HOST>/as/authorization.oauth2 | 
| Token endpoint | https://<PINGFEDERATE\_HOST>/as/token.oauth2 | 
| JWKS URI | https://<PINGFEDERATE\_HOST>/pf/JWKS | 

### PingOne
<a name="desktop-enterprise-pingone"></a>

For more information, see [Editing an application – Native](https://docs.pingidentity.com/pingone/applications/p1_edit_application_native.html) in the Ping Identity documentation.

**To create the PingOne OIDC native application**

1. In the PingOne admin console, go to **Applications → Applications** and choose the **\+** icon.

1. Enter `Amazon Quick Desktop` as the application name.

1. In the **Application Type** section, select **Native**, then choose **Save**.

1. On the **Configuration** tab, choose **Edit** and configure the following settings:


<table>
<thead>
  <tr><th>Setting</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td>Response Type</td><td>Code</td></tr>
  <tr><td>Grant Type</td><td>Authorization Code and Refresh Token</td></tr>
  <tr><td>PKCE Enforcement</td><td>S256</td></tr>
  <tr><td>Redirect URIs</td><td><code>http://localhost:18080</code></td></tr>
  <tr><td>Token Endpoint Authentication Method</td><td>None</td></tr>
</tbody>
</table>


1. Choose **Save**.

1. On the **Resources** tab, add the following scopes: `openid`, `email`, `profile`, `offline_access`.
**Add scopes on the Resources tab, not the Configuration tab**  
This is a separate step from the **Configuration** tab. PingOne grants only the `openid` scope by default, so you must explicitly add `email`, `profile`, and `offline_access` on the **Resources** tab. If you skip this step, sign-in fails with "User info request failed (HTTP 401)". This error occurs because sign-in requires tokens issued with these scopes, and PingOne does not grant them unless you add them on this tab.

1. On the **Attribute Mappings** tab, verify that the `email` attribute is mapped to the user's email address.

1. Toggle the application to **Enabled**.

1. Note the **Client ID** and **Environment ID** from the **Configuration** tab.

**Note**  
The PingOne domain varies by region. The following examples use `.com`. Replace the domain with the one for your environment (for example, `.ca`, `.eu`, or `.asia`).

Record the following OIDC endpoints. You enter these values, together with the **Client ID** you noted earlier, in Step 2. Replace `<ENV_ID>` with your PingOne environment ID.


| Field | Value | 
| --- | --- | 
| Client ID | The Client ID from the Configuration tab | 
| Issuer URL | https://auth.pingone.com/<ENV\_ID>/as | 
| Authorization endpoint | https://auth.pingone.com/<ENV\_ID>/as/authorize | 
| Token endpoint | https://auth.pingone.com/<ENV\_ID>/as/token | 
| JWKS URI | https://auth.pingone.com/<ENV\_ID>/as/jwks | 

**Use the correct JWKS URI path for PingOne**  
For the JSON Web Key Set (JWKS) URI, use the `/as/jwks` path shown in the preceding table. Do not use `/.well-known/jwks.json`, which can appear as a placeholder in some PingOne forms. PingOne does not use this path, and sign-in token validation fails if you enter it.

## Step 2: Add the desktop connector with your identity provider configuration
<a name="w2aac51c53c15c27c29c19"></a>

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
<a name="w2aac51c53c15c27c29c21"></a>

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