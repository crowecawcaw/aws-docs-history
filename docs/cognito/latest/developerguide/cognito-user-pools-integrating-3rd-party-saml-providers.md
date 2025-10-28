# Configuring your third-party SAML identity provider

When you want to add a SAML identity provider (IdP) to your user pool, you must
make some configuration updates in the management interface of your IdP. This
section describes how to format the values that you must provide to your IdP. You
can also learn about how to retrieve the static or active-URL metadata document that
identifies the IdP and its SAML claims to your user pool.

To configure third-party SAML 2.0 identity provider (IdP) solutions to work with
federation for Amazon Cognito user pools, you must configure your SAML IdP to redirect to the
following Assertion Consumer Service (ACS) URL:
`https://`mydomain.auth.us-east-1.amazoncognito.com`/saml2/idpresponse`.
If your user pool has an Amazon Cognito domain, you can find your user pool domain path in
the **Domain** menu of your user pool in the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").

Some SAML IdPs require that you provide the `urn`, also called the
audience URI or SP entity ID, in the form
`urn:amazon:cognito:sp:`us-east-1_EXAMPLE``.
You can find your user pool ID under **User pool overview** in the
Amazon Cognito console.

You must also configure your SAML IdP to provide values for any attributes that
you designated as _required attributes_ in your
user pool. Typically, `email` is a required attribute for user pools, in
which case the SAML IdP must provide some form of an `email` claim in
their SAML assertion, and you must map the claim to the attribute for that
provider.

The following configuration information for third-party SAML 2.0 IdP solutions is
a good place to start setting up federation with Amazon Cognito user pools. For the most
current information, consult your provider's documentation directly.

To sign SAML requests, you must configure your IdP to trust requests signed by
your user pool signing certificate. To accept encrypted SAML responses, you must
configure your IdP to encrypt _all_ SAML responses
to your user pool. Your provider will have documentation about configuring these
features. For an example from Microsoft, see [Configure Microsoft Entra SAML token encryption](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/howto-saml-token-encryption "https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/howto-saml-token-encryption").

###### Note

Amazon Cognito only requires your identity provider metadata document. Your provider
might also offer customized configuration information for SAML 2.0 federation
with IAM or AWS IAM Identity Center. To learn how to set up Amazon Cognito integration, look for
general directions for retrieving the metadata document and manage the rest of
the configuration in your user pool.

| Solution                     | More information                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Microsoft Entra ID           | [Federation Metadata](https://learn.microsoft.com/en-us/entra/identity-platform/federation-metadata "https://learn.microsoft.com/en-us/entra/identity-platform/federation-metadata")                                                                                                                                                                               |
| Okta                         | [How to Download the IdP Metadata and SAML Signing Certificates for a SAML App Integration](https://support.okta.com/help/s/article/Location-to-download-Okta-IDP-XML-metadata-for-a-SAML-app-in-the-new-Admin-User-Interface "https://support.okta.com/help/s/article/Location-to-download-Okta-IDP-XML-metadata-for-a-SAML-app-in-the-new-Admin-User-Interface") |
| Auth0                        | [Configure Auth0 as SAML Identity Provider](https://auth0.com/docs/authenticate/protocols/saml/saml-sso-integrations/configure-auth0-saml-identity-provider "https://auth0.com/docs/authenticate/protocols/saml/saml-sso-integrations/configure-auth0-saml-identity-provider")                                                                                     |
| Ping Identity (PingFederate) | [Exporting SAML metadata from PingFederate](https://docs.pingidentity.com/integrations/contentful/configuring_single_sign-on/pf_contentful_integration_exporting_saml_metadata_from_pf.html "https://docs.pingidentity.com/integrations/contentful/configuring_single_sign-on/pf_contentful_integration_exporting_saml_metadata_from_pf.html")                     |
| JumpCloud                    | [SAML Configuration Notes](https://jumpcloud.com/support/saml-configuration-notes "https://jumpcloud.com/support/saml-configuration-notes")                                                                                                                                                                                                                        |
| SecureAuth                   | [SAML application integration](https://docs.secureauth.com/2104/en/saml-application-integration.html "https://docs.secureauth.com/2104/en/saml-application-integration.html")                                                                                                                                                                                      |
