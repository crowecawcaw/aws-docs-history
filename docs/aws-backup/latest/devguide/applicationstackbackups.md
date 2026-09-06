

# CloudFormation stack backups
<a name="applicationstackbackups"></a>

A CloudFormation stack consists of multiple stateful and stateless resources that you can back up as a single unit. In other words, you can backup and restore an application containing multiple resources by backing up a stack and restoring the resources within it. All the resources in a stack are defined by the stack's CloudFormation template.

When a CloudFormation stack is backed up, recovery points are created for the CloudFormation template and for each additional resource supported by AWS Backup in the stack. These recovery points are grouped together within a overarching recovery point called a **composite**.

This composite recovery point cannot be restored, but nested recovery points can be restored. You can restore anywhere from one to all nested backups within a composite backup using the console or the AWS CLI.

## CloudFormation application stack terminology
<a name="appstackterminology"></a>
+ **Composite recovery point**: A recovery point used to group nested recovery points together, as well other metadata.
+ **Nested recovery point**: A recovery point of a resource that is part of a CloudFormation stack and is backed up as part of the composite recovery point. Each nested recovery point belongs in the stack of one composite recovery point.
+ **Composite job**: A backup, copy, or restore job for a CloudFormation stack which can trigger other backup jobs for individual resources within the stack.
+ **Nested job**: A backup, copy, or restore job for a resource within a CloudFormation stack.

## CloudFormation stack backup jobs
<a name="howtobackupcfn"></a>

