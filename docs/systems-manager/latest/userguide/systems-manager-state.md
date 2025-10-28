# AWS Systems Manager State Manager

State Manager, a tool in AWS Systems Manager, is a secure and scalable configuration management service
that automates the process of keeping your managed nodes and other AWS resources in a
state that you define. To get started with State Manager, open the [Systems Manager console](https://console.aws.amazon.com/systems-manager/state-manager "https://console.aws.amazon.com/systems-manager/state-manager"). In the navigation pane,
choose **State Manager**.

###### Note

State Manager and Maintenance Windows can perform some similar types of updates on your managed nodes.
Which one you choose depends on whether you need to automate system compliance or perform
high-priority, time-sensitive tasks during periods you specify.

For more information, see [Choosing between State Manager and
Maintenance Windows](state-manager-vs-maintenance-windows.md "state-manager-vs-maintenance-windows.md").

## How can State Manager benefit my

organization?

By using pre-configured Systems Manager documents (SSM documents), State Manager offers the
following benefits for managing your nodes:

- Bootstrap nodes with specific software at start-up.
- Download and update agents on a defined schedule, including the
  SSM Agent.
- Configure network settings.
- Join nodes to a Microsoft Active Directory domain.
- Run scripts on Linux, macOS, and Windows Server managed nodes throughout their
  lifecycle.

To manage configuration drift across other AWS resources, you can use Automation, a
tool in Systems Manager, with State Manager to perform the following types of tasks:

- Attach a Systems Manager role to Amazon Elastic Compute Cloud (Amazon EC2) instances to make them
  _managed nodes_.
- Enforce desired ingress and egress rules for a security group.
- Create or delete Amazon DynamoDB backups.
- Create or delete Amazon Elastic Block Store (Amazon EBS) snapshots.
- Turn off read and write permissions on Amazon Simple Storage Service (Amazon S3) buckets.
- Start, restart, or stop managed nodes and Amazon Relational Database Service (Amazon RDS) instances.
- Apply patches to Linux, macOS, and Window AMIs.

For information about using State Manager with Automation runbooks, see [Scheduling
automations with State Manager associations](scheduling-automations-state-manager-associations.md "scheduling-automations-state-manager-associations.md").

## Who should use State Manager?

State Manager is appropriate for any AWS customer that wants to improve the management
and governance of their AWS resources and reduce configuration drift.

## What are the features of State Manager?

Key features of State Manager include the following:

- ###### State Manager associations

A State Manager _association_ is a configuration that you
assign to your AWS resources. The configuration defines the state that you
want to maintain on your resources. For example, an association can specify
that antivirus software must be installed and running on a managed node, or
that certain ports must be closed.

An association specifies a schedule for when to apply the configuration and
the targets for the association. For example, an association for antivirus
software might run once a day on all managed nodes in an AWS account. If the
software isn't installed on a node, then the association could instruct State Manager
to install it. If the software is installed, but the service isn't running, then
the association could instruct State Manager to start the service.

- ###### Flexible scheduling options

State Manager offers the following options for scheduling when an association
runs:

    + **Immediate or delayed
     processing**


    When you create an association, by default, the system immediately
     runs it on the specified resources. After the initial run, the
     association runs in intervals according to the schedule that you
     defined.


    You can instruct State Manager not to run an association immediately by
     using the **Apply association only at the next specified Cron
     interval** option in the console or the
     `ApplyOnlyAtCronInterval` parameter from the command
     line.
    + **Cron and rate expressions**


    When you create an association, you specify a schedule for when
     State Manager applies the configuration. State Manager supports most standard cron
     and rate expressions for scheduling when an association runs. State Manager
     also supports cron expressions that include a day of the week and the
     number sign (#) to designate the *n*th day of a month
     to run an association and the (L) sign to indicate the last
     *X* day of the month.


    ###### Note

    State Manager doesn't currently support specifying months in cron
     expressions for associations.


    To further control when an association runs, for example if you want
     to run an association two days after patch Tuesday, you can specify an
     offset. An *offset* defines how many days to wait
     after the scheduled day to run an association.


    For information about building cron and rate expressions, see [Reference: Cron and rate expressions
     for Systems Manager](reference-cron-and-rate-expressions.md "reference-cron-and-rate-expressions.md").

- ###### Multiple targeting options

An association also specifies the targets for the association. State Manager
supports targeting AWS resources by using tags, AWS Resource Groups, individual node
IDs, or all managed nodes in the current AWS Region and
AWS account.

- ###### Amazon S3 support

Store the command output from association runs in an Amazon S3 bucket of your
choice. For more information, see [Working with associations in Systems Manager](state-manager-associations.md "state-manager-associations.md").

- ###### EventBridge support

This Systems Manager tool is supported as both an _event_ type and a
_target_ type in Amazon EventBridge rules. For information, see [Monitoring Systems Manager events with
Amazon EventBridge](monitoring-eventbridge-events.md "monitoring-eventbridge-events.md") and [Reference: Amazon EventBridge event patterns and types
for Systems Manager](reference-eventbridge-events.md "reference-eventbridge-events.md").

## Is there a charge to use State Manager?

State Manager is available at no additional charge.

###### Topics

- [Understanding how State Manager works](state-manager-about.md "state-manager-about.md")
- [Working with associations in Systems Manager](state-manager-associations.md "state-manager-associations.md")
- [Creating associations
  that run MOF files](systems-manager-state-manager-using-mof-file.md "systems-manager-state-manager-using-mof-file.md")
- [Creating associations that run
  Ansible playbooks](systems-manager-state-manager-ansible.md "systems-manager-state-manager-ansible.md")
- [Creating associations that run
  Chef recipes](systems-manager-state-manager-chef.md "systems-manager-state-manager-chef.md")
- [Walkthrough: Automatically update
  SSM Agent with the AWS CLI](state-manager-update-ssm-agent-cli.md "state-manager-update-ssm-agent-cli.md")
- [Walkthrough: Automatically update PV
  drivers on EC2 instances for Windows Server](state-manager-update-pv-drivers.md "state-manager-update-pv-drivers.md")

**More info**

- [Combating Configuration Drift Using Amazon EC2 Systems Manager and Windows
  PowerShell DSC](https://aws.amazon.com/blogs/mt/combating-configuration-drift-using-amazon-ec2-systems-manager-and-windows-powershell-dsc/ "https://aws.amazon.com/blogs/mt/combating-configuration-drift-using-amazon-ec2-systems-manager-and-windows-powershell-dsc/")
- [Configure Amazon EC2 Instances in an Auto Scaling Group Using
  State Manager](https://aws.amazon.com/blogs/mt/configure-amazon-ec2-instances-in-an-auto-scaling-group-using-state-manager/ "https://aws.amazon.com/blogs/mt/configure-amazon-ec2-instances-in-an-auto-scaling-group-using-state-manager/")
