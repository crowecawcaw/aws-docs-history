# Configuring Zoho CRM connections

The grant type determines how AWS Glue communicates with Zoho CRM to request access to your data. Your choice affects the requirements that you must meet before you create the connection. Zoho CRM supports only the AUTHORIZATION_CODE grant type for OAuth 2.0.

- This grant type is considered "three-legged" OAuth as it relies on redirecting users to a third-party authorization server to authenticate the user. It is used when creating connections via the AWS Glue console. The AWS Glue console will redirect the user to Zoho CRM where the user must login and allow Glue the requested permissions to access their Zoho CRM instance.
- Users may still opt to create their own connected app in Zoho CRM and provide their own client ID, Auth URL, Token URL, and Instance URL when creating connections through the AWS Glue console. In this scenario, they will still be redirected to Zoho CRM to login and authorize AWS Glue to access their resources.
- This grant type results in a refresh token and access token. The access token will remain valid for one hour, and may be refreshed automatically without user interaction using the refresh token.
- For public Zoho CRM documentation on creating a connected app for Authorization Code OAuth flow, see [Authentication](https://www.zoho.com/crm/developer/docs/api/v7/oauth-overview.html "https://www.zoho.com/crm/developer/docs/api/v7/oauth-overview.html").
  To configure a Zoho CRM connection:

1. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select Zoho CRM.
   2. Provide the `INSTANCE_URL` of the Zoho CRM instance you want to connect to.
   3. Provide the user client application client ID.
   4. Select the appropriate **Auth URL** from the dropdown.
   5. Select the appropriate **Token URL** from the dropdown.
   6. Select the AWS IAM role which AWS Glue can assume and has permissions for following actions:

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

   7. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens.
   8. Select the network options if you want to use your network.

2. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
3. In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.
