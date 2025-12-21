# Enabling WebAuthn redirection support in Amazon WorkSpaces Secure Browser

###### Warning

WebAuthn redirection only works in browser sessions with internet access enabled. Ensure your portal's network settings allow internet access for WebAuthn functionality to work properly.

WorkSpaces Secure Browser supports WebAuthn (Web Authentication) for websites accessed within the remote browser session. This allows users to authenticate to websites using their local FIDO2 security keys, biometric authenticators, and platform authenticators while browsing in their WorkSpaces Secure Browser session.

###### Note

WebAuthn redirection is available for end users using Google Chrome 136 (or later) or Microsoft Edge 137 (or later). **This feature is not available for non-Chromium browsers such as Safari or Firefox.**

**To enable WebAuthn redirection functionality, administrators must configure both:**

1. **Portal User settings** - Enable WebAuthn redirection in the portal settings
2. **End-user local browser policies** - Configure the WebAuthenticationRemoteDesktopAllowedOrigins browser policy on user devices to allow WebAuthn redirection

###### Topics

- [Enabling WebAuthn redirection in portal settings](enable-webauthn-portal.md "enable-webauthn-portal.md")
- [Configuring local browser policy for WebAuthn](configure-local-browser-policy.md "configure-local-browser-policy.md")
- [Using WebAuthn redirection in remote browser sessions](webauthn-usage.md "webauthn-usage.md")
- [Troubleshooting WebAuthn redirection issues](webauthn-troubleshooting.md "webauthn-troubleshooting.md")
