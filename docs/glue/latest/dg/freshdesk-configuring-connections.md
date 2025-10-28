# Configuring Freshdesk connections

Freshdesk supports custom authentication.

For public Freshdesk documentation on generating the required API keys for custom authorization, see [Freshdesk authentication](https://developer.freshdesk.com/api/#authentication "https://developer.freshdesk.com/api/#authentication").

The following are the steps to configure Freshdesk connection:

- In AWS Secrets Manager, create a secret with the following details:
  - For customer managed connected app – the secret should contain the connected app API key with `apiKey` as key. Note that you must create a secret per connection in AWS Glue.

- In the AWS Glue Studio, create a connection under **Data Connections** by following the steps below:
  - When selecting a **Data source**, select Freshdesk.
  - Provide the `INSTANCE_URL` of the Freshdesk instance you want to connect to.
  - Select the AWS IAM role which AWS Glue can assume and has permissions for following actions:

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

  - Select the `secretName` that you want to use for this connection in AWS Glue to put the tokens.
  - Select the network options if you want to use your network.

- Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
- In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.
