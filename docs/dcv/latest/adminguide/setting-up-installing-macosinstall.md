

# Installing the Amazon DCV Server on Amazon EC2 Mac instances
<a name="setting-up-installing-macosinstall"></a>

You can use an installation wizard to install the Amazon DCV server on an Amazon EC2 Mac instance. To install with the installation wizard, you need to have [ interactive GUI access](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-mac-instance.html#mac-instance-vnc). The wizard guides you through a series of steps that show how to customize your Amazon DCV server installation. Alternatively, you can use the command line to perform an unattended installation. This uses default settings to automate the installation procedure. To perform unattended installations, [System Integrity Protection (SIP) must be disabled](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mac-sip-settings.html). 

**Note**  
Amazon DCV server for macOS is only supported on Amazon EC2 Apple silicon instances.

**Contents**
+ [Using an unattended installation](#setting-up-installing-windows-unattended)
+ [Using the wizard](#setting-up-installing-windows-wizard-mac)
+ [Configuring Privacy and Security settings](#setting-up-macos-privacy-settings)

## Using an unattended installation
<a name="setting-up-installing-windows-unattended"></a>

Amazon DCV can install and activate the server software automatically. This is called an "unattended installation". By default, an unattended installation enables Amazon DCV server auto-start. An example Amazon Machine Image creation automation can be found in the aws-samples Github within the [dcv-samples repository](https://github.com/aws-samples/dcv-samples/tree/main/cdk/dcv-mac-image-automation).

**To install the Amazon DCV server on Amazon EC2 Mac instance using an unattended installation**

1. Launch and [ connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-mac-instance.html#mac-instance-ssh) to the server that you intend to install the Amazon DCV server on.

1. Confirm [ System Integrity Protection (SIP) is disabled](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mac-sip-settings.html#mac-sip-check-settings).

1. Download the Amazon DCV server installer from the [Amazon DCV](http://download.amazondcv.com) website.
**Note**  
The Amazon DCV server is available only in a 64-bit version and supported on 64-bit ARM Amazon EC2 instances.

1. Download the packages from the [Amazon DCV download website](http://download.amazondcv.com).

   ```
   $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-server-macos-arm64.dist.pkg
   ```

1. Run the unattended installer with the following command:

   ```
   $ sudo installer -pkg nice-dcv-server-2025.0-{{version_number}}-macos-arm64.dist.pkg -target /
   ```

## Using the wizard
<a name="setting-up-installing-windows-wizard-mac"></a>

Use the Amazon DCV server installation wizard for a guided installation.

**To install the Amazon DCV server on Amazon EC2 Mac instances using the wizard**

1. Launch and [ connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-mac-instance.html#mac-instance-vnc) to the server on which to install the Amazon DCV server.

1. Download the Amazon DCV server installer from the [Amazon DCV](http://download.amazondcv.com) website.
**Note**  
The Amazon DCV server is available only in a 64-bit version and supported on 64-bit ARM Amazon EC2 instances.
**Tip**  
The [latest packages](http://download.amazondcv.com/latest.html) page of the download website contains links that point to the newest available version. You can use these links to automatically retrieve the newest Amazon DCV packages.

1. Run `nice-dcv-server-2025.0-{{version_number}}-macos-arm64.dist.pkg`. 

1. On the Introduction screen, choose **Continue**.

1. On the Installation Type screen, check the package check boxes, and then choose **Continue**.

1. Choose **Install**.

1. Click **Allow** when prompted during installation.

## Configuring Privacy and Security settings
<a name="setting-up-macos-privacy-settings"></a>

After installing the Amazon DCV server, you must configure macOS Privacy and Security settings to allow Amazon DCV to access system features.

**To configure Privacy and Security settings for Amazon DCV**

1. Open **System Settings** and navigate to **Privacy and Security**.

1. Under **Accessibility**, select the checkbox next to `DCV Server` to allow access. If `DCV Server` is not listed, drag `/Applications/DCV Server.app` to the allowed list and then select the checkbox.

1. Under **Screen & System Audio Recording**, select the checkbox next to `DCV Server` to allow access. If `DCV Server` is not listed, drag `/Applications/DCV Server.app` to the allowed list and then select the checkbox

1. Reboot the machine to apply the changes:

   ```
   $ sudo reboot
   ```

1. After reboot, ensure you have a valid Amazon DCV license. For licensing information, see [Step 2: License the Amazon DCV Server](setting-up-license.md).

1. Reconnect using VNC and create a Amazon DCV console session:

   ```
   $ sudo dcv create-session --type console --owner ec2-user console
   ```

1. Click **Allow** when prompted for Microphone access.

1. Click **Allow** when prompted for `dcvagentlauncher` access.

1. When prompted for **Remote Control access**, click **Open System Settings**, enable the setting, and choose **Quit & Reopen**.

1. You can now connect using the Amazon DCV Client.