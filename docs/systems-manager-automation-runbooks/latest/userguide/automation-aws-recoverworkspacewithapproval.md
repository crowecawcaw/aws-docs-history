

# `AWSSupport-RecoverWorkSpaceWithApproval`
<a name="automation-aws-recoverworkspacewithapproval"></a>

The `AWSSupport-RecoverWorkSpaceWithApproval` runbook performs recovery steps on the Amazon WorkSpaces (WorkSpaces) instance you specify if its operational state is `Unhealthy`. Depending on the values you specify for the input parameters and the snapshots available, the runbook reboots, restores, and rebuilds the WorkSpaces until its status becomes `Available`. This runbook uses the `aws:approve` automation action, which temporarily pauses the automation until the designated principals either approve or deny the recovery actions selected.

**Important**  
Restoring or rebuilding a WorkSpace is a potentially destructive action that can result in the loss of data. This is because the WorkSpace is restored from the last available snapshot and data recovered from snapshots can be as old as 12 hours.  
The restore option recreates both the root volume and user volume based on the most recent snapshots. The rebuild option recreates the user volume from the most recent snapshot and recreates the WorkSpace from the image associated with the bundle the WorkSpace was created from. Applications that were installed or system settings that were changed after the WorkSpace was created are lost. For more information about restoring and rebuilding WorkSpaces, see [Restore a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/restore-workspace.html) and [Rebuild a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/rebuild-workspace.html) in the *Amazon WorkSpaces Administration Guide*.

Before using this runbook, we recommend reviewing the [Troubleshooting Amazon WorkSpaces Issues](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-troubleshooting.html) topic in the Amazon WorkSpaces Administration Guide.

The runbook performs the following recovery actions in sequence, stopping as soon as the WorkSpaces reaches an `Available` state:
+ Retrieves the initial state of the WorkSpaces and confirms it is in a recoverable state (`Unhealthy`, `Error`, `Impaired`, `Stopped`, or `Available`).
+ If the WorkSpaces is `Stopped`, starts it and waits for the result.
+ Retrieves available rebuild and restore snapshots for the WorkSpaces.
+ Sends an approval notification via Amazon Simple Notification Service (Amazon SNS) to the designated approvers and pauses until approved or denied.
+ If approved and `Reboot` is set to `Yes`, reboots the WorkSpaces and waits for the result.
+ If the WorkSpaces is still not `Available` and `Restore` is set to `Yes`, restores the WorkSpaces from the most recent snapshot and waits for the result.
+ If the WorkSpaces is still not `Available` and `Rebuild` is set to `Yes`, rebuilds the WorkSpaces from the most recent bundle image and waits for the result.
+ Confirms the final state of the WorkSpaces is `Available`.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-RecoverWorkSpaceWithApproval) 

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `sns:Publish`
+ `workspaces:DescribeWorkspaces`
+ `workspaces:DescribeWorkspaceSnapshots`
+ `workspaces:RebootWorkspaces`
+ `workspaces:RebuildWorkspaces`
+ `workspaces:RestoreWorkspace`
+ `workspaces:StartWorkspaces`

