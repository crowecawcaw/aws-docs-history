

# WebAuthn authentication for WorkSpaces client
<a name="webauthn_support"></a>

In-session WebAuthn authentication is supported using the DCV for Windows and Linux WorkSpaces, on Windows, Linux and macOS clients. WorkSpaces using the PCoIP protocol doesn't support WebAuthn redirection.

You can use WebAuthn authentication for in-session authentication using FIDO2-enabled authentication methods like security keys or biometrics. In-session authentication refers to WebAuthn authentication that's performed after logging in and requested by web applications running within the session. For example, you can use Yubikey for in-session authentication while using Google Chrome. 

## Client version requirements
<a name="webauthn-client-versions"></a>

The following WorkSpaces client versions support WebAuthn:


| WebAuthn Type | Client versions supported | 
| --- | --- | 
| Standard WebAuthn |  + Windows client 5.19.0 or above<br />+ Mac client 5.19.0 or above<br />+ Linux client 2024.0 or above  | 
| Enhanced WebAuthn |  + Windows client 5.29.0 or above<br />+ Mac client 5.29.0 or above  | 

## Get Started
<a name="webauthn_get_started"></a>
+ [Configure WebAuthn on Windows WorkSpaces](webauthn_windows.md)
+ [Configure WebAuthn on Linux WorkSpaces](webauthn_linux.md)