

# WebAuthn redirection

WebAuthn redirection lets users sign in to websites and applications in a WorkSpaces Applications streaming session with a FIDO2 authenticator attached to their local device. Supported authenticators include a YubiKey or other security key, or a platform authenticator such as Windows Hello or Touch ID. When an application in the session makes a WebAuthn request, WorkSpaces Applications forwards the request to the user's device. The authenticator signs the request locally and returns the signed response to the application. Private keys never leave the user's device.

You enable WebAuthn redirection on a stack. The setting applies to every fleet associated with that stack. On Windows fleets, you can also control which processes are allowed to use WebAuthn redirection with a process compatibility list.

WebAuthn redirection works differently on Windows and Linux fleets:
+ Windows fleets use Enhanced WebAuthn redirection. WorkSpaces Applications redirects requests made through the Windows WebAuthn API for any process on the process compatibility list. Supported processes include web browsers, native Windows applications, and the Microsoft sign-in broker used by Microsoft Teams and Microsoft 365. No browser extension is required.
+ Linux fleets use Standard WebAuthn redirection. WorkSpaces Applications redirects requests made in Google Chrome, Chromium, or Microsoft Edge through the Amazon DCV WebAuthn redirection browser extension. WorkSpaces Applications installs this extension automatically when a session starts. Other browsers and native applications are not supported, and the process compatibility list does not apply.

**Topics**
+ [Prerequisites](webauthn-redirection-prerequisites.md)
+ [Enable WebAuthn redirection](webauthn-redirection-enable.md)
+ [Configure the process compatibility list (Windows fleets)](webauthn-redirection-configure-process-compatibility-list.md)
+ [Troubleshooting](webauthn-redirection-troubleshooting.md)
+ [Security considerations and best practices](webauthn-redirection-security.md)