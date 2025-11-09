# Provide Your Users with Access to WorkSpaces Applications

Users can access WorkSpaces Applications streaming sessions by using either a web browser or the WorkSpaces Applications client on a supported device.

Depending on your organizational requirements, you can enable user access to WorkSpaces Applications streaming sessions by: Setting up identity federation using SAML 2.0, using an WorkSpaces Applications user pool, or creating a streaming URL. Following are recommendations for choosing a connection method.

- [SAML 2.0](external-identity-providers-setting-up-saml.md "external-identity-providers-setting-up-saml.md"): Use
  this connection method when you have an identity provider that manages your users
  and supports SAML 2.0 federation.

###### Note

This connection method is required when your WorkSpaces Applications fleet is joined to a
Microsoft Active Directory domain.

- [WorkSpaces Applications user pools](user-pool.md "user-pool.md"): Use this connection method
  when:
  - You want to set up a Proof-of-Concept (POC) quickly before you configure
    your SAML 2.0-compliant identity provider.
  - You don't have a SAML 2.0-compliant identity provider.
  - You want to manage users directly within the WorkSpaces Applications console.

- [Streaming
  URL](use-client-start-streaming-session-streaming-URL.md "use-client-start-streaming-session-streaming-URL.md"): Use this connection method when you want to programmatically provide
  access to WorkSpaces Applications by using temporary URLs. We recommend this connection method when
  you want to use your existing identity provider to provide programmatic access to
  WorkSpaces Applications.
