AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Uninstall a Distributor

package

You can use the AWS Management Console or the AWS Command Line Interface (AWS CLI) to uninstall Distributor packages
from your AWS Systems Manager managed nodes by using Run Command. Distributor and Run Command are tools
in AWS Systems Manager. In this release, you can uninstall one version of one package per
command. You can uninstall a specific version or the default version.

###### Important

Packages that you install using Distributor should be uninstalled only by
using Distributor. Otherwise, Systems Manager can still register the application as
`INSTALLED` and lead to other unintended results.

###### Topics

- [Uninstalling a package using
  the console](#distributor-pkg-uninstall-console "#distributor-pkg-uninstall-console")
- [Uninstalling a package using the
  AWS CLI](#distributor-pkg-uninstall-cli "#distributor-pkg-uninstall-cli")

## Uninstalling a package using

the console

You can use Run Command in the Systems Manager console to uninstall a package one time.
Distributor uses [AWS Systems Manager Run Command](run-command.md "run-command.md") to
uninstall packages.

###### To uninstall a package using the console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Run Command**.
3. On the Run Command home page, choose **Run
   command**.
4. Choose the `AWS-ConfigureAWSPackage` command
   document.
5. From **Action**, choose
   **Uninstall**
6. For **Name**, enter the name of the package that you
   want to uninstall.
7. For **Targets**, choose how you want to target your
   managed nodes. You can specify a tag key and values that are shared by
   the targets. You can also specify targets by choosing attributes, such
   as an ID, platform, and SSM Agent version.
8. You can use the advanced options to add comments about the operation,
   change **Concurrency** and **Error
   threshold** values in **Rate control**,
   specify output options, or configure Amazon Simple Notification Service (Amazon SNS) notifications.
   For more information, see [Running Commands from the Console](rc-console.md "rc-console.md") in this guide.
9. When you're ready to uninstall the package, choose
   **Run**, and then choose **View
   results**.
10. In the commands list, choose the `AWS-ConfigureAWSPackage`
    command that you ran. If the command is still in progress, choose the
    refresh icon in the top-right corner of the console.
11. When the **Status** column shows
    **Success** or **Failed**, choose
    the **Output** tab.
12. Choose **View output**. The command output page shows
    the results of your command execution.

## Uninstalling a package using the

AWS CLI

You can use the AWS CLI to uninstall a Distributor package from managed nodes by
using Run Command.

###### To uninstall a package using the AWS CLI

- Run the following command in the AWS CLI.

```
aws ssm send-command \
    --document-name "AWS-ConfigureAWSPackage" \
    --instance-ids "`instance-IDs`" \
    --parameters '{"action":["Uninstall"],"name":["`package-name (in same account) or package-ARN (shared from different account)`"]}'
```

The following is an example.

```
aws ssm send-command \
    --document-name "AWS-ConfigureAWSPackage" \
    --instance-ids "i-02573cafcfEXAMPLE" \
    --parameters '{"action":["Uninstall"],"name":["Test-ConfigureAWSPackage"]}'
```

For information about other options you can use with the
**send-command** command, see [**send-command**](../../../cli/latest/reference/ssm/send-command.md "../../../cli/latest/reference/ssm/send-command.md") in the AWS Systems Manager section of the
_AWS CLI Command Reference_.
