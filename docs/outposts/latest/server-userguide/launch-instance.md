# Launch an instance on your Outposts server

After your Outpost is installed and the compute and storage capacity is available for use,
you can get started by creating resources. For example, you can launch Amazon EC2 instances.

###### Prerequisite

You must have an Outpost installed at your site. For more information, see [Create an Outpost and order Outpost capacity](order-outpost-capacity.md "order-outpost-capacity.md").

###### Tasks

- [Step 1: Create a subnet](#create-subnet "#create-subnet")
- [Step 2: Launch an instance on the Outpost](#launch-instances "#launch-instances")
- [Step 3: Configure connectivity](#configure-routing "#configure-routing")
- [Step 4: Test the connectivity](#test-connecitivity "#test-connecitivity")

## Step 1: Create a subnet

You can add Outpost subnets to any VPC in the AWS Region for the Outpost. When you do
so, the VPC also spans the Outpost. For more information, see [Network components](how-outposts-works.md#outposts-networking-components "how-outposts-works.md#outposts-networking-components").

###### Note

If you are launching an instance in an Outpost subnet that has been shared with you by
another AWS account, skip to [Step 2: Launch an instance on the Outpost](#launch-instances "#launch-instances").

###### To create an outpost subnet

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. On the navigation pane, choose **Outposts**.
3. Select the Outpost, and then choose **Actions**, **Create
   subnet**. You are redirected to create a subnet in the Amazon VPC console. We select
   the Outpost for you and the Availability Zone that the Outpost is homed to.
4. Select a VPC and specify an IP address range for the subnet.
5. Choose **Create**.
6. After the subnet is created, you must enable the subnet for local network interfaces.
   Use the [modify-subnet-attribute](../../../cli/latest/reference/ec2/modify-subnet-attribute.md "../../../cli/latest/reference/ec2/modify-subnet-attribute.md") command from the AWS CLI. You must specify the position
   of the network interface on the device index. All instances launched in an enabled Outpost
   subnet use this device position for local network interfaces. The following example uses a
   value of 1 to specify a secondary network interface.

```
aws ec2 modify-subnet-attribute \
    --subnet-id `subnet-1a2b3c4d` \
    --enable-lni-at-device-index `1`
```

## Step 2: Launch an instance on the Outpost

You can launch EC2 instances in the Outpost subnet that you created, or in an Outpost
subnet that has been shared with you. Security groups control inbound and outbound VPC traffic
for instances in an Outpost subnet, just as they do for instances in an Availability Zone
subnet. To connect to an EC2 instance in an Outpost subnet, you can specify a key pair when
you launch the instance, just as you do for instances in an Availability Zone subnet.

###### Considerations

- Instances on Outposts servers include instance store volumes but not EBS volumes. Choose an
  instance size with enough instance storage to meet the needs of your application. For more
  information, see [Instance store
  volumes](../../../AWSEC2/latest/UserGuide/instance-store-volumes.md "../../../AWSEC2/latest/UserGuide/instance-store-volumes.md") and [Create an instance store-backed AMI](../../../AWSEC2/latest/UserGuide/creating-an-ami-instance-store.md "../../../AWSEC2/latest/UserGuide/creating-an-ami-instance-store.md") in the
  _Amazon EC2 User Guide_.
- You must use an Amazon EBS-backed AMI with only a single EBS snapshot. AMIs with more than
  one EBS snapshot are not supported.
- The data on instance store volumes persists after an instance reboot but does not
  persist after instance termination. To retain the long-term data on your instance store
  volumes beyond the lifetime of the instance, be sure to back up the data to persistent
  storage, such as an Amazon S3 bucket or a network storage device in your on-premises
  network.
- To use block data or boot volumes backed by compatible third-party storage, you
  must provision and configure these volumes for use with EC2 instances on Outposts.
  For more information, see [Third-party block storage on
  Outposts servers](outpost-third-party-block-storage.md "outpost-third-party-block-storage.md").
- To connect an instance in an Outpost subnet to your on-premises
  network, you must add a [local network
  interface](local-network-interface.md "local-network-interface.md"), as described in the following procedure.

###### To launch instances in your Outpost subnet

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. On the navigation pane, choose **Outposts**.
3. Select the Outpost, and then choose **Actions, View details**.
4. On the **Outpost summary** page, choose **Launch
   instance**. You are redirected to the instance launch wizard in the Amazon EC2
   console. We select the Outpost subnet for you, and show you only the instance types that
   are supported by your Outposts servers.
5. Choose an instance type that is supported by your Outposts servers. Note that instances
   that appear grayed out are not available.
6. (Optional) You can add a local network interface now or after you create the instance.
   To add it now, expand **Advanced network configuration** and choose
   **Add network interface**. Choose the Outpost subnet. This creates a
   network interface for the instance using device index 1. If you specified 1 as the local
   network interface device index for the Outpost subnet, this network interface is the local
   network interface for the instance. Alternatively, to add it later, see [Add a local network interface](add-lni.md "add-lni.md").
7. (Optional) You can add a [third-party data volume](outpost-third-party-block-storage.md "outpost-third-party-block-storage.md").
   1. Expand **Configure storage**. Next to **External storage volume**,
      choose **Edit**.
   2. For **Storage Network Protocol**, choose **iSCSI**.
   3. Enter the Initiator IQN, then add the target IP address, the port, and the IQN of the
      external storage array.

8. Complete the wizard to launch the instance in your Outpost subnet. For more
   information, see [Launch an EC2
   instance](../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md "../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md") in the _Amazon EC2 User Guide_:

## Step 3: Configure connectivity

If you did not add a local network interface to your instance during instance launch, you
must do so now. For more information, see [Add a local network interface](add-lni.md "add-lni.md").

You must configure the local network interface for the instance with an IP address from
your local network. For information, see the
documentation for the operating system running on the instance. Search for information about
configuring additional network interfaces and secondary IP addresses.

## Step 4: Test the connectivity

You can test connectivity by using the appropriate use cases.

###### Test connectivity from your local network to the Outpost

From a computer in your local network, run the `ping` command to the Outpost
instance's local network interface IP address.

```
ping `10.0.3.128`
```

The following is example output.

```
Pinging 10.0.3.128

Reply from 10.0.3.128:  bytes=32 time=<1ms TTL=128
Reply from 10.0.3.128:  bytes=32 time=<1ms TTL=128
Reply from 10.0.3.128:  bytes=32 time=<1ms TTL=128

Ping statistics for 10.0.3.128
Packets:  Sent = 3,  Received = 3,  Lost = 0 (0% lost)

Approximate round trip time in milliseconds
Minimum = 0ms,  Maximum = 0ms,  Average = 0ms
```

###### Test the connectivity from an Outpost instance to your local network

Depending on your operating system, use **ssh** or
**rdp** to connect to the private IP address of your Outpost instance.
For information about connecting to an EC2 instance, see [Connect to your EC2 instance](../../../AWSEC2/latest/UserGuide/connect.md "../../../AWSEC2/latest/UserGuide/connect.md") in the
_Amazon EC2 User Guide_.

After the instance is running, run the `ping` command to an IP address of a
computer in your local network. In the following example, the IP address is
172.16.0.130.

```
ping `172.16.0.130`
```

The following is example output.

```
Pinging 172.16.0.130

Reply from 172.16.0.130:  bytes=32 time=<1ms TTL=128
Reply from 172.16.0.130:  bytes=32 time=<1ms TTL=128
Reply from 172.16.0.130:  bytes=32 time=<1ms TTL=128

Ping statistics for 172.16.0.130
Packets:  Sent = 3,  Received = 3,  Lost = 0 (0% lost)

Approximate round trip time in milliseconds
Minimum = 0ms,  Maximum = 0ms,  Average = 0ms
```

###### Test connectivity between the AWS Region and the Outpost

Launch an instance in the subnet in the AWS Region. For example, use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command.

```
aws ec2 run-instances \
    --image-id `ami-abcdefghi1234567898` \
    --instance-type c5.large \
    --key-name `MyKeyPair` \
    --security-group-ids `sg-1a2b3c4d123456787` \
    --subnet-id `subnet-6e7f829e123445678`
```

After the instance is running, perform the following operations:

1. Get the private IP address of the instance in the AWS Region. This information is
   available in the Amazon EC2 console on the instance detail page.
2. Depending on your operating system, use **ssh** or
   **rdp** to connect to the private IP address of your Outpost
   instance.
3. Run the **ping** command from your Outpost instance, specifying the IP
   address of the instance in the AWS Region.

```
ping `10.0.1.5`
```

The following is example output.

```
Pinging 10.0.1.5

Reply from 10.0.1.5:  bytes=32 time=<1ms TTL=128
Reply from 10.0.1.5:  bytes=32 time=<1ms TTL=128
Reply from 10.0.1.5:  bytes=32 time=<1ms TTL=128

Ping statistics for 10.0.1.5
Packets:  Sent = 3,  Received = 3,  Lost = 0 (0% lost)

Approximate round trip time in milliseconds
Minimum = 0ms,  Maximum = 0ms,  Average = 0ms
```
