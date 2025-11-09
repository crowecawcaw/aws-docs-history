AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Running commands from the console

You can use Run Command, a tool in AWS Systems Manager, from the AWS Management Console to configure managed
nodes without having to log into them. This topic includes an example that shows how
to [update SSM Agent](run-command-tutorial-update-software.md#rc-console-agentexample "run-command-tutorial-update-software.md#rc-console-agentexample") on a managed node
by using Run Command.

###### Before you begin

Before you send a command using Run Command, verify that your managed nodes meet
all Systems Manager [setup
requirements](systems-manager-setting-up-nodes.md "systems-manager-setting-up-nodes.md").

###### To send a command using Run Command

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Run Command**.
3. Choose **Run command**.
4. In the **Command document** list, choose a Systems Manager
   document.
5. In the **Command parameters** section, specify values for
   required parameters.
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

9. (Optional) Choose a CloudWatch alarm to apply to your command for monitoring. To
   attach a CloudWatch alarm to your command, the IAM principal that runs the
   command must have permission for the
   `iam:createServiceLinkedRole` action. For more information
   about CloudWatch alarms, see [Using
   Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md"). Note that if your alarm activates, any pending
   command invocations do not run.
10. (Optional) For **Output options**, to save the command output to a file,
    select the **Write command output to an S3 bucket** box. Enter the bucket
    and prefix (folder) names in the boxes.

###### Note

The S3 permissions that grant the ability to write the data to an S3 bucket are those
of the instance profile (for EC2 instances) or IAM service role (hybrid-activated
machines) assigned to the instance, not those of the IAM user performing this task.
For more information, see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md") or [Create an IAM service role for a hybrid
environment](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md"). In addition, if the specified S3 bucket is in a different
AWS account, make sure that the instance profile or IAM service role associated with
the managed node has the necessary permissions to write to that bucket. 11. In the **SNS notifications** section, if you want notifications sent
about the status of the command execution, select the **Enable SNS
notifications** check box.

For more information about configuring Amazon SNS notifications for Run Command, see [Monitoring Systems Manager status changes using
Amazon SNS notifications](monitoring-sns-notifications.md "monitoring-sns-notifications.md"). 12. Choose **Run**.
For information about canceling a command, see [Canceling a command](cancel-run-command.md "cancel-run-command.md").

## Rerunning commands

Systems Manager includes two options to help you rerun a command from the **Run
Command** page in the Systems Manager console.

- **Rerun**: This button allows you to run the same
  command without making changes to it.
- **Copy to new**: This button copies the settings of
  one command to a new command and gives you the option to edit those
  settings before you run it.

###### To rerun a command

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Run Command**.
3. Choose a command to rerun. You can rerun a command immediately after
   executing it from the command details page. Or, you can choose a command
   that you previously ran from the **Command history**
   tab.
4. Choose either **Rerun** to run the same command
   without changes, or choose **Copy to new** to edit the
   command settings before you run it.
