# Launch clusters into a VPC with Amazon EMR

After you have a subnet that is configured to host Amazon EMR clusters, launch the
cluster in that subnet by specifying the associated subnet identifier when
creating the cluster.

###### Note

Amazon EMR supports private subnets in release versions 4.2 and above.

When the cluster is launched, Amazon EMR adds security groups based on whether the
cluster is launching into VPC private or public subnets. All security groups
allow ingress at port 8443 to communicate to the Amazon EMR service, but IP address
ranges vary for public and private subnets. Amazon EMR manages all of these security
groups, and may need to add additional IP addresses to the AWS range over
time. For more information, see [Control network traffic with security groups for your Amazon EMR cluster](emr-security-groups.md "emr-security-groups.md").

To manage the cluster on a VPC, Amazon EMR attaches a network device to the primary
node and manages it through this device. You can view this device using the
Amazon EC2 API action [`DescribeInstances`](../../../AWSEC2/latest/APIReference/ApiReference-query-DescribeInstances.md "../../../AWSEC2/latest/APIReference/ApiReference-query-DescribeInstances.md"). If you modify this device in
any way, the cluster may fail.

Console

###### To launch a cluster into a VPC with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left
   navigation pane, choose **Clusters**, and
   then choose **Create cluster**.
3. Under **Networking**, go to the
   **Virtual private cloud (VPC)** field.
   Enter the name of your VPC or choose
   **Browse** to select your VPC.
   Alternatively, choose **Create VPC** to
   create a VPC that you can use for your cluster.
4. Choose any other options that apply to your
   cluster.
5. To launch your cluster, choose **Create
   cluster**.

AWS CLI

###### To launch a cluster into a VPC with the AWS CLI

###### Note

The AWS CLI does not provide a way to create a NAT instance
automatically and connect it to your private subnet.
However, to create a S3 endpoint in your subnet, you can use
the Amazon VPC CLI commands. Use the console to create NAT
instances and launch clusters in a private
subnet.

After your VPC is configured, you can launch Amazon EMR clusters in
it by using the `create-cluster` subcommand with the
`--ec2-attributes` parameter. Use the
`--ec2-attributes` parameter to specify the VPC
subnet for your cluster.

- To create a cluster in a specific subnet, type the
  following command, replace `myKey`
  with the name of your Amazon EC2 key pair, and replace
  `77XXXX03` with your subnet
  ID.

```
aws emr create-cluster --name `"Test cluster"` --release-label `emr-4.2.0` --applications Name=`Hadoop` Name=`Hive` Name=`Pig` --use-default-roles --ec2-attributes KeyName=`myKey`,SubnetId=subnet-`77XXXX03` --instance-type `m5.xlarge` --instance-count `3`
```

When you specify the instance count without using the
`--instance-groups` parameter, a single
primary node is launched, and the remaining instances are
launched as core nodes. All nodes use the instance type
specified in the command.

###### Note

If you have not previously created the default Amazon EMR
service role and EC2 instance profile, type `aws
 emr create-default-roles` to create them
before typing the `create-cluster`
subcommand.

## Ensuring available IP addresses for an EMR cluster on EC2

To ensure that a subnet with enough free IP addresses is available when you launch, the EC2 subnet selection checks IP availability. It
The creation process uses a subnet with the necessary count of IP address to launch core, primary and task nodes as required, even if upon initial creation, only core nodes for the
cluster are created. EMR checks the number of IP addresses required to launch primary and task nodes during creation, as well as calculating separately the number of IP
addresses needed to launch core nodes. The minimum number of primary and task instances or nodes required is determined automatically by Amazon EMR.

###### Important

If no subnets in the VPC have enough available IPs to accommodate essential nodes, an error is returned and the
cluster isn't created.

In most deployment cases, there is a time difference between each launch of core, primary and task nodes. Additionally, it's possible for multiple clusters
to share a subnet. In these cases, IP-address availability can fluctuate and subsequent task-node launches, for instance, can be limited
by available IP addresses.
