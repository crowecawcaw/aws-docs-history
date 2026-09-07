

# WebAuthn redirection not working
<a name="webauthn-not-working"></a>

If WebAuthn authentication prompts do not appear or fail to work:

1. Verify WebAuthn is enabled in the portal settings under **User permissions**.

1. Check that the local browser policy is configured correctly by navigating to `chrome://policy` or `edge://policy` and confirming `WebAuthenticationRemoteDesktopAllowedOrigins` includes your region's content URL.

1. Ensure the browser version meets requirements: Chrome 136\+ or Edge 137\+.

1. Test with a different authenticator (security key vs. platform authenticator).