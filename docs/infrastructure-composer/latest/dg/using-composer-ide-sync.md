# Sync Infrastructure Composer to deploy to the AWS Cloud

Use the **sync** button in AWS Infrastructure Composer from the AWS Toolkit for Visual Studio Code to deploy your application to the AWS Cloud.

The **sync** button initiates the `sam sync` command from the AWS SAM Command Line Interface (CLI).

The `sam sync` command can deploy new applications or quickly sync changes that you make locally to the
AWS Cloud. Running `sam sync` may include the following:

- Building your application with `sam build` to prepare your local application files for deployment by
  creating or updating a local `.aws-sam` directory.
- For resources that support AWS service APIs, the AWS SAM CLI will use the APIs to deploy your changes.
  The AWS SAM CLI does this to quickly update your resources in the cloud.
- If necessary, the AWS SAM CLI performs an AWS CloudFormation deployment to update your entire stack through a
  change set.
  The `sam sync` command is best suited for rapid development environments when quickly updating your cloud
  resources can benefit your development and testing workflows.

To learn more about `sam sync`, see [Using sam sync](../../../serverless-application-model/latest/developerguide/using-sam-cli-sync.md "../../../serverless-application-model/latest/developerguide/using-sam-cli-sync.md") in the
_AWS Serverless Application Model Developer Guide_.

## Set up

To use the **sync** feature in Infrastructure Composer, you must have the AWS SAM CLI installed on your
local machine. For instructions, see [Installing the AWS SAM CLI](../../../serverless-application-model/latest/developerguide/install-sam-cli.md "../../../serverless-application-model/latest/developerguide/install-sam-cli.md") in the _AWS Serverless Application Model Developer Guide_.

When you use the **sync** feature in Infrastructure Composer, the AWS SAM CLI references your configuration
file for the information it needs to sync your application to the AWS Cloud. For instructions on creating, modifying, and
using configuration files, see [Configure project settings](../../../serverless-application-model/latest/developerguide/using-sam-cli-configure.md#using-sam-cli-configure-project "../../../serverless-application-model/latest/developerguide/using-sam-cli-configure.md#using-sam-cli-configure-project") in the _AWS Serverless Application Model Developer Guide_.

## Sync and deploy your application

###### To sync your application to the AWS Cloud

1. Select the **sync** button on the Infrastructure Composer canvas.
2. You may receive a prompt to confirm that you are working with a development stack. Select **OK** to
   continue.
3. Infrastructure Composer may prompt you to configure the following options:
   - **AWS Region** – The region to sync your application to.
   - **AWS CloudFormation stack name** – The name of your AWS CloudFormation stack. You can select an existing stack name or create a new one.
   - **Amazon Simple Storage Service (Amazon S3) bucket** – The name of your Amazon S3 bucket. The AWS SAM CLI will package and store your application files
     and function code here. You can select an existing bucket or create a new one.

Infrastructure Composer will initiate the AWS SAM CLI `sam sync` command and open a terminal window in your IDE to output its progress.
