# AWS Lambda function and parameter reference

Following is the reference for the functions and parameters to use for invoking Lambda with
Aurora PostgreSQL
.

###### Functions and parameters

- [aws_lambda.invoke](#aws_lambda.invoke "#aws_lambda.invoke")
- [aws_commons.create_lambda_function_arn](#aws_commons.create_lambda_function_arn "#aws_commons.create_lambda_function_arn")
- [aws_lambda parameters](#aws_lambda.parameters "#aws_lambda.parameters")

## aws_lambda.invoke

Runs a Lambda function for an
Aurora PostgreSQL DB cluster
.

For more details about invoking Lambda functions, see also [Invoke](../../../lambda/latest/dg/API_Invoke.md "../../../lambda/latest/dg/API_Invoke.md") in
the _AWS Lambda Developer Guide._

**Syntax**

JSON

```
aws_lambda.invoke(
IN function_name TEXT,
IN payload JSON,
IN region TEXT DEFAULT NULL,
IN invocation_type TEXT DEFAULT 'RequestResponse',
IN log_type TEXT DEFAULT 'None',
IN context JSON DEFAULT NULL,
IN qualifier VARCHAR(128) DEFAULT NULL,
OUT status_code INT,
OUT payload JSON,
OUT executed_version TEXT,
OUT log_result TEXT)
```

```
aws_lambda.invoke(
IN function_name aws_commons._lambda_function_arn_1,
IN payload JSON,
IN invocation_type TEXT DEFAULT 'RequestResponse',
IN log_type TEXT DEFAULT 'None',
IN context JSON DEFAULT NULL,
IN qualifier VARCHAR(128) DEFAULT NULL,
OUT status_code INT,
OUT payload JSON,
OUT executed_version TEXT,
OUT log_result TEXT)
```

JSONB

```
aws_lambda.invoke(
IN function_name TEXT,
IN payload JSONB,
IN region TEXT DEFAULT NULL,
IN invocation_type TEXT DEFAULT 'RequestResponse',
IN log_type TEXT DEFAULT 'None',
IN context JSONB DEFAULT NULL,
IN qualifier VARCHAR(128) DEFAULT NULL,
OUT status_code INT,
OUT payload JSONB,
OUT executed_version TEXT,
OUT log_result TEXT)
```

```
aws_lambda.invoke(
IN function_name aws_commons._lambda_function_arn_1,
IN payload JSONB,
IN invocation_type TEXT DEFAULT 'RequestResponse',
IN log_type TEXT DEFAULT 'None',
IN context JSONB DEFAULT NULL,
IN qualifier VARCHAR(128) DEFAULT NULL,
OUT status_code INT,
OUT payload JSONB,
OUT executed_version TEXT,
OUT log_result TEXT
)
```

###### Input parameters

**function_name**

The identifying name of the Lambda function. The value can be the
function name, an ARN, or a partial ARN. For a listing of possible
formats, see [Lambda function name formats](../../../lambda/latest/dg/API_Invoke.md#API_Invoke_RequestParameters "../../../lambda/latest/dg/API_Invoke.md#API_Invoke_RequestParameters") in the _AWS Lambda Developer Guide._

_payload_

The input for the Lambda function. The format can be JSON or
JSONB. For more information, see [JSON Types](https://www.postgresql.org/docs/current/datatype-json.html "https://www.postgresql.org/docs/current/datatype-json.html")
in the PostgreSQL documentation.

_region_

(Optional) The Lambda Region for the function. By default, Aurora resolves the AWS Region from the full ARN in the
`function_name` or it uses the Aurora PostgreSQL
DB instance
Region. If this Region value conflicts with the one provided in the
`function_name` ARN, an error is raised.

_invocation_type_

The invocation type of the Lambda function. The value is
case-sensitive. Possible values include the following:

- `RequestResponse` – The default. This type
  of invocation for a Lambda function is synchronous and returns a
  response payload in the result. Use the
  `RequestResponse` invocation type when your
  workflow depends on receiving the Lambda function result
  immediately.
- `Event` – This type of invocation for a
  Lambda function is asynchronous and returns immediately without
  a returned payload. Use the `Event` invocation type
  when you don't need results of the Lambda function before your
  workflow moves on.
- `DryRun` – This type of invocation tests
  access without running the Lambda function.

_log_type_

The type of Lambda log to return in the `log_result` output
parameter. The value is case-sensitive. Possible values include the
following:

- Tail – The returned `log_result` output
  parameter will include the last 4 KB of the execution log.
- None – No Lambda log information is returned.

_context_

Client context in JSON or JSONB format. Fields to use include than
`custom` and `env`.

_qualifier_

A qualifier that identifies a Lambda function's version to be
invoked. If this value conflicts with one provided in the
`function_name` ARN, an error is raised.

###### Output parameters

_status_code_

An HTTP status response code. For more information, see [Lambda Invoke response elements](../../../lambda/latest/dg/API_Invoke.md#API_Invoke_ResponseElements "../../../lambda/latest/dg/API_Invoke.md#API_Invoke_ResponseElements") in the _AWS Lambda Developer Guide._

_payload_

The information returned from the Lambda function that ran. The format
is in JSON or JSONB.

_executed_version_

The version of the Lambda function that ran.

_log_result_

The execution log information returned if the `log_type`
value is `Tail` when the Lambda function was invoked. The
result contains the last 4 KB of the execution log encoded in
Base64.

## aws_commons.create_lambda_function_arn

Creates an `aws_commons._lambda_function_arn_1` structure to hold
Lambda function name information. You can use the results of the
`aws_commons.create_lambda_function_arn` function in the
`function_name` parameter of the aws_lambda.invoke [aws_lambda.invoke](#aws_lambda.invoke "#aws_lambda.invoke") function.

**Syntax**

```
aws_commons.create_lambda_function_arn(
    function_name TEXT,
    region TEXT DEFAULT NULL
    )
    RETURNS aws_commons._lambda_function_arn_1
```

###### Input parameters

_function_name_

A required text string containing the Lambda function name. The
value can be a function name, a partial ARN, or a full ARN.

_region_

An optional text string containing the AWS Region that the Lambda
function is in. For a listing of Region names and associated values, see
[Regions and Availability Zones](Concepts.md "Concepts.md").

## aws_lambda parameters

In this table, you can find parameters associated with the `aws_lambda` function.

| Parameter                       | Description                                                                                                                                                                                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aws_lambda.connect_timeout_ms` | This is a dynamic parameter and it sets the maximum wait time while connecting to AWS Lambda.<br>The default values is `1000`. Allowed values for this parameter are 1<br>• 900000.                                         |
| `aws_lambda.request_timeout_ms` | This is a dynamic parameter and it sets the maximum wait time while waiting for response from AWS Lambda.<br>The default values is `3000`. Allowed values for this parameter are 1<br>• 900000.                             |
| `aws_lambda.endpoint_override`  | Specifies the endpoint that can be used to connect to AWS Lambda. An empty string selects the default AWS Lambda endpoint for the region.<br>You must restart the database for this static parameter change to take effect. |
