# AWS SAM prerequisites

Complete the following prerequisites before installing and using the AWS Serverless Application Model Command Line Interface (AWS SAM CLI).

To use the AWS SAM CLI, you need the following:

- An AWS account, AWS Identity and Access Management (IAM) credentials, and an IAM access key pair.
- The AWS Command Line Interface (AWS CLI) to configure AWS credentials.

###### Topics

- [Step 1: Sign up for an AWS account](#prerequisites-sign-up "#prerequisites-sign-up")
- [Step 2: Create an IAM user account](#prerequisites-create-user "#prerequisites-create-user")
- [Step 3: Create an access key ID and secret access key](#prerequisites-create-keys "#prerequisites-create-keys")
- [Step 4: Install the AWS CLI](#prerequisites-install-cli "#prerequisites-install-cli")
- [Step 5: Use the AWS CLI to configure AWS credentials](#prerequisites-configure-credentials "#prerequisites-configure-credentials")
- [Step 6: (Optional) Install AWS Toolkit for VS Code](#prerequisites-install-vscode "#prerequisites-install-vscode")
- [Next steps](#prerequisites-next-steps "#prerequisites-next-steps")

## Step 1: Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

## Step 2: Create an IAM user account

To create an administrator user, choose one of the following options.

| Choose one way to manage your administrator | To                                                                                                                                                                                                                                                                                                                                                  | By                                                                                                                                                                                                                                          | You can also                                                                                                                                                                                                                                          |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| In IAM Identity Center (Recommended)        | Use short-term credentials to access AWS.This aligns with the security best<br>practices. For information about best practices, see [Security best<br>practices in IAM](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_. | Following the instructions in [Getting started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the<br>_AWS IAM Identity Center User Guide_.                      | Configure programmatic access by [Configuring the AWS CLI to use<br>AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the _AWS Command Line Interface User Guide_. |
| In IAM (Not recommended)                    | Use long-term credentials to access AWS.                                                                                                                                                                                                                                                                                                            | Following the instructions in [Create an IAM user for emergency access](../../../IAM/latest/UserGuide/getting-started-emergency-iam-user.md "../../../IAM/latest/UserGuide/getting-started-emergency-iam-user.md") in the _IAM User Guide_. | Configure programmatic access by [Manage access keys for IAM<br>users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_.                            |

## Step 3: Create an access key ID and secret access key

For CLI access, you need an access key ID and a secret access key.
Use temporary credentials instead of long-term access keys when possible.
Temporary credentials include an access key ID, a secret access key, and a
security token that indicates when the credentials expire. For more information,
see [Using temporary credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                 | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |

## Step 4: Install the AWS CLI

The AWS CLI is an open source tool that enables you to interact with AWS services using commands in your
command-line shell. The AWS SAM CLI requires the AWS CLI for activities such as configuring credentials. To learn more about
the AWS CLI, see [What is the AWS Command Line Interface?](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md")
in the _AWS Command Line Interface User Guide_.

To install the AWS CLI, see [Installing or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

## Step 5: Use the AWS CLI to configure AWS credentials

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

## Step 6: (Optional) Install AWS Toolkit for VS Code

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

##

Next steps

- You are now ready to install the AWS SAM CLI and start using AWS SAM. To install the AWS SAM CLI, see
  [Install the AWS SAM CLI](install-sam-cli.md "install-sam-cli.md").
- To set up Visual Studio Code for serverless development, see [Setting up the AWS Toolkit for VS Code](../../../toolkit-for-vscode/latest/userguide/setting-up.md "../../../toolkit-for-vscode/latest/userguide/setting-up.md").
