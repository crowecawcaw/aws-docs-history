# Enable enhanced networking on your instance

The procedure that you use depends on the operating system of the instance.

The AMIs for Amazon Linux include the kernel driver required for
enhanced networking with ENA installed and have ENA support enabled. Therefore, if
you launch an instance with an HVM version of Amazon Linux on a supported instance type,
enhanced networking is already enabled for your instance. For more information, see
[Test whether enhanced networking is enabled](test-enhanced-networking-ena.md "test-enhanced-networking-ena.md").

The latest Ubuntu HVM AMIs include the kernel driver required for enhanced networking
with ENA installed and have ENA support enabled. Therefore, if you launch an
instance with the latest Ubuntu HVM AMI on a supported instance type, enhanced
networking is already enabled for your instance. For more information, see [Test whether enhanced networking is enabled](test-enhanced-networking-ena.md "test-enhanced-networking-ena.md").

If you launched your instance using an older AMI and it does not have enhanced
networking enabled already, you can install the `linux-aws`
kernel package to get the latest enhanced networking drivers and update the required
attribute.

###### To install the `linux-aws` kernel package (Ubuntu 16.04 or later)

Ubuntu 16.04 and 18.04 ship with the Ubuntu custom kernel (`linux-aws` kernel
package). To use a different kernel, contact [Support](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support").

###### To install the `linux-aws`

kernel package (Ubuntu Trusty 14.04)

1. Connect to your instance.
2. Update the package cache and packages.

```
`ubuntu:~$` sudo apt-get update && sudo apt-get upgrade -y linux-aws
```

###### Important

If during the update process you are prompted to install
`grub`, use `/dev/xvda` to
install `grub` onto, and then choose to keep the
current version of `/boot/grub/menu.lst`. 3. [EBS-backed instance] From your local computer, stop the instance using
the Amazon EC2 console or one of the following commands: [stop-instances](../../../cli/latest/reference/ec2/stop-instances.md "../../../cli/latest/reference/ec2/stop-instances.md") (AWS CLI) or [Stop-EC2Instance](../../../powershell/latest/reference/items/Stop-EC2Instance.md "../../../powershell/latest/reference/items/Stop-EC2Instance.md") (AWS Tools for Windows PowerShell).

[Instance store-backed instance] You can't stop the instance to modify the
attribute. Instead, proceed to this procedure: [To enable enhanced
networking on Ubuntu (instance store-backed instances)](#enhanced-networking-ena-instance-store-ubuntu "#enhanced-networking-ena-instance-store-ubuntu"). 4. From your local computer, enable the enhanced networking attribute using
one of the following commands:

    * [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md")
     (AWS CLI)



    ```
    aws ec2 modify-instance-attribute --instance-id `i-1234567890abcdef0` --ena-support
    ```
    * [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md")
     (Tools for Windows PowerShell)



    ```
    Edit-EC2InstanceAttribute -InstanceId `i-1234567890abcdef0` -EnaSupport $true
    ```

5. (Optional) Create an AMI from the instance, as described in [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md"). The
   AMI inherits the enhanced networking `enaSupport` attribute from
   the instance. Therefore, you can use this AMI to launch another instance
   with enhanced networking enabled by default.
6. From your local computer, start the instance using the Amazon EC2 console or
   one of the following commands: [start-instances](../../../cli/latest/reference/ec2/start-instances.md "../../../cli/latest/reference/ec2/start-instances.md") (AWS CLI) or [Start-EC2Instance](../../../powershell/latest/reference/items/Start-EC2Instance.md "../../../powershell/latest/reference/items/Start-EC2Instance.md") (AWS Tools for Windows PowerShell).

###### To enable enhanced

networking on Ubuntu (instance store-backed instances)

Follow the previous procedure until the step where you stop the instance.
Create a new AMI as described in [Create an Amazon S3-backed AMI](creating-an-ami-instance-store.md "creating-an-ami-instance-store.md"), making sure to enable the
enhanced networking attribute when you register the AMI.

- [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") (AWS CLI)

```
aws ec2 register-image --ena-support `...`
```

- [Register-EC2Image](../../../powershell/latest/reference/items/Register-EC2Image.md "../../../powershell/latest/reference/items/Register-EC2Image.md") (AWS Tools for Windows PowerShell)

```
Register-EC2Image -EnaSupport $true `...`
```

The latest AMIs for Red Hat Enterprise Linux, SUSE Linux Enterprise Server, and
CentOS include the kernel driver required for enhanced networking with ENA and have ENA
support enabled. Therefore, if you launch an instance with the latest AMI on a
supported instance type, enhanced networking is already enabled for your instance.
For more information, see [Test whether enhanced networking is enabled](test-enhanced-networking-ena.md "test-enhanced-networking-ena.md").

The following procedure provides the general steps for enabling enhanced
networking on a Linux distribution other than Amazon Linux AMI or Ubuntu. For more
information, such as detailed syntax for commands, file locations, or package and
tool support, see the documentation for your Linux distribution.

###### To enable enhanced networking on Linux

1. Connect to your instance.
2. Clone the source code for the `ena` kernel driver on your
   instance from GitHub at [https://github.com/amzn/amzn-drivers](https://github.com/amzn/amzn-drivers "https://github.com/amzn/amzn-drivers").
   (SUSE Linux Enterprise Server 12 SP2 and later include ENA 2.02 by default,
   so you are not required to download and compile the ENA driver. For SUSE
   Linux Enterprise Server 12 SP2 and later, you should file a request to add
   the driver version you want to the stock kernel).

```
git clone https://github.com/amzn/amzn-drivers
```

3. Compile and install the `ena` kernel driver on your instance.
   These steps depend on the Linux distribution. For more information about
   compiling the kernel driver on Red Hat Enterprise Linux, see [How do I
   install the latest ENS driver for enhanced network support on an Amazon EC2 instance
   that runs RHEL?](https://repost.aws/knowledge-center/install-ena-driver-rhel-ec2 "https://repost.aws/knowledge-center/install-ena-driver-rhel-ec2")
4. Run the **sudo depmod** command to update kernel driver
   dependencies.
5. Update `initramfs` on your instance to ensure that the
   new kernel driver loads at boot time. For example, if your distribution supports
   **dracut**, you can use the following command.

```
dracut -f -v
```

6. Determine if your system uses predictable network interface names by
   default. Systems that use **systemd** or
   **udev** versions 197 or greater can rename Ethernet
   devices and they do not guarantee that a single network interface will be
   named `eth0`. This behavior can cause problems connecting to your
   instance. For more information and to see other configuration options, see
   [Predictable Network Interface Names](https://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames/ "https://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames/") on the freedesktop.org
   website.
   1. You can check the **systemd** or
      **udev** versions on RPM-based systems with the
      following command.

   ```
   rpm -qa | grep -e '^systemd-[0-9]\+\|^udev-[0-9]\+'`systemd-208-11.el7_0.2.x86_64`
   ```

   In the above Red Hat Enterprise Linux 7 example, the
   **systemd** version is 208, so predictable
   network interface names must be disabled. 2. Disable predictable network interface names by adding the
   `net.ifnames=0` option to the
   `GRUB_CMDLINE_LINUX` line in
   `/etc/default/grub`.

   ```
   sudo sed -i '/^GRUB\_CMDLINE\_LINUX/s/\"$/\ net\.ifnames\=0\"/' /etc/default/grub
   ```

   3. Rebuild the grub configuration file.

   ```
   sudo grub2-mkconfig -o /boot/grub2/grub.cfg
   ```

7. [EBS-backed instance] From your local computer, stop the instance using
   the Amazon EC2 console or one of the following commands: [stop-instances](../../../cli/latest/reference/ec2/stop-instances.md "../../../cli/latest/reference/ec2/stop-instances.md") (AWS CLI), [Stop-EC2Instance](../../../powershell/latest/reference/items/Stop-EC2Instance.md "../../../powershell/latest/reference/items/Stop-EC2Instance.md") (AWS Tools for Windows PowerShell).

[Instance store-backed instance] You can't stop the instance to modify the
attribute. Instead, proceed to this procedure: [To enable
enhanced networking on Linux (instance store–backed instances)](#other-linux-enhanced-networking-ena-instance-store "#other-linux-enhanced-networking-ena-instance-store"). 8. From your local computer, enable the enhanced networking
`enaSupport` attribute using one of the following
commands:

    * [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md")
     (AWS CLI)



    ```
    aws ec2 modify-instance-attribute --instance-id `i-1234567890abcdef0` --ena-support
    ```
    * [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md")
     (Tools for Windows PowerShell)



    ```
    Edit-EC2InstanceAttribute -InstanceId `i-1234567890abcdef0` -EnaSupport $true
    ```

9. (Optional) Create an AMI from the instance, as described in [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md"). The AMI
   inherits the enhanced networking `enaSupport` attribute from the
   instance. Therefore, you can use this AMI to launch another instance with
   enhanced networking enabled by default.

If your instance operating system contains an
`/etc/udev/rules.d/70-persistent-net.rules` file,
you must delete it before creating the AMI. This file contains the MAC
address for the Ethernet adapter of the original instance. If another
instance boots with this file, the operating system will be unable to
find the device and `eth0` might fail, causing boot issues.
This file is regenerated at the next boot cycle, and any instances
launched from the AMI create their own version of the file. 10. From your local computer, start the instance using the Amazon EC2 console or
one of the following commands: [start-instances](../../../cli/latest/reference/ec2/start-instances.md "../../../cli/latest/reference/ec2/start-instances.md") (AWS CLI) or [Start-EC2Instance](../../../powershell/latest/reference/items/Start-EC2Instance.md "../../../powershell/latest/reference/items/Start-EC2Instance.md") (AWS Tools for Windows PowerShell). 11. (Optional) Connect to your instance and verify that the kernel driver is
installed.

If you are unable to connect to your instance after enabling
enhanced networking, see [Troubleshoot the ENA kernel driver on Linux](troubleshooting-ena.md "troubleshooting-ena.md").

###### To enable

enhanced networking on Linux (instance store–backed instances)

Follow the previous procedure until the step where you stop the instance.
Create a new AMI as described in [Create an Amazon S3-backed AMI](creating-an-ami-instance-store.md "creating-an-ami-instance-store.md"), making sure to enable the
enhanced networking attribute when you register the AMI.

- [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") (AWS CLI)

```
aws ec2 register-image --ena-support `...`
```

- [Register-EC2Image](../../../powershell/latest/reference/items/Register-EC2Image.md "../../../powershell/latest/reference/items/Register-EC2Image.md") (AWS Tools for Windows PowerShell)

```
**Register-EC2Image** -EnaSupport `...`
```

This method is for testing and feedback purposes only. It is not intended for use
with production deployments. For production deployments, see [Ubuntu](#enhanced-networking-ena-ubuntu "#enhanced-networking-ena-ubuntu").

###### Important

Using DKMS voids the support agreement for your subscription. It should not be
used for production deployments.

###### To enable enhanced networking with ENA on Ubuntu (EBS-backed

instances)

1. Follow steps 1 and 2 in [Ubuntu](#enhanced-networking-ena-ubuntu "#enhanced-networking-ena-ubuntu").
2. Install the `build-essential` packages to compile the
   kernel driver and the `dkms` package so that your
   `ena` kernel driver is rebuilt every time your kernel is
   updated.

```
`ubuntu:~$` sudo apt-get install -y build-essential dkms
```

3. Clone the source for the `ena` kernel driver on your instance
   from GitHub at [https://github.com/amzn/amzn-drivers](https://github.com/amzn/amzn-drivers "https://github.com/amzn/amzn-drivers").

```
`ubuntu:~$` git clone https://github.com/amzn/amzn-drivers
```

4. Move the `amzn-drivers` package to the
   `/usr/src/` directory so DKMS can find it and build
   it for each kernel update. Append the version number (you can find the
   current version number in the release notes) of the source code to the
   directory name. For example, version `1.0.0` is shown in
   the following example.

```
`ubuntu:~$` sudo mv amzn-drivers /usr/src/amzn-drivers-1.0.0
```

5. Create the DKMS configuration file with the following values, substituting
   your version of `ena`.

Create the file.

```
`ubuntu:~$` sudo touch /usr/src/amzn-drivers-1.0.0/dkms.conf
```

Edit the file and add the following values.

```
`ubuntu:~$` sudo vim /usr/src/amzn-drivers-1.0.0/dkms.conf
PACKAGE_NAME="ena"
PACKAGE_VERSION="1.0.0"
CLEAN="make -C kernel/linux/ena clean"
MAKE="make -C kernel/linux/ena/ BUILD_KERNEL=${kernelver}"
BUILT_MODULE_NAME[0]="ena"
BUILT_MODULE_LOCATION="kernel/linux/ena"
DEST_MODULE_LOCATION[0]="/updates"
DEST_MODULE_NAME[0]="ena"
AUTOINSTALL="yes"
```

6. Add, build, and install the `ena` kernel driver on your
   instance using DKMS.

Add the kernel driver to DKMS.

```
`ubuntu:~$` sudo dkms add -m amzn-drivers -v 1.0.0
```

Build the kernel driver using the **dkms** command.

```
`ubuntu:~$` sudo dkms build -m amzn-drivers -v 1.0.0
```

Install the kernel driver using **dkms**.

```
`ubuntu:~$` sudo dkms install -m amzn-drivers -v 1.0.0
```

7. Rebuild `initramfs` so the correct kernel driver is loaded at
   boot time.

```
`ubuntu:~$` sudo update-initramfs -u -k all
```

8. Verify that the `ena` kernel driver is installed using the
   modinfo ena command from [Test whether enhanced networking is enabled](test-enhanced-networking-ena.md "test-enhanced-networking-ena.md").

```
`ubuntu:~$` modinfo ena
filename:	   /lib/modules/3.13.0-74-generic/updates/dkms/ena.ko
version:		1.0.0
license:		GPL
description:	Elastic Network Adapter (ENA)
author:		 Amazon.com, Inc. or its affiliates
srcversion:	 9693C876C54CA64AE48F0CA
alias:		  pci:v00001D0Fd0000EC21sv*sd*bc*sc*i*
alias:		  pci:v00001D0Fd0000EC20sv*sd*bc*sc*i*
alias:		  pci:v00001D0Fd00001EC2sv*sd*bc*sc*i*
alias:		  pci:v00001D0Fd00000EC2sv*sd*bc*sc*i*
depends:
vermagic:	   3.13.0-74-generic SMP mod_unload modversions
parm:		   debug:Debug level (0=none,...,16=all) (int)
parm:		   push_mode:Descriptor / header push mode (0=automatic,1=disable,3=enable)
		  0 - Automatically choose according to device capability (default)
		  1 - Don't push anything to device memory
		  3 - Push descriptors and header buffer to device memory (int)
parm:		   enable_wd:Enable keepalive watchdog (0=disable,1=enable,default=1) (int)
parm:		   enable_missing_tx_detection:Enable missing Tx completions. (default=1) (int)
parm:		   numa_node_override_array:Numa node override map
(array of int)
parm:		   numa_node_override:Enable/Disable numa node override (0=disable)
(int)
```

9. Continue with Step 3 in [Ubuntu](#enhanced-networking-ena-ubuntu "#enhanced-networking-ena-ubuntu").
   If you launched your instance and it does not have enhanced networking enabled
   already, you must download and install the required network adapter driver on your
   instance, and then set the `enaSupport` instance attribute to activate
   enhanced networking.

###### To enable enhanced networking

1. Connect to your instance and log in as the local administrator.
2. [Windows Server 2016 and 2019 only] Run the following EC2Launch
   PowerShell script to configure the instance after the driver is
   installed.

```
`PS C:\>` C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeInstance.ps1 -Schedule
```

3.  From the instance, install the driver as follows:
    1. [Download](https://s3.amazonaws.com/ec2-windows-drivers-downloads/ENA/Latest/AwsEnaNetworkDriver.zip "https://s3.amazonaws.com/ec2-windows-drivers-downloads/ENA/Latest/AwsEnaNetworkDriver.zip") the latest driver to the instance.
    2. Extract the zip archive.
    3. Install the driver by running the `install.ps1`
       PowerShell script.

    ###### Note

    If you get an execution policy error, set the policy to
    `Unrestricted` (by default it is set to
    `Restricted` or `RemoteSigned`). In a
    command line, run `Set-ExecutionPolicy -ExecutionPolicy
 Unrestricted`, and then run the
    `install.ps1` PowerShell script
    again.

4.  From your local computer, stop the instance using the Amazon EC2 console or one
    of the following commands: [stop-instances](../../../cli/latest/reference/ec2/stop-instances.md "../../../cli/latest/reference/ec2/stop-instances.md") (AWS CLI) or [Stop-EC2Instance](../../../powershell/latest/reference/items/Stop-EC2Instance.md "../../../powershell/latest/reference/items/Stop-EC2Instance.md") (AWS Tools for Windows PowerShell).
5.  Enable ENA support on your instance as follows:
    1.  From your local computer, check the EC2 instance ENA support
        attribute on your instance by running one of the following commands.
        If the attribute is not enabled, the output will be "[]" or blank.
        `EnaSupport` is set to `false` by
        default.
        - [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md")
          (AWS CLI)

        ```
        aws ec2 describe-instances --instance-ids `i-1234567890abcdef0` --query "Reservations[].Instances[].EnaSupport"
        ```

        - [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md")
          (Tools for Windows PowerShell)

        ```
        (Get-EC2Instance -InstanceId `i-1234567890abcdef0`).Instances.EnaSupport
        ```

    2.  To enable ENA support, run one of the following commands:

            * [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md")
             (AWS CLI)



            ```
            aws ec2 modify-instance-attribute --instance-id `i-1234567890abcdef0` --ena-support
            ```
            * [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md")
             (AWS Tools for Windows PowerShell)



            ```
            Edit-EC2InstanceAttribute -InstanceId `i-1234567890abcdef0` -EnaSupport $true
            ```

        If you encounter problems when you restart the instance, you can
        also disable ENA support using one of the following commands:

            * [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md")
             (AWS CLI)



            ```
            aws ec2 modify-instance-attribute --instance-id `i-1234567890abcdef0` --no-ena-support
            ```
            * [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md")
             (AWS Tools for Windows PowerShell)



            ```
            Edit-EC2InstanceAttribute -InstanceId `i-1234567890abcdef0` -EnaSupport $false
            ```

    3.  Verify that the attribute has been set to `true` using
        **describe-instances** or
        **Get-EC2Instance** as shown previously. You
        should now see the following output:

    ```
    [
    	true
    ]
    ```

6.  From your local computer, start the instance using the Amazon EC2 console or
    one of the following commands: [start-instances](../../../cli/latest/reference/ec2/start-instances.md "../../../cli/latest/reference/ec2/start-instances.md") (AWS CLI) or [Start-EC2Instance](../../../powershell/latest/reference/items/Start-EC2Instance.md "../../../powershell/latest/reference/items/Start-EC2Instance.md") (AWS Tools for Windows PowerShell).
7.  On the instance, validate that the ENA driver is installed and enabled as
    follows:
    1. Right-click the network icon and choose **Open Network and
       Sharing Center**.
    2. Choose the Ethernet adapter (for example, **Ethernet
       2**).
    3. Choose **Details**. For **Network
       Connection Details**, check that
       **Description** is **Amazon Elastic
       Network Adapter**.

8.  (Optional) Create an AMI from the instance. The AMI inherits the
    `enaSupport` attribute from the instance. Therefore, you can
    use this AMI to launch another instance with ENA enabled by default.
