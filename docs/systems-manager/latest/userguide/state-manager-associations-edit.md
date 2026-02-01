• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Editing and creating a new version

of an association

You can edit a State Manager association to specify a new name, schedule, severity
level, targets, or other values. For associations based on SSM Command-type
documents, you can also choose to write the output of the command to an Amazon Simple Storage Service
(Amazon S3) bucket. After you edit an association, State Manager creates a new version. You
can view different versions after editing, as described in the following procedures.

###### Note

In order for associations that are created with Automation runbooks to be
applied when new target nodes are detected, certain conditions must be met. For
information, see [About target updates with Automation
runbooks](state-manager-about.md#runbook-target-updates "state-manager-about.md#runbook-target-updates").

The following procedures describe how to edit and create a new version of an
association using the Systems Manager console, AWS Command Line Interface (AWS CLI), and AWS Tools for PowerShell (Tools for PowerShell).

###### Important

State Manager doesn't support running associations that use a new version of a
document if that document is shared from another account. State Manager always runs
the `default` version of a document if shared from another account,
even though the Systems Manager console shows that a new version was processed. If you
want to run an association using a new version of a document shared form another
account, you must set the document version to `default`.

## Edit an association

(console)

The following procedure describes how to use the Systems Manager console to edit and
create a new version of an association.

###### Note

For associations that use SSM Command documents, not Automation runbooks,
this procedure requires that you have write access to an existing Amazon S3
bucket. If you haven't used Amazon S3 before, be aware that you will incur
charges for using Amazon S3. For information about how to create a bucket, see
[Create a
Bucket](../../../AmazonS3/latest/userguide/CreatingABucket.md "../../../AmazonS3/latest/userguide/CreatingABucket.md").

###### To edit a State Manager association

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **State Manager**.
3. Choose an existing association, and then choose
   **Edit**.
4. Reconfigure the association to meet your current requirements.

For information about association options with `Command`
and `Policy` documents, see [Creating associations](state-manager-associations-creating.md "state-manager-associations-creating.md"). For
information about association options with Automation runbooks, see
[Scheduling
automations with State Manager associations](scheduling-automations-state-manager-associations.md "scheduling-automations-state-manager-associations.md"). 5. Choose **Save Changes**. 6. (Optional) To view association information, in the
**Associations** page, choose the name of the
association you edited, and then choose the
**Versions** tab. The system lists each version of
the association you created and edited. 7. (Optional) To view output for associations based on SSM
`Command` documents, do the following:

    1. Open the Amazon S3 console at
     [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
    2. Choose the name of the Amazon S3 bucket you specified for storing
     command output, and then choose the folder named with the ID of
     the node that ran the association. (If you chose to store output
     in a folder in the bucket, open it first.)
    3. Drill down several levels, through the
     `awsrunPowerShell` folder, to the
     `stdout` file.
    4. Choose **Open** or
     **Download** to view the host name.

## Edit an

association (command line)

The following procedure describes how to use the AWS CLI (on Linux or Windows Server)
or AWS Tools for PowerShell to edit and create a new version of an association.

###### To edit a State Manager association

1. Install and configure the AWS CLI or the AWS Tools for PowerShell, if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and [Installing the
AWS Tools for PowerShell](../../../powershell/latest/userguide/pstools-getting-set-up.md "../../../powershell/latest/userguide/pstools-getting-set-up.md"). 2. Use the following format to create a command to edit and create a new
version of an existing State Manager association. Replace each
`example resource placeholder` with your
own information.

###### Important

When you call `update-association`, the
system drops all optional parameters from the request and overwrites
the association with null values for those parameters. This is by
design. You must specify all optional parameters in the call, even
if you are not changing the parameters. This includes the
`--name` parameter. Before calling this action, we
recommend that you call the
`describe-association` operation and
make a note of all optional parameters required for your
`update-association` call.

Linux & macOS

```
aws ssm update-association \
    --name `document_name` \
    --document-version `version_of_document_applied` \
    --instance-id `instances_to_apply_association_on` \
    --parameters `(if any)` \
    --targets `target_options` \
    --schedule-expression "`cron_or_rate_expression`" \
    --schedule-offset "`number_between_1_and_6`" \
    --output-location `s3_bucket_to_store_output_details` \
    --association-name `association_name` \
    --max-errors `a_number_of_errors_or_a_percentage_of_target_set` \
    --max-concurrency `a_number_of_instances_or_a_percentage_of_target_set` \
    --compliance-severity `severity_level` \
    --calendar-names `change_calendar_names` \
    --target-locations `aws_region_or_account`
```

Windows

```
aws ssm update-association ^
    --name `document_name` ^
    --document-version `version_of_document_applied` ^
    --instance-id `instances_to_apply_association_on` ^
    --parameters `(if any)` ^
    --targets `target_options` ^
    --schedule-expression "`cron_or_rate_expression`" ^
    --schedule-offset "`number_between_1_and_6`" ^
    --output-location `s3_bucket_to_store_output_details` ^
    --association-name `association_name` ^
    --max-errors `a_number_of_errors_or_a_percentage_of_target_set` ^
    --max-concurrency `a_number_of_instances_or_a_percentage_of_target_set` ^
    --compliance-severity `severity_level` ^
    --calendar-names `change_calendar_names` ^
    --target-locations `aws_region_or_account`
```

PowerShell

```
Update-SSMAssociation `
    -Name `document_name` `
    -DocumentVersion `version_of_document_applied` `
    -InstanceId `instances_to_apply_association_on` `
    -Parameters `(if any)` `
    -Target `target_options` `
    -ScheduleExpression "`cron_or_rate_expression`" `
    -ScheduleOffset "`number_between_1_and_6`" `
    -OutputLocation `s3_bucket_to_store_output_details` `
    -AssociationName `association_name` `
    -MaxError  `a_number_of_errors_or_a_percentage_of_target_set`
    -MaxConcurrency `a_number_of_instances_or_a_percentage_of_target_set` `
    -ComplianceSeverity `severity_level` `
    -CalendarNames `change_calendar_names` `
    -TargetLocations `aws_region_or_account`
```

The following example updates an existing association to change the
name to `TestHostnameAssociation2`. The new association
version runs every hour and writes the output of commands to the
specified Amazon S3 bucket.

Linux & macOS

```
aws ssm update-association \
  --association-id 8dfe3659-4309-493a-8755-01234EXAMPLE \
  --association-name TestHostnameAssociation2 \
  --parameters commands="echo Association" \
  --output-location S3Location='{OutputS3Region=us-east-1,OutputS3BucketName=amzn-s3-demo-bucket,OutputS3KeyPrefix=logs}' \
  --schedule-expression "cron(0 */1 * * ? *)"
```

Windows

```
aws ssm update-association ^
  --association-id 8dfe3659-4309-493a-8755-01234EXAMPLE ^
  --association-name TestHostnameAssociation2 ^
  --parameters commands="echo Association" ^
  --output-location S3Location='{OutputS3Region=us-east-1,OutputS3BucketName=amzn-s3-demo-bucket,OutputS3KeyPrefix=logs}' ^
  --schedule-expression "cron(0 */1 * * ? *)"
```

PowerShell

```
Update-SSMAssociation `
  -AssociationId b85ccafe-9f02-4812-9b81-01234EXAMPLE `
  -AssociationName TestHostnameAssociation2 `
  -Parameter @{"commands"="echo Association"} `
  -S3Location_OutputS3BucketName amzn-s3-demo-bucket `
  -S3Location_OutputS3KeyPrefix logs `
  -S3Location_OutputS3Region us-east-1 `
  -ScheduleExpression "cron(0 */1 * * ? *)"
```

The following example updates an existing association to change the
name to `CalendarAssociation`. The new association runs when
the calendar is open and writes command output to the specified Amazon S3
bucket.

Linux & macOS

```
aws ssm update-association \
  --association-id 8dfe3659-4309-493a-8755-01234EXAMPLE \
  --association-name CalendarAssociation \
  --parameters commands="echo Association" \
  --output-location S3Location='{OutputS3Region=us-east-1,OutputS3BucketName=amzn-s3-demo-bucket,OutputS3KeyPrefix=logs}' \
  --calendar-names "arn:aws:ssm:us-east-1:123456789012:document/testCalendar2"
```

Windows

```
aws ssm update-association ^
  --association-id 8dfe3659-4309-493a-8755-01234EXAMPLE ^
  --association-name CalendarAssociation ^
  --parameters commands="echo Association" ^
  --output-location S3Location='{OutputS3Region=us-east-1,OutputS3BucketName=amzn-s3-demo-bucket,OutputS3KeyPrefix=logs}' ^
  --calendar-names "arn:aws:ssm:us-east-1:123456789012:document/testCalendar2"
```

PowerShell

```
Update-SSMAssociation `
  -AssociationId b85ccafe-9f02-4812-9b81-01234EXAMPLE `
  -AssociationName CalendarAssociation `
  -AssociationName OneTimeAssociation `
  -Parameter @{"commands"="echo Association"} `
  -S3Location_OutputS3BucketName amzn-s3-demo-bucket `
  -CalendarNames "arn:aws:ssm:us-east-1:123456789012:document/testCalendar2"
```

The following example updates an existing association to change the
name to `MultiCalendarAssociation`. The new association runs
when the calendars are open and writes command output to the specified
Amazon S3 bucket.

Linux & macOS

```
aws ssm update-association \
  --association-id 8dfe3659-4309-493a-8755-01234EXAMPLE \
  --association-name MultiCalendarAssociation \
  --parameters commands="echo Association" \
  --output-location S3Location='{OutputS3Region=us-east-1,OutputS3BucketName=amzn-s3-demo-bucket,OutputS3KeyPrefix=logs}' \
  --calendar-names "arn:aws:ssm:us-east-1:123456789012:document/testCalendar1" "arn:aws:ssm:us-east-2:123456789012:document/testCalendar2"
```

Windows

```
aws ssm update-association ^
  --association-id 8dfe3659-4309-493a-8755-01234EXAMPLE ^
  --association-name MultiCalendarAssociation ^
  --parameters commands="echo Association" ^
  --output-location S3Location='{OutputS3Region=us-east-1,OutputS3BucketName=amzn-s3-demo-bucket,OutputS3KeyPrefix=logs}' ^
  --calendar-names "arn:aws:ssm:us-east-1:123456789012:document/testCalendar1" "arn:aws:ssm:us-east-2:123456789012:document/testCalendar2"
```

PowerShell

```
Update-SSMAssociation `
  -AssociationId b85ccafe-9f02-4812-9b81-01234EXAMPLE `
  -AssociationName MultiCalendarAssociation `
  -Parameter @{"commands"="echo Association"} `
  -S3Location_OutputS3BucketName amzn-s3-demo-bucket `
  -CalendarNames "arn:aws:ssm:us-east-1:123456789012:document/testCalendar1" "arn:aws:ssm:us-east-2:123456789012:document/testCalendar2"
```

3. To view the new version of the association, run the following
   command.

Linux & macOS

```
aws ssm describe-association \
  --association-id b85ccafe-9f02-4812-9b81-01234EXAMPLE
```

Windows

```
aws ssm describe-association ^
  --association-id b85ccafe-9f02-4812-9b81-01234EXAMPLE
```

PowerShell

```
Get-SSMAssociation `
  -AssociationId b85ccafe-9f02-4812-9b81-01234EXAMPLE | Select-Object *
```

The system returns information like the following.

Linux & macOS

```
{
    "AssociationDescription": {
        "ScheduleExpression": "cron(0 */1 * * ? *)",
        "OutputLocation": {
            "S3Location": {
                "OutputS3KeyPrefix": "logs",
                "OutputS3BucketName": "amzn-s3-demo-bucket",
                "OutputS3Region": "us-east-1"
            }
        },
        "Name": "AWS-RunPowerShellScript",
        "Parameters": {
            "commands": [
                "echo Association"
            ]
        },
        "LastExecutionDate": 1559316400.338,
        "Overview": {
            "Status": "Success",
            "DetailedStatus": "Success",
            "AssociationStatusAggregatedCount": {}
        },
        "AssociationId": "b85ccafe-9f02-4812-9b81-01234EXAMPLE",
        "DocumentVersion": "$DEFAULT",
        "LastSuccessfulExecutionDate": 1559316400.338,
        "LastUpdateAssociationDate": 1559316389.753,
        "Date": 1559314038.532,
        "AssociationVersion": "2",
        "AssociationName": "TestHostnameAssociation2",
        "Targets": [
            {
                "Values": [
                    "Windows"
                ],
                "Key": "tag:Environment"
            }
        ]
    }
}
```

Windows

```
{
    "AssociationDescription": {
        "ScheduleExpression": "cron(0 */1 * * ? *)",
        "OutputLocation": {
            "S3Location": {
                "OutputS3KeyPrefix": "logs",
                "OutputS3BucketName": "amzn-s3-demo-bucket",
                "OutputS3Region": "us-east-1"
            }
        },
        "Name": "AWS-RunPowerShellScript",
        "Parameters": {
            "commands": [
                "echo Association"
            ]
        },
        "LastExecutionDate": 1559316400.338,
        "Overview": {
            "Status": "Success",
            "DetailedStatus": "Success",
            "AssociationStatusAggregatedCount": {}
        },
        "AssociationId": "b85ccafe-9f02-4812-9b81-01234EXAMPLE",
        "DocumentVersion": "$DEFAULT",
        "LastSuccessfulExecutionDate": 1559316400.338,
        "LastUpdateAssociationDate": 1559316389.753,
        "Date": 1559314038.532,
        "AssociationVersion": "2",
        "AssociationName": "TestHostnameAssociation2",
        "Targets": [
            {
                "Values": [
                    "Windows"
                ],
                "Key": "tag:Environment"
            }
        ]
    }
}
```

PowerShell

```
AssociationId                 : b85ccafe-9f02-4812-9b81-01234EXAMPLE
AssociationName               : TestHostnameAssociation2
AssociationVersion            : 2
AutomationTargetParameterName :
ComplianceSeverity            :
Date                          : 5/31/2019 2:47:18 PM
DocumentVersion               : $DEFAULT
InstanceId                    :
LastExecutionDate             : 5/31/2019 3:26:40 PM
LastSuccessfulExecutionDate   : 5/31/2019 3:26:40 PM
LastUpdateAssociationDate     : 5/31/2019 3:26:29 PM
MaxConcurrency                :
MaxErrors                     :
Name                          : AWS-RunPowerShellScript
OutputLocation                : Amazon.SimpleSystemsManagement.Model.InstanceAssociationOutputLocation
Overview                      : Amazon.SimpleSystemsManagement.Model.AssociationOverview
Parameters                    : {[commands, Amazon.Runtime.Internal.Util.AlwaysSendList`1[System.String]]}
ScheduleExpression            : cron(0 */1 * * ? *)
Status                        :
Targets                       : {tag:Environment}
```
