# Examples: Invoking Lambda functions from your RDS for PostgreSQL DB instance

Following, you can find several examples of calling the [aws_lambda.invoke](PostgreSQL-Lambda-functions.md#aws_lambda.invoke "PostgreSQL-Lambda-functions.md#aws_lambda.invoke") function. Most of the examples
use the composite structure `aws_lambda_arn_1` that you create in [Step 4: Use Lambda helper functions with your
RDS for PostgreSQL DB instance (Optional)](PostgreSQL-Lambda.md#PostgreSQL-Lambda-specify-function "PostgreSQL-Lambda.md#PostgreSQL-Lambda-specify-function") to simplify passing the function details.
For an example of asynchronous invocation, see [Example: Asynchronous (Event) invocation of Lambda functions](#PostgreSQL-Lambda-Event "#PostgreSQL-Lambda-Event"). All the other examples listed use synchronous invocation.

To learn more about Lambda invocation types, see [Invoking Lambda functions](../../../lambda/latest/dg/lambda-invocation.md "../../../lambda/latest/dg/lambda-invocation.md")
in the _AWS Lambda Developer Guide_.
For more information about `aws_lambda_arn_1`,
see [aws_commons.create_lambda_function_arn](PostgreSQL-Lambda-functions.md#aws_commons.create_lambda_function_arn "PostgreSQL-Lambda-functions.md#aws_commons.create_lambda_function_arn").

###### Examples list

- [Example: Synchronous (RequestResponse) invocation of Lambda functions](#PostgreSQL-Lambda-RequestResponse "#PostgreSQL-Lambda-RequestResponse")
- [Example: Asynchronous (Event) invocation of Lambda functions](#PostgreSQL-Lambda-Event "#PostgreSQL-Lambda-Event")
- [Example: Capturing the Lambda execution log in a function response](#PostgreSQL-Lambda-log-response "#PostgreSQL-Lambda-log-response")
- [Example: Including client context in a Lambda function](#PostgreSQL-Lambda-client-context "#PostgreSQL-Lambda-client-context")
- [Example: Invoking a specific
  version of a Lambda function](#PostgreSQL-Lambda-function-version "#PostgreSQL-Lambda-function-version")

## Example: Synchronous (RequestResponse) invocation of Lambda functions

Following are two examples of a synchronous Lambda function invocation. The results of these `aws_lambda.invoke` function calls are the same.

```
SELECT * FROM aws_lambda.invoke('aws_lambda_arn_1', '{"body": "Hello from Postgres!"}'::json);

```

```
SELECT * FROM aws_lambda.invoke('aws_lambda_arn_1', '{"body": "Hello from Postgres!"}'::json, 'RequestResponse');
```

The parameters are described as follows:

- `:'aws_lambda_arn_1'` – This parameter identifies the composite structure
  created in [Step 4: Use Lambda helper functions with your
  RDS for PostgreSQL DB instance (Optional)](PostgreSQL-Lambda.md#PostgreSQL-Lambda-specify-function "PostgreSQL-Lambda.md#PostgreSQL-Lambda-specify-function"), with the `aws_commons.create_lambda_function_arn` helper
  function. You can also create this structure
  inline within your `aws_lambda.invoke` call as follows.

```
SELECT * FROM aws_lambda.invoke(aws_commons.create_lambda_function_arn('my-function', '`aws-region`'),
'{"body": "Hello from Postgres!"}'::json
);
```

- `'{"body": "Hello from
PostgreSQL!"}'::json` – The JSON payload to pass to
  the Lambda function.
- `'RequestResponse'` – The Lambda invocation type.

## Example: Asynchronous (Event) invocation of Lambda functions

Following is an example of an asynchronous Lambda function invocation. The
`Event` invocation type schedules the Lambda function invocation with
the specified input payload and returns immediately. Use the `Event`
invocation type in certain workflows that don't depend on the results of the
Lambda function.

```
SELECT * FROM aws_lambda.invoke('aws_lambda_arn_1', '{"body": "Hello from Postgres!"}'::json, 'Event');
```

## Example: Capturing the Lambda execution log in a function response

You can include the last 4 KB of the execution log in the function
response by using the `log_type` parameter in your `aws_lambda.invoke`
function call. By default, this parameter is set to `None`, but you can specify `Tail` to
capture the results of the Lambda execution log in the response, as shown following.

```
SELECT *, select convert_from(decode(log_result, 'base64'), 'utf-8') as log FROM aws_lambda.invoke(:'aws_lambda_arn_1', '{"body": "Hello from Postgres!"}'::json, 'RequestResponse', 'Tail');
```

Set the [aws_lambda.invoke](PostgreSQL-Lambda-functions.md#aws_lambda.invoke "PostgreSQL-Lambda-functions.md#aws_lambda.invoke")
function's `log_type` parameter to `Tail` to include the
execution log in the response. The default value for the `log_type`
parameter is `None`.

The `log_result` that's returned is a `base64` encoded
string. You can decode the contents using a combination of the `decode`
and `convert_from` PostgreSQL functions.

For more information about `log_type`, see [aws_lambda.invoke](PostgreSQL-Lambda-functions.md#aws_lambda.invoke "PostgreSQL-Lambda-functions.md#aws_lambda.invoke").

## Example: Including client context in a Lambda function

The `aws_lambda.invoke` function has a `context` parameter that you can
use to pass information separate from the payload, as shown following.

```
SELECT *, convert_from(decode(log_result, 'base64'), 'utf-8') as log FROM aws_lambda.invoke(:'aws_lambda_arn_1', '{"body": "Hello from Postgres!"}'::json, 'RequestResponse', 'Tail');
```

To include client context, use a JSON object for the [aws_lambda.invoke](PostgreSQL-Lambda-functions.md#aws_lambda.invoke "PostgreSQL-Lambda-functions.md#aws_lambda.invoke") function's
`context` parameter.

For more information about the `context` parameter, see the [aws_lambda.invoke](PostgreSQL-Lambda-functions.md#aws_lambda.invoke "PostgreSQL-Lambda-functions.md#aws_lambda.invoke") reference.

## Example: Invoking a specific

version of a Lambda function

You can specify a particular version of a Lambda function by including the `qualifier`
parameter with the `aws_lambda.invoke` call. Following, you can find an
example that does this using `'`custom_version`'`
as an alias for the version.

```
SELECT * FROM aws_lambda.invoke('aws_lambda_arn_1', '{"body": "Hello from Postgres!"}'::json, 'RequestResponse', 'None', NULL, '`custom_version`');
```

You can also supply a Lambda function qualifier with the function name
details instead, as follows.

```
SELECT * FROM aws_lambda.invoke(aws_commons.create_lambda_function_arn('my-function:custom_version', 'us-west-2'),
'{"body": "Hello from Postgres!"}'::json);
```

For more information about `qualifier` and other parameters, see the [aws_lambda.invoke](PostgreSQL-Lambda-functions.md#aws_lambda.invoke "PostgreSQL-Lambda-functions.md#aws_lambda.invoke") reference.
