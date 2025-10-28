# Configuring Docusign Monitor connections

Docusign Monitor supports the AUTHORIZATION_CODE grant type.

- This grant type is considered three-legged OAuth as it relies on redirecting users to the third-party authorization server to authenticate the user. It is used when creating connections via the AWS Glue console.
- Users may opt to create their own connected app in Docusign Monitor and provide their own client ID and client secret when creating connections through the AWS Glue console. In this scenario, they will still be redirected to Docusign Monitor to login and authorize AWS Glue to access their resources.
- This grant type results in a refresh token and an access token. The access token is short lived, and may be refreshed automatically without user interaction using the refresh token.
- For public Docusign Monitor documentation on creating a connected app for the Authorization Code OAuth flow, see [OAuth for Docusign Connect](https://developers.docusign.com/platform/webhooks/connect/validation-and-security/oauth-connect/ "https://developers.docusign.com/platform/webhooks/connect/validation-and-security/oauth-connect/").
  To configure a Docusign Monitor connection:

1. In AWS Secrets Manager, create a secret with the following details:
   1. For the customer managed connected app, the Secret should contain the connected app API key with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.
   2. Note: you must create a secret for your connections in AWS Glue.

1. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. Under **Connections**, choose **Create connection**.
   2. When selecting a **Data Source**, select Docusign Monitor.
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

   4. Provide the **User Managed Client Application ClientId** of the Docusign Monitor app.
   5. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens.
   6. Select the network options if you want to use your network.

1. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
