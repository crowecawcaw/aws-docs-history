# Restore CloudFormation stacks

A CloudFormation composite backup is a combination of a CloudFormation template and all
associated nested recovery points. Any number of nested recovery points can be restored, but
the composite recovery point (which is the top-level recovery point) cannot be
restored.

When you restore a CloudFormation template recovery point, you create a new stack with a
change set to represent the backup.

## Restore CloudFormation with the AWS Backup console

From the [CloudFormation console](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/") you
can see the new stack and change set. To learn more about change sets, see [Updating stacks using change sets](../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.md") in the _AWS CloudFormation User
Guide_.

Determine which nested recovery points you want to restore from with your CloudFormation
stack, and then restore them using the AWS Backup console.

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Go to **Backup vaults**, select the backup vault containing your
   desired recovery point, then click on **Recovery points**.
3. Restore the AWS CloudFormation template recovery point.
   1. Click the composite recovery point containing the nested recovery points you
      want to restore to bring up the Details page for the composite recovery
      point.
   2. Under **Nested recovery points**, the nested recovery points
      will be displayed. Each recovery point will have a recovery point ID, a status, a
      resource ID, a resource type, a backup type, and the time that recovery point was
      created. Click the radio button next to the AWS CloudFormation recovery point, then click
      **Restore**. Ensure that you are selecting the recovery point
      that has **resource type: AWS CloudFormation** and **backup type:
      backup.**

4. Once the restore job for the CloudFormation template is completed, your restored AWS CloudFormation
   template will be visible in the [AWS CloudFormation
   console](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/") under **Stacks**.
5. Under **Stack names** you should find the restored template with
   the status of `REVIEW_IN_PROGRESS`.
6. Click on the name of the stack to see the stack's details.
7. There are tabs under the stack name. Click on **Change
   sets**.
8. Execute the change set.
9. After this processes, the resources in the original stack will be recreated in the
   new stack. The stateful resources will be recreated empty. To recover the stateful
   resources, go back to the list of recovery points in the AWS Backup console, select the
   recovery point you need, and initiate a restore.

## Restore CloudFormation with AWS CLI

In the command line interface, [`start-restore-job`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-restore-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-restore-job.html") allows you to restore a CloudFormation stack.

The following list is the accepted metadata to restore an CloudFormation resource.

```
// Mandatory metadata:
ChangeSetName // This is the name of the change set which will be created
StackName // This is the name of the stack that will be created by the new change set

// Optional metadata:
ChangeSetDescription // This is the description of the new change set
StackParameters // This is the JSON of the stack parameters required by the stack
aws:backup:request-id
```
