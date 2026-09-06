

# Paravirtual drivers for Windows instances
<a name="xen-drivers-overview"></a>

Windows AMIs contain a set of drivers to permit access to virtualized hardware. These drivers are used by Amazon EC2 to map instance store and Amazon EBS volumes to their devices. The following table shows key differences between the different drivers.


|  | Red Hat PV | Citrix PV | AWS PV | 
| --- | --- | --- | --- | 
| Instance type | Not supported for all instance types. If you specify an unsupported instance type, the instance is impaired. | Supported for Xen instance types. | Supported for Xen instance types. | 
| Attached volumes | Supports up to 16 attached volumes. | Supports more than 16 attached volumes. | Supports more than 16 attached volumes. | 
| Network | The driver has known issues where the network connection resets under high loads; for example, fast FTP file transfers. |  | The driver automatically configures jumbo frames on the network adapter when on a compatible instance type. When the instance is in a cluster placement group, this offers better network performance between instances that are in the cluster placement group. For more information, see [Placement groups for your Amazon EC2 instances](placement-groups.md). | 

The following table shows which PV drivers you should run on each version of Windows Server on Amazon EC2.


| Windows Server version | PV driver version | 
| --- | --- | 
| Windows Server 2025 | Not supported | 
| Windows Server 2022 | AWS PV latest version | 
| Windows Server 2019 | AWS PV latest version | 
| Windows Server 2016 | AWS PV latest version | 
| Windows Server 2012 R2 | AWS PV version 8.4.3 | 
| Windows Server 2012  | AWS PV version 8.4.3 | 
| Windows Server 2008 R2 | AWS PV version 8.3.5 | 
| Windows Server 2008 | Citrix PV 5.9 | 
| Windows Server 2003 | Citrix PV 5.9 | 

