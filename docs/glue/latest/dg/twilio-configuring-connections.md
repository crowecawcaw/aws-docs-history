# Configuring Twilio connections

Twilio supports username and password for Basic Authentication. Basic Authentication is a simple authentication method where clients provide credentials directly to access protected resources. AWS Glue is able to use the username (Account SID) and password (Auth Token) to authenticate Twilio APIs.

For public Twilio documentation for Basic Authentication flow, see [Basic Authentication | Twilio](https://www.twilio.com/docs/glossary/what-is-basic-authentication "https://www.twilio.com/docs/glossary/what-is-basic-authentication").

To configure a Twilio connection:

1. In AWS Secrets Manager, create a secret with the following details:
   - For Basic Authentication: the Secret should contain the connected app Consumer Secret with the **Account SID** (Username) and **Auth Token** (Password).

   ###### Note

   You must create a secret for your connections in AWS Glue.

2. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select Twilio.
   2. Provide the `Edge_Location` of the Twilio instance you want to connect to.
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
