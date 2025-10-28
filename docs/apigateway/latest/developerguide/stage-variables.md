# Use stage variables for a REST API in API Gateway

Stage variables are key-value pairs that you can define as configuration attributes associated with a deployment
stage of a REST API. They act like environment variables and can be used in your API setup and mapping templates.
With deployment stages in API Gateway, you can manage multiple release stages for each API and use stage variables you can
configure an API deployment stage to interact with different backend endpoints.

Stage variables are not intended to be used for sensitive data, such as credentials. To pass sensitive data to
integrations, use an AWS Lambda authorizer. You can pass sensitive data to integrations in the output of the Lambda
authorizer. To learn more, see [Output from an API Gateway Lambda authorizer](api-gateway-lambda-authorizer-output.md "api-gateway-lambda-authorizer-output.md").

## Use cases for stage variables

The following are use cases for your stage variables.

**Specify a different backend endpoint**
Your API can pass a `GET` request as an HTTP proxy to the backend web host. You can use a
stage variable so that when API callers invoke your production endpoint, API Gateway calls `example.com`.
Then, when API callers invoke the beta stage, API Gateway calls a different web host, such as
`beta.example.com`. Similarly, stage variables can be used to specify a different AWS Lambda
function name for each stage in your API. You can't use a stage variable to set a different integration
endpoint, such as pointing the `GET` request to an HTTP proxy integration in one stage and a Lambda
proxy integration in another stage.

When specifying a Lambda function name as a stage variable value, you must configure the permissions on the
Lambda function manually. When you specify a Lambda function in the API Gateway console, a AWS CLI command will pop-up to configure the
proper permissions. You can also use the following AWS CLI command to do this.

```
aws lambda add-permission --function-name "arn:aws:lambda:`us-east-2`:`123456789012`:function:`my-function`" --source-arn "arn:aws:execute-api:`us-east-2`:`123456789012`:`api_id`/*/HTTP_METHOD/resource" --principal apigateway.amazonaws.com --statement-id apigateway-access --action lambda:InvokeFunction
```

**Pass information using mapping templates**
You can access stage variables in the mapping templates, or pass configuration parameters to your AWS Lambda
or HTTP backend. For example, you might want to reuse the same Lambda function for multiple stages in your API, but the
function should read data from a different Amazon DynamoDB table depending on the stage. In the
mapping templates that generate the request for the Lambda function, you can use stage variables to pass the table
name to Lambda.

To use a stage variable, you first configure a stage variable, and then you assign it a
value. For example, to customize the HTTP integration endpoint, first create the `url` stage variable,
and then in your API's integration request, enter the stage variable value,
`http://${stageVariables.url}`. This value tells API Gateway to substitute your stage variable
`${}` at runtime, depending on which stage your API is running. For more information, see [Set up stage variables for REST APIs in API Gateway](how-to-set-stage-variables-aws-console.md "how-to-set-stage-variables-aws-console.md").
