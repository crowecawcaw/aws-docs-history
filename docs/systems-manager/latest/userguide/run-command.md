AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# AWS Systems Manager Run Command

Using Run Command, a tool in AWS Systems Manager, you can remotely and securely manage the
configuration of your managed nodes. A _managed node_ is any Amazon Elastic Compute Cloud
(Amazon EC2) instance or non-EC2 machine in your [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment that has been configured
for Systems Manager. Run Command allows you to automate common administrative tasks and perform one-time
configuration changes at scale. You can use Run Command from the AWS Management Console, the AWS Command Line Interface
(AWS CLI), AWS Tools for Windows PowerShell, or the AWS SDKs. Run Command is offered at no additional cost. To get
started with Run Command, open the [Systems Manager console](https://console.aws.amazon.com//systems-manager/run-command "https://console.aws.amazon.com//systems-manager/run-command"). In the navigation pane, choose
**Run Command**.

Administrators use Run Command to install or bootstrap applications, build a deployment
pipeline, capture log files when an instance is removed from an Amazon EC2 Auto Scaling group, join instances
to a Windows domain, and more.

The Run Command API follows an eventual consistency model, due to the distributed nature of
the system supporting the API. This means that the result of an API command you run that
affects your resources might not be immediately visible to all subsequent commands you run.
You should keep this in mind when you carry out an API command that immediately follows a
previous API command.

###### Getting Started

The following table includes information to help you get started with Run Command.

| Topic                                                                                                                                                       | Details                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Setting up managed nodes for<br>AWS Systems Manager](systems-manager-setting-up-nodes.md "systems-manager-setting-up-nodes.md")                            | Verify that you have completed the setup requirements for your<br>Amazon Elastic Compute Cloud (Amazon EC2) instances and non-EC2 machines in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types")<br>environment. |
| [Managing nodes in hybrid and multicloud<br>environments with Systems Manager](systems-manager-hybrid-multicloud.md "systems-manager-hybrid-multicloud.md") | (Optional) Register on-premises servers and VMs with AWS so you can<br>manage them using Run Command.                                                                                                                                                                                                                    |
| [Managing edge devices with<br>Systems Manager](systems-manager-setting-up-edge-devices.md "systems-manager-setting-up-edge-devices.md")                    | (Optional) Configure edge devices so you can manage them using<br>Run Command.                                                                                                                                                                                                                                           |
| [Running commands on managed nodes](running-commands.md "running-commands.md")                                                                              | Learn how to run a command that targets one or more managed nodes by<br>using the AWS Management Console.                                                                                                                                                                                                                |
| [Run Command walkthroughs](run-command-walkthroughs.md "run-command-walkthroughs.md")                                                                       | Learn how to run commands using either Tools for Windows PowerShell or the AWS CLI.                                                                                                                                                                                                                                      |

###### EventBridge support

This Systems Manager tool is supported as both an _event_ type and a
_target_ type in Amazon EventBridge rules. For information, see [Monitoring Systems Manager events with
Amazon EventBridge](monitoring-eventbridge-events.md "monitoring-eventbridge-events.md") and [Reference: Amazon EventBridge event patterns and types
for Systems Manager](reference-eventbridge-events.md "reference-eventbridge-events.md").

**More info**

- [Remotely Run Command on an EC2 Instance (10 minute
  tutorial)](https://aws.amazon.com/getting-started/hands-on/remotely-run-commands-ec2-instance-systems-manager/ "https://aws.amazon.com/getting-started/hands-on/remotely-run-commands-ec2-instance-systems-manager/")
- [Systems Manager service quotas](../../../general/latest/gr/ssm.md#limits_ssm "../../../general/latest/gr/ssm.md#limits_ssm") in the
  _Amazon Web Services General Reference_
- [AWS Systems Manager API Reference](../APIReference.md "../APIReference.md")

###### Topics

- [Setting up Run Command](run-command-setting-up.md "run-command-setting-up.md")
- [Running commands on managed nodes](running-commands.md "running-commands.md")
- [Using exit codes in commands](run-command-handle-exit-status.md "run-command-handle-exit-status.md")
- [Understanding command statuses](monitor-commands.md "monitor-commands.md")
- [Run Command walkthroughs](run-command-walkthroughs.md "run-command-walkthroughs.md")
- [Troubleshooting Systems Manager Run
  Command](troubleshooting-remote-commands.md "troubleshooting-remote-commands.md")