The process of a backup creation is called a backup job. A CloudFormation stack backup job has a [ status](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup.html#backup-job-statuses). When a backup job has finished, it has the status of `Completed`. This signifies a [CloudFormation recovery point](#cfnrecoverypoints) (a backup) has been created.

CloudFormation stacks can be backed up using the console or backed up programatically. To backup any resource, including a CloudFormation stack, see [ Creating a backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup.html) elsewhere in this *AWS Backup Developer Guide*.

CloudFormation stacks can be backed up using the API command `StartBackupJob`. Note that the documentation and console refer to composite and nested recovery points; the API language uses the terminology "parent and child recovery points" in the same contextual relationship.

CloudFormation stacks contain all AWS resources are indicated by your [CloudFormation template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Note that your template may contain resources not yet supported by AWS Backup. If your template contains a combination of AWS supported resources and unsupported resources, AWS Backup will still back up the template into a composite stack, but Backup will only create recovery points of the Backup-supported services. All resource types contained within the CloudFormation template will be included within a backup, even if you have not opted into to a particular service (toggling a service to “Enabled” in console Settings).

## CloudFormation recovery point
<a name="cfnrecoverypoints"></a>

### Recovery point status
<a name="cfnrecoverypointstatus"></a>

When the backup job of a stack is finished (the job status is `Completed`), a backup of the stack has been created. This backup is also known as a composite recovery point. A composite recovery point can have one of the following statuses: `Completed`, `Failed`, or `Partial`. Note that a backup job has a status, and a recovery point (also called a backup) also has a separate status.

A completed backup job means your entire stack and the resources within in are protected by AWS Backup. A failed status indicates that the backup job was unsuccessful; you should create the backup again once the issue that caused the failure is corrected.

A `Partial` status means that not all the resources in the stack were backed up. This may happen if the CloudFormation template contains resources that are not currently supported by AWS Backup, or it may happen if one or more of the backup jobs belonging to resources within the stack (nested resources) have statuses other than `Completed`. You can manually create an on-demand backup to rerun any resources that resulted in a status other than `Completed`. If you expected the stack to have the status of `Completed` but it is marked as `Partial` instead, check to see which of the conditions above might be true about your stack.

Each nested resource within the composite recovery point has its own individual recovery point, each with its own status (either `Completed` or `Failed`). Nested recovery points with a status of `Completed` can be restored.

### Manage recovery points
<a name="cfnmanagerecoverypoints"></a>

Composite recovery points (backups) can be copied; nested recovery points can be copied, deleted, disassociated, or restored. A composite recovery point which contains nested backups cannot be deleted. After the nested recovery points within a composite recovery point have been deleted or disassociated, you can manually delete the composite recovery point manually or let it remain until the backup plan lifecycle deletes it. 

### Delete a recovery point
<a name="cfndeleterecoverypoint"></a>

You can delete a recovery point using the AWS Backup console or using the AWS CLI.

To delete recovery points using the AWS Backup console,

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. Click on **Protected Resources** in the left-hand navigation. In the text box, type `CloudFormation` to display only your CloudFormation stacks.

1. Composite recovery points will be displayed in the Recovery points pane. The plus sign (\+) to the left of each recovery point ID can be clicked to expand each composite recovery point, showing all nested recovery points contained in the composite. You can check the box to the left of any recovery point to include it in your selection of recovery points you wish to delete.

1. Click the **Delete** button.

When you use the console to delete one or more composite recovery points, a warning box will pop up. This warning box requires you to confirm your intention to delete the composite recovery points, including nested recovery points within composite stacks.

To delete recovery points using API, use the `DeleteRecoveryPoint` command.

When you use API with the AWS Command Line Interface you must delete all nested recovery points prior to deleting a composite point. If you send an API request to delete a composite stack backup (recovery point) that still contains nested recovery points within it, the request will return an error.

### Disassociate a nested recovery point from composite recovery point
<a name="cfndisassociaterecoverypoints"></a>

You can disassociate a nested recovery point from a composite recovery point (for example, you wish to keep the nested recovery point but delete the composite recovery point). Both recovery points will remain, but they will no longer be connected; that is, actions that occur on the composite recovery point will no longer apply to the nested recovery point once it has been disassociated.

You can disassociate the recovery point using the console, or you can call the API `DisassociateRecoveryPointFromParent`. [Note that the API calls use the term “parent” to refer to composite recovery points.]

### Copy a recovery point
<a name="cfncopyrecoverypoint"></a>

You can copy a composite recovery point, or you can copy a nested recovery point if the resource supports [cross-account and cross-Region copy](backup-feature-availability.md#features-by-resource).

To copy recovery points using the AWS Backup console:

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. Click on **Protected Resources** in the left-hand navigation. In the text box, type `CloudFormation` to display only your CloudFormation stacks.

1. Composite recovery points will be displayed in the Recovery points pane. The plus sign (\+) to the left of each recovery point ID can be clicked to expand each composite recovery point, showing all nested recovery points contained in the composite. You can click the radial circle button to the left of any recovery point to copy it.

1. Once it is selected, click the **Copy** button in the top-right corner of the pane.

When you copy a composite recovery point, nested recovery points that don’t support copy functionality won’t end up in the copied stack. The composite recovery point will have a status of `Partial`.

## Frequently Asked Questions
<a name="cfnfaq"></a>

1. *"What is included as part of the application backup?"*

   As part of each backup of an application defined using CloudFormation, the template, the processed value of each parameter in the template, and the nested resources supported by AWS Backup are backed up. A nested resource is backed up in the same way as an individual resource not part of a CloudFormation stack is backed up. Note that values of parameters marked as `no-echo` will not be backed up.

   

1. *"Can I back up my CloudFormation stack that has nested stacks?"*

   Yes. Your CloudFormation stacks which contain nested stacks can be in your backup.

   

1. *"Does a `Partial` status mean the creation of my backup failed?"*

   No. A partial status indicates that some of the recovery points were backed up, while some were not. There are three conditions to check if you were expecting a `Completed` backup result:

   1. Does your CloudFormation stack contain resources currently unsupported by AWS Backup? For a list of supported resources, see [ Supported AWS resources and third-party applications](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#supported-resources) in our Developer Guide.

   1. One or more of the backup jobs belonging to resources within the stack were not successful and the job has to be rerun.

   1. A nested recovery point was deleted or disassociated from the composite recovery point.

   

1. *"How do I exclude resources in my CloudFormation stack backup?"*

   When you back up your CloudFormation stack, you can exclude resources from being part of the backup. In the console, during the [create a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html) and [update a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/updating-a-backup-plan.html) processes, there is an [assign resources](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html) step. In this step, there is a **Resource selection** section. If you choose **include specific resource types** and have included CloudFormation as a resource to backup, you can **exclude specific resource IDs from the selected resource types**. You can also use tags to exclude resources within the stack.
**Important**  
Resources that belong to a CloudFormation stack must be in the exclusion list of *every* resource selection in the backup plan that targets that resource type. If a resource is excluded only from the CloudFormation backup selection but is matched by another resource selection (for example, an S3 selection using `arn:aws:s3:::*`), the resource will still be backed up by that other selection.

   Using CLI, you can use
   + `NotResources` in your backup plan to exclude a specific resource from your CloudFormation stacks.
   + `StringNotLike` to exclude items through tags.

   

1. *"What types of backups are supported for nested resources?"*

   Backups of nested resources may be either full or incremental backups, depending on which kind of backup is supported by AWS Backup for these resources. For more information, see [ How incremental backups work](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup.html#how-incremental-backup-works). However, note that PITR (point-in-time restore) is [not supported](backup-feature-availability.md#features-by-resource) for Amazon S3 and Amazon RDS nested resources.

   

1. *"Are change sets that are part of the CloudFormation stack backed up?"*

   No. Change sets are not backed up as part of CloudFormation stack backup.

   

1. *"How does the status of the CloudFormation stack impact the backup?"*

   The status of the CloudFormation stack may impact the backup. A stack with a status that includes `COMPLETE` can be backed up, such as statuses `CREATE_COMPLETE`, `ROLLBACK_COMPLETE`, `UPDATE_COMPLETE`, `UPDATE_ROLLBACK_COMPLETE`, `IMPORT_COMPLETE`, or `IMPORT_ROLLBACK_COMPLETE`.

   In the case where an upload of a new template fails and the stack move to the status of `ROLLBACK_COMPLETE`, the new template will be backed up but backups of the nested resources will be based on the rolled-back resources.

   

1. *"How do application stack lifecycles differ from other recovery point lifecycles?" *

   Nested recovery point lifecycles are determined by the backup plan to which they belong. The composite recovery point is determined by the longest lifecycle of all nested recovery points. When the last remaining nested recovery point within a composite recovery point is deleted or disassociated, the composite recovery point will also be deleted.

   

1. *“How are tags of a CloudFormation copied to recovery points?”*

   Yes. Those tags will be copied to each respective nested recovery point.

1. *“Is there an order for deleting composite and nested recovery points (backups)?”*

   Yes. Some backups must be deleted before others can be deleted. Composite backups which contain nested recovery points cannot be deleted until all recovery points within the composite have been deleted. Once a composite recovery point is no longer contains nested recovery points, you can delete it manually. Otherwise, it will be deleted in accordance with its backup plan lifecycle.

   

## Restore applications within a stack
<a name="restore-app-stack"></a>

See [ How to restore application stack backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-application-stacks.html) for information on restoring nested recovery points.