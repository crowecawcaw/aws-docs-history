# Configuring Google Search Console connections

Google Search Console supports the AUTHORIZATION_CODE grant type for OAuth2. The grant type determines how AWS Glue communicates with Google Search Console to request access to your data.

- This grant type is considered "three-legged" OAuth as it relies on redirecting users to a third-party authorization server to authenticate the user. It is used when creating connections via the AWS Glue console.
- Users may still opt to create their own connected app in Google Search Console and provide their own client ID and client secret when creating connections through the AWS Glue console. In this scenario, they will still be redirected to Google Search Console to login and authorize AWS Glue to access their resources.
- This grant type results in a refresh token and access token. The access token is short lived, and may be refreshed automatically without user interaction using the refresh token.
- For public Google Search Console documentation on creating a connected app for Authorization Code OAuth flow, see [Using OAuth 2.0 to Access Google APIs](https://developers.google.com/identity/protocols/oauth2 "https://developers.google.com/identity/protocols/oauth2").
  To configure a Google Search Console connection:

1. In AWS Secrets Manager, create a secret with the following details:
   1. For the customer managed connected app, the Secret should contain the connected app Consumer Secret with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.
   2. Note: you must create a secret for your connections in AWS Glue.

1. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select Google Search Console.
   2. Select the AWS IAM role which AWS Glue can assume and has permissions for following actions:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "secretsmanager:DescribeSecret",
    "secretsmanager:GetSecretValue",
    "secretsmanager:PutSecretValue",
    "ec2:CreateNetworkInterface",
    "ec2:DescribeNetworkInterfaces",
    "ec2:DeleteNetworkInterface"
    ],
    "Resource": "*"
    }
    ]
   }`

   ```

   3. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens.
   4. Select the network options if you want to use your network.

1. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
