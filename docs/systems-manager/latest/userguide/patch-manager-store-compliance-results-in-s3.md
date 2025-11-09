AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Generating .csv

patch compliance reports

You can use the AWS Systems Manager console to generate patch compliance reports that
are saved as a .csv file to an Amazon Simple Storage Service (Amazon S3) bucket of your choice. You can
generate a single on-demand report or specify a schedule for generating the
reports automatically.

Reports can be generated for a single managed node or for all managed nodes in
your selected AWS account and AWS Region. For a single node, a report
contains comprehensive details, including the IDs of patches related to a node
being noncompliant. For a report on all managed nodes, only summary information
and counts of noncompliant nodes' patches are provided.

After a report is generated, you can use a tool like Amazon Quick Suite to import and
analyze the data. Quick Suite is a business intelligence (BI) service you can use to
explore and interpret information in an interactive visual environment. For more
information, see the [Amazon Quick Suite User Guide](../../../quicksuite/latest/userguide/what-is.md "../../../quicksuite/latest/userguide/what-is.md").

###### Note

When you create a custom patch baseline, you can specify a compliance
severity level for patches approved by that patch baseline, such as
`Critical` or `High`. If the patch state of any
approved patch is reported as `Missing`, then the patch
baseline's overall reported compliance severity is the severity level you
specified.

You can also specify an Amazon Simple Notification Service (Amazon SNS) topic to use for sending
notifications when a report is generated.

###### Service roles for generating patch compliance reports

The first time you generate a report, Systems Manager creates an Automation assume
role named `AWS-SystemsManager-PatchSummaryExportRole` to use for
the export process to S3.

###### Note

If you are exporting compliance data to an encrypted S3 bucket, you must
update its associated AWS KMS key policy to provide the necessary permissions
for `AWS-SystemsManager-PatchSummaryExportRole`. For instance,
add a permission similar to this to your S3 bucket's AWS KMS policy:

```
{
    "Effect": "Allow",
    "Action": [
        "kms:GenerateDataKey"
    ],
    "Resource": "`role-arn`"
}
```

Replace `role-arn` with the Amazon Resource Name
(ARN) of the created in your account, in the format
`arn:aws:iam::`111222333444`:role/service-role/AWS-SystemsManager-PatchSummaryExportRole`.

