

# Setting up the authorization code flow for Bitbucket

The OAuth 2.0 authorization code flow is three-legged. When you create the connection, AWS Glue redirects you to Bitbucket to authorize access. AWS Glue then stores the access token and refresh token in your secret and refreshes them.

To set up the authorization code flow for Bitbucket:

1. In your Bitbucket workspace settings, under **Apps and features**, choose **OAuth consumers**, and then add a consumer.

1. For the callback URL, enter the redirect URI that the AWS Glue console uses. If multi-session support is turned on in the AWS Management Console, use `https://3rdp.oauth.console.api.aws`. Otherwise, use `https://{{region}}.console.aws.amazon.com/gluestudio/oauth`, where {{region}} is the AWS Region where you create the connection.

1. Grant read permissions for account, workspace membership, projects, repositories, pull requests, and pipelines.

1. Save the consumer, and then copy its key and secret.

1. In Secrets Manager, create a secret with the key `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` set to the consumer secret.

1. When you create the connection, choose OAuth 2.0, enter the consumer key as the client ID, choose the secret and the IAM role that AWS Glue assumes to read and update the secret, and then complete the authorization in Bitbucket.