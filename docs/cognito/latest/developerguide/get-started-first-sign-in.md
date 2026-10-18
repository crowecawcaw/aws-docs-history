

# Your first sign-in: an end-to-end walkthrough
<a name="get-started-first-sign-in"></a>

This page is a map, not a replacement for the detailed procedures it links to. It shows how the setup steps connect so that you can see the whole journey before you dive into any single step. Each numbered step links to the authoritative procedure.

**Note**  
This walkthrough uses a user pool with managed login, the most common starting point for an application that signs in users. *Managed login* is the current Amazon Cognito-hosted sign-in UI, with a visual branding editor; the earlier *classic hosted UI* is a simpler alternative. You choose one or the other as the branding version on your user pool domain, and that choice applies to all app clients that use the domain. Managed login requires the *Essentials* or *Plus* feature plan—on the *Lite* plan, the classic hosted UI is your only hosted option. For the differences, see [User pool managed login](cognito-user-pools-managed-login.md) and [User pool feature plans](cognito-sign-in-feature-plans.md). If your goal is temporary AWS credentials for an existing identity source instead, start with [Getting started with Amazon Cognito identity pools](getting-started-with-identity-pools.md).

**From empty account to validated token**

1. **Create a user pool.** A user pool is your user directory and the identity provider that issues tokens. See [Create a new application in the Amazon Cognito console](getting-started-user-pools-application.md).

1. **Add a domain.** Managed login pages are served from a user pool domain—either an Amazon Cognito prefix domain or your own custom domain. Without a domain, there is no hosted sign-in page to send users to. See [Configuring a user pool domain](cognito-user-pools-assign-domain.md).

1. **Create an app client.** An app client represents your application to the user pool. It carries the settings that control sign-in, such as the allowed callback URLs and the sign-in methods. The branding version (managed login or classic hosted UI) is set on the domain, not the app client. See [Application-specific settings with app clients](user-pool-settings-client-apps.md).

1. **Send the user to managed login to sign in.** With a domain and an app client in place, your application redirects users to the managed login pages to sign up and sign in. Amazon Cognito returns your user to your callback URL with an authorization code. See [User pool managed login](cognito-user-pools-managed-login.md).

1. **Exchange the code for tokens.** Your application exchanges the authorization code at the token endpoint for an ID token, an access token, and a refresh token. See [The token endpoint](token-endpoint.md).

1. **Validate the token.** Your application (or your API) verifies the token's signature and claims before trusting it. See [Verifying JSON web tokens](amazon-cognito-user-pools-using-tokens-verifying-a-jwt.md).

At this point you have a signed-in user and a validated token. To authorize that token against your own API or backend—the most common next step—see [Accessing resources after successful sign-in](accessing-resources.md). If instead you need to grant the user temporary AWS credentials to call AWS services such as Amazon S3 directly from your app, continue to [Amazon Cognito identity pools](cognito-identity.md).