**Topics**
+ [AWS PV drivers](#xen-driver-awspv)
+ [Citrix PV drivers](#xen-driver-citrix)
+ [Red Hat PV drivers](#xen-driver-redhat)
+ [Subscribe to notifications](#drivers-subscribe-notifications)
+ [Upgrade PV drivers on EC2 Windows instances](Upgrading_PV_drivers.md)
+ [Troubleshoot PV drivers on Windows instances](pvdrivers-troubleshooting.md)

## AWS PV drivers
<a name="xen-driver-awspv"></a>

The AWS PV drivers are stored in the `%ProgramFiles%\Amazon\Xentools` directory. This directory also contains public symbols and a command line tool, `xenstore_client.exe`, that enables you to access entries in XenStore. For example, the following PowerShell command returns the current time from the Hypervisor:

```
PS C:\> [DateTime]::FromFileTimeUTC((gwmi -n root\wmi -cl AWSXenStoreBase).XenTime).ToString("hh:mm:ss")
11:17:00
```

The AWS PV driver components are listed in the Windows registry under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services`. These driver components are as follows: xenbus, xeniface, xennet, xenvbd, and xenvif.

AWS PV drivers also have a Windows service named LiteAgent, which runs in user-mode. It handles tasks such as shutdown and restart events from AWS APIs on Xen generation instances. You can access and manage services by running `Services.msc` from the command line. When running on Nitro generation instances, the AWS PV drivers are not used and the LiteAgent service will self-stop starting with driver version 8.2.4. Updating to the latest AWS PV driver also updates the LiteAgent and improves reliability on all instance generations.

### Install the latest AWS PV drivers
<a name="aws-pv-download"></a>

Amazon Windows AMIs contain a set of drivers to permit access to virtualized hardware. These drivers are used by Amazon EC2 to map instance store and Amazon EBS volumes to their devices. We recommend that you install the latest drivers to improve stability and performance of your EC2 Windows instances.

**Installation options**
+ Use AWS Systems Manager to automatically update the PV drivers. For more information, see [Walkthrough: Automatically Update PV Drivers on EC2 Windows Instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-update-pv-drivers.html) in the *AWS Systems Manager User Guide*.
+  [Download](https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSPV/Latest/AWSPVDriver.zip) the driver package and run the install program manually. For information about downloading and installing the AWS PV drivers, or upgrading a domain controller, see [Upgrade Windows Server instances (AWS PV upgrade) manually](Upgrading_PV_drivers.md#aws-pv-upgrade).

For system requirements for installing the AWS PV driver package, see [System requirements for the AWS PV driver package](Upgrading_PV_drivers.md#aws-pv-requirements).

### AWS PV driver package history
<a name="pv-driver-history"></a>

The following table shows the changes to AWS PV drivers for each driver release.


| Package version | Details | Release date | 
| --- | --- | --- | 
|  [8.6.1](https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSPV/8.6.1/AWSPVDriver.zip)  |  +  Updated runtime dependencies in the installer package.   | July 21, 2026 | 
| 8.6.0 |  +  Stability fixes to XenStore interactions.   | May 27, 2025 | 
| 8.5.0 |  +  Stability fixes to address rare cases of crashes during network device detachment. <br />+  Stability fixes to address rare cases of crashes during EBS volume detachment. <br />+  Fixed bugs in the package installer. <br />+  Updated the PV installer to use `Pnputil`.   | October 31, 2024 | 
|  [8.4.3](https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSPV/8.4.3/AWSPVDriver.zip)  | Fixed bugs in the package installer to improve the upgrade experience. This is the last version that can run on Windows Server 2012 and 2012 R2. This version is available for download, however it is no longer supported since Windows Server 2012 and 2012 R2 have reached end of support. | January 24, 2023 | 
| 8.4.2 | Stability fixes to address race condition. | April 13, 2022 | 
| 8.4.1 | Improved package installer. | January 7, 2022 | 
| 8.4.0 |  +  Stability fixes to address rare cases of stuck disk IO.  <br />+  Stability fixes to address rare cases of crashes during EBS volume detachment. <br />+  Added feature to distribute load across multiple cores for workloads that leverage more than 20,000 IOPS and experience degradation due to bottlenecks. To enable this feature, see [Workloads that leverage more than 20,000 disk IOPS experience degradation due to CPU bottlenecks](pvdrivers-troubleshooting.md#pvdriver-troubleshooting-cpu-bottlenecks).   | March 2, 2021 | 
|  [8.3.5](https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSPV/8.3.5/AWSPVDriver.zip)  | Improved package installer.<br />This is the last version that can run on Windows Server 2008 R2. This version is available for download but no longer supported. Windows Server 2008 R2 has reached end-of-life, and is no longer supported by Microsoft. | January 7, 2022 | 
| 8.3.4 | Improved reliability of network device attachment. | August 4, 2020 | 
| 8.3.3 | +  Update to XenStore-facing component to prevent bug check during error-handling paths.  <br />+  Update to storage component to avoid crashes when an invalid SRB is submitted. To update this driver on Windows Server 2008 R2 instances, you must first verify that the appropriate patches are installed to address the following Microsoft Security Advisory: [Microsoft Security Advisory 3033929](https://learn.microsoft.com/en-us/security-updates/SecurityAdvisories/2015/3033929). | February 4, 2020 | 
| 8.3.2 | Enhanced reliability of networking components. | July 30, 2019 | 
| 8.3.1 | Improved performance and robustness of storage component. | June 12, 2019 | 
| 8.2.7 | Improved efficiency to support migrating to latest generation instance types. | May 20, 2019 | 
| 8.2.6 | Improved efficiency of crash dump path. | January 15, 2019 | 
| 8.2.5 | Additional security enhancements.<br />PowerShell installer now available in package. | December 12, 2018 | 
| 8.2.4 | Reliability improvements. | October 2, 2018 | 
| 8.2.3 | Bug fixes and performance improvements.<br />Report EBS volume ID as disk serial number for EBS volumes. This enables cluster scenarios such as S2D. | May 29, 2018 | 
| 8.2.1 | Network and storage performance improvements plus multiple robustness fixes.<br />To verify that this version has been installed, refer to the following Windows registry value: `HKLM\Software\Amazon\PVDriver\Version 8.2.1`. | March 8, 2018 | 
| 7.4.3 | Added support for Windows Server 2016.<br />Stability fixes for all supported Windows OS versions.<br />\*AWS PV driver version 7.4.3's signature expires on March 29, 2019. We recommend updating to the latest AWS PV driver.  | November 18, 2016 | 
| 7.4.2 | Stability fixes for support of X1 instance type. | August 2, 2016 | 
| 7.4.1 |  +  Performance improvement in AWS PV Storage driver. <br />+  Stability fixes in AWS PV Storage driver: Fixed an issue where the instances were hitting a system crash with bug check code 0x0000DEAD. <br />+  Stability fixes in AWS PV Network driver. <br />+  Added support for Windows Server 2008R2.   | July 12, 2016 | 
| 7.3.2 |  +  Improved logging and diagnostics. <br />+  Stability fix in AWS PV Storage driver. In some cases disks may not surface in Windows after reattaching the disk to the instance. <br />+  Added support for Windows Server 2012.   | June 24, 2015 | 
| 7.3.1 | TRIM update: Fix related to TRIM requests. This fix stabilizes instances and improves instance performance when managing large numbers of TRIM requests. |  | 
| 7.3.0 | TRIM support: The AWS PV driver now sends TRIM requests to the hypervisor. Ephemeral disks will properly process TRIM requests given the underlying storage supports TRIM (SSD). Note that EBS-based storage does not support TRIM as of March 2015. |  | 
| 7.2.5 |  +  Stability fix in AWS PV Storage drivers: In some cases the AWS PV driver could dereference invalid memory and cause a system failure. <br />+  Stability fix while generating a crash dump: In some cases the AWS PV driver could get stuck in a race condition when writing a crash dump. Before this release, the issue could only be resolved by forcing the driver to stop and restart which lost the memory dump.   |  | 
| 7.2.4 | Device ID persistence: This driver fix masks the platform PCI device ID and forces the system to always surface the same device ID, even if the instance is moved. More generally, the fix affects how the hypervisor surfaces virtual devices. The fix also includes modifications to the co-installer for the AWS PV drivers so the system persists mapped virtual devices. |  | 
| 7.2.2 |  +  Load the AWS PV drivers in Directory Services Restore Mode (DSRM) mode: Directory Services Restore Mode is a safe mode boot option for Windows Server domain controllers. <br />+  Persist device ID when virtual network adapter device is reattached: This fix forces the system to check the MAC address mapping and persist the device ID. This fix ensures that adapters retain their static settings if the adapters are reattached.   |  | 
| 7.2.1 |  +  Run in safe mode: Fixed an issue where the driver would not load in safe mode. Previously the AWS PV Drivers would only instantiate in normal running systems. <br />+  Add disks to Microsoft Windows Storage Pools: Previously we synthesized page 83 queries. The fix disabled page 83 support. Note this does not affect storage pools that are used in a cluster environment because PV disks are not valid cluster disks.   |  | 
| 7.2.0 | Base: The AWS PV base version. |  | 

## Citrix PV drivers
<a name="xen-driver-citrix"></a>

The Citrix PV drivers are stored in the `%ProgramFiles%\Citrix\XenTools` (32-bit instances) or `%ProgramFiles(x86)%\Citrix\XenTools` (64-bit instances) directory.

The Citrix PV driver components are listed in the Windows registry under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services`. These driver components are as follows: xenevtchn, xeniface, xennet, Xennet6, xensvc, xenvbd, and xenvif.

Citrix also has a driver component named XenGuestAgent, which runs as a Windows service. It handles tasks such as shutdown and restart events from the API. You can access and manage services by running `Services.msc` from the command line.

If you are encountering networking errors while performing certain workloads, you may need to disable the TCP offloading feature for the Citrix PV driver. For more information, see [TCP offloading](pvdrivers-troubleshooting.md#citrix-tcp-offloading).

## Red Hat PV drivers
<a name="xen-driver-redhat"></a>

Red Hat drivers are supported for legacy instances, but are not recommended on newer instances with more than 12GB of RAM due to driver limitations. Instances with more than 12GB of RAM running Red Hat drivers can fail to boot and become inaccessible. We recommend upgrading Red Hat drivers to Citrix PV drivers, and then upgrade Citrix PV drivers to AWS PV drivers.

The source files for the Red Hat drivers are in the `%ProgramFiles%\RedHat` (32-bit instances) or `%ProgramFiles(x86)%\RedHat` (64-bit instances) directory. The two drivers are `rhelnet`, the Red Hat Paravirtualized network driver, and `rhelscsi`, the Red Hat SCSI miniport driver.

## Subscribe to notifications
<a name="drivers-subscribe-notifications"></a>

Amazon SNS can notify you when new versions of EC2 Windows Drivers are released. You can subscribe to these notifications.

**Note**  
You must specify the Region in which the SNS topic was created.

Whenever new EC2 Windows drivers are released, we send notifications to subscribers. If you no longer want to receive these notifications, you can unsubscribe. For more information, see [Delete an SNS topic and subscription](https://docs.aws.amazon.com/sns/latest/dg/sns-delete-subscription-topic.html).

------
#### [ Console ]

**To subscribe to notifications**

1. Open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home).

1. In the navigation bar, change the Region to **US East (N. Virginia)**, if necessary. You must select this Region because the SNS notifications that you are subscribing to are in this Region.

1. In the navigation pane, choose **Subscriptions**.

1. Choose **Create subscription**.

1. In the **Create subscription** dialog box, do the following:

   1. For **TopicARN**, copy the following Amazon Resource Name (ARN):

      arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers

   1. For **Protocol**, choose `Email`.

   1. For **Endpoint**, type an email address that you can use to receive the notifications.

   1. Choose **Create subscription**.

1. You'll receive a confirmation email. Open the email and follow the directions to complete your subscription.

------
#### [ AWS CLI ]

**To subscribe to notifications**  
Use the following command.

```
aws sns subscribe \
    --topic-arn arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers \
    --region us-east-1 \
    --protocol email \
    --notification-endpoint {{YourUserName@YourDomainName.ext}}
```

------
#### [ PowerShell ]

**To subscribe to notifications**  
Use the following command.

```
Connect-SNSNotification `
    -TopicArn 'arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers' `
    -Region us-east-1 `
    -Protocol email `
    -Endpoint "{{YourUserName@YourDomainName.ext}}"
```

------