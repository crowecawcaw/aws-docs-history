

# Add Facebook as a social identity provider
<a name="cognito-user-pools-social-idp-facebook"></a>

**Note**  
**Last verified against the provider console:** October 2, 2026. Facebook steps use the [Meta for Developers](https://developers.facebook.com/) console, which organizes app setup around **Use cases**. The OAuth redirect settings are under **Use cases**, **Customize**, **Settings**.

To let your users sign in with Facebook, you create a Meta app with the Facebook Login use case, then add Facebook as an identity provider (IdP) in your user pool. You must enable managed login first.

## Create a Meta app for Facebook Login
<a name="social-idp-facebook-register"></a>

**To create and configure a Meta app**

1. Sign in to [Meta for Developers](https://developers.facebook.com/), choose **My Apps**, then **Create App**.

1. For the use case, choose **Authenticate and request data from users with Facebook Login**. Finish creating the app. New apps start in **Development** mode.

1. From **App settings**, then **Basic**, record the **App ID** and **App secret**. Set **App Domains** to your user pool domain host (`<your-prefix>.auth.<region>.amazoncognito.com` or `auth.example.com`), and add the **Website** platform with your managed login sign-in URL as the **Site URL**.

1. Go to **Use cases**, choose your Facebook Login use case, then **Customize**. Confirm the `public_profile` permission (required) and add `email`.

1. In the use case **Settings**, set **Valid OAuth Redirect URIs** to the `/oauth2/idpresponse` endpoint of your user pool domain:
   + Default Amazon Cognito domain: `https://<your-prefix>.auth.<region>.amazoncognito.com/oauth2/idpresponse`
   + Custom domain: `https://auth.example.com/oauth2/idpresponse`

## Add Facebook to your user pool
<a name="social-idp-facebook-configure"></a>

**To add Facebook as an IdP in the AWS Management Console**

1. In the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home), choose your user pool, then **Social and external providers**, then **Add an identity provider**, then **Facebook**.

1. Enter the **App ID** and **App secret**, and choose a Facebook API version. Choose the latest available version, because each version has a discontinuation date and scopes can vary between versions.

1. For **Authorized scopes**, enter `public_profile,email`, separated by commas.

1. Map `email` to `email` and `name` to `name`.

1. Choose **Add identity provider**, and enable Facebook on your app client.

## Test Facebook sign-in
<a name="social-idp-facebook-test"></a>

While the app is in **Development** mode, add your own Facebook account as an app role (Administrator, Developer, or Tester). Then open your managed login sign-in page and choose **Continue with Facebook**.

**Checkpoint**  
Facebook returns through `/oauth2/idpresponse` to your app with an authorization code, and a new federated user appears in your user pool with `email` and `name` populated. Then switch the app to **Live** mode and confirm a non-role account can sign in. A non-role account that sees "app not active" or "in development mode" means the app is still in Development mode or lacks Advanced Access.

## Facebook-specific pitfalls
<a name="social-idp-facebook-pitfalls"></a>

Development mode and app review  
A new app is in **Development** mode and only app-role users (Administrator, Developer, Tester) can sign in. To let the general public sign in, switch the app to **Live** mode, complete Business Verification, and obtain Advanced Access for `email` (and increased access for `public_profile`). First-time testers often hit "app not active" because they test with a non-role account.

No email\_verified claim  
Facebook does not return an `email_verified` claim, so there is nothing to map, and Amazon Cognito treats the Facebook email as unverified. Don't assume a verified email from Facebook, and link accounts by email only through deliberate, trusted logic rather than automatically.

Keep scopes small  
Sign-in completion drops sharply past about four permissions. Keep the request to `public_profile` and `email`. Amazon Cognito federation is also not compatible with Facebook Limited Login on iOS.