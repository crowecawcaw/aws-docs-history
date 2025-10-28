# Configuring LinkedIn connections

LinkedIn supports `AUTHORIZATION_CODE` grant type for OAuth2.

This grant type is considered “three-legged” `OAuth` as it relies on
redirecting users to the third-party authorization server to authenticate the user.
Users may opt to create their own connected app in LinkedIn and provide their own client
ID and client secret when creating connections through the AWS Glue console. In this
scenario, they will still be redirected to LinkedIn to login and authorize AWS Glue to
access their resources.

This grant type results in both a refresh token and an access token. The access
token expires 60 days after creation. A new access token can be obtained using the
refresh token.

For public LinkedIn documentation on creating a connected app for
`Authorization Code OAuth` flow, see [Authorization Code Flow (3-legged OAuth)](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?toc=%2Flinkedin%2Fmarketing%2Ftoc.json&bc=%2Flinkedin%2Fbreadcrumb%2Ftoc.json&view=li-lms-2024-07&tabs=HTTPS1 "https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?toc=%2Flinkedin%2Fmarketing%2Ftoc.json&bc=%2Flinkedin%2Fbreadcrumb%2Ftoc.json&view=li-lms-2024-07&tabs=HTTPS1").

###### Configuring a LinkedIn connection

1. In AWS Secrets Manager, create a secret with the following details:
   - For customer managed connected app – Secret should contain the connected app Consumer
     Secret with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET`
     as key.
   - For AWS Managed connected app – Empty secret or secret with some temporary value.

   ###### Note

   It is a must to create a secret per connection in AWS Glue.

2. In the AWS Glue Studio, create a connection under **Data
   Connections** by following the steps below:
   1. When selecting a **Connection type**, select
      **LinkedIn**.
   2. Provide the LinkedIn environment.
   3. Select the IAM role for which AWS Glue can assume and has
      permissions for following actions:

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
   5. Select the **Network options** if you want to use
      your network.

3. Grant the IAM role associated with your AWS Glue job permission to read
   `secretName`.
