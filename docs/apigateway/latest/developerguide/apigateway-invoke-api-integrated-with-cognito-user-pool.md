# Call a REST API integrated with an Amazon Cognito user pool

To call a method with a user pool authorizer configured, the client must do the
following:

- Enable the user to sign up with the user pool.
- Enable the user to sign in to the user pool.
- Obtain an [identity or access token](../../../cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.md "../../../cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.md") of the signed-in user from the user pool.
- Include the token in the `Authorization` header (or
  another header you specified when you created the authorizer).
  You can use AWS Amplify to perform these tasks.
  See [Integrating Amazon Cognito With Web and Mobile Apps](../../../cognito/latest/developerguide/cognito-integrate-apps.md "../../../cognito/latest/developerguide/cognito-integrate-apps.md")
  for more information.

- For Android, see [Getting Started with Amplify for Android](https://docs.amplify.aws/android/build-a-backend/auth/ "https://docs.amplify.aws/android/build-a-backend/auth/").
- To use iOS see [Getting started with Amplify for iOS](https://docs.amplify.aws/swift/build-a-backend/auth/ "https://docs.amplify.aws/swift/build-a-backend/auth/").
- To use JavaScript, see [Getting Started with Amplify for Javascript](https://docs.amplify.aws/javascript/build-a-backend/auth/ "https://docs.amplify.aws/javascript/build-a-backend/auth/").
