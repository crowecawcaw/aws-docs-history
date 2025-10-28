# Getting started with AWS Local Zones

To get started with AWS Local Zones, you must first enable a Local Zone through the Amazon EC2 console or the
AWS CLI. Next, create a subnet in a VPC in the parent Region, specifying the Local Zone when you create
it. Finally, create AWS resources in the Local Zone subnet.

###### Tasks

- [Step 1: Enable a Local Zone](#getting-started-find-local-zone "#getting-started-find-local-zone")
- [Step 2: Create a Local Zone subnet](#getting-started-create-local-zone-subnet "#getting-started-create-local-zone-subnet")
- [Step 3: Create a resource in your Local Zone
  subnet](#getting-started-create-resources "#getting-started-create-resources")
- [Step 4: Clean up](#getting-started-cleanup "#getting-started-cleanup")

## Step 1: Enable a Local Zone

You can use the Amazon EC2 console or a command line interface to determine which Local Zones are
available for your account, and then enable the Local Zone that you want to use.

###### To enable a Local Zone using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the navigation bar, choose the **Regions** selector and then choose
   the parent Region.
3. From the Amazon EC2 console dashboard, in the **Account attributes** box,
   choose **Zones**.
4. (Optional) To filter the list of zones, choose the **All Zones** filter
   and then **Local Zones**.
5. Select the row of the Local Zone that you want to use.
6. Choose **Actions**, **Manage Zone group**.
7. On the **Manage zone group** pop-up, select
   **Enable**.
8. Choose **Update**.
9. To confirm that you want to enable the Local Zone, enter **Enable**.
10. Choose **Enable zone group**.

###### To enable a Local Zone using the AWS CLI

Use the [describe-availability-zones](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-availability-zones.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-availability-zones.html") command as follows to describe all Local Zones in the specified
Region.

```
aws ec2 describe-availability-zones \
  --region `us-west-2` \
  --filters Name=zone-type,Values=local-zone \
  --all-availability-zones
```

Use the [modify-availability-zone-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-availability-zone-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-availability-zone-group.html") command as follows to enable a specific Local Zone.

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

###### To add a Local Zone subnet to a VPC using the console

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

###### To add a Local Zone subnet to a VPC using the AWS CLI

Use the [create-subnet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-subnet.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-subnet.html") command as
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

###### To launch an Amazon EC2 instance in a Local Zone subnet using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the Amazon EC2 console dashboard, in the **Launch instance** box, choose
   **Launch instance**.
3. Under **Name and tags**, enter a descriptive name for the instance (for
   example, _my-lz-instance_). Doing so creates a tag with a key of
   `Name` and the value that you specify.
4. Under **Application and OS Images (Amazon Machine Image)**, do the
   following:
   1. Select an operating system for your instance.
   2. Select the **Amazon Machine Image (AMI)**. An _Amazon Machine
      Image (AMI)_ is a basic configuration that serves as a template for your
      instance.
   3. Select the **Architecture**.

5. Under **Instance type**, from the **Instance type**
   list, select the hardware configuration for your instance that's supported in a Local Zone. For
   example, the `t3.micro` instance type.
6. Under **Key pair (login)**, choose an existing key pair or create a new
   one.

###### Warning

Do not choose **Proceed without a key pair (Not recommended)**. If you
launch your instance without a key pair, then you can't connect to it. 7. Next to **Network settings**, choose **Edit**, and
then:

    1. Select your VPC.
    2. Select your Local Zone subnet.
    3. Enable or disable **Auto-assign public IP**.
    4. Create a security group or select an existing one.

8. You can keep the default selections for the other configuration settings for your
   instance. To determine the storage types that are supported, see the _Compute and
   storage_ section in [AWS Local Zones features](https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/").
9. Review a summary of your instance configuration in the **Summary** panel,
   and when you're ready, choose **Launch instance**.
10. A confirmation page lets you know that your instance is launching. Choose **View
    all instances** to close the confirmation page and return to the console.
11. On the **Instances** screen, you can view the status of the launch. It
    takes a short time for an instance to launch. When you launch an instance, its initial state is
    `pending`. After the instance starts, its state changes to `running` and
    it receives a public DNS name. If the **Public IPv4 DNS** column is hidden,
    choose the settings icon (
    ![Settings icon.](images/settings-icon.png)
    ) in the top-right corner, turn on **Public IPv4 DNS**,
    and choose **Confirm**.
12. It can take a few minutes for the instance to be ready for you to connect to it. Check
    that your instance has passed its status checks; you can view this information in the
    **Status check** column.

###### To launch an EC2 instance in a Local Zone subnet using the AWS CLI

Use the [run-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html") command as
follows to launch an instance in the specified Local Zone subnet.

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

When you are finished with a Local Zone, delete the resources in the Local Zone. Then contact
AWS Support to disable it.
