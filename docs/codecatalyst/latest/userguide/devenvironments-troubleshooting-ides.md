Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Troubleshooting problems with IDEs

Consult the following sections to troubleshoot problems related to IDEs in CodeCatalyst. For more
information on IDEs, see [Creating a Dev Environment in an IDE](devenvironment-create.md#devenvironment-using-ide "devenvironment-create.md#devenvironment-using-ide").

###### Topics

- [I have mismatched runtime image versions in AWS Cloud9](#troubleshooting-devenvironments-c9-runtime "#troubleshooting-devenvironments-c9-runtime")
- [I can't access my files in /projects/projects in AWS Cloud9](#troubleshooting-devenvironments-c9-filesystem "#troubleshooting-devenvironments-c9-filesystem")
- [I can't launch my Dev Environment in AWS Cloud9 using a custom devfile](#troubleshooting-devenvironments-c9-image "#troubleshooting-devenvironments-c9-image")
- [I'm having issues in AWS Cloud9](#troubleshooting-c9 "#troubleshooting-c9")
- [In JetBrains, I can't connect to my Dev Environments through CodeCatalyst](#troubleshooting-jetbrains-connect "#troubleshooting-jetbrains-connect")
- [I can't install AWS Toolkit for my IDE](#troubleshooting-ide-toolkit "#troubleshooting-ide-toolkit")
- [In my IDE, I can't launch my Dev Environments](#troubleshooting-ide-launch "#troubleshooting-ide-launch")

## I have mismatched runtime image versions in AWS Cloud9

AWS Cloud9 is using different versions of the frontend asset and the backend runtime image. Using different versions might cause the Git extension and AWS Toolkit to work incorrectly.
To fix the problem, navigate to the Dev Environment dashboard, stop your Dev Environment, and then start it again. To fix the problem using APIs, use the `UpdateDevEnvironment` API to update the runtime.
For more information, see [UpdateDevEnvironment](../APIReference/API_UpdateDevEnvironment.md "../APIReference/API_UpdateDevEnvironment.md") in the _Amazon CodeCatalyst API reference_.

## I can't access my files in `/projects/projects` in AWS Cloud9

The AWS Cloud9 editor is unable to access files in the directory `/projects/projects`. To fix the problem, use the AWS Cloud9 terminal to access your files or move them to a different directory.

## I can't launch my Dev Environment in AWS Cloud9 using a custom devfile

Your devfile image might not be compatible with AWS Cloud9. To fix the problem, review the devfile from your repository and corresponding Dev Environment and create a new one to continue.

## I'm having issues in AWS Cloud9

For other issues, check the troubleshooting section in the [AWS Cloud9 User Guide](../../../cloud9/latest/user-guide/troubleshooting.md "../../../cloud9/latest/user-guide/troubleshooting.md").

## In JetBrains, I can't connect to my Dev Environments through CodeCatalyst

To fix the problem, check that you have only latest version of JetBrains installed. If you have multiple versions,
uninstall the older versions and register your protocol handler again by closing the IDE and the browser. Then open JetBrains and
register the protocol handler again.

## I can't install AWS Toolkit for my IDE

To fix this problem for VS Code, manually install AWS Toolkit for Visual Studio Code from [GitHub](https://github.com/aws/aws-toolkit-vscode/releases "https://github.com/aws/aws-toolkit-vscode/releases").

To fix this problem for JetBrains, manually install AWS Toolkit for JetBrains from [GitHub](https://github.com/aws/aws-toolkit-jetbrains/releases "https://github.com/aws/aws-toolkit-jetbrains/releases").

## In my IDE, I can't launch my Dev Environments

To fix this problem for VS Code, check that you have latest version of VS Code and AWS Toolkit for Visual Studio Code installed. If you don't have the latest version, update and launch your Dev Environment.
For more information, see [Amazon CodeCatalyst for VS Code](../../../toolkit-for-vscode/latest/userguide/codecatalyst-service.md "../../../toolkit-for-vscode/latest/userguide/codecatalyst-service.md").

To fix this problem for JetBrains, check that you have latest version of JetBrains and AWS Toolkit for JetBrains installed. If you don't have the latest version, update and launch your Dev Environment.
For more information, see [Amazon CodeCatalyst for JetBrains](../../../toolkit-for-jetbrains/latest/userguide/codecatalyst-overview.md "../../../toolkit-for-jetbrains/latest/userguide/codecatalyst-overview.md").
