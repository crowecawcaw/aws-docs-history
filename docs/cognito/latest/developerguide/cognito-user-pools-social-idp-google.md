

# Add Google as a social identity provider
<a name="cognito-user-pools-social-idp-google"></a>

**Note**  
**Last verified against the provider console:** October 2, 2026. Google console steps follow the Google Auth Platform (the sections **Branding**, **Audience**, **Data Access**, and **Clients**). If the Google console differs from these steps, consult the [Google Auth Platform documentation](https://support.google.com/cloud/answer/15544987).

To let your users sign in with Google, you register an OAuth client in the Google Auth Platform, then add Google as an identity provider (IdP) in your user pool. You must enable managed login first.

## Register an OAuth client in the Google Auth Platform
<a name="social-idp-google-register"></a>

**To register a Google OAuth client**

1. Sign in to the [Google Cloud console](https://console.cloud.google.com/) and create or select a project.

1. Open **Menu**, then **Google Auth Platform**. If this is your first time, choose **Get started** on the **Overview** page and provide your app name, user support email, audience type (**External**), and contact information.

1. Choose **Branding**. Under **Authorized domains**, add the registrable domains of your user pool, not the full URLs:
   + `amazoncognito.com`, for the default Amazon Cognito domain.
   + The root of your custom domain, for example `example.com`, if you use one.

1. Choose **Data Access**, then **Add or remove scopes**. Add `openid`, `.../auth/userinfo.email`, and `.../auth/userinfo.profile`.

1. Choose **Clients**, then **Create client**. For **Application type**, choose **Web application**.

1. Under **Authorized JavaScript origins**, enter your user pool domain with no path:
   + Default Amazon Cognito domain: `https://<your-prefix>.auth.<region>.amazoncognito.com`
   + Custom domain: `https://auth.example.com`

1. Under **Authorized redirect URIs**, enter the `/oauth2/idpresponse` endpoint of your user pool domain:
   + Default Amazon Cognito domain: `https://<your-prefix>.auth.<region>.amazoncognito.com/oauth2/idpresponse`
   + Custom domain: `https://auth.example.com/oauth2/idpresponse`

1. Choose **Create**. Securely store the **Client ID** and **Client secret** that Google displays. You enter these values when you add Google to your user pool.
**Note**  
For clients created after June 2025, Google shows the client secret only once. Store it immediately.

## Add Google to your user pool
<a name="social-idp-google-configure"></a>

**To add Google as an IdP in the AWS Management Console**

1. In the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home), choose your user pool, then **Social and external providers**, then **Add an identity provider**.

1. Choose **Google**. Enter the **Client ID** and **Client secret** from the Google Auth Platform.

1. For **Authorized scopes**, enter `profile email openid`, separated by spaces.

1. Map the Google attributes you want to your user pool attributes. At a minimum, map `email` to `email` and `email_verified` to `email_verified`. If you don't map `email_verified`, Amazon Cognito treats the email as unverified.

1. Choose **Add identity provider**, and enable Google on your app client.

## Test Google sign-in
<a name="social-idp-google-test"></a>

Open your managed login sign-in page and choose **Continue with Google**, or open the authorize endpoint directly:

```
https://<your-prefix>.auth.<region>.amazoncognito.com/oauth2/authorize?response_type=code&client_id=<app-client-id>&redirect_uri=<your-app-callback>&identity_provider=Google
```

**Checkpoint**  
The browser completes the Google account chooser and returns through `/oauth2/idpresponse` to your app with an authorization code. In **User management**, a new federated user appears with the Google provider, a populated `email`, and `email_verified` set to `true`. You should see no `redirect_uri_mismatch` error.

## Google-specific pitfalls
<a name="social-idp-google-pitfalls"></a>

Unverified consent screen user cap  
An app with the **Testing** publishing status is limited to the test users you list. An app that shows the unverified-app screen is capped at 100 new users for the lifetime of the project, and the cap can't be reset. However, if your app requests only the basic sign-in scopes (`openid`, `email`, `profile`), test users don't need to be listed, see no warning, and their authorizations don't expire. Keep to these scopes to avoid the cap, or verify your app in the Verification Center.

Redirect-URI propagation  
Changes to authorized origins and redirect URIs can take from five minutes to a few hours to take effect. A mismatch returns `redirect_uri_mismatch`; an unregistered origin returns `origin_mismatch`.

email\_verified and account linking  
Google asserts `email_verified=true` for Gmail and Google Workspace accounts. Amazon Cognito doesn't automatically merge a Google user with an existing user that has the same email. To link them, implement linking (for example, with a pre sign-up Lambda trigger and `AdminLinkProviderForUser`), and only link on a trusted `email_verified` value.