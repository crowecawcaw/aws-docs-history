# AWS SAM prerequisites

Complete the following prerequisites before installing and using the AWS Serverless Application Model Command Line Interface (AWS SAM CLI).

To use the AWS SAM CLI, you need the following:

- An AWS account, AWS Identity and Access Management (IAM) credentials, and an IAM access key pair.
- The AWS Command Line Interface (AWS CLI) to configure AWS credentials.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Step 1: Install the AWS CLI](#prerequisites-install-cli "#prerequisites-install-cli")
- [Step 2: Use the AWS CLI to configure AWS credentials](#prerequisites-configure-credentials "#prerequisites-configure-credentials")
- [Step 3: (Optional) Install AWS Toolkit for VS Code](#prerequisites-install-vscode "#prerequisites-install-vscode")
- [Next steps](#prerequisites-next-steps "#prerequisites-next-steps")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Step 1: Install the AWS CLI

The AWS CLI is an open source tool that enables you to interact with AWS services using commands in your
command-line shell. The AWS SAM CLI requires the AWS CLI for activities such as configuring credentials. To learn more about
the AWS CLI, see [What is the AWS Command Line Interface?](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md")
in the _AWS Command Line Interface User Guide_.

To install the AWS CLI, see [Installing or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

## Step 2: Use the AWS CLI to configure AWS credentials

###### To configure credentials with IAM Identity Center

- To configure credentials with IAM Identity Center, see [Configure your profile with the AWS configure sso wizard](../../../cli/latest/userguide/cli-configure-sso.md#cli-configure-sso-configure "../../../cli/latest/userguide/cli-configure-sso.md#cli-configure-sso-configure").

###### To configure credentials with the AWS CLI

1. Run the `aws configure` command from the command line.
2. Configure the following. Select each link to learn more:

   1. [Access key ID](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-creds "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-creds")
   2. [Secret access key](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-creds "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-creds")
   3. [AWS Region](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-region "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-region")
   4. [Output format](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-format "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-format")The following example shows sample values.

````
`$` `aws configure`
`AWS Access Key ID [None]: ``AKIAIOSFODNN7EXAMPLE``
AWS Secret Access Key [None]: ``wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY``
Default region name [None]: ``us-west-2``
Default output format [None]: ``json```
````

The AWS CLI stores this information in a _profile_ (a collection of settings) named
`default` in the `credentials` and `config` files. These files are
located in the `.aws` file in your home directory. By default, the information in this profile is used
when you run an AWS CLI command that doesn't explicitly specify a profile to use. For more information on the
`credentials` file, see [Configuration and credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") in the _AWS Command Line Interface User Guide_.

For more information on configuring credentials, such as using an existing configuration and credentials file, see
[Quick setup](../../../cli/latest/userguide/getting-started-quickstart.md "../../../cli/latest/userguide/getting-started-quickstart.md")
in the _AWS Command Line Interface User Guide_.

## Step 3: (Optional) Install AWS Toolkit for VS Code

For developers who prefer an integrated development environment, the AWS Toolkit for VS Code provides powerful features for serverless development including visual debugging,
CodeLens integration, and streamlined deployment workflows.

**Prerequisites for VS Code development**

- Visual Studio Code (version 1.73.0 or a later version) installed on your system
- YAML language support extension for VS Code

###### To install the AWS Toolkit for VS Code

1. Open Visual Studio Code
2. Open the Extensions view (Ctrl+Shift+X or Cmd+Shift+X)
3. Search for "AWS Toolkit"
4. Install the "AWS Toolkit" extension by Amazon Web Services
5. Install the "YAML" extension by Red Hat (required for SAM template CodeLens features)

**Benefits of using VS Code with AWS SAM**

- Visual debugging: Set breakpoints and step through your Lambda functions locally
- CodeLens integration: Build, deploy, and invoke functions directly from your SAM template
- Integrated terminal: Access AWS SAM AWS CLI commands without leaving your editor
- Template validation: Real-time validation and IntelliSense for SAM templates

For information about configuring your AWS credentials in VS Code, see [Setting up credentials](../../../toolkit-for-vscode/latest/userguide/setup-credentials.md "../../../toolkit-for-vscode/latest/userguide/setup-credentials.md") in the AWS Toolkit for VS Code User Guide.

## Next steps

- You are now ready to install the AWS SAM CLI and start using AWS SAM. To install the AWS SAM CLI, see
  [Install the AWS SAM CLI](install-sam-cli.md "install-sam-cli.md").
- To set up Visual Studio Code for serverless development, see [Setting up the AWS Toolkit for VS Code](../../../toolkit-for-vscode/latest/userguide/setting-up.md "../../../toolkit-for-vscode/latest/userguide/setting-up.md").
