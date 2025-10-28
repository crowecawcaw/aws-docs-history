# Registering maintenance window

tasks without targets

For each maintenance window you create, you can specify one or more tasks to perform
when the maintenance window runs. In most cases, you must specify the resources, or
targets, that the task is to run on. In some cases, however, you don't need to specify
targets explicitly in the task.

One or more targets must be specified for maintenance window Systems Manager Run Command-type
tasks. Depending on the nature of the task, targets are optional for other maintenance
window task types (Systems Manager Automation, AWS Lambda, and AWS Step Functions).

For Lambda and Step Functions task types, whether a target is required depends on the content of
the function or state machine you have created.

###### Note

When a task has registered targets, Automation, AWS Lambda, and AWS Step Functions tasks
resolve the targets from resource groups and tags and send one invocation per
resolved resource, which results in multiple task invocations. But say, for example,
that you want only one invocation for a Lambda task that's registered with a resource
group containing more than one instance. In this case, if you are working in the
AWS Management Console, choose the option **Task target not required** in the
**Register Lambda task** or **Edit Lambda task**
page. If you are using the AWS CLI command, do not specify targets using the
`--targets` parameter when running the
[register-task-with-maintenance-window](../../../cli/latest/reference/ssm/register-task-with-maintenance-window.md "../../../cli/latest/reference/ssm/register-task-with-maintenance-window.md") command or
[update-maintenance-window-task](../../../cli/latest/reference/ssm/update-maintenance-window-task.md "../../../cli/latest/reference/ssm/update-maintenance-window-task.md") command.

In many cases, you don't need to explicitly specify a target for an automation task.
For example, say that you're creating an Automation-type task to update an Amazon Machine Image
(AMI) for Linux using the `AWS-UpdateLinuxAmi` runbook. When the task runs, the
AMI is updated with the latest available Linux distribution packages and Amazon software.
New instances created from the AMI already have these updates installed. Because the ID of
the AMI to be updated is specified in the input parameters for the runbook, there is no
need to specify a target again in the maintenance window task.

Similarly, suppose you're using the AWS Command Line Interface (AWS CLI) to register a maintenance window
Automation task that uses the `AWS-RestartEC2Instance` runbook. Because the
node to restart is specified in the `--task-invocation-parameters` argument,
you don't need to also specify a `--targets` option.

###### Note

For maintenance window tasks without a target specified, you can't supply values for
`--max-errors` and `--max-concurrency`. Instead, the system
inserts a placeholder value of `1`, which might be reported in the response to
commands such as [describe-maintenance-window-tasks](../../../cli/latest/reference/ssm/describe-maintenance-window-tasks.md "../../../cli/latest/reference/ssm/describe-maintenance-window-tasks.md") and
[get-maintenance-window-task](../../../cli/latest/reference/ssm/get-maintenance-window-task.md "../../../cli/latest/reference/ssm/get-maintenance-window-task.md"). These values don't affect the running of
your task and can be ignored.

The following example demonstrates omitting the `--targets`,
`--max-errors`, and `--max-concurrency` options for a
targetless maintenance window task.

Linux & macOS

```
aws ssm register-task-with-maintenance-window \
    --window-id "mw-ab12cd34eEXAMPLE" \
    --service-role-arn "arn:aws:iam::123456789012:role/MaintenanceWindowAndAutomationRole" \
    --task-type "AUTOMATION" \
    --name "RestartInstanceWithoutTarget" \
    --task-arn "AWS-RestartEC2Instance" \
    --task-invocation-parameters "{\"Automation\":{\"Parameters\":{\"InstanceId\":[\"i-02573cafcfEXAMPLE\"]}}}" \
    --priority 10
```

Windows

```
aws ssm register-task-with-maintenance-window ^
    --window-id "mw-ab12cd34eEXAMPLE" ^
    --service-role-arn "arn:aws:iam::123456789012:role/MaintenanceWindowAndAutomationRole" ^
    --task-type "AUTOMATION" ^
    --name "RestartInstanceWithoutTarget" ^
    --task-arn "AWS-RestartEC2Instance" ^
    --task-invocation-parameters "{\"Automation\":{\"Parameters\":{\"InstanceId\":[\"i-02573cafcfEXAMPLE\"]}}}" ^
    --priority 10
```

###### Note

For maintenance window tasks registered before December 23, 2020: If you specified
targets for the task and one is no longer required, you can update that task to
remove the targets using the Systems Manager console or the
[update-maintenance-window-task](../../../cli/latest/reference/ssm/update-maintenance-window-task.md "../../../cli/latest/reference/ssm/update-maintenance-window-task.md") AWS CLI command.

**More info**

- [Error messages:
  "Maintenance window tasks without targets don't support MaxConcurrency values"
  and "Maintenance window tasks without targets don't support MaxErrors
  values"](troubleshooting-maintenance-windows.md#maxconcurrency-maxerrors-not-supported "troubleshooting-maintenance-windows.md#maxconcurrency-maxerrors-not-supported")
