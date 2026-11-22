

# Setting up the authorization code flow for Miro

Before you create the connection, create a client app in your Miro developer team. For more information, see [Get started with OAuth 2.0 and Miro](https://developers.miro.com/docs/getting-started-with-oauth) on the Miro Developer Platform website.

1. In your Miro developer team, create an app.

1. In the app's permissions, select `boards:read`.

1. When you create the app, select **Expire user authorization token** so that Miro issues a refresh token. If an existing app doesn't use expiring tokens, create a new app.

1. Add both of the following redirect URIs to the app. The AWS Glue console uses `https://3rdp.oauth.console.api.aws` when multi-session support is turned on in the AWS Management Console, and `https://{{region}}.console.aws.amazon.com/gluestudio/oauth` otherwise, where {{region}} is the AWS Region where you create the connection.

1. Note the app's client ID and client secret.

Miro grants permissions from the app configuration, so you don't enter scopes in AWS Glue. If the token doesn't have `boards:read`, you can't read boards.