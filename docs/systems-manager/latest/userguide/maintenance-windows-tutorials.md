# Tutorials

The tutorials in this section show you how to perform common tasks when working with
maintenance windows.

###### Complete prerequisites

Before trying these tutorials, complete the following prerequisites.

- **Configure the AWS CLI on your local machine**
  – Before you can run AWS CLI commands, you must install and configure the
  CLI on your local machine. For information, see [Installing or
  updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and [Installing the
  AWS Tools for PowerShell](../../../powershell/latest/userguide/pstools-getting-set-up.md "../../../powershell/latest/userguide/pstools-getting-set-up.md").
- **Verify maintenance window roles and
  permissions** – An AWS administrator in your account must
  grant you the AWS Identity and Access Management (IAM) permissions you need to manage maintenance
  windows using the CLI. For information, see [Setting up Maintenance Windows](setting-up-maintenance-windows.md "setting-up-maintenance-windows.md").
- **Create or configure an instance that is compatible with
  Systems Manager** – You need at least one Amazon Elastic Compute Cloud (Amazon EC2) instance
  that is configured for use with Systems Manager to complete the tutorials. This means that
  SSM Agent is installed on the instance, and an IAM instance profile for Systems Manager
  is attached to the instance.

We recommend launching an instance from one AWS managed Amazon Machine Image (AMI)
with the agent preinstalled. For more information, see [Find AMIs with the SSM Agent
preinstalled](ami-preinstalled-agent.md "ami-preinstalled-agent.md").

For information about installing SSM Agent on an instance, see the following
topics:

    + [Manually installing and
     uninstalling SSM Agent on EC2 instances for Windows Server](manually-install-ssm-agent-windows.md "manually-install-ssm-agent-windows.md")
    + [Manually installing and
     uninstalling SSM Agent on EC2 instances for Linux](manually-install-ssm-agent-linux.md "manually-install-ssm-agent-linux.md")

For information about configuring IAM permissions for Systems Manager to your
instance, see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md").

- **Create additional resources as needed**
  – Run Command, a tool in Systems Manager, includes many tasks that don't require you
  to create resources other than those listed in this prerequisites topic. For
  that reason, we provide a simple Run Command task for you to use your first time
  through the tutorials. You also need an EC2 instance that is configured to use
  with Systems Manager, as described earlier in this topic. After you configure that
  instance, you can register a simple Run Command task.

The Systems Manager Maintenance Windows tool supports running the following four types of tasks:

    + Run Command commands
    + Systems Manager Automation workflows
    + AWS Lambda functions
    + AWS Step Functions tasks

In general, if a maintenance window task that you want to run requires
additional resources, you should create them first. For example, if you want a
maintenance window that runs an AWS Lambda function, create the Lambda function
before you begin; for a Run Command task, create the S3 bucket that you can save
command output to (if you plan to do so); and so on.

###### Tutorials

- [Tutorials: Create and manage
  maintenance windows using the AWS CLI](maintenance-window-tutorial-cli.md "maintenance-window-tutorial-cli.md")
- [Tutorial: Create a
  maintenance window for patching using the console](maintenance-window-tutorial-patching.md "maintenance-window-tutorial-patching.md")
