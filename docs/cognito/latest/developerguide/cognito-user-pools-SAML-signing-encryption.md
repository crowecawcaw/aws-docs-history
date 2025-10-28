# SAML signing and

encryption

SAML 2.0 sign-in is built around the user of an application as a bearer of
requests and responses in their authentication flow. You might want to ensure that
users aren't reading or modifying these SAML documents in transit. To accomplish
this, add SAML signing and encryption to the SAML identity providers (IdPs) in your
user pool. With SAML signing, your user pools adds a signature to SAML sign-in and
sign-out requests. With your user pool public key, your IdP can verify that it's
receiving unmodified SAML requests. Then, when your IdP responds and passes SAML
assertions to users' browser sessions, the IdP can encrypt that response so that the
user can't inspect their own attributes and entitlements.

With SAML signing and encryption, all cryptographic operations during user pool
SAML operations must generate signatures and ciphertext with user-pool-provided keys
that Amazon Cognito generates. Currently, you can't configure a user pool to sign requests or
accept encrypted assertions with an external key.

###### Note

Your user pool certificates are valid for 10 years. Once per year, Amazon Cognito
generates new signing and encryption certificates for your user pool. Amazon Cognito
returns the most recent certificate when you request the signing certificate,
and signs requests with the most recent signing certificate. Your IdP can
encrypt SAML assertions with any user pool encryption certificate that isn’t
expired. Your previous certificates continue to be valid for their entire
duration and the public key doesn't change between certificates. As a best
practice, update the certificate in your provider configuration annually.

###### Topics

- [Accepting encrypted SAML
  responses from your IdP](#cognito-user-pools-SAML-encryption "#cognito-user-pools-SAML-encryption")
- [Signing SAML requests](#cognito-user-pools-SAML-signing "#cognito-user-pools-SAML-signing")

## Accepting encrypted SAML

responses from your IdP

Amazon Cognito and your IdP can establish confidentiality in SAML responses when users
sign in and sign out. Amazon Cognito assigns a public-private RSA key pair and a
certificate to each external SAML provider that you configure in your user pool.
When you enable response encryption for your user pool SAML provider, you must
upload your certificate to an IdP that supports encrypted SAML responses. Your
user pool connection to your SAML IdP isn’t functional before your IdP begins to
encrypt all SAML assertions with the provided key.

The following is an overview of the flow of an encrypted SAML sign-in.

1. Your user starts sign-in and chooses their SAML IdP.
2. Your user pool [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md") redirects your user to their SAML
   IdP with a SAML sign-in request. Your user pool can optionally accompany
   this request with a signature that enables integrity verification by the
   IdP. When you want to sign SAML requests, you must configure your IdP to
   accept requests that your user pool has signed with the public key in
   the signing certificate.
3. The SAML IdP signs in your user and generates a SAML response. The IdP
   encrypts the response with the public key and redirects your user to
   your user pool `/saml2/idpresponse` endpoint. The IdP must
   encrypt the response as defined by the SAML 2.0 specification. For more
   information, see `Element <EncryptedAssertion>` in [Assertions and Protocols for the OASIS Security Assertion Markup
   Language (SAML) V2.0](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf "https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf").
4. Your user pool decrypts the ciphertext in the SAML response with the
   private key and signs in your user.

###### Important

When you enable response encryption for a SAML IdP in your user pool, your
IdP must encrypt all responses with a public key that's specific to the
provider. Amazon Cognito doesn't accept unencrypted SAML responses from a SAML
external IdP that you configure to support encryption.

Any external SAML IdP in your user pool can support response encryption, and
each IdP receives its own key pair.

AWS Management Console

###### To configure SAML response encryption

1. Create a [user pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md"), [app client](cognito-user-pools-configuring-app-integration.md "cognito-user-pools-configuring-app-integration.md"), and SAML IdP.
2. When you create or edit your SAML identity provider, under
   **Sign requests and encrypt
   responses**, check the box with the title
   **Require encrypted SAML assertions from this
   provider**.
3. From the **Social and external
   providers** menu of your user pool, select your
   SAML IdP and choose **View encryption
   certificate**.
4. Choose **Download as .crt** and provide
   the downloaded file to your SAML IdP. Configure your SAML
   IdP to encrypt SAML responses with the key in the
   certificate.

API/CLI
**To configure SAML response
encryption**

Configure response encryption with the
`EncryptedResponses` parameter of a [CreateIdentityProvider](../../../cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.md") or [UpdateIdentityProvider](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateIdentityProvider.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateIdentityProvider.md") API request. The following is an
example `ProviderDetails` of an IdP that supports request
signing.

```
"ProviderDetails": {
      "MetadataURL" : "`https://myidp.example.com/saml/metadata`",
      "IDPSignout" : "`true`",
      "RequestSigningAlgorithm" : "rsa-sha256",
      **"EncryptedResponses" : "true",**
      "IDPInit" : "`true`"
}
```

To get the encryption certificate from your user pool, make a
[DescribeIdentityProvider](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeIdentityProvider.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeIdentityProvider.md") API request and retrieve the
value of `ActiveEncryptionCertificate` in the response
parameter `ProviderDetails`. Save this certificate and
provide it to your IdP as the encryption certificate for sign-in
requests from your user pool.

## Signing SAML requests

The ability to prove the integrity of SAML 2.0 requests to your IdP is a
security advantage of Amazon Cognito SP-initiated SAML sign-in. Each user pool with a
domain receives a user pool X.509 signing certificate. With the public key in
this certificate, user pools apply a cryptographic signature to the _sign-out requests_ that your user pool generates
when your users select a SAML IdP. You can optionally configure your app client
to sign SAML _sign-in requests_. When you sign
your SAML requests, your IdP can check that the signature in the XML metadata of
your requests matches the public key in the user pool certificate that you
provide.

AWS Management Console

###### To configure SAML request signing

1. Create a [user pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md"), [app client](cognito-user-pools-configuring-app-integration.md "cognito-user-pools-configuring-app-integration.md"), and SAML IdP.
2. When you create or edit your SAML identity provider, under
   **Sign requests and encrypt
   responses**, check the box with the title
   **Sign SAML requests to this
   provider**.
3. From the **Social and external
   providers** menu of your user pool, choose
   **View signing certificate**.
4. Choose **Download as .crt** and provide
   the downloaded file to your SAML IdP. Configure your SAML
   IdP to verify the signature of incoming SAML
   requests.

API/CLI
**To configure SAML request
signing**

Configure request signing with the
`RequestSigningAlgorithm` parameter of a [CreateIdentityProvider](../../../cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.md") or [UpdateIdentityProvider](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateIdentityProvider.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateIdentityProvider.md") API request. The following is an
example `ProviderDetails` of an IdP that supports request
signing.

```
"ProviderDetails": {
      "MetadataURL" : "`https://myidp.example.com/saml/metadata`",
      "IDPSignout" : "true",
      **"RequestSigningAlgorithm" : "rsa-sha256"**,
      "EncryptedResponses" : "true",
      "IDPInit" : "true"
}
```
