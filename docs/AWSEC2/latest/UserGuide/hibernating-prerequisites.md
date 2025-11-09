# Prerequisites for EC2 instance hibernation

You can enable hibernation support for an On-Demand Instance or a Spot Instance when you launch it. You
can't enable hibernation on an existing instance, whether it is running or stopped. For
more information, see [Enable instance
hibernation](enabling-hibernation.md "enabling-hibernation.md").

###### Requirements to hibernate an instance

- [AWS Regions](#hibernation-prereqs-regions "#hibernation-prereqs-regions")
- [AMIs](#hibernation-prereqs-supported-amis "#hibernation-prereqs-supported-amis")
- [Instance families](#hibernation-prereqs-supported-instance-families "#hibernation-prereqs-supported-instance-families")
- [Instance RAM size](#instance-ram-size "#instance-ram-size")
- [Root volume type](#hibernation-prereqs-root-volume-type "#hibernation-prereqs-root-volume-type")
- [Root volume size](#hibernation-prereqs-ebs-root-volume-size "#hibernation-prereqs-ebs-root-volume-size")
- [Root volume
  encryption](#hibernation-prereqs-ebs-root-volume-encryption "#hibernation-prereqs-ebs-root-volume-encryption")
- [EBS volume type](#hibernation-prereqs-ebs-volume-types "#hibernation-prereqs-ebs-volume-types")
- [Spot Instance requests](#hibernation-prereqs-spot-request "#hibernation-prereqs-spot-request")

## AWS Regions

You can use hibernation with instances in all AWS Regions.

## AMIs

You must use an HVM AMI that supports hibernation. The following AMIs support
hibernation:

###### AMIs for Intel and AMD instance types

- AL2023 AMI released 2023.09.20 or later ¹
- Amazon Linux 2 AMI released 2019.08.29 or later
- Amazon Linux AMI 2018.03 released 2018.11.16 or later
- CentOS version 8 AMI ² ([Additional configuration](hibernation-enabled-AMI.md#configure-centos-for-hibernation "hibernation-enabled-AMI.md#configure-centos-for-hibernation") is required)
- Fedora version 34 or later AMI ² ([Additional configuration](hibernation-enabled-AMI.md#configure-fedora-for-hibernation "hibernation-enabled-AMI.md#configure-fedora-for-hibernation") is required)
- Red Hat Enterprise Linux (RHEL) 9 AMI ² ([Additional
  configuration](hibernation-enabled-AMI.md#configure-RHEL-for-hibernation "hibernation-enabled-AMI.md#configure-RHEL-for-hibernation") is required)
- Red Hat Enterprise Linux (RHEL) 8 AMI ² ([Additional
  configuration](hibernation-enabled-AMI.md#configure-RHEL-for-hibernation "hibernation-enabled-AMI.md#configure-RHEL-for-hibernation") is required)
- Ubuntu 22.04.2 LTS (Jammy Jellyfish) AMI released with serial number 20230303 or later
  ³
- Ubuntu 20.04 LTS (Focal Fossa) AMI released with serial number 20210820 or later
  ³
- Ubuntu 18.04 LTS (Bionic Beaver) AMI released with serial number 20190722.1 or later
  ³ ⁵
- Ubuntu 16.04 LTS (Xenial Xerus) AMI ³ ⁴ ⁵ ([Additional
  configuration](hibernation-enabled-AMI.md#configure-ubuntu1604-for-hibernation "hibernation-enabled-AMI.md#configure-ubuntu1604-for-hibernation") is required)

###### AMIs for Graviton instance types

- AL2023 AMI (64-bit Arm) released 2024.07.01 or later ¹
- Amazon Linux 2 AMI (64-bit Arm) released 2024.06.20 or later
- Ubuntu 22.04.2 LTS (64-bit Arm) (Jammy Jellyfish) AMI released with serial number
  20240701 or later ³
- Ubuntu 20.04 LTS (64-bit Arm) (Focal Fossa) AMI released with serial number 20240701 or
  later ³

 

¹ For AL2023 minimal AMI, [additional configuration is required](hibernation-enabled-AMI.md#configure-AL2023-minimal-for-hibernation "hibernation-enabled-AMI.md#configure-AL2023-minimal-for-hibernation").

² For CentOS, Fedora, and Red Hat Enterprise Linux, hibernation is supported on
Nitro-based instances only.

³ We recommend disabling KASLR on instances with Ubuntu 22.04.2 LTS (Jammy
Jellyfish), Ubuntu 20.04 LTS (Focal Fossa), Ubuntu 18.04 LTS (Bionic
Beaver), and Ubuntu 16.04 LTS (Xenial Xerus). For more information, see
[Disable KASLR on an instance (Ubuntu
only)](hibernation-disable-kaslr.md "hibernation-disable-kaslr.md").

⁴ For the Ubuntu 16.04 LTS (Xenial Xerus) AMI, hibernation is not supported on
`t3.nano` instance types. No patch will be made available
because Ubuntu (Xenial Xerus) ended support in April 2021. If you want to
use `t3.nano` instance types, we recommend that you upgrade to
the Ubuntu 22.04.2 LTS (Jammy Jellyfish), Ubuntu 20.04 LTS (Focal Fossa)
AMI, or the Ubuntu 18.04 LTS (Bionic Beaver) AMI.

⁵ Support for Ubuntu 18.04 LTS (Bionic Beaver) and Ubuntu 16.04 LTS
(Xenial Xerus) has reached end of life.

To configure your own AMI to support hibernation, see [Configure a Linux AMI to support
hibernation](hibernation-enabled-AMI.md "hibernation-enabled-AMI.md").

Support for other versions of Ubuntu and other operating systems is coming
soon.

- Windows Server 2022 AMI released 2023.09.13 or later
- Windows Server 2019 AMI released 2019.09.11 or later
- Windows Server 2016 AMI released 2019.09.11 or later
- Windows Server 2012 R2 AMI released 2019.09.11 or later
- Windows Server 2012 AMI released 2019.09.11 or later

## Instance families

You must use an instance family that supports hibernation. However,
bare metal instances are not supported.

- General purpose: M3, M4, M5, M5a, M5ad, M5d, M6a, M6g, M6gd, M6i, M6id, M6idn, M6in, M7a, M7g, M7gd, M7i, M7i-flex, M8a, M8g, M8gd, M8i, M8i-flex, T2, T3, T3a, T4g
- Compute optimized: C3, C4, C5, C5d, C6a, C6g, C6gd, C6gn, C6i, C6id, C6in, C7a, C7g, C7gd, C7gn, C7i, C7i-flex, C8g, C8gd, C8gn, C8i, C8i-flex
- Memory optimized: R3, R4, R5, R5a, R5ad, R5d, R6a, R6g, R6gd, R6idn, R6in, R7a, R7g, R7gd, R7i, R7iz, R8a, R8g, R8gb, R8gd, R8gn, R8i, R8i-flex, X2gd
- Storage optimized: I3, I3en, I4g, I7i, I7ie, I8g, I8ge, Im4gn, Is4gen

Console

###### To get the instance types that support hibernation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instance Types**.
3. Add the filter **On-Demand Hibernation support = true**.
4. (Optional) Add filters to further scope to specific instance types of interest.

AWS CLI

###### To get the instance types that support hibernation

Use the [describe-instance-types](../../../cli/latest/reference/describe-instance-types.md "../../../cli/latest/reference/describe-instance-types.md") command. Note that the available
instance types vary by Region.

```
aws ec2 describe-instance-types \
    --filters Name=hibernation-supported,Values=true \
    --query "InstanceTypes[*].[InstanceType]" \
    --output text | sort
```

PowerShell

###### To get the instance types that support hibernation

Use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md") cmdlet. Note that the available
instance types vary by Region.

```
(Get-EC2InstanceType `
    -Filter @{Name="hibernation-supported"; Values="true"}).InstanceType | Sort-Object
```

## Instance RAM size

Linux instances – Must be less than 150 GiB.

Windows instances – Must be less than or equal to 16
GiB. For hibernating a T3 or T3a Windows instance, we recommend at least 1 GiB of
RAM.

## Root volume type

The root volume must be an EBS volume, not an instance store volume.

## Root volume size

The root volume must be large enough to store the RAM contents and accommodate
your expected usage, for example, OS or applications. If you enable hibernation,
space is allocated on the root volume at launch to store the RAM.

## Root volume

encryption

The root volume must be encrypted to ensure the protection of sensitive content
that is in memory at the time of hibernation. When RAM data is moved to the EBS root
volume, it is always encrypted. Encryption of the root volume is enforced at
instance launch.

Use one of the following three options to ensure that the root volume is an
encrypted EBS volume:

- **EBS encryption by default** – You
  can enable EBS encryption by default to ensure that all new EBS volumes
  created in your AWS account are encrypted. This way, you can enable
  hibernation for your instances without specifying encryption intent at
  instance launch. For more information, see [Enable encryption by default](../../../ebs/latest/userguide/encryption-by-default.md "../../../ebs/latest/userguide/encryption-by-default.md").
- **EBS "single-step" encryption** – You
  can launch encrypted EBS-backed EC2 instances from an unencrypted AMI and
  also enable hibernation at the same time. For more information, see [Use encryption with EBS-backed AMIs](AMIEncryption.md "AMIEncryption.md").
- **Encrypted AMI** – You can enable EBS
  encryption by using an encrypted AMI to launch your instance. If your AMI
  does not have an encrypted root snapshot, you can copy it to a new AMI and
  request encryption. For more information, see [Encrypt an unencrypted image during copy](AMIEncryption.md#copy-unencrypted-to-encrypted "AMIEncryption.md#copy-unencrypted-to-encrypted") and [Copy an AMI](CopyingAMIs.md#ami-copy-steps "CopyingAMIs.md#ami-copy-steps").

## EBS volume type

The EBS volumes must use one of the following EBS volume types:

- General Purpose SSD (`gp2` and `gp3`)
- Provisioned IOPS SSD (`io1` and `io2`)

If you choose a Provisioned IOPS SSD volume type, you must provision the EBS volume with the
appropriate IOPS to achieve optimum performance for hibernation. For more
information, see [Amazon EBS volume types](../../../ebs/latest/userguide/ebs-volume-types.md "../../../ebs/latest/userguide/ebs-volume-types.md") in
the _Amazon EBS User Guide_.

## Spot Instance requests

For Spot Instances, the following requirements apply:

- The Spot Instance request type must be `persistent`.
- You can't specify a launch group in the Spot Instance request.
