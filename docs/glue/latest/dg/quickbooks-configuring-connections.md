# Configuring QuickBooks connections

QuickBooks supports the AUTHORIZATION_CODE grant type for OAuth2. The grant type determines how AWS Glue communicates with QuickBooks to request access to your data.

- This grant type is considered "three-legged" OAuth as it relies on redirecting users to a third-party authorization server to authenticate the user. It is used when creating connections via the AWS Glue console.
- Users may still opt to create their own connected app in QuickBooks and provide their own client ID and client secret when creating connections through the AWS Glue console. In this scenario, they will still be redirected to QuickBooks to login and authorize AWS Glue to access their resources.
- This grant type results in a refresh token and access token. The access token is short lived, and may be refreshed automatically without user interaction using the refresh token.
- For public QuickBooks documentation on creating a connected app for Authorization Code OAuth flow, see [Set up OAuth 2.0](https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0 "https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0").
  To configure a QuickBooks connection:

1. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select QuickBooks.
   2. Provide the instance URL and company ID of the QuickBooks instance you want to connect to.
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

2. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
