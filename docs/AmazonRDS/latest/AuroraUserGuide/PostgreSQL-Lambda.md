# Invoking an AWS Lambda function from an

Aurora PostgreSQL DB cluster

AWS Lambda is an event-driven compute service that lets you run code without provisioning or managing servers. It's available for use
with many AWS services, including Aurora PostgreSQL.
For example, you can use Lambda functions to process event notifications from a database, or to load data from files whenever a new file is uploaded to
Amazon S3. To learn more about Lambda,
see [What is AWS Lambda?](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") in the _AWS Lambda Developer Guide._

###### Note

Invoking AWS Lambda functions is supported in Aurora PostgreSQL 11.9 and higher (including Aurora Serverless v2).

Setting up Aurora PostgreSQL
to work with Lambda functions is a multi-step process involving AWS Lambda, IAM, your VPC, and
your Aurora PostgreSQL DB cluster.
Following, you can find summaries of the necessary steps.

For more information about Lambda functions, see [Getting started with Lambda](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md") and
[AWS Lambda foundations](../../../lambda/latest/dg/lambda-foundation.md "../../../lambda/latest/dg/lambda-foundation.md") in
the _AWS Lambda Developer Guide_.

###### Topics

- [Step 1: Configure your Aurora PostgreSQL DB cluster for outbound connections to AWS Lambda](#PostgreSQL-Lambda-network "#PostgreSQL-Lambda-network")
- [Step 2: Configure IAM for your Aurora PostgreSQL DB cluster and AWS Lambda](#PostgreSQL-Lambda-access "#PostgreSQL-Lambda-access")
- [Step 3: Install the aws_lambda extension for an Aurora PostgreSQL DB cluster](#PostgreSQL-Lambda-install-extension "#PostgreSQL-Lambda-install-extension")
- [Step 4: Use Lambda helper functions with your
  Aurora PostgreSQL DB cluster (Optional)](#PostgreSQL-Lambda-specify-function "#PostgreSQL-Lambda-specify-function")
- [Step 5: Invoke a Lambda function from your Aurora PostgreSQL DB cluster](#PostgreSQL-Lambda-invoke "#PostgreSQL-Lambda-invoke")
- [Step 6: Grant other users permission to invoke Lambda functions](#PostgreSQL-Lambda-grant-users-permissions "#PostgreSQL-Lambda-grant-users-permissions")
- [Examples: Invoking Lambda functions from your Aurora PostgreSQL DB cluster](PostgreSQL-Lambda-examples.md "PostgreSQL-Lambda-examples.md")
- [Lambda function error messages](PostgreSQL-Lambda-errors.md "PostgreSQL-Lambda-errors.md")
- [AWS Lambda function and parameter reference](PostgreSQL-Lambda-functions.md "PostgreSQL-Lambda-functions.md")

## Step 1: Configure your Aurora PostgreSQL DB cluster for outbound connections to AWS Lambda

Lambda functions always run inside an Amazon VPC that's owned by the AWS Lambda service. Lambda applies network access and security rules to this
VPC and it maintains and monitors the VPC automatically. Your Aurora PostgreSQL DB cluster
sends network traffic to the Lambda service's VPC.
How you configure this depends on whether your Aurora DB cluster's primary
DB instance is public or private.

- Public Aurora PostgreSQL DB
  cluster – A DB
  cluster's primary DB instance is public if it's located in a public subnet on your
  VPC, and if the instance's "PubliclyAccessible" property is
  `true`. To find the value of this property, you can use the
  [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") AWS CLI command. Or, you can use the AWS Management Console
  to open the **Connectivity & security** tab and check that
  **Publicly accessible** is **Yes**. To
  verify that the instance is in the public subnet of your VPC, you can use the
  AWS Management Console or the AWS CLI.

To set up access to Lambda, you use the AWS Management Console or the AWS CLI to create an
outbound rule on your VPC's security group. The outbound rule specifies
that TCP can use port 443 to send packets to any IPv4 addresses
(0.0.0.0/0).

- Private Aurora PostgreSQL DB
  cluster – In this case, the instance's
  "PubliclyAccessible" property is `false` or it's in a
  private subnet. To allow the instance to work with Lambda, you can use a Network
  Address Translation) NAT gateway. For more information, see [NAT
  gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md"). Or, you can configure your VPC with a VPC endpoint for
  Lambda. For more information, see [VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the _Amazon VPC User Guide_. The
  endpoint responds to calls made by your Aurora PostgreSQL
  DB cluster to your Lambda functions.

Your VPC can now interact with the AWS Lambda VPC at the network level. Next, you configure the permissions using IAM.

## Step 2: Configure IAM for your Aurora PostgreSQL DB cluster and AWS Lambda

Invoking Lambda functions from your Aurora PostgreSQL DB cluster
requires certain privileges. To configure the necessary privileges, we recommend that you create an IAM policy that allows invoking Lambda functions, assign that policy to a role, and then apply
the role to your DB cluster.
This approach gives the DB cluster privileges to
invoke the specified Lambda function on your behalf. The following steps show you how to do this using the AWS CLI.

###### To configure IAM permissions for using your cluster with Lambda

1. Use the [create-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-policy.html") AWS CLI
   command to create an IAM policy that allows your
   Aurora PostgreSQL DB cluster to invoke the specified Lambda function. (The statement ID (Sid)
   is an optional description for your policy statement and has no effect on usage.) This policy gives your Aurora DB cluster the minimum permissions needed to invoke the specified Lambda function.

```
aws iam create-policy  --policy-name `rds-lambda-policy` --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Sid": "AllowAccessToExampleFunction",
        "Effect": "Allow",
        "Action": "lambda:InvokeFunction",
        "Resource": "arn:aws:lambda:``aws-region`:444455556666:function:my-function`"
        }
    ]
}'
```

Alternatively, you can use the predefined `AWSLambdaRole`
policy that allows you to invoke any of your Lambda functions. For more information, see
[Identity-based IAM policies for Lambda](../../../lambda/latest/dg/access-control-identity-based.md#access-policy-examples-aws-managed "../../../lambda/latest/dg/access-control-identity-based.md#access-policy-examples-aws-managed") 2. Use the [create-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html") AWS CLI
command to create an IAM role that the policy can assume at runtime.

```
aws iam create-role  --role-name `rds-lambda-role` --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": "rds.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
        }
    ]
}'
```

3. Apply the policy to the role by using the [attach-role-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-role-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-role-policy.html") AWS CLI
   command.

```
aws iam attach-role-policy \
    --policy-arn arn:aws:iam::`444455556666`:policy/`rds-lambda-policy` \
    --role-name `rds-lambda-role` --region `aws-region`

```

4. Apply the role to your Aurora PostgreSQL DB cluster
   by using the

[add-role-to-db-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/add-role-to-db-cluster.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/add-role-to-db-cluster.html")

AWS CLI command. This last step
allows your DB cluster's database users to invoke Lambda functions.

```
aws rds add-role-to-db-cluster \
       --db-cluster-identifier `my-cluster-name` \
       --feature-name Lambda \
       --role-arn  arn:aws:iam::`444455556666:role/rds-lambda-role`   \
       --region `aws-region`
```

With the VPC and the IAM configurations complete, you can now install the `aws_lambda` extension. (Note that you can
install the extension at any time, but until you set up the correct VPC support and IAM privileges, the `aws_lambda`
extension adds nothing to your Aurora PostgreSQL DB cluster's
capabilities.)

## Step 3: Install the `aws_lambda` extension for an Aurora PostgreSQL DB cluster

To use AWS Lambda with your Aurora PostgreSQL DB
cluster,
add the `aws_lambda` PostgreSQL extension to your Aurora PostgreSQL DB cluster. This extension
provides your Aurora PostgreSQL DB cluster with the ability to call
Lambda functions from PostgreSQL.

###### To install the `aws_lambda` extension in your

Aurora PostgreSQL DB cluster

Use the PostgreSQL `psql` command-line or the pgAdmin tool to connect to your
Aurora PostgreSQL DB cluster .

1. Connect to your Aurora PostgreSQL DB cluster
   instance as a user with `rds_superuser`
   privileges. The default `postgres` user is shown in the example.

```
psql -h `cluster-instance.444455556666.`aws-region``.rds.amazonaws.com -U postgres -p 5432
```

2. Install the `aws_lambda` extension. The `aws_commons` extension is also required. It
   provides helper functions to `aws_lambda` and many other Aurora extensions for PostgreSQL. If it's
   not already on your Aurora PostgreSQLDB cluster
   , it's installed with
   `aws_lambda` as shown following.

```
CREATE EXTENSION IF NOT EXISTS aws_lambda CASCADE;
`NOTICE: installing required extension "aws_commons"
CREATE EXTENSION`
```

The `aws_lambda` extension is installed in your Aurora PostgreSQL DB cluster's primary
DB instance. You can now create convenience structures for invoking your Lambda functions.

## Step 4: Use Lambda helper functions with your

Aurora PostgreSQL DB cluster (Optional)

You can use the helper functions in the `aws_commons` extension to prepare entities that you can more easily invoke from PostgreSQL. To do this,
you need to have the following information about your Lambda functions:

- **Function name** – The name, Amazon Resource Name (ARN), version, or alias of the Lambda function. The IAM
  policy created in [Step 2: Configure IAM for your cluster
  and Lambda](#PostgreSQL-Lambda-access "#PostgreSQL-Lambda-access")
  requires the ARN, so we recommend that you use your function's ARN.
- **AWS Region** – (Optional) The AWS Region where the
  Lambda function is located if it's not in the same Region as your
  Aurora PostgreSQL DB cluster.

To hold the Lambda function name information, you use the [aws_commons.create_lambda_function_arn](PostgreSQL-Lambda-functions.md#aws_commons.create_lambda_function_arn "PostgreSQL-Lambda-functions.md#aws_commons.create_lambda_function_arn") function. This helper function
creates an `aws_commons._lambda_function_arn_1` composite structure with
the details needed by the invoke function. Following, you can find three alternative
approaches to setting up this composite structure.

```
SELECT aws_commons.create_lambda_function_arn(
   'my-function',
   '`aws-region`'
) AS aws_lambda_arn_1 \gset

```

```
SELECT aws_commons.create_lambda_function_arn(
   '111122223333:function:my-function',
   '`aws-region`'
) AS lambda_partial_arn_1 \gset

```

```
SELECT aws_commons.create_lambda_function_arn(
   'arn:aws:lambda:`aws-region`:111122223333:function:my-function'
) AS lambda_arn_1 \gset
```

Any of these values can be used in calls to the [aws_lambda.invoke](PostgreSQL-Lambda-functions.md#aws_lambda.invoke "PostgreSQL-Lambda-functions.md#aws_lambda.invoke") function. For
examples, see [Step 5: Invoke a Lambda function from your Aurora PostgreSQL DB cluster](#PostgreSQL-Lambda-invoke "#PostgreSQL-Lambda-invoke").

## Step 5: Invoke a Lambda function from your Aurora PostgreSQL DB cluster

The `aws_lambda.invoke` function behaves synchronously or asynchronously, depending on the `invocation_type`.
The two alternatives for this parameter are `RequestResponse` (the default) and `Event`, as follows.

- **`RequestResponse`** – This invocation type is _synchronous_. It's the
  default behavior when the call is made without specifying an invocation type. The response
  payload includes the results of the `aws_lambda.invoke` function. Use this invocation type when your workflow requires receiving results from the Lambda function
  before proceeding.
- **`Event`** – This invocation type is _asynchronous_.
  The response doesn't include a payload containing results. Use this invocation type when
  your workflow doesn't need a result from the Lambda function to continue processing.

As a simple test of your setup, you can connect to your DB instance using `psql` and invoke an example function from the command line.
Suppose that
you have one of the basic functions set up on your Lambda service, such as the simple Python function shown in the following screenshot.

![Example Lambda function shown in the AWS CLI for AWS Lambda](images/lambda_simple_function.png)

###### To invoke an example function

1. Connect to your primary DB instance using `psql` or pgAdmin.

```
psql -h `cluster.444455556666.`aws-region``.rds.amazonaws.com -U postgres -p 5432
```

2. Invoke the function using its ARN.

```
SELECT * from aws_lambda.invoke(aws_commons.create_lambda_function_arn('arn:aws:lambda:`aws-region`:444455556666:function:simple', 'us-west-1'), '{"body": "Hello from Postgres!"}'::json );
```

The response looks as follows.

```
`status_code | payload | executed_version | log_result
-------------+-------------------------------------------------------+------------------+------------
 200 | {"statusCode": 200, "body": "\"Hello from Lambda!\""} | $LATEST |
(1 row)`
```

If your invocation attempt doesn't succeed, see [Lambda function error messages](PostgreSQL-Lambda-errors.md "PostgreSQL-Lambda-errors.md") .

## Step 6: Grant other users permission to invoke Lambda functions

At this point in the procedures, only you as `rds_superuser` can invoke your Lambda functions. To allow other users to invoke any functions that you create, you
need to grant them permission.

###### To grant others permission to invoke Lambda functions

1. Connect to your primary DB instance using `psql` or pgAdmin.

```
psql -h `cluster.444455556666.`aws-region``.rds.amazonaws.com -U postgres -p 5432
```

2. Run the following SQL commands:

```
`postgres=>`  GRANT USAGE ON SCHEMA aws_lambda TO `db_username`;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA aws_lambda TO `db_username`;
```
