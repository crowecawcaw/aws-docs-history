# Add a SAML 2.0

identity provider

Your app users can sign in with a SAML 2.0 identity provider (IdP). You might choose
SAML 2.0 IdPs over social IdPs when your customers are the internal customers or linked
businesses of your organization. Where a social IdP permits all users to register for an
account, a SAML IdP is more likely to pair with a user directory that your organization
controls. Whether your users sign in directly or through a third party, all users have a
profile in the user pool. Skip this step if you don't want to add sign in through a SAML
identity provider.

For more information, see [Using SAML identity providers with a user
pool](cognito-user-pools-saml-idp.md "cognito-user-pools-saml-idp.md").

You must update your SAML identity provider and configure your user pool. For
information about how to add your user pool as a relying party or application for your SAML
2.0 identity provider, see the documentation for your SAML identity provider.

You must also provide an assertion consumer service (ACS) endpoint to your SAML identity
provider. Configure the following endpoint in your user pool domain for SAML 2.0 POST
binding in your SAML identity provider. For more information about user pool domains, see
[Configuring a user pool domain](cognito-user-pools-assign-domain.md "cognito-user-pools-assign-domain.md").

```
**https://`Your user pool domain`/saml2/idpresponse**
With an Amazon Cognito domain:
https://`<yourDomainPrefix>`.auth.`<region>`.amazoncognito.com/saml2/idpresponse
With a custom domain:
https://`Your custom domain`/saml2/idpresponse
```

You can find your domain prefix and the Region value for your user pool in the
**Domain** menu in the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").

For some SAML identity providers, you also need to provide the service provider (SP)
`urn`, also called the audience URI or SP entity ID, in the format:

```
`urn:amazon:cognito:sp:`<yourUserPoolID>``
```

You can find your user pool ID in the **Overview** dashboard for your
user pool in the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").

You should also configure your SAML identity provider to provide attribute values for
any attributes that are required in your user pool. Typically, `email` is a
required attribute for user pools. In that case, the SAML identity provider should provide
an `email` value (claim) in the SAML assertion.

Amazon Cognito user pools support SAML 2.0 federation with post-binding endpoints. This
eliminates the need for your app to retrieve or parse SAML assertion responses because the
user pool directly receives the SAML response from your identity provider through a user
agent.

###### To configure a SAML 2.0 identity provider in your user pool

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). If
   prompted, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list, or [create a user
   pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md").
4. Choose the **Social and external providers** menu. Locate
   **Federated sign-in** and select **Add an identity
   provider**.
5. Choose a **SAML** social identity provider.
6. Enter **Identifiers** separated by commas. An identifier tells
   Amazon Cognito it should check the email address that a user enters when they sign in. Then it
   directs them to the provider that corresponds to their domain.
7. Choose **Add sign-out flow** if you want Amazon Cognito to send signed
   sign-out requests to your provider when a user logs out. You must configure your SAML
   2.0 identity provider to send sign-out responses to the
   `https://`<your Amazon Cognito domain>`/saml2/logout`
   endpoint that is created when you configure managed login. The `saml2/logout`
   endpoint uses the POST binding.

###### Note

If this option is selected and your SAML identity provider expects a signed logout
request, you will also need to configure the signing certificate that is provided by
Amazon Cognito with your SAML IdP.

The SAML IdP will process the signed logout request and will log out your user
from the Amazon Cognito session. 8. Choose a **Metadata document source**. If your identity provider
offers SAML metadata at a public URL, you can choose **Metadata document
URL** and enter that public URL. Otherwise, choose **Upload metadata
document** and select a metadata file you downloaded from your provider
earlier.

###### Note

We recommend that you enter a metadata document URL if your provider has a public
endpoint, rather than uploading a file. This allows Amazon Cognito to refresh the metadata
automatically. Typically, metadata refresh happens every 6 hours or before the
metadata expires, whichever is earlier. 9. Select **Map attributes between your SAML provider and your app**
to map SAML provider attributes to the user profile in your user pool. Include your user
pool required attributes in your attribute map.

For example, when you choose the **User pool attribute**
`email`, enter the SAML attribute name as it appears in the SAML assertion
from your identity provider. Your identity provider might offer sample SAML assertions
for reference. Some identity providers use simple names, such as `email`,
while others use URL-formatted attribute names, such as the following example:

```
`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`
```

10. Choose **Create**.
