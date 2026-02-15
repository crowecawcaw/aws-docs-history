# Getting started with AWS Local Zones

To get started with AWS Local Zones, you must first opt-in to a Local Zone through the AWS Global View
console or the AWS CLI. Next, create a subnet in a VPC in the parent Region, specifying the Local Zone
when you create it. Finally, create AWS resources in the Local Zone subnet.

###### Tasks

- [Step 1: Opt-in to a Local Zone](#getting-started-find-local-zone "#getting-started-find-local-zone")
- [Step 2: Create a Local Zone subnet](#getting-started-create-local-zone-subnet "#getting-started-create-local-zone-subnet")
- [Step 3: Create a resource in your Local Zone
  subnet](#getting-started-create-resources "#getting-started-create-resources")
- [Step 4: Clean up](#getting-started-cleanup "#getting-started-cleanup")

## Step 1: Opt-in to a Local Zone

You can use the AWS Global View console or a command line interface to determine which
Local Zones are available for your account. Then opt in to the Local Zone that you want to use.

AWS Global View console

###### To opt in to a Local Zone

1. Sign in to the [AWS Global View console](https://console.aws.amazon.com/ec2globalview/home#RegionsAndZones "https://console.aws.amazon.com/ec2globalview/home#RegionsAndZones").
2. From the navigation pane, choose **Regions and Zones**.
3. Choose the **Local Zones** tab.
4. Find the Local Zone that you want to enable. You can scroll down the list or enter a term
   in the Search field.
5. Select the row for the Local Zone.
6. Choose **Opt-in**.
7. You will be asked to enable the parent Region of the Local Zone. Choose **Enable
   Region**.
8. On the **Enable Region** pop-up, choose **Enable
   Region**.
9. From the **Local Zones** tab on the **Regions and Zones**
   page, select the Local Zone and choose **Opt-in**.
10. On the **Opt-in Zone group** pop-up, choose **Opt-in Zone
    group**.

You can now use the Local Zone.

AWS CLI

###### To opt in to a Local Zone

1. Use the [describe-availability-zones](../../../cli/latest/reference/ec2/describe-availability-zones.md "../../../cli/latest/reference/ec2/describe-availability-zones.md") command as follows to describe all Local Zones in the specified
   Region.

```
aws ec2 describe-availability-zones \
  --region `us-west-2` \
  --filters Name=zone-type,Values=local-zone \
  --all-availability-zones
```

2. Use the [modify-availability-zone-group](../../../cli/latest/reference/ec2/modify-availability-zone-group.md "../../../cli/latest/reference/ec2/modify-availability-zone-group.md") command as follows to enable a specific Local Zone.

```
aws ec2 modify-availability-zone-group \
  --region `us-west-2` \
  --group-name `us-west-2-lax-1` \
  --opt-in-status opted-in
```

## Step 2: Create a Local Zone subnet

When you add a subnet, you must specify an IPv4 CIDR block for the subnet from the range of
your VPC. You can optionally specify an IPv6 CIDR block for a subnet if there is an IPv6 CIDR
block associated with the VPC. You can specify the Local Zone where the subnet resides. You can have
multiple subnets in the same Local Zone.

Console

###### To add a Local Zone subnet to a VPC

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. From the navigation bar, choose the **Regions** selector and then choose
   the parent Region.
3. In the navigation pane, choose **Subnets**.
4. Choose **Create subnet**.
5. For **VPC ID**, select the VPC.
6. For **Subnet name**, enter a name for your subnet. Doing so creates a tag
   with a key of `Name` and the value that you specify.
7. For **Availability Zone**, choose the Local Zone that you enabled.
8. Specify the IPv4 CIDR block for the subnet.
9. (Optional) Specify an IPv6 CIDR block for the subnet. This option is available only if an
   IPv6 CIDR block is associated with the VPC.
10. (Optional) To add a tag, enter the tag key and tag value. Choose **Add new
    tag** to add another tag.
11. Choose **Create subnet**.

AWS CLI

###### To add a Local Zone subnet to a VPC

Use the [create-subnet](../../../cli/latest/reference/ec2/create-subnet.md "../../../cli/latest/reference/ec2/create-subnet.md") command as
follows to create a subnet for the specified VPC in the specified Local Zone.

```
aws ec2 create-subnet \
  --region `us-west-2` \
  --availability-zone `us-west-2-lax-1a` \
  --vpc-id `vpc-081ec835f303f720e`
```

## Step 3: Create a resource in your Local Zone

subnet

After you create a subnet in a Local Zone, you can deploy AWS resources in the Local Zone. For
example, the following procedure shows how to launch an Amazon EC2 instance in a Local Zone.

Console

###### To launch an Amazon EC2 instance in a Local Zone subnet

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Instances**, choose
   **Instance Types**.
3. In the search field, choose **Availability zones**, choose **Contains**,
   and then enter the zone name (for example, `us-west-2-lax-1`.) Select the first
   item, or whichever item has just this zone ID and the Availability Zones for the parent Region.
4. Select one of the instance types, and then choose **Actions**, **Launch instance**.
5. Under **Name and tags**, enter a descriptive name for the instance (for
   example, _my-lz-instance_). Doing so creates a tag with a key of
   `Name` and the value that you specify.
6. Under **Application and OS Images (Amazon Machine Image)**, do the
   following:
   1. Select an operating system for your instance.
   2. Select the **Amazon Machine Image (AMI)**. An _Amazon Machine
      Image (AMI)_ is a basic configuration that serves as a template for your
      instance.
   3. Select the **Architecture**.

7. Under **Key pair (login)**, choose an existing key pair or create a new
   one. This is required if you want to connect to your EC2 instance.
8. Next to **Network settings**, choose **Edit**, and
   then:
   1. Select your VPC.
   2. Select your Local Zone subnet.
   3. Enable or disable **Auto-assign public IP**.
   4. Create a security group or select an existing one.

9. You can keep the default selections for the other configuration settings for your
   instance. To determine the storage types that are supported, see the _Compute and
   storage_ section in [AWS Local Zones features](https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/").
10. Review a summary of your instance configuration in the **Summary** panel,
    and when you're ready, choose **Launch instance**.
11. A confirmation page lets you know that your instance is launching. Choose **View
    all instances** to close the confirmation page and return to the console.
12. On the **Instances** screen, you can view the status of the
    launch. It takes a short time for an instance to launch. When you launch an
    instance, its initial state is `pending`. After the instance starts,
    its state changes to `running` and it receives a public DNS name. If
    the **Public IPv4 DNS** column is hidden, choose the settings
    icon (
    ![Settings icon.](images/settings-icon.png)
    ) in the top-right corner, turn on **Public IPv4
    DNS**, and choose **Confirm**.
13. It can take a few minutes for the instance to be ready for you to connect to
    it. Check that your instance has passed its status checks; you can view this
    information in the **Status check** column.

AWS CLI

###### To get the instance types supported in a Local Zone

Use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md") command.

```
aws ec2 describe-instance-type-offerings \
    --filters Name=location,Values=`us-west-2-lax-1a` \
    --location-type availability-zone \
    --query InstanceTypeOfferrings[*].InstanceType
```

###### To launch an EC2 instance in a Local Zone subnet

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command.

```
aws ec2 run-instances \
  --region `us-west-2` \
  --subnet-id `subnet-08fc749671b2d077c` \
  --instance-type `t3.micro` \
  --image-id `ami-0abcdef1234567890` \
  --security-group-ids `sg-0b0384b66d7d692f9` \
  --key-name `my-key-pair`
```

## Step 4: Clean up

When you are finished with a Local Zone, delete the resources in the Local Zone. To disable a zone group,
you must contact AWS Support. Open a case titled "Disable zone group" and provide the name of the
zone group.
