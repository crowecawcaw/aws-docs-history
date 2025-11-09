# Using a custom AMI to provide more flexibility for Amazon EMR cluster configuration

When you use Amazon EMR 5.7.0 or higher, you can choose to specify a custom Amazon Linux AMI
instead of the default Amazon Linux AMI for Amazon EMR. A custom AMI is useful if you want to do the
following:

- Pre-install applications and perform other customizations instead of using
  bootstrap actions. This can improve cluster start time and streamline the
  startup work flow. For more information and an example, see [Creating a custom Amazon Linux AMI from a
  preconfigured instance](#emr-custom-ami-preconfigure "#emr-custom-ami-preconfigure").
- Implement more sophisticated cluster and node configurations than bootstrap
  actions allow.
- Encrypt the EBS root device volumes (boot volumes) of EC2 instances in your
  cluster if you are using an Amazon EMR version lower than 5.24.0. As with the default
  AMI, the minimum root volume size for a custom AMI is 10 GiB for Amazon EMR
  releases 6.9 and lower, and 15 GiB for Amazon EMR releases 6.10 and higher. For
  more information, see [Creating a custom AMI with an encrypted
  Amazon EBS root device volume](#emr-custom-ami-encrypted "#emr-custom-ami-encrypted").

###### Note

Beginning with Amazon EMR version 5.24.0, you can use a security configuration option to
encrypt EBS root device and storage volumes when you specify AWS KMS as your key provider. For more information, see [Local disk encryption](emr-data-encryption-options.md#emr-encryption-localdisk "emr-data-encryption-options.md#emr-encryption-localdisk").
A custom AMI must exist in the same AWS Region where you create the cluster. It
should also match the EC2 instance architecture. For example, an m5.xlarge instance has
an x86_64 architecture. Therefore, to provision an m5.xlarge using a custom AMI, your
custom AMI should also have x86_64 architecture. Similarly, to provision an m6g.xlarge
instance, which has arm64 architecture, your custom AMI should have arm64 architecture.
For more information about identifying a Linux AMI for your instance type, see [Find a Linux
AMI](../../../AWSEC2/latest/UserGuide/finding-an-ami.md "../../../AWSEC2/latest/UserGuide/finding-an-ami.md") in the _Amazon EC2 User Guide_.

###### Important

EMR clusters that run Amazon Linux or Amazon Linux 2 Amazon Machine Images (AMIs) use default Amazon Linux behavior, and do not
automatically download and install important and critical kernel updates that require a reboot.
This is the same behavior as other Amazon EC2 instances that run the default Amazon Linux AMI. If new Amazon Linux software updates
that require a reboot (such as kernel, NVIDIA, and CUDA updates) become available after
an Amazon EMR release becomes available, EMR cluster instances that run the default AMI do not automatically
download and install those updates. To get kernel updates, you can [customize your Amazon EMR AMI](emr-custom-ami.md "emr-custom-ami.md") to
[use the latest Amazon Linux AMI](../../../AWSEC2/latest/UserGuide/finding-an-ami.md "../../../AWSEC2/latest/UserGuide/finding-an-ami.md").

## Creating a custom Amazon Linux AMI from a

preconfigured instance

The basic steps for pre-installing software and performing other configurations to
create a custom Amazon Linux AMI for Amazon EMR are as follows:

- Launch an instance from the base Amazon Linux AMI.
- Connect to the instance to install software and perform other
  customizations.
- Create a new image (AMI snapshot) of the instance you configured.

After you create the image based on your customized instance, you can copy that
image to an encrypted target as described in [Creating a custom AMI with an encrypted
Amazon EBS root device volume](#emr-custom-ami-encrypted "#emr-custom-ami-encrypted").

### Tutorial: Creating an

AMI from an instance with custom software installed

###### To launch an EC2 instance based on the most recent Amazon Linux AMI

1. Use the AWS CLI to run the following command, which creates an instance
   from an existing AMI. Replace
   `MyKeyName` with the key pair
   you use to connect to the instance and
   `MyAmiId` with the ID of an appropriate
   Amazon Linux AMI. For the most recent AMI IDs, see [Amazon Linux AMI](https://aws.amazon.com/amazon-linux-ami/ "https://aws.amazon.com/amazon-linux-ami/").

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```

aws ec2 run-instances --image-id `MyAmiID` \
--count 1 --instance-type `m5.xlarge` \
--key-name `MyKeyName` --region `us-west-2`

```

The `InstanceId` output value is used as
`MyInstanceId` in the next
step. 2. Run the following command:

```
aws ec2 describe-instances --instance-ids `MyInstanceId`
```

The `PublicDnsName` output value is used to connect to the
instance in the next step.

###### To connect to the instance and install software

1. Use an SSH connection that lets you run shell commands on your Linux
   instance. For more information, see [Connecting to your
   Linux instance using SSH](../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md "../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md") in the
   _Amazon EC2 User Guide_.
2. Perform any required customizations. For example:

```
sudo yum install `MySoftwarePackage`
sudo pip install `MySoftwarePackage`
```

###### To create a snapshot from your customized image

- After you customize the instance, use the `create-image`
  command to create an AMI from the instance.

```
aws ec2 create-image --no-dry-run --instance-id `MyInstanceId` --name `MyEmrCustomAmi`
```

The `imageID` output value is used when you launch the
cluster or create an encrypted snapshot. For more information, see [Use a single custom AMI in an EMR
cluster](#single-custom-ami "#single-custom-ami") and
[Creating a custom AMI with an encrypted
Amazon EBS root device volume](#emr-custom-ami-encrypted "#emr-custom-ami-encrypted").

## How to use a custom AMI in an Amazon EMR

cluster

You can use a custom AMI to provision an Amazon EMR cluster in two ways:

- Use a single custom AMI for all the EC2 instances in the cluster.
- Use different custom AMIs for the different EC2 instance types used in the
  cluster.

You can use only one of the two options when provisioning an EMR cluster, and you
cannot change it once the cluster has started.

Considerations for using single versus multiple custom AMIs in an Amazon EMR
cluster| Consideration | Single custom AMI | Multiple custom AMIs |
| --- | --- | --- |
| Use both x86 and Graviton2 processors with custom AMIs in the<br>same cluster | Not supported | Supported |
| AMI customization varies across instance types | Not supported | Supported |
| Change custom AMIs when adding new task instance groups/fleets<br>to a running cluster. Note: you cannot change the custom AMI of<br>existing instance groups/fleets. | Not supported | Supported |
| Use AWS Console to start a cluster | Supported | Not supported |
| Use AWS CloudFormation to start a cluster | Supported | Supported |

## Use a single custom AMI in an EMR

cluster

To specify a custom AMI ID when you create a cluster, use one of the
following:

- AWS Management Console
- AWS CLI
- Amazon EMR SDK
- Amazon EMR API [RunJobFlow](../APIReference/API_RunJobFlow.md "../APIReference/API_RunJobFlow.md")
- AWS CloudFormation (see the `CustomAmiID` property in [Cluster InstanceGroupConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.md"), [Cluster InstanceTypeConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.md"), [Resource InstanceGroupConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.md"), or [Resource InstanceFleetConfig-InstanceTypeConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.md"))

Amazon EMR console

###### To specify a single custom AMI from the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and then choose
   **Create cluster**.
3. Under **Name and applications**, find
   **Operating system options**. Choose
   **Custom AMI**, and enter your AMI ID in
   the **Custom AMI** field.
4. Choose any other options that apply to your cluster.
5. To launch your cluster, choose **Create
   cluster**.

AWS CLI

###### To specify a single custom AMI with the AWS CLI

- Use the `--custom-ami-id` parameter to specify the
  AMI ID when you run the `aws emr create-cluster` command.

The following example specifies a cluster that uses a single
custom AMI with a 20 GiB boot volume. For more information, see
[Customizing the Amazon EBS root device
volume](emr-custom-ami-root-volume-size.md "emr-custom-ami-root-volume-size.md").

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```

aws emr create-cluster --name "`Cluster with My Custom AMI`" \
--custom-ami-id `MyAmiID` --ebs-root-volume-size `20` \
--release-label emr-5.7.0 --use-default-roles \
--instance-count `2` --instance-type `m5.xlarge`

```

## Use multiple custom AMIs in an Amazon EMR

cluster

To create a cluster using multiple custom AMIs, use one of the following:

- AWS CLI version 1.20.21 or higher
- AWS SDK
- Amazon EMR [RunJobFlow](../APIReference/API_RunJobFlow.md "../APIReference/API_RunJobFlow.md") in
  the _Amazon EMR API Reference_
- AWS CloudFormation (see the `CustomAmiID` property in [Cluster InstanceGroupConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.md"), [Cluster InstanceTypeConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.md"), [Resource InstanceGroupConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.md"), or [Resource InstanceFleetConfig-InstanceTypeConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.md"))

The AWS Management Console currently does not support creating a cluster using
multiple custom AMIs.

###### Example - Use the AWS CLI to create an instance group cluster using multiple custom

AMIs

Using the AWS CLI version 1.20.21 or higher, you can assign a single custom
AMI to the entire cluster, or you can assign multiple custom AMIs to every
instance node in your cluster.

The following example shows a uniform instance group cluster created with two
instance types (m5.xlarge) used across node types (primary, core, task). Each
node has multiple custom AMIs. The example illustrates several features of the
multiple custom AMI configuration:

- There is no custom AMI assigned at the cluster level. This is to avoid
  conflicts between the multiple custom AMIs and a single custom AMI,
  which would cause the cluster launch to fail.
- The cluster can have multiple custom AMIs across primary, core, and
  individual task nodes. This allows individual AMI customizations, such
  as pre-installed applications, sophisticated cluster configurations, and
  encrypted Amazon EBS root device volumes.
- The instance group core node can have only one instance type and
  corresponding custom AMI. Similarly, the primary node can have only one
  instance type and corresponding custom AMI.
- The cluster can have multiple task nodes.

```
aws emr create-cluster --instance-groups
InstanceGroupType=PRIMARY,InstanceType=`m5.xlarge`,InstanceCount=`1`,CustomAmiId=`ami-123456`
InstanceGroupType=CORE,InstanceType=`m5.xlarge`,InstanceCount=`1`,CustomAmiId=`ami-234567`
InstanceGroupType=TASK,InstanceType=`m6g.xlarge`,InstanceCount=`1`,CustomAmiId=`ami-345678`
InstanceGroupType=TASK,InstanceType=`m5.xlarge`,InstanceCount=`1`,CustomAmiId=`ami-456789`
```

###### Example - Use the AWS CLI version 1.20.21 or higher to add a task node to a running

instance group cluster with multiple instance types and multiple custom
AMIs

Using the AWS CLI version 1.20.21 or higher, you can add multiple custom
AMIs to an instance group that you add to a running cluster. The
`CustomAmiId` argument can be used with the
`add-instance-groups` command as shown in the following example.
Notice that the same multiple custom AMI ID (ami-123456) is used in more than
one node.

```
aws emr create-cluster --instance-groups
InstanceGroupType=PRIMARY,InstanceType=m5.xlarge,InstanceCount=1,CustomAmiId=ami-123456
InstanceGroupType=CORE,InstanceType=m5.xlarge,InstanceCount=1,CustomAmiId=ami-123456
InstanceGroupType=TASK,InstanceType=m5.xlarge,InstanceCount=1,CustomAmiId=ami-234567

{
    "ClusterId": "j-123456",
    ...
}

aws emr add-instance-groups --cluster-id j-123456 --instance-groups InstanceGroupType=Task,InstanceType=m6g.xlarge,InstanceCount=1,CustomAmiId=ami-345678
```

###### Example - Use the AWS CLI version 1.20.21 or higher to create an instance fleet

cluster, multiple custom AMIs, multiple instance types, On-Demand primary,
On-Demand core, multiple core and task nodes

```
aws emr create-cluster --instance-fleets
InstanceFleetType=PRIMARY,TargetOnDemandCapacity=1,InstanceTypeConfigs=['{InstanceType=m5.xlarge, CustomAmiId=ami-123456}']
InstanceFleetType=CORE,TargetOnDemandCapacity=1,InstanceTypeConfigs=['{InstanceType=m5.xlarge,CustomAmiId=ami-234567},{InstanceType=m6g.xlarge, CustomAmiId=ami-345678}']
InstanceFleetType=TASK,TargetSpotCapacity=1,InstanceTypeConfigs=['{InstanceType=m5.xlarge,CustomAmiId=ami-456789},{InstanceType=m6g.xlarge, CustomAmiId=ami-567890}']

```

###### Example - Use the AWS CLI version 1.20.21 or higher to add task nodes to a running

cluster with multiple instance types and multiple custom AMIs

```
aws emr create-cluster --instance-fleets
InstanceFleetType=PRIMARY,TargetOnDemandCapacity=1,InstanceTypeConfigs=['{InstanceType=m5.xlarge, CustomAmiId=ami-123456}']
InstanceFleetType=CORE,TargetOnDemandCapacity=1,InstanceTypeConfigs=['{InstanceType=m5.xlarge,CustomAmiId=ami-234567},{InstanceType=m6g.xlarge, CustomAmiId=ami-345678}']

{
    "ClusterId": "j-123456",
    ...
}

aws emr add-instance-fleet --cluster-id j-123456 --instance-fleet
InstanceFleetType=TASK,TargetSpotCapacity=1,InstanceTypeConfigs=['{InstanceType=m5.xlarge,CustomAmiId=ami-234567},{InstanceType=m6g.xlarge, CustomAmiId=ami-345678}']

```

## Managing AMI package repository

updates

On first boot, by default, Amazon Linux AMIs connect to package repositories to install
security updates before other services start. Depending on your requirements, you
may choose to disable these updates when you specify a custom AMI for Amazon EMR. The
option to disable this feature is available only when you use a custom AMI. By
default, Amazon Linux kernel updates and other software packages that require a reboot are
not updated. Note that your networking configuration must allow for HTTP and HTTPS
egress to Amazon Linux repositories in Amazon S3, otherwise security updates will not
succeed.

###### Warning

We strongly recommend that you choose to update all installed packages on
reboot when you specify a custom AMI. Choosing not to update packages creates
additional security risks.

With the AWS Management Console, you can select the option to disable updates when you choose
**Custom AMI**.

With the AWS CLI, you can specify `--repo-upgrade-on-boot NONE` along
with `--custom-ami-id` when using the **create-cluster**
command.

With the Amazon EMR API, you can specify `NONE` for the [RepoUpgradeOnBoot](../../../ElasticMapReduce/latest/API/API_RunJobFlow.md#EMR-RunJobFlow-request-RepoUpgradeOnBoot "../../../ElasticMapReduce/latest/API/API_RunJobFlow.md#EMR-RunJobFlow-request-RepoUpgradeOnBoot") parameter.

## Creating a custom AMI with an encrypted

Amazon EBS root device volume

To encrypt the Amazon EBS root device volume of an Amazon Linux AMI for Amazon EMR, copy a snapshot
image from an unencrypted AMI to an encrypted target. For information about creating
encrypted EBS volumes, see [Amazon EBS encryption](../../../AWSEC2/latest/UserGuide/EBSEncryption.md "../../../AWSEC2/latest/UserGuide/EBSEncryption.md") in the _Amazon EC2 User Guide_. The source
AMI for the snapshot can be the base Amazon Linux AMI, or you can copy a snapshot from an
AMI derived from the base Amazon Linux AMI that you customized.

###### Note

Beginning with Amazon EMR version 5.24.0, you can use a security configuration option to
encrypt EBS root device and storage volumes when you specify AWS KMS as your key provider. For more information, see [Local disk encryption](emr-data-encryption-options.md#emr-encryption-localdisk "emr-data-encryption-options.md#emr-encryption-localdisk").

You can use an external key provider or an AWS KMS key to encrypt the EBS root
volume. The service role that Amazon EMR uses (usually the default
`EMR_DefaultRole`) must be allowed to encrypt and decrypt the volume,
at minimum, for Amazon EMR to create a cluster with the AMI. When using AWS KMS as the key
provider, this means that the following actions must be allowed:

- `kms:encrypt`
- `kms:decrypt`
- `kms:ReEncrypt*`
- `kms:CreateGrant`
- `kms:GenerateDataKeyWithoutPlaintext"`
- `kms:DescribeKey"`

The simplest way to do this is to add the role as a key user as described in the
following tutorial. The following example policy statement is provided if you need
to customize role policies.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EmrDiskEncryptionPolicy",
 "Effect": "Allow",
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:CreateGrant",
 "kms:GenerateDataKeyWithoutPlaintext",
 "kms:DescribeKey"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

### Tutorial: Creating a

custom AMI with an encrypted root device volume using a KMS key

The first step in this example is to find the ARN of a KMS key or create a
new one. For more information about creating keys, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
_AWS Key Management Service Developer Guide_. The following procedure shows you how
to add the default service role, `EMR_DefaultRole`, as a key user to
the key policy. Write down the **ARN** value for the key as you
create or edit it. You use the ARN higher, when you create the AMI.

###### To add the service role for Amazon EC2 to the list of encryption key users

with the console

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. Choose the alias of the KMS key to use.
4. On the key details page under **Key Users**, choose
   **Add**.
5. In the **Attach** dialog box, choose the Amazon EMR
   service role. The name of the default role is
   `EMR_DefaultRole`.
6. Choose **Attach**.

###### To create an encrypted AMI with the AWS CLI

- Use the `aws ec2 copy-image` command from the AWS CLI to
  create an AMI with an encrypted EBS root device volume and the key that
  you modified. Replace the `--kms-key-id` value specified with
  the full ARN of the key that you created or modified lower.

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```

aws ec2 copy-image --source-image-id `MyAmiId` \
--source-region `us-west-2` --name `MyEncryptedEMRAmi` \
--encrypted --kms-key-id `arn:aws:kms:us-west-2:12345678910:key/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
```

The output of the command provides the ID of the AMI that you created, which
you can specify when you create a cluster. For more information, see [Use a single custom AMI in an EMR
cluster](#single-custom-ami "#single-custom-ami"). You can
also choose to customize this AMI by installing software and performing other
configurations. For more information, see [Creating a custom Amazon Linux AMI from a
preconfigured instance](#emr-custom-ami-preconfigure "#emr-custom-ami-preconfigure").

## Best practices and

considerations

When you create a custom AMI for Amazon EMR, consider the following:

- The Amazon EMR 7.x series are based on Amazon Linux 2023. For these Amazon EMR versions, you need to use images based on Amazon Linux 2023 for custom AMIs. To find a base custom AMI, see [Finding a Linux AMI](../../../AWSEC2/latest/UserGuide/finding-an-ami.md "../../../AWSEC2/latest/UserGuide/finding-an-ami.md").
- For Amazon EMR versions lower than 7.x, Amazon Linux 2023 AMIs are not supported.
- Amazon EMR 5.30.0 and higher, and the Amazon EMR 6.x series are based on Amazon Linux 2. For
  these Amazon EMR versions, you need to use images based on Amazon Linux 2 for custom
  AMIs. To find a base custom AMI, see [Finding a Linux AMI](../../../AWSEC2/latest/UserGuide/finding-an-ami.md "../../../AWSEC2/latest/UserGuide/finding-an-ami.md").
- For Amazon EMR versions lower than 5.30.0 and 6.x, Amazon Linux 2 AMIs are not
  supported.
- You must use a 64-bit Amazon Linux AMI. A 32-bit AMI is not supported.
- Amazon Linux AMIs with multiple Amazon EBS volumes are not supported.
- Base your customization on the most recent EBS-backed [Amazon Linux AMI](https://aws.amazon.com/amazon-linux-ami/ "https://aws.amazon.com/amazon-linux-ami/"). For a list of
  Amazon Linux AMIs and corresponding AMI IDs, see [Amazon Linux AMI](https://aws.amazon.com/amazon-linux-ami/ "https://aws.amazon.com/amazon-linux-ami/").
- Do not copy a snapshot of an existing Amazon EMR instance to create a custom
  AMI. This causes errors.
- Only the HVM virtualization type and instances compatible with Amazon EMR are
  supported. Be sure to select the HVM image and an instance type compatible
  with Amazon EMR as you go through the AMI customization process. For compatible
  instances and virtualization types, see [Supported instance types with Amazon EMR](emr-supported-instance-types.md "emr-supported-instance-types.md").
- Your service role must have launch permissions on the AMI, so either the
  AMI must be public, or you must be the owner of the AMI or have it shared
  with you by the owner.
- Creating users on the AMI with the same name as applications causes errors
  (for example, `hadoop`, `hdfs`, `yarn`, or
  `spark`).
- The contents of `/tmp`, `/var`, and
  `/emr` (if they exist on the AMI) are moved to
  `/mnt/tmp`, `/mnt/var`, and `/mnt/emr`
  respectively during startup. Files are preserved, but if there is a large
  amount of data, startup may take longer than expected.
- If you use a custom Amazon Linux AMI based on an Amazon Linux AMI with a creation date of 2018-08-11, the Oozie server fails to start. If you use Oozie, create a custom AMI based on an Amazon Linux AMI ID with a different creation date. You can use the following AWS CLI command to return a list of Image IDs for all HVM Amazon Linux AMIs with a 2018.03 version, along with the release date, so that you can choose an appropriate Amazon Linux AMI as your base. Replace MyRegion with your Region identifier, such as us-west-2.

```
aws ec2 --region `MyRegion` describe-images --owner amazon --query 'Images[?Name!=`null`]|[?starts_with(Name, `amzn-ami-hvm-2018.03`) == `true`].[CreationDate,ImageId,Name]' --output text | sort -rk1

```

- In cases where you use a VPC with a non-standard domain name and
  AmazonProvidedDNS, you should not use the `rotate` option in the
  Operating Systems DNS configuration.
- If you create a custom AMI that includes the Amazon EC2 Systems Manager (SSM) agent, the enabled SSM agent
  can cause a provisioning error on the cluster. To avoid this, disable the SSM agent when you use a custom AMI. To do this, when you choose and
  launch your Amazon EC2 instance, disable the SSM agent prior to using the instance to create a custom AMI and subsequently creating your EMR cluster.

For more information, see [Creating an Amazon EBS-backed Linux AMI](../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md "../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md") in the
_Amazon EC2 User Guide_.
