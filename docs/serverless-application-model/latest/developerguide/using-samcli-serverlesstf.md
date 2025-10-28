# Using the AWS SAM CLI with Serverless.tf for local

debugging and testing

The AWS Serverless Application Model Command Line Interface (AWS SAM CLI) can be used with Serverless.tf modules for
local debugging and testing of your AWS Lambda functions and layers. The following AWS SAM CLI
commands are supported:

- `sam build`
- `sam local invoke`
- `sam local start-api`
- `sam local start-lambda`

###### Note

Serverless.tf version 4.6.0 and newer supports AWS SAM CLI integration.

To begin using the AWS SAM CLI with your Serverless.tf modules, update to the latest version of
Serverless.tf and the AWS SAM CLI.

Starting from **serverless.tf version 6.0.0**, you must set the `create_sam_metadata` parameter as `true`. This generates
the metadata resources that the AWS SAM CLI `sam build` command requires.

To learn more about Serverless.tf, see the [terraform-aws-lambda-module](https://registry.terraform.io/modules/terraform-aws-modules/lambda/aws/latest "https://registry.terraform.io/modules/terraform-aws-modules/lambda/aws/latest").
