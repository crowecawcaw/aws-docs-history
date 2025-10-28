# Configuring Stripe connections

Stripe supports custom authentication. For more information on generating the required API keys for custom authorization,
see [STRIPE REST API Documentation](https://docs.stripe.com/api/authentication "https://docs.stripe.com/api/authentication").

To configure a Stripe connection:

1. In AWS Secrets Manager, create a secret with the following details. It is required to create a secret for
   each connection in AWS Glue.
   1. For customer managed connected app – Secret should contain the
      connected app Consumer Secret with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.

2. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select Stripe.
   2. Select the IAM role which AWS Glue can assume and has permissions for following actions:

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

   3. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens.
   4. Select the network options if you want to use your network.

3. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
