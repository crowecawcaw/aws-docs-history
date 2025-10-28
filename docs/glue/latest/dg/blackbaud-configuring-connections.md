# Configuring Blackbaud Raiser's Edge NXT connections

Blackbaud Raiser's Edge NXT supports the AUTHORIZATION_CODE grant type for OAuth2.

- This grant type is considered "three-legged" OAuth as it relies on redirecting users to a third-party authorization server to authenticate the user. It is used when creating connections via the AWS Glue console. The AWS Glue console will redirect the user to Blackbaud Raiser's Edge NXT where the user must login and allow AWS Glue the requested permissions to access their Blackbaud Raiser's Edge NXT instance.
- Users may opt to create their own connected app in Blackbaud Raiser's Edge NXT and provide their own Client ID, Subscription Key, and Instance URL when creating connections through the AWS Glue console. In this scenario, they will still be redirected to Blackbaud Raiser's Edge NXT to login and authorize AWS Glue to access their resources.
- This grant type results in a refresh token and access token. The access token is short lived, and may be refreshed automatically without user interaction using the refresh token.
- For public Blackbaud Raiser’s Edge NXT documentation on creating a connected app for Authorization Code OAuth flow, see [Authorization](https://developer.blackbaud.com/skyapi/docs/authorization "https://developer.blackbaud.com/skyapi/docs/authorization").
  To configure a Blackbaud Raiser's Edge NXT connection:

1. In AWS Secrets Manager, create a secret with the following details:
   1. For the customer managed connected app, the Secret should contain the connected app API key with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.
   2. Note: you must create a secret for your connections in AWS Glue.

1. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Data Source**, select Blackbaud Raiser's Edge NXT.
   2. Provide the `INSTANCE_URL` of the Blackbaud Raiser's Edge NXT account you want to connect to.
   3. Provide the user managed client application `clientId`.
   4. Provide the subscription key associated with your account.
   5. Select the AWS IAM role which AWS Glue can assume and has permissions for following actions:

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

   6. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens.
   7. Select the network options if you want to use your network.

1. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
