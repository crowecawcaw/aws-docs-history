

# AWS SAM prerequisites
<a name="prerequisites"></a>

Complete the following prerequisites before installing and using the AWS Serverless Application Model Command Line Interface (AWS SAM CLI).

To use the AWS SAM CLI, you need the following:
+ An AWS account, AWS Identity and Access Management (IAM) credentials, and an IAM access key pair.
+ The AWS Command Line Interface (AWS CLI) to configure AWS credentials.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Step 1: Install the AWS CLI](#prerequisites-install-cli)
+ [Step 2: Use the AWS CLI to configure AWS credentials](#prerequisites-configure-credentials)
+ [Step 3: (Optional) Install AWS Toolkit for VS Code](#prerequisites-install-vscode)
+ [Next steps](#prerequisites-next-steps)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Step 1: Install the AWS CLI
<a name="prerequisites-install-cli"></a>

The AWS CLI is an open source tool that enables you to interact with AWS services using commands in your command-line shell. The AWS SAM CLI requires the AWS CLI for activities such as configuring credentials. To learn more about the AWS CLI, see [What is the AWS Command Line Interface?](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS Command Line Interface User Guide*.

To install the AWS CLI, see [ Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

## Step 2: Use the AWS CLI to configure AWS credentials
<a name="prerequisites-configure-credentials"></a>

**To configure credentials with IAM Identity Center**
+ To configure credentials with IAM Identity Center, see [Configure your profile with the AWS configure sso wizard](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html#cli-configure-sso-configure).

**To configure credentials with the AWS CLI**

1. Run the `aws configure` command from the command line.

1. Configure the following. Select each link to learn more:

   1. [ Access key ID](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-creds)

   1. [ Secret access key](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-creds)

   1. [AWS Region](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-region)

   1. [ Output format](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-format)

   The following example shows sample values.

   ```
   $ aws configure
   AWS Access Key ID [None]: {{AKIAIOSFODNN7EXAMPLE}}
   AWS Secret Access Key [None]: {{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
   Default region name [None]: {{us-west-2}}
   Default output format [None]: {{json}}
   ```

The AWS CLI stores this information in a *profile* (a collection of settings) named `default` in the `credentials` and `config` files. These files are located in the `.aws` file in your home directory. By default, the information in this profile is used when you run an AWS CLI command that doesn't explicitly specify a profile to use. For more information on the `credentials` file, see [ Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) in the *AWS Command Line Interface User Guide*.

For more information on configuring credentials, such as using an existing configuration and credentials file, see [Quick setup](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html) in the *AWS Command Line Interface User Guide*.

## Step 3: (Optional) Install AWS Toolkit for VS Code
<a name="prerequisites-install-vscode"></a>

For developers who prefer an integrated development environment, the AWS Toolkit for VS Code provides powerful features for serverless development including visual debugging, CodeLens integration, and streamlined deployment workflows.

**Prerequisites for VS Code development**
+ Visual Studio Code (version 1.73.0 or a later version) installed on your system
+ YAML language support extension for VS Code

**To install the AWS Toolkit for VS Code**

1. Open Visual Studio Code

1. Open the Extensions view (Ctrl\+Shift\+X or Cmd\+Shift\+X)

1. Search for "AWS Toolkit"

1. Install the "AWS Toolkit" extension by Amazon Web Services

1. Install the "YAML" extension by Red Hat (required for SAM template CodeLens features)

**Benefits of using VS Code with AWS SAM**
+ Visual debugging: Set breakpoints and step through your Lambda functions locally
+ CodeLens integration: Build, deploy, and invoke functions directly from your SAM template
+ Integrated terminal: Access AWS SAM AWS CLI commands without leaving your editor
+ Template validation: Real-time validation and IntelliSense for SAM templates

For information about configuring your AWS credentials in VS Code, see [ Setting up credentials](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-credentials.html) in the AWS Toolkit for VS Code User Guide.

## Next steps
<a name="prerequisites-next-steps"></a>
+ You are now ready to install the AWS SAM CLI and start using AWS SAM. To install the AWS SAM CLI, see [Install the AWS SAM CLI](install-sam-cli.md).
+ To set up Visual Studio Code for serverless development, see [Setting up the AWS Toolkit for VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setting-up.html).