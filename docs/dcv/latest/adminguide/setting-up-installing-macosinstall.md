# Installing the Amazon DCV Server on Amazon EC2 Mac instances

You can use an installation wizard to install the Amazon DCV server on an Amazon EC2 Mac instance.
To install with the installation wizard, you need to have [interactive GUI access](../../../AWSEC2/latest/UserGuide/connect-to-mac-instance.md#mac-instance-vnc "../../../AWSEC2/latest/UserGuide/connect-to-mac-instance.md#mac-instance-vnc").
The wizard guides you through a series of steps that show how to customize your Amazon DCV server
installation. Alternatively, you can use the command line to perform an unattended
installation. This uses default settings to automate the installation procedure.
To perform unattended installations, [System Integrity Protection (SIP)
must be disabled](../../../AWSEC2/latest/UserGuide/mac-sip-settings.md "../../../AWSEC2/latest/UserGuide/mac-sip-settings.md").

###### Note

Amazon DCV server for macOS is only supported on Amazon EC2 Apple silicon instances.

###### Contents

- [Using an unattended
  installation](setting-up-installing-macosinstall.md#setting-up-installing-windows-unattended "setting-up-installing-macosinstall.md#setting-up-installing-windows-unattended")
- [Using the wizard](setting-up-installing-macosinstall.md#setting-up-installing-windows-wizard-mac "setting-up-installing-macosinstall.md#setting-up-installing-windows-wizard-mac")

## Using an unattended

installation

Amazon DCV can install and activate the server software automatically. This is called
an "unattended installation". By default, an unattended installation enables Amazon DCV server auto-start.
An example Amazon Machine Image creation automation can be found in the aws-samples Github within
the [dcv-samples
repository](https://github.com/aws-samples/dcv-samples/tree/main/cdk/dcv-mac-image-automation "https://github.com/aws-samples/dcv-samples/tree/main/cdk/dcv-mac-image-automation").

###### To install the Amazon DCV server on Amazon EC2 Mac instance using an unattended installation

1. Launch and [connect](../../../AWSEC2/latest/UserGuide/connect-to-mac-instance.md#mac-instance-ssh "../../../AWSEC2/latest/UserGuide/connect-to-mac-instance.md#mac-instance-ssh") to the server that you intend to install the Amazon DCV server
   on.
2. Confirm [System Integrity Protection (SIP) is disabled](../../../AWSEC2/latest/UserGuide/mac-sip-settings.md#mac-sip-check-settings "../../../AWSEC2/latest/UserGuide/mac-sip-settings.md#mac-sip-check-settings").
3. Download the Amazon DCV server installer from the [Amazon DCV](http://download.amazondcv.com "http://download.amazondcv.com") website.

###### Note

The Amazon DCV server is available only in a 64-bit version and supported on 64-bit ARM Amazon EC2 instances. 4. Download the packages from the [Amazon DCV download website](http://download.amazondcv.com "http://download.amazondcv.com").

```
`$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Servers/nice-dcv-server-2025.0-20103-macos-arm64.dist.pkg
```

5. Run the unattended installer with the following command:

```
`$` sudo installer -pkg nice-dcv-server-2025.0-`version_number`-macos-arm64.dist.pkg -target /
```

## Using the wizard

Use the Amazon DCV server installation wizard for a guided installation.

###### To install the Amazon DCV server on Amazon EC2 Mac instances using the wizard

1. Launch and [connect](../../../AWSEC2/latest/UserGuide/connect-to-mac-instance.md#mac-instance-vnc "../../../AWSEC2/latest/UserGuide/connect-to-mac-instance.md#mac-instance-vnc") to the server on which to install the Amazon DCV server.
2. Download the Amazon DCV server installer from the [Amazon DCV](http://download.amazondcv.com "http://download.amazondcv.com") website.

###### Note

The Amazon DCV server is available only in a 64-bit version and supported on 64-bit ARM Amazon EC2 instances.

###### Tip

The [latest packages](http://download.amazondcv.com/latest.html "http://download.amazondcv.com/latest.html") page of the download website contains links that always point to the newest available version.
You can use these links to automatically retrieve the newest Amazon DCV packages. 3. Run `nice-dcv-server-2025.0-`version_number`-macos-arm64.dist.pkg`. 4. On the Introduction screen, choose **Continue**. 5. On the Installation Type screen, check the package check boxes, and then choose
**Continue**. 6. Choose **Install**.
