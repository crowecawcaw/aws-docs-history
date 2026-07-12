# Troubleshooting enterprise sign-in for Amazon Quick on desktop

|                                           |
| ----------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition |

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

Use the following guidance to resolve common enterprise sign-in issues, regardless
of which identity provider you use.

###### Tip

To help diagnose a sign-in problem, you can export application logs from the
sign-in screen. Include these logs when you contact your administrator or
AWS Support.

###### Note

If the application cannot reach the sign-in page, complete authentication, or
load content, the issue might be network related. In restricted environments,
confirm that the required domains are on your allow list and that firewall and VPN
settings are not blocking the connections. For the list of required domains, see
[Network access and required domains](desktop-security.md#desktop-network-access "desktop-security.md#desktop-network-access").

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
itself was not. In the Amazon Quick console, in the left navigation pane,
choose **Extensions** (you might need to choose
**More** to find it), and create the extension,
selecting the extension access you previously configured.

User info request failed (HTTP 504)

This is a transient backend timeout. Sign in to your Amazon Quick
account via the web browser first, then retry the desktop sign-in.
If the error persists, verify network connectivity to the Amazon Quick
service endpoint. For the list of required domains, see [Network access and required domains](desktop-security.md#desktop-network-access "desktop-security.md#desktop-network-access").

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
