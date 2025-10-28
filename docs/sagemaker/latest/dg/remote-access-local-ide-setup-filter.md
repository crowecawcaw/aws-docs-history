# Filter your Studio

spaces

You can use filtering to display only the relevant Amazon SageMaker AI spaces in the
AWS Toolkit for Visual Studio Code explorer. The following provides information on manual filtering and
automated filtering. For more information on the definitions of manual and automatic
filtering, see [Filtering
overview](remote-access-remote-setup-filter.md#remote-access-remote-setup-filter-overview "remote-access-remote-setup-filter.md#remote-access-remote-setup-filter-overview").

This setup only applies when using the [Method 2: AWS Toolkit for Visual Studio Code](remote-access-local-ide-setup.md#remote-access-local-ide-setup-local-vs-code-method-2-aws-toolkit-in-vs-code "remote-access-local-ide-setup.md#remote-access-local-ide-setup-local-vs-code-method-2-aws-toolkit-in-vs-code") method to connect from local Visual Studio Code to Amazon SageMaker Studio spaces. See [Set up remote access](remote-access-remote-setup.md "remote-access-remote-setup.md") for more information.

###### Topics

- [Manual
  filtering](#remote-access-local-ide-setup-filter-manual "#remote-access-local-ide-setup-filter-manual")
- [Automatic filtering setup when using IAM credentials to sign-in](#remote-access-local-ide-setup-filter-automatic-IAM-credentials "#remote-access-local-ide-setup-filter-automatic-IAM-credentials")

## Manual

filtering

To manually filter displayed spaces:

- Open VS Code and navigate to the Toolkit for VS Code side panel
  explorer
- Find the **SageMaker AI** section
- Choose the filter icon on the right of the SageMaker AI section header. This
  will open a dropdown menu.
- In the dropdown menu, select the user profiles for which you want to
  display spaces

## Automatic filtering setup when using IAM credentials to sign-in

Automated filtering depends on the authentication method during sign-in. See
[Connecting to AWS from the Toolkit](../../../toolkit-for-vscode/latest/userguide/connect.md#connect-to-aws "../../../toolkit-for-vscode/latest/userguide/connect.md#connect-to-aws") in the Toolkit for VS Code
User Guide for more information.

When you authenticate and connect with **IAM Credentials**,
automated filtering requires [Set
up when connecting with IAM credentials](remote-access-remote-setup-filter.md#remote-access-remote-setup-filter-set-up-iam-credentials "remote-access-remote-setup-filter.md#remote-access-remote-setup-filter-set-up-iam-credentials").
Without this setup, if users opt-in for identity filtering, no spaces will be
shown.

Once the above is set up, AWS Toolkit matches spaces belonging to user
profiles that start with the authenticated IAM user name or assumed role
session name.

Automatic filtering is opt-in for users:

- Open VS Code settings
- Navigate to the **AWS Toolkit** extension
- Find **Enable Identity Filtering**
- Choose to enable automatic filtration of spaces based on your AWS
  identity
