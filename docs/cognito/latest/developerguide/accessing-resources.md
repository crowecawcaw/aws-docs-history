# Accessing resources after successful sign-in

Your app users can either sign in directly through a user pool, or they can federate through a
third-party identity provider (IdP). The user pool manages the overhead of handling the tokens
that are returned from social sign-in through Facebook, Google, Amazon, and Apple, and from OpenID
Connect (OIDC) and SAML IdPs. For more information, see [Understanding
user pool JSON web tokens (JWTs)](amazon-cognito-user-pools-using-tokens-with-identity-providers.md "amazon-cognito-user-pools-using-tokens-with-identity-providers.md").

After a successful authentication, your app will receive user pool tokens from Amazon Cognito. You
can use user pool tokens to:

- Retrieve AWS credentials that authorize requests for application resources in
  AWS services like Amazon DynamoDB and Amazon S3.
- Provide temporary, revocable proof of authentication.
- Populate identity data to a user profile in your app.
- Authorize changes to the signed-in user's profile in the user pool directory.
- Authorize requests for user information with an access token.
- Authorize requests to data that is behind access-protected external APIs with access
  tokens.
- Authorize access to application assets that are stored on the client or server with
  Amazon Verified Permissions.
  For more information, see [An example authentication
  session](authentication.md#amazon-cognito-user-pools-authentication-flow "authentication.md#amazon-cognito-user-pools-authentication-flow") and [Understanding
  user pool JSON web tokens (JWTs)](amazon-cognito-user-pools-using-tokens-with-identity-providers.md "amazon-cognito-user-pools-using-tokens-with-identity-providers.md").

![Authentication overview.](images/scenario-authentication-cup.png)

###### Topics

- [Authorizing access to client or server resources with
  Amazon Verified Permissions](scenario-backend.md "scenario-backend.md")
- [Accessing resources
  with API Gateway after sign-in](user-pool-accessing-resources-api-gateway-and-lambda.md "user-pool-accessing-resources-api-gateway-and-lambda.md")
- [Accessing
  AWS services using an identity pool after sign-in](amazon-cognito-integrating-user-pools-with-identity-pools.md "amazon-cognito-integrating-user-pools-with-identity-pools.md")
