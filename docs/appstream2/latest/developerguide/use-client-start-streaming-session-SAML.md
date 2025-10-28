# SAML 2.0

If you use external identity providers to federate your users to an AppStream 2.0 stack, you must create a
registry value to configure the AppStream 2.0 client with a prepopulated URL whenever the
client is launched. The URL must use a certificate that is trusted by the device.
The certificate must contain a Subject Alternative Name (SAN) that includes the
URL's domain name.

For more information, see:

- [Setting Up SAML](external-identity-providers-setting-up-saml.md "external-identity-providers-setting-up-saml.md")
- [Set the StartURL Registry Value for AppStream 2.0 Client Users](install-client-configure-settings.md#set-start-url-registry-value "install-client-configure-settings.md#set-start-url-registry-value")
