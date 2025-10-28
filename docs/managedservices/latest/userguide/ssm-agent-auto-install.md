# SSM Agent automatic installation

###### Important

SSM Agent automatic installation doesn’t support the Asia Pacific (Malaysia) Region.

To have AMS manage your Amazon Elastic Compute Cloud (Amazon EC2) instances, you must install AWS Systems Manager SSM Agent on each instance. If your instances don't have SSM Agent installed, then you can use the AMS SSM Agent auto-installation feature.

###### Note

- This feature is only available for EC2 instances that aren't in an Auto Scaling group and that run Linux operating systems supported by AMS.
- The AMS SSM Agent auto-installation feature is disabled by default. To enable it, reach out to your CA or CSDM.

## Prerequisites for SSM Agent use

- Make sure the instance profile associated with the target instances has one of the following policies (or equivalent permissions as allowlisted in them):
  - AmazonSSMManagedEC2InstanceDefaultPolicy
  - AmazonSSMManagedInstanceCore

- Make sure that there isn't a Service Control Policy at the AWS Organizations level that explicitly denies the permissions listed in the preceding policies.

For more information, see [Configure instance permissions required for Systems Manager](../../../systems-manager/latest/userguide/setup-instance-permissions.md "../../../systems-manager/latest/userguide/setup-instance-permissions.md").

- To block outbound traffic, ensure that the following interface endpoints are enabled on the VPC where the target instances reside, (replace "region" in the URL appropriately):

      + ssm.<region>.amazonaws.com
      + ssmmessages.<region>.amazonaws.com
      + ec2messages.<region>.amazonaws.com

  For more information, see [Improve the security of EC2 instances by using VPC endpoints for Systems Manager](../../../systems-manager/latest/userguide/setup-create-vpc.md "../../../systems-manager/latest/userguide/setup-create-vpc.md").

For general tips on enabling or troubleshooting managed node availability, see [Solution 2: Verify that an IAM instance profile has been specified for the instance (EC2 instances only)](../../../systems-manager/latest/userguide/troubleshooting-managed-instances.md#instances-missing-solution-2 "../../../systems-manager/latest/userguide/troubleshooting-managed-instances.md#instances-missing-solution-2").

###### Note

AMS stops and starts each instance as part of the auto-installation process. When an instance is stopped, data stored in instance store volumes and data stored on the RAM is lost. For more information, see [What happens when you stop an instance](../../../AWSEC2/latest/UserGuide/Stop_Start.md#what-happens-stop "../../../AWSEC2/latest/UserGuide/Stop_Start.md#what-happens-stop").

## Request automatic installation of SSM Agent on your instances

If your accounts are onboarded to AMS Accelerate Patch Add-On, then configure a patch maintenance window (MW) for the instances. A working SSM Agent is required to complete the patch process. If SSM Agent is missing on an instance, then AMS tries to automatically install it during the patch maintenance window.

###### Note

AMS stops and starts each instance as part of the auto-installation process. When an instance is stopped, data stored in instance store volumes and data stored on the RAM is lost. For more information, see [What happens when you stop an instance](../../../AWSEC2/latest/UserGuide/Stop_Start.md#what-happens-stop "../../../AWSEC2/latest/UserGuide/Stop_Start.md#what-happens-stop").

## How SSM Agent automatic installation works

AMS uses EC2 user data to run the installation script on your instances. To add the user data script and run it on your instances, AMS must stop and start each instance.

If your instance already has an existing user data script, then AMS completes the following steps during the auto installation process:

1. Creates a backup of the existing user data script.
2. Replaces the existing user data script with the SSM Agent installation script.
3. Restarts the instance to install SSM Agent.
4. Stops the instance and restores the original script.
5. Restarts the instance with the original script.
