

# Conversion prerequisites for License Manager license types
<a name="conversion-prerequisites"></a>

To convert license types with License Manager, there are general and operating system specific prerequisites.

**Topics**
+ [General](#conversion-prerequisites-general)
+ [Windows](#conversion-prerequisites-windows)
+ [Linux](#conversion-prerequisites-linux)

## General
<a name="conversion-prerequisites-general"></a>

You must meet the following general prerequisites before performing a license type conversion:
+ Your AWS account must be onboarded to License Manager. See [Get started with License Manager](getting-started.md).
+ The target instance must run on AWS. On-premises instances are not supported.
+ The target instance must be in the stopped state before you convert the license type. For more information, see [Stop and start your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html) in the *Amazon EC2 User Guide*.
+ If stop protection is enabled on the target instance, the conversion process will fail. For more information, see [Troubleshooting license type conversion in License Manager](conversion-troubleshooting.md).
+ The target instance must be configured with AWS Systems Manager Inventory. For more information, see [Setting up Systems Manager for EC2 instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-ec2.html) and [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) in the *AWS Systems Manager User Guide*.
+ Your user or role must have the following permissions:
  + `ssm:GetInventory`
  + `ssm:StartAutomationExecution`
  + `ssm:GetAutomationExecution`
  + `ssm:SendCommand`
  + `ssm:GetCommandInvocation`
  + `ssm:DescribeInstanceInformation`
  + `ec2:DescribeImages`
  + `ec2:DescribeInstances`
  + `ec2:StartInstances`
  + `ec2:StopInstances`
  + `license-manager:CreateLicenseConversionTaskForResource`
  + `license-manager:GetLicenseConversionTask`
  + `license-manager:ListLicenseConversionTasks`
  + `license-manager:GetLicenseConfiguration`
  + `license-manager:ListUsageForLicenseConfiguration`
  + `license-manager:ListLicenseSpecificationsForResource`
  + `license-manager:ListAssociationsForLicenseConfiguration`
  + `license-manager:ListLicenseConfigurations`

  For more information about Systems Manager Inventory, see [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html). 

## Windows
<a name="conversion-prerequisites-windows"></a>

Windows instances must meet the following prerequisites:
+ Instances that were originally launched from an Amazon provided Amazon Machine Image (AMI) are not eligible for license type conversion to BYOL. The original Amazon EC2 instance must be launched from your own virtual machine (VM) image. For more information about converting a VM to Amazon EC2, see [VM Import/Export](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html#import-vm-image). 
+ To change your SQL Server license to BYOL, SQL Server must have been installed using your own media.

## Linux
<a name="conversion-prerequisites-linux"></a>

Linux instances must meet the following prerequisites:

------
#### [ RHEL ]
+ If converting from AWS-provided subscriptions to subscriptions sold by Red Hat as an AMI listing on AWS Marketplace, you must first subscribe to the Marketplace AMI listing from Red Hat before initiating the license conversion.
+ For transitions from AWS-provided subscriptions to the Red Hat Subscriptions SaaS listing on AWS Marketplace you'll need to purchase subscriptions from Red Hat prior to conversion.

------
#### [ RHEL for SAP ]
+ For RHEL for SAP and Update Services conversions, instances must be launched from AWS Marketplace with a RunInstance:0010 usage operation and an attached AWS Marketplace product code.
+ If converting from AWS-provided subscriptions to subscriptions sold by Red Hat as an AMI listing on AWS Marketplace, you must first subscribe to the Marketplace AMI listing from Red Hat before initiating the license conversion.
+ For transitions from AWS-provided subscriptions to the Red Hat Subscriptions SaaS listing on AWS Marketplace you'll need to purchase subscriptions from Red Hat prior to conversion.

------
#### [ Ubuntu ]
+ Instances must be running Ubuntu LTS.
+ The Ubuntu Pro Client must be installed in your Ubuntu operating system.
  + Run the following command to confirm if the Ubuntu Pro Client is installed:

    ```
    pro --version
    ```
  + If the command is not found, or the version needs to be updated, run the following command to install the Ubuntu Pro Client:

    ```
    apt-get update && apt-get dist-upgrade
    ```
+ Instances must be able to reach multiple endpoints to activate their Ubuntu Pro subscription and receive updates. You must allow outbound traffic from your instance over TCP port 443 to reach the following endpoints: 
  + **contracts.canonical.com** – Used for Ubuntu Pro activation.
  + **esm.ubuntu.com** – Used for APT repository access for most services.
  + **api.snapcraft.io** – Used for installing and running snaps.
  + **dashboard.snapcraft.io** – Used for installing and running snaps.
  + **login.ubuntu.com** – Used for installing and running snaps.
  + **cloudfront.cdn.snapcraftcontent.com** – Used for downloading from content development networks (CDNs).
  + **livepatch.canonical.com** – Used for downloading patches from the Livepatch server.

  For more information, see [Ubuntu Pro Client network requirements](https://canonical-ubuntu-pro-client.readthedocs-hosted.com/en/latest/references/network_requirements/) in the Ubuntu Pro Client documentation and [Network requirements](https://snapcraft.io/docs/network-requirements) in the Canonical Snapcraft documentation.

------