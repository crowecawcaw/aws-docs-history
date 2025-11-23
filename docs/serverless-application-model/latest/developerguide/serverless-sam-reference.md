# AWS SAM reference

This section contains AWS SAM reference material. This includes AWS SAM CLI reference material,
like reference information on AWS SAM CLI commands and additional AWS SAM CLI information, like configuration, version control, and troubleshooting information.
Additionally, this section includes reference information on the AWS SAM specification and the AWS SAM template, like reference information on connectors, image repositories, and deployments.

## AWS SAM specification and the AWS SAM template

The AWS SAM specification is an open-source specification under the Apache 2.0 license. The
current version of the AWS SAM specification is available in the [AWS SAM template](sam-specification.md "sam-specification.md"). AWS SAM specification comes with
a simplified short-hand syntax you use to define the functions, events, APIs, configurations,
and permissions of your serverless application.

You interact with AWS SAM specification through the AWS SAM application project directory, which are the folders and files that are created when you run the **sam init** command.
This directory includes the AWS SAM template, an important file that defines your AWS resources. The AWS SAM template is an extension of a AWS CloudFormation template. For the full reference for CloudFormation
templates, see [Template reference](../../../AWSCloudFormation/latest/UserGuide/template-reference.md "../../../AWSCloudFormation/latest/UserGuide/template-reference.md")
in the _AWS CloudFormation User Guide_.

## AWS SAM CLI command reference

The AWS Serverless Application Model Command Line Interface (AWS SAM CLI) is a command line tool that you can use
with AWS SAM templates and supported third-party integrations to build and run your serverless
applications.

You can use the AWS SAM CLI commands to develop, test, and deploy your serverless
applications to the AWS Cloud. The following are some examples of AWS SAM CLI commands:

- `sam init` – If you're a first-time AWS SAM CLI user, you can run the
  `sam init` command without any parameters to create a Hello World
  application. The command generates a preconfigured AWS SAM template and example application
  code in the language that you choose.
- `sam local invoke` and `sam local start-api` – Use these
  commands to test your application code locally, before deploying it to the
  AWS Cloud.
- `sam logs` – Use this command to fetch logs that your Lambda function
  generates. This can help you with testing and debugging your application after you've
  deployed it to the AWS Cloud.
- `sam package` – Use this command to bundle your application code and
  dependencies into a _deployment package_. You need the
  deployment package to upload your application to the AWS Cloud.
- `sam deploy` – Use this command to deploy your serverless
  application to the AWS Cloud. It creates the AWS resources and sets permissions and
  other configurations that are defined in the AWS SAM template.

For instructions about installing the AWS SAM CLI, see [Install the AWS SAM CLI](install-sam-cli.md "install-sam-cli.md").

## AWS SAM policy templates

With AWS SAM, you can choose from a list of policy templates to scope your AWS Lambda
function's permissions to the resources that your application uses. For a list of available policy templates,
refer to [Policy template table](serverless-policy-templates.md#serverless-policy-template-table "serverless-policy-templates.md#serverless-policy-template-table").
For general information on policy templates and AWS SAM, refer to [AWS SAM policy templates](serverless-policy-templates.md "serverless-policy-templates.md").

## Topics

- [AWS SAM template](sam-specification.md "sam-specification.md")
- [AWS SAM CLI command reference](serverless-sam-cli-command-reference.md "serverless-sam-cli-command-reference.md")
- [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md")
- [AWS SAM connector reference](reference-sam-connector.md "reference-sam-connector.md")
- [AWS SAM policy templates](serverless-policy-templates.md "serverless-policy-templates.md")
- [Image repositories for AWS SAM](serverless-image-repositories.md "serverless-image-repositories.md")
- [Telemetry in the AWS SAM CLI](serverless-sam-telemetry.md "serverless-sam-telemetry.md")
- [Set up and manage resource access in your AWS SAM template](sam-permissions.md "sam-permissions.md")
