

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AMS Amazon Machine Images (AMIs)
<a name="ams-amis"></a>

AMS produces updated Amazon Machine Images (AMIs) every month for AMS supported operating systems. In addition, AMS also produces security enhanced images (AMIs) based on CIS Level 1 benchmark for a subset of [AMS's supported operating systems](https://docs.aws.amazon.com/managedservices/latest/userguide/supported-configs.html). To find out which operating systems have a security enhanced image available, see the AMS Security User Guide, which is available through AWS Artifact -> Reports page (find the **Reports** option in the left navigation pane) filtered for AWS Managed Services. To access AWS Artifact, can contact your CSDM for instructions or go to [Getting Started with AWS Artifact](https://aws.amazon.com/artifact/getting-started).

To receive alerts when new AMS AMIs are released, you can subscribe to an Amazon Simple Notification Service (Amazon SNS) notification topic called "AMS AMI". For details, see [AMS AMI notifications with SNS](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-ami-notifications.html).

The AMS AMI naming convention is: `customer-ams-<operating system>-<release date> - <version>`. (for example, `customer-ams-rhel6-2018.11-3`)

Only use AMS AMIs that start with `customer`.

AMS recommends always using the most recent AMI. You can find the most recent AMIs by either:
+ Looking in the AMS console, on the **AMIs** page.
+ Viewing the latest AMS AMI CSV file, available from your CSDM or through this ZIP file: [AMS 11.2024 AMI contents and CSV file in a ZIP](https://docs.aws.amazon.com/managedservices/latest/userguide/samples/AMIs.csv-and-notes.11.2024.zip).

  For past AMI ZIP files, see the [Doc History](https://docs.aws.amazon.com/managedservices/latest/userguide/doc-history-ug.html).
+ Running this AMS `SKMS` command (AMS SKMS SDK required):

  ```
  aws amsskms list-amis --vpc-id {{VPC_ID}} --query "Amis.sort_by(@,&Name)[? starts_with(Name,'customer')].[Name,AmiId,CreationTime]" --output table
  ```

**AMS AMI content added to base AWS AMIs, by operating system (OS)**
+ Linux AMIs:
  + [AWS CLI Tools](https://aws.amazon.com/cli/)
  + [NTP](http://www.ntp.org/documentation.html)
  + [Trend Micro Endpoint Protection Service Agent](https://www.trendmicro.com/en_us/business.html)
  + [Code Deploy](https://github.com/aws/aws-codedeploy-agent)
  + [PBIS Enterprise / Beyond Trust AD Bridge](https://www.beyondtrust.com/products/active-directory-bridge)
**Note**  
As of June 2022, BeyondTrust no longer supports PBIS Open. You can't use PBIS Open on AMIs that AMS supports after June 2022. If AMS supported your AMI before June 2022, you can continue to use PBIS Open at your own discretion.
  + [SSM Agent](https://github.com/aws/amazon-ssm-agent)
  + Yum Upgrade for critical patches
  + AMS custom scripts / management software (controlling boot, AD join, monitoring, security, and logging)
+ Windows Server AMIs:
  + [Microsoft .NET Framework 4.5](https://www.microsoft.com/en-us/download/details.aspx?id=30653)
  + [ PowerShell 5.1](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
  + [AWS Tools for Windows PowerShell](https://aws.amazon.com/powershell/)
  + AMS PowerShell Modules controlling boot, AD join, monitoring, security, and logging
  + [Trend Micro Endpoint Protection Service Agent](https://www.trendmicro.com/en_us/business.html)
  + [SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html)
  + [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
  + EC2Config service (through Windows Server 2012 R2)
  + EC2Launch (Windows Server 2016 and Windows Server 2019)
  + EC2LaunchV2 (Windows Server 2022 and later)

**Linux-based AMIs**:
+ Amazon Linux 2023 (Latest Minor Release) (Minimal AMI not supported)
+ Amazon Linux 2 (Latest Minor Release)
+ Amazon Linux 2 (ARM64)
+ Red Hat Enterprise 8 (Latest Minor Release)
+ Red Hat Enterprise 9 (Latest Minor Release)
+ SUSE Linux Enterprise Server 15 SP6
+ Ubuntu Linux 20.04
+ Ubuntu Linux 22.04
+ Ubuntu Linux 24.04
+ Amazon Linux: For product overview, pricing information, usage information, and support information, see [Amazon Linux 2](https://aws.amazon.com/amazon-linux-2/).

  For more information, see [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/).
+ SUSE Linux Enterprise Server for SAP applications 15 SP6:
  + Run the following steps once per account:

    1. Navigate to the **AWS Marketplace**.

    1. Search for the SUSE 15 SAP product.

    1. Choose **Continue to subscribe**.

    1. Choose **Accept terms**.
  + Complete the following steps **every time** you need to launch a new **SUSE Linux Enterprise Server for SAP Applications 15 SP6** instance:

    1. Note the AMI ID for the subscribed **SUSE Linux Enterprise Server for SAP Applications 15** AMI.

    1. Create a Deployment \| Advanced stack components \| EC2 stack \| Create change type ct-14027q0sjyt1h RFC. Replace {{InstanceAmiId}} with the AWS Marketplace AMI ID that you subscribed to.

**Windows-based AMIs**:

Microsoft Windows Server (2016, 2019, 2022, and 2025), based on latest Windows AMIs.

For examples of creating AMIs, see [Create AMI](https://docs.aws.amazon.com/managedservices/latest/ctref/ex-ami-create-col.html).

**Offboarding AMS AMIs**:

AMS does not unshare any AMIs from you during offboarding to avoid impact for any of your depedencies. If you want to remove AMS AMIs from your account, you can use the `cancel-image-launch-permission` API to hide specific AMIs. For example, you can use the script below to hide all of the AMS AMIs that were shared with your account earlier:

```
for ami in $(aws ec2 describe-images --executable-users self --owners 027415890775 --query 'Images[].ImageId' --output text) ; 
    do
    aws ec2 cancel-image-launch-permission --image-id $ami ; 
    done
```

You must have the AWS CLI v2 installed for the script to execute without any errors. For AWS CLI installation steps, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). For details on the `cancel-image-launch-permission` command, see [`cancel-image-launch-permission`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-image-launch-permission.html).