Example IAM policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "workspaces:DescribeWorkspaces",
                "workspaces:DescribeWorkspaceSnapshots",
                "workspaces:RebootWorkspaces",
                "workspaces:RebuildWorkspaces",
                "workspaces:RestoreWorkspace",
                "workspaces:StartWorkspaces"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "sns:Publish",
            "Resource": "arn:aws:sns:*:*:Automation*"
        }
    ]
}
```

Follow these steps to configure the automation:

1. Open [AWSSupport-RecoverWorkSpaceWithApproval](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-RecoverWorkSpaceWithApproval/description) in Systems Manager under Documents.

1. Choose Execute automation.

1. For the input parameters, enter the following:
   + **AutomationAssumeRole (Optional):**

     The AWS IAM role ARN that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook. Type: `AWS::IAM::Role::Arn`.
   + **WorkspaceId (Required):**

     The ID of the WorkSpaces to recover. Must match the pattern `^ws-[0-9a-z]{8,63}$`. Type: `String`.
   + **Reboot (Optional):**

     Set to `Yes` to allow the WorkSpaces to be rebooted. Default: `Yes`. Allowed values: `Yes` \| `No`. Type: `String`.
   + **Restore (Optional):**

     Set to `Yes` to allow the WorkSpaces to be restored. The system is restored to the most recent snapshot of the root volume. Any applications installed or system settings changed after the most recent snapshot was created are lost. The user volume is recreated from the most recent snapshot and its current contents are overwritten. Default: `No`. Allowed values: `Yes` \| `No`. Type: `String`.
   + **Rebuild (Optional):**

     Set to `Yes` to allow the WorkSpaces to be rebuilt. The system is refreshed with the most recent image of the bundle that the WorkSpaces was created from. Any applications installed or system settings changed after the WorkSpaces was created are lost. The user volume is recreated from the most recent snapshot and its current contents are overwritten. Default: `No`. Allowed values: `Yes` \| `No`. Type: `String`.
   + **Acknowledge (Required):**

     Enter `Yes` to acknowledge that both the restore and rebuild actions recover the WorkSpaces from the most recent snapshot, and that data restored from snapshots can be as old as 12 hours. Allowed pattern: `^[Yy][Ee][Ss]$`. Type: `String`.
   + **Approvers (Required):**

     A list of IAM user names or ARNs of the approvers for the automation action. You can specify principals as an IAM user name, IAM user ARN, IAM role ARN, or IAM assume role user ARN. Minimum: 1, Maximum: 10. Type: `StringList`.
   + **MinRequiredApprovals (Optional):**

     The minimum number of approvals required to resume the automation execution. The value cannot exceed the number of approvers defined by the `Approvers` parameter. Default: `1`. Allowed values: `1`–`10`. Type: `Integer`.
   + **SNSTopicArn (Required):**

     The Amazon SNS topic ARN used to send the pending approval notification. The Amazon SNS topic name must be prefixed with `Automation`. Type: `String`.

1. Choose Execute.

1. The automation initiates.

1. The document performs the following steps:
   + **`getWorkSpaceInitialState`**: Retrieves the current state of the WorkSpaces.
   + **`assertWorkSpaceInitialState`**: Confirms the WorkSpaces is in a recoverable state (`Available`, `Error`, `Stopped`, `Unhealthy`, or `Impaired`). The automation ends if the WorkSpaces is in any other state.
   + **`branchOnWorkSpaceInitialState`**: Branches based on the initial WorkSpaces state. If `Stopped`, proceeds to start the WorkSpaces. If `Unhealthy`, `Error`, or `Impaired`, proceeds to retrieve snapshots.
   + **`startWorkSpace`**: Starts the WorkSpaces if it was in a `Stopped` state.
   + **`waitForStartWorkSpace`**: Waits up to 10 minutes for the WorkSpaces to reach `Starting` status.
   + **`waitForStartWorkSpaceResult`**: Waits up to 30 minutes for the WorkSpaces to reach `Unhealthy`, `Error`, `Impaired`, or `Available` status after starting.
   + **`getWorkSpaceStateAfterStart`**: Retrieves the WorkSpaces state after the start attempt.
   + **`branchOnWorkSpaceStateAfterStart`**: If the WorkSpaces is `Available`, proceeds to final assertion. Otherwise, proceeds to retrieve snapshots.
   + **`getWorkSpaceSnapshots`**: Retrieves available rebuild and restore snapshots for the WorkSpaces.
   + **`approval`**: Sends an approval notification to the specified Amazon SNS topic and pauses the automation for up to 24 hours, waiting for the designated approvers to approve or deny the recovery actions.
   + **`branchOnRebootAllowed`**: If `Reboot` is set to `Yes`, proceeds to reboot the WorkSpaces. Otherwise, proceeds to the restore branch.
   + **`rebootWorkSpace`**: Reboots the WorkSpaces.
   + **`waitForRebootWorkSpace`**: Waits up to 10 minutes for the WorkSpaces to reach `Rebooting` status.
   + **`waitForRebootWorkSpaceResult`**: Waits up to 30 minutes for the WorkSpaces to reach `Unhealthy`, `Error`, or `Available` status after rebooting.
   + **`getWorkSpaceStateAfterReboot`**: Retrieves the WorkSpaces state after the reboot attempt.
   + **`branchOnWorkSpaceStateAfterReboot`**: If the WorkSpaces is `Available`, proceeds to final assertion. Otherwise, proceeds to the restore branch.
   + **`branchOnRestoreAllowed`**: If `Restore` is set to `Yes`, proceeds to restore the WorkSpaces. Otherwise, proceeds to the rebuild branch.
   + **`restoreWorkSpace`**: Restores the WorkSpaces from the most recent snapshot. If the restore fails, the automation proceeds to the rebuild branch.
   + **`waitForRestoreWorkSpace`**: Waits up to 10 minutes for the WorkSpaces to reach `Restoring` status.
   + **`waitForRestoreWorkSpaceResult`**: Waits up to 30 minutes for the WorkSpaces to reach `Unhealthy`, `Error`, or `Available` status after restoring.
   + **`getWorkSpaceStateAfterRestore`**: Retrieves the WorkSpaces state after the restore attempt.
   + **`branchOnWorkSpaceStateAfterRestore`**: If the WorkSpaces is `Available`, proceeds to final assertion. Otherwise, proceeds to the rebuild branch.
   + **`branchOnRebuildAllowed`**: If `Rebuild` is set to `Yes`, proceeds to rebuild the WorkSpaces. Otherwise, proceeds to final assertion.
   + **`rebuildWorkSpace`**: Rebuilds the WorkSpaces from the most recent bundle image.
   + **`waitForRebuildWorkSpace`**: Waits up to 10 minutes for the WorkSpaces to reach `Rebuilding` status.
   + **`waitForRebuildWorkSpaceResult`**: Waits up to 30 minutes for the WorkSpaces to reach `Unhealthy`, `Error`, or `Available` status after rebuilding.
   + **`getWorkSpaceStateAfterRebuild`**: Retrieves the WorkSpaces state after the rebuild attempt.
   + **`assertWorkSpaceFinalState`**: Confirms the WorkSpaces status is `Available`. The automation fails if the WorkSpaces is not in an `Available` state.

1. After completion, review the Outputs section for the detailed results of the execution.

Systems Manager Automation
+ [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-RecoverWorkSpaceWithApproval/description)
+ [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html)
+ [Setting up an Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html)
+ [Running an automation with approvers](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing-approval.html)
+ [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/)