For more information, see [Key policies in
AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_.

The first time you generate a report on a schedule, Systems Manager creates another
service role named `AWS-EventBridge-Start-SSMAutomationRole`, along
with the service role `AWS-SystemsManager-PatchSummaryExportRole` (if
not created already) to use for the export process.
`AWS-EventBridge-Start-SSMAutomationRole` enables Amazon EventBridge to
start an automation using the runbook [AWS-ExportPatchReportToS3](../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-exportpatchreporttos3.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-exportpatchreporttos3.md").

We recommend against attempting to modify these policies and roles. Doing so
could cause patch compliance report generation to fail. For more information,
see [Troubleshooting
patch compliance report generation](#patch-compliance-reports-troubleshooting "#patch-compliance-reports-troubleshooting").

###### Topics

- [What's in a
  generated patch compliance report?](#patch-compliance-reports-to-s3-examples "#patch-compliance-reports-to-s3-examples")
- [Generating
  patch compliance reports for a single managed node](#patch-compliance-reports-to-s3-one-instance "#patch-compliance-reports-to-s3-one-instance")
- [Generating
  patch compliance reports for all managed nodes](#patch-compliance-reports-to-s3-all-instances "#patch-compliance-reports-to-s3-all-instances")
- [Viewing patch
  compliance reporting history](#patch-compliance-reporting-history "#patch-compliance-reporting-history")
- [Viewing patch
  compliance reporting schedules](#patch-compliance-reporting-schedules "#patch-compliance-reporting-schedules")
- [Troubleshooting
  patch compliance report generation](#patch-compliance-reports-troubleshooting "#patch-compliance-reports-troubleshooting")

## What's in a

generated patch compliance report?

This topic provides information about the types of content included in the
patch compliance reports that are generated and downloaded to a specified S3
bucket.

A report generated for a single managed node provides both summary
and detailed information.

[Download a sample report (single node)](samples/Sample-single-instance-patch-compliance-report.md "samples/Sample-single-instance-patch-compliance-report.md")

Summary information for a single managed node includes the
following:

- Index
- Instance ID
- Instance name
- Instance IP
- Platform name
- Platform version
- SSM Agent version
- Patch baseline
- Patch group
- Compliance status
- Compliance severity
- Noncompliant Critical severity patch count
- Noncompliant High severity patch count
- Noncompliant Medium severity patch count
- Noncompliant Low severity patch count
- Noncompliant Informational severity patch count
- Noncompliant Unspecified severity patch count
  Detailed information for a single managed node includes the
  following:

- Index
- Instance ID
- Instance name
- Patch name
- KB ID/Patch ID
- Patch state
- Last report time
- Compliance level
- Patch severity
- Patch classification
- CVE ID
- Patch baseline
- Logs URL
- Instance IP
- Platform name
- Platform version
- SSM Agent version

###### Note

When you create a custom patch baseline, you can specify a
compliance severity level for patches approved by that patch
baseline, such as `Critical` or `High`. If
the patch state of any approved patch is reported as
`Missing`, then the patch baseline's overall
reported compliance severity is the severity level you
specified.

A report generated for all managed nodes provides only summary
information.

[Download a sample report (all managed nodes)](samples/Sample-all-instances-patch-compliance-report.md "samples/Sample-all-instances-patch-compliance-report.md")

Summary information for all managed nodes includes the
following:

- Index
- Instance ID
- Instance name
- Instance IP
- Platform name
- Platform version
- SSM Agent version
- Patch baseline
- Patch group
- Compliance status
- Compliance severity
- Noncompliant Critical severity patch count
- Noncompliant High severity patch count
- Noncompliant Medium severity patch count
- Noncompliant Low severity patch count
- Noncompliant Informational severity patch count
- Noncompliant Unspecified severity patch count

## Generating

patch compliance reports for a single managed node

Use the following procedure to generate a patch summary report for a
single managed node in your AWS account. The report for a single managed
node provides details about each patch that is out of compliance, including
patch names and IDs.

###### To generate patch compliance reports for a single managed

node

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Patch Manager**.
3. Choose the **Compliance reporting** tab.
4. Choose the button for the row of the managed node for which you
   want to generate a report, and then choose **View
   detail**.
5. In the **Patch summary** section, choose
   **Export to S3**.
6. For **Report name**, enter a name to help you
   identify the report later.
7. For **Reporting frequency**, choose one of the
   following:
   - **On demand** – Create a one-time
     report. Skip to Step 9.
   - **On a schedule** – Specify a
     recurring schedule for automatically generating reports.
     Continue to Step 8.

8. For **Schedule type**, specify either a rate
   expression, such as every 3 days, or provide a cron expression to
   set the report frequency.

For information about cron expressions, see [Reference: Cron and rate expressions
for Systems Manager](reference-cron-and-rate-expressions.md "reference-cron-and-rate-expressions.md"). 9. For **Bucket name**, select the name of an S3
bucket where you want to store the .csv report files.

###### Important

If you're working in an AWS Region that was launched after
March 20, 2019, you must select an S3 bucket in that same
Region. Regions launched after that date were turned off by
default. For more information and a list of these Regions, see
[Enabling a Region](../../../general/latest/gr/rande-manage.md#rande-manage-enable "../../../general/latest/gr/rande-manage.md#rande-manage-enable") in the
_Amazon Web Services General Reference_. 10. (Optional) To send notifications when the report is generated,
expend the **SNS topic** section, and then choose
an existing Amazon SNS topic from **SNS topic Amazon Resource
Name (ARN)**. 11. Choose **Submit**.

For information about viewing a history of generated reports, see [Viewing patch
compliance reporting history](#patch-compliance-reporting-history "#patch-compliance-reporting-history").

For information about viewing details of reporting schedules you have
created, see [Viewing patch
compliance reporting schedules](#patch-compliance-reporting-schedules "#patch-compliance-reporting-schedules").

## Generating

patch compliance reports for all managed nodes

Use the following procedure to generate a patch summary report for all
managed nodes in your AWS account. The report for all managed nodes
indicates which nodes are out of compliance and the numbers of noncompliant
patches. It doesn't provide the names or other identifiers of the patches.
For these additional details, you can generate a patch compliance report for
a single managed node. For information, see [Generating
patch compliance reports for a single managed node](#patch-compliance-reports-to-s3-one-instance "#patch-compliance-reports-to-s3-one-instance") earlier in
this topic.

###### To generate patch compliance reports for all managed nodes

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Patch Manager**.
3. Choose the **Compliance reporting** tab.
4. Choose **Export to S3**. (Don't select a node ID
   first.)
5. For **Report name**, enter a name to help you
   identify the report later.
6. For **Reporting frequency**, choose one of the
   following:
   - **On demand** – Create a one-time
     report. Skip to Step 8.
   - **On a schedule** – Specify a
     recurring schedule for automatically generating reports.
     Continue to Step 7.

7. For **Schedule type**, specify either a rate
   expression, such as every 3 days, or provide a cron expression to
   set the report frequency.

For information about cron expressions, see [Reference: Cron and rate expressions
for Systems Manager](reference-cron-and-rate-expressions.md "reference-cron-and-rate-expressions.md"). 8. For **Bucket name**, select the name of an S3
bucket where you want to store the .csv report files.

###### Important

If you're working in an AWS Region that was launched after
March 20, 2019, you must select an S3 bucket in that same
Region. Regions launched after that date were turned off by
default. For more information and a list of these Regions, see
[Enabling a Region](../../../general/latest/gr/rande-manage.md#rande-manage-enable "../../../general/latest/gr/rande-manage.md#rande-manage-enable") in the
_Amazon Web Services General Reference_. 9. (Optional) To send notifications when the report is generated,
expend the **SNS topic** section, and then choose
an existing Amazon SNS topic from **SNS topic Amazon Resource
Name (ARN)**. 10. Choose **Submit**.

For information about viewing a history of generated reports, see [Viewing patch
compliance reporting history](#patch-compliance-reporting-history "#patch-compliance-reporting-history").

For information about viewing details of reporting schedules you have
created, see [Viewing patch
compliance reporting schedules](#patch-compliance-reporting-schedules "#patch-compliance-reporting-schedules").

## Viewing patch

compliance reporting history

Use the information in this topic to help you view details about the patch
compliance reports generated in your AWS account.

###### To view patch compliance reporting history

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Patch Manager**.
3. Choose the **Compliance reporting** tab.
4. Choose **View all S3 exports**, and then choose
   the **Export history** tab.

## Viewing patch

compliance reporting schedules

Use the information in this topic to help you view details about the patch
compliance reporting schedules created in your AWS account.

###### To view patch compliance reporting history

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Patch Manager**.
3. Choose the **Compliance reporting** tab.
4. Choose **View all S3 exports**, and then choose
   the **Report schedule rules** tab.

## Troubleshooting

patch compliance report generation

Use the following information to help you troubleshoot problems with
generating patch compliance report generation in Patch Manager, a tool in
AWS Systems Manager.

###### Topics

- [A message
  reports that the
  AWS-SystemsManager-PatchManagerExportRolePolicy
  policy is corrupted](#patch-compliance-reports-troubleshooting-1 "#patch-compliance-reports-troubleshooting-1")
- [After
  deleting patch compliance policies or roles, scheduled reports
  aren't generated successfully](#patch-compliance-reports-troubleshooting-2 "#patch-compliance-reports-troubleshooting-2")

### A message

reports that the
`AWS-SystemsManager-PatchManagerExportRolePolicy`
policy is corrupted

**Problem**: You receive an error message
similar to the following, indicating the
`AWS-SystemsManager-PatchManagerExportRolePolicy` is
corrupted:

```
An error occurred while updating the AWS-SystemsManager-PatchManagerExportRolePolicy
policy. If you have edited the policy, you might need to delete the policy, and any
role that uses it, then try again. Systems Manager recreates the roles and policies
you have deleted.
```

- **Solution**: Use the Patch Manager
  console or AWS CLI to delete the affected roles and policies
  before generating a new patch compliance report.

###### To delete the corrupt policy using the console

    1. Open the IAM console at
     [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
    2. Do one of the following:


    **On-demand reports**
     – If the problem occurred while generating a
     one-time on-demand report, in the left navigation,
     choose **Policies**, search for
     `AWS-SystemsManager-PatchManagerExportRolePolicy`,
     then delete the policy. Next, choose
     **Roles**, search for
     `AWS-SystemsManager-PatchSummaryExportRole`,
     then delete the role.


    **Scheduled reports**
     – If the problem occurred while generating a
     report on a schedule, in the left navigation, choose
     **Policies**, search one at a time
     for
     `AWS-EventBridge-Start-SSMAutomationRolePolicy`
     and
     `AWS-SystemsManager-PatchManagerExportRolePolicy`,
     and delete each policy. Next, choose
     **Roles**, search one at a time for
     `AWS-EventBridge-Start-SSMAutomationRole`
     and
     `AWS-SystemsManager-PatchSummaryExportRole`,
     and delete each role.

###### To delete the corrupt policy using the AWS CLI

Replace the `placeholder values`
with your account ID.

    + If the problem occurred while generating a one-time
     on-demand report, run the following commands:



    ```
    aws iam delete-policy --policy-arn arn:aws:iam::`account-id`:policy/AWS-SystemsManager-PatchManagerExportRolePolicy
    ```


    ```
    aws iam delete-role --role-name AWS-SystemsManager-PatchSummaryExportRole
    ```

    If the problem occurred while generating a report on a
     schedule, run the following commands:



    ```
    aws iam delete-policy --policy-arn arn:aws:iam::`account-id`:policy/AWS-EventBridge-Start-SSMAutomationRolePolicy
    ```


    ```
    aws iam delete-policy --policy-arn arn:aws:iam::`account-id`:policy/AWS-SystemsManager-PatchManagerExportRolePolicy
    ```


    ```
    aws iam delete-role --role-name AWS-EventBridge-Start-SSMAutomationRole
    ```


    ```
    aws iam delete-role --role-name AWS-SystemsManager-PatchSummaryExportRole
    ```

After completing either procedure, follow the steps to
generate or schedule a new patch compliance report.

### After

deleting patch compliance policies or roles, scheduled reports
aren't generated successfully

**Problem**: The first time you generate
a report, Systems Manager creates a service role and a policy to use for the
export process (`AWS-SystemsManager-PatchSummaryExportRole`
and `AWS-SystemsManager-PatchManagerExportRolePolicy`). The
first time you generate a report on a schedule, Systems Manager creates another
service role and a policy
(`AWS-EventBridge-Start-SSMAutomationRole` and
`AWS-EventBridge-Start-SSMAutomationRolePolicy`). These
let Amazon EventBridge start an automation using the runbook [AWS-ExportPatchReportToS3](../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-exportpatchreporttos3.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-exportpatchreporttos3.md") .

If you delete any of these policies or roles, the connections between
your schedule and your specified S3 bucket and Amazon SNS topic might be
lost.

- **Solution**: To work around this
  problem, we recommend deleting the previous schedule and
  creating a new schedule to replace the one that was experiencing
  issues.
