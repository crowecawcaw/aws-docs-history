

# Local testing with AWS SAM CLI
<a name="using-sam-cli-local-testing"></a>

The AWS SAM CLI enables you to test serverless applications locally across different infrastructure as code (IaC) tools. This guide explains how to use the AWS SAM CLI for local testing with various IaC frameworks.

Key benefits of using AWS SAM CLI for local testing include:
+ **Rapid development** - Test code changes without deploying to AWS
+ **Cost efficiency** - Develop and test without incurring AWS charges
+ **Offline capability** - Work on your applications without an internet connection
+ **Simplified debugging** - Step through Lambda function code locally using a debugger
+ **Realistic testing** - Test your applications using local emulation of AWS services

## Test AWS SAM applications locally
<a name="using-sam-cli-local-testing-sam"></a>

For information about testing applications defined using AWS SAM templates, see [Testing and debugging serverless applications](serverless-test-and-debug.md) in this guide.

## Test CloudFormation templates locally
<a name="using-sam-cli-local-testing-cfn"></a>

To use the AWS SAM CLI's local testing capabilities with CloudFormation, add the AWS SAM transform to your CloudFormation template. For more information, see [AWS SAM template anatomy](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html) for:
+ Adding AWS SAM transform to CloudFormation templates
+ Understanding template compatibility
+ Exploring serverless resource syntax

## Test AWS CDK applications locally
<a name="using-sam-cli-local-testing-cdk"></a>

You can use the AWS SAM CLI to test AWS CDK applications locally after you synthesize the AWS CDK application to CloudFormation templates using the cdk synth command.

For more information, look at [Locally test and build AWS CDK applications with the AWS SAM CLI](https://docs.aws.amazon.com/cdk/v2/guide/testing-locally.html) in the AWS CDK developer guide. This includes:
+ [Getting started with locally testing](https://docs.aws.amazon.com/cdk/v2/guide/testing-locally.html#testing-locally-getting-started)
+ [Local testing AWS CDK applications with AWS SAM](https://docs.aws.amazon.com/cdk/v2/guide/testing-locally.html#testing-locally-sam)

## Test Terraform applications locally
<a name="using-sam-cli-local-testing-terraform"></a>

The AWS SAM CLI supports Terraform projects and Terraform Cloud. You can use it to perform local debugging and testing of: Lambda functions and layers and the Amazon API Gateway HTTP and REST APIs.

To set up your environment and learn about all available features, see [Terraform Support](terraform-support.md) in this guide. This includes:
+ [Getting started with Terraform support for AWS SAM CLI](gs-terraform-support.md)
+ [Using the AWS SAM CLI with Terraform for local debugging and testing](using-samcli-terraform.md)