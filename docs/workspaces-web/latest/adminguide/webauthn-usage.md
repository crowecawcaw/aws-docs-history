

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Using WebAuthn redirection in remote browser sessions
<a name="webauthn-usage"></a>

Once WebAuthn redirection is enabled in the portal settings and the local browser policy is configured, users can use WebAuthn authentication on websites within their WorkSpaces Secure Browser remote browser sessions.

Users can authenticate to websites using:
+ FIDO2 security keys connected to their local device
+ Passkeys
+ Platform authenticators like Windows Hello or Touch ID

The WebAuthn authentication process is seamlessly forwarded from the remote browser session to the user's local device, providing secure passwordless authentication while maintaining the security benefits of the remote browsing environment.