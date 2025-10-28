# API Gateway stage variables reference for REST APIs in API Gateway

You can use API Gateway stage variables in the following cases.

## Parameter mapping expressions

A stage variable can be used in a parameter mapping expression for an API method's request or response
header parameter, without any partial substitution. In the following example, the stage variable is referenced
without the `$` and the enclosing `{...}`.

- `stageVariables.<variable_name>`

## Mapping templates

A stage variable can be used anywhere in a mapping template, as shown in the following examples.

- `{ "name" : "$stageVariables.<variable_name>"}`
- `{ "name" : "${stageVariables.<variable_name>}"}`

## HTTP integration URIs

A stage variable can be used as part of an HTTP integration URL, as shown in the following examples:

- A full URI without protocol – `http://${stageVariables.<variable_name>}`
- A full domain –
  `http://${stageVariables.<variable_name>}/resource/operation`
- A subdomain –
  `http://${stageVariables.<variable_name>}.example.com/resource/operation`
- A path – `http://example.com/${stageVariables.<variable_name>}/bar`
- A query string – `http://example.com/foo?q=${stageVariables.<variable_name>}`

## AWS integration URIs

A stage variable can be used as part of AWS URI action or path components, as shown in the following
example.

- `arn:aws:apigateway:<region>:<service>:${stageVariables.<variable_name>}`

## AWS integration URIs (Lambda

functions)

A stage variable can be used in place of a Lambda function name, or version/alias, as shown in the following
examples.

- `arn:aws:apigateway:<region>:lambda:path/2015-03-31/functions/arn:aws:lambda:<region>:<account_id>:function:${stageVariables.<function_variable_name>}/invocations`
- `arn:aws:apigateway:<region>:lambda:path/2015-03-31/functions/arn:aws:lambda:<region>:<account_id>:function:<function_name>:${stageVariables.<version_variable_name>}/invocations`

###### Note

To use a stage variable for a Lambda function, the function must be in the same account as the API. Stage
variables don't support cross-account Lambda functions.

## Amazon Cognito user pool

A stage variable can be used in place of a Amazon Cognito user pool for a `COGNITO_USER_POOLS` authorizer.

- `arn:aws:cognito-idp:<region>:<account_id>:userpool/${stageVariables.<variable_name>}`

## AWS integration credentials

A stage variable can be used as part of AWS user/role credential ARN, as shown in the following example.

- `arn:aws:iam::<account_id>:${stageVariables.<variable_name>}`
