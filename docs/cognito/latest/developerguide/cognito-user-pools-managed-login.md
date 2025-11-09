# User pool managed login

You can choose a web domain to host services for your user pool. An Amazon Cognito user pool gains
the following functions when you add a domain, collectively referred to as _managed login_.

- An [authorization server](https://datatracker.ietf.org/doc/html/rfc6749#section-1.1 "https://datatracker.ietf.org/doc/html/rfc6749#section-1.1") that acts as an identity provider (IdP) to
  applications that work with OAuth 2.0 and OpenID Connect (OIDC). The authorization
  server [routes requests](authorization-endpoint.md "authorization-endpoint.md"), [issues and manages JSON web tokens (JWTs)](token-endpoint.md "token-endpoint.md"), and
  [delivers user attribute
  information](userinfo-endpoint.md "userinfo-endpoint.md").
- A ready-to-use user interface (UI) for authentication operations like sign-in,
  sign-out and password management. The _managed login
  pages_ act as a web front end for authentication services.
- A service provider (SP), or relying party (RP), to SAML 2.0 IdPs, OIDC IdPs,
  Facebook, Login with Amazon, Sign in with Apple, and Google.
  An additional option that shares some features with managed login is the classic _hosted UI_. The classic hosted UI is a first-generation version
  of the managed login services. Hosted UI IdP and RP services generally have the same
  characteristics as managed login, but the login pages have a simpler design and fewer
  features. For example, passkey sign-in isn't available in the classic hosted UI. In the Lite
  [feature plan](cognito-sign-in-feature-plans.md "cognito-sign-in-feature-plans.md"), the classic hosted UI
  is your only option for user pool domain services.

The managed login pages are a collection of web interfaces for basic sign-up, sign-in,
multi-factor authentication and password-reset activities in your user pool. They also
connect users to one or more third-party identity providers (IdPs) when you want to give
users a choice of sign-in option. Your app can invoke your managed login pages in users'
browsers when you want to authenticate and authorize users.

You can make the managed login user experience fit your brand with custom logos,
backgrounds and styles. You have two options for the branding that you might apply to your
managed login UI: the _branding editor_ for managed login,
and _hosted UI (classic) branding_ for the hosted
UI.

**Branding editor**

An updated user experience with the most up-to-date authentication options and
a visual editor in the Amazon Cognito console.

**Hosted UI branding**

A familiar user experience for previous adopters of Amazon Cognito user pools. Branding for the
hosted UI is a file-based system. To apply branding to hosted UI pages, you
upload a logo image file and a file that sets values for several predetermined
CSS style options.

The branding editor isn't available in all feature plans for user pools. For more
information, see [User pool feature plans](cognito-sign-in-feature-plans.md "cognito-sign-in-feature-plans.md").

For more information about constructing requests to managed login and hosted UI services,
see [User pool endpoints and
managed login reference](cognito-userpools-server-contract-reference.md "cognito-userpools-server-contract-reference.md").

###### Note

Amazon Cognito managed login doesn't support custom authentication
with [custom authentication challenge Lambda triggers](user-pool-lambda-challenge.md "user-pool-lambda-challenge.md").

###### Topics

- [Managed login localization](#managed-login-localization "#managed-login-localization")
- [Terms documents](#managed-login-terms-documents "#managed-login-terms-documents")
- [Setting up managed login
  with AWS Amplify](#cognito-user-pools-app-integration-amplify "#cognito-user-pools-app-integration-amplify")
- [Setting up managed login with the Amazon Cognito
  console](#set-up-managed-login "#set-up-managed-login")
- [Viewing your sign-in
  page](#view-login-pages "#view-login-pages")
- [Customizing
  your authentication pages](#cognito-user-pools-app-integration-customize-hosted-ui "#cognito-user-pools-app-integration-customize-hosted-ui")
- [Things to know about managed login and
  the hosted UI](#managed-login-things-to-know "#managed-login-things-to-know")
- [Configuring a user pool domain](cognito-user-pools-assign-domain.md "cognito-user-pools-assign-domain.md")
- [Apply branding to managed login pages](managed-login-branding.md "managed-login-branding.md")

## Managed login localization

Managed login defaults to the English language in user-interactive pages. You can
display your managed login pages localized for the language of your choice. The
available languages are those available in the AWS Management Console. In the link that you
distribute to users, add a `lang` query parameter, as shown in the following
example.

```
https://`<your domain>`/oauth2/authorize?lang=`es`&response_type=`code`&client_id=`<your app client id>`&redirect_uri=`<your relying-party url>`
```

Amazon Cognito sets a cookie in users' browser with their language preference after the initial
request with a `lang` parameter. After the cookie is set, the language
selection persists without displaying or requiring you to include the parameter in
requests. For example, after a user makes a sign-in request with a `lang=de`
parameter, their managed login pages render in German until they clear their cookies or
make a new request with a new localization parameter like
`lang=`en``.

Localization is only available for managed login. You must be on the Essentials or
Plus [feature plan](cognito-sign-in-feature-plans.md "cognito-sign-in-feature-plans.md") and have assigned
your domain to use [managed login
branding](managed-login-branding.md "managed-login-branding.md").

The selection that your user makes in managed login isn't available to [custom email or SMS sender
triggers](user-pool-lambda-custom-sender-triggers.md "user-pool-lambda-custom-sender-triggers.md"). When you implement these triggers, you must use other mechanisms to
determine a user's preferred language. In sign-in flows, the `locale`
attribute might indicate the user's preferred language based on location. In sign-up
flows, the region or app client ID of your user pool might indicate a language
preference.

The following languages are available.

| Managed login languages | Language | Code |
| ----------------------- | -------- | ---- |
| German                  | de       |
| English                 | en       |
| Spanish                 | es       |
| French                  | fr       |
| Bahasa Indonesia        | id       |
| Italian                 | it       |
| Japanese                | ja       |
| Korean                  | ko       |
| Portuguese (Brazil)     | pt-BR    |
| Chinese (Simplified)    | zh-CN    |
| Chinese (Traditional)   | zh-TW    |

## Terms documents

You can configure your managed login pages to display links to your **Terms of
use** and **Privacy policy** documents when users sign up.
When you set up both terms documents in your app client, users see the following text
during sign-up: **By signing up, you agree to our Terms of use and Privacy
policy.** The phrases **Terms of use** and
**Privacy policy** appear in your managed login page, hyperlinked
to your documents.

Terms documents support language-specific URLs that align with managed login
localization. When users select a language with the `lang` query parameter,
Amazon Cognito displays links to your terms documents in that language. If you haven't configured
a URL for a specific language, Amazon Cognito uses the default URL that you configured for the
app client.

To configure terms documents for your app client, navigate to the **Managed
login** menu in your user pool. Under **Terms documents**,
choose **Create terms document**.

Amazon Cognito console

###### To create a terms document

1. Navigate to your user pool and choose the **Managed login**
   menu. Locate **Terms documents**.
2. Choose **Create terms document**.
3. Select the app client that you want to assign the terms document to.
4. Enter a **Terms name**. This identifies your document in the
   console.
5. Under **Links**, choose a **Language** and
   enter the **URL** where you host your terms document in that
   language.
6. To add URLs for additional languages, choose **Add
   another**.
7. Choose **Create**.

Amazon Cognito user pools API
The following is an example [CreateTerms](../../../cognito-user-identity-pools/latest/APIReference/API_CreateTerms.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateTerms.md") request body.
It causes the sign-up page for app client `1example23456789` to render links for a french-language and a portuguese-language (Brazil) version of the privacy policy
when managed login is localized to that language. A separate request is required to set URLs for `terms-of-use` before managed login will render links at the
sign-up page.

```
{
   "ClientId": "1example23456789",
   "Enforcement": "NONE",
   "Links": {
      "cognito:default" : "https://example.com/privacy/",
      "cognito:french" : "https://example.com/fr/privacy/",
      "cognito:portuguese-brazil" : "https://example.com/pt/privacy/"
   },
   "TermsName": "privacy-policy",
   "TermsSource": "LINK",
   "UserPoolId": "us-east-1_EXAMPLE"
}
```

###### Note

You must create both a terms of use and a privacy policy document for your app
client before Amazon Cognito will display terms documents in your managed login pages.

## Setting up managed login

with AWS Amplify

If you use AWS Amplify to add authentication to your web or mobile app, you can set
up your managed login pages in the Amplify command line interface (CLI) and libraries
in the Amplify framework. To add authentication to your app, add the `Auth`
category to your project. Then, in your application, authenticate user pool users with
Amplify client libraries.

You can invoke managed login pages for authentication or you can federate users
through an authorization endpoint that redirects to an IdP. After a user successfully
authenticates with the provider, Amplify creates a new user in your user pool and
passes the user's tokens to your app.

The following examples show how to use AWS Amplify to set up managed login with
social providers in your app.

- [React](https://docs.amplify.aws/react/build-a-backend/auth/concepts/external-identity-providers/ "https://docs.amplify.aws/react/build-a-backend/auth/concepts/external-identity-providers/")
- [Swift](https://docs.amplify.aws/swift/build-a-backend/auth/concepts/external-identity-providers/ "https://docs.amplify.aws/swift/build-a-backend/auth/concepts/external-identity-providers/")
- [Flutter](https://docs.amplify.aws/flutter/build-a-backend/auth/concepts/external-identity-providers/ "https://docs.amplify.aws/flutter/build-a-backend/auth/concepts/external-identity-providers/")
- [Android](https://docs.amplify.aws/android/build-a-backend/auth/concepts/external-identity-providers/ "https://docs.amplify.aws/android/build-a-backend/auth/concepts/external-identity-providers/")

## Setting up managed login with the Amazon Cognito

console

The first requirement for managed login and hosted UI is a user pool domain. In the
user pools console, navigate to the **Domain** tab of your user pool
and add a **Cognito domain** or a **custom domain**.
You can also choose a domain during the process of creating a new user pool. For more
information, see [Configuring a user pool domain](cognito-user-pools-assign-domain.md "cognito-user-pools-assign-domain.md"). When a domain is active in your user
pool, all app clients serve public authentication pages on that domain.

When you create or modify a user pool domain, you set the **Branding
version** for your domain. This branding version is a choice of
**Managed login** or **Hosted UI (classic)**. Your
choice of branding version applies to all app clients that use the sign-in services at
your domain.

The next step is to create an [app
client](user-pool-settings-client-apps.md "user-pool-settings-client-apps.md") from the **App clients** tab of your user pool. In
the process of creating an app client, Amazon Cognito will ask you for information about your
application, then prompt you to select a **Return URL**. The return URL
is also called the relying party (RP) URL, the redirect URI, and the callback URL. This
is the URL that your application runs from, for example
`https://www.example.com` or `myapp://example`.

After you configure a domain and app client with a branding style in your user pool,
your managed login pages become available on the internet.

## Viewing your sign-in

page

In the Amazon Cognito console, choose the **View login pages** button in the
**Login pages** tab for your app client under the **App
clients** menu. This button takes you to a sign-in page in your user pool
domain with the following basic parameters.

- The app client id
- An authorization code grant request
- A request for all scopes that you have activated for the current app
  client
- The first callback URL in the list for the current app client

The **View login page** button is useful when you want to test the
basic functions of your managed login pages. Your login pages will match the
**Branding version** that you assigned to your [user pool domain](cognito-user-pools-assign-domain.md "cognito-user-pools-assign-domain.md"). You can
customize your sign-in URL with additional and modified parameters. In most cases, the
automatically-generated parameters of the **View login page** link
don’t fully match the needs of your app. In these cases, you must customize the URL that
your app invokes when it signs in your users. For more information about sign-in
parameter keys and values, see [User pool endpoints and
managed login reference](cognito-userpools-server-contract-reference.md "cognito-userpools-server-contract-reference.md").

The sign-in webpage uses the following URL format. This example requests an
authorization code grant with the `response_type=code` parameter.

```
https://`<your domain>`/oauth2/authorize?response_type=`code`&client_id=`<your app client id>`&redirect_uri=`<your relying-party url>`
```

You can look up your user pool domain string from the **Domain** menu
in your user pool. In the **App clients** menu, you can identify app
client IDs, their callback URLs, their allowed scopes, and other configuration.

When you navigate to the `/oauth2/authorize` endpoint with your custom
parameters, Amazon Cognito either redirects you to the `/oauth2/login`
endpoint or, if you have an `identity_provider` or
`idp_identifier` parameter, silently redirects you to your IdP sign-in
page.

###### Example request for an implicit grant

You can view your sign-in webpage with the following URL for the implicit code
grant where `response_type=token`. After a successful sign-in, Amazon Cognito
returns user pool tokens to your web browser's address bar.

```

            https://`mydomain.auth.us-east-1.amazoncognito.com`/authorize?response_type=token&client_id=`1example23456789`&redirect_uri=`https://mydomain.example.com`

```

The identity and access tokens appear as parameters appended to your redirect
URL.

The following is an example response from an implicit grant request.

```

            https://`auth.example.com`/#id_token=`eyJraaBcDeF1234567890`&access_token=`eyJraGhIjKlM1112131415`&expires_in=3600&token_type=Bearer

```

## Customizing

your authentication pages

In the past, Amazon Cognito only hosted login pages with the classic _hosted UI_, a simple design that grants a universal look to
authentication webpages. You could customize Amazon Cognito user pools with a logo image and tweak some
styles with a file that specified some CSS style values. Later, Amazon Cognito introduced
_managed login_, an updated hosted authentication
service. Managed login is an updated look-and-feel with the _branding editor_. The branding editor is a no-code visual editor and a
larger suite of options than the hosted UI customization experience. Managed login also
introduced custom background images and a dark mode theme.

You can switch between the managed login and hosted UI branding experiences in user
pools. To learn more about customizing your managed login pages, see [Apply branding to managed login pages](managed-login-branding.md "managed-login-branding.md").

## Things to know about managed login and

the hosted UI

###### The one-hour managed login and hosted UI session cookie

When a user signs in with your login pages or a third-party provider, Amazon Cognito sets a
cookie in their browser. With this cookie, users can sign in again with the same
authentication method for one hour. When they sign in with their browser cookie,
they get fresh tokens that last the duration specified in your app client
configuration. Changes to user attributes or authentication factors have no effect
on their ability to sign in again with their browser cookie.

Authentication with the session cookie doesn't reset the cookie duration to an
additional hour. Users must sign in again if they attempt to access your sign-in pages
more than an hour after their most recent successful interactive authentication.

###### Confirming user accounts and verifying user attributes

For user pool [local users](cognito-terms.md#terms-localuser "cognito-terms.md#terms-localuser"), managed login
and the hosted UI work best when you configure your user pool to **Allow
Cognito to automatically send messages to verify and confirm**. When
you enable this setting, Amazon Cognito sends a message with a confirmation code to users who
sign up. When you instead confirm users as a user pool administrator, your login
pages display an error message after sign-up. In this state, Amazon Cognito has created the
new user, but hasn't been able to send a verification message. You can still confirm
users as an administrator, but they might contact your support desk after they
encounter an error. For more information about administrative confirmation, see
[Allowing users to
sign up in your app but confirming them as a user pool administrator](signing-up-users-in-your-app.md#signing-up-users-in-your-app-and-confirming-them-as-admin "signing-up-users-in-your-app.md#signing-up-users-in-your-app-and-confirming-them-as-admin").

###### Managed login scope of operations

Managed login and the classic hosted UI support sign-up, sign-in, and password
management. This includes completing sign-in with multi-factor authentication (MFA)
and registration of webAuthn authenticators. Managed login doesn't support user
self-service profile management like attribute changes and setting of MFA
preference. You must implement profile management in your own application code.
Managed login also doesn't provide the capacity to confirm attribute changes when
you update email addresses and phone numbers as an administrator with the [AdminUpdateUserAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md") API operation.

###### Viewing your changes to configuration

If you make style changes to your pages and they do not immediately appear, wait a
few minutes and then refresh the page.

###### Decoding user pool tokens

Amazon Cognito user pool tokens are signed using an RS256 algorithm. You can decode and
verify user pool tokens using AWS Lambda. See [Decode and verify Amazon Cognito JWT tokens](https://github.com/awslabs/aws-support-tools/tree/master/Cognito/decode-verify-jwt "https://github.com/awslabs/aws-support-tools/tree/master/Cognito/decode-verify-jwt") on GitHub.

###### TLS version

Managed login and hosted UI pages require encryption in transit. User pool domains
that are provided by Amazon Cognito require that users' browsers negotiate a minimum TLS
version of 1.2. Custom domains support browser connections with TLS version 1.2. The
hosted UI (classic) **doesn't require** TLS 1.2 for
custom domains, but the newer managed login **requires** TLS version 1.2 both for custom and prefix domains. Because
Amazon Cognito manages the configuration of your domain services, you can't modify the TLS
requirements of your user pool domain.

###### CORS policies

Neither managed login nor the hosted UI support custom cross-origin resource
sharing (CORS) origin policies. A CORS policy would prevent users from passing
authentication parameters in their requests. Instead, implement a CORS policy in
your application front end. Amazon Cognito returns an `Access-Control-Allow-Origin:
 *` response header to requests to the following endpoints.

1. [Token endpoint](token-endpoint.md "token-endpoint.md")
2. [Revoke endpoint](revocation-endpoint.md "revocation-endpoint.md")
3. [userInfo endpoint](userinfo-endpoint.md "userinfo-endpoint.md")

###### Cookies

Managed login and the hosted UI set cookies in users' browsers. The cookies
conform to the requirements of some browsers that sites not set third-party cookies.
They are scoped only to your user pool endpoints and include the following:

- An `XSRF-TOKEN` cookie for each request.
- A `csrf-state` cookie for session consistency when a user is
  redirected.
- A `csrf-state-legacy` cookie for session consistency, read by Amazon Cognito
  as a fallback when your browser doesn't have support for the
  `SameSite` attribute.
- A `cognito` session cookie that preserves successful sign-in
  attempts for an hour.
- A `lang` cookie that preserves a user's choice of [language localization](#managed-login-localization "#managed-login-localization") in managed
  login.
- A `page-data` cookie that persists required data as a user
  navigates between managed login pages.

In iOS, you can [block all
cookies](https://support.apple.com/en-us/105082 "https://support.apple.com/en-us/105082"). This setting isn't compatible with managed login or the hosted UI.
To work with users who might enable this setting, build user pool authentication into a
native iOS app with an AWS SDK. In this scenario, you can build your own session
storage that isn't cookie-based.

###### Effects of managed login version change

Consider the following effects of adding domains and setting the managed login
version.

- When you add a prefix domain, either with managed login or hosted UI (classic)
  branding, it can take up to 60 seconds before your login pages are
  available.
- When you add a custom domain, either with managed login or hosted UI (classic)
  branding, it can take up to five minutes before your login pages are
  available.
- When you change the branding version for your domain, it can take up to four
  minutes before your login pages are available in the new branding
  version.
- When you switch between managed login and hosted UI (classic) branding, Amazon Cognito
  doesn't maintain user sessions. They must sign in again with the new
  interface.

###### Default style

When you create an app client in the AWS Management Console, Amazon Cognito automatically assigns a
branding style to your app client. When you programmatically create an app client
with the [CreateUserPoolClient](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.md") operation, no branding style is created. Managed
login isn't available for an app client created with an AWS SDK until you create
one with a [CreateManagedLoginBranding](../../../cognito-user-identity-pools/latest/APIReference/API_CreateManagedLoginBranding.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateManagedLoginBranding.md") request.

###### Managed login authentication prompt times out

Amazon Cognito cancels authentication requests that do not complete within five minutes, and
redirects the user to managed login. The page displays a `Something went
 wrong` error message.
