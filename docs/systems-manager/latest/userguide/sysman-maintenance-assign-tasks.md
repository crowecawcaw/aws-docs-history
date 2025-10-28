# Assign tasks to a maintenance

window using the console

In this procedure, you add a task to a maintenance window. Tasks are the actions
performed when a maintenance window runs.

The following four types of tasks can be added to a maintenance window:

- AWS Systems Manager Run Command commands
- Systems Manager Automation workflows
- AWS Step Functions tasks
- AWS Lambda functions

###### Important

The IAM policy for Maintenance Windows requires that you add the prefix `SSM` to
Lambda function (or alias) names. Before you proceed to register this type of task,
update its name in AWS Lambda to include `SSM`. For example, if your Lambda
function name is `MyLambdaFunction`, change it to
`SSMMyLambdaFunction`.

###### To assign tasks to a maintenance window

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Maintenance Windows**.
3. In the list of maintenance windows, choose a maintenance window.
4. Choose **Actions**, and then choose the option for the
   type of task you want to register with the maintenance window.
   - **Register Run command task**
   - **Register Automation task**
   - **Register Lambda task**
   - **Register Step Functions task**

   ###### Note

   Maintenance window tasks support Step Functions Standard state machine
   workflows only. They don't support Express state machine
   workflows. For information about state machine workflow types,
   see [Standard vs. Express Workflows](../../../step-functions/latest/dg/concepts-standard-vs-express.md "../../../step-functions/latest/dg/concepts-standard-vs-express.md") in the
   _AWS Step Functions Developer Guide_.

5. (Optional) For **Name**, enter a name for the
   task.
6. (Optional) For **Description**, enter a
   description.
7. For **New task invocation cutoff**, if you don't want any
   new task invocations to start after the maintenance window cutoff time is
   reached, choose **Enabled**.

When this option is _not_ enabled, the
task continues running when the cutoff time is reached and starts new task
invocations until completion.

###### Note

The status for tasks that are not completed when you enable this
option is `TIMED_OUT`. 8. For this step, choose the tab for your selected task
type.

Run Command

    1. In the **Command document** list,
     choose the Systems Manager Command document (SSM document) that
     defines the tasks to run.
    2. For **Document version**, choose the
     document version to use.
    3. For **Task priority**, specify a
     priority for this task. Zero (`0`) is the
     highest priority. Tasks in a maintenance window are
     scheduled in priority order with tasks that have the
     same priority scheduled in parallel.

Automation

    1. In the **Automation document** list,
     choose the Automation runbook that defines the tasks to
     run.
    2. For **Document version**, choose the
     runbook version to use.
    3. For **Task priority**, specify a
     priority for this task. Zero (`0`) is the
     highest priority. Tasks in a maintenance window are
     scheduled in priority order with tasks that have the
     same priority scheduled in parallel.

Lambda

    1. In the **Lambda parameters** area,
     choose a Lambda function from the list.
    2. (Optional) Provide any content for
     **Payload**, **Client
     Context**, or
     **Qualifier** that you want to
     include.


    ###### Note

    In some cases, you can use a *pseudo parameter* as part
     of your `Payload` value. Then when the
     maintenance window task runs, it passes the correct
     values instead of the pseudo parameter placeholders.
     For information, see [Using pseudo parameters
     when registering maintenance window tasks](maintenance-window-tasks-pseudo-parameters.md "maintenance-window-tasks-pseudo-parameters.md").
    3. For **Task priority**, specify a
     priority for this task. Zero (`0`) is the
     highest priority. Tasks in a maintenance window are
     scheduled in priority order with tasks that have the
     same priority scheduled in parallel.

Step Functions

    1. In the **Step Functions parameters** area,
     choose a state machine from the list.
    2. (Optional) Provide a name for the state machine
     execution and any content for **Input**
     that you want to include.


    ###### Note

    In some cases, you can use a *pseudo parameter* as part
     of your `Input` value. Then when the
     maintenance window task runs, it passes the correct
     values instead of the pseudo parameter placeholders.
     For information, see [Using pseudo parameters
     when registering maintenance window tasks](maintenance-window-tasks-pseudo-parameters.md "maintenance-window-tasks-pseudo-parameters.md").
    3. For **Task priority**, specify a
     priority for this task. Zero (`0`) is the
     highest priority. Tasks in a maintenance window are
     scheduled in priority order with tasks that have the
     same priority scheduled in parallel.

