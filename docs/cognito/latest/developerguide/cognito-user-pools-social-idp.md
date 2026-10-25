

# Using social identity providers with a user pool
<a name="cognito-user-pools-social-idp"></a>

Your web and mobile app users can sign in through social identity providers (IdP) like Google, Facebook, Amazon, and Apple. You enable managed login, and Amazon Cognito adds a sign-in button for each social IdP to your managed login pages. Amazon Cognito handles the OAuth 2.0 and OpenID Connect exchanges with the provider and issues your app one standard set of user pool tokens, so your back-end systems can standardize on user pool tokens regardless of how the user signed in. For more information about the endpoints that Amazon Cognito creates for these exchanges, see the [Amazon Cognito user pools Auth API reference](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-userpools-server-contract-reference.html).

Each provider has its own developer console, its own values to enter, and its own pitfalls. Choose your provider for step-by-step instructions:
+ [Add Google as a social identity provider](cognito-user-pools-social-idp-google.md)
+ [Add Sign in with Apple as a social identity provider](cognito-user-pools-social-idp-apple.md)
+ [Add Facebook as a social identity provider](cognito-user-pools-social-idp-facebook.md)
+ [Add Login with Amazon as a social identity provider](cognito-user-pools-social-idp-lwa.md)

**Note**  
Sign-in through a third party (federation) is available in Amazon Cognito user pools. This feature is independent of federation through Amazon Cognito identity pools (federated identities).

**Topics**
+ [Add Google as a social identity provider](cognito-user-pools-social-idp-google.md)
+ [Add Sign in with Apple as a social identity provider](cognito-user-pools-social-idp-apple.md)
+ [Add Facebook as a social identity provider](cognito-user-pools-social-idp-facebook.md)
+ [Add Login with Amazon as a social identity provider](cognito-user-pools-social-idp-lwa.md)