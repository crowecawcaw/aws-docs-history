Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Updating the SSL certificate on Snowball Edge devices

If you plan to keep your Snowball Edge for more than 360 days, you will need to
update the Secure Sockets Layer (SSL) certificate on the device to avoid interruption of
your use of the device. If the certificate expires, you will not be able to use the
device and will have to return it to AWS.

AWS will notify you 30 days before the SSL certificate expires for Snowball Edge you have. The notification is provided through email, AWS Health Dashboard, and as a AWS CloudTrail event. The email notification is sent from Amazon Web Services, Inc. to the email address attached to the AWS account used to order the Snowball Edge device. When you receive the notification, follow the instructions in this topic and request an update as soon as possible to avoid
interruption of your use of the device. For more information about AWS Health Dashboard, see [AWS Health User Guide](../../../health/latest/ug.md "../../../health/latest/ug.md"). For more information about CloudWatch Events, see [Working with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

Updating the SSL certificate is done through the Snowball Edge client. The latest version of the
Snowball Edge client must be downloaded and installed on a computer in your
local environment that has a network connection to the device you want to
update. For more information, see [Using the Snowball Edge Client](using-client.md "using-client.md").

This topic explains how to determine when the certificate will expire and how to update your device.

1. Use the `snowballEdge describe-device-software` command to determine when the certificate will expire. In the output of the command, the value of `CertificateExpiry` includes the date and time at which the certificate will expire.

###### Example of `describe-device-software` output

```

Installed version: 101
Installing version: 102
Install State: Downloading
CertificateExpiry : Thur Jan 01 00:00:00 UTC 1970

```

2. Contact Support and request an SSL certificate update.
3. Support will provide an update file. [Download](download-updates.md "download-updates.md") and [install](install-updates.md "install-updates.md") the update file.
4. Use the new unlock code and manifest file when [Unlocking the Snowball Edge](unlockdevice.md "unlockdevice.md").
