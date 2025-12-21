# WebAuthn redirection not working

If WebAuthn authentication prompts do not appear or fail to work:

1. Verify WebAuthn is enabled in the portal settings under **User permissions**.
2. Check that the local browser policy is configured correctly by navigating to `chrome://policy` or `edge://policy` and confirming `WebAuthenticationRemoteDesktopAllowedOrigins` includes your region's content URL.
3. Ensure the browser version meets requirements: Chrome 136+ or Edge 137+.
4. Test with a different authenticator (security key vs. platform authenticator).
