

# Add Sign in with Apple as a social identity provider
<a name="cognito-user-pools-social-idp-apple"></a>

**Note**  
**Last verified against the provider console:** October 2, 2026. Apple steps use [Certificates, Identifiers & Profiles](https://developer.apple.com/account/resources) in the Apple Developer account. You must have the Account Holder or Admin role.

Sign in with Apple requires four artifacts: an App ID, a Services ID (your Amazon Cognito client ID), a private key, and your Team ID. You then add Apple as an identity provider (IdP) in your user pool. You must enable managed login first.

## Create your Apple identifiers and key
<a name="social-idp-apple-register"></a>

**To create the Apple artifacts**

1. In **Certificates, Identifiers & Profiles**, create an **App ID** (Identifiers, then **\+**, then **App IDs**, then **App**) and enable the **Sign in with Apple** capability.

1. Create a **Services ID** (Identifiers, then **\+**, then **Services IDs**). Enter a description and a reverse-domain identifier, for example `com.example.auth.cognito`. This identifier is your Amazon Cognito **Services ID** (client ID).

1. Select the Services ID, enable **Sign in with Apple**, and choose **Configure**. Choose your primary App ID, then enter the web URLs:
   + **Domains and Subdomains** (host only, no scheme): `<your-prefix>.auth.<region>.amazoncognito.com` for the default Amazon Cognito domain, or `auth.example.com` for a custom domain.
   + **Return URLs** (full URL with `https://`): `https://<your-prefix>.auth.<region>.amazoncognito.com/oauth2/idpresponse`, or `https://auth.example.com/oauth2/idpresponse` for a custom domain.

1. Create a private key (Keys, then **\+**), enable **Sign in with Apple**, and download the `.p8` file. You can download it only once. Record the **Key ID**.

1. Record your 10-character **Team ID** from the Membership page. You enter the Services ID, Team ID, Key ID, and private key when you add Apple to your user pool.

## Add Apple to your user pool
<a name="social-idp-apple-configure"></a>

**To add Apple as an IdP in the AWS Management Console**

1. In the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home), choose your user pool, then **Social and external providers**, then **Add an identity provider**, then **Sign in with Apple**.

1. Enter the **Services ID**, **Team ID**, **Key ID**, and **private key**. Amazon Cognito uses the private key to generate the client secret for you.

1. For **Authorized scopes**, enter `email name`. Use only `email` if you don't need the user's name.

1. Map `email` to `email` and `sub` to your user name attribute. Apple returns the user's name only on the first sign-in, so capture it then if you map it.

1. Choose **Add identity provider**, and enable Apple on your app client.

## Test Sign in with Apple
<a name="social-idp-apple-test"></a>

Open your managed login sign-in page and choose **Continue with Apple**. Test both **Share My Email** and **Hide My Email**.

**Checkpoint**  
The browser returns through `/oauth2/idpresponse` to your app with an authorization code. A user appears in your user pool with the **SignInWithApple** provider and a `sub`. The Share My Email run shows the real email; the Hide My Email run shows a `@privaterelay.appleid.com` address. An `invalid_client` error almost always means the client-secret JWT has expired or the Services ID or Return URL doesn't match `/oauth2/idpresponse` exactly.

## Apple-specific pitfalls
<a name="social-idp-apple-pitfalls"></a>

The client secret is a JWT that expires  
Apple's client secret is not a static string. It's an ES256-signed JWT with a maximum lifetime of six months (15,777,000 seconds), and when it expires, Apple sign-in breaks with `invalid_client` and no warning. In the configuration described here, you give Amazon Cognito the private key (along with the Services ID, Team ID, and Key ID), and Amazon Cognito generates the client-secret JWT from that key—you don't paste a pre-built secret. Keep the private key you registered with Apple valid and current in the IdP configuration; if you revoke or replace the Apple key, update the IdP (for example, with `UpdateIdentityProvider`) with the new key.

Private relay email and account linking  
When a user chooses **Hide My Email**, Apple returns a `@privaterelay.appleid.com` address instead of the real one. This address differs from the email the same person uses with other providers, so don't link accounts across identity providers by email when Apple is involved—link by the provider `sub` instead. To send mail to a relay address, register your sending domains under **Sign in with Apple for Email Communication**.

email\_verified type and managed accounts  
Apple's `email_verified` claim can arrive as the string `"true"` or the boolean `true`—handle both. It's always true for consumer Apple Accounts. For Apple at Work & School (managed) accounts it can be false. Prefer `sub`-based linking and normalize the string value before any merge logic.