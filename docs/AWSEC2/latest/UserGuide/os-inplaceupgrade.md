# Perform an in-place upgrade on your EC2 Windows instance

Before you perform an in-place upgrade, you must determine which network drivers the
instance is running. PV network drivers enable you to access your instance using Remote
Desktop. Instances use either AWS PV, Intel Network Adapter, or
the Enhanced Networking drivers. For more information, see [Paravirtual drivers for Windows instances](xen-drivers-overview.md "xen-drivers-overview.md").

## Before you begin an in-place upgrade

Complete the following tasks and note the following important details before you
begin your in-place upgrade.

- Read the Microsoft documentation to understand the upgrade requirements,
  known issues, and restrictions. Also review the official instructions for
  upgrading.
  - [Upgrade Options for Windows Server 2012](<https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj574204(v=ws.11)> "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj574204(v=ws.11)")
  - [Upgrade Options for Windows Server 2012 R2](<https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn303416(v=ws.11)> "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn303416(v=ws.11)")
  - [Upgrade and conversion options for Windows Server 2016 and above](https://learn.microsoft.com/en-us/windows-server/get-started/install-upgrade-migrate "https://learn.microsoft.com/en-us/windows-server/get-started/install-upgrade-migrate")
  - [Windows
    Server Upgrades](https://learn.microsoft.com/en-us/windows-server/get-started/upgrade-overview "https://learn.microsoft.com/en-us/windows-server/get-started/upgrade-overview")

- We recommend performing an operating system upgrade on instances with at
  least 2 vCPUs and 4GB of RAM. If needed, you can change the instance to a
  larger size of the same type (t2.small to t2.large, for example), perform
  the upgrade, and then resize it back to the original size. If you are
  required to retain the instance size, you can monitor the progress using the
  [instance console screenshot](troubleshoot-unreachable-instance.md#instance-console-screenshot "troubleshoot-unreachable-instance.md#instance-console-screenshot").
  For more information, see [Amazon EC2 instance type changes](ec2-instance-resize.md "ec2-instance-resize.md").
- Verify that the root volume on your Windows instance has enough free disk
  space. The Windows Setup process might not warn you of insufficient disk
  space. For information about how much disk space is required to upgrade a
  specific operating system, see the Microsoft documentation. If the volume
  does not have enough space, it can be expanded. For more information, see
  [Amazon EBS Elastic Volumes](../../../ebs/latest/userguide/ebs-modify-volume.md "../../../ebs/latest/userguide/ebs-modify-volume.md")
  in the _Amazon EBS User Guide_.
- Determine your upgrade path. You must upgrade the operating system to the
  same architecture. For example, you must upgrade a 32-bit system to a 32-bit
  system. Windows Server 2008 R2 and later are 64-bit only.
- Disable antivirus and anti-spyware software and firewalls. These types of
  software can conflict with the upgrade process. Re-enable antivirus and
  anti-spyware software and firewalls after the upgrade completes.
- Update to the latest drivers as described in [Migrate an EC2 Windows instance to a Nitro-based instance type](migrating-latest-types.md "migrating-latest-types.md").
- The Upgrade Helper Service only supports instances running Citrix PV
  drivers. If the instance is running Red Hat drivers, you must manually [upgrade those drivers](Upgrading_PV_drivers.md "Upgrading_PV_drivers.md")
  first.

## Upgrade an instance in-place with AWS PV, Intel

Network Adapter, or the Enhanced Networking drivers

Use the following procedure to upgrade a Windows Server instance using the AWS
PV, Intel Network Adapter, or the Enhanced Networking network drivers.

###### To perform the in-place upgrade

1. Create an AMI of the system you plan to upgrade for either backup or
   testing purposes. You can then perform the upgrade on the copy to simulate a
   test environment. If the upgrade completes, you can switch traffic to this
   instance with little downtime. If the upgrade fails, you can revert to the
   backup. For more information, see [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md").
2. Ensure that your Windows Server instance is using the latest network
   drivers.
   1. To update your AWS PV driver, see [Upgrade PV drivers on EC2 Windows
      instances](Upgrading_PV_drivers.md "Upgrading_PV_drivers.md").
   2. To update your ENA driver, see
      [Install the ENA driver on EC2 Windows instances](ena-adapter-driver-install-upgrade-win.md "ena-adapter-driver-install-upgrade-win.md").
   3. To update your Intel drivers, see [Enhanced networking with the Intel 82599 VF interface](sriov-networking.md "sriov-networking.md")

3. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
4. In the navigation pane, choose **Instances**. Locate the
   instance. Make a note of the instance ID and Availability Zone for the
   instance. You need this information later in this procedure.
5. If you are upgrading from Windows Server 2012 or 2012 R2 to Windows Server
   2016 or later, perform the following on your instance before you proceed.
   1. Uninstall the EC2Config service. For more information, see [Windows Service administration for EC2Launch v2 and EC2Config agents](launch-agents-service-admin.md "launch-agents-service-admin.md").
   2. Install EC2Launch v1 or the EC2Launch v2 agent. For more information, see [Use the EC2Launch v1 agent to perform tasks during EC2 Windows
      instance launch](ec2launch.md "ec2launch.md") and [Use the EC2Launch v2 agent to perform tasks during EC2 Windows
      instance launch](ec2launch-v2.md "ec2launch-v2.md").
   3. Install the AWS Systems Manager SSM Agent. For more information, see
      [Manually install SSM Agent on Amazon EC2 for Windows Server](../../../systems-manager/latest/userguide/manually-install-ssm-agent-windows.md "../../../systems-manager/latest/userguide/manually-install-ssm-agent-windows.md")
      in the _AWS Systems Manager User Guide_.

6. Create a new volume from a Windows Server installation media
   snapshot.
   1. In the left navigation pane, under **Elastic Block
      Store**, choose **Snapshots**.
   2. From the filter bar, choose **Public
      snapshots**.
   3. In the search bar, specify the following filters:
      - Choose **Owner Alias**, then
        **=**, then
        **amazon**.
      - Choose **Description**, and then start
        typing `Windows`. Select the Windows
        filter that matches the system architecture and language
        preference you're upgrading to. For example, choose
        **Windows 2019 English Installation
        Media** to upgrade to Windows Server
      2019.

   4. Select the checkbox next to the snapshot that matches the system
      architecture and language preference you're upgrading to, and then
      choose **Actions**, **Create volume from
      snapshot**.
   5. On the **Create volume** page, choose the
      Availability Zone that matches your Windows instance, and then
      choose **Create volume**.

7. In the **Successfully created volume
   vol-`1234567890example`** banner
   at the top of the page, choose the ID of the volume that you just
   created.
8. Choose **Actions**, **Attach
   volume**.
9. On the **Attach volume** page, for
   **Instance**, select the instance ID of your Windows
   instance, and then choose **Attach volume**.
10. Make the new volume available for use by following the steps at [Make
    an Amazon EBS volume available for use](../../../ebs/latest/userguide/ebs-using-volumes.md "../../../ebs/latest/userguide/ebs-using-volumes.md").

###### Important

Do not initialize the disk because doing so will delete the existing
data. 11. In Windows PowerShell, switch to the new volume drive. Begin the upgrade
by opening the installation media volume you attached to the
instance.

    1. If you are upgrading to Windows Server 2016 or later, run the
     following:



    ```
    .\setup.exe /auto upgrade /dynamicupdate disable
    ```

    ###### Note

    Running the setup.exe with the `/dynamicupdate`
     option set to disabled prevents Windows from installing updates
     during the Windows Server upgrade process, as installing updates
     during the upgrade can cause failures. You can install updates
     with Windows Update after the upgrade completes.


    If you are upgrading to an earlier version of Windows Server, run
     the following:



    ```
    Sources\setup.exe
    ```
    2. For **Select the operating system you want to
     install**, select the full installation option for your
     Windows Server instance, and choose
     **Next**.
    3. For **Which type of installation do you want?**,
     choose **Upgrade**.
    4. Complete the wizard.

Windows Server Setup copies and processes files. After several minutes, your
Remote Desktop session closes. The time it takes to upgrade depends on the number of
applications and server roles running on your Windows Server instance. The upgrade
process could take as little as 40 minutes or several hours. The instance may fail
one or more status checks during the upgrade process. When the upgrade completes, all
status checks pass. You can check the system log for console output or use Amazon CloudWatch
metrics for disk and CPU activity to determine whether the upgrade is
progressing.

###### Note

If upgrading to Windows Server 2019, after the upgrade is complete you can
change the desktop background manually to remove the previous operating system
name if desired.

If the instance has not passed all status checks after several hours, see [Troubleshoot an operating system upgrade on an EC2 Windows instance](os-upgrade-trbl.md "os-upgrade-trbl.md").

## Post upgrade tasks

1. Log in to the instance to initiate an upgrade for the .NET Framework and
   reboot the system when prompted.
2. If you haven't already done so in a prior step, install the EC2Launch v1 or
   EC2Launch v2 agent. For more information, see [Use the EC2Launch v1 agent to perform tasks during EC2 Windows
   instance launch](ec2launch.md "ec2launch.md") and [Use the EC2Launch v2 agent to perform tasks during EC2 Windows
   instance launch](ec2launch-v2.md "ec2launch-v2.md").
3. If you upgraded to Windows Server 2012 R2, we recommend that you upgrade
   the PV drivers to AWS PV drivers. If you upgraded on a Nitro-based
   instance, we recommend that you install or upgrade the NVME and ENA drivers.
   For more information, see [AWS NVMe drivers](aws-nvme-drivers.md "aws-nvme-drivers.md") or
   [Enable enhanced networking on Windows](enabling_enhanced_networking.md#enable-enhanced-networking-ena-windows "enabling_enhanced_networking.md#enable-enhanced-networking-ena-windows").
4. Re-enable antivirus and anti-spyware software and firewalls.
