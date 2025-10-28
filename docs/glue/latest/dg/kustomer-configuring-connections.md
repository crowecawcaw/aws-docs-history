# Configuring Kustomer connections

To configure a Kustomer connection:

1. In AWS Secrets Manager, create a secret with the following details:
   1. For the customer managed connected app, the Secret should contain the connected app Consumer Secret with `apiKey` as the key.
   2. Note: you must create a secret for your connections in AWS Glue.

1. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. Under **Connections**, choose **Create connection**.
   2. When selecting a **Data Source**, select Kustomer.
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
