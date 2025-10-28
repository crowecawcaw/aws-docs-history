# Using EC2 Fast Launch with Windows platform branches

The EC2 Fast Launch feature reduces Windows instance launch times in your Elastic Beanstalk environments. The purpose of this topic is to guide you on using this
feature with your Elastic Beanstalk environments. Starting with Windows platform version 2.16.2, released on [January 22, 2025](../relnotes/release-2025-01-22-windows.md "../relnotes/release-2025-01-22-windows.md"), Elastic Beanstalk platform releases include base AMIs with EC2 Fast
Launch enabled.

## Default EC2 Fast Launch availability

The latest Elastic Beanstalk Windows platform versions include base AMIs with EC2 Fast Launch automatically enabled, with no additional costs. However, when newer
platform versions are released, EC2 Fast Launch may not remain automatically enabled on base AMIs from older platform versions.

We recommend upgrading to the latest Windows platform version to use base AMIs with EC2 Fast Launch automatically enabled. However, if you need to
continue using your existing platform version, you can manually enable EC2 Fast Launch on your environment's base AMI. For instructions, see [Manually configuring EC2 Fast Launch](#dotnet-ec2fastlaunch-manual "#dotnet-ec2fastlaunch-manual").

## Manually configuring EC2 Fast Launch

###### Note

Manually enabling EC2 Fast Launch may incur additional costs compared to using platform versions with EC2 Fast Launch automatically enabled. For
more information about EC2 Fast Launch costs, see the [Manage costs for EC2 Fast Launch
underlying resources](../../../AWSEC2/latest/UserGuide/win-fast-launch-manage-costs.md "../../../AWSEC2/latest/UserGuide/win-fast-launch-manage-costs.md") page in the _Amazon EC2 User Guide_.

Follow these steps to enable EC2 Fast Launch on a Windows base AMI used by your Elastic Beanstalk environment:

###### To manually enable EC2 Fast Launch for your Elastic Beanstalk environment

1. Identify your environment's base AMI:

Follow the steps in [Creating a Custom AMI](using-features.md "using-features.md") to identify your environment's base AMI ID. Note that
you don't need to create a custom AMI - you only need to follow the steps to locate your current base AMI ID. 2. Enable EC2 Fast Launch on the AMI:

Use the instructions in [Enable EC2 Fast Launch](../../../AWSEC2/latest/UserGuide/win-fast-launch-configure.md "../../../AWSEC2/latest/UserGuide/win-fast-launch-configure.md") in the
_Amazon EC2 User Guide_ to configure EC2 Fast Launch for your AMI.
