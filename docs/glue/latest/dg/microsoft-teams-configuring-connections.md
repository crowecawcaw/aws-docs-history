# Configuring Microsoft Teams connections

Microsoft Teams supports following two types for authentication mechanism:

1.  OAuth Auth: Microsoft Teams supports AUTHORIZATION_CODE grant type for OAuth2.

        * This grant type is considered “three-legged” OAuth as it relies on redirecting users to the third party authorization server to
         authenticate the user. It is used when creating connections via the AWS Glue Console. The user creating a connection may by default rely on a
         AWS Glue-owned connected app where they do not need to provide any OAuth related information except for the Microsoft Teams instanceurl. The AWS Glue
         Console will redirect the user to Microsoft Teams where the user must login and allow AWS Glue the requested permissions to access their Microsoft Teams
         instance.
        * Users may opt to create their own connected app in Microsoft Teams and provide their own client id and client secret when creating
         connections through the AWS Glue Console. In this scenario, they will still be redirected to Microsoft Teams to login and authorize AWS Glue to access
         their resources.
        * This grant type results in a refresh token and access token. The access token is active for one hour, and may be refreshed automatically
         without user interaction using the refresh token.
        * For public Microsoft Teams documentation on creating a connected app for Authorization Code OAuth flow, see | Microsoft Learn.
         [Register an application with the Microsoft identity platform - Microsoft Graph](https://learn.microsoft.com/en-us/graph/auth-register-app-v2 "https://learn.microsoft.com/en-us/graph/auth-register-app-v2").

    To configure a Microsoft Teams connection:

1.  In AWS Secrets Manager, create a secret with the following details. It is required to create a secret for
    each connection in AWS Glue.
    1. For OAuth auth:
       - For customer managed connected app - Secret should contain the connected app Consumer Secret with
         USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET as key.

1.  In AWS Glue Studio, create a connection under **Data Connections** by following the steps below:
    1. Under Data Connections, choose **Create connection**.
    2. When selecting a **Data Source**, select Microsoft Teams.
    3. Provide your Microsoft Teams **Tenant ID**.
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

    5. Provide User Managed Client Application ClientId of Microsoft Teams app.
    6. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens.
    7. Select the network options if you want to use your network.

1.  Grant the IAM role associated with your AWS Glue job permission to read `secretName`. Choose
    **Next**.
1.  In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.
