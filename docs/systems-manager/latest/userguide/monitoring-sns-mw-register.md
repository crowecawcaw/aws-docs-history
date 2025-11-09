AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use a maintenance window to send a

command that returns status notifications

The following procedures show how to register a Run Command task with your
maintenance window using the AWS Systems Manager console or the AWS Command Line Interface (AWS CLI). Run Command is
a tool in AWS Systems Manager. The procedures also describe how to configure the Run Command task
to return status notifications.

###### Before you begin

If you haven't created a maintenance window or registered targets, see [Create and manage maintenance windows using
the console](sysman-maintenance-working.md "sysman-maintenance-working.md") for steps on how to create a
maintenance window and register targets.

To receive notifications from the Amazon Simple Notification Service (Amazon SNS) service, attach an
`iam:PassRole` policy to the Maintenance Windows service role specified in the
registered task. If you haven't added `iam:PassRole` permissions to your
Maintenance Windows service role, see [Task 5: Attach the iam:PassRole
policy to your maintenance window role](monitoring-sns-notifications.md#monitoring-sns-passpolicy-mw "monitoring-sns-notifications.md#monitoring-sns-passpolicy-mw").

## Registering a Run Command task

to a maintenance window that returns notifications (console)

Use the following procedure to register a Run Command task that is configured to
return status notifications to your maintenance window using the Systems Manager
console.

###### To register a Run Command task with your maintenance window that returns

notifications (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Maintenance Windows**.
3. Select the maintenance window for which you would like to register a
   Run Command task configured to send Amazon Simple Notification Service (Amazon SNS) notifications.
4. Choose **Actions** and then choose **Register
   Run command task**.
5. (Optional) In the **Name** field, enter a name for
   the task.
6. (Optional) In the **Description** field, enter a
   description.
7. For **Command document**, choose a Command
   document.
8. For **Task priority**, specify a priority for this
   task. Zero (`0`) is the highest priority. Tasks in a
   maintenance window are scheduled in priority order. Tasks that have the
   same priority are scheduled in parallel.
9. In the **Targets** section, select a registered
   target group or select unregistered targets.
10. For **Rate control**:
    - For **Concurrency**, specify either a number or a percentage of
      managed nodes on which to run the command at the same time.

    ###### Note

    If you selected targets by specifying tags applied to managed nodes or by
    specifying AWS resource groups, and you aren't certain how many managed
    nodes are targeted, then restrict the number of targets that can run the
    document at the same time by specifying a percentage.
    - For **Error threshold**, specify when to stop running the command
      on other managed nodes after it fails on either a number or a percentage of nodes.
      For example, if you specify three errors, then Systems Manager stops sending the command when
      the fourth error is received. Managed nodes still processing the command might also
      send errors.

11. In the **IAM service role** area, choose the
    Maintenance Windows service role that has `iam:PassRole` permissions to
    the SNS role.

###### Note

Add `iam:PassRole` permissions to the Maintenance Windows role to
allow Systems Manager to pass the SNS role to Amazon SNS. If you haven't added
`iam:PassRole` permissions, see Task 5 in the topic
[Monitoring Systems Manager status changes using
Amazon SNS notifications](monitoring-sns-notifications.md "monitoring-sns-notifications.md"). 12. (Optional) For **Output options**, to save the command output to a file,
select the **Enable writing output to S3** box. Enter the bucket and prefix
(folder) names in the boxes.

###### Note

The S3 permissions that grant the ability to write the data to an S3 bucket are those
of the instance profile assigned to the managed node, not those of the IAM user
performing this task. For more information, see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md")
or [Create an IAM service role for a
hybrid environment](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md"). In addition, if the specified S3 bucket is in a different
AWS account, verify that the instance profile or IAM service role associated with
the managed node has the necessary permissions to write to that bucket. 13. In the **SNS notifications** section, do the
following:

    * Choose **Enable SNS Notifications**.
    * For **IAM role**, choose the Amazon SNS IAM
     role Amazon Resource Name (ARN) you created in Task 3 in [Monitoring Systems Manager status changes using
     Amazon SNS notifications](monitoring-sns-notifications.md "monitoring-sns-notifications.md") to initiate
     Amazon SNS.
    * For **SNS topic**, enter the Amazon SNS topic ARN
     to be used.
    * For **Event type**, choose the events for
     which you want to receive notifications.
    * For **Notification type**, choose to receive
     notifications for each copy of a command sent to multiple nodes
     (invocations) or the command summary.

14. In the **Parameters** section, enter the required
    parameters based on the Command document you chose.
15. Choose **Register Run command task**.
16. After the next time your maintenance window runs, check your email for
    a message from Amazon SNS and open the email message. Amazon SNS can take a few
    minutes to send the email message.

## Registering a Run Command task to

a maintenance window that returns notifications (CLI)

Use the following procedure to register a Run Command task that is configured to
return status notifications to your maintenance window using the AWS CLI.

###### To register a Run Command task with your maintenance window that returns

notifications (CLI)

###### Note

To better manage your task options, this procedure uses the command
option `--cli-input-json`, with option values stored in a
JSON file.

1. On your local machine, create a file named
   `RunCommandTask.json`.
2. Paste the following contents into the file.

```
{
    "Name": "`Name`",
    "Description": "`Description`",
    "WindowId": "`mw-0c50858d01EXAMPLE`",
    "ServiceRoleArn": "arn:aws:iam::`account-id`:role/`MaintenanceWindowIAMRole`",
    "MaxConcurrency": "`1`",
    "MaxErrors": "`1`",
    "Priority": `3`,
    "Targets": [
        {
            "Key": "WindowTargetIds",
            "Values": [
                "`e32eecb2-646c-4f4b-8ed1-205fbEXAMPLE`"
            ]
        }
    ],
    "TaskType": "RUN_COMMAND",
    "TaskArn": "`CommandDocumentName`",
    "TaskInvocationParameters": {
        "RunCommand": {
            "Comment": "`Comment`",
            "TimeoutSeconds": `3600`,
            "NotificationConfig": {
                "NotificationArn": "arn:aws:sns:`region`:`account-id`:`SNSTopicName`",
                "NotificationEvents": [
                    "`All`"
                ],
                "NotificationType": "`Command`"
            },
            "ServiceRoleArn": "arn:aws:iam::`account-id`:role/`SNSIAMRole`"
        }
    }
}
```

3. Replace the example values with information about your own resources.

You can also restore options we've omitted from this example if you
want to use them. For example, you can save command output to an S3
bucket.

For more information, see
[register-task-with-maintenance-window](../../../cli/latest/reference/ssm/register-task-with-maintenance-window.md "../../../cli/latest/reference/ssm/register-task-with-maintenance-window.md") in the _AWS CLI Command Reference_. 4. Save the file. 5. In the directory on your local machine where you saved the file, run
the following command.

```
aws ssm register-task-with-maintenance-window --cli-input-json file://RunCommandTask.json
```

###### Important

Be sure to include `file://` before the file name. It's
required in this command.

If successful, the command returns information similar to the
following.

```
{
    "WindowTaskId": "j2l8d5b5c-mw66-tk4d-r3g9-1d4d1EXAMPLE"
}

```

6. After the next execution of your maintenance window, check your email
   for a message from Amazon SNS and open the email message. Amazon SNS can take a
   few minutes to send the email message.

For more information about registering tasks for a maintenance window from the
command line, see [Register tasks with the maintenance window](mw-cli-tutorial-tasks.md "mw-cli-tutorial-tasks.md").
