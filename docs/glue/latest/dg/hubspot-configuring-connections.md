# Configuring HubSpot connections

HubSpot supports the AUTHORIZATION_CODE grant type for OAuth2.

- This grant type is considered "three-legged" OAuth as it relies on redirecting users to a third-party authorization server to authenticate the user. It is used when creating connections via the AWS Glue console. The user creating a connection needs to provide the OAuth related information like Client ID and Client Secret for their HubSpot client application. The AWS Glue console will redirect the user to HubSpot where the user must login and allow AWS Glue the requested permissions to access their HubSpot instance.
- Users may still opt to create their own connected app in HubSpot and provide their own client id and client secret when creating connections through the AWS Glue console. In this scenario, they will still be redirected to HubSpot to login and authorize AWS Glue to access their resources.
- This grant type results in a refresh token and access token. The access token is short lived, and may be refreshed automatically without user interaction using the refresh token.
- For public HubSpot documentation on creating a connected app for Authorization Code OAuth flow, see [Public apps](https://developers.hubspot.com/docs/api/creating-an-app "https://developers.hubspot.com/docs/api/creating-an-app").
  To configure a HubSpot connection:

1. In AWS Secrets Manager, create a secret with the following details:
   1. For the customer managed connected app, the Secret should contain the connected app Consumer Secret with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.
   2. Note: You must create a secret for the connection in AWS Glue.

2. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select HubSpot.
   2. Provide the HubSpot environment.
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
4. In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.
