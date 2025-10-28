# Things to know about

SAML IdPs in Amazon Cognito user pools

Implementation of a SAML 2.0 IdP comes with some requirements and restrictions.
Refer to this section when you're implementing your IdP. You'll also find
information that's useful for troubleshooting errors during SAML federation with a
user pool.

**Amazon Cognito processes SAML assertions for you**

Amazon Cognito user pools support SAML 2.0 federation with POST-binding endpoints. This
eliminates the need for your app to retrieve or parse SAML assertion
responses, because the user pool directly receives the SAML response
from your IdP through a user agent. Your user pool acts as a service
provider (SP) on behalf of your application. Amazon Cognito supports SP-initiated
and IdP-initiated single sign-on (SSO) as described in sections 5.1.2
and 5.1.4 of the [SAML V2.0 Technical Overview](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0-cd-02.html "http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0-cd-02.html").

**Provide a valid IdP signing certificate**

The signing certificate in your SAML provider metadata must not be
expired when you configure the SAML IdP in your user
pool.

**User pools support multiple signing certificates**

When your SAML IdP includes more than one signing certificate in SAML
metadata, at sign-in your user pool determines that the SAML assertion
is valid if it matches any certificate in the SAML metadata. Each
signing certificate must be no longer than 4,096 characters in
length.

**Maintain the relay state parameter**

Amazon Cognito and your SAML IdP maintain session information with a
`relayState` parameter.

1. Amazon Cognito supports `relayState` values greater than 80
   bytes. While SAML specifications state that the
   `relayState` value "must not exceed 80 bytes in
   length”, current industry practice often deviates from this
   behavior. As a consequence, rejecting `relayState`
   values greater than 80 bytes will break many standard SAML
   provider integrations.
2. The `relayState` token is an opaque reference to
   state information maintained by Amazon Cognito. Amazon Cognito doesn't guarantee
   the contents of the `relayState` parameter. Don't
   parse its contents such that your app depends on the result. For
   more information, see the [SAML 2.0 specification](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html "http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html").

**Identify the ACS endpoint**

Your SAML identity provider requires that you set an assertion
consumer endpoint. Your IdP redirects your users to this endpoint with
their SAML assertion. Configure the following endpoint in your user pool
domain for SAML 2.0 POST binding in your SAML identity provider.

```
**https://`Your user pool domain`/saml2/idpresponse**
With an Amazon Cognito domain:
https://`mydomain.auth.us-east-1.amazoncognito.com`/saml2/idpresponse
With a custom domain:
https://`auth.example.com`/saml2/idpresponse
```

See [Configuring a user pool domain](cognito-user-pools-assign-domain.md "cognito-user-pools-assign-domain.md") for more
information about user pool domains.

**No replayed assertions**

You can't repeat, or _replay_, a SAML
assertion to your Amazon Cognito `saml2/idpresponse` endpoint. A
replayed SAML assertion has an assertion ID that duplicates the ID of an
earlier IdP response.

**User pool ID is SP entity ID**

You must provide your IdP with your user pool ID in the service
provider (SP) `urn`, also called the _audience URI_ or _SP entity
ID_. The audience URI for your user pool has the following
format.

```
urn:amazon:cognito:sp:`us-east-1_EXAMPLE`
```

You can find your user pool ID under **User pool
overview** in the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").

**Map all required attributes**

Configure your SAML IdP to provide values for any attributes that you
set as required in your user pool. For example, `email` is a
common required attribute for user pools. Before your users can sign in,
your SAML IdP assertions must include a claim that you map to the
**User pool attribute**
`email`. For more information about attribute mapping, see
[Mapping IdP attributes
to profiles and tokens](cognito-user-pools-specifying-attribute-mapping.md "cognito-user-pools-specifying-attribute-mapping.md").

**Assertion format has specific requirements**

Your SAML IdP must include the following claims in the SAML
assertion.

- A `NameID` claim. Amazon Cognito associates a SAML assertion
  with the destination user by `NameID`. If
  `NameID` changes, Amazon Cognito considers the assertion
  to be for a new user. The attribute that you set to
  `NameID` in your IdP configuration must have a
  persistent value. To assign SAML users to a consistent user
  profile in your user pool, assign your `NameID` claim
  from an attribute with a value that doesn't change.

```
<saml2:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:persistent">
  carlos
</saml2:NameID>
```

