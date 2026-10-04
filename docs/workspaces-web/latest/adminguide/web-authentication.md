

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Enabling WebAuthn redirection support in Amazon WorkSpaces Secure Browser
<a name="web-authentication"></a>

**Warning**  
WebAuthn redirection only works in browser sessions with internet access enabled. Ensure your portal's network settings allow internet access for WebAuthn functionality to work properly.

WorkSpaces Secure Browser supports WebAuthn (Web Authentication) for websites accessed within the remote browser session. This allows users to authenticate to websites using their local FIDO2 security keys, biometric authenticators, and platform authenticators while browsing in their WorkSpaces Secure Browser session.

**Note**  
WebAuthn redirection is available for end users using Google Chrome 136 (or later) or Microsoft Edge 137 (or later). **This feature is not available for non-Chromium browsers such as Safari or Firefox.**  
**To enable WebAuthn redirection functionality, administrators must configure both:**  
**Portal User settings** - Enable WebAuthn redirection in the portal settings
**End-user local browser policies** - Configure the WebAuthenticationRemoteDesktopAllowedOrigins browser policy on user devices to allow WebAuthn redirection

**Topics**
+ [Enabling WebAuthn redirection in portal settings](enable-webauthn-portal.md)
+ [Configuring local browser policy for WebAuthn](configure-local-browser-policy.md)
+ [Using WebAuthn redirection in remote browser sessions](webauthn-usage.md)
+ [Troubleshooting WebAuthn redirection issues](webauthn-troubleshooting.md)