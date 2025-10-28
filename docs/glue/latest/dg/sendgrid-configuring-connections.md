# Configuring SendGrid connections

SendGrid supports custom authentication.

For public SendGrid documentation on generating the required API keys for custom authentication, see [Authentication](https://www.twilio.com/docs/sendgrid/api-reference/how-to-use-the-sendgrid-v3-api/authentication "https://www.twilio.com/docs/sendgrid/api-reference/how-to-use-the-sendgrid-v3-api/authentication").

To configure a SendGrid connection:

1. In AWS Secrets Manager, create a secret with the following details:
   1. For the customer managed connected app, the Secret should contain the connected app Consumer Secret with `api_key` as key.
   2. Note: you must create a secret for your connections in AWS Glue.

1. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select SendGrid.
   2. Provide the `INSTANCE_URL` of the SendGrid instance you want to connect to.
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
