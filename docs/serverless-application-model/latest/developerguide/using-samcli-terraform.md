# Using the AWS SAM CLI with Terraform for local debugging

and testing

This topic covers how to use supported AWS Serverless Application Model Command Line Interface (AWS SAM CLI) commands with your
Terraform projects and Terraform Cloud.

To provide feedback and submit feature requests, create a [GitHub
Issue](https://github.com/aws/aws-sam-cli/issues/new?labels=area%2Fterraform "https://github.com/aws/aws-sam-cli/issues/new?labels=area%2Fterraform").

###### Topics

- [Local testing with sam local
  invoke](#using-samcli-terraform-local-invoke "#using-samcli-terraform-local-invoke")
- [Local testing with sam local start-api](#using-samcli-terraform-local-start-api "#using-samcli-terraform-local-start-api")
- [Local testing with sam local
  start-lambda](#using-samcli-terraform-local-start-lambda "#using-samcli-terraform-local-start-lambda")
- [Terraform limitations](#using-samcli-terraform-unsupported "#using-samcli-terraform-unsupported")

## Local testing with sam local

invoke

###### Note

To use the AWS SAM CLI to test locally, you must have Docker installed and configured. For
instructions, see [Installing Docker to use with the AWS SAM CLI](install-docker.md "install-docker.md").

The following is an example of testing your Lambda function locally by passing in an
event:

```
`$` `sam local invoke --hook-name terraform `hello_world_function` -e `events/event.json` -`
```

To learn more about using this command, see [Introduction to testing with sam local invoke](using-sam-cli-local-invoke.md "using-sam-cli-local-invoke.md").

## Local testing with sam local start-api

To use `sam local start-api` with Terraform, run the following:

```
`$` `sam local start-api --hook-name terraform`
```

The following is an example:

```
`$` `sam local start-api --hook-name terraform`

Running Prepare Hook to prepare the current application
Executing prepare hook of hook "terraform"
Initializing Terraform application
...
Creating terraform plan and getting JSON output
....
Generating metadata file

Unresolvable attributes discovered in project, run terraform apply to resolve them.

Finished generating metadata file. Storing in...
Prepare hook completed and metadata file generated at: ...
Mounting HelloWorldFunction at http://127.0.0.1:3000/hello [GET]
Mounting None at http://127.0.0.1:3000/hello [POST]
You can now browse to the above endpoints to invoke your functions. You do not need to restart/reload SAM CLI while working on your functions, changes will be reflected instantly/automatically. If you
used sam build before running local commands, you will need to re-run sam build for the changes to be picked up. You only need to restart SAM CLI if you update your AWS SAM template
2023-06-26 13:21:20  * Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)
```

To learn more about this command, see [Introduction to testing with sam local start-api](using-sam-cli-local-start-api.md "using-sam-cli-local-start-api.md").

### Lambda functions that use Lambda authorizers

For Lambda functions configured to use Lambda authorizers, the AWS SAM CLI will automatically invoke your Lambda
authorizer before invoking your Lambda function endpoint.

- To learn more about this feature in the AWS SAM CLI, see [Lambda functions that use Lambda authorizers](using-sam-cli-local-start-api.md#using-sam-cli-local-start-api-authorizers "using-sam-cli-local-start-api.md#using-sam-cli-local-start-api-authorizers").
- For more information on using Lambda authorizers in Terraform, see [Resource: aws_api_gateway_authorizer](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_authorizer#example-usage "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_authorizer#example-usage") in the _Terraform
  registry_.

## Local testing with sam local

start-lambda

The following is an example of testing your Lambda function locally with the AWS Command Line Interface (AWS CLI):

1. Use the AWS SAM CLI to create a local testing environment:

```
`$` `sam local start-lambda --hook-name terraform `hello_world_function``
```

2. Use the AWS CLI to invoke your function locally:

```
`$` `aws lambda invoke --function-name `hello_world_function` --endpoint-url `http://127.0.0.1:3001/ response.json --cli-binary-format raw-in-base64-out --payload file://events/event.json``
```

To learn more about this command, see [Introduction to testing with sam local start-lambda](using-sam-cli-local-start-lambda.md "using-sam-cli-local-start-lambda.md").

## Terraform limitations

The following are limitations when using the AWS SAM CLI with Terraform:

- Lambda functions linked to multiple layers.
- Terraform local variables that define links between resources.
- Referencing a Lambda function that hasn’t been created yet. This includes functions that are defined in the body
  attribute of the REST API resource.

To avoid these limitations, you can run `terraform apply` when a new resource is added.
