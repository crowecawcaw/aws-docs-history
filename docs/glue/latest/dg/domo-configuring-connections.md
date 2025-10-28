# Configuring Domo connections

Domo supports the CLIENT_CREDENTIALS grant type for OAuth2.

- This grant type is considered two-legged OAuth as only the client application authenticates itself to the server, with no involvement to the user.
- Users may opt to create their own connected app in Domo and provide their own client ID and client secret when creating connections through the AWS Glue console.
- For public Domo documentation on creating a connected app for the Authorization Code OAuth flow, see [OAuth Authentication](https://developer.domo.com/portal/1845fc11bbe5d-api-authentication "https://developer.domo.com/portal/1845fc11bbe5d-api-authentication").
  To configure a Domo connection:

1. In AWS Secrets Manager, create a secret with the following details:
   1. For the customer managed connected app, the Secret should contain the connected app access token, `client_id`, and `client_secret`.
   2. Note: you must create a secret for your connections in AWS Glue.

1. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. Under **Connections**, choose **Create connection**.
   2. When selecting a **Data Source**, select Domo.
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

1. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
