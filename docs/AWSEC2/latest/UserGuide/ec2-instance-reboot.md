# Reboot your Amazon EC2 instance

An instance reboot is equivalent to an operating system reboot. In most cases, it takes only
a few minutes to reboot your instance.

When you reboot an instance, it keeps the following:

- Public DNS name (IPv4)
- Private IPv4 address
- Public IPv4 address
- IPv6 address (if applicable)
- Any data on its instance store volumes
  Rebooting an instance doesn't start a new instance billing period, unlike [stopping and starting](Stop_Start.md "Stop_Start.md") an instance (which starts a new billing
  period with a one-minute minimum charge).

An instance reboot can be user-initiated (where you manually reboot the instance) or
initiated by AWS (for automatic instance recovery, or in response to a scheduled reboot event
for necessary maintenance, such as to apply updates that require a reboot).

For user-initiated reboots, we recommend using the Amazon EC2 console, CLI, or API instead of
running the operating system reboot command from your instance. When using Amazon EC2, if the
instance does not cleanly shut down within a few minutes, Amazon EC2 performs a hard reboot.
Furthermore, AWS CloudTrail creates an API record of when your instance was rebooted.

This topic describes how to perform a user-initiated reboot. For information about reboots
performed by AWS, see [Automatic instance recovery](ec2-instance-recover.md "ec2-instance-recover.md") and [Manage Amazon EC2 instances scheduled for
reboot](schedevents_actions_reboot.md "schedevents_actions_reboot.md").

###### Important

If updates are installing on your instance, we recommend that you do not reboot or shut
down your instance using the Amazon EC2 console or the command line until all the updates are
installed. When you use the Amazon EC2 console or the command line to reboot or shut down your
instance, there is a risk that your instance will be hard rebooted. A hard reboot while
updates are being installed could throw your instance into an unstable state.

Console

###### To reboot an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance and choose **Instance state**,
   **Reboot instance**.
4. Choose **Reboot** when prompted for confirmation.

The instance remains in the `running` state.

AWS CLI

###### To reboot an instance

Use the [reboot-instances](../../../cli/latest/reference/ec2/reboot-instances.md "../../../cli/latest/reference/ec2/reboot-instances.md") command.

```
aws ec2 reboot-instances --instance-ids `i-1234567890abcdef0`
```

PowerShell

###### To reboot an instance

Use the [Restart-EC2Instance](../../../powershell/latest/reference/items/Restart-EC2Instance.md "../../../powershell/latest/reference/items/Restart-EC2Instance.md") cmdlet.

```
Restart-EC2Instance -InstanceId `i-1234567890abcdef0`
```

###### To run a controlled fault injection experiment

You can use AWS Fault Injection Service to test how your application responds when your instance is rebooted. For more
information, see the [AWS Fault Injection Service User Guide](../../../fis/latest/userguide/what-is.md "../../../fis/latest/userguide/what-is.md").
