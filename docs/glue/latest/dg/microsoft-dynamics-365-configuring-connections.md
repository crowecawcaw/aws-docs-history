# Configuring Microsoft Dynamics 365 CRM connections

**AUTHORIZATION_CODE Grant Type**

- This grant type is considered “three-legged” OAuth as it relies on redirecting users to the third party authorization server to
  authenticate the user. It is used when creating connections via the AWS Glue Console. The AWS Glue Console will redirect the user to
  Microsoft Dynamics 365 CRM where the user must login and allow AWS Glue the requested permissions to access their Microsoft Dynamics 365 CRM
  instance.
- Users may opt to create their own connected app in Microsoft Dynamics 365 CRM and provide their own client id and client secret when creating
  connections through the AWS Glue Console. In this scenario, they will still be redirected to Microsoft Dynamics 365 CRM to login and authorize AWS Glue to access
  their resources.
- This grant type results in a refresh token and access token. The access token is short lived, and may be refreshed automatically
  without user interaction using the refresh token.
- For public Microsoft Dynamics 365 CRM documentation on creating a connected app for Authorization Code OAuth flow, see | Microsoft Learn.
  [Microsoft App Registration](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth#app-registration "https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth#app-registration").
  Microsoft Dynamics 365 CRM supports OAuth2.0 authentication.

To configure a Microsoft Dynamics 365 CRM connection:

1. In AWS Secrets Manager, create a secret with the following details. It is required to create a secret for
   each connection in AWS Glue.
   - For AuthorizationCode grant type:

   For customer managed connected app - Secret should contain the connected app Client Secret with
   `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.

2. In AWS Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Data Source**, select Microsoft Dynamics 365 CRM.
   2. Select the **INSTANCE_URL** of the Microsoft Dynamics 365 CRM instance you want to connect to.
   3. Select the IAM role that AWS Glue can assume and has permissions for following actions:

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

   4. Select **Token URL** and **Authorization Code URL** to access your Microsoft Dynamics 365 CRM workspace.
   5. Provide **User Managed Client Application ClientId** of your Microsoft Dynamics 365 CRM app.
   6. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens.
   7. Select the network options if you want to use your network.

3. Grant the IAM role associated with your AWS Glue job permission to read `secretName`. Choose
   **Next**.
4. In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.
