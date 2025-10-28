# Local testing with AWS SAM CLI

The AWS SAM CLI enables you to test serverless applications locally across different infrastructure as code (IaC) tools. This guide explains how to use the AWS SAM CLI for local testing with various IaC frameworks.

Key benefits of using AWS SAM CLI for local testing include:

- **Rapid development** - Test code changes without deploying to AWS
- **Cost efficiency** - Develop and test without incurring AWS charges
- **Offline capability** - Work on your applications without an internet connection
- **Simplified debugging** - Step through Lambda function code locally using a debugger
- **Realistic testing** - Test your applications using local emulation of AWS services

## Test AWS SAM applications locally

For information about testing applications defined using AWS SAM templates, see [Testing and debugging serverless applications](serverless-test-and-debug.md "serverless-test-and-debug.md") in this guide.

## Test AWS CloudFormation templates locally

To use the AWS SAM CLI's local testing capabilities with AWS CloudFormation, add the AWS SAM transform to your AWS CloudFormation template. For more information, see [AWS SAM template anatomy](sam-specification-template-anatomy.md "sam-specification-template-anatomy.md") for:

- Adding AWS SAM transform to AWS CloudFormation templates
- Understanding template compatibility
- Exploring serverless resource syntax

## Test AWS CDK applications locally

You can use the AWS SAM CLI to test AWS CDK applications locally after you synthesize the AWS CDK application to AWS CloudFormation templates using the cdk synth command.

For more information, look at [Locally test and build AWS CDK applications with the AWS SAM CLI](../../../cdk/v2/guide/testing-locally.md "../../../cdk/v2/guide/testing-locally.md") in the AWS CDK developer guide. This includes:

- [Getting started with locally testing](../../../cdk/v2/guide/testing-locally.md#testing-locally-getting-started "../../../cdk/v2/guide/testing-locally.md#testing-locally-getting-started")
- [Local testing AWS CDK applications with AWS SAM](../../../cdk/v2/guide/testing-locally.md#testing-locally-sam "../../../cdk/v2/guide/testing-locally.md#testing-locally-sam")

## Test Terraform applications locally

The AWS SAM CLI supports Terraform projects and Terraform Cloud. You can use it to perform local debugging and testing of: Lambda functions and layers and the Amazon API Gateway HTTP and REST APIs.

To set up your environment and learn about all available features, see [Terraform Support](terraform-support.md "terraform-support.md") in this guide. This includes:

- [Getting started with Terraform support for AWS SAM CLI](gs-terraform-support.md "gs-terraform-support.md")
- [Using the AWS SAM CLI with Terraform for local debugging and testing](using-samcli-terraform.md "using-samcli-terraform.md")
