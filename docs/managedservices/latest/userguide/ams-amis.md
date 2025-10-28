# AMS Amazon Machine Images (AMIs)

AMS produces updated Amazon Machine Images (AMIs) every month for AMS supported operating systems.
In addition, AMS also produces security enhanced images (AMIs) based on CIS Level 1 benchmark for a subset of
[AMS's supported operating systems](supported-configs.md "supported-configs.md").
To find out which operating systems have a security enhanced image available,
see the AMS Security User Guide, which is available through AWS Artifact -> Reports page (find the **Reports** option in the left navigation pane)
filtered for AWS Managed Services. To access AWS Artifact, can contact your CSDM for instructions or go to
[Getting Started with AWS Artifact](https://aws.amazon.com/artifact/getting-started "https://aws.amazon.com/artifact/getting-started").

To receive alerts when new AMS AMIs are released, you can
subscribe to an Amazon Simple Notification Service (Amazon SNS) notification topic called "AMS AMI". For details, see
[AMS AMI notifications with SNS](ams-ami-notifications.md "ams-ami-notifications.md").

The AMS AMI naming convention is:
`customer-ams-<operating system>-<release date> - <version>`.
(for example, `customer-ams-rhel6-2018.11-3`)

Only use AMS AMIs that start with `customer`.

AMS recommends always using the most recent AMI. You can find the most recent AMIs by either:

- Looking in the AMS console, on the **AMIs** page.
- Viewing the latest AMS AMI CSV file, available from your CSDM or through this ZIP file:
  [AMS 11.2024 AMI contents and CSV file in a ZIP](samples/AMIs.csv-and-notes.11.2024.md "samples/AMIs.csv-and-notes.11.2024.md").

For past AMI ZIP files, see the
[Doc History](doc-history-ug.md "doc-history-ug.md").

- Running this AMS `SKMS` command (AMS SKMS SDK required):

```
aws amsskms list-amis --vpc-id `VPC_ID` --query "Amis.sort_by(@,&Name)[? starts_with(Name,'customer')].[Name,AmiId,CreationTime]" --output table
```

**AMS AMI content added to base AWS AMIs, by operating system (OS)**

- Linux AMIs:
  - [AWS CLI Tools](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/")
  - [NTP](http://www.ntp.org/documentation.html "http://www.ntp.org/documentation.html")
  - [Trend Micro Endpoint Protection Service Agent](https://www.trendmicro.com/en_us/business.html "https://www.trendmicro.com/en_us/business.html")
  - [Code Deploy](https://github.com/aws/aws-codedeploy-agent "https://github.com/aws/aws-codedeploy-agent")
  - [PBIS / Beyond Trust AD Bridge](https://www.beyondtrust.com/products/active-directory-bridge "https://www.beyondtrust.com/products/active-directory-bridge")
  - [SSM Agent](https://github.com/aws/amazon-ssm-agent "https://github.com/aws/amazon-ssm-agent")
  - Yum Upgrade for critical patches
  - AMS custom scripts / management software (controlling boot, AD join, monitoring, security, and logging)

- Windows Server AMIs:

      + [Microsoft .NET Framework 4.5](https://www.microsoft.com/en-us/download/details.aspx?id=30653 "https://www.microsoft.com/en-us/download/details.aspx?id=30653")
      + [PowerShell 5.1](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1 "https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1")
      + [AWS Tools for Windows PowerShell](https://aws.amazon.com/powershell/ "https://aws.amazon.com/powershell/")
      + AMS PowerShell Modules controlling boot, AD join, monitoring, security, and logging
      + [Trend Micro Endpoint Protection Service Agent](https://www.trendmicro.com/en_us/business.html "https://www.trendmicro.com/en_us/business.html")
      + [SSM Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md")
      + [CloudWatch Agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md")
      + EC2Config service (through Windows Server 2012 R2)
      + EC2Launch (Windows Server 2016 and Windows Server 2019)
      + EC2LaunchV2 (Windows Server 2022 and later)

  **Linux-based AMIs**:

- Amazon Linux 2023 (Latest Minor Release) (Minimal AMI not supported)
- Amazon Linux 2 (Latest Minor Release)
- Amazon Linux 2 (ARM64)
- Red Hat Enterprise 7 (Latest Minor Release)
- Red Hat Enterprise 8 (Latest Minor Release)
- Red Hat Enterprise 9 (Latest Minor Release)
- SUSE Linux Enterprise Server 15 SP6
- Ubuntu Linux 18.04
- Ubuntu Linux 20.04
- Ubuntu Linux 22.04
- Ubuntu Linux 24.04
- Amazon Linux: For product overview, pricing information, usage information, and support information, see
  [Amazon Linux AMI (HVM / 64-bit)](https://aws.amazon.com/marketplace/pp/B00CIYTQTC "https://aws.amazon.com/marketplace/pp/B00CIYTQTC")
  and [Amazon Linux 2](https://aws.amazon.com/amazon-linux-2/ "https://aws.amazon.com/amazon-linux-2/").

For more information, see
[Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/ "https://aws.amazon.com/amazon-linux-2/faqs/").

- RedHat Enterprise Linux (RHEL): For product overview, pricing information, usage information, and support information, see
  [Red Hat Enterprise Linux (RHEL) 7 (HVM)](https://aws.amazon.com/marketplace/pp/B00KWBZVK6/ref=ptnr_catgtm_centos "https://aws.amazon.com/marketplace/pp/B00KWBZVK6/ref=ptnr_catgtm_centos").
- Ubuntu Linux 18.04: For product overview, pricing information, usage information, and support information, see
  [Ubuntu 18.04 LTS - Bionic](https://aws.amazon.com/marketplace/pp/prodview-pkjqrkcfgcaog "https://aws.amazon.com/marketplace/pp/prodview-pkjqrkcfgcaog").
- SUSE Linux Enterprise Server for SAP applications 15 SP6:

      + Run the following steps once per account:




      	1. Navigate to the **AWS Marketplace**.
      	2. Search for the SUSE 15 SAP product.
      	3. Choose **Continue to subscribe**.
      	4. Choose **Accept terms**.
      + Complete the following steps **every time**
       you need to launch a new **SUSE Linux Enterprise Server for SAP Applications 15 SP6** instance:




      	1. Note the AMI ID for the subscribed **SUSE Linux Enterprise Server for SAP Applications 15** AMI.
      	2. Create a Deployment | Advanced stack components | EC2 stack | Create change type ct-14027q0sjyt1h RFC. Replace `InstanceAmiId` with the AWS Marketplace AMI ID that you subscribed to.

  **Windows-based AMIs**:

Microsoft Windows Server (2016, 2019 and 2022), based on latest Windows AMIs.

For examples of creating AMIs, see
[Create AMI](../ctref/ex-ami-create-col.md "../ctref/ex-ami-create-col.md").

**Offboarding AMS AMIs**:

AMS does not unshare any AMIs from you during offboarding to avoid impact for any of your depedencies. If you want to remove AMS AMIs from
your account, you can use the `cancel-image-launch-permission` API to hide specific AMIs. For example, you can use the script below to hide all of the AMS AMIs
that were shared with your account earlier:

```
for ami in $(aws ec2 describe-images --executable-users self --owners 027415890775 --query 'Images[].ImageId' --output text) ;
    do
    aws ec2 cancel-image-launch-permission --image-id $ami ;
    done
```

You must have the AWS CLI v2 installed for the script to execute without any errors. For AWS CLI installation steps, see
[Installing or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
For details on the `cancel-image-launch-permission` command, see
[`cancel-image-launch-permission`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-image-launch-permission.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-image-launch-permission.html").
