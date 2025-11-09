AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Viewing AWS

predefined patch baselines

Patch Manager, a tool in AWS Systems Manager, includes a predefined patch baseline for each
operating system supported by Patch Manager. You can use these patch baselines (you
can't customize them), or you can create your own. The following procedure
describes how to view a predefined patch baseline to see if it meets your needs.
To learn more about patch baselines, see [Predefined and
custom patch baselines](patch-manager-predefined-and-custom-patch-baselines.md "patch-manager-predefined-and-custom-patch-baselines.md").

###### To view AWS predefined patch baselines

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Patch Manager**.
3. In the patch baselines list, choose the baseline ID of one of the
   predefined patch baselines.

-or-

If you are accessing Patch Manager for the first time in the current
AWS Region, choose **Start with an overview**, choose
the **Patch baselines** tab, and then choose the
baseline ID of one of the predefined patch baselines.

###### Note

For Windows Server, three predefined patch baselines are provided. The patch baselines
`AWS-DefaultPatchBaseline` and
`AWS-WindowsPredefinedPatchBaseline-OS` support only operating system updates
on the Windows operating system itself. `AWS-DefaultPatchBaseline` is used as the
default patch baseline for Windows Server managed nodes unless you specify a different patch
baseline. The configuration settings in these two patch baselines are the same. The newer of
the two, `AWS-WindowsPredefinedPatchBaseline-OS`, was created to distinguish it
from the third predefined patch baseline for Windows Server. That patch baseline,
`AWS-WindowsPredefinedPatchBaseline-OS-Applications`, can be used to apply
patches to both the Windows Server operating system and supported applications released by
Microsoft.

For more information, see [Setting an existing patch
baseline as the default](patch-manager-default-patch-baseline.md "patch-manager-default-patch-baseline.md"). 4. In the **Approval rules** section, review the patch
baseline configuration. 5. If the configuration is acceptable for your managed nodes, you can
skip ahead to the procedure [Creating and managing patch
groups](patch-manager-tag-a-patch-group.md "patch-manager-tag-a-patch-group.md").

-or-

To create your own default patch baseline, continue to the topic [Working with custom patch
baselines](patch-manager-manage-patch-baselines.md "patch-manager-manage-patch-baselines.md").
