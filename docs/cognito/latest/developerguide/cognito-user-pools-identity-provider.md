# Configuring identity providers for

your user pool

With user pools, you can implement sign-in through a variety of external identity
providers (IdPs). This section of the guide has instructions for setting up these identity
providers with your user pool in the Amazon Cognito console. Alternatively, you can use the user
pools API and an AWS SDK to programmatically add user pool identity providers. For more
information, see [CreateIdentityProvider](../../../cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.md").

The supported identity provider options include social providers like Facebook, Google,
and Amazon, as well as OpenID Connect (OIDC) and SAML 2.0 providers. Before you get started,
set yourself up with administrative credentials for your IdP. For each type of provider,
you'll need to register your application, obtain the necessary credentials, and then
configure the provider details in your user pool. Your users can then sign up and sign in to
your application with their existing accounts from the connected identity providers.

The **Social and external providers** menu under
**Authentication** adds and updates user pool IdPs. For more
information, see [User pool sign-in with third party
identity providers](cognito-user-pools-identity-federation.md "cognito-user-pools-identity-federation.md").

###### Topics

- [Set up user sign-in with a social
  IdP](#cognito-user-pools-facebook-provider "#cognito-user-pools-facebook-provider")
- [Set up user sign-in with an OIDC
  IdP](#cognito-user-pools-oidc-providers "#cognito-user-pools-oidc-providers")
- [Set up user sign-in with a SAML
  IdP](#cognito-user-pools-saml-providers "#cognito-user-pools-saml-providers")

## Set up user sign-in with a social

IdP

You can use federation to integrate Amazon Cognito user pools with social identity providers such as
Facebook, Google, and Login with Amazon.

To add a social identity provider, you first create a developer account with the
identity provider. After you have your developer account, register your app with the
identity provider. The identity provider creates an app ID and an app secret for your
app, and you configure those values in your Amazon Cognito user pools.

- [Google identity
  platform](https://developers.google.com/identity/ "https://developers.google.com/identity/")
- [Facebook for
  developers](https://developers.facebook.com/docs/facebook-login "https://developers.facebook.com/docs/facebook-login")
- [Login with
  Amazon](https://developer.amazon.com/login-with-amazon "https://developer.amazon.com/login-with-amazon")
- [Sign in with
  Apple](https://developer.apple.com/sign-in-with-apple/ "https://developer.apple.com/sign-in-with-apple/")

###### To integrate user sign-in with a social IdP

1. Sign in to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). If prompted, enter your AWS credentials.
2. In the navigation pane, choose **User Pools**, and choose the
   user pool you want to edit.
3. Choose the **Social and external providers** menu.
4. Choose **Add an identity provider**, or choose the
   **Facebook**, **Google**,
   **Amazon**, or **Apple** identity provider
   you have configured, locate **Identity provider information**,
   and choose **Edit**. For more information about adding a social
   identity provider, see [Using social identity providers with a
   user pool](cognito-user-pools-social-idp.md "cognito-user-pools-social-idp.md").
5. Enter your social identity provider's information by completing one of the
   following steps, based on your choice of IdP:

**Facebook, Google, and Login with Amazon**

Enter the app ID and app secret that you received when you created
your client app.

**Sign In with Apple**

Enter the service ID that you provided to Apple, and the team ID,
key ID, and private key you received when you created your app
client. 6. For **Authorized scopes**, enter the names of the social
identity provider scopes that you want to map to user pool attributes. Scopes
define which user attributes, such as name and email, that you want to access
with your app. When entering scopes, use the following guidelines based on your
choice of IdP:

    * **Facebook** — Separate scopes
     with commas. For example:


    `public_profile, email`
    * **Google, Login with Amazon, and Sign In with
     Apple** — Separate scopes with spaces. For
     example:




    	+ **Google:**
    	`profile email openid`
    	+ **Login with Amazon:**
    	`profile postal_code`
    	+ **Sign In with Apple:**
    	`name email`


    	###### Note

    	For Sign In with Apple (console), use the check boxes to
    	 choose scopes.

7. Choose **Save changes**.
8. From the **App clients** menu,
   choose
   an app client from the list and then select
   **Edit**. Add the new social identity
   provider to the app client under **Identity providers**.
9. Choose **Save changes**.

For more information on social IdPs, see [Using social identity providers with a
user pool](cognito-user-pools-social-idp.md "cognito-user-pools-social-idp.md").

## Set up user sign-in with an OIDC

IdP

You can integrate user sign-in with an OpenID Connect (OIDC) identity provider (IdP)
such as Salesforce or Ping Identity.

###### To add an OIDC provider to a user pool

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
   If prompted, enter your AWS credentials.
2. Choose **User Pools** from the navigation menu.
3. Choose an existing user pool from the list, or [create a user
   pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md").
4. Choose the **Social and external providers** menu and select
   **Add an identity provider**.
5. Choose an **OpenID Connect** identity provider.
6. Enter a unique name into **Provider name**.
7. Enter the client ID that you received from your provider into **Client
   ID**.
8. Enter the client secret that you received from your provider into
   **Client secret**.
9. Enter **Authorized scopes** for this provider. Scopes define
   which groups of user attributes (such as `name` and
   `email`) that your application will request from your provider.
   Scopes must be separated by spaces, following the [OAuth 2.0](https://tools.ietf.org/html/rfc6749#section-3.3 "https://tools.ietf.org/html/rfc6749#section-3.3")
   specification.

Your user must consent to provide these attributes to your application. 10. Choose an **Attribute request method** to provide Amazon Cognito with
the HTTP method (either GET or POST) that Amazon Cognito uses to fetch the details of the
user from the **userInfo** endpoint operated by your
provider. 11. Choose a **Setup method** to retrieve OpenID Connect
endpoints either by **Auto fill through issuer URL** or
**Manual input**. Use **Auto fill through issuer
URL** when your provider has a public
`.well-known/openid-configuration` endpoint where Amazon Cognito can
retrieve the URLs of the `authorization`, `token`,
`userInfo`, and `jwks_uri` endpoints. 12. Enter the issuer URL or `authorization`, `token`,
`userInfo`, and `jwks_uri` endpoint URLs from your
IdP.

###### Note

You can use only port numbers 443 and 80 with discovery, auto-filled, and
manually entered URLs. User logins fail if your OIDC provider uses any
nonstandard TCP ports.

The issuer URL must start with `https://`, and must not end
with a `/` character. For example, Salesforce uses this
URL:

`https://login.salesforce.com`

The `openid-configuration` document associated with your issuer
URL must provide HTTPS URLs for the following values:
`authorization_endpoint`, `token_endpoint`,
`userinfo_endpoint`, and `jwks_uri`. Similarly,
when you choose **Manual input**, you can only enter HTTPS
URLs. 13. The OIDC claim **sub** is mapped to the user pool attribute
**Username** by default. You can map other OIDC [claims](https://openid.net/specs/openid-connect-basic-1_0.html#StandardClaims "https://openid.net/specs/openid-connect-basic-1_0.html#StandardClaims") to user pool attributes. Enter the OIDC claim, and select
the corresponding user pool attribute from the drop-down list. For example, the
claim **email** is often mapped to the user pool attribute
**Email**. 14. Map additional attributes from your identity provider to your user pool. For
more information, see [Specifying Identity Provider attribute mappings for your user
pool](cognito-user-pools-specifying-attribute-mapping.md "cognito-user-pools-specifying-attribute-mapping.md"). 15. Choose **Create**. 16. From the **App clients** menu, select an app client from the
list. To add the new SAML identity provider to the app client, navigate to the
**Login pages** tab and select **Edit** on
**Managed login pages configuration**. 17. Choose **Save changes**.

For more information on OIDC IdPs, see [Using OIDC identity providers with a user
pool](cognito-user-pools-oidc-idp.md "cognito-user-pools-oidc-idp.md").

## Set up user sign-in with a SAML

IdP

You can use federation for Amazon Cognito user pools to integrate with a SAML identity provider (IdP).
You supply a metadata document, either by uploading the file or by entering a metadata
document endpoint URL. For information about obtaining metadata documents for
third-party SAML IdPs, see [Configuring your third-party SAML identity provider](cognito-user-pools-integrating-3rd-party-saml-providers.md "cognito-user-pools-integrating-3rd-party-saml-providers.md").

###### To configure a SAML 2.0 identity provider in your user pool

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
   If prompted, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list, or [create a user
   pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md").
4. Choose the **Social and external provider** menu and select
   **Add an identity provider**.
5. Choose a **SAML** identity provider.
6. Enter **Identifiers** separated by commas. An identifier
   directs Amazon Cognito to check the user sign-in email address, and then direct the user
   to the provider that corresponds to their domain.
7. Choose **Add sign-out flow** if you want Amazon Cognito to send signed
   sign-out requests to your provider when a user logs out. Configure your SAML 2.0
   identity provider to send sign-out responses to the
   `https://`mydomain.auth.us-east-1.amazoncognito.com`/saml2/logout`
   endpoint that Amazon Cognito creates when you configure managed login. The
   `saml2/logout` endpoint uses POST binding.

###### Note

If you select this option and your SAML identity provider expects a signed
logout request, you also must configure the signing certificate provided by
Amazon Cognito with your SAML IdP.

The SAML IdP will process the signed logout request and logout your user
from the Amazon Cognito session. 8. Choose a **Metadata document source**. If your identity
provider offers SAML metadata at a public URL, you can choose **Metadata
document URL** and enter that public URL. Otherwise, choose
**Upload metadata document** and select a metadata file you
downloaded from your provider earlier.

###### Note

If your provider has a public endpoint, we recommend that you enter a
metadata document URL, rather than uploading a file. If you use the URL,
Amazon Cognito refreshes metadata automatically. Typically, metadata refresh happens
every 6 hours or before the metadata expires, whichever is earlier. 9. **Map attributes between your SAML provider and your app** to
map SAML provider attributes to the user profile in your user pool. Include your
user pool required attributes in your attribute map.

For example, when you choose **User pool attribute**
`email`, enter the SAML attribute name as it appears in the SAML
assertion from your identity provider. Your identity provider might offer sample
SAML assertions for reference. Some identity providers use simple names, such as
`email`, while others use URL-formatted attribute names similar
to:

```
`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`
```

10. Choose **Create**.

###### Note

If you see `InvalidParameterException` while creating a SAML IdP with
an HTTPS metadata endpoint URL, make sure that the metadata endpoint has SSL
correctly set up and that there is a valid SSL certificate associated with it. One
example of such an exception would be "Error retrieving metadata from
`<metadata endpoint>`".

###### To set up the SAML IdP to add a signing certificate

- To get the certificate containing the public key that the IdP uses to verify
  the signed logout request, do the following:
  1.  Go to the **Social and external providers** menu of
      your user pool.
  2.  Select your SAML provider,
  3.  Choose **View signing certificate.**

For more information on SAML IdPs see [Using SAML identity providers with a user
pool](cognito-user-pools-saml-idp.md "cognito-user-pools-saml-idp.md").
