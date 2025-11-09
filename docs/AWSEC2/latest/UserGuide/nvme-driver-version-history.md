# AWS NVMe Windows driver version

history

The following table shows which AWS NVMe drivers run on each version of Windows
Server on Amazon EC2.

| Windows Server version | AWS NVMe driver version   |
| ---------------------- | ------------------------- |
| Windows Server 2025    | latest version            |
| Windows Server 2022    | latest version            |
| Windows Server 2019    | latest version            |
| Windows Server 2016    | latest version            |
| Windows Server 2012 R2 | version 1.5.1 and earlier |
| Windows Server 2012    | version 1.5.1 and earlier |
| Windows Server 2008 R2 | version 1.3.2 and earlier |
| Windows Server 2008    | version 1.3.2 and earlier |

The following table describes the released versions of the AWS NVMe driver.

| Package version                                                                                                                                                        | Driver version | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Release date      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [1.7.0](https://s3.amazonaws.com/ec2-windows-drivers-downloads/NVMe/1.7.0/AWSNVMe.zip "https://s3.amazonaws.com/ec2-windows-drivers-downloads/NVMe/1.7.0/AWSNVMe.zip") | 1.7.0          | • Added support for NVMe Get Log Page Command.<br>• Added support for detailed performance statistics for EBS and EC2 instance<br>store volumes.<br>• Bug fixes for the Identify Namespace command.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 17 September 2025 |
| [1.6.0](https://s3.amazonaws.com/ec2-windows-drivers-downloads/NVMe/1.6.0/AWSNVMe.zip "https://s3.amazonaws.com/ec2-windows-drivers-downloads/NVMe/1.6.0/AWSNVMe.zip") | 1.6.0          | • Updated the install script to use PnPUtil.<br>• Updated ebsnvme-id.exe to use NVMe IOCTL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 25 October 2024   |
| [1.5.1](https://s3.amazonaws.com/ec2-windows-drivers-downloads/NVMe/1.5.1/AWSNVMe.zip "https://s3.amazonaws.com/ec2-windows-drivers-downloads/NVMe/1.5.1/AWSNVMe.zip") | 1.5.0          | Fixed the install script to create a folder for the<br>`ebsnvme-id` tool if it is not<br>present.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 17 November 2023  |
| 1.5.0                                                                                                                                                                  | 1.5.0          | Added support for Small Computer System Interface (SCSI)<br>persistent reservations for instances running Windows Server 2016<br>and later. The ebsnvme-id tool (`ebsnvme-id.exe`)<br>is now installed by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 31 August 2023    |
| 1.4.2                                                                                                                                                                  | 1.4.2          | Fixed a bug where the AWS NVMe driver did not support instance store<br>volumes on D3 instances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 16 March 2023     |
| 1.4.1                                                                                                                                                                  | 1.4.1          | Reports Namespace Preferred Write Granularity (NPGW) for EBS<br>volumes that support this optional NVMe feature. For more<br>information, see section 8.25, "Improving Performance through I/O<br>Size and Alignment Adherence," in the [NVMe Base Specification, version 1.4](https://nvmexpress.org/wp-content/uploads/NVM-Express-1_4b-2020.09.21-Ratified.pdf "https://nvmexpress.org/wp-content/uploads/NVM-Express-1_4b-2020.09.21-Ratified.pdf").                                                                                                                                                                                                                                                                                                                                                                                                                                              | 20 May 2022       |
| 1.4.0                                                                                                                                                                  | 1.4.0          | • Added support for IOCTLs that allow applications to<br>interact with NVMe devices. This support allows applications<br>to get `IdentifyController`,<br>`IdentifyNamespace`, and<br>`NameSpace` list from the NVMe device. For<br>more information, see [Protocol-specific queries](https://learn.microsoft.com/en-us/windows/win32/fileio/working-with-nvme-devices#protocol-specific-queries "https://learn.microsoft.com/en-us/windows/win32/fileio/working-with-nvme-devices#protocol-specific-queries") in the Microsoft<br>documentation.<br>• The 1.4.0 driver version and the latest<br>`ebsnvme-id` tool<br>(`ebsnvme-id.exe`) are combined in a single<br>package. This combination allows you to install both driver<br>and tool from a single package. For more details, see [AWS NVMe drivers](aws-nvme-drivers.md "aws-nvme-drivers.md").<br>• Bug fixes and reliability improvements. | 23 November 2021  |
| [1.3.2](https://s3.amazonaws.com/ec2-windows-drivers-downloads/NVMe/1.3.2/AWSNVMe.zip "https://s3.amazonaws.com/ec2-windows-drivers-downloads/NVMe/1.3.2/AWSNVMe.zip") | 1.3.2          | Fixed issue with modifying EBS volumes actively processing IO, which<br>may result in data corruption. Customers who do not modify online EBS<br>volumes (for example, resizing or changing type) are not<br>impacted.<br>This is the last version that can run on Windows Server 2008 and 2008 R2.<br>This version is available for download but no longer supported.<br>Windows Server 2008 and 2008 R2 has reached end-of-life, and is no longer supported by Microsoft.                                                                                                                                                                                                                                                                                                                                                                                                                           | 10 September 2019 |
| 1.3.1                                                                                                                                                                  | 1.3.1          | Reliability Improvements.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 21 May 2019       |
| 1.3.0                                                                                                                                                                  | 1.3.0          | Device optimization improvements.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 31 August 2018    |
| 1.2.0                                                                                                                                                                  | 1.2.0          | Performance and reliability improvements for AWS NVMe devices on<br>all supported instances, including bare metal instances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 13 June 2018      |
| >1.0.0                                                                                                                                                                 | >1.0.0         | AWS NVMe driver for supported instance types running Windows<br>Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 12 February 2018  |

## Subscribe to

notifications

Amazon SNS can notify you when new versions of EC2 Windows Drivers are released. Use
the following procedure to subscribe to these notifications.

###### To subscribe to EC2 notifications from the console

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation bar, change the Region to
   **US East (N. Virginia)**, if necessary. You must select
   this Region because the SNS notifications that you are subscribing to are in
   this Region.
3. In the navigation pane, choose **Subscriptions**.
4. Choose **Create subscription**.
5. In the **Create subscription** dialog box, do the
   following:
   1. For **TopicARN**, copy the following Amazon
      Resource Name (ARN):

   arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers 2. For **Protocol**, choose
   `Email`. 3. For **Endpoint**, type an email address that you
   can use to receive the notifications. 4. Choose **Create subscription**.

6. You'll receive a confirmation email. Open the email and follow the
   directions to complete your subscription.

Whenever new EC2 Windows drivers are released, we send notifications to
subscribers. If you no longer want to receive these notifications, use the following
procedure to unsubscribe.

###### To unsubscribe from Amazon EC2 Windows driver notification

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Subscriptions**.
3. Select the checkbox for the subscription and then choose
   **Actions**, **Delete subscriptions**.
   When prompted for confirmation, choose **Delete**.

###### To subscribe to EC2 notifications using the AWS CLI

To subscribe to EC2 notifications with the AWS CLI, use the following command.

```
aws sns subscribe --topic-arn `arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers` --protocol `email` --notification-endpoint `YourUserName@YourDomainName.ext`
```

###### To subscribe to EC2 notifications using AWS Tools for Windows PowerShell

To subscribe to EC2 notifications with AWS Tools for Windows PowerShell, use the following command.

```
Connect-SNSNotification -TopicArn `'arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers'` -Protocol `email` -Region `us-east-1` -Endpoint `'YourUserName@YourDomainName.ext'`
```
