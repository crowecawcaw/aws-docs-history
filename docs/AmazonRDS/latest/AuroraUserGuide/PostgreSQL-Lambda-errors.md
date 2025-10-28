# Lambda function error messages

In the following list you can find information about error messages, with possible causes
and solutions.

- VPC configuration issues

VPC configuration issues can raise the following error messages when trying to connect:

```
`ERROR: invoke API failed
DETAIL: AWS Lambda client returned 'Unable to connect to endpoint'.
CONTEXT: SQL function "invoke" statement 1`
```

A common cause for this error is improperly configured VPC security group. Make sure you have an outbound rule
for TCP open on port 443 of your VPC security group so that your VPC can connect to the Lambda VPC.

- Lack of permissions needed to invoke Lambda functions

If you see either of the following error messages, the user (role) invoking the function doesn't have proper permissions.

```
ERROR:  permission denied for schema aws_lambda
```

```
ERROR:  permission denied for function invoke
```

A user (role) must be given specific grants to invoke Lambda functions. For more information,
see [Step 6: Grant other users permission to invoke Lambda functions](PostgreSQL-Lambda.md#PostgreSQL-Lambda-grant-users-permissions "PostgreSQL-Lambda.md#PostgreSQL-Lambda-grant-users-permissions").

- Improper handling of errors in your Lambda functions

If a Lambda function throws an exception during request processing,
`aws_lambda.invoke` fails with a PostgreSQL error such as the
following.

```
SELECT * FROM aws_lambda.invoke('aws_lambda_arn_1', '{"body": "Hello from Postgres!"}'::json);
`ERROR: lambda invocation failed
DETAIL: "arn:aws:lambda:us-west-2:555555555555:function:my-function" returned error "Unhandled", details: "<Error details string>".`
```

Be sure to handle errors in your Lambda functions or in your PostgreSQL application.
