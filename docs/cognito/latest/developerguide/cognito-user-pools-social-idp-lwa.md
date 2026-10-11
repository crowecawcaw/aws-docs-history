

# Add Login with Amazon as a social identity provider
<a name="cognito-user-pools-social-idp-lwa"></a>

**Note**  
**Last verified against the provider console:** October 2, 2026. Login with Amazon steps use the [Amazon Developer console](https://developer.amazon.com/loginwithamazon/console/site/lwa/overview.html) (not the AWS console).

To let your users sign in with their Amazon account, you register a Login with Amazon security profile, then add Login with Amazon as an identity provider (IdP) in your user pool. You must enable managed login first.

## Register a Login with Amazon security profile
<a name="social-idp-lwa-register"></a>

**To create and configure a security profile**

1. Sign in to the [Amazon Developer console](https://developer.amazon.com/loginwithamazon/console/site/lwa/overview.html), or go to **Apps and Services**, then **Login with Amazon**.

1. Choose **Create a New Security Profile**. Enter a **Name** (shown on the consent screen), a **Description**, and a **Consent Privacy Notice URL**. Choose **Save**.

1. Reveal the **Client ID** and **Client Secret** for the security profile. You enter these when you add Login with Amazon to your user pool.

1. Open **Web Settings** for the profile and choose **Edit**. Enter the values below, then **Save**.
   + **Allowed Origins** (HTTPS, no path): `https://<your-prefix>.auth.<region>.amazoncognito.com` or `https://auth.example.com`.
   + **Allowed Return URLs** (the `/oauth2/idpresponse` endpoint): `https://<your-prefix>.auth.<region>.amazoncognito.com/oauth2/idpresponse` or `https://auth.example.com/oauth2/idpresponse`. Amazon Cognito uses the redirect flow, so the return URL is the value it depends on.

## Add Login with Amazon to your user pool
<a name="social-idp-lwa-configure"></a>

**To add Login with Amazon as an IdP in the AWS Management Console**

1. In the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home), choose your user pool, then **Social and external providers**, then **Add an identity provider**, then **Login with Amazon**.

1. Enter the **Client ID** and **Client Secret** from the security profile.

1. For **Authorized scopes**, enter `profile`. This returns the user's name, email, and user ID. (Add `postal_code` only if you need the ZIP or postal code.)

1. Map `email` to `email`, `name` to `name`, and `user_id` to your user name attribute.

1. Choose **Add identity provider**, and enable Login with Amazon on your app client.

## Test Login with Amazon sign-in
<a name="social-idp-lwa-test"></a>

Open your managed login sign-in page and choose **Continue with Amazon**, then authenticate and accept the consent screen.

**Checkpoint**  
The browser returns through `/oauth2/idpresponse` to your app with an authorization code, and the user appears in your user pool as a federated user whose user name is prefixed `LoginWithAmazon_`. The ID token contains the mapped `email` and `name`. Note that `email_verified` reads `false` unless you set it with a trigger (see pitfalls).

## Login with Amazon pitfalls
<a name="social-idp-lwa-pitfalls"></a>

No email\_verified claim  
The `profile` scope returns only `email`, `name`, and `user_id`—there is no `email_verified` claim to map. Mapped emails are unverified by default, so Login with Amazon users land with `email_verified` set to `false`.

Effect on account linking  
Because the email is unverified, Amazon Cognito won't automatically merge a Login with Amazon user into an existing email-verified user. To link or mark the email verified, use a pre sign-up Lambda trigger (and `AdminLinkProviderForUser`), and only when your trust model justifies trusting the Amazon-asserted email.

Mapped attributes must be writable  
Any custom attribute you map must be mutable and writable by the app client, or sign-in fails or silently skips the attribute. Standard `email` and `name` are fine.