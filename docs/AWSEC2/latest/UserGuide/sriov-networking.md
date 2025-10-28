# Enhanced networking with the Intel 82599 VF interface

For [Xen-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type"), the Intel 82599 Virtual Function (VF) interface provides enhanced
networking capabilities. The interface uses the Intel `ixgbevf` driver.

The following tabs show how to verify the network adapter driver that's installed for your
instance operating system.

Linux

###### Linux network interface driver

Use the following command to verify that the module is being used on a
particular interface, substituting the interface name that you want to check. If
you are using a single interface (default), this is `eth0`. If the
operating system supports [predictable network names](#predictable-network-names-sriov "#predictable-network-names-sriov"), this could be a name like
`ens5`.

In the following example, the `ixgbevf` module is
not loaded, because the listed driver is `vif`.

````
`[ec2-user ~]$` `ethtool -i `eth0```driver: vif
version:
firmware-version:
bus-info: vif-0
supports-statistics: yes
supports-test: no
supports-eeprom-access: no
supports-register-dump: no
supports-priv-flags: no`
````

In this example, the `ixgbevf` module is loaded.
This instance has enhanced networking properly configured.

````
`[ec2-user ~]$` `ethtool -i `eth0```driver: ixgbevf
version: 4.0.3
firmware-version: N/A
bus-info: 0000:00:03.0
supports-statistics: yes
supports-test: yes
supports-eeprom-access: no
supports-register-dump: yes
supports-priv-flags: no`
````

Windows

###### Windows network adapter

To verify that the driver is installed, connect to your instance and open
Device Manager. You should see `Intel(R) 82599 Virtual Function`
listed under **Network adapters**.

###### Contents

- [Prepare your instance for enhanced networking](#ixgbevf-requirements "#ixgbevf-requirements")
- [Test whether enhanced networking is enabled](#test-enhanced-networking "#test-enhanced-networking")
- [Enable enhanced networking on your instance](#enable-enhanced-networking "#enable-enhanced-networking")
- [Troubleshoot connectivity issues](#enhanced-networking-troubleshooting "#enhanced-networking-troubleshooting")

## Prepare your instance for enhanced networking

To prepare for enhanced networking using the Intel 82599 VF interface, set up your
instance as follows:

- Verify that the instance type is one of the following: C3, C4, D2, I2, M4
  (excluding `m4.16xlarge`), and R3.
- Ensure that the instance has internet connectivity.
- If you have important data on the instance that you want to preserve, you
  should back that data up now by creating an AMI from your instance. Updating
  kernels and kernel modules, as well as enabling the
  `sriovNetSupport` attribute, might render incompatible
  instances or operating systems unreachable. If you have a recent backup,
  your data will still be retained if this happens.
- Linux instances –
  Launch the instance from an HVM AMI using Linux kernel version of 2.6.32
  or later. The latest Amazon Linux HVM AMIs have the modules required for enhanced
  networking installed and have the required attributes set. Therefore, if you
  launch an Amazon EBS–backed, enhanced networking–supported instance
  using a current Amazon Linux HVM AMI, enhanced networking is already enabled for
  your instance.

###### Warning

Enhanced networking is supported only for HVM instances. Enabling
enhanced networking with a PV instance can make it unreachable. Setting
this attribute without the proper module or module version can also make
your instance unreachable.

- Windows instances –
  Launch the instance from a 64-bit HVM AMI. You can't enable enhanced
  networking on Windows Server 2008. Enhanced networking is already enabled
  for Windows Server 2012 R2 and Windows Server 2016 and later AMIs. Windows
  Server 2012 R2 includes Intel driver 1.0.15.3 and we recommend that you
  upgrade that driver to the latest version using the Pnputil.exe utility.
- Use [AWS CloudShell](https://console.aws.amazon.com/cloudshell "https://console.aws.amazon.com/cloudshell") from the AWS Management Console, or install and configure the [AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") or the
  [AWS Tools for Windows PowerShell](../../../powershell/latest/userguide.md "../../../powershell/latest/userguide.md") on any computer you choose,
  preferably your local desktop or laptop. For more information, see [Access Amazon EC2](concepts.md#access-ec2 "concepts.md#access-ec2") or the
  [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md"). Enhanced networking
  cannot be managed from the Amazon EC2 console.

## Test whether enhanced networking is enabled

Verify that the `sriovNetSupport` attribute is set on the instance or the image.

AWS CLI

###### To check the instance attribute (sriovNetSupport)

Use the following [describe-instance-attribute](../../../cli/latest/reference/ec2/describe-instance-attribute.md "../../../cli/latest/reference/ec2/describe-instance-attribute.md") command. If the attribute is set,
the value is `simple`.

```
aws ec2 describe-instance-attribute \
    --instance-id `i-1234567890abcdef0` \
    --attribute sriovNetSupport
```

###### To check the image attribute (sriovNetSupport)

Use the following [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command. If the attribute is set,
the value is `simple`.

```
aws ec2 describe-images \
    --image-id `ami-0abcdef1234567890` \
    --query "Images[].SriovNetSupport"
```

PowerShell

###### To check the instance attribute (sriovNetSupport)

Use the [Get-EC2InstanceAttribute](../../../powershell/latest/reference/items/Get-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Get-EC2InstanceAttribute.md") cmdlet. If the attribute is set,
the value is `simple`.

```
Get-EC2InstanceAttribute `
    -InstanceId `i-1234567890abcdef0` `
    -Attribute sriovNetSupport
```

###### To check the image attribute (sriovNetSupport)

Use the following [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command. If the attribute is set,
the value is `simple`.

```
(Get-EC2Image -ImageId `ami-0abcdef1234567890`).SriovNetSupport
```

## Enable enhanced networking on your instance

The procedure that you use depends on the operating system of the instance.

###### Warning

There is no way to disable the enhanced networking attribute after you've
enabled it.

The latest Amazon Linux HVM AMIs have the `ixgbevf` module
required for enhanced networking installed and have the required
`sriovNetSupport` attribute set. Therefore, if you launch an instance
type using a current Amazon Linux HVM AMI, enhanced networking is already enabled for your
instance. For more information, see [Test whether enhanced networking is enabled](#test-enhanced-networking "#test-enhanced-networking").

If you launched your instance using an older Amazon Linux AMI and it does not
have enhanced networking enabled already, use the following procedure to enable
enhanced networking.

###### To enable enhanced networking

1. Connect to your instance.
2. From the instance, run the following command to update your instance with
   the newest kernel and kernel modules, including
   `ixgbevf`:

```
`[ec2-user ~]$` **sudo yum** update
```

3. From your local computer, reboot your instance using the Amazon EC2 console or
   one of the following commands: [reboot-instances](../../../cli/latest/reference/ec2/reboot-instances.md "../../../cli/latest/reference/ec2/reboot-instances.md") (AWS CLI) or [Restart-EC2Instance](../../../powershell/latest/reference/items/Restart-EC2Instance.md "../../../powershell/latest/reference/items/Restart-EC2Instance.md") (AWS Tools for Windows PowerShell).
4. Connect to your instance again and verify that the
   `ixgbevf` module is installed and at the minimum
   recommended version using the **modinfo ixgbevf** command
   from [Test whether enhanced networking is enabled](#test-enhanced-networking "#test-enhanced-networking").
5. [EBS-backed instance] From your local
   computer, stop the instance using the Amazon EC2 console or one of the following
   commands: [stop-instances](../../../cli/latest/reference/ec2/stop-instances.md "../../../cli/latest/reference/ec2/stop-instances.md") (AWS CLI) or [Stop-EC2Instance](../../../powershell/latest/reference/items/Stop-EC2Instance.md "../../../powershell/latest/reference/items/Stop-EC2Instance.md") (AWS Tools for Windows PowerShell).

[Instance store-backed instance] You can't stop the instance to
modify the attribute. Instead, skip to the next procedure. 6. From your local computer, enable the enhanced networking attribute using
one of the following commands:

AWS CLI
Use the [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md") command as follows.

```
aws ec2 modify-instance-attribute \
    --instance-id `i-1234567890abcdef0` \
    --sriov-net-support simple
```

PowerShell
Use the [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md") cmdlet as follows.

```
Edit-EC2InstanceAttribute `
    -InstanceId `i-1234567890abcdef0` `
    -SriovNetSupport "simple"
```

7. (Optional) Create an AMI from the instance, as described in
   [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md").
   The AMI inherits the enhanced networking attribute from the instance. Therefore,
   you can use this AMI to launch another instance with enhanced networking enabled
   by default.
8. From your local computer, start the instance using the Amazon EC2 console or
   one of the following commands: [start-instances](../../../cli/latest/reference/ec2/start-instances.md "../../../cli/latest/reference/ec2/start-instances.md") (AWS CLI) or [Start-EC2Instance](../../../powershell/latest/reference/items/Start-EC2Instance.md "../../../powershell/latest/reference/items/Start-EC2Instance.md") (AWS Tools for Windows PowerShell).
9. Connect to your instance and verify that the `ixgbevf`
   module is installed and loaded on your network interface using the
   **ethtool -i eth`n`** command
   from [Test whether enhanced networking is enabled](#test-enhanced-networking "#test-enhanced-networking").

###### To enable enhanced networking (instance store-backed instances)

Follow the previous procedure until the step where you stop the instance.
Create a new AMI as described in [Create an Amazon S3-backed AMI](creating-an-ami-instance-store.md "creating-an-ami-instance-store.md"), making sure to enable the
enhanced networking attribute when you register the AMI.

AWS CLI
Use the [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") command as follows.

```
aws ec2 register-image --sriov-net-support simple ...
```

PowerShell
Use [Register-EC2Image](../../../powershell/latest/reference/items/Register-EC2Image.md "../../../powershell/latest/reference/items/Register-EC2Image.md") as follows.

```
Register-EC2Image -SriovNetSupport "simple" `...`
```

Before you begin, [check if enhanced
networking is already enabled](#test-enhanced-networking "#test-enhanced-networking") on your instance.

The Quick Start Ubuntu HVM AMIs include the necessary drivers for enhanced
networking. If you have a version of `ixgbevf` earlier than
2.16.4, you can install the `linux-aws` kernel package to get the
latest enhanced networking drivers.

The following procedure provides the general steps for compiling the
`ixgbevf` module on an Ubuntu instance.

###### To install the `linux-aws`

kernel package

1. Connect to your instance.
2. Update the package cache and packages.

```
`ubuntu:~$` sudo apt-get update && sudo apt-get upgrade -y linux-aws
```

###### Important

If during the update process, you are prompted to install
`grub`, use `/dev/xvda` to
install `grub`, and then choose to keep the current
version of `/boot/grub/menu.lst`.
Before you begin, [check if enhanced
networking is already enabled](#test-enhanced-networking "#test-enhanced-networking") on your instance. The latest Quick Start
HVM AMIs include the necessary drivers for enhanced networking, therefore you do not
need to perform additional steps.

The following procedure provides the general steps if you need to enable enhanced
networking with the Intel 82599 VF interface on a Linux distribution other than Amazon Linux
or Ubuntu. For more information, such as detailed syntax for commands, file
locations, or package and tool support, see the specific documentation for your
Linux distribution.

###### To enable enhanced networking on Linux

1. Connect to your instance.
2. Download the source for the `ixgbevf` module on your
   instance from Sourceforge at [https://sourceforge.net/projects/e1000/files/ixgbevf%20stable/](https://sourceforge.net/projects/e1000/files/ixgbevf%20stable/ "https://sourceforge.net/projects/e1000/files/ixgbevf%20stable/").

Versions of `ixgbevf` earlier than 2.16.4, including
version 2.14.2, do not build properly on some Linux distributions, including
certain versions of Ubuntu. 3. Compile and install the `ixgbevf` module on your
instance.

###### Warning

If you compile the `ixgbevf` module for your
current kernel and then upgrade your kernel without rebuilding the
driver for the new kernel, your system might revert to the
distribution-specific `ixgbevf` module at the next
reboot. This could make your system unreachable if the
distribution-specific version is incompatible with enhanced
networking. 4. Run the **sudo depmod** command to update module
dependencies. 5. Update `initramfs` on your instance to ensure that the
new module loads at boot time. 6. Determine if your system uses predictable network interface names by
default. Systems that use **systemd** or
**udev** versions 197 or greater can rename Ethernet
devices and they do not guarantee that a single network interface will be
named `eth0`. This behavior can cause problems connecting to your
instance. For more information and to see other configuration options, see
[Predictable Network Interface Names](https://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames/ "https://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames/") on the freedesktop.org
website.

    1. You can check the **systemd** or
     **udev** versions on RPM-based systems with the
     following command:



    ```
    `[ec2-user ~]$` `rpm -qa | grep -e '^systemd-[0-9]\+\|^udev-[0-9]\+'``systemd-208-11.el7_0.2.x86_64`
    ```

    In the above Red Hat Enterprise Linux 7 example, the
     **systemd** version is 208, so predictable
     network interface names must be disabled.
    2. Disable predictable network interface names by adding the
     `net.ifnames=0` option to the
     `GRUB_CMDLINE_LINUX` line in
     `/etc/default/grub`.



    ```
    `[ec2-user ~]$` sudo sed -i '/^GRUB\_CMDLINE\_LINUX/s/\"$/\ net\.ifnames\=0\"/' /etc/default/grub
    ```
    3. Rebuild the grub configuration file.



    ```
    `[ec2-user ~]$` sudo grub2-mkconfig -o /boot/grub2/grub.cfg
    ```

7. [EBS-backed instance] From your local computer, stop the instance using
   the Amazon EC2 console or one of the following commands: [stop-instances](../../../cli/latest/reference/ec2/stop-instances.md "../../../cli/latest/reference/ec2/stop-instances.md")
   (AWS CLI) or [Stop-EC2Instance](../../../powershell/latest/reference/items/Stop-EC2Instance.md "../../../powershell/latest/reference/items/Stop-EC2Instance.md") (AWS Tools for Windows PowerShell).

[Instance store-backed instance] You can't stop the instance to modify the
attribute. Instead, skip to the next procedure. 8. From your local computer, enable the enhanced networking attribute using
one of the following commands:

AWS CLI
Use the [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md") command as follows.

```
aws ec2 modify-instance-attribute \
    --instance-id `i-1234567890abcdef0` -\
    -sriov-net-support simple
```

PowerShell
Use the [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md") cmdlet as follows.

```
Edit-EC2InstanceAttribute `
    -InstanceId `i-1234567890abcdef0` `
    -SriovNetSupport "simple"
```

9. (Optional) Create an AMI from the instance, as described in [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md"). The AMI
   inherits the enhanced networking attribute from the instance. Therefore, you
   can use this AMI to launch another instance with enhanced networking enabled
   by default.

If your instance operating system contains an
`/etc/udev/rules.d/70-persistent-net.rules` file,
you must delete it before creating the AMI. This file contains the MAC
address for the Ethernet adapter of the original instance. If another
instance boots with this file, the operating system will be unable to
find the device and `eth0` might fail, causing boot issues.
This file is regenerated at the next boot cycle, and any instances
launched from the AMI create their own version of the file. 10. From your local computer, start the instance using the Amazon EC2 console or
one of the following commands: [start-instances](../../../cli/latest/reference/ec2/start-instances.md "../../../cli/latest/reference/ec2/start-instances.md") (AWS CLI) or [Start-EC2Instance](../../../powershell/latest/reference/items/Start-EC2Instance.md "../../../powershell/latest/reference/items/Start-EC2Instance.md") (AWS Tools for Windows PowerShell). 11. (Optional) Connect to your instance and verify that the module is
installed.

###### To enable enhanced networking (instance store–backed instances)

Follow the previous procedure until the step where you stop the instance.
Create a new AMI as described in [Create an Amazon S3-backed AMI](creating-an-ami-instance-store.md "creating-an-ami-instance-store.md"), making sure to enable the
enhanced networking attribute when you register the AMI.

AWS CLI
Use the [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") command as follows.

```
aws ec2 register-image --sriov-net-support simple `...`
```

PowerShell
Use [Register-EC2Image](../../../powershell/latest/reference/items/Register-EC2Image.md "../../../powershell/latest/reference/items/Register-EC2Image.md") as follows.

```
Register-EC2Image -SriovNetSupport "simple" `...`
```

If you launched your instance and it does not have enhanced
networking enabled already, you must download and install the required network
adapter driver on your instance, and then set the `sriovNetSupport`
instance attribute to activate enhanced networking. You can only enable this
attribute on supported instance types. For more information, see [Enhanced networking on Amazon EC2 instances](enhanced-networking.md "enhanced-networking.md").

###### Important

To view the latest driver updates in the Windows AMIs, see
[Windows AMI version history](../../../ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.md "../../../ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.md") in the _AWS Windows AMI Reference_.

###### To enable enhanced networking

1. Connect to your instance and log in as the local administrator.
2. [Windows Server 2016 and later] Run the following EC2 Launch PowerShell
   script to configure the instance after the driver is installed.

```
`PS C:\>` C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeInstance.ps1 -Schedule
```

###### Important

The administrator password will reset when you enable the initialize
instance EC2 Launch script. You can modify the configuration file to
disable the administrator password reset by specifying it in the
settings for the initialization tasks. 3. From the instance, download the Intel network adapter driver for your operating system:

    * **Windows Server 2022**


    Visit the [download page](https://www.intel.com/content/www/us/en/download/706171/intel-network-adapter-driver-for-windows-server-2022.html "https://www.intel.com/content/www/us/en/download/706171/intel-network-adapter-driver-for-windows-server-2022.html") and download
     `Wired_driver_`version`_x64.zip`.
    * **Windows Server 2019** including for Server version 1809 and later\*


    Visit the [download page](https://www.intel.com/content/www/us/en/download/19372/intel-network-adapter-driver-for-windows-server-2019.html "https://www.intel.com/content/www/us/en/download/19372/intel-network-adapter-driver-for-windows-server-2019.html") and download
     `Wired_driver_`version`_x64.zip`.
    * **Windows Server 2016** including for Server version 1803 and earlier\*


    Visit the [download page](https://www.intel.com/content/www/us/en/download/18737/intel-network-adapter-driver-for-windows-server-2016.html "https://www.intel.com/content/www/us/en/download/18737/intel-network-adapter-driver-for-windows-server-2016.html") and download `Wired_driver_`version`_x64.zip`.
    * **Windows Server 2012 R2**


    Visit the [download page](https://www.intel.com/content/www/us/en/download/17480/intel-network-adapter-driver-for-windows-server-2012-r2.html "https://www.intel.com/content/www/us/en/download/17480/intel-network-adapter-driver-for-windows-server-2012-r2.html") and download `Wired_driver_`version`_x64.zip`.
    * **Windows Server 2012**


    Visit the [download page](https://www.intel.com/content/www/us/en/download/16789/intel-network-adapter-driver-for-windows-server-2012.html "https://www.intel.com/content/www/us/en/download/16789/intel-network-adapter-driver-for-windows-server-2012.html") and download `Wired_driver_`version`_x64.zip`.
    * **Windows Server 2008 R2**


    Visit the [download page](https://www.intel.com/content/www/us/en/download/15590/intel-network-adapter-driver-for-windows-7-final-release.html "https://www.intel.com/content/www/us/en/download/15590/intel-network-adapter-driver-for-windows-7-final-release.html") and download `PROWinx64Legacy.exe`.

\*Server versions 1803 and earlier as well as 1809 and later are not specifically
addressed on the Intel Drivers and Software pages. 4. Install the Intel network adapter driver for your operating system.

    * **Windows Server 2008 R2**




    	1. In the **Downloads** folder, locate the
    	 `PROWinx64Legacy.exe` file and rename it
    	 to `PROWinx64Legacy.zip`.
    	2. Extract the contents of the
    	 `PROWinx64Legacy.zip` file.
    	3. Open the command line, navigate to the extracted folder,
    	 and run the following command to use the `pnputil`
    	 utility to add and install the INF file in the driver store.



    	```
    	`C:\>` pnputil -a PROXGB\Winx64\NDIS62\vxn62x64.inf
    	```
    * **Windows Server 2022, Windows Server 2019, Windows Server 2016, Windows Server 2012 R2,
     and Windows Server 2012**




    	1. In the **Downloads** folder, extract the contents of the
    	 `Wired_driver_`version`_x64.zip` file.
    	2. Open the command line, navigate to the extracted folder,
    	 and run one of the following commands to use the `pnputil`
    	 utility to add and install the INF file in the driver store.




    		+ Windows Server 2022



    		```
    		pnputil -i -a PROXGB\Winx64\NDIS68\vxn68x64.inf
    		```
    		+ Windows Server 2019



    		```
    		pnputil -i -a PROXGB\Winx64\NDIS68\vxn68x64.inf
    		```
    		+ Windows Server 2016



    		```
    		pnputil -i -a PROXGB\Winx64\NDIS65\vxn65x64.inf
    		```
    		+ Windows Server 2012 R2



    		```
    		pnputil -i -a PROXGB\Winx64\NDIS64\vxn64x64.inf
    		```
    		+ Windows Server 2012



    		```
    		pnputil -i -a PROXGB\Winx64\NDIS63\vxn63x64.inf
    		```

5. From your local computer, enable the enhanced networking attribute using
   one of the following commands:

AWS CLI
Use the [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md") command as follows.

```
aws ec2 modify-instance-attribute \
    --instance-id `i-1234567890abcdef0` \
    --sriov-net-support simple
```

PowerShell
Use the [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md") cmdlet as follows.

```
Edit-EC2InstanceAttribute `
    -InstanceId `i-1234567890abcdef0` `
    -SriovNetSupport "simple"
```

6. (Optional) Create an AMI from the instance, as described in
   [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md").
   The AMI inherits the enhanced networking attribute from the instance. Therefore,
   you can use this AMI to launch another instance with enhanced networking enabled
   by default.
7. From your local computer, start the instance using the Amazon EC2 console or
   one of the following commands: [start-instances](../../../cli/latest/reference/ec2/start-instances.md "../../../cli/latest/reference/ec2/start-instances.md") (AWS CLI) or [Start-EC2Instance](../../../powershell/latest/reference/items/Start-EC2Instance.md "../../../powershell/latest/reference/items/Start-EC2Instance.md") (AWS Tools for Windows PowerShell).

## Troubleshoot connectivity issues

If you lose connectivity while enabling enhanced networking, the
`ixgbevf` module might be incompatible with the kernel. Try
installing the version of the `ixgbevf` module included with the
distribution of Linux for your instance.

If you enable enhanced networking for a PV instance or AMI, this can make your
instance unreachable.

For more information, see [How
do I turn on and configure enhanced networking on my EC2 instances?](https://repost.aws/knowledge-center/enable-configure-enhanced-networking "https://repost.aws/knowledge-center/enable-configure-enhanced-networking")
