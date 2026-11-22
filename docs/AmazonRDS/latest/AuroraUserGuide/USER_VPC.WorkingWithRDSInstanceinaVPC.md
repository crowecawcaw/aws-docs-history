

# Working with a DB cluster in a VPC

Most Aurora DB clusters are in a virtual private cloud (VPC). A VPC is a virtual network that is logically isolated from other virtual networks in the AWS Cloud. Amazon VPC makes it possible for you to launch AWS resources, such as an Amazon Aurora DB cluster or Amazon EC2 instance, into a VPC. The VPC can either be a default VPC that comes with your account or one that you create. All VPCs are associated with your AWS account. 

Aurora PostgreSQL DB clusters can also run without VPC networking. You connect to them over the internet through the internet access gateway. You can move a DB cluster into a VPC, out of a VPC, or to a different VPC without changing its endpoint. For more information, see [Updating the VPC for a DB cluster](#USER_VPC.WorkingWithRDSInstanceinaVPC.UpdatingVPC), [Moving a DB cluster out of a VPC](#USER_VPC.WorkingWithRDSInstanceinaVPC.MoveOutOfVPC), and [Moving a DB cluster into a VPC](#USER_VPC.WorkingWithRDSInstanceinaVPC.MoveIntoVPC).

Your default VPC has three subnets that you can use to isolate resources inside the VPC. The default VPC also has an internet gateway that can be used to provide access to resources inside the VPC from outside the VPC. 

For a list of scenarios involving Amazon Aurora DB clusters in a VPC , see [Scenarios for accessing a DB cluster in a VPC](USER_VPC.Scenarios.md). 

**Topics**
+ [Working with a DB cluster in a VPC](#Overview.RDSVPC.Create)
+ [VPC encryption control](#USER_VPC.EncryptionControl)
+ [Working with DB subnet groups](#USER_VPC.Subnets)
+ [Shared subnets](#USER_VPC.Shared_subnets)
+ [Amazon Aurora IP addressing](#USER_VPC.IP_addressing)
+ [Hiding a DB cluster in a VPC from the internet](#USER_VPC.Hiding)
+ [Creating a DB cluster in a VPC](#USER_VPC.InstanceInVPC)
+ [Updating the VPC for a DB cluster](#USER_VPC.WorkingWithRDSInstanceinaVPC.UpdatingVPC)
+ [Moving a DB cluster out of a VPC](#USER_VPC.WorkingWithRDSInstanceinaVPC.MoveOutOfVPC)
+ [Moving a DB cluster into a VPC](#USER_VPC.WorkingWithRDSInstanceinaVPC.MoveIntoVPC)

In the following tutorials, you can learn to create a VPC that you can use for a common Amazon Aurora scenario:
+ [Tutorial: Create a VPC for use with a DB cluster (IPv4 only)](CHAP_Tutorials.WebServerDB.CreateVPC.md)
+ [Tutorial: Create a VPC for use with a DB cluster (dual-stack mode)](CHAP_Tutorials.CreateVPCDualStack.md)

## Working with a DB cluster in a VPC
<a name="Overview.RDSVPC.Create"></a>

Here are some tips on working with a DB cluster in a VPC:
+ Your VPC must have at least two subnets. These subnets must be in two different Availability Zones in the AWS Region where you want to deploy your DB cluster. A *subnet* is a segment of a VPC's IP address range that you can specify and that you can use to group DB clusters based on your security and operational needs. 
+ If you want your DB cluster in the VPC to be publicly accessible, make sure to turn on the VPC attributes *DNS hostnames* and *DNS resolution*. 
+ Your VPC must have a DB subnet group that you create. You create a DB subnet group by specifying the subnets you created. Amazon Aurora chooses a subnet and an IP address within that subnet to associate with the primary DB instance in your DB cluster. The primary DB instance uses the Availability Zone that contains the subnet.
+ Your VPC must have a VPC security group that allows access to the DB cluster.

  For more information, see [Scenarios for accessing a DB cluster in a VPC](USER_VPC.Scenarios.md).
+ The CIDR blocks in each of your subnets must be large enough to accommodate spare IP addresses for Amazon Aurora to use during maintenance activities, including failover and compute scaling. For example, a range such as 10.0.0.0/24 and 10.0.1.0/24 is typically large enough.
+ A VPC can have an *instance tenancy* attribute of either *default* or *dedicated*. All default VPCs have the instance tenancy attribute set to default, and a default VPC can support any DB instance class.

  If you choose to have your DB cluster in a dedicated VPC where the instance tenancy attribute is set to dedicated, the DB instance class of your DB cluster must be one of the approved Amazon EC2 dedicated instance types. For example, the r5.large EC2 dedicated instance corresponds to the db.r5.large DB instance class. For information about instance tenancy in a VPC, see [Dedicated instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html) in the *Amazon Elastic Compute Cloud User Guide*.

  For more information about the instance types that can be in a dedicated instance, see [Amazon EC2 dedicated instances](https://aws.amazon.com/ec2/purchasing-options/dedicated-instances/) on the Amazon EC2 pricing page. 
**Note**  
When you set the instance tenancy attribute to dedicated for a DB cluster, it doesn't guarantee that the DB cluster will run on a dedicated host.

## VPC encryption control
<a name="USER_VPC.EncryptionControl"></a>

VPC encryption controls allow you to enforce encryption-in-transit for all network traffic within your VPCs. Use encryption control to meet regulatory compliance requirements by ensuring that only encryption-capable Nitro-based hardware can be provisioned in designated VPCs. Encryption control also catches compatibility issues at API request time rather than during provisioning. Your existing workloads continue operating and only new incompatible requests are blocked.

Set your VPC encryption controls by setting the VPC control mode to :
+ *disabled* (default)
+ *monitor*
+ *enforced*

To check the current control mode for your VPC, use the AWS Management Console or [DescribeVpcs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html) CLI or API command.

If your VPC enforces encryption, you can only provision Nitro-based DB clusters that support encryption in transit in that VPC. For more information see, [DB instance class types](Concepts.DBInstanceClass.Types.md). For information about Nitro instances, see [Instances built on the AWS Nitro System](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) in the *Amazon EC2 User Guide*.

**Note**  
If you try to provision incompatible DB clusters in an encryption-enforced VPC, Aurora returns a `VpcEncryptionControlViolationException` exception.

For Aurora Serverless for MySQL and PostreSQL, encryption control requires platform version 3 or higher.

## Working with DB subnet groups
<a name="USER_VPC.Subnets"></a>

*Subnets* are segments of a VPC's IP address range that you designate to group your resources based on security and operational needs. A *DB subnet group* is a collection of subnets (typically private) that you create in a VPC and that you then designate for your DB clusters. By using a DB subnet group, you can specify a particular VPC when creating DB clusters using the AWS CLI or RDS API. If you use the console, you can choose the VPC and subnet groups you want to use.

Each DB subnet group should have subnets in at least two Availability Zones in a given AWS Region. When creating a DB cluster in a VPC, you choose a DB subnet group for it. From the DB subnet group, Amazon Aurora chooses a subnet and an IP address within that subnet to associate with the primary DB instance in your DB cluster. The DB uses the Availability Zone that contains the subnet. Aurora assigns an IP address from a subnet that has free IP address space.

The subnets in a DB subnet group are either public or private. Whether a subnet is public or private depends on the configuration that you set for its network access control lists (network ACLs) and route tables. For a DB cluster to be publicly accessible, all of the subnets in its DB subnet group must be public. Don't mix public and private subnets in the DB subnet group of a publicly accessible DB cluster. Aurora chooses a subnet from the DB subnet group for each DB instance in the cluster. If a DB instance in a private subnet becomes the writer instance during a failover, clients outside the VPC can't connect to the cluster. Likewise, if you change a subnet in the DB subnet group from public to private, DB instances in that subnet are no longer reachable from outside the VPC.

To create a DB subnet group that supports dual-stack mode, make sure that each subnet that you add to the DB subnet group has an Internet Protocol version 6 (IPv6) CIDR block associated with it. For more information, see [Amazon Aurora IP addressing](#USER_VPC.IP_addressing) and [Migrating to IPv6](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html) in the *Amazon VPC User Guide.*

When Amazon Aurora creates a DB cluster in a VPC, it assigns a network interface to your DB cluster by using an IP address from your DB subnet group. However, we strongly recommend that you use the Domain Name System (DNS) name to connect to your DB cluster. We recommend this because the underlying IP address changes during failover. 

**Note**  
For each DB cluster that you run in a VPC, make sure to reserve at least one address in each subnet in the DB subnet group for use by Amazon Aurora for recovery actions. 

## Shared subnets
<a name="USER_VPC.Shared_subnets"></a>

You can create a DB cluster in a shared VPC.

Some considerations to keep in mind while using shared VPCs:
+ You can move a DB cluster from a shared VPC subnet to a non-shared VPC subnet and vice-versa.
+ You can move a DB cluster into a shared VPC. The DB subnet group must be in the DB cluster's account, and you must specify the VPC security groups. For more information, see [Updating the VPC for a DB cluster](#USER_VPC.WorkingWithRDSInstanceinaVPC.UpdatingVPC).
+ Participants in a shared VPC must create a security group in the VPC to allow them to create a DB cluster.
+ Owners and participants in a shared VPC can access the database by using SQL queries. However, only the creator of a resource can make any API calls on the resource.



## Amazon Aurora IP addressing
<a name="USER_VPC.IP_addressing"></a>

IP addresses enable resources in your VPC to communicate with each other, and with resources over the internet. Amazon Aurora supports both IPv4 and IPv6 addressing protocols. By default, Amazon Aurora and Amazon VPC use the IPv4 addressing protocol. You can't turn off this behavior. When you create a VPC, make sure to specify an IPv4 CIDR block (a range of private IPv4 addresses). You can optionally assign an IPv6 CIDR block to your VPC and subnets, and assign IPv6 addresses from that block to DB clusters in your subnet.

Support for the IPv6 protocol expands the number of supported IP addresses. By using the IPv6 protocol, you ensure that you have sufficient available addresses for the future growth of the internet. New and existing RDS resources can use IPv4 and IPv6 addresses within your VPC. Configuring, securing, and translating network traffic between the two protocols used in different parts of an application can cause operational overhead. You can standardize on the IPv6 protocol for Amazon RDS resources to simplify your network configuration.

**Topics**
+ [IPv4 addresses](#USER_VPC.IP_addressing.IPv4)
+ [IPv6 addresses](#USER_VPC.IP_addressing.IPv6)
+ [Dual-stack mode](#USER_VPC.IP_addressing.dual-stack-mode)

### IPv4 addresses
<a name="USER_VPC.IP_addressing.IPv4"></a>

When you create a VPC, you must specify a range of IPv4 addresses for the VPC in the form of a CIDR block, such as `10.0.0.0/16`. A *DB subnet group* defines the range of IP addresses in this CIDR block that a DB cluster can use. These IP addresses can be private or public.

A private IPv4 address is an IP address that's not reachable over the internet. You can use private IPv4 addresses for communication between your DB cluster and other resources, such as Amazon EC2 instances, in the same VPC. Each DB cluster has a private IP address for communication in the VPC.

A public IP address is an IPv4 address that's reachable from the internet. You can use public addresses for communication between your DB cluster and resources on the internet, such as a SQL client. You control whether your DB cluster receives a public IP address.

Amazon RDS uses Public Elastic IPv4 addresses from EC2's public IPv4 address pool for publicly accessible database instances. These IP addresses are visible in your AWS account when using the `describe-addresses` CLI, API or viewing the Elastic IPs (EIP) section in the AWS Management Console. Each RDS-managed IP address is marked with a `service_managed` attribute set to `"rds"`.

While these IPs are visible in your account, they remain fully managed by Amazon RDS and cannot be modified or released. Amazon RDS releases IPs back into the public IPv4 address pool when no longer in use.

CloudTrail logs API calls related to RDS's EIP, such as the `AllocateAddress`. These API calls are invoked by the Service Principal `rds.amazonaws.com`.

**Note**  
IPs allocated by Amazon RDS do not count against your account's EIP limits.

For a tutorial that shows you how to create a VPC with only private IPv4 addresses that you can use for a common Amazon Aurora scenario, see [Tutorial: Create a VPC for use with a DB cluster (IPv4 only)](CHAP_Tutorials.WebServerDB.CreateVPC.md). 

### IPv6 addresses
<a name="USER_VPC.IP_addressing.IPv6"></a>

You can optionally associate an IPv6 CIDR block with your VPC and subnets, and assign IPv6 addresses from that block to the resources in your VPC. Each IPv6 address is globally unique. 

The IPv6 CIDR block for your VPC is automatically assigned from Amazon's pool of IPv6 addresses. You can't choose the range yourself.

When connecting to an IPv6 address, make sure that the following conditions are met:
+ The client is configured so that client to database traffic over IPv6 is allowed.
+ RDS security groups used by the DB instance are configured correctly so that client to database traffic over IPv6 is allowed.
+ The client operating system stack allows traffic on the IPv6 address, and operating system drivers and libraries are configured to choose the correct default DB instance endpoint (either IPv4 or IPv6).

For more information about IPv6, see [ IP Addressing](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html) in the *Amazon VPC User Guide*.

### Dual-stack mode
<a name="USER_VPC.IP_addressing.dual-stack-mode"></a>

A DB cluster runs in dual-stack mode when it can communicate over both IPv4 and IPv6 addressing protocols. Resources can then communicate with the DB cluster using either IPv4, IPv6, or both protocols. Private dual-stack mode DB instances have IPv6 endpoints that RDS restricts to VPC access only, ensuring your IPv6 endpoints remain private. Public dual-stack mode DB instances provide both IPv4 and IPv6 endpoints that you can access from the internet.

**Topics**
+ [Dual-stack mode and DB subnet groups](#USER_VPC.IP_addressing.dual-stack-db-subnet-groups)
+ [Working with dual-stack mode DB instances](#USER_VPC.IP_addressing.dual-stack-working-with)
+ [Modifying IPv4-only DB clusters to use dual-stack mode](#USER_VPC.IP_addressing.dual-stack-modifying-ipv4)
+ [Availability of dual-stack network DB clusters](#USER_VPC.IP_addressing.dual-stack-availability)
+ [Limitations for dual-stack network DB clusters](#USER_VPC.IP_addressing.dual-stack-limitations)

For a tutorial that shows you how to create a VPC with both IPv4 and IPv6 addresses that you can use for a common Amazon Aurora scenario, see [Tutorial: Create a VPC for use with a DB cluster (dual-stack mode)](CHAP_Tutorials.CreateVPCDualStack.md). 

#### Dual-stack mode and DB subnet groups
<a name="USER_VPC.IP_addressing.dual-stack-db-subnet-groups"></a>

To use dual-stack mode, make sure that each subnet in the DB subnet group that you associate with the DB cluster has an IPv6 CIDR block associated with it. You can create a new DB subnet group or modify an existing DB subnet group to meet this requirement. After a DB cluster is in dual-stack mode, clients can connect to it normally. Make sure that client security firewalls and RDS DB instance security groups are accurately configured to allow traffic over IPv6. To connect, clients use the DB cluster primary instance's endpoint. Client applications can specify which protocol is preferred when connecting to a database. In dual-stack mode, the DB cluster detects the client's preferred network protocol, either IPv4 or IPv6, and uses that protocol for the connection.

If a DB subnet group stops supporting dual-stack mode because of subnet deletion or CIDR disassociation, there's a risk of an incompatible network state for DB instances that are associated with the DB subnet group. Also, you can't use the DB subnet group when you create a new dual-stack mode DB cluster.

To determine whether a DB subnet group supports dual-stack mode by using the AWS Management Console, view the **Network type** on the details page of the DB subnet group. To determine whether a DB subnet group supports dual-stack mode by using the AWS CLI, run the [describe-db-subnet-groups](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-subnet-groups.html) command and view `SupportedNetworkTypes` in the output.

Read replicas are treated as independent DB instances and can have a network type that's different from the primary DB instance. If you change the network type of a read replica's primary DB instance, the read replica isn't affected. When you are restoring a DB instance, you can restore it to any network type that's supported.

#### Working with dual-stack mode DB instances
<a name="USER_VPC.IP_addressing.dual-stack-working-with"></a>

When you create or modify a DB cluster, you can specify dual-stack mode to allow your resources to communicate with your DB cluster over IPv4, IPv6, or both.

When you use the AWS Management Console to create or modify a DB instance, you can specify dual-stack mode in the **Network type** section. The following image shows the **Network type** section in the console.

![Network type section in the console with Dual-stack mode selected.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/dual-stack-mode.png)


When you use the AWS CLI to create or modify a DB cluster, set the `--network-type` option to `DUAL` to use dual-stack mode. When you use the RDS API to create or modify a DB cluster, set the `NetworkType` parameter to `DUAL` to use dual-stack mode. When you are modifying the network type of a DB instance, downtime is possible. If dual-stack mode isn't supported by the specified DB engine version or DB subnet group, the `NetworkTypeNotSupported` error is returned.

For more information about creating a DB cluster, see [Creating an Amazon Aurora DB cluster](Aurora.CreateInstance.md). For more information about modifying a DB cluster, see [Modifying an Amazon Aurora DB cluster](Aurora.Modifying.md).

To determine whether a DB cluster is in dual-stack mode by using the console, view the **Network type** on the **Connectivity & security** tab for the DB cluster.

#### Modifying IPv4-only DB clusters to use dual-stack mode
<a name="USER_VPC.IP_addressing.dual-stack-modifying-ipv4"></a>

You can modify an IPv4-only DB cluster to use dual-stack mode. To do so, change the network type of the DB cluster. The modification might result in downtime.

It is recommended that you change the network type of your Amazon Aurora DB clusters during a maintenance window. Currently, setting the network type of new instances to dual-stack mode isn't supported. You can set network type manually by using the `modify-db-cluster` command. 

Before modifying a DB cluster to use dual-stack mode, make sure that its DB subnet group supports dual-stack mode. If the DB subnet group associated with the DB cluster doesn't support dual-stack mode, specify a different DB subnet group that supports it when you modify the DB cluster. Modifying the DB subnet group of a DB cluster can cause downtime.

If you modify the DB subnet group of a DB cluster before you change the DB cluster to use dual-stack mode, make sure that the DB subnet group is valid for the DB cluster before and after the change. 

We recommend that you run the [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) API with only the `--network-type` parameter with value `DUAL` to change the network of an Amazon Aurora cluster to dual-stack mode. Adding other parameters along with the `--network-type` parameter in the same API call could result in downtime.

If you can't connect to the DB cluster after the change, make sure that the client and database security firewalls and route tables are accurately configured to allow traffic to the database on the selected network (either IPv4 or IPv6). You might also need to modify operating system parameter, libraries, or drivers to connect using an IPv6 address.

**To modify an IPv4-only DB cluster to use dual-stack mode**

1. Modify a DB subnet group to support dual-stack mode, or create a DB subnet group that supports dual-stack mode:

   1. Associate an IPv6 CIDR block with your VPC.

      For instructions, see [ Add an IPv6 CIDR block to your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/modify-vpcs.html#vpc-associate-ipv6-cidr) in the *Amazon VPC User Guide*.

   1. Attach the IPv6 CIDR block to all of the subnets in your the DB subnet group.

      For instructions, see [ Add an IPv6 CIDR block to your subnet](https://docs.aws.amazon.com/vpc/latest/userguide/modify-subnets.html#subnet-associate-ipv6-cidr) in the *Amazon VPC User Guide*.

   1. Confirm that the DB subnet group supports dual-stack mode.

      If you are using the AWS Management Console, select the DB subnet group, and make sure that the **Supported network types** value is **Dual, IPv4**.

      If you are using the AWS CLI, run the [describe-db-subnet-groups](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-subnet-groups.html) command, and make sure that the `SupportedNetworkType` value for the DB instance is `Dual, IPv4`.

1. Modify the security group associated with the DB cluster to allow IPv6 connections to the database, or create a new security group that allows IPv6 connections.

   For instructions, see [ Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html) in the *Amazon VPC User Guide*.

1. Modify the DB cluster to support dual-stack mode. To do so, set the **Network type** to **Dual-stack mode**.

   If you are using the console, make sure that the following settings are correct:
   + **Network type** – **Dual-stack mode**  
![Network type section in the console with Dual-stack mode selected.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/dual-stack-mode.png)
   + **DB subnet group** – The DB subnet group that you configured in a previous step
   + **Security group** – The security that you configured in a previous step

   If you are using the AWS CLI, make sure that the following settings are correct:
   + `--network-type` – `dual`
   + `--db-subnet-group-name` – The DB subnet group that you configured in a previous step
   + `--vpc-security-group-ids` – The VPC security group that you configured in a previous step

   For example: 

   ```
   aws rds modify-db-cluster --db-cluster-identifier my-cluster --network-type "DUAL"
   ```

1. Confirm that the DB cluster supports dual-stack mode.

   If you are using the console, choose the **Configuration** tab for the DB cluster. On that tab, make sure that the **Network type** value is **Dual-stack mode**.

   If you are using the AWS CLI, run the [ describe-db-clusters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html) command, and make sure that the `NetworkType` value for the DB cluster is `dual`.

   Run the `dig` command on the writer DB instance endpoint to identify the IPv6 address associated with it.

   ```
   dig {{db-instance-endpoint}} AAAA
   ```

   Use the writer DB instance endpoint, not the IPv6 address, to connect to the DB cluster.

#### Availability of dual-stack network DB clusters
<a name="USER_VPC.IP_addressing.dual-stack-availability"></a>

Dual-stack network DB clusters are available in all AWS Regions except for the following:
+ Asia Pacific (Hyderabad)
+ Asia Pacific (Malaysia)
+ Asia Pacific (Melbourne)
+ Asia Pacific (Thailand)
+ Canada West (Calgary)
+ Europe (Spain)
+ Europe (Zurich)
+ Israel (Tel Aviv)
+ Mexico (Central)
+ Middle East (UAE)

The following DB engine versions support dual-stack network DB clusters:
+ Aurora MySQL versions: 
  + 3.02 and higher 3 versions
  + 2.09.1 and higher 2 versions

  For more information about Aurora MySQL versions, see the [*Release Notes for Aurora MySQL*](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/Welcome.html).
+ Aurora PostgreSQL versions:
  + 15.2 and all higher versions
  + 14.3 and higher 14 versions
  + 13.7 and higher 13 versions

  For more information about Aurora PostgreSQL versions, see the [*Release Notes for Aurora PostgreSQL*](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/Welcome.html).

#### Limitations for dual-stack network DB clusters
<a name="USER_VPC.IP_addressing.dual-stack-limitations"></a>

The following limitations apply to dual-stack network DB clusters:
+ DB clusters can't use the IPv6 protocol exclusively. They can use IPv4 exclusively, or they can use the IPv4 and IPv6 protocol (dual-stack mode).
+ Amazon RDS doesn't support native IPv6 subnets.
+ You can't use RDS Proxy with dual-stack mode DB clusters.

## Hiding a DB cluster in a VPC from the internet
<a name="USER_VPC.Hiding"></a>

One common Amazon Aurora scenario is to have a VPC in which you have an Amazon EC2 instance with a public-facing web application and a DB cluster with a database that isn't publicly accessible. For example, you can create a VPC that has a public subnet and a private subnet. EC2 instances that function as web servers can be deployed in the public subnet. The DB clusters are deployed in the private subnet. In such a deployment, only the web servers have access to the DB clusters. For an illustration of this scenario, see [A DB cluster in a VPC accessed by an Amazon EC2 instance in the same VPC](USER_VPC.Scenarios.md#USER_VPC.Scenario1). 

When you launch a DB cluster inside a VPC, the DB cluster has a private IP address for traffic inside the VPC. This private IP address isn't publicly accessible. You can use the **Public access** option to designate whether the DB cluster also has a public IP address in addition to the private IP address. If the DB cluster is designated as publicly accessible, its DNS endpoint resolves to the private IP address from within the VPC. It resolves to the public IP address from outside of the VPC. Access to the DB cluster is ultimately controlled by the security group it uses. That public access is not permitted if the security group assigned to the DB cluster doesn't include inbound rules that permit it. In addition, for a DB cluster to be publicly accessible, the subnets in its DB subnet group must have an internet gateway. For more information, see [Can't connect to Amazon RDS DB instance](CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting)

You can modify a DB cluster to turn on or off public accessibility by modifying the **Public access** option. The following illustration shows the **Public access** option in the **Additional connectivity configuration** section. To set the option, open the **Additional connectivity configuration** section in the **Connectivity** section. 

![Set your database Public access option in the Additional connectivity configuration section to No.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/VPC-example4.png)


For information about modifying a DB instance to set the **Public access** option, see [Modifying a DB instance in a DB cluster](Aurora.Modifying.md#Aurora.Modifying.Instance).

## Creating a DB cluster in a VPC
<a name="USER_VPC.InstanceInVPC"></a>

The following procedures help you create a DB cluster in a VPC. To use the default VPC, you can begin with step 2, and use the VPC and DB subnet group have already been created for you. If you want to create an additional VPC, you can create a new VPC. 

**Note**  
If you want your DB cluster in the VPC to be publicly accessible, you must update the DNS information for the VPC by enabling the VPC attributes *DNS hostnames* and *DNS resolution*. For information about updating the DNS information for a VPC instance, see [Updating DNS support for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html). 

Follow these steps to create a DB instance in a VPC:
+ [Step 1: Create a VPC](#USER_VPC.CreatingVPC) 
+  [Step 2: Create a DB subnet group](#USER_VPC.CreateDBSubnetGroup)
+  [Step 3: Create a VPC security group](#USER_VPC.CreateVPCSecurityGroup)
+  [Step 4: Create a DB instance in the VPC](#USER_VPC.CreateDBInstanceInVPC) 

### Step 1: Create a VPC
<a name="USER_VPC.CreatingVPC"></a>

Create a VPC with subnets in at least two Availability Zones. You use these subnets when you create a DB subnet group. If you have a default VPC, a subnet is automatically created for you in each Availability Zone in the AWS Region.

For more information, see [Create a VPC with private and public subnets](CHAP_Tutorials.WebServerDB.CreateVPC.md#CHAP_Tutorials.WebServerDB.CreateVPC.VPCAndSubnets), or see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#Create-VPC) in the *Amazon VPC User Guide*. 

### Step 2: Create a DB subnet group
<a name="USER_VPC.CreateDBSubnetGroup"></a>

A DB subnet group is a collection of subnets (typically private) that you create for a VPC and that you then designate for your DB clusters. A DB subnet group allows you to specify a particular VPC when you create DB clusters using the AWS CLI or RDS API. If you use the console, you can just choose the VPC and subnets you want to use. Each DB subnet group must have at least one subnet in at least two Availability Zones in the AWS Region. As a best practice, each DB subnet group should have at least one subnet for every Availability Zone in the AWS Region.

For a DB cluster to be publicly accessible, the subnets in the DB subnet group must have an internet gateway. For more information about internet gateways for subnets, see [Connect to the internet using an internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*. 

When you create a DB cluster in a VPC, you can choose a DB subnet group. Amazon Aurora chooses a subnet and an IP address within that subnet to associate with your DB cluster. If no DB subnet groups exist, Amazon Aurora creates a default subnet group when you create a DB cluster. Amazon Aurora creates and associates an Elastic Network Interface to your DB cluster with that IP address. The DB cluster uses the Availability Zone that contains the subnet.

In this step, you create a DB subnet group and add the subnets that you created for your VPC.

**To create a DB subnet group**

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Subnet groups**.

1. Choose **Create DB Subnet Group**.

1. For **Name**, type the name of your DB subnet group.

1. For **Description**, type a description for your DB subnet group. 

1. For **VPC**, choose the default VPC or the VPC that you created.

1. In the **Add subnets** section, choose the Availability Zones that include the subnets from **Availability Zones**, and then choose the subnets from **Subnets**.  
![Create a DB subnet group.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/RDSVPC101.png)

1. Choose **Create**. 

   Your new DB subnet group appears in the DB subnet groups list on the RDS console. You can choose the DB subnet group to see details, including all of the subnets associated with the group, in the detail pane. 

### Step 3: Create a VPC security group
<a name="USER_VPC.CreateVPCSecurityGroup"></a>

Before you create your DB cluster, you can create a VPC security group to associate with your DB cluster. If you don't create a VPC security group, you can use the default security group when you create a DB cluster. For instructions on how to create a security group for your DB cluster, see [Create a VPC security group for a private DB cluster](CHAP_Tutorials.WebServerDB.CreateVPC.md#CHAP_Tutorials.WebServerDB.CreateVPC.SecurityGroupDB), or see [Control traffic to resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon VPC User Guide*. 

### Step 4: Create a DB instance in the VPC
<a name="USER_VPC.CreateDBInstanceInVPC"></a>

In this step, you create a DB cluster and use the VPC name, the DB subnet group, and the VPC security group you created in the previous steps.

**Note**  
If you want your DB cluster in the VPC to be publicly accessible, you must enable the VPC attributes *DNS hostnames* and *DNS resolution*. For more information, see [DNS attributes for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html) in the *Amazon VPC User Guide*.

For details on how to create a DB cluster, see [Creating an Amazon Aurora DB cluster](Aurora.CreateInstance.md).

When prompted in the **Connectivity** section, enter the VPC name, the DB subnet group, and the VPC security group.

**Note**  
After you create a DB cluster, you can move it to a different VPC. For more information, see [Updating the VPC for a DB cluster](#USER_VPC.WorkingWithRDSInstanceinaVPC.UpdatingVPC).

## Updating the VPC for a DB cluster
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.UpdatingVPC"></a>

For Aurora PostgreSQL and Aurora MySQL DB clusters, you can move a DB cluster from one VPC to another. For example, you might move a cluster from a development VPC to a production VPC, or consolidate clusters into a shared VPC. You move the cluster by modifying it and specifying a DB subnet group in the destination VPC. You don't need to take a snapshot and restore it into a new cluster.

The cluster endpoint and the reader endpoint don't change. Aurora moves all DB instances in the DB cluster. The cluster uses VPC networking before and after the move. Aurora doesn't turn on the internet access gateway.

The same process runs whenever you change the DB subnet group, even if the new DB subnet group is in the same VPC. The connectivity interruption and the other requirements in this section also apply to that change. If you specify the DB subnet group that the DB cluster already uses, the cluster isn't moved.

**Important**  
Connectivity to the DB cluster is interrupted while Aurora moves it to the new VPC. Apply the change immediately at a time when an interruption is acceptable, or let Aurora apply it during the next maintenance window. After the move, the IP addresses of the DB instances change. Make sure that your applications connect by using the endpoint DNS name, not an IP address, and that they can reach the new VPC.

### Before you begin
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.UpdatingVPC.BeforeYouBegin"></a>
+ **Create a DB subnet group in the destination VPC.** The DB subnet group must have a subnet with available IP addresses in each Availability Zone where the cluster has a DB instance. To find these Availability Zones, run `aws rds describe-db-instances --filters Name=db-cluster-id,Values={{cluster}} --query "DBInstances[].AvailabilityZone"`. If you plan to add DB instances in other Availability Zones later, include subnets in those zones too. For more information, see [Working with DB subnet groups](#USER_VPC.Subnets).
+ **Create VPC security groups in the destination VPC.** The security groups must belong to the VPC of the destination DB subnet group, and must allow your clients to connect on the database port. If you don't specify security groups, Aurora uses the default security group of the destination VPC. If the destination is a shared VPC, you must specify the security groups. If you change the DB subnet group within the same VPC and want to keep the current security groups, specify their IDs. Otherwise, the default security group replaces them.
+ **Choose the network type.** If you don't specify a network type, the cluster uses IPv4 after the move. To keep a Dual-stack cluster in Dual-stack mode, specify the Dual-stack network type. You can use Dual-stack mode only if the destination subnets support it. For more information, see [Amazon Aurora IP addressing](#USER_VPC.IP_addressing).
+ **If any DB instance is publicly accessible, prepare the destination VPC for it.** Public access stays turned on after the move, and the DB instance gets a new public IP address. Make sure that the destination VPC has an internet gateway and that the destination subnets have a route to it. Aurora doesn't check this before the move. If the destination subnets have no route to an internet gateway, the move completes, but you can't reach the DB instance from the internet. If the destination VPC has no internet gateway, the move fails, and the DB instances are unavailable. Make sure that the destination VPC has an internet gateway before you move the cluster.
+ **Remove or turn off features that the move doesn't support.** The request fails if the DB cluster has any of the following. Set them up again in the new VPC after the move, if needed.
  + Membership in an Aurora global database
  + Aurora Limitless Database
  + Enhanced binlog (Aurora MySQL) or enhanced logical replication (Aurora PostgreSQL) turned on in the DB cluster parameter group
  + Babelfish for Aurora PostgreSQL (turned on, or a change pending)
  + An in-Region or cross-Region read replica relationship, whether the DB cluster is the source or the replica (Aurora Replicas inside the DB cluster aren't affected)
  + A database activity stream that isn't stopped
  + Registration as an RDS Proxy target
  + An active zero-ETL integration
  + A blue/green deployment
+ **Apply pending changes first.** If the DB cluster has a pending change to its DB cluster parameter group, or to a Babelfish, enhanced binlog, or enhanced logical replication parameter, apply it before you move the cluster. Wait until any pending VPC networking or internet access gateway change is complete.
+ **Make sure that all DB instances in the DB cluster are available.** If a DB instance is in the incompatible-network state when the move starts, the move fails and the whole DB cluster can enter that state.
+ **Don't delete or change the subnets or security groups in the current VPC until the move is complete.** Aurora needs them to return the cluster to the current VPC if the move fails.
+ **Plan client connectivity in the destination VPC.** Clients must be able to reach the new VPC, for example from resources in the VPC, or through VPC peering, AWS Transit Gateway, AWS Site-to-Site VPN, or Direct Connect.
+ **Check your IAM permissions.** See [IAM permissions](#USER_VPC.WorkingWithRDSInstanceinaVPC.UpdatingVPC.IAM).

### IAM permissions
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.UpdatingVPC.IAM"></a>

To move a DB cluster to a different VPC, you need permission for `rds:ModifyDBCluster` on the DB cluster and on the destination DB subnet group. You don't need the `rds:EnableVpcNetworking` permission unless you also specify `--enable-vpc-networking`.

To apply a scheduled move immediately, you also need permission for `rds:EnableVpcNetworking`.

### Console
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.UpdatingVPC.Console"></a>

**To move a DB cluster to a different VPC**

1. Sign in to the AWS Management Console and open the [Amazon RDS console](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the DB cluster that you want to move.

1. Choose **Modify**.

1. In the **Connectivity** section, for **Virtual private cloud (VPC)**, choose the destination VPC.

1. For **DB subnet group**, choose a DB subnet group in the destination VPC.

1. For **VPC security group (firewall)**, choose one or more security groups in the destination VPC. Optionally, change the **Network type**.

1. Choose **Continue** and review the summary of modifications.

1. To move the cluster now, choose **Apply immediately**. Otherwise, Aurora moves the cluster during the next maintenance window.

1. Choose **Modify cluster**.

The cluster status changes to `modifying` during the move. When the status returns to `available`, the DB cluster is in the new VPC.

### AWS CLI
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.UpdatingVPC.CLI"></a>

Call the [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) command and specify the following options:
+ `--db-cluster-identifier` – the DB cluster to move.
+ `--db-subnet-group-name` – a DB subnet group in the destination VPC.
+ `--vpc-security-group-ids` (optional) – one or more security groups in the destination VPC. Required if the destination is a shared VPC.
+ `--network-type` (optional) – `IPV4` or `DUAL`. If you omit it, the cluster uses IPv4.
+ `--apply-immediately` (optional) – move the cluster now. If you specify `--no-apply-immediately` or omit the option, Aurora moves the cluster during the next maintenance window.

Don't specify `--no-enable-vpc-networking`. That option turns off VPC networking, and combining it with a DB subnet group is rejected. You don't need to specify `--enable-vpc-networking` or the internet access gateway options.

Example:

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --db-cluster-identifier mydbcluster \
    --db-subnet-group-name mysubnetgroup-vpc2 \
    --vpc-security-group-ids sg-0abcd1234efgh5678 \
    --network-type DUAL \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-cluster ^
    --db-cluster-identifier mydbcluster ^
    --db-subnet-group-name mysubnetgroup-vpc2 ^
    --vpc-security-group-ids sg-0abcd1234efgh5678 ^
    --network-type DUAL ^
    --apply-immediately
```

Because the change is asynchronous, the response still shows the cluster's current DB subnet group and security groups.

### RDS API
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.UpdatingVPC.API"></a>

Call the ModifyDBCluster operation. Specify `DBClusterIdentifier` and a `DBSubnetGroupName` in the destination VPC. Optionally, specify `VpcSecurityGroupIds` in the destination VPC and `NetworkType`. Set `ApplyImmediately` to `true` to move the cluster now, or to `false` to move it during the next maintenance window. Don't set `EnableVPCNetworking` to `false`.

### Verifying the move
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.UpdatingVPC.Verifying"></a>

Run the [describe-db-clusters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html) command:

For Linux, macOS, or Unix:

```
aws rds describe-db-clusters \
    --db-cluster-identifier mydbcluster \
    --query "DBClusters[0].[Status,DBSubnetGroup,VpcSecurityGroups,NetworkType]"
```

For Windows:

```
aws rds describe-db-clusters ^
    --db-cluster-identifier mydbcluster ^
    --query "DBClusters[0].[Status,DBSubnetGroup,VpcSecurityGroups,NetworkType]"
```

When the move is complete, `Status` is `available`, and `DBSubnetGroup` and `VpcSecurityGroups` show the values in the destination VPC.

If you scheduled the move for the next maintenance window, `PendingModifiedValues` shows `VPCNetworkingEnabled: true`. It doesn't show the destination DB subnet group or security groups. While the move is pending, other VPC networking or internet access gateway changes are rejected. To apply the pending move now, run modify-db-cluster with only `--db-cluster-identifier`, `--enable-vpc-networking`, and `--apply-immediately`. Don't include `--db-subnet-group-name`, `--vpc-security-group-ids`, or `--network-type`, or the request is rejected.

### If the move doesn't complete
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.UpdatingVPC.NotComplete"></a>

If Aurora can't move the DB cluster, it returns the cluster to its original VPC and publishes an RDS event. Check the event for the cause, correct it, and try again.

If Aurora also can't restore the network configuration in the original VPC, the DB cluster and its DB instances enter the incompatible-network state, and you can't connect to the cluster. You can't take a snapshot of a DB cluster in this state, but you can restore an earlier snapshot, or do a point-in-time restore, to a new DB cluster. If the cluster status doesn't return to `available`, contact AWS Support.

Aurora publishes RDS-EVENT-0673 when the move starts, RDS-EVENT-0674 when it completes, and RDS-EVENT-0675 if it fails. If Aurora rejects the change before the move starts, it publishes RDS-EVENT-0675 without RDS-EVENT-0673. If the DB cluster enters the incompatible-network state, Aurora publishes RDS-EVENT-0676. For more information, see [Amazon RDS event categories and event messages for Aurora](USER_Events.Messages.md).

## Moving a DB cluster out of a VPC
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.MoveOutOfVPC"></a>

For Aurora PostgreSQL DB clusters, you can move a DB cluster out of its VPC so that you connect to it over the internet through the internet access gateway. For example, you might do this for a development or test cluster that you want to reach from tools outside AWS without a VPN or Direct Connect. For more information about the internet access gateway, see [Internet access gateway](CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.md#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.InternetAccessGateway).

When you move a DB cluster out of a VPC, Aurora turns off VPC networking and turns on the internet access gateway in a single operation. The cluster is never left without a connectivity path. The cluster endpoint doesn't change. After the move, the endpoint works through the internet access gateway.

**Important**  
The internet access gateway supports only IAM database authentication. After the move, the cluster must use IAM database authentication, and the master user authentication type must be IAM. Applications that connect with a database password, Secrets Manager credentials, or Kerberos authentication can't connect after the move. Before you move the cluster, update your applications to connect with IAM authentication tokens. For more information, see [IAM database authentication ](UsingWithRDS.IAMDBAuth.md).  
Connectivity to the DB cluster is briefly interrupted during the move. After the move, VPC security groups no longer apply to the cluster. Access is controlled by IAM: any IAM principal with `rds-db:connect` permission for the cluster can connect from the internet. Review your IAM policies before you move the cluster.

### Before you begin
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.MoveOutOfVPC.BeforeYouBegin"></a>
+ **Engine.** The DB cluster must be an Aurora PostgreSQL DB cluster.
+ **Change these settings first, in separate requests.** Each of these must be complete before you move the cluster out of the VPC:
  + **Network type.** The DB cluster must use IPv4. If it uses Dual-stack mode, change it to IPv4 first. You can't change the network type in the same request as the move.
  + **Kerberos authentication.** The DB cluster can't be joined to a directory. Remove it from the directory first. You can't do this in the same request as the move.
  + **Port.** The DB cluster must use the default port, 5432. If it uses another port, change it to 5432 first.
  + **Public access.** Turn off public access for every DB instance in the DB cluster.
+ **Remove or turn off features that aren't supported without VPC networking.** The request fails if the DB cluster has any of the following:
  + Membership in an Aurora global database
  + Aurora PostgreSQL Limitless Database
  + Enhanced logical replication turned on in the DB cluster parameter group
  + Babelfish for Aurora PostgreSQL (turned on, or a change pending)
  + An in-Region or cross-Region read replica relationship, whether the DB cluster is the source or the replica
  + A database activity stream that isn't stopped
  + Registration as an RDS Proxy target
  + An active zero-ETL integration
  + A blue/green deployment
+ **Apply pending changes first.** If the DB cluster has a pending change to its DB cluster parameter group, or to a Babelfish or enhanced logical replication parameter, apply it before you move the cluster. Wait until any pending VPC networking or internet access gateway change is complete.
+ **Make sure that all DB instances in the DB cluster are available.** If a DB instance is in the incompatible-network state when the move starts, the move fails and the whole DB cluster can enter that state.
+ **Don't delete or change the subnets or security groups in the current VPC until the move is complete.** Aurora needs them to return the cluster to the VPC if the move fails.
+ **Update your applications to use IAM database authentication.** See the Important notice above. If the master user password is managed in Secrets Manager, Aurora stops managing the password and deletes the secret. The master user switches to IAM database authentication right away, even if the move waits for the maintenance window, so password logins for the master user stop soon after you make the request.
+ **Plan client connectivity.** Clients that are inside a VPC need outbound internet access to reach the internet access gateway, for example through a NAT gateway or an internet gateway.
+ **Check your IAM permissions.** See [IAM permissions](#USER_VPC.WorkingWithRDSInstanceinaVPC.MoveOutOfVPC.IAM).

### IAM permissions
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.MoveOutOfVPC.IAM"></a>

To move a DB cluster out of a VPC, you need permission for the following actions on the DB cluster:
+ `rds:ModifyDBCluster`
+ `rds:DisableVpcNetworking`
+ `rds:EnableInternetAccessGateway`

These additional permissions help prevent a DB cluster from being moved out of a VPC by mistake. `rds:ModifyDBCluster` permission alone isn't enough.

To prevent DB clusters from being moved out of a VPC, deny `rds:DisableVpcNetworking` in an IAM policy or a service control policy (SCP). This also blocks creating or restoring a DB cluster with VPC networking turned off. It doesn't block creating a DB cluster with express configuration without a VPC, because that request doesn't turn off VPC networking.

### Console
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.MoveOutOfVPC.Console"></a>

**To move a DB cluster out of a VPC**

1. Sign in to the AWS Management Console and open the [Amazon RDS console](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the Aurora PostgreSQL DB cluster that you want to move.

1. Choose **Modify**.

1. In the **Connectivity** section, for **Network access type**, choose **Internet access gateway**.

1. Make sure that IAM database authentication is turned on for the DB cluster.

1. Choose **Continue** and review the summary of modifications.

1. To move the cluster now, choose **Apply immediately**. Otherwise, Aurora moves the cluster during the next maintenance window.

   If you turn on IAM database authentication in the same change, choose **Apply immediately**.

1. Choose **Modify cluster**.

The cluster status changes to `modifying` during the move. When the status returns to `available`, you can connect to the cluster through the internet access gateway. For more information, see [Connecting to clusters with express configuration](CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.md#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Connecting).

### AWS CLI
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.MoveOutOfVPC.CLI"></a>

Call the [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) command and specify `--no-enable-vpc-networking` and `--enable-internet-access-gateway` together. If the DB cluster doesn't already use IAM database authentication for the master user, also specify `--enable-iam-database-authentication` and `--master-user-authentication-type iam-db-auth`. If the master user password is managed in Secrets Manager, also specify `--no-manage-master-user-password`. If you turn on IAM database authentication in the same request, also specify `--apply-immediately`.

Don't specify `--db-subnet-group-name`, `--vpc-security-group-ids`, or `--network-type`. To move the cluster now, specify `--apply-immediately`. If you specify `--no-apply-immediately` or omit the option, Aurora moves the cluster during the next maintenance window.

Example:

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --db-cluster-identifier mydbcluster \
    --no-enable-vpc-networking \
    --enable-internet-access-gateway \
    --enable-iam-database-authentication \
    --master-user-authentication-type iam-db-auth \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-cluster ^
    --db-cluster-identifier mydbcluster ^
    --no-enable-vpc-networking ^
    --enable-internet-access-gateway ^
    --enable-iam-database-authentication ^
    --master-user-authentication-type iam-db-auth ^
    --apply-immediately
```

### RDS API
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.MoveOutOfVPC.API"></a>

Call the ModifyDBCluster operation. Set `EnableVPCNetworking` to `false` and `EnableInternetAccessGateway` to `true`. If the DB cluster doesn't already use them, set `EnableIAMDatabaseAuthentication` to `true` and `MasterUserAuthenticationType` to `iam-db-auth`. If the master user password is managed in Secrets Manager, also set `ManageMasterUserPassword` to `false`. If the request sets `EnableIAMDatabaseAuthentication`, `ApplyImmediately` must be `true`. Otherwise, set `ApplyImmediately` to `true` to move the cluster now, or to `false` to move it during the next maintenance window.

### Verifying the move
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.MoveOutOfVPC.Verifying"></a>

Run the [describe-db-clusters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html) command:

For Linux, macOS, or Unix:

```
aws rds describe-db-clusters \
    --db-cluster-identifier mydbcluster \
    --query "DBClusters[0].[Status,VPCNetworkingEnabled,InternetAccessGatewayEnabled,IAMDatabaseAuthenticationEnabled]"
```

For Windows:

```
aws rds describe-db-clusters ^
    --db-cluster-identifier mydbcluster ^
    --query "DBClusters[0].[Status,VPCNetworkingEnabled,InternetAccessGatewayEnabled,IAMDatabaseAuthenticationEnabled]"
```

When the move is complete, `Status` is `available`, `VPCNetworkingEnabled` is `false`, `InternetAccessGatewayEnabled` is `true`, and `IAMDatabaseAuthenticationEnabled` is `true`.

If you scheduled the move for the next maintenance window, it appears in `PendingModifiedValues` as `VPCNetworkingEnabled: false` and `InternetAccessGatewayEnabled: true`. While the move is pending, other VPC networking or internet access gateway changes are rejected. To apply the pending move now, run the same modify-db-cluster command again with `--apply-immediately`.

### If the move doesn't complete
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.MoveOutOfVPC.NotComplete"></a>

If Aurora can't move the DB cluster out of the VPC, it returns the cluster to its original VPC configuration and publishes an RDS event. Check the event for the cause, correct it, and try again.

If Aurora also can't restore the network configuration in the VPC, the DB cluster and its DB instances enter the incompatible-network state. You can't take a snapshot of a DB cluster in this state, but you can restore an earlier snapshot, or do a point-in-time restore, to a new DB cluster. If the cluster status doesn't return to `available`, contact AWS Support.

Aurora publishes RDS-EVENT-0673 when the move starts, RDS-EVENT-0674 when it completes, and RDS-EVENT-0675 if it fails. If Aurora rejects the change before the move starts, it publishes RDS-EVENT-0675 without RDS-EVENT-0673. If the DB cluster enters the incompatible-network state, Aurora publishes RDS-EVENT-0676. For more information, see [Amazon RDS event categories and event messages for Aurora](USER_Events.Messages.md).

## Moving a DB cluster into a VPC
<a name="USER_VPC.WorkingWithRDSInstanceinaVPC.MoveIntoVPC"></a>

If an Aurora PostgreSQL DB cluster uses the internet access gateway, for example because you created it with express configuration or moved it out of a VPC, you can move it into a VPC. Aurora turns on VPC networking and turns off the internet access gateway in a single operation, and the cluster endpoint doesn't change. For the full procedure, see [Moving a cluster with express configuration into a VPC](CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.md#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC).