AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Autostarting EC2-compatible instances with launch

templates on a Snowball Edge

You can automatically start your Amazon EC2-compatible instances on your AWS Snowball Edge device using launch
templates and Snowball Edge client launch configuration commands.

A _launch template_ contains the configuration
information necessary to create an Amazon EC2-compatible instance on your Snowball Edge. You can use a
launch template to store launch parameters so you don't have to specify them every
time that you start an EC2-compatible instance on your Snowball Edge.

When you use autostart configurations on your Snowball Edge, you configure the
parameters that you want your Amazon EC2-compatible instance to start with. After your Snowball Edge
is configured, when you reboot and unlock it, it uses your autostart configuration to
launch an instance with the parameters that you specified. If an instance that you
launched using an autostart configuration is stopped, the instance starts running when
you unlock your device.

###### Note

After you first configure an autostart configuration, restart your device to
launch it. All subsequent instance launches (after planned or unplanned reboots)
happen automatically after your device is unlocked.

A launch template can specify the Amazon Machine Image (AMI) ID, instance type, user
data, security groups, and tags for an Amazon EC2-compatible instance when you launch that instance. For
a list of supported instance types, see [Quotas for compute instances on a Snowball Edge device](ec2-edge-limits.md "ec2-edge-limits.md").

To automatically launch EC2-compatible instances on your Snowball Edge, take the following
steps:

1. When you order your AWS Snowball Edge device, create a job to order a Snowball Edge device with compute instances. For
   more information, see [Creating a job to order a Snowball Edge](create-job-common.md "create-job-common.md").
2. After receiving your Snowball Edge, unlock it.
3. Use the EC2-compatible API command `aws ec2 create-launch-template` to create
   a launch template.
4. Use the Snowball Edge client command `snowballEdge
create-autostart-configuration` to bind your EC2-compatible instance launch template to
   your network configuration. For more information, see [Creating an EC2-compatible launch configuration on a Snowball Edge](using-ec2-edge-client.md#ec2-edge-create-autostart-config "using-ec2-edge-client.md#ec2-edge-create-autostart-config").
5. Reboot, then unlock your device. Your EC2-compatible instances are automatically
   started using the attributes specified in your launch template and your
   Snowball Edge client command
   `create-autostart-configuration`.
   To view the status of your running instances, use the EC2-compatible API command
   `describe-autostart-configurations`.

###### Note

There is no console or job management API for AWS Snowball Edge support for launch templates. You use EC2-compatible and
Snowball Edge client CLI commands to automatically start EC2-compatible instances on your
AWS Snowball Edge device.
