# Install the CodeDeploy agent using

AWS Systems Manager

You can use the AWS Management Console or the AWS CLI to install the CodeDeploy agent to your Amazon EC2 or
on-premises instances by using AWS Systems Manager. You can choose to install a specific version or
choose to always install the latest version of the agent. For more information about
AWS Systems Manager, see [What is AWS Systems Manager](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md").

Using AWS Systems Manager is the recommended method for installing and updating the CodeDeploy agent.
You can also install the CodeDeploy agent from an Amazon S3 bucket. For information about using an
Amazon S3 download link, see [Install the CodeDeploy agent using the
command line](codedeploy-agent-operations-install-cli.md "codedeploy-agent-operations-install-cli.md").

###### Topics

- [Prerequisites](#install-codedeploy-agent-prereqs "#install-codedeploy-agent-prereqs")
- [Install the CodeDeploy
  agent](#download-codedeploy-agent-on-EC2-Instance "#download-codedeploy-agent-on-EC2-Instance")

## Prerequisites

Follow the steps in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md") to set up IAM permissions and the
AWS CLI.

If installing the CodeDeploy agent on an on-premises server with Systems Manager, you must register
your on-premises server with Amazon EC2 Systems Manager. For more information, see [Setting up Systems Manager in hybrid
environments](../../../systems-manager/latest/userguide/systems-manager-managedinstances.md "../../../systems-manager/latest/userguide/systems-manager-managedinstances.md") in the _AWS Systems Manager User Guide_.

## Install the CodeDeploy

agent

Before you can use Systems Manager to install the CodeDeploy agent, you must make sure that the
instance is configured correctly for Systems Manager.

### Installing or updating the

SSM agent

On an Amazon EC2 instance, the CodeDeploy agent requires that the instance is running version
2.3.274.0 or later. Before you install the CodeDeploy agent, update or install SSM agent on
the instance if you haven't already done so.

The SSM agent comes preinstalled on some Amazon EC2 AMIs provided by AWS. For more
information, see [Amazon Machine
Images (AMIs) with SSM agent preinstalled](../../../systems-manager/latest/userguide/ami-preinstalled-agent.md "../../../systems-manager/latest/userguide/ami-preinstalled-agent.md").

###### Note

Make sure that the instance's operating system is also supported by the CodeDeploy
agent. For more information, see [Operating systems
supported by the CodeDeploy agent](codedeploy-agent.md#codedeploy-agent-supported-operating-systems "codedeploy-agent.md#codedeploy-agent-supported-operating-systems").

For information about installing or updating SSM agent on an instance running Linux,
see [Installing and configuring
the SSM agent on Linux instances](../../../systems-manager/latest/userguide/sysman-install-ssm-agent.md "../../../systems-manager/latest/userguide/sysman-install-ssm-agent.md") in the
_AWS Systems Manager User Guide_.

For information about installing or updating SSM agent on an instance running Windows
Server, see [Installing and
configuring SSM agent on Windows instances](../../../systems-manager/latest/userguide/sysman-install-ssm-win.md "../../../systems-manager/latest/userguide/sysman-install-ssm-win.md") in the
_AWS Systems Manager User Guide_.

### (Optional) Verify Systems Manager

prerequisites

Before you use Systems Manager Run Command to install the CodeDeploy agent, verify that your instances
meet the minimum Systems Manager requirements. For more information, see [Setting up AWS Systems Manager](../../../systems-manager/latest/userguide/systems-manager-setting-up.md "../../../systems-manager/latest/userguide/systems-manager-setting-up.md") in
the _AWS Systems Manager User Guide_.

### Install the CodeDeploy agent

With SSM, you can install the CodeDeploy once or set up a schedule to install new
versions.

To install the CodeDeploy agent, choose the `AWSCodeDeployAgent` package
while you follow the steps in [Install or update packages with AWS Systems Manager distributor](../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md "../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md").
