# Install the ENA driver on EC2 Windows instances

If your instance isn't based on one of the latest Windows Amazon Machine Images
(AMIs) that Amazon provides, use the following procedure to install the current
ENA driver on your instance. You should perform this update at a time when it’s
convenient to reboot your instance. If the install script doesn’t automatically reboot
your instance, we recommend that you reboot the instance as the final step.

If you use an instance store volume to store data while the instance is running,
that data is erased when you stop the instance. Before you stop your instance, verify
that you've copied any data that you need from your instance store volumes to persistent
storage, such as Amazon EBS or Amazon S3.

## Prerequisites

To install or upgrade the ENA driver, your Windows instance must meet the following
prerequisites:

- PowerShell version 3.0 or later is installed.
- The commands shown in this section must run in the 64-bit version of
  PowerShell. Do not use the `x86` version of PowerShell. That is
  the 32-bit version of the shell, and is not supported for these commands.

## Step 1: Back up your data

We recommend that you create a backup AMI, in case you're not able to roll back
your changes through the **Device Manager**. To create a backup AMI
with the AWS Management Console, follow these steps:

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance that requires the driver upgrade, and choose
   **Stop instance** from the **Instance
   state** menu.
4. After the instance is stopped, select the instance again. To create
   your backup, choose **Image and templates** from the
   **Actions** menu, then choose
   **Create image**.
5. To restart your instance, choose **Start instance**
   from the **Instance state** menu.

## Step 2: Install or upgrade your

ENA driver

You can install or upgrade your ENA driver with AWS Systems Manager Distributor, or with
PowerShell cmdlets. For further instructions, select the tab that matches the method
that you want to use.

Systems Manager Distributor
You can use the Systems Manager Distributor feature to deploy packages to your
Systems Manager managed nodes. With Systems Manager Distributor, you can install the ENA driver
package once, or with scheduled updates. For more information about how to
install the ENA driver package (`AwsEnaNetworkDriver`)
with Systems Manager Distributor, see [Install
or update packages](../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md "../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md") in the _AWS Systems Manager User Guide_.

PowerShell
This section covers how to download and install ENA driver packages on
your instance with PowerShell cmdlets.

###### Option 1: Download and extract the latest version

1. Connect to your instance and log in as the local administrator.
2. Use the **invoke-webrequest** cmdlet to download the latest driver package:

```
`PS C:\>` `invoke-webrequest https://ec2-windows-drivers-downloads.s3.amazonaws.com/ENA/Latest/AwsEnaNetworkDriver.zip -outfile `$env:USERPROFILE\AwsEnaNetworkDriver.zip``
```

###### Note

If you receive an error when downloading the file, and you
are using Windows Server 2016 or earlier, TLS 1.2 might need
to be enabled for your PowerShell terminal. You can enable
TLS 1.2 for the current PowerShell session with the
following command and then try again:

```
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

Alternatively, you can download the latest driver package from a browser window on your instance. 3. Use the **expand-archive** cmdlet to extract the zip archive
that you downloaded to your instance:

```
`PS C:\>` `expand-archive `$env:userprofile\AwsEnaNetworkDriver.zip` -DestinationPath `$env:userprofile\AwsEnaNetworkDriver``
```

###### Option 2: Download and extract a specific version

1. Connect to your instance and log in as the local administrator.
2. Download the ENA driver package for the specific version you want
   from the version link in the [ENA Windows driver version history](ena-driver-releases-windows.md#ena-win-driver-release-history "ena-driver-releases-windows.md#ena-win-driver-release-history") table.
3. Extract the zip archive to your instance.

###### Install the ENA driver with PowerShell

The install steps are the same whether you've downloaded the latest driver or
a specific version. To install the ENA driver, follow these steps.

1. To install the driver, run the `install.ps1` PowerShell
   script from the `AwsEnaNetworkDriver` directory on your instance.
   If you get an error, make sure that you’re using PowerShell 3.0 or later.
2. If the installer doesn’t automatically reboot your instance, run the
   **Restart-Computer** PowerShell cmdlet.

```
`PS C:\>` `Restart-Computer`
```

## Step 3 (optional): Verify the

ENA driver version after installation

To ensure that the ENA driver package was successfully installed on your instance,
you can verify the new version as follows:

1. Connect to your instance and log in as the local administrator.
2. To open the Windows Device Manager, enter `devmgmt.msc` in the
   **Run** box.
3. Choose **OK**. This opens the Device Manager window.
4. Select the arrow to the left of **Network adapters**
   to expand the list.
5. Choose the name, or open the context menu for the **Amazon Elastic Network
   Adapter**, and then choose
   **Properties**. This opens the **Amazon Elastic Network Adapter Properties**
   dialog.

###### Note

ENA adapters all use the same driver. If you have multiple ENA adapters, you can
select any one of them to update the driver for all of the ENA adapters. 6. To verify the current version that's installed, open the **Driver**
tab and check the **Driver Version**. If the current version doesn't
match your target version, see [Troubleshoot the Elastic Network Adapter Windows driver](troubleshoot-ena-driver.md "troubleshoot-ena-driver.md").

## Roll back an ENA driver installation

If anything goes wrong with the installation, you might need to roll back the
driver. Follow these steps to roll back to the previous version of the ENA driver that
was installed on your instance.

1. Connect to your instance and log in as the local administrator.
2. To open the Windows Device Manager, enter `devmgmt.msc` in the
   **Run** box.
3. Choose **OK**. This opens the Device Manager window.
4. Select the arrow to the left of **Network adapters**
   to expand the list.
5. Choose the name, or open the context menu for the **Amazon Elastic Network
   Adapter**, and then choose
   **Properties**. This opens the **Amazon Elastic Network Adapter Properties**
   dialog.

###### Note

ENA adapters all use the same driver. If you have multiple ENA adapters, you can
select any one of them to update the driver for all of the ENA adapters. 6. To roll back the driver, open the **Driver** tab and choose
**Roll Back Driver**. This opens the **Driver Package
rollback** window.

###### Note

If the **Driver** tab doesn't show the **Roll Back
Driver** action, or if the action is unavailable, it means that the
[Driver Store](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/driver-store "https://learn.microsoft.com/en-us/windows-hardware/drivers/install/driver-store")
on your instance doesn't contain the previously installed driver
package. To troubleshoot this issue, see [Troubleshooting scenarios](troubleshoot-ena-driver.md#ts-ena-drv-scenarios "troubleshoot-ena-driver.md#ts-ena-drv-scenarios"), and expand the **Unexpected
ENA driver version installed** section. For more information
about the device driver package selection process, see
[How
Windows selects a driver package for a device](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/how-windows-selects-a-driver-for-a-device "https://learn.microsoft.com/en-us/windows-hardware/drivers/install/how-windows-selects-a-driver-for-a-device")
on the _Microsoft documentation website_.
