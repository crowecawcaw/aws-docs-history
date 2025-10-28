# Set up for deploying with the AWS SAM CLI and Infrastructure Composer

To deploy your application with AWS SAM, you first need to install and access the AWS CLI and the AWS SAM CLI. The topics in this section provide details on doing this.

## Install the AWS CLI

We recommend installing and setting up the AWS CLI before installing the AWS SAM CLI. For instructions, see
[Install or update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

###### Note

After installing the AWS CLI, you must configure AWS credentials. To learn more, see [Quick setup](../../../cli/latest/userguide/getting-started-quickstart.md "../../../cli/latest/userguide/getting-started-quickstart.md") in the
_AWS Command Line Interface User Guide_.

## Install the AWS SAM CLI

To install the AWS SAM CLI, see [Installing the AWS SAM CLI](../../../serverless-application-model/latest/developerguide/install-sam-cli.md "../../../serverless-application-model/latest/developerguide/install-sam-cli.md")
in the _AWS Serverless Application Model Developer Guide_.

## Access the AWS SAM CLI

If you use Infrastructure Composer from the AWS Management Console, you have the following options to use the AWS SAM CLI.

**Activate local sync mode**

With local sync mode, your project folder, including the AWS SAM template, are automatically saved to your
local machine. Infrastructure Composer structures your project directory in a way that AWS SAM recognizes. You can run
the AWS SAM CLI from the root directory of your project.

For more information about **local sync** mode, see [Locally sync and save your
project in the Infrastructure Composer console](using-composer-project-local-sync.md "using-composer-project-local-sync.md").

**Export your template**

You can export your template to your local machine. Then, run the AWS SAM CLI from the
parent folder that contains the template. You can also use the `--template-file` option with any
AWS SAM CLI command and provide the path to your template.

**Use Infrastructure Composer from the AWS Toolkit for Visual Studio Code**

You can use Infrastructure Composer from the Toolkit for VS Code to bring Infrastructure Composer to your local machine. Then, use Infrastructure Composer and
the AWS SAM CLI from VS Code.

## Next steps

To deploy your application, refer to [Use Infrastructure Composer with AWS SAM to build and deploy](other-services-cfn-sam-examples-example1.md "other-services-cfn-sam-examples-example1.md").
