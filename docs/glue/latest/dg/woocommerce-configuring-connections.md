# Configuring WooCommerce connections

WooCommerce supports custom authentication. For public WooCommerce documentation on generating the required API keys for custom authorization, see [Authentication – WooCommerce REST API Documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/#authentication "https://woocommerce.github.io/woocommerce-rest-api-docs/#authentication").

To configure a WooCommerce connection:

1. In AWS Secrets Manager, create a secret with the following details:
   - For a customer managed connected app, the Secret should contain the connected app Consumer Secret with `consumerKey` and `consumerSecret` as keys. Note: you must create a secret per connection in AWS Glue.

1. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select WooCommerce.
   2. Provide the `INSTANCE_URL` of the WooCommerce instance you want to connect to.
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
