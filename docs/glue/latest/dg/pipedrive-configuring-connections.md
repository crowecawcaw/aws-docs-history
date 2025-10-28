# Configuring Pipedrive connections

Pipedrive supports AUTHORIZATION_CODE grant type for OAuth2.

- This grant type is considered “three-legged” OAuth as it relies on redirecting users to the third party authorization server to
  authenticate the user. It is used when creating connections via the AWS Glue Console. The user creating a connection may by default rely on a
  AWS Glue-owned connected app where they do not need to provide any OAuth related information except for the Pipedrive instanceurl. The AWS Glue
  Console will redirect the user to Pipedrive where the user must login and allow AWS Glue the requested permissions to access their Pipedrive
  instance.
- Users should opt to create their own connected app in Pipedrive and provide their own client id and client secret when creating
  connections through the AWS Glue Console. In this scenario, they will still be redirected to Pipedrive to login and authorize AWS Glue to access
  their resources.
- This grant type results in a refresh token and access token. The access token is active for one hour, and may be refreshed automatically
  without user interaction using the refresh token.
- For more information, see
  [documentation on creating a connected app for
  AUTHORIZATION_CODE OAuth flow](https://developers.pipedrive.com/docs/api/v1/Oauth "https://developers.pipedrive.com/docs/api/v1/Oauth").
  To configure a Pipedrive connection:

1. In AWS Secrets Manager, create a secret with the following details. It is required to create a secret for
   each connection in AWS Glue.
   1. For customer managed connected app - Secret should contain the connected app Consumer Secret with USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET as key.

2. In AWS Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. Under Data Connections, choose **Create connection**.
   2. When selecting a **Data Source**, select Pipedrive.
   3. Provide your Pipedrive **instanceURL**.
   4. Select the IAM role that AWS Glue can assume and has permissions for following actions:

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

   5. Provide the User Managed Client Application ClientId of the Pipedrive you want to connect to.
   6. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens.
   7. Select the network options if you want to use your network.

3. Grant the IAM role associated with your AWS Glue job permission to read `secretName`. Choose
   **Next**.
4. Provide the **connectionName** and choose **Next**.
5. On the next page choose **Create connection**. You will be asked to login into Pipedrive. Provide your username and
   password and choose **Log In**.
6. Once you are logged in, choose **Continue to the App**. Now your connection is ready to be used.
7. In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.
