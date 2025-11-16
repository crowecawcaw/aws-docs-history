AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Using AWS OpsHub to Manage Devices

The Snowball Edge now offer a user-friendly tool, AWS OpsHub, that you can use to
manage your devices and local AWS services. You use AWS OpsHub on a client
computer to perform tasks such as unlocking and configuring single or clustered devices,
transferring files, and launching and managing instances running on Snowball Edge. You can
use AWS OpsHub to manage both the Storage Optimized and Compute Optimized Snow device types.
The AWS OpsHub application is available at no additional cost to you.

AWS OpsHub takes all the existing operations available in the Snowball API and
presents them as a graphical user interface. This interface helps you quickly migrate data
to the AWS Cloud and deploy edge computing applications on Snowball Edge.

AWS OpsHub provides a unified view of the AWS services that are running on
Snowball Edge and automates operational tasks through AWS Systems Manager. With AWS OpsHub, users with
different levels of technical expertise can manage a large number of Snowball Edge. With a
few clicks, you can unlock devices, transfer files, manage Amazon EC2-compatible instances, and monitor
device metrics.

When your Snow device arrives at your site, you download, install, and launch the
AWS OpsHub application on a client machine, such as a laptop. After installation, you can
unlock the device and start managing it and using supported AWS services
locally. AWS OpsHub provides a dashboard that summarizes key metrics such as storage capacity
and active instances on your device. It also provides a selection of AWS
services that are supported on the Snowball Edge. Within minutes, you can begin transferring
files to the device.

This video provides an overview of AWS OpsHub functionality.

###### Topics

- [Downloading AWS OpsHub for Snowball Edge](download-OpsHub-for-snow-family.md "download-OpsHub-for-snow-family.md")
- [Unlocking a Snowball Edge device with AWS OpsHub](connect-unlock-device.md "connect-unlock-device.md")
- [Verifying the PGP signature of AWS OpsHub
  (optional)](verify-signature.md "verify-signature.md")
- [Managing AWS services on the Snowball Edge with AWS OpsHub](manage-services.md "manage-services.md")
- [Rebooting the device with AWS OpsHub](reboot-device.md "reboot-device.md")
- [Managing profiles with AWS OpsHub](#manage-profile "#manage-profile")
- [Shutting down the device with AWS OpsHub](shutdown-device.md "shutdown-device.md")
- [Editing the device alias with AWS OpsHub](edit-device-alias.md "edit-device-alias.md")
- [Managing public key certificates using OpsHub](snowball-edge-certificates-opshub.md "snowball-edge-certificates-opshub.md")
- [Getting updates for the Snowball Edge](get-updates.md "get-updates.md")
- [Updating the AWS OpsHub application](update-opshub.md "update-opshub.md")
- [Automating your management tasks with AWS OpsHub](automate-task.md "automate-task.md")
- [Setting the NTP time servers for the device with AWS OpsHub](setting-ntp.md "setting-ntp.md")

## Managing profiles with AWS OpsHub

You can create a _profile_ for persistent storage of your
credentials on your local file system. Using AWS OpsHub, you have the option to create
a new profile any time you unlock the device using the device IP address, unlock
code, and manifest file.

You can also use the Snowball Edge Client to create a profile at any time. See
[Configuring a profile for the Snowball Edge Client](using-client-commands.md#client-configuration "using-client-commands.md#client-configuration").

###### To create a profile

1. Unlock your device locally and sign in according to the instructions in
   [Unlocking a Snowball Edge device with AWS OpsHub](connect-unlock-device.md "connect-unlock-device.md").
2. Name the profile and choose **Save profile name**.
