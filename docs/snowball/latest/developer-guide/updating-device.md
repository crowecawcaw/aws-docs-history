AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Updating software on Snowball Edge devices

AWS will notify you when new software is available for Snowball Edge you have. The notification is provided through email, AWS Health Dashboard, and as a CloudWatch event. The email notification is sent from Amazon Web Services, Inc. to the email address attached to the AWS account used to order the Snowball Edge device. When you receive the notification, follow the instructions in this topic and download and install the update as soon as possible to avoid
interruption of your use of the device. For more information about AWS Health Dashboard, see [AWS Health User Guide](../../../health/latest/ug.md "../../../health/latest/ug.md"). For more information about CloudWatch Events, see [Amazon CloudWatch Events User Guide](../../../AmazonCloudWatch/latest/events.md "../../../AmazonCloudWatch/latest/events.md").

You can download software updates from AWS and install them on Snowball Edge devices
in your on-premises environments. These updates happen in the background. You can continue
to use your devices as normal while the latest software is downloaded securely from AWS to
your device. However, to apply downloaded updates, you must stop workloads on the device and restart it.

Software updates provided by AWS for Snowball Edge/Snowball Edge devices (Appliances) are Appliance Software as per Section 9 of the Service Terms.

The software updates are provided solely for the purpose of installing the software updates on the applicable Appliance on behalf of AWS. You will not (or attempt to), and will not permit or authorize third parties to (or attempt to) (i) make any copies of the software updates other than those necessary to install the software updates on the applicable Appliance, or (ii) circumvent or disable any features or measures in the software updates, including, but not limited to, any encryption applied to the software update. Once the software updates have been installed on the applicable Appliance, you agree to delete the software updates from any and all media utilized in installing the software updates to the Appliance.

###### Warning

We highly recommend that you suspend all activity on your device before installing the update. Updating the device and restarting will stop running instances and interrupt any writes to local Amazon S3
buckets.

###### Topics

- [Prerequisites for updating software on Snowball Edge devices](#prereq-updating-device "#prereq-updating-device")
- [Downloading updates to Snowball Edge devices](download-updates.md "download-updates.md")
- [Installing updates to Snowball Edge devices](install-updates.md "install-updates.md")
- [Updating the SSL certificate on Snowball Edge devices](update-ssl-cert.md "update-ssl-cert.md")
- [Updating your Amazon Linux 2 AMIs on Snowball Edge](update-ami.md "update-ami.md")

## Prerequisites for updating software on Snowball Edge devices

Before you can update your device, the following prerequisites must be met:

- You've created your job, have the device on-premises, and you've unlocked it.
  For more information, see [Getting started with Snowball Edge](getting-started.md "getting-started.md").
- Updating Snowball Edge devices is done through the Snowball Edge client. The latest version of the
  Snowball Edge client must be downloaded and installed on a computer in your
  local environment that has a network connection to the device you want to
  update. For more information, see [Using the Snowball Edge Client](using-client.md "using-client.md").
- (Optional) We recommend that you configure a profile for the Snowball Edge
  client. For more information, see [Configuring a Profile for the Snowball Edge Client](using-client-commands.md#client-configuration "using-client-commands.md#client-configuration").
- For Amazon S3 compatible storage on Snowball Edge on clustered Snowball Edge devices, stop the S3-Snow service and disable auto-start for it. See [Configuring Amazon S3 compatible storage on Snowball Edge to autostart using AWS OpsHub](s3-edge-snow-opshub.md#autostart-s3compatible "s3-edge-snow-opshub.md#autostart-s3compatible").

###### Note

For clustered devices, all commands have to be run for each device.

After you complete these tasks, you can download and install updates for Snowball Edge devices.
