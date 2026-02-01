• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Canceling a command

You can attempt to cancel a command as long as the service shows that it's in
either a Pending or Executing state. However, even if a command is still in one of
these states, we can't guarantee that the command will be canceled and the
underlying process stopped.

###### To cancel a command using the console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Run Command**.
3. Select the command invocation that you want to cancel.
4. Choose **Cancel command**.

###### To cancel a command using the AWS CLI

Run the following command. Replace each `example resource
 placeholder` with your own information.

Linux & macOS

```
aws ssm cancel-command \
    --command-id "`command-ID`" \
    --instance-ids "`instance-ID`"
```

Windows

```
aws ssm cancel-command ^
    --command-id "`command-ID`" ^
    --instance-ids "`instance-ID`"
```

For information about the status of a canceled command, see [Understanding command statuses](monitor-commands.md "monitor-commands.md").
