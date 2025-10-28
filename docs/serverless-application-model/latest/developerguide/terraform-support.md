# AWS SAM CLI Terraform support

This section covers using the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) with your Terraform projects and Terraform Cloud.

To provide feedback and submit feature requests, create a [GitHub
Issue](https://github.com/aws/aws-sam-cli/issues/new?labels=area%2Fterraform "https://github.com/aws/aws-sam-cli/issues/new?labels=area%2Fterraform").

###### Topics

- [Getting started with Terraform support for
  AWS SAM CLI](gs-terraform-support.md "gs-terraform-support.md")
- [Using the AWS SAM CLI with Terraform for local debugging
  and testing](using-samcli-terraform.md "using-samcli-terraform.md")
- [Using the AWS SAM CLI with Serverless.tf for local
  debugging and testing](using-samcli-serverlesstf.md "using-samcli-serverlesstf.md")
- [AWS SAM CLI with Terraform reference](terraform-reference.md "terraform-reference.md")
- [What is AWS SAM CLI support for
  Terraform?](#what-is-terraform-support "#what-is-terraform-support")

## What is AWS SAM CLI support for

Terraform?

Use the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) with your Terraform projects or Terraform Cloud to
perform local debugging and testing of:

- AWS Lambda functions and layers.
- Amazon API Gateway APIs.

For an introduction to Terraform, see [What is Terraform?](https://developer.hashicorp.com/terraform/intro "https://developer.hashicorp.com/terraform/intro")
at the _HashiCorp Terraform website_.

To provide feedback and submit feature requests, create a [GitHub
Issue](https://github.com/aws/aws-sam-cli/issues/new?labels=area%2Fterraform "https://github.com/aws/aws-sam-cli/issues/new?labels=area%2Fterraform").

###### Note

As part of the parsing step of AWS SAM CLI's integration, AWS SAM CLI processes user commands generate project files and data.
The command output should remain unchanged, but in certain environments, the environment or runner may inject additional logs or information in the output.

###### Topics

- [What is the AWS SAM CLI?](#what-is-terraform-support-sam-cli "#what-is-terraform-support-sam-cli")
- [How do I use the AWS SAM CLI with Terraform?](#what-is-terraform-support-how "#what-is-terraform-support-how")
- [Next steps](#what-is-terraform-support-next "#what-is-terraform-support-next")

### What is the AWS SAM CLI?

The AWS SAM CLI is a command line tool that you can use with AWS SAM templates and supported third-party integrations, such as Terraform, to build and run your
serverless applications. For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli").

The AWS SAM CLI supports the following commands for Terraform:

- `sam local invoke` – Initiate a one-time invocation of an AWS Lambda function resource locally. To learn
  more about this command, see [Introduction to testing with sam local invoke](using-sam-cli-local-invoke.md "using-sam-cli-local-invoke.md").
- `sam local start-api` – Run your Lambda resources locally and test through a local HTTP server host. This type of testing is helpful for Lambda
  functions that are invoked by an API Gateway endpoint. To learn more about this command, see
  [Introduction to testing with sam local start-api](using-sam-cli-local-start-api.md "using-sam-cli-local-start-api.md").
- `sam local start-lambda` – Start a local endpoint for your Lambda
  function in order to invoke your function locally using AWS Command Line Interface (AWS CLI) or SDKs. To
  learn more about this command, see [Introduction to testing with sam local start-lambda](using-sam-cli-local-start-lambda.md "using-sam-cli-local-start-lambda.md").

### How do I use the AWS SAM CLI with Terraform?

The [core Terraform workflow](https://developer.hashicorp.com/terraform/intro/core-workflow "https://developer.hashicorp.com/terraform/intro/core-workflow") consists of three stages:
**Write**, **Plan**, and **Apply**. With AWS SAM CLI support for Terraform,
you can take advantage of the AWS SAM CLI `sam local` set of commands while continuing to use your Terraform workflows to manage your applications on AWS.
Generally, this means the following:

- **Write** – Author your infrastructure as code using Terraform.
- **Test and debug** – Use the AWS SAM CLI to locally test and debug your applications.
- **Plan** – Preview changes before applying.
- **Apply** – Provision your infrastructure.

For an example of using the AWS SAM CLI with Terraform, see [Better together: AWS SAM CLI and HashiCorp Terraform](https://aws.amazon.com/blogs/compute/better-together-aws-sam-cli-and-hashicorp-terraform/ "https://aws.amazon.com/blogs/compute/better-together-aws-sam-cli-and-hashicorp-terraform/") at the _AWS Compute Blog_.

### Next steps

To complete all prerequisites and set up Terraform, see [Getting started with Terraform support for
AWS SAM CLI](gs-terraform-support.md "gs-terraform-support.md").
