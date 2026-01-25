# Use stage variables for HTTP APIs in API Gateway

Stage variables are key-value pairs that you can define for a stage of an
HTTP API. They act like environment variables and can be used in your API
setup.

Stage variables are not intended to be used for sensitive data, such as credentials. To pass sensitive data to
integrations, use an AWS Lambda authorizer. You can pass sensitive data to integrations in the output of the Lambda
authorizer. To learn more, see [Lambda authorizer
response format](http-api-lambda-authorizer.md#http-api-lambda-authorizer.payload-format-response "http-api-lambda-authorizer.md#http-api-lambda-authorizer.payload-format-response").

## Example – Use a stage variable to customize the HTTP integration endpoint

For example, you can define a stage variable, and then set its value as an HTTP
endpoint for an HTTP proxy integration. Later, you can reference the endpoint by using
the associated stage variable name. By doing this, you can use the same API setup with a
different endpoint at each stage. Similarly, you can use stage variables to specify a
different AWS Lambda function integration for each stage of your API.

To use a stage variable to customize the HTTP integration endpoint, you must first
set the name and value of the stage variable (for example, `url`) with a
value of `example.com`. Next, set up an HTTP proxy integration. Instead
of entering the endpoint's URL, you can tell API Gateway to use the stage variable value,
`http://${stageVariables.url}`. This value tells API Gateway to
substitute your stage variable `${}` at runtime, depending on the stage
of your API.

You can reference stage variables in a similar way to specify a Lambda function
name or an AWS role ARN.

When specifying a Lambda function name as a stage variable value, you must configure the permissions on the
Lambda function manually. The following [add-permission](../../../cli/latest/reference/lambda/add-permission.md "../../../cli/latest/reference/lambda/add-permission.md") command configures the permission for the Lambda function:

```
aws lambda add-permission --function-name arn:aws:lambda:XXXXXX:your-lambda-function-name --source-arn arn:aws:execute-api:us-east-1:YOUR_ACCOUNT_ID:api_id/*/HTTP_METHOD/resource --principal apigateway.amazonaws.com --statement-id apigateway-access --action lambda:InvokeFunction
```
