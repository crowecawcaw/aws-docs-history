

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# WebAuthn redirection not working
<a name="webauthn-not-working"></a>

If WebAuthn authentication prompts do not appear or fail to work:

1. Verify WebAuthn is enabled in the portal settings under **User permissions**.

1. Check that the local browser policy is configured correctly by navigating to `chrome://policy` or `edge://policy` and confirming `WebAuthenticationRemoteDesktopAllowedOrigins` includes your region's content URL.

1. Ensure the browser version meets requirements: Chrome 136\+ or Edge 137\+.

1. Test with a different authenticator (security key vs. platform authenticator).