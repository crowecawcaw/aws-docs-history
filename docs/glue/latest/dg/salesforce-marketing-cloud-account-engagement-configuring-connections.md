# Configuring Salesforce Marketing Cloud Account Engagement connections

The grant type determines how AWS Glue communicates with Salesforce Marketing Cloud Account Engagement to request access to your data. Your choice affects the requirements that you must meet before you create the connection. Salesforce Marketing Cloud Account Engagement supports only the AUTHORIZATION_CODE grant type for OAuth 2.0.

- This grant type is considered "three-legged" OAuth as it relies on redirecting users to a third-party authorization server to authenticate the user. It is used when creating connections via the AWS Glue console.
- Users may still opt to create their own connected app in Salesforce Marketing Cloud Account Engagement and provide their own client ID and client secret when creating connections through the AWS Glue console. In this scenario, they will still be redirected to Salesforce Marketing Cloud Account Engagement to login and authorize AWS Glue to access their resources.
- This grant type results in a refresh token and access token. The access token is short lived, and may be refreshed automatically without user interaction using the refresh token.
- For public Salesforce Marketing Cloud Account Engagement documentation on creating a connected app for Authorization Code OAuth flow, see [Authentication](https://developer.salesforce.com/docs/marketing/pardot/guide/version5overview.html#authentication "https://developer.salesforce.com/docs/marketing/pardot/guide/version5overview.html#authentication").
  To configure a Salesforce Marketing Cloud Account Engagement connection:

1. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select Salesforce Marketing Cloud Account Engagement.
   2. Provide the `INSTANCE_URL` of the Salesforce Marketing Cloud Account Engagement instance you want to connect to.
   3. Provide the `PARDOT_BUSINESS_UNIT_ID` of the Salesforce Marketing Cloud Account Engagement instance you want to connect to.
   4. Select the appropriate **Authorization Code URL** from the dropdown.
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

   7. Provide the User Managed Client Application Client ID (the client ID from the connected app).
   8. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens. The selected secret needs to have a key `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` with the value being the Client Secret from the connected app.
   9. Select the network options if you want to use your network.

2. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
3. In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.
