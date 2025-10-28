# Configuring Zendesk connections

The Zendesk connector supports the Authorization Code grant type.

- This grant type is considered "three-legged" OAuth as it relies on redirecting users to a third-party authorization server to authenticate the user. It is used when creating connections via the AWS Glue console. The user creating a connection may by default rely on an AWS Glue-owned connected app (AWS Glue-managed client application) where they do not need to provide any OAuth related information except for their Zendesk instance URL. The AWS Glue console will redirect the user to Zendesk where the user must login and allow AWS Glue the requested permissions to access their Zendesk instance.
- You may still opt to create your own connected app in Zendesk and provide your own client ID and client secret when creating connections through the AWS Glue console. In this scenario, you will still be redirected to Zendesk to login and authorize AWS Glue to access your resources.
- This grant type results in an access token. The access token never expires.
  For public Zendesk documentation on creating a connected app for the Authorization Code OAuth flow, see [OAuth Tokens for Grant Types](https://developer.zendesk.com/api-reference/ticketing/oauth/grant_type_tokens/ "https://developer.zendesk.com/api-reference/ticketing/oauth/grant_type_tokens/").

To configure a Zendesk connection:

1. In AWS Secrets Manager, create a secret with the following details:
   1. For the AuthorizationCode grant type: for a customer managed connected app the secret should contain the connected app Consumer Secret with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.
   2. Note: You must create a secret per connection in AWS Glue.

2. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select Zendesk.
   2. Provide the INSTANCE_URL of the Zendesk you want to connect to.
   3. Provide the Zendesk environment.
   4. Select the AWS IAM role which AWS Glue can assume and has permissions for following actions:

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

   5. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens.
   6. Select the network options if you want to use your network.

3. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
