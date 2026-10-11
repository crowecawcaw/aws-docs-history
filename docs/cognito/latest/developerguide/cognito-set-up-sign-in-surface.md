

# Setting up your sign-in surface
<a name="cognito-set-up-sign-in-surface"></a>

Before your users can authenticate, you set up the surface they sign in through. For managed login, that means a user pool domain to serve the pages and an app client that points to them, plus the branding you apply. This chapter covers:
+ **Managed login**—the hosted sign-in pages, the user pool domain that serves them, and the branding editor.
+ **Migrating from the classic hosted UI**—what changes when you move an existing user pool to managed login.

To decide between managed login, the user pools API, and federation in the first place, see [Choose your authentication approach](cognito-authentication-approach.md). For the authentication flows themselves, see [Authentication with Amazon Cognito user pools](authentication.md).