A `Format` in your IdP `NameID` claim of
`urn:oasis:names:tc:SAML:1.1:nameid-format:persistent`
indicates that your IdP is passing an unchanging value. Amazon Cognito
doesn't require this format declaration, and assigns a format of
`urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`
if your IdP doesn't specify a format of the `NameID`
claim. This behavior complies with section 2.2.2 _Complex Type NameIDType_, of [the SAML 2.0 specification](https://groups.oasis-open.org/higherlogic/ws/public/download/35711/sstc-saml-core-errata-2.0-wd-06-diff.pdf/latest "https://groups.oasis-open.org/higherlogic/ws/public/download/35711/sstc-saml-core-errata-2.0-wd-06-diff.pdf/latest").

- An `AudienceRestriction` claim with an
  `Audience` value that sets your user pool SP
  entity ID as the target of the response.

```
<saml:AudienceRestriction>
  <saml:Audience> urn:amazon:cognito:sp:`us-east-1_EXAMPLE`
</saml:AudienceRestriction>
```

- For SP-initiated single sign-on, a `Response`
  element with an `InResponseTo` value of the original
  SAML request ID.

```
<saml2p:Response Destination="https://`mydomain.auth.us-east-1.amazoncognito.com`/saml2/idpresponse" ID="`id123`" InResponseTo="_dd0a3436-bc64-4679-a0c2-cb4454f04184" IssueInstant="`Date-time stamp`" Version="2.0" xmlns:saml2p="urn:oasis:names:tc:SAML:2.0:protocol" xmlns:xs="http://www.w3.org/2001/XMLSchema">
```

###### Note

IdP-initiated SAML assertions must _not_ contain an `InResponseTo`
value.

- A `SubjectConfirmationData` element with a
  `Recipient` value of your user pool
  `saml2/idpresponse` endpoint and, for
  SP-initiated SAML, an `InResponseTo` value that
  matches the original SAML request ID.

```
<saml2:SubjectConfirmationData InResponseTo="_dd0a3436-bc64-4679-a0c2-cb4454f04184" NotOnOrAfter="`Date-time stamp`" Recipient="https://`mydomain.auth.us-east-1.amazoncognito.com`/saml2/idpresponse"/>
```

**SP-initiated sign-in requests**

When the [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md") redirects your user to your
IdP sign-in page, Amazon Cognito includes a _SAML
request_ in a URL parameter of the `HTTP GET`
request. A SAML request contains information about your user pool,
including your ACS endpoint. You can optionally apply a cryptographic
signature to these requests.

**Sign requests and encrypt responses**

Every user pool with a SAML provider generates an asymmetric key pair
and _signing certificate_ for a digital
signature that Amazon Cognito assigns to SAML requests. Every external SAML IdP
that you configure to support encrypted SAML response causes Amazon Cognito to
generate a new key pair and _encryption
certificate_ for that provider. To view and download the
certificates with the public key, choose your IdP in the
**Social and external providers** menu in the Amazon Cognito
console.

To establish trust with SAML requests from your user pool, provide
your IdP with a copy of your user pool SAML 2.0 signing certificate.
Your IdP might ignore SAML requests that your user pool signed if you
don’t configure the IdP to accept signed requests.

1. Amazon Cognito applies a digital signature to SAML requests that your
   user passes to your IdP. Your user pool signs all single logout
   (SLO) requests, and you can configure your user pool to sign
   single sign-on (SSO) requests for any SAML external IdP. When
   you provide a copy of the certificate, your IdP can verify the
   integrity of your users' SAML requests.
2. Your SAML IdP can encrypt SAML responses with the encryption
   certificate. When you configure an IdP with SAML encryption,
   your IdP must only send encrypted responses.

**Encode non-alphanumeric characters**

Amazon Cognito doesn't accept 4-byte UTF-8 characters like 😐 or
𠮷 that your IdP passes as an attribute value. You
can encode the character to Base64, pass it as text, and then decode it
in your app.

In the following example, the attribute claim will not be
accepted:

```
<saml2:Attribute Name="Name" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
  <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xsd:string">😐</saml2:AttributeValue>
</saml2:Attribute>
```

In contrast to the preceding example, the following attribute claim
will be accepted:

```
<saml2:Attribute Name="Name" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
  <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xsd:string">8J+YkA==</saml2:AttributeValue>
</saml2:Attribute>
```

**Metadata endpoint must have valid transport-layer security**

If you see `InvalidParameterException` while creating a
SAML IdP with an HTTPS metadata endpoint URL, for example, "Error
retrieving metadata from `<metadata
 endpoint>`," make sure that the metadata endpoint
has SSL correctly set up and that there is a valid SSL certificate
associated with it. For more information about validating certificates,
see [What Is An
SSL/TLS Certificate?](https://aws.amazon.com/what-is/ssl-certificate/ "https://aws.amazon.com/what-is/ssl-certificate/").

**Metadata endpoint must be on standard TCP port for HTTP or HTTPS**

Amazon Cognito only accepts metadata URLs for SAML providers on the standard
TCP ports 80 for HTTP and 443 for HTTPS. As a security best practice,
host SAML metadata at a TLS-encrypted URL with the
`https://` prefix. Enter metadata URLs in the format
`http://www.example.com/saml2/metadata.xml`
or
`https://www.example.com/saml2/metadata.xml`.
The Amazon Cognito console accepts metadata URLs only with the
`https://` prefix. You can also configure IdP metadata
with [CreateIdentityProvider](../../../cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.md") and [UpdateIdentityProvider](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateIdentityProvider.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateIdentityProvider.md").

**App clients with IdP-initiated SAML can only sign in with SAML**

When you activate support for a SAML 2.0 IdP that supports
IdP-initiated sign in an app client, you can only add other SAML 2.0
IdPs to that app client. You're prevented from adding the user directory
in the user pool _and_ all non-SAML
external identity providers to an app client configured in this
way.

**Logout responses must use POST binding**

The `/saml2/logout` endpoint accepts
`LogoutResponse` as `HTTP POST` requests. User
pools don't accept logout responses with `HTTP GET`
binding.

**Metadata Signing Certificate Rotation**

Amazon Cognito caches SAML metadata for up to six hours when you provide
metadata with a URL. When performing any metadata signing certificate
rotation, configure your metadata source to publish _both_ the original and new certificates for
at least six hours. When Amazon Cognito refreshes the cache from the metadata
URL, it treats each certificate as valid and your SAML IdP can start
signing SAML assertions with the new certificate. After this period has
elapsed, you can remove the original certificate from the published
metadata.
