# Configuring Zoom Meetings connections

Zoom Meetings supports the AUTHORIZATION_CODE grant type for OAuth2. The grant type determines how AWS Glue communicates with Zoom Meetings to request access to your data.

- This grant type is considered "three-legged" OAuth as it relies on redirecting users to a third-party authorization server to authenticate the user. It is used when creating connections via the AWS Glue console. The user creating a connection need to provide OAuth related information like Client ID and Client Secret for their Zoom Meetings client application. The AWS Glue console will redirect the user to Zoom where the user must login and allow AWS Glue the requested permissions to access their Zoom Meetings instance.
- Users may still opt to create their own connected app in Zoom Meetings and provide their own client ID and client secret when creating connections through the AWS Glue console. In this scenario, they will still be redirected to Zoom Meetings to login and authorize AWS Glue to access their resources.
- This grant type results in a refresh token and access token. The access token is short lived, and may be refreshed automatically without user interaction using the refresh token.
- For public Zoom Meetings documentation on creating a connected app for Authorization Code OAuth flow, see [Using OAuth 2.0](https://developers.zoom.us/docs/api/using-zoom-apis/#using-oauth-20 "https://developers.zoom.us/docs/api/using-zoom-apis/#using-oauth-20").
  To configure a Zoom Meetings connection:

1. In AWS Secrets Manager, create a secret with the following details:
   1. For the customer managed connected app, the Secret should contain the connected app Consumer Secret with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.
   2. Note: you must create a secret for your connections in AWS Glue.

1. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select Zoom Meetings.
   2. Provide the Zoom Meetings environment you want to connect to.
   3. Select the AWS IAM role which AWS Glue can assume and has permissions for following actions:

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

   4. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens.
   5. Select the network options if you want to use your network.

1. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
