# Configuring Adobe Analytics connections

Adobe Analytics supports `AUTHORIZATION_CODE` grant type for
`OAuth2`.

This grant type is considered “three-legged” `OAuth` as it relies on
redirecting users to the third-party authorization server to authenticate the user.
Users may opt to create their own connected app in Adobe Analytics and provide their own
client ID and client secret when creating connections through the AWS Glue console. In this
scenario, they will still be redirected to Adobe Analytics to login and authorize AWS Glue
to access their resources.

This grant type results in a refresh token and access token. The access token is short
lived, and may be refreshed automatically without user interaction using the refresh
token.

For public Adobe Analytics documentation on creating a connected app for AUTHORIZATION_CODE OAuth flow, see [Adobe Analytics APIs](https://adobedocs.github.io/analytics-2.0-apis/ "https://adobedocs.github.io/analytics-2.0-apis/") .

To configure a Adobe Analytics connection:

1. In AWS Secrets Manager, create a secret with the following details:

For customer managed connected app – Secret should contain the
connected app Consumer Secret with
`USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.

###### Note

It is a must to create a secret per connection in AWS Glue. 2. In AWS Glue Studio, create a connection under **Data Connections**
by following the steps below:

    1. When selecting a **Connection type**, select
     Adobe Analytics.
    2. Provide the `x_api_key, instanceUrl` of the Adobe Analytics you want to connect to.
    3. Select the IAM role for which AWS Glue can assume and has permissions
     for following actions:



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
    4. Select the `secretName` which you want to use for this
     connection in AWS Glue to put the tokens.
    5. Select the network options if you want to use your network.

3. Grant the IAM role associated with your AWS Glue job permission to read
   `secretName`.
