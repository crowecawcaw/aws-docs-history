• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use Run Command to send a command that returns

status notifications

The following procedures show how to use the AWS Command Line Interface (AWS CLI) or AWS Systems Manager
console to send a command through Run Command, a tool in AWS Systems Manager, that is configured
to return status notifications.

## Sending a Run Command that returns

notifications (console)

Use the following procedure to send a command through Run Command that is
configured to return status notifications using the Systems Manager console.

###### To send a command that returns notifications (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Run Command**.
3. Choose **Run command**.
4. In the **Command document** list, choose a Systems Manager
   document.
5. In the **Command parameters** section, specify values
   for required parameters.
6. In the **Targets** section, choose the managed nodes on which you want to
   run this operation by specifying tags, selecting instances or edge devices manually, or
   specifying a resource group.

###### Tip

If a managed node you expect to see isn't listed, see [Troubleshooting managed
node availability](fleet-manager-troubleshooting-managed-nodes.md "fleet-manager-troubleshooting-managed-nodes.md") for troubleshooting
tips. 7. For **Other parameters**:

    * For **Comment**, enter information about this command.
    * For **Timeout (seconds)**, specify the number of seconds for the
     system to wait before failing the overall command execution.

8. For **Rate control**:
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

9. (Optional) For **Output options**, to save the command output to a file,
   select the **Write command output to an S3 bucket** box. Enter the bucket
   and prefix (folder) names in the boxes.

###### Note

The S3 permissions that grant the ability to write the data to an S3 bucket are those
of the instance profile (for EC2 instances) or IAM service role (hybrid-activated
machines) assigned to the instance, not those of the IAM user performing this task.
For more information, see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md") or [Create an IAM service role for a hybrid
environment](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md"). In addition, if the specified S3 bucket is in a different
AWS account, make sure that the instance profile or IAM service role associated with
the managed node has the necessary permissions to write to that bucket. 10. In the **SNS Notifications** section, choose
**Enable SNS notifications**. 11. For **IAM role**, choose the Amazon SNS IAM role ARN
you created in Task 3 in [Monitoring Systems Manager status changes using
Amazon SNS notifications](monitoring-sns-notifications.md "monitoring-sns-notifications.md"). 12. For **SNS topic**, enter the Amazon SNS topic ARN to be
used. 13. For **Event notifications**, choose the events for
which you want to receive notifications. 14. For **Change notifications**, choose to receive
notifications for the command summary only (**Command status
changes**) or for each copy of a command sent to multiple
nodes (**Command status on each instance changes**)
. 15. Choose **Run**. 16. Check your email for a message from Amazon SNS and open the email message.
Amazon SNS can take several minutes to send the email message.

## Sending a Run Command that returns

notifications (CLI)

Use the following procedure to send a command through Run Command that is
configured to return status notifications using the AWS CLI.

###### To send a command that returns notifications (CLI)

1. Open the AWS CLI.
2. Specify parameters in the following command to target based on managed
   node IDs.

```
aws ssm send-command --instance-ids "`ID-1, ID-2`" --document-name "`Name`" --parameters `'{"commands":["input"]}'` --service-role `"SNSRoleARN"` --notification-config '{"NotificationArn":"`SNSTopicName`","NotificationEvents":["`All`"],"NotificationType":"`Command`"}'
```

Following is an example.

```
aws ssm send-command --instance-ids "i-02573cafcfEXAMPLE, i-0471e04240EXAMPLE" --document-name "AWS-RunPowerShellScript" --parameters '{"commands":["Get-Process"]}' --service-role "arn:aws:iam::111122223333:role/SNS_Role" --notification-config '{"NotificationArn":"arn:aws:sns:us-east-1:111122223333:SNSTopic","NotificationEvents":["All"],"NotificationType":"Command"}'
```

###### Alternative commands

Specify parameters in the following command to target managed
instances using tags.

```
aws ssm send-command --targets "Key=tag:`TagName`,Values=`TagKey`" --document-name "`Name`" --parameters `'{"commands":["input"]}'` --service-role `"SNSRoleARN"` --notification-config '{"NotificationArn":"`SNSTopicName`","NotificationEvents":["`All`"],"NotificationType":"`Command`"}'
```

Following is an example.

```
aws ssm send-command --targets "Key=tag:Environment,Values=Dev" --document-name "AWS-RunPowerShellScript" --parameters '{"commands":["Get-Process"]}' --service-role "arn:aws:iam::111122223333:role/SNS_Role" --notification-config '{"NotificationArn":"arn:aws:sns:us-east-1:111122223333:SNSTopic","NotificationEvents":["All"],"NotificationType":"Command"}'
```

3. Press **Enter**.
4. Check your email for a message from Amazon SNS and open the email message.
   Amazon SNS can take several minutes to send the email message.

For more information, see [send-command](../../../cli/latest/reference/ssm/send-command.md "../../../cli/latest/reference/ssm/send-command.md") in the _AWS CLI Command Reference_.
