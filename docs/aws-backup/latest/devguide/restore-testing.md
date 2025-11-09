# Restore testing

_Restore testing_, a feature offered by AWS Backup, provides automated and
periodic evaluation of restore viability, as well as the ability to monitor restore job
duration times.

###### Contents

- [Overview](#restore-testing-overview "#restore-testing-overview")
- [Restore testing compared with restore
  process](#restore-testing-compare "#restore-testing-compare")
- [Restore testing management](#restore-testing-management "#restore-testing-management")
- [Create a restore testing plan](#restore-testing-create "#restore-testing-create")
- [Update a restore testing plan](#restore-testing-update "#restore-testing-update")
- [View existing restore testing plans](#restore-testing-view "#restore-testing-view")
- [View restore testing jobs](#restore-testing-jobs "#restore-testing-jobs")
- [Delete a restore testing plan](#restore-testing-delete "#restore-testing-delete")
- [Audit restore testing](#restore-testing-audit "#restore-testing-audit")
- [Restore testing quotas and parameters](#restore-testing-quotas "#restore-testing-quotas")
- [Restore testing failure
  troubleshooting](#restore-testing-troubleshooting "#restore-testing-troubleshooting")
- [Restore testing inferred
  metadata](restore-testing-inferred-metadata.md "restore-testing-inferred-metadata.md")
- [Restore testing validation](restore-testing-validation.md "restore-testing-validation.md")

## Overview

First, you create a restore testing plan where you provide a name for your plan, the
frequency for your restore tests, and the target start time. Then, you assign the resources
you want to include in your plan. You then choose to include specific or random recovery
points in your test. AWS Backup backup intelligently [infers the
metadata](restore-testing-inferred-metadata.md "restore-testing-inferred-metadata.md") that will be needed for your restore job to be successful.

When the scheduled time in your plan arrives, AWS Backup starts restore jobs based on your
plan and monitors the time taken to complete the restore.

After the restore test plan completes its run, you can use the results to show
compliance for organizational or governance requirements such as the successful completion
of restore test scenarios or the restore job completion time.

Optionally, you can use [Restore testing validation](restore-testing-validation.md "restore-testing-validation.md") to confirm the restore test results.

Once the optional validation completes or the validation window closes, AWS Backup deletes
the resources involved with the restore test, and the resources will be deleted in
accordance with service SLAs.

At the end of the testing process, you can view the results and the completion time of
the tests.

## Restore testing compared with restore

process

Restore testing runs restore jobs in the same way as on-demand restores and uses the
same recovery points (backups) as an on-demand restore. You will see calls to
`StartRestoreJob` in CloudTrail (if opted-in) for each job started by restore
testing

However, there are a few differences between the operation of a schedule restore test
and an on-demand restore operation:

|                              | Restore Testing                                                                                                                                                                                                                                | Restore                                                                             |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Account**                  | Recommended best practice is to designate an account to be used for<br>restore tests                                                                                                                                                           | You can restore resources from an account                                           |
| **AWS Backup Audit Manager** | Can turn on a control to confirm if a restore test meets specified<br>restore objectives                                                                                                                                                       |                                                                                     |
| **Cadence**                  | Periodically as part of a scheduled plan.                                                                                                                                                                                                      | On demand                                                                           |
| **Resources**                | The resource types you can assign to your testing plan include: Aurora,<br>Amazon DocumentDB, Amazon DynamoDB, Amazon EBS, Amazon EC2, Amazon EFS, Amazon FSx (Lustre, ONTAP, OpenZFS, Windows),<br>Amazon Neptune, Amazon RDS, and Amazon S3. | All resources can be restored.                                                      |
| **Results**                  | After the restore testing job is completed, the restored resource is<br>deleted after the [Restore testing validation](restore-testing-validation.md "restore-testing-validation.md") window finishes.                                         | Once the restore job is completed, the restored version of the resource<br>remains. |
| **Tags**                     | For resource types which support tag on restore, testing applies tags on<br>restore.                                                                                                                                                           | Tags are optional for supported resources.                                          |

## Restore testing management

You can create, view, update, or delete a restore testing plan in the [AWS Backup console](https://console.aws.amazon.com/backup/ "https://console.aws.amazon.com/backup/").

You can use [AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup") to programmatically carry out operations for restore testing plans. Each
CLI is specific to the AWS service in which it originates. Commands should be prepended
with `aws backup`.

### Data deletion

When a restore test is finished, AWS Backup begins deleting the resources involved in the
test. This deletion is not instantaneous. Each resource has an underlying configuration
that determines how those resources are stored and lifecycled. For example, if Amazon S3
buckets are part of the restore test, [lifecycle rules are added to
the bucket](../../../AmazonS3/latest/userguide/intro-lifecycle-rules.md "../../../AmazonS3/latest/userguide/intro-lifecycle-rules.md"). It can take up to several days for the rules to execute and for the
bucket and its objects to be fully deleted, but charges will only occur for these
resources until the day when the lifecycle rule initiates (by default this is 1 days).
Speed of deletion will depend upon the resource type.

Resources that are part of a restore testing plan contain a tag called
`awsbackup-restore-test`. If a user removes this tag, AWS Backup cannot delete the
resource at the end of the testing period and the user will have to delete it manually
instead.

To check why resources may not have been deleted as expected, you can search through
failed jobs in the console or use the command line interface to call the API request
`DescribeRestoreJob` to retrieve deletion status messages.

Backup plans (non-restore testing plans) ignore resources created by restore testing
(those with tag `awsbackup-restore-test` or a name starting with
`awsbackup-restore-test`).

### Cost control

Restore testing has a cost per restore test. Depending on what resources are included
in your restore testing plan, the restore jobs that are part of the plan may also have a
cost. See [AWS Backup Pricing](https://aws.amazon.com/backup/pricing/ "https://aws.amazon.com/backup/pricing/") for
full details.

When you set up a restore testing plan for the first time, you may find it beneficial
to include a minimum number of resource types and protected resources to familiarize
yourself with the feature, the process, and the average costs involved. You can update a
plan after its creation to add more resource types and protected resources.

## Create a restore testing plan

A restore testing plan has two parts: plan creation and assigning resources.

When you use the console, these parts are sequential. In the first part, you set the
name, frequency, and start times. During the second part you assign resources to your
testing plan.

When using AWS CLI and API, first use [`create-restore-testing-plan`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-restore-testing-plan.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-restore-testing-plan.html"). After you receive a successful
response and the plan has been created, then use [`create-restore-testing-selection`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-restore-testing-selection.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-restore-testing-selection.html"), for each resource type
to include in your plan.

When you create a restore testing plan, we create a service-linked role for you. For
more information, see [Using roles for restore testing](using-service-linked-roles-AWSServiceRoleForBackupRestoreTesting.md "using-service-linked-roles-AWSServiceRoleForBackupRestoreTesting.md").

Console

###### Part I: Create a restore testing plan using the console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the left-hand navigation, locate **Restore testing** and
   select it.
3. Choose **create restore testing plan**.
4. **General**
   1. **Name:** Type in a name for your new restore testing
      plan. The name cannot be changed after creation. The name must consist of only
      alphanumeric characters and underscores.
   2. **Test frequency:** Choose the frequency at which the
      restore tests will run.
   3. **Start Time:** Set the time (in hour and minute) you
      prefer the test to begin. You can also set the local time zone in which you
      want the restore testing plan to operate.
   4. **Start within:** This value (in hours) is the period of
      time in which the restore test is designated to begin. AWS Backup makes a best
      effort to commence all designated restore jobs during the start within time
      and randomizes start times within this period.

5. **Recovery point selection:** Here you set the source vaults,
   the recovery point range, and selection criteria for which recovery points
   (backups) you want to be part of the plan.
   1. **Source vaults:** Choose whether to include all
      available vaults or just specific vaults to help filter which recovery points
      can be in your plan. If you choose **specific vaults**,
      select from the drop down menu the vaults you wish to include.
   2. **Eligible recovery points:** Specify the time frame from
      which recovery points will be selected. You can select 1 to 365 days, 1 to 52
      weeks, 1 to 12 months, or 1 year.
   3. **Selection criteria:** Once your date range of recovery
      points is specified, you can choose whether to include the latest one or one
      at random in your plan. You may wish to choose a random one to gauge the
      general health of recovery points at more regular frequency in case a restore
      to an older version is ever warranted.
   4. **Point-in-time recovery points:** If your plan includes
      resources that have continuous backup (point-in-time-restore/PITR) points, you
      can check this box to have your testing plan include continuous backups as
      eligible recovery points (see [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") for which resources types have
      this feature).

6. _(optional)_
   **Tags added to restore testing plan:** You can choose to add up
   to 50 tags to your restore testing plan. Each tag must be added separately. To add
   a new tag, select **Add new tag**.

###### Part II: Assign resources to the plan using the console

In this section, you choose the resources you have backed up to include in your
restore testing plan. You will choose the name of the resource assignment, choose
the role you use for the restore test, and set the retention period before cleanup.
Then, you will select the resource type, select the scope, and optionally refine
your selection with tags.

###### Tip

To navigate back to the restore testing plan to which you want to add
resources, you can go to the [AWS Backup
console](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup"), select **Restore testing**, then find your
preferred testing plan and select it.

1. **General**
   1. **Resource assignment name:** Input a name for this
      resource assignment using a string of alphanumeric characters and underscores,
      with no white spaces.
   2. **Restore IAM role:** The test must use an Identity and
      Access Management (IAM) role you designate. You can choose the AWS Backup default
      role or a different one. If the AWS Backup default does not yet exist as you finish
      this process, AWS Backup will create it for you automatically with the necessary
      permissions. The IAM role you choose for restore testing must contain the
      permissions found in [AWSBackupServiceRolePolicyForRestores](security-iam-awsmanpol.md#aws-managed-policies "security-iam-awsmanpol.md#aws-managed-policies").
   3. **Retention period before cleanup:** During a restore
      test, backup data is temporarily restored. By default, this data is deleted
      after the test is complete. You have the option to delay deletion of this data
      if you wish to run validation on the restore.

   If you plan to run validation, select **retain for a specific
   number of hours** and input a value from 1 to 168 hours, inclusive.
   Note that validation can be run programmatically but not from the AWS Backup
   console.

2. **Protected resources:**
   1. **Select resource type:** Select which resource types and
      the scope of which backups of those types to include in the resource testing
      plan. Each plan can contain multiple resource types, but each type of resource
      must be assigned to the plan individually.
   2. **Resource selection scope:** Once the type is chosen,
      select if you want to include all available protected resources of that type
      or if you want to include specific protected resources only.
   3. _(optional)_
      **Refine resource selection using tags:** If your backups
      have tags, you can filter by tags to **select specific protected
      resources**. Enter the tag key, the condition for this key to be or
      not to be included, and the value for the key. Then, select the **Add
      tags** button.

   Tags on protected resources are evaluated by checking the tags on the
   latest recovery point within the backup vault containing the protected
   resource.

3. **Restore parameters:** Certain resources require specifying
   parameters in preparation for a restore job. In most cases, AWS Backup will infer the
   values based on the stored backup.

It is recommended in most cases to maintain these parameters; however, you can
change the values by choosing a different selection from the dropdown menu.
Examples where changing the values may be optimal can include overriding
encryption keys, Amazon FSx settings where data cannot be inferred, and creation of
subnets.

For example, if an RDS database is one of the resource types you assign to
your restore testing plan, parameters such as availability zone, database name,
database instance class, and VPC security group will appear with inferred values
you can change if applicable.

AWS CLI
The CLI command `CreateRestoreTestingPlan` is used to make a restore
testing plan.

The testing plan must contain:

- `RestoreTestingPlan`, which must contain a unique
  `RestoreTestingPlanName`
- [`ScheduleExpression`](API_RestoreTestingPlanForCreate.md#Backup-Type-RestoreTestingPlanForCreate-ScheduleExpression "API_RestoreTestingPlanForCreate.md#Backup-Type-RestoreTestingPlanForCreate-ScheduleExpression") cron expression
- [`RecoveryPointSelection`](API_RestoreTestingRecoveryPointSelection.md "API_RestoreTestingRecoveryPointSelection.md")

Though named similarly, this is **NOT** the same as
`RestoreTestingSelection`.

[`RecoveryPointSelection`](API_RestoreTestingRecoveryPointSelection.md "API_RestoreTestingRecoveryPointSelection.md") has five
parameters (three required and two optional). The values you specify determine
which recovery point is included in the restore test. You must indicate with
`Algorithm` if you want the latest recovery point within your
`SelectionWindowDays` or if you want a random recovery point, and you
must indicate through `IncludeVaults` from which vaults the recovery
points can be chosen.

A selection can have one or more protected resource ARNs or can have one or more
conditions, but it cannot have not both.

You can also include:

- [`ScheduleExpressionTimezone`](API_RestoreTestingPlanForCreate.md#Backup-Type-RestoreTestingPlanForCreate-ScheduleExpressionTimeZone "API_RestoreTestingPlanForCreate.md#Backup-Type-RestoreTestingPlanForCreate-ScheduleExpressionTimeZone")
- [`Tags`](API_CreateRestoreTestingPlan.md#Backup-CreateRestoreTestingPlan-request-Tags "API_CreateRestoreTestingPlan.md#Backup-CreateRestoreTestingPlan-request-Tags")
- [`CreatorRequestId`](API_CreateRestoreTestingPlan.md#API_CreateRestoreTestingPlan_RequestSyntax "API_CreateRestoreTestingPlan.md#API_CreateRestoreTestingPlan_RequestSyntax")
- [`StartWindowHours`](API_CreateRestoreTestingPlan.md#API_CreateRestoreTestingPlan_RequestSyntax "API_CreateRestoreTestingPlan.md#API_CreateRestoreTestingPlan_RequestSyntax")

Use CLI command [`create-restore-testing-plan`.](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-restore-testing-plan.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-restore-testing-plan.html")

Once the plan has been created successfully, you need to assign resources to it
using [`create-restore-testing-selection`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-restore-testing-selection.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-restore-testing-selection.html").

This consists of `RestoreTestingSelectionName`,
`ProtectedResourceType`, and one of the following:

###### Note

**RestoreTestingSelectionName naming requirements:**

- Must be 1-256 characters in length
- Can contain letters (a-z, A-Z), numbers (0-9), hyphens (-), and underscores (\_)
- Must start with a letter or number
- Cannot end with a hyphen or underscore
- Must be unique within the restore testing plan

- `ProtectedResourceArns`

- `ProtectedResourceConditions`

Each protected resource type can have one single value. A restore testing
selection can include a wildcard value ("\*") for `ProtectedResourceArns`
along with `ProtectedResourceConditions`. Alternatively, you can include up
to 30 specific protected resource ARNs in `ProtectedResourceArns`.

**Recovery point determination**

Each time a testing plan runs (according to the frequency and start time you specified),
one eligible recovery point per protected resource in selection is restored by the restore
test. If no recovery points for a resource meet the recovery point selection criteria, that
resource will not be included in the test.

A recovery point for a protected resource in a testing selection is eligible if meets
the criteria for the specified time frame and included vaults in the restore testing
plan.

A protected resource is selected if the resource testing selection includes the resource
type and if either of the following conditions are true:

- The resource ARN is specified in that selection; or,
- The tag conditions on that selection match the tags on the latest recovery point for
  the resource

## Update a restore testing plan

You can update parts of your restore testing plan and the resource selections within it
through the console or AWS CLI.

Console

###### Update restore testing plans and selections in the console

When you view the restore testing plan details page in the console, you can edit
(update) many of the settings of your plan. To do this,

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the left-hand navigation, locate **Restore testing** and
   select it.
3. Select the **Edit** button.
4. Adjust the frequency, the start time, and the time the test will begin within
   which the test will begin after the chosen start time.
5. Save your changes.

AWS CLI

###### Update restore testing plans and selections through AWS CLI

Requests [UpdateRestoreTestingPlan](API_UpdateRestoreTestingPlan.md "API_UpdateRestoreTestingPlan.md") and [UpdateRestoreTestingSelection](API_UpdateRestoreTestingSelection.md "API_UpdateRestoreTestingSelection.md") can be used to send partial updates to a
specified plan or selection. The names cannot be changed, but you can update other
parameters. Include only parameters you wish to change in each request.

Before sending an update request, use [GetRestoreTestingPlan](API_GetRestoreTestingPlan.md "API_GetRestoreTestingPlan.md") and [GetRestoreTestingSelection](API_GetRestoreTestingSelection.md "API_GetRestoreTestingSelection.md") to determine if your RestoreTestingSelection
contains specific ARNs or if it uses the wildcard and conditions.

If your restore testing selection has specified ARNs (instead of wildcard) and
you wish to change it to a wildcard with conditions, the update request must include
both the ARN wildcard and the conditions. A selection can have either protected
resource ARNs or use the wildcard with conditions, but it cannot have both.

- [`get-restore-testing-plan`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-restore-testing-plan.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-restore-testing-plan.html")
- [`get-restore-testing-selection`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-restore-testing-selection.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-restore-testing-selection.html")
- [`update-restore-testing-plan`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/updated-restore-testing-plan.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/updated-restore-testing-plan.html")
- [`update-restore-testing-selection`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/update-restore-testing-selection.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/update-restore-testing-selection.html")

## View existing restore testing plans

Console

###### View details about an existing restore testing plan and assigned resources in

the console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Select **Restore testing** from the left-hand navigation. The
   display shows your restore testing plans. The plans are displayed by default by
   last runtime.
3. Select the link from a plan to see its details, including a summary of the
   plan, its name, frequency, start time, and start within value.

You can also view the protected resources within this plan, the restore testing
jobs from the most recent 30 days included in this plan, and any tags you can created
to be part of this testing plan.

AWS CLI

###### Get details about an existing restore testing plan and testing selection using

the command line

- [`list-restore-testing-plan`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-restore-testing-plan.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-restore-testing-plan.html")
- [`list-restore-testing-selections`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-restore-testing-selections.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-restore-testing-selections.html")
- [`get-restore-testing-plan`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-restore-testing-plan.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-restore-testing-plan.html")
- [`get-restore-testing-selection`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-restore-testing-selection.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-restore-testing-selection.html")

## View restore testing jobs

Console

###### View existing restore testing jobs in the console

Restore testing jobs are included on the restore jobs page.

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Navigate to **Jobs** page.

Alternatively, you can select **Restore testing**, then
select a restore testing plan to see its details and the jobs associated with the
plan. 3. Select the **Restore jobs** tab.

On this page, you can view the status, restore time, restore type, resource
ID, resource type, restore testing plan to which the job belongs, the creation
time, and the recovery point ID of the restore job.

Jobs included in a restore testing plan have the restore type
**Test**.

Restore testing jobs have several status categories:

- A **status** type that requires attention is underlined;
  hover over the status to see additional details if they are available.
- A **validation status** will display if [Restore testing validation](restore-testing-validation.md "restore-testing-validation.md") has been initiated on the test (not available within the console).
- Deletion status notes the status of the data generated by a restore test.
  There are three possible deletion statuses: **Successful**,
  **Deleting**, and **Failed**.

If a restore test job deletion failed, you will need to remove the resource
manually since the restore testing flow could not complete it automatically.
Often, a failed deletion is triggered if the tag
`awsbackup-restore-test` is removed from the resource.

AWS CLI

###### View existing restore testing jobs from the command line

- [`list-restore-jobs-by-protected-resource`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-restore-jobs-by-protected-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-restore-jobs-by-protected-resource.html")

## Delete a restore testing plan

Console

###### Delete restore testing plan in the console

1. Go to [View existing restore testing plans](#restore-testing-view "#restore-testing-view") to see your current restore testing
   plans.
2. On the restore testing plan details page, delete a plan by selecting
   **Delete**.
3. After you select delete, a pop-up confirmation screen will appear to ensure
   you want to delete your plan. On this screen, the name of your specific restore
   testing plan will be displayed in bold. To proceed, type in the exact
   case-sensitive name of the testing plan, including any underscores, dashes, and
   periods.

If the option for **Delete restore testing plan** is not
selectable, re-enter the name until it matches the displayed name. Once it is an
exact match, the option to delete the restore testing plan will become
selectable.

AWS CLI

###### Delete restore testing plan through the command line

The CLI command [DeleteRestoreTestingSelection](API_DeleteRestoreTestingSelection.md "API_DeleteRestoreTestingSelection.md") can be used to delete a restore testing
selection. Include `RestoreTestingPlanName` and
`RestoreTestingSelectionName` in the request.

All testing selections associated with a testing plan need to be deleted before
you delete the testing plan. Once all testing selections have been deleted, you can
use the API request [DeleteRestoreTestingPlan](API_DeleteRestoreTestingPlan.md "API_DeleteRestoreTestingPlan.md") to delete a restore testing plan. You need to
include `RestoreTestingPlanName`.

- [`delete-restore-testing-selection`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-restore-testing-selection.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-restore-testing-selection.html")
- [`delete-restore-testing-plan`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-restore-testing-plan.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-restore-testing-plan.html")

## Audit restore testing

Restore testing integrations with AWS Backup Audit manager to help you evaluate if a restored
resource completed within your target restore time.

For more information, see [Restore time for resources meet target](controls-and-remediation.md#restore-time-meets-target-control "controls-and-remediation.md#restore-time-meets-target-control") control in [AWS Backup Audit Manager
controls and remediation](controls-and-remediation.md "controls-and-remediation.md").

## Restore testing quotas and parameters

- 100 restore testing plans
- 50 tags can be added to each restore testing plan
- 30 selections per plan
- 30 protected resource ARNs per selection
- 30 protected resource conditions per selection (including those within both
  `StringEquals` and `StringNotEquals`)
- 30 vault selectors per selection
- Max selection window days: 365 days
- Start window hours: Min: 1 hour; Max: 168 hours (7 days)
- Max plan name length: 50 characters
- Max selection name length: 50 characters

Additional information regarding limits can be viewed at [AWS Backup quotas](aws-backup-limits.md "aws-backup-limits.md").

## Restore testing failure

troubleshooting

If you have restore testing jobs with a restore status of `Failed`, the
following reasons can help you determine the cause and remedy.

Error message(s) [can be
viewed](restore-testing.md#restore-testing-jobs "restore-testing.md#restore-testing-jobs") in the AWS Backup console in the job status details page or by using the
CLI commands `list-restore-jobs-by-protected-resource` or
`list-restore-jobs`.

1. **\*Error:** `No default VPC for this user. `GroupName` is only supported 
for EC2-Classic and default VPC.`\*

**Solution 1:** Update your restore testing selection and [override](restore-testing-inferred-metadata.md "restore-testing-inferred-metadata.md") the parameter `SubnetId`. The AWS Backup console
displays this parameter as "Subnet".

**Solution 2:** Recreate the [default
VPC](../../../vpc/latest/userguide/default-vpc.md#create-default-vpc "../../../vpc/latest/userguide/default-vpc.md#create-default-vpc").

**Resource types affected:** Amazon EC2 2. **\*Error:**
`No subnets found for the default VPC [vpc]. Please specify a
 subnet.`\*

**Solution 1:** Update your restore testing selection and [override](restore-testing-inferred-metadata.md "restore-testing-inferred-metadata.md") the `SubnetId` restore parameter. The AWS Backup console
displays this parameter as "Subnet".

**Solution 2:**
[Create a default
subnet](../../../vpc/latest/userguide/default-vpc.md#create-default-subnet "../../../vpc/latest/userguide/default-vpc.md#create-default-subnet") in the default VPC.

**Resource types affected:** Amazon EC2 3. **\*Error:**
`No default subnet detected in VPC. Please contact AWS Support to recreate default
 Subnets.`\*

**Solution 1:** Update your restore testing selection and [override](restore-testing-inferred-metadata.md "restore-testing-inferred-metadata.md") the `DBSubnetGroupName` restore parameter. The AWS Backup
console displays this parameter as Subnet group.

**Solution 2:**
[Create a default
subnet](../../../vpc/latest/userguide/default-vpc.md#create-default-subnet "../../../vpc/latest/userguide/default-vpc.md#create-default-subnet") in the default VPC.

**Resource types affected:** Amazon Aurora, Amazon DocumentDB, Amazon RDS,
Neptune 4. **\*Error:**
`IAM Role cannot be assumed by AWS Backup`.\*

**Solution:** The restore role must be assumable by AWS Backup. Either
update the role's trust policy in IAM to allow it to be assumed by
`"backup.amazonaws.com"` or update your restore testing selection to use a
role that is assumable by AWS Backup.

**Resource types affected:** all 5. **\*Error:**
`Access denied to KMS key.` or `The specified AWS KMS key
 *ARN* does not exist, is not enabled or you do not have
 permissions to access it.`\*

**Solution:** Verify the following:

    1. The restore role has access to the AWS KMS key used to encrypt your backups and,
     if applicable, the KMS key used to encrypt the restored resource.
    2. The resource policies on the above KMS key(s) allow the restore role to access
     them.

If the above conditions are not yet met, configure the restore role and the resource
policies for appropriate access. Then, run the restore testing job again.

**Resource types affected:** all 6. **\*Errors:**
`User `ARN`is not authorized to perform
`action`on`resource`because
 no identity based policy allows the`action`.` or
`Access denied performing `s3:CreateBucket`on
`awsbackup-restore-test-xxxxxx``.\*

**Solution:** The restore role does not have adequate permissions.
Update the permissions in IAM for the restore role.

**Resource types affected:** all 7. **\*Errors:**
`User `ARN`is not authorized to perform
`action`on`resource`because
 no resource-based policy allows the`action`.` or
`User `ARN`is not authorized to perform
`action`on`resource` with an
 explicit deny in a resource based policy.`\*

**Solution:** The restore role does not have adequate access to the
resource specified in the message. Update the resource policy on the resource
mentioned.

**Resource types affected:** all