9. In the **Targets** area, choose one of the
   following:
   - **Selecting registered target groups**: Select
     one or more maintenance window targets you have registered with the
     current maintenance window.
   - **Selecting unregistered targets**: Choose
     available resources one by one as targets for the task.

   If a managed node you expect to see isn't listed, see [Troubleshooting managed
   node availability](fleet-manager-troubleshooting-managed-nodes.md "fleet-manager-troubleshooting-managed-nodes.md") for troubleshooting
   tips.
   - **Task target not required**: Targets for the
     task might already be specified in other functions for all but
     Run Command-type tasks.

   Specify one or more targets for maintenance window Run Command-type tasks. Depending on the
   task, targets are optional for other maintenance window task types (Automation, AWS Lambda,
   and AWS Step Functions). For more information about running tasks that don't specify targets,
   see [Registering maintenance window
   tasks without targets](maintenance-windows-targetless-tasks.md "maintenance-windows-targetless-tasks.md").

   ###### Note

   In many cases, you don't need to explicitly specify a target for an automation task.
   For example, say that you're creating an Automation-type task to update an Amazon Machine Image
   (AMI) for Linux using the `AWS-UpdateLinuxAmi` runbook. When the task runs, the
   AMI is updated with the latest available Linux distribution packages and Amazon software.
   New instances created from the AMI already have these updates installed. Because the ID of
   the AMI to be updated is specified in the input parameters for the runbook, there is no
   need to specify a target again in the maintenance window task.

10. _Automation tasks only:_

In the **Input parameters** area, provide values for any
required or optional parameters needed to run your task.

###### Note

In some cases, you can use a _pseudo
parameter_ for certain input parameter values. Then when
the maintenance window task runs, it passes the correct values instead
of the pseudo parameter placeholders. For information, see [Using pseudo parameters
when registering maintenance window tasks](maintenance-window-tasks-pseudo-parameters.md "maintenance-window-tasks-pseudo-parameters.md"). 11. For **Rate control**:

    * For **Concurrency**, specify either a number or a percentage of
     managed nodes on which to run the command at the same time.


    ###### Note

    If you selected targets by specifying tags applied to managed nodes or by
     specifying AWS resource groups, and you aren't certain how many managed
     nodes are targeted, then restrict the number of targets that can run the
     document at the same time by specifying a percentage.
    * For **Error threshold**, specify when to stop running the command
     on other managed nodes after it fails on either a number or a percentage of nodes.
     For example, if you specify three errors, then Systems Manager stops sending the command when
     the fourth error is received. Managed nodes still processing the command might also
     send errors.

12. (Optional) For **IAM service role**, choose a role to
    provide permissions for Systems Manager to assume when running a maintenance window
    task.

If you don't specify a service role ARN, Systems Manager uses a service-linked role
in your account. This role is not listed in the drop-down menu. If no
appropriate service-linked role for Systems Manager exists in your account, it's
created when the task is registered successfully.

###### Note

For an improved security posture, we strongly recommend creating a
custom policy and custom service role for running your maintenance
window tasks. The policy can be crafted to provide only the permissions
needed for your particular maintenance window tasks. For more
information, see [Setting up Maintenance Windows](setting-up-maintenance-windows.md "setting-up-maintenance-windows.md"). 13. _Run Command tasks only:_

(Optional) For **Output options**, do the
following:

    * Select the **Enable writing to S3** check box to
     save the command output to a file. Enter the bucket and prefix
     (folder) names in the boxes.
    * Select the **CloudWatch output** check box to
     write complete output to Amazon CloudWatch Logs. Enter the name of a CloudWatch Logs log
     group.


    ###### Note

    The permissions that grant the ability to write data to an S3
     bucket or CloudWatch Logs are those of the instance profile assigned to
     the node, not those of the IAM user performing this task. For
     more information, see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md"). In
     addition, if the specified S3 bucket or log group is in a
     different AWS account, verify that the instance profile
     associated with the node has the necessary permissions to write
     to that bucket.

14. _Run Command tasks only:_

In the **SNS notifications** section, if you want notifications sent
about the status of the command execution, select the **Enable SNS
notifications** check box.

For more information about configuring Amazon SNS notifications for Run Command, see [Monitoring Systems Manager status changes using
Amazon SNS notifications](monitoring-sns-notifications.md "monitoring-sns-notifications.md"). 15. _Run Command tasks only:_

In the **Parameters** area, specify parameters for the
document.

###### Note

In some cases, you can use a _pseudo
parameter_ for certain input parameter values. Then when
the maintenance window task runs, it passes the correct values instead
of the pseudo parameter placeholders. For information, see [Using pseudo parameters
when registering maintenance window tasks](maintenance-window-tasks-pseudo-parameters.md "maintenance-window-tasks-pseudo-parameters.md"). 16. _Run Command and Automation tasks
only:_

(Optional) In the **CloudWatch alarm** area, for
**Alarm name**, choose an existing CloudWatch alarm to apply
to your task for monitoring.

If the alarm activates, the task is stopped.

###### Note

To attach a CloudWatch alarm to your task, the IAM principal that runs the
task must have permission for the
`iam:createServiceLinkedRole` action. For more
information about CloudWatch alarms, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md"). 17. Depending on your task type, choose one of the following:

    * **Register Run command task**
    * **Register Automation task**
    * **Register Lambda task**
    * **Register Step Functions task**
