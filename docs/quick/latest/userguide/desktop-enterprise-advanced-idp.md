

# Using a dedicated identity provider configuration (advanced)
<a name="desktop-enterprise-advanced-idp"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

Choose **Configure Identity Provider** when you add the desktop connector if you want to manage desktop sign-in separately from web and mobile sign-in in your identity provider.

If your users already sign in to Quick on the web through your identity provider, such as Okta or Microsoft Entra ID, the default option, **Use Quick's existing configured sign-in method**, already uses it, and you don't need **Configure Identity Provider**.

This option takes more setup than the default. You register an OpenID Connect (OIDC) application in your identity provider, and each user's email address in your identity provider must exactly match their email address in Quick. For more information, see [How sign-in works with a dedicated identity provider](#desktop-enterprise-how-it-works).

## Additional prerequisites
<a name="desktop-enterprise-advanced-idp-prerequisites"></a>

In addition to the prerequisites in [Prerequisites](desktop-enterprise-setup.md#desktop-enterprise-prerequisites), verify that you have the following:
+ Access to your identity provider with permissions to create OIDC application registrations.

## How sign-in works with a dedicated identity provider
<a name="desktop-enterprise-how-it-works"></a>

When you use a dedicated identity provider configuration, the Amazon Quick desktop application uses the OIDC protocol to authenticate users. When you choose **Continue with SSO**, a browser window opens to Amazon Quick. Amazon Quick identifies your configured identity provider and redirects to your IdP's authorization endpoint. The application then exchanges the resulting authorization code for tokens using Proof Key for Code Exchange (PKCE).

To identify the configured identity provider, your browser must have an active Amazon Quick web session. If no session exists, the browser prompts you to sign in to Amazon Quick before the application redirects to your IdP.

Amazon Quick validates the token and maps the user to an identity in your account. The email address in your IdP must exactly match the email address of the user in Amazon Quick, and your IdP must not mark the email address as unverified.

**Note**  
If you sign in for the first time, the browser checks for an active Amazon Quick web session. If no session exists, the browser opens the Amazon Quick sign-in page instead of redirecting to your IdP. Sign in to Amazon Quick in the browser to continue. The desktop application then completes sign-in through your configured identity provider.

### Session limits
<a name="desktop-enterprise-session-limits"></a>

With a dedicated identity provider configuration, a desktop session ends when the shorter of these limits is reached:
+ The Amazon Quick limit: 30 days from sign-in, regardless of activity.
+ Your identity provider's session limit.

When the session ends, users sign in again.

## Supported token signing algorithms
<a name="desktop-enterprise-token-signing"></a>

When you use a dedicated identity provider configuration, Amazon Quick verifies the signature on each ID token against the public keys published at your identity provider's JWKS URI. Your IdP must sign ID tokens with one of the following asymmetric algorithms.


**Supported signing algorithms by key type**  

| Key type | Supported `alg` values | 
| --- | --- | 
| RSA | RS256, RS384, RS512, PS256, PS384, PS512 | 
| ECDSA | ES256, ES384, ES512 | 

**Symmetric signing is not supported**  
Amazon Quick does not accept ID tokens signed with HMAC (`HS256`, `HS384`, or `HS512`). These algorithms sign the token with the client secret rather than with a key that can be published in a JWKS, so the signature cannot be verified against your IdP's JWKS URI. Unsecured tokens (an `alg` value of `none`) are also rejected. If your IdP is configured to use one of these, sign-in fails with a token validation error.

You do not select the algorithm in Amazon Quick. Your IdP chooses it when it issues the token, and Amazon Quick accepts any of the algorithms in the preceding table. Most identity providers use `RS256` by default.

## Setup process
<a name="desktop-enterprise-process"></a>

Setting up a dedicated identity provider configuration involves the same three steps regardless of which identity provider you use:

1. **Create an OIDC application in your identity provider.** Register a public OIDC client and record its Client ID and OIDC endpoints. The steps and endpoint formats are specific to your identity provider.

1. **Add the desktop connector with your identity provider configuration.** In the Amazon Quick console, go to **Inbound connectors**, choose the **Quick Desktop** tab, and then choose **Add desktop connector**. Choose **Configure Identity Provider**, and enter the Client ID and OIDC endpoints from Step 1.

1. **Download, verify, and distribute the desktop application.** Download and install the application, choose **Continue with SSO** to confirm that authentication succeeds, and then direct your users to download and sign in.

The complete procedure for each step is on the page for your identity provider:
+ [Microsoft Entra ID](desktop-enterprise-entra-id.md)
+ [Google Workspace](desktop-enterprise-google-workspace.md)
+ [Okta](desktop-enterprise-okta.md)
+ [Ping Identity](desktop-enterprise-ping-identity.md) (PingFederate and PingOne)

If you have problems during setup or sign-in, see [Troubleshooting enterprise sign-in for Amazon Quick on desktop](desktop-enterprise-setup-troubleshooting.md).

**Topics**
+ [Additional prerequisites](#desktop-enterprise-advanced-idp-prerequisites)
+ [How sign-in works with a dedicated identity provider](#desktop-enterprise-how-it-works)
+ [Supported token signing algorithms](#desktop-enterprise-token-signing)
+ [Setup process](#desktop-enterprise-process)
+ [Set up enterprise sign-in with Microsoft Entra ID for Amazon Quick on desktop](desktop-enterprise-entra-id.md)
+ [Set up enterprise sign-in with Google Workspace for Amazon Quick on desktop](desktop-enterprise-google-workspace.md)
+ [Set up enterprise sign-in with Okta for Amazon Quick on desktop](desktop-enterprise-okta.md)
+ [Set up enterprise sign-in with Ping Identity for Amazon Quick on desktop](desktop-enterprise-ping-identity.md)