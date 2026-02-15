# API Gateway stage

variables reference for HTTP APIs in API Gateway

You can use API Gateway stage variables for HTTP APIs in the following cases.

## HTTP

integration URIs

You can use a stage variable as part of an HTTP integration URI, as shown in
the following examples.

- A full URI without protocol – `http://${stageVariables.<variable_name>}`
- A full domain – `http://${stageVariables.<variable_name>}/resource/operation`
- A subdomain – `http://${stageVariables.<variable_name>}.example.com/resource/operation`
- A path – `http://example.com/${stageVariables.<variable_name>}/bar`
- A query string – `http://example.com/foo?q=${stageVariables.<variable_name>}`

## Lambda functions

You can use a stage variable in place of a Lambda function integration name or alias, as
shown in the following examples.

- `arn:aws:apigateway:<region>:lambda:path/2015-03-31/functions/arn:aws:lambda:<region>:<account_id>:function:${stageVariables.<function_variable_name>}/invocations`
- `arn:aws:apigateway:<region>:lambda:path/2015-03-31/functions/arn:aws:lambda:<region>:<account_id>:function:<function_name>:${stageVariables.<version_variable_name>}/invocations`

###### Note

To use a stage variable for a Lambda function, the function must be in the same account as the API. Stage
variables don't support cross-account Lambda functions.

## AWS integration credentials

You can use a stage variable as part of an AWS user or role credential ARN,
as shown in the following example.

- `arn:aws:iam::<account_id>:${stageVariables.<variable_name>}`
