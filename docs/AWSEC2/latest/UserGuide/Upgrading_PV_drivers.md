# Upgrade PV drivers on EC2 Windows

instances

We recommend that you install the latest PV drivers to improve the stability and
performance of your EC2 Windows instances. The directions on this page help you download
the driver package and run the install program.

###### To verify which driver your Windows instance uses

Open **Device Manager** and view **Network
Adapters**. Check whether the PV driver is one of the following:

- AWS PV Network Device
- Citrix PV Ethernet Adapter
- Red Hat PV NIC Driver

###### System requirements

Be sure to check the `readme.txt` file in the download for
system requirements.

###### Contents

- [Upgrade Windows Server instances (AWS
  PV upgrade) with Distributor](#aws-pv-upgrade-distributor "#aws-pv-upgrade-distributor")
- [Upgrade Windows Server instances (AWS PV upgrade)
  manually](#aws-pv-upgrade "#aws-pv-upgrade")
- [Upgrade a domain controller (AWS PV
  upgrade)](#aws-pv-upgrade-dc "#aws-pv-upgrade-dc")
- [Upgrade Windows Server 2008 and 2008 R2
  instances (Red Hat to Citrix PV upgrade)](#win2008-citrix-upgrade "#win2008-citrix-upgrade")
- [Upgrade your Citrix Xen guest agent
  service](#citrix-pv-guest-agent-upgrade "#citrix-pv-guest-agent-upgrade")

## Upgrade Windows Server instances (AWS

PV upgrade) with Distributor

You can use Distributor, a capability of AWS Systems Manager, to install or upgrade the
AWS PV driver package. The installation or upgrade can be performed one time, or
you can install or update it on a schedule. The `In-place update` option
for **Installation Type** isn't supported for this Distributor
package.

###### Important

If your instance is a domain controller, see [Upgrade a domain controller (AWS PV
upgrade)](#aws-pv-upgrade-dc "#aws-pv-upgrade-dc"). The upgrade process for domain
controller instances is different than standard editions of Windows.

1. We recommend that you create a backup in case you need to roll back your
   changes.

###### Tip

Instead of creating the AMI from the Amazon EC2 console, you can use Systems Manager
Automation to create the AMI using the `AWS-CreateImage`
runbook. For more information, see [AWS-CreateImage](../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-createimage.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-createimage.md") in the
_AWS Systems Manager Automation runbook reference User
Guide_.

    1. When you stop an instance, the data on any instance store volumes
     is erased. Before you stop an instance, verify that you've copied
     any data that you need from your instance store volumes to
     persistent storage, such as Amazon EBS or Amazon S3.
    2. In the navigation pane, choose
     **Instances**.
    3. Select the instance that requires the driver upgrade, and choose
     **Instance state**, **Stop
     instance**.
    4. After the instance is stopped, select the instance, choose
     **Actions**, then **Image and
     templates**, and then choose **Create
     image**.
    5. Choose **Instance state**, **Start
     instance**.

2. Connect to the instance using Remote Desktop. For more information, see
   [Connect to your Windows instance using an RDP client](connect-rdp.md "connect-rdp.md").
3. We recommend that you take all non-system disks offline and note any drive
   letter mappings to the secondary disks in Disk Management before you perform
   this upgrade. This step is not required if you are performing an in-place
   update of AWS PV drivers. We also recommend setting non-essential services
   to **Manual** start-up in the Services console.
4. For the instructions for how to install or upgrade the AWS PV driver
   package using Distributor, see the procedures in [Install or update packages](../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md "../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md") in the _AWS Systems Manager User
   Guide_.
5. For **Name**, choose
   **AWSPVDriver**.
6. For **Installation type**, select **Uninstall and
   reinstall**.
7. Configure the other parameters for the package as necessary and run
   installation or upgrade using the referenced procedure in [Step 4](#distributor-procedure-awspv "#distributor-procedure-awspv").

After running the Distributor package, the instance automatically reboots
and then upgrades the driver. The instance will not be available for up to
15 minutes. 8. After the upgrade is complete, and the instance passes both health checks
in the Amazon EC2 console, verify that the new driver was installed by connecting
to the instance using Remote Desktop. 9. After you are connected, run the following PowerShell command:

```
Get-ItemProperty HKLM:\SOFTWARE\Amazon\PVDriver
```

10. Verify that the driver version is the same as the latest version listed in
    the Driver Version History table. For more information, see [AWS PV driver package history](xen-drivers-overview.md#pv-driver-history "xen-drivers-overview.md#pv-driver-history") Open
    Disk Management to review any offline secondary volumes and bring them
    online corresponding to the drive letters noted in [Step 3](#secondary-disks-step-distributor "#secondary-disks-step-distributor").

If you previously disabled [TCP offloading](pvdrivers-troubleshooting.md#citrix-tcp-offloading "pvdrivers-troubleshooting.md#citrix-tcp-offloading") using Netsh for Citrix PV drivers we
recommend that you re-enable this feature after upgrading to AWS PV drivers. TCP
Offloading issues with Citrix drivers are not present in the AWS PV drivers. As a
result, TCP Offloading provides better performance with AWS PV drivers.

If you previously applied a static IP address or DNS configuration to the network
interface, you might need to reapply the static IP address or DNS configuration
after upgrading AWS PV drivers.

## Upgrade Windows Server instances (AWS PV upgrade)

manually

Use the following procedure to perform an in-place upgrade of AWS PV drivers, or
to upgrade from Citrix PV drivers to AWS PV drivers on Windows Server 2008 R2,
Windows Server 2012, Windows Server 2012 R2, Windows Server 2016, Windows Server
2019, or Windows Server 2022. This upgrade is not available for Red Hat drivers, or
for other versions of Windows Server.

Some older versions of Windows Server can't use the latest drivers. To verify
which driver version to use for your operating system, see the driver version table
in the [Paravirtual drivers for Windows instances](xen-drivers-overview.md "xen-drivers-overview.md")
page.

###### Important

If your instance is a domain controller, see [Upgrade a domain controller (AWS PV
upgrade)](#aws-pv-upgrade-dc "#aws-pv-upgrade-dc"). The upgrade process for domain
controller instances is different than standard editions of Windows.

###### To upgrade AWS PV drivers manually

1. We recommend that you create a backup in case you need to roll back your
   changes.

###### Tip

Instead of creating the AMI from the Amazon EC2 console, you can use Systems Manager
Automation to create the AMI using the `AWS-CreateImage`
runbook. For more information, see [AWS-CreateImage](../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-createimage.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-createimage.md") in the
_AWS Systems Manager Automation runbook reference User
Guide_.

    1. When you stop an instance, the data on any instance store volumes
     is erased. Before you stop an instance, verify that you've copied
     any data that you need from your instance store volumes to
     persistent storage, such as Amazon EBS or Amazon S3.
    2. In the navigation pane, choose
     **Instances**.
    3. Select the instance that requires the driver upgrade, and choose
     **Instance state**, **Stop
     instance**.
    4. After the instance is stopped, select the instance, choose
     **Actions**, then **Image and
     templates**, and then choose **Create
     image**.
    5. Choose **Instance state**, **Start
     instance**.

2. Connect to the instance using Remote Desktop.
3. We recommend that you take all non-system disks offline and note any drive
   letter mappings to the secondary disks in Disk Management before you perform
   this upgrade. This step is not required if you are performing an in-place
   update of AWS PV drivers. We also recommend setting non-essential services
   to **Manual** start-up in the Services console.
4. Download the drivers to your instance using one of the following
   options:
   - Browser – [Download](https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSPV/Latest/AWSPVDriver.zip "https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSPV/Latest/AWSPVDriver.zip")

   the latest driver package to the instance and
   extract the zip archive.
   - PowerShell – Run the
     following commands:

   ```
   Invoke-WebRequest https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSPV/Latest/AWSPVDriver.zip -outfile $env:USERPROFILE\pv_driver.zip
   Expand-Archive $env:userprofile\pv_driver.zip -DestinationPath $env:userprofile\pv_drivers
   ```

   If you receive an error when downloading the file, and you
   are using Windows Server 2016 or earlier, TLS 1.2 might need
   to be enabled for your PowerShell terminal. You can enable
   TLS 1.2 for the current PowerShell session with the
   following command and then try again:

   ```
   [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
   ```

5. Run `AWSPVDriverSetup.msi`.

After running the MSI, the instance automatically reboots and then upgrades the
driver. The instance will not be available for up to 15 minutes. After the upgrade
is complete and the instance passes both health checks in the Amazon EC2 console, you can
verify that the new driver was installed by connecting to the instance using Remote
Desktop and then running the following PowerShell command:

```
Get-ItemProperty HKLM:\SOFTWARE\Amazon\PVDriver
```

Verify that the driver version is the same as the latest version listed in the
Driver Version History table. For more information, see [AWS PV driver package history](xen-drivers-overview.md#pv-driver-history "xen-drivers-overview.md#pv-driver-history") Open Disk
Management to review any offline secondary volumes and bring them online
corresponding to the drive letters noted in [Step 3](#secondary-disks-step-manual "#secondary-disks-step-manual").

If you previously disabled [TCP offloading](pvdrivers-troubleshooting.md#citrix-tcp-offloading "pvdrivers-troubleshooting.md#citrix-tcp-offloading") using Netsh for Citrix PV drivers we
recommend that you re-enable this feature after upgrading to AWS PV drivers. TCP
Offloading issues with Citrix drivers are not present in the AWS PV drivers. As a
result, TCP Offloading provides better performance with AWS PV drivers.

If you previously applied a static IP address or DNS configuration to the network
interface, you might need to reapply the static IP address or DNS configuration
after upgrading AWS PV drivers.

## Upgrade a domain controller (AWS PV

upgrade)

Use the following procedure on a domain controller to perform either an in-place
upgrade of AWS PV drivers, or to upgrade from Citrix PV drivers to AWS PV
drivers. To ensure that your FSMO roles remain operational during the upgrade, we
recommend that you transfer those roles to other domain controllers before you start
the upgrade. For more information, see [How to view and transfer FSMO roles](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/view-transfer-fsmo-roles "https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/view-transfer-fsmo-roles") on the _Microsoft
Learn_ website.

###### To upgrade a domain controller

1. We recommend that you create a backup of your domain controller in case
   you need to roll back your changes. Using an AMI as a backup is not
   supported. For more information, see [Backup and restore considerations](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controllers-hyper-v#backup-and-restore-considerations "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controllers-hyper-v#backup-and-restore-considerations") in the Microsoft
   documentation.
2. Run the following command to configure Windows to boot into Directory
   Services Restore Mode (DSRM).

###### Warning

Before running this command, confirm that you know the DSRM password.
You'll need this information so that you can log in to your instance
after the upgrade is complete and the instance automatically
reboots.

```
bcdedit /set {default} safeboot dsrepair
```

PowerShell:

```
PS C:\> bcdedit /set "{default}" safeboot dsrepair
```

The system must boot into DSRM because the upgrade utility removes Citrix
PV storage drivers so it can install AWS PV drivers. Therefore we
recommend noting any drive letter and folder mappings to the secondary disks
in Disk Management. When Citrix PV storage drivers are not present,
secondary drives are not detected. Domain controllers that use an NTDS
folder on secondary drives will not boot because the secondary disk is not
detected.

###### Warning

After you run this command do not manually reboot the system. The
system will be unreachable because Citrix PV drivers do not support
DSRM. 3. Run the following command to add `DisableDCCheck` to
the registry:

```
reg add HKLM\SOFTWARE\Wow6432Node\Amazon\AWSPVDriverSetup /v DisableDCCheck /t REG_SZ /d true
```

4. [Download](https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSPV/Latest/AWSPVDriver.zip "https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSPV/Latest/AWSPVDriver.zip")

the latest driver package to the instance and extract
the zip archive. 5. Run `AWSPVDriverSetup.msi`.

After running the MSI, the instance automatically reboots and then
upgrades the driver. The instance will not be available for up to 15
minutes. 6. After the upgrade is complete and the instance passes both health checks
in the Amazon EC2 console, connect to the instance using Remote Desktop. Open
Disk Management to review any offline secondary volumes and bring them
online corresponding to the drive letters and folder mappings noted
earlier.

You must connect to the instance by specifying the username in the
following format _hostname_\administrator. For example,
Win2k12TestBox\administrator. 7. Run the following command to remove the DSRM boot configuration:

```
bcdedit /deletevalue safeboot
```

8. Reboot the instance.
9. To complete the upgrade process, verify that the new driver was installed.
   In Device Manager, under **Storage Controllers**, locate
   **AWS PV Storage Host Adapter**. Verify that the
   driver version is the same as the latest version listed in the Driver
   Version History table. For more information, see [AWS PV driver package history](xen-drivers-overview.md#pv-driver-history "xen-drivers-overview.md#pv-driver-history").
10. Run the following command to delete `DisableDCCheck`
    from the registry:

```
reg delete HKLM\SOFTWARE\Wow6432Node\Amazon\AWSPVDriverSetup /v DisableDCCheck
```

###### Note

If you previously disabled [TCP offloading](pvdrivers-troubleshooting.md#citrix-tcp-offloading "pvdrivers-troubleshooting.md#citrix-tcp-offloading") using Netsh for Citrix PV drivers we
recommend that you re-enable this feature after upgrading to AWS PV Drivers.
TCP Offloading issues with Citrix drivers are not present in the AWS PV
drivers. As a result, TCP Offloading provides better performance with AWS PV
drivers.

## Upgrade Windows Server 2008 and 2008 R2

instances (Red Hat to Citrix PV upgrade)

Before you start upgrading your Red Hat drivers to Citrix PV drivers, make sure
you do the following:

- Install the latest version of the EC2Config service. For more information,
  see [Install the latest version of EC2Config](UsingConfig_Install.md "UsingConfig_Install.md").
- Verify that you have Windows PowerShell 3.0 installed. To verify the
  version that you have installed, run the following command in a PowerShell
  window:

```
`PS C:\>` $PSVersionTable.PSVersion
```

Windows PowerShell 3.0 is bundled in the Windows Management Framework
(WMF) version 3.0 install package. If you need to install Windows PowerShell
3.0, see [Windows Management Framework 3.0](https://www.microsoft.com/en-us/download/details.aspx?id=34595 "https://www.microsoft.com/en-us/download/details.aspx?id=34595") in the Microsoft Download
Center.

- Back up your important information on the instance, or create an AMI from
  the instance. For more information about creating an AMI, see [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md").

###### Tip

Instead of creating the AMI from the Amazon EC2 console, you can use Systems Manager
Automation to create the AMI using the `AWS-CreateImage`
runbook. For more information, see [AWS-CreateImage](../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-createimage.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-createimage.md") in the
_AWS Systems Manager Automation runbook reference User
Guide_.

If you create an AMI, make sure that you do the following:

    + Write down your password.
    + Do not run the Sysprep tool manually or using the EC2Config
     service.
    + Set your Ethernet adapter to obtain an IP address automatically
     using DHCP.

###### To upgrade Red Hat drivers

1. Connect to your instance and log in as the local administrator. For more
   information about connecting to your instance, see [Connect to your Windows instance using RDP](connecting_to_windows_instance.md "connecting_to_windows_instance.md").
2. In your instance, [download](https://s3.amazonaws.com/ec2-downloads-windows/Drivers/Citrix-Win_PV.zip "https://s3.amazonaws.com/ec2-downloads-windows/Drivers/Citrix-Win_PV.zip") the Citrix PV upgrade package.
3. Extract the contents of the upgrade package to a location of your
   choice.
4. Double-click the **Upgrade.bat** file. If you get a
   security warning, choose **Run**.
5. In the **Upgrade Drivers** dialog box, review the
   information and choose **Yes** if you are ready to start
   the upgrade.
6. In the **Red Hat Paravirtualized Xen Drivers for Windows
   uninstaller** dialog box, choose **Yes** to
   remove the Red Hat software. Your instance will be rebooted.

###### Note

If you do not see the uninstaller dialog box, choose **Red Hat
Paravirtualize** in the Windows taskbar.

![Red Hat Paravirtualized in taskbar.](images/win2003-citrix-taskbar.png) 7. Check that the instance has rebooted and is ready to be used.

    1. Open the Amazon EC2 console at
     [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
    2. On the **Instances** page, select
     **Actions**, then **Monitor and
     troubleshoot**, and then choose **Get system
     log**.
    3. The upgrade operations should have restarted the server 3 or 4
     times. You can see this in the log file by the number of times
     `Windows is Ready to use` is displayed.



    ![Windows system log.](images/win2008-sys-log.png)

8. Connect to your instance and log in as the local administrator.
9. Close the **Red Hat Paravirtualized Xen Drivers for Windows
   uninstaller** dialog box.
10. Confirm that the installation is complete. Navigate to the
    `Citrix-WIN_PV` folder that you extracted earlier,
    open the `PVUpgrade.log` file, and then check for the
    text `INSTALLATION IS COMPLETE`.

![PVUpgrade log file.](images/win2008-pvupgrade-log.png)

## Upgrade your Citrix Xen guest agent

service

If you are using Citrix PV drivers on Windows Server, you can upgrade the Citrix
Xen guest agent service. This Windows service handles tasks such as shutdown and
restart events from the API. You can run this upgrade package on any version of
Windows Server, as long as the instance is running Citrix PV drivers.

###### Important

For Windows Server 2008 R2 and later, we recommend you upgrade to AWS PV
drivers that include the Guest Agent update.

Before you start upgrading your drivers, make sure you back up your important
information on the instance, or create an AMI from the instance. For more
information about creating an AMI, see [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md").

###### Tip

Instead of creating the AMI from the Amazon EC2 console, you can use Systems Manager
Automation to create the AMI using the `AWS-CreateImage`
runbook. For more information, see [AWS-CreateImage](../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-createimage.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-createimage.md") in the
_AWS Systems Manager Automation runbook reference User
Guide_.

If you create an AMI, make sure you do the following:

- Do not enable the Sysprep tool in the EC2Config service.
- Write down your password.
- Set your Ethernet adapter to DHCP.

###### To upgrade your Citrix Xen guest agent service

1. Connect to your instance and log in as the local administrator. For more
   information about connecting to your instance, see [Connect to your Windows instance using RDP](connecting_to_windows_instance.md "connecting_to_windows_instance.md").
2. On your instance, [download](https://s3.amazonaws.com/ec2-downloads-windows/Drivers/Citrix-Win_PV.zip "https://s3.amazonaws.com/ec2-downloads-windows/Drivers/Citrix-Win_PV.zip") the Citrix upgrade package.
3. Extract the contents of the upgrade package to a location of your
   choice.
4. Double-click the **Upgrade.bat** file. If you get a
   security warning, choose **Run**.
5. In the **Upgrade Drivers** dialog box, review the
   information and choose **Yes** if you are ready to start
   the upgrade.
6. When the upgrade is complete, the `PVUpgrade.log` file
   will open and contain the text `UPGRADE IS COMPLETE`.
7. Reboot your instance.
