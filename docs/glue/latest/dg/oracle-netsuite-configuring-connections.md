# Configuring Oracle NetSuite connections

Oracle NetSuite supports the AUTHORIZATION_CODE grant type for OAuth2. The grant type determines how AWS Glue communicates with Oracle NetSuite to request access to your data.

- This grant type is considered "three-legged" OAuth as it relies on redirecting users to a third-party authorization server to authenticate the user. It is used when creating connections via the AWS Glue console. The user creating a connection may by default rely on an AWS Glue-owned connected app (AWS Glue managed client application) where they do not need to provide any OAuth-related information except for their Oracle NetSuite instance URL. The AWS Glue console will redirect the user to Oracle NetSuite where the user must log in and allow AWS Glue the requested permissions to access their Oracle NetSuite instance.
- Users may still opt to create their own connected app in Oracle NetSuite and provide their own client id and client secret when creating connections through the AWS Glue console. In this scenario, they will still be redirected to Oracle NetSuite to login and authorize AWS Glue to access their resources.
- This grant type results in a refresh token and access token. The access token is short lived, and may be refreshed automatically without user interaction using the refresh token.
- For public Oracle NetSuite documentation on creating a connected app for Authorization Code OAuth flow, see [Public apps](https://developers.oracle-netsuite.com/docs/api/creating-an-app "https://developers.oracle-netsuite.com/docs/api/creating-an-app").
  To configure a Oracle NetSuite connection:

1. In AWS Secrets Manager, create a secret with the following details:
   1. For the customer managed connected app, the Secret should contain the connected app Consumer Secret with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.
   2. Note: You must create a secret for your connection in AWS Glue.

2. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select Oracle NetSuite.
   2. Provide the Oracle NetSuite environment.
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

3. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
