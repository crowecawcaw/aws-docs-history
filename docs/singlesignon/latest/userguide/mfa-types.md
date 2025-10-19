# Available MFA types for IAM Identity Center

Multi-factor authentication (MFA) is a simple and effective mechanism to enhance the
 security of your users. A user’s first factor — their password — is a secret that they
 memorize, also known as a knowledge factor. Other factors can be possession factors
 (something you have, such as a security key) or inherence factors (something you are,
 such as a biometric scan). We strongly recommend that you configure MFA to add an
 additional layer of security to your account. 

IAM Identity Center MFA supports the following device types. All MFA types are supported for both
 browser-based console access as well as using the AWS CLI v2 with IAM Identity Center. 


* [FIDO2 authenticators](#mfa-types-fido2 "#mfa-types-fido2"), including
 built-in authenticators and security keys
* [Virtual authenticator apps](#mfa-types-apps "#mfa-types-apps")
* Your own [RADIUS MFA](#about-radius "#about-radius")
 implementation connected through AWS Managed Microsoft AD
A user can have up to **eight** MFA devices, which
 include up to two virtual authenticator apps and six FIDO authenticators, registered to
 one AWS account. You can also configure MFA settings to require MFA whenever they
 attempt to sign-in from a new device or browser, or when signing in from an unknown IP
 address. For more information about how to configure MFA settings for your users, see
 [Choose MFA types for user
 authentication](how-to-configure-mfa-types.md "how-to-configure-mfa-types.md") and [Configure MFA device
 enforcement](how-to-configure-mfa-device-enforcement.md "how-to-configure-mfa-device-enforcement.md").


## FIDO2 authenticators


[FIDO2](https://fidoalliance.org/fido2/ "https://fidoalliance.org/fido2/") is a standard that
 includes CTAP2 and [WebAuthn](https://www.w3.org/TR/webauthn-2/ "https://www.w3.org/TR/webauthn-2/")
 and is based on public key cryptography. FIDO credentials are phishing-resistant
 because they are unique to the website that the credentials were created such as
 AWS.


AWS supports the two most common form factors for FIDO authenticators: built-in
 authenticators and security keys. See below for more information about the most
 common types of FIDO authenticators.


###### Topics

* [Built-in authenticators](#mfa-types-built-in-auth "#mfa-types-built-in-auth")
* [Security keys](#mfa-types-keys "#mfa-types-keys")
* [Password managers, passkey providers, and
 other FIDO authenticators](#mfa-types-other "#mfa-types-other")

### Built-in authenticators


Many modern computers and mobile phones have built-in authenticators, such as
 TouchID on Macbook or a Windows Hello-compatible camera. If your device has a
 FIDO-compatible built-in authenticator, you can use your fingerprint, face, or
 device pin as a second factor. 


### Security keys


Security keys are FIDO-compatible external hardware authenticators that you
 can purchase and connect to your device through USB, BLE, or NFC. When you’re
 prompted for MFA, you simply complete a gesture with the key’s sensor. Some
 examples of security keys include YubiKeys and Feitian keys, and the most common
 security keys create device-bound FIDO credentials. For a list of all
 FIDO-certified security keys, see [FIDO
 Certified Products](https://fidoalliance.org/certification/fido-certified-products/ "https://fidoalliance.org/certification/fido-certified-products/").


### Password managers, passkey providers, and
 other FIDO authenticators


Multiple third party providers support FIDO authentication in mobile
 applications, as features in password managers, smart cards with a FIDO mode,
 and other form factors. These FIDO-compatible devices can work with IAM Identity Center, but
 we recommend that you test a FIDO authenticator yourself before enabling this
 option for MFA.


###### Note

Some FIDO authenticators can create discoverable FIDO credentials known as
 passkeys. Passkeys may be bound to the device that creates them, or they may be
 syncable and backed up to a cloud. For example, you can register a passkey using
 Apple Touch ID on a supported Macbook, and then log in to a site from a Windows
 laptop using Google Chrome with your passkey in iCloud by following the
 on-screen prompts at sign-in. For more information about which devices support
 syncable passkeys and current passkey interoperability between operating systems
 and browsers, see [Device
 Support](https://passkeys.dev/device-support/ "https://passkeys.dev/device-support/") at [passkeys.dev](https://passkeys.dev/ "https://passkeys.dev/"),
 a resource maintained by the FIDO Alliance And World Wide Web Consortium (W3C).
 


## Virtual authenticator apps


Authenticator apps are essentially one-time password (OTP)–based third
 party-authenticators. You can use an authenticator application installed on your
 mobile device or tablet as an authorized MFA device. The third-party authenticator
 application must be compliant with RFC 6238, which is a standards-based time-based
 one-time password (TOTP) algorithm capable of generating six-digit authentication
 codes. 


When prompted for MFA, users must enter a valid code from their authenticator app
 within the input box presented. Each MFA device assigned to a user must be unique.
 Two authenticator apps can be registered for any given user.


### Tested authenticator apps


Any TOTP-compliant application will work with IAM Identity Center MFA. The following table
 lists well-known third-party authenticator apps to choose from.




| Operating system | Tested authenticator app |
| --- | --- |
| Android | [Authy](https://play.google.com/store/apps/details?id=com.authy.authy "https://play.google.com/store/apps/details?id=com.authy.authy"), [Duo Mobile](https://play.google.com/store/apps/details?id=com.duosecurity.duomobile "https://play.google.com/store/apps/details?id=com.duosecurity.duomobile"), [Microsoft Authenticator](https://play.google.com/store/apps/details?id=com.azure.authenticator "https://play.google.com/store/apps/details?id=com.azure.authenticator"), [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2 "https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2") |
| iOS | [Authy](https://apps.apple.com/us/app/authy/id494168017 "https://apps.apple.com/us/app/authy/id494168017"), [Duo Mobile](https://apps.apple.com/us/app/duo-mobile/id422663827 "https://apps.apple.com/us/app/duo-mobile/id422663827"), [Microsoft Authenticator](https://apps.apple.com/us/app/microsoft-authenticator/id983156458 "https://apps.apple.com/us/app/microsoft-authenticator/id983156458"), [Google Authenticator](https://apps.apple.com/us/app/google-authenticator/id388497605 "https://apps.apple.com/us/app/google-authenticator/id388497605") | ## RADIUS MFA [Remote Authentication Dial-In User Service (RADIUS)](https://en.wikipedia.org/wiki/RADIUS "https://en.wikipedia.org/wiki/RADIUS") is an industry-standard client-server protocol that provides authentication, authorization, and accounting management so users can connect to network services. AWS Directory Service includes a RADIUS client that connects to the RADIUS server upon which you have implemented your MFA solution. For more information, see [Enable Multi-Factor Authentication for AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html "https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html"). You can use either RADIUS MFA or MFA in IAM Identity Center for user sign-ins to the user portal, but not both. MFA in IAM Identity Center is an alternative to RADIUS MFA in cases where you want AWS native two-factor authentication for access to the portal. When you enable MFA in IAM Identity Center, your users need an MFA device to sign in to the AWS access portal. If you had previously used RADIUS MFA, enabling MFA in IAM Identity Center effectively overrides RADIUS MFA for users who sign in to the AWS access portal. However, RADIUS MFA continues to challenge users when they sign in to all other applications that work with AWS Directory Service, such as Amazon RDS for SQL Server. If your MFA is **Disabled** on the IAM Identity Center console and you have configured RADIUS MFA with AWS Directory Service, RADIUS MFA governs AWS access portal sign-in. This means that IAM Identity Center falls back to RADIUS MFA configuration if MFA is disabled.
