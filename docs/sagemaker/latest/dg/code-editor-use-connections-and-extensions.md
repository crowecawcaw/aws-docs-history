# Code Editor Connections and

Extensions

Code Editor supports IDE connections to AWS services as well as extensions available
in the [Open VSX Registry](https://open-vsx.org/ "https://open-vsx.org/").

## Connections to AWS

Code Editor environments are integrated with the [AWS Toolkit for VS Code](../../../toolkit-for-vscode/latest/userguide/welcome.md "../../../toolkit-for-vscode/latest/userguide/welcome.md")
to add connections to AWS services. To get started with connections to AWS services,
you must have valid AWS Identity and Access Management (IAM) credentials. For more information, see [Authentication and
access for the AWS Toolkit for Visual Studio Code](../../../toolkit-for-vscode/latest/userguide/establish-credentials.md "../../../toolkit-for-vscode/latest/userguide/establish-credentials.md").

Within your Code Editor environment, you can add connections to:

- [AWS Explorer](../../../toolkit-for-vscode/latest/userguide/aws-explorer.md "../../../toolkit-for-vscode/latest/userguide/aws-explorer.md")
  – View, modify, and deploy AWS resources in Amazon S3, CloudWatch, and more.

Accessing certain features within AWS Explorer requires certain AWS
permissions. For more information, see [Authentication
and access for the AWS Toolkit for Visual Studio Code](../../../toolkit-for-vscode/latest/userguide/establish-credentials.md "../../../toolkit-for-vscode/latest/userguide/establish-credentials.md").

- [Amazon CodeWhisperer](../../../toolkit-for-vscode/latest/userguide/codewhisperer.md "../../../toolkit-for-vscode/latest/userguide/codewhisperer.md") – Build applications faster with
  AI-powered code suggestions.

To use Amazon CodeWhisperer with Code Editor, you must add the following
permissions to your SageMaker AI execution role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CodeWhispererPermissions",
 "Effect": "Allow",
 "Action": ["codewhisperer:GenerateRecommendations"],
 "Resource": "*"
 }
 ]
}`

```

For more information, see [Creating IAM
policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") and [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM
User Guide_.

## Extensions

Code Editor supports IDE extensions available in the [Open
VSX Registry](https://open-vsx.org/ "https://open-vsx.org/").

To get started with extensions in your Code Editor environment, choose the
**Extensions** icon (
![Icon showing two overlapping squares representing multiple windows or instances.](images/code-editor/code-editor-extensions-icon.png)
) in the left navigation pane. Here, you can configure connections to
AWS by installing the AWS Toolkit. For more information, see [Installing the AWS Toolkit for Visual Studio Code](../../../toolkit-for-vscode/latest/userguide/setup-toolkit.md "../../../toolkit-for-vscode/latest/userguide/setup-toolkit.md").

In the search bar, you can search directly for additional extensions through the
[Open VSX Registry](https://open-vsx.org/ "https://open-vsx.org/"), such as the
AWS Toolkit, Jupyter, Python, and more.
