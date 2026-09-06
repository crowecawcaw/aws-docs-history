

# Troubleshooting enterprise sign-in for Amazon Quick on desktop
<a name="desktop-enterprise-setup-troubleshooting"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

Use the following guidance to resolve common enterprise sign-in issues, regardless of which identity provider you use.

**Tip**  
To help diagnose a sign-in problem, you can export application logs from the sign-in screen. Include these logs when you contact your administrator or AWS Support.

**Note**  
If the application cannot reach the sign-in page, complete authentication, or load content, the issue might be network related. In restricted environments, confirm that the required domains are on your allow list and that firewall and VPN settings are not blocking the connections. For the list of required domains, see [Network access and required domains](desktop-security.md#desktop-network-access).

`redirect_mismatch` error  
Verify that the redirect URI in your IdP is exactly `http://localhost:18080` and is configured as a public client or native platform.

Access blocked: app not verified (Google Workspace)  
This error means the OAuth consent screen is set to **External**. In the Google Cloud Console, navigate to **Google Auth Platform** → **Branding** and set the **User type** to **Internal**, which restricts sign-in to users in your Google Workspace organization.

User not found after sign-in  
This error has two common causes:  

1. **The email claim is not being returned in the token.** For Microsoft Entra ID, you must add the `email` optional claim to the ID token under Token configuration (see Step 1). Additionally, the user's **Mail** attribute must be populated in their Entra ID profile. The User Principal Name (UPN) alone is not sufficient.

1. **No matching user exists in Amazon Quick.** The email in the token must exactly match the email of a provisioned user. For IAM Identity Center accounts, verify the user's email in Identity Center matches. Email matching is case-sensitive.

Token validation failure  
Verify that the issuer URL in the extension access configuration matches the issuer URL in your IdP's OIDC configuration exactly.

Invalid issuer error (Microsoft Entra ID)  
If sign-in fails with "Invalid issuer: https://login.microsoftonline.com/TENANT\_ID/v2.0", verify that the Issuer URL in your extension access configuration includes the `/v2.0` path suffix. The Entra ID v2.0 endpoint issues tokens with an `iss` claim that includes `/v2.0`. If the suffix is missing, delete the extension access and recreate it with the correct Issuer URL.

Enterprise sign-in not configured for this account  
This error means the extension access was created but the extension itself was not. In the Amazon Quick console, in the left navigation pane, choose **Extensions** (you might need to choose **More** to find it), and create the extension, selecting the extension access you previously configured.

User info request failed (HTTP 504)  
This is a transient backend timeout. Sign in to your Amazon Quick account via the web browser first, then retry the desktop sign-in. If the error persists, verify network connectivity to the Amazon Quick service endpoint. For the list of required domains, see [Network access and required domains](desktop-security.md#desktop-network-access).

Consent or permission errors (Microsoft Entra ID)  
Grant admin consent for the required API permissions in the Azure portal. Navigate to the app registration's **API permissions** page and choose **Grant admin consent for [your organization]**.

Session expires frequently  
Verify that your IdP is configured to issue refresh tokens. For Microsoft Entra ID, the `offline_access` scope is required. For Google Workspace, include `access_type=offline` in the authorization request (handled automatically by Quick). For Okta, the Refresh Token grant type must be enabled and the `offline_access` scope must be granted. For Ping Identity, the Refresh Token grant type must be enabled and the `offline_access` scope must be granted. For PingFederate, also verify that **Return ID Token On Refresh Grant** is selected in the OIDC policy.

Application not enabled (PingOne)  
If authentication fails immediately without reaching the PingOne login page, verify that the application toggle is set to **Enabled** in the PingOne admin console.

User info request failed (HTTP 401) (PingOne)  
The required scopes are not enabled on the application's **Resources** tab. This is a separate step from the **Configuration** tab: PingOne grants only the `openid` scope by default. In the PingOne admin console, open the application's **Resources** tab and add the `email`, `profile`, and `offline_access` scopes.

Token validation failure with a PingOne JSON Web Key Set (JWKS) URI  
Verify that the JWKS URI in your extension access configuration uses the `/as/jwks` path (for example, `https://auth.pingone.com/<ENV_ID>/as/jwks`). Do not use `/.well-known/jwks.json`, which can appear as a placeholder in some PingOne forms. PingOne does not use this path.

Missing email claim after refresh (PingFederate)  
Verify that the `email` claim is included in the OIDC policy **Attribute Contract** and mapped to the correct user attribute. The mapping must produce the `email` claim for both initial authentication and refresh token grants.