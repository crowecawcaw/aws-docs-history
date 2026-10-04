

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Common error messages
<a name="common-error-messages"></a>

The following are common error messages and their resolutions:


**WebAuthn error messages and resolutions**  

| Error message | Resolution | 
| --- | --- | 
| Amazon DCV WebAuthn redirection failed to complete the registration request: Webauthn redirection is not supported by the client | Check that you are using a supported browser and version (Chrome 136\+ or Edge 137\+). | 
| Prompt appears but unable to interact with local authenticators | Check that the Amazon DCV WebAuthn redirection extension is installed and enabled in your remote browser. | 
| Amazon DCV WebAuthn redirection failed to complete the registration request: The relying party ID is not a registrable domain suffix of, nor equal to the current domain. Subsequently, an attempt to fetch the .well-known/webauthn resource of the claimed RP ID failed. | This means that the WebAuthenticationRemoteDesktopAllowedOrigins local browser policy is not applied. Check the policy and update to allow the content domain. Ensure that the browser is restarted. You may have to start a new session for changes to apply. | 
| The operation either timed out or was not allowed. See: https://www.w3.org/TR/webauthn-2/\#sctn-privacy-considerations-client. | This error could occur if: (1) The DCV WebAuthn redirection extension is not installed or enabled, (2) The user cancels the authentication prompt, (3) The user enters an incorrect PIN for their security key, or (4) The user does not interact with the prompt and the request times out. | 