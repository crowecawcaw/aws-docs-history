

# Set up for deploying with the AWS SAM CLI and Infrastructure Composer
<a name="other-services-cfn-sam-using"></a>

To deploy your application with AWS SAM, you first need to install and access the AWS CLI and the AWS SAM CLI. The topics in this section provide details on doing this.

## Install the AWS CLI
<a name="other-services-cfn-sam-prerequisites-aws"></a>

We recommend installing and setting up the AWS CLI before installing the AWS SAM CLI. For instructions, see [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

**Note**  
After installing the AWS CLI, you must configure AWS credentials. To learn more, see [Quick setup](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html) in the *AWS Command Line Interface User Guide*.

## Install the AWS SAM CLI
<a name="other-services-cfn-sam-prerequisites-sam"></a>

To install the AWS SAM CLI, see [Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) in the *AWS Serverless Application Model Developer Guide*.

## Access the AWS SAM CLI
<a name="w2aac23c13c13"></a>

If you use Infrastructure Composer from the AWS Management Console, you have the following options to use the AWS SAM CLI.

**Activate local sync mode**  
With local sync mode, your project folder, including the AWS SAM template, are automatically saved to your local machine. Infrastructure Composer structures your project directory in a way that AWS SAM recognizes. You can run the AWS SAM CLI from the root directory of your project.  
For more information about **local sync** mode, see [Locally sync and save your project in the Infrastructure Composer console](using-composer-project-local-sync.md).

**Export your template**  
You can export your template to your local machine. Then, run the AWS SAM CLI from the parent folder that contains the template. You can also use the `--template-file` option with any AWS SAM CLI command and provide the path to your template.

**Use Infrastructure Composer from the AWS Toolkit for Visual Studio Code**  
You can use Infrastructure Composer from the Toolkit for VS Code to bring Infrastructure Composer to your local machine. Then, use Infrastructure Composer and the AWS SAM CLI from VS Code.

## Next steps
<a name="w2aac23c13c15"></a>

To deploy your application, refer to [Use Infrastructure Composer with AWS SAM to build and deploy](other-services-cfn-sam-examples-example1.md).