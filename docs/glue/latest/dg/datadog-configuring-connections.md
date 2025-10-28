# Configuring Datadog connections

Datadog supports custom authentication. Following are the steps to configure Datadog
connection:

To configure a Datadog connection:

1. In AWS Secrets Manager, create a secret with the following details:

For customer managed connected app – Secret should contain the
connected app Consumer Secret with `**API\_KEY**` and `**APPLICATION\_KEY**` as keys.

###### Note

It is a must to create a secret per connection in AWS Glue. 2. In AWS Glue Studio, create a connection under **Data Connections**
by following the steps below:

    1. When selecting a **Connection type**, select
     Datadog.
    2. Provide the `Instance_Url` of the Datadog you want to
     connect to.
    3. Select the IAM role for which AWS Glue can assume and has permissions
     for following actions:



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
    4. Select the `secretName` which you want to use for this
     connection in AWS Glue to put the tokens.
    5. Select the network options if you want to use your network.

3. Grant the IAM role associated with your AWS Glue job permission to read
   `secretName`.
