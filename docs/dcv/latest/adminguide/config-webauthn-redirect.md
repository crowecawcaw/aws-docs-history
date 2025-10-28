# Configuring WebAuthn Redirection

Beginning with Amazon DCV Server 2023.1, users can authenticate on web applications that use the Web Authentication (WebAuthn) standard in supported
browsers within remote sessions. This is done by redirecting the authentication prompts to locally connected authenticators, such as Windows Hello
or YubiKey, or any other FIDO2 compliant authenticator.

WebAuthn redirection operates independently of USB redirection. There is no requirement to install any vendor-specific drivers on the Amazon DCV server.
Redirection of WebAuthn requests is facilitated through the native API of the browser.

Before using WebAuthn, double check the [Supported Features](servers.md#features "servers.md#features") table to make sure you meet all of the requirements.

###### Topics

- [Configuring WebAuthn redirection on Windows hosts](webauth-windows.md "webauth-windows.md")
- [Configuring WebAuthn redirection on Linux hosts](webauth-linux.md "webauth-linux.md")
  WebAuthn is supported on Windows and Linux hosts, and on Windows, Mac and Linux clients.

- Google Chrome 116 or later
- Microsoft Edge 116 or later
  WebAuthn redirection can be enabled or disabled using the `webauthn-redirection` permission. For more information, see [Working with permissions files](security-authorization-file-create.md "security-authorization-file-create.md").

WebAuthn redirection requires a browser extension to be installed on the remote server. When the feature is enabled and the browser extension is installed, any WebAuthn requests initiated by
the web applications running in the browser within the session are seamlessly redirected to the local client. Users can then use utilize devices like Windows Hello or YubiKey to finalize the authentication.

###### Note

While this feature allows WebAuthn within a browser during a remote session, it does not
support DCV session authentication using WebAuthn authenticators.
