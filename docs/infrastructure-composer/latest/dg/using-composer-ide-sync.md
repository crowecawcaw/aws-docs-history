

# Sync Infrastructure Composer to deploy to the AWS Cloud
<a name="using-composer-ide-sync"></a>

Use the **sync** button in AWS Infrastructure Composer from the AWS Toolkit for Visual Studio Code to deploy your application to the AWS Cloud.

The **sync** button initiates the `sam sync` command from the AWS SAM Command Line Interface (CLI).

The `sam sync` command can deploy new applications or quickly sync changes that you make locally to the AWS Cloud. Running `sam sync` may include the following:
+ Building your application with `sam build` to prepare your local application files for deployment by creating or updating a local `.aws-sam` directory.
+ For resources that support AWS service APIs, the AWS SAM CLI will use the APIs to deploy your changes. The AWS SAM CLI does this to quickly update your resources in the cloud.
+ If necessary, the AWS SAM CLI performs an AWS CloudFormation deployment to update your entire stack through a change set.

The `sam sync` command is best suited for rapid development environments when quickly updating your cloud resources can benefit your development and testing workflows.

To learn more about `sam sync`, see [Using sam sync](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-sync.html) in the *AWS Serverless Application Model Developer Guide*.

## Set up
<a name="using-composer-ide-sync-setup"></a>

To use the **sync** feature in Infrastructure Composer, you must have the AWS SAM CLI installed on your local machine. For instructions, see [Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) in the *AWS Serverless Application Model Developer Guide*.

When you use the **sync** feature in Infrastructure Composer, the AWS SAM CLI references your configuration file for the information it needs to sync your application to the AWS Cloud. For instructions on creating, modifying, and using configuration files, see [ Configure project settings](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-configure.html#using-sam-cli-configure-project) in the *AWS Serverless Application Model Developer Guide*.

## Sync and deploy your application
<a name="using-composer-ide-sync-use"></a>

**To sync your application to the AWS Cloud**

1. Select the **sync** button on the Infrastructure Composer canvas.

1. You may receive a prompt to confirm that you are working with a development stack. Select **OK** to continue.

1. Infrastructure Composer may prompt you to configure the following options:
   + **AWS Region** – The region to sync your application to.
   + **CloudFormation stack name** – The name of your CloudFormation stack. You can select an existing stack name or create a new one.
   + **Amazon Simple Storage Service (Amazon S3) bucket** – The name of your Amazon S3 bucket. The AWS SAM CLI will package and store your application files and function code here. You can select an existing bucket or create a new one.

Infrastructure Composer will initiate the AWS SAM CLI `sam sync` command and open a terminal window in your IDE to output its progress.