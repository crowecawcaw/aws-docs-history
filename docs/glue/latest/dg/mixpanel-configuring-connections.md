# Configuring Mixpanel connections

Mixpanel supports username and password for `BasicAuth`. Basic
Authentication is a simple authentication method where clients provide credentials
directly to access protected resources. AWS Glue is able to use the username and password
to authenticate Mixpanel APIs.

For public Mixpanel documentation about `BasicAuth` flow, see [Mixpanel Service
Accounts](https://developer.mixpanel.com/reference/service-accounts "https://developer.mixpanel.com/reference/service-accounts") .

To configure a Mixpanel connection:

1. In AWS Secrets Manager, create a secret with the following details:
   - For Basic Authentication, Secret should contain the
     connected app Consumer Secret with `USERNAME` and `PASSWORD` as key.

   ###### Note

   It is a must to create a secret per connection in AWS Glue.

2. In the AWS Glue Studio, create a connection under **Data
   Connections** by following the steps below:
   1. When selecting a **Connection type**, select
      **Mixpanel**.
   2. Provide the `INSTANCE_URL` of the Mixpanel that you want to connect to.
   3. Select the IAM role for which AWS Glue can assume and has
      permissions for the following actions:

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
   5. Select **Network options** if you want to use
      your network.

3. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
