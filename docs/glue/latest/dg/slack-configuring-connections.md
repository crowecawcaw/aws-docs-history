# Configuring Slack connections

Slack supports the `AUTHORIZATION_CODE` grant type for OAuth 2.

This grant type is considered “three-legged” OAuth as it relies on redirecting users to the third party authorization server
to authenticate the user. It is used when creating connections via the AWS Glue Console. The AWS Glue Console will redirect the user to Slack
where the user must login and allow AWS Glue the requested permissions to access their Slack instance.

Users may still opt to create their own connected app in Slack and provide their own client id and client secret
when creating connections through the AWS Glue Console. In this scenario, they will still be redirected to Slack to
login and authorize AWS Glue to access their resources.

This grant type results in a refresh token and access token. The access token expires after 1 hour of creation. A new access
token can be fetched using the refresh token.

For more information on creating a connected app for Authorization Code OAuth flow, see
[Slack API](https://api.slack.com/quickstart "https://api.slack.com/quickstart") .

To configure an Slack connection:

1. In AWS Secrets Manager, create a secret with the following details. You must create a secret for
   the connection in AWS Glue.
   1. For customer managed connected app – Secret should contain the
      connected app Consumer Secret with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.

2. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select Slack.
   2. Provide the Slack environment.
   3. Select the IAM role which AWS Glue can assume and has permissions for following actions:

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
