# Customizing the Amazon EBS root device

volume

You can set your volume type and other attributes, depending on your use case and cost requirements. You can accept default values or make customizations.

## EBS root volume defaults

With Amazon EMR 4.x and higher, you can specify the root volume size when you create a
cluster. With Amazon EMR releases 6.15.0 and higher, you can also specify the root volume
IOPS and throughput. The attributes apply only to the Amazon EBS root device volume, and
apply to all instances in the cluster. The attributes don’t apply to storage
volumes, which you specify separately for each instance type when you create your
cluster.

- The default root volume size is 15 GiB in Amazon EMR 6.10.0 and higher.
  Earlier releases have a default root volume size of 10 GiB. You can
  adjust this up to 100 GiB.
- The default root volume IOPS is 3000. You can adjust this up to

16000.

- The default root volume throughput is 125 MiB/s. You can adjust this
  up to 1000 Mib/s.

###### Note

The root volume size and IOPS can’t have a ratio higher than 1 volume to
500 IOPS (1:500), while root volume IOPS and throughput can’t have a ratio
higher than 1 IOPS to 0.25 throughput (1:0.25).

For more information about Amazon EBS, see [Amazon EC2 root device
volume](../../../AWSEC2/latest/UserGuide/RootDeviceStorage.md "../../../AWSEC2/latest/UserGuide/RootDeviceStorage.md").

## Root device volume type with the

default AMI

When you use the default AMI, the root device volume type is determined by the
Amazon EMR release that you use.

- With Amazon EMR releases 6.15.0 and higher, Amazon EMR attaches **General Purpose SSD (gp3)** as the root device
  volume type.
- With Amazon EMR releases lower than 6.15.0, Amazon EMR attaches **General Purpose SSD (gp2)** as the root device
  volume type.

## Root device volume type with the custom

AMI

A custom AMI might have different root device volume types. Amazon EMR always uses your
custom AMI volume type.

- With Amazon EMR releases 6.15.0 and higher, you can configure root volume size,
  IOPS, and throughput for your custom AMI, provided tht these attributes are
  applicable to the custom AMI volume type.
- With Amazon EMR releases lower than 6.15.0, you can only configure the root
  volume size for your custom AMI.

If you do not configure root volume size, IOPS, or throughput when you create your
cluster, Amazon EMR uses the values from the custom AMI if applicable. If you decide to
configure these values when you create your cluster, Amazon EMR uses the values that you
specify as long as the values are compatible with and supported by the custom AMI
root volume. For more information, see [Using a custom AMI to provide more flexibility for Amazon EMR cluster configuration](emr-custom-ami.md "emr-custom-ami.md").

## Root device volume size pricing

The cost of the EBS root device volume is pro-rated by the hour, based on the
monthly EBS charges for that volume type in the Region where the cluster runs. The
same is true of storage volumes. Charges are in GB, but you specify the size of the
root volume in GiB, so you might want to consider this in your estimates (1 GB is
0.931323 GiB).

General Purpose SSD gp2 and gp3 are billed differently. To estimate the
charges associated with EBS root device volumes in your cluster, use the
following formulas:

**General Purpose SSD gp2**

Cost for **gp2** includes only the EBS
volume size in GB.

```
($EBS size in GB/month) * 0.931323 / 30 / 24 * EMR_EBSRootVolumesizeInGiB * InstanceCount
```

For example, take a cluster that has a primary node, a core node, and
uses the base Amazon Linux AMI, with the default 10 GiB root device volume. If
the EBS cost in the Region is USD $0.10/GB/month, that works out to be
approximately $0.00129 per instance per hour, and $0.00258 per hour for
the cluster ($0.10/GB/month divided by 30 days, divided by 24 hours,
multiplied by 10 GB, multiplied by 2 cluster instances).

**General Purpose SSD gp3**

Cost for **gp3** includes EBS volume size
in GB, IOPS above 3000 (3000 IOPS free), and throughput above 125 MB/s
(125 MB/s free).

```
($EBS size in GB/month) * 0.931323 / 30 / 24 * EMR_EBSRootVolumesizeInGiB * InstanceCount
+
($EBS IOPS/Month)/30/24* (EMR_EBSRootVolumeIops - 3000) * InstanceCount
+
($EBS throughput/Month)/30/24* (EMR_EBSRootVolumeThroughputInMb/s - 125) * InstanceCount

```

For example, take a cluster that has a primary node, a core node, and
uses the base Amazon Linux AMI, with the default 15 GiB root device volume Size,
4000 IOPS, and 140 throughput. If the EBS cost in the Region is USD
$0.10/GB/month, $0.005/provisioned IOPS/month over 3000, and
$0.040/provisioned MB/s/month over 125. That works out to be
approximately $0.009293 per instance per hour, and $0.018586 per hour
for the cluster.

## Specifying custom root device volume

settings

###### Note

The root volume size and IOPS can’t have a ratio higher than 1 volume to
500 IOPS (1:500), while root volume IOPS and throughput can’t have a ratio
higher than 1 IOPS to 0.25 throughput (1:0.25).

Console

###### To specify Amazon EBS root device volume attributes from the Amazon EMR

console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and then choose
   **Create cluster**.
3. Select Amazon EMR release 6.15.0 or higher.
4. Under **Cluster configuration**, navigate to
   the **EBS root volume** section and enter a
   value for any of the attributes that you want to
   configure.
5. Choose any other options that apply to your cluster.
6. To launch your cluster, choose **Create
   cluster**.

CLI

###### To specify Amazon EBS root device volume attributes with the

AWS CLI

- Use the `--ebs-root-volume-size`,
  `--ebs-root-volume-iops`, and
  `--ebs-root-volume-throughput` parameters of the
  [create-cluster](../../../cli/latest/reference/emr/create-cluster.md "../../../cli/latest/reference/emr/create-cluster.md") command, as shown in the following
  example.

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr create-cluster --release-label emr-6.15.0\
--ebs-root-volume-size 20 \
--ebs-root-volume-iops 3000\
--ebs-root-volume-throughput 135\
--instance-groups InstanceGroupType=MASTER,\
InstanceCount=1,InstanceType=m5.xlarge InstanceGroupType=CORE,InstanceCount=2,InstanceType=m5.xlarge

```
