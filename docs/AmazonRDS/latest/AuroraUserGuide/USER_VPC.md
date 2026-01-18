# Working with a DB cluster in a VPC

Your DB cluster is in a virtual private cloud (VPC). A VPC is a virtual network
that is logically isolated from other virtual networks in the AWS Cloud. Amazon VPC makes
it possible for you to launch AWS resources, such as an Amazon Aurora DB cluster
or Amazon EC2 instance, into a VPC. The VPC can either be a default VPC that comes with your
account or one that you create. All VPCs are associated with your AWS account.

Your default VPC has three subnets that you can use to isolate resources inside the
VPC. The default VPC also has an internet gateway that can be used to provide access to
resources inside the VPC from outside the VPC.

For a list of scenarios involving Amazon Aurora DB clusters in a VPC , see [Scenarios for accessing a DB cluster in a VPC](USER_VPC.md "USER_VPC.md").

###### Topics

- [Working with a DB cluster in a VPC](#Overview.RDSVPC.Create "#Overview.RDSVPC.Create")
- [VPC encryption control](#USER_VPC.EncryptionControl "#USER_VPC.EncryptionControl")
- [Working with DB subnet groups](#USER_VPC.Subnets "#USER_VPC.Subnets")
- [Shared subnets](#USER_VPC.Shared_subnets "#USER_VPC.Shared_subnets")
- [Amazon Aurora IP
  addressing](#USER_VPC.IP_addressing "#USER_VPC.IP_addressing")
- [Hiding a DB cluster in a VPC from
  the internet](#USER_VPC.Hiding "#USER_VPC.Hiding")
- [Creating a DB cluster in a
  VPC](#USER_VPC.InstanceInVPC "#USER_VPC.InstanceInVPC")
  In the following tutorials, you can learn to create a VPC that you can use for a
  common Amazon Aurora scenario:

- [Tutorial: Create a VPC for use with a
  DB cluster (IPv4 only)](CHAP_Tutorials.WebServerDB.md "CHAP_Tutorials.WebServerDB.md")
- [Tutorial: Create a VPC for use with a DB
  cluster (dual-stack mode)](CHAP_Tutorials.md "CHAP_Tutorials.md")

## Working with a DB cluster in a VPC

Here are some tips on working with a DB cluster in a VPC:

- Your VPC must have at least two subnets. These subnets must be in two
  different Availability Zones in the AWS Region where you want to deploy
  your DB cluster. A _subnet_ is a segment of a VPC's IP address range that you can
  specify and that you can use to group DB clusters based on
  your security and operational needs.
- If you want your DB cluster in the VPC to be publicly
  accessible, make sure to turn on the VPC attributes _DNS
  hostnames_ and _DNS resolution_.
- Your VPC must have a DB subnet group that you create. You create a DB
  subnet group by specifying the subnets you created. Amazon Aurora chooses a
  subnet and an IP address within that subnet to associate with the primary DB
  instance in your DB cluster. The primary DB instance uses the Availability
  Zone that contains the subnet.
- Your VPC must have a VPC security group that allows access to the DB
  cluster.

For more information, see [Scenarios for accessing a DB cluster in a VPC](USER_VPC.md "USER_VPC.md").

- The CIDR blocks in each of your subnets must be large enough to
  accommodate spare IP addresses for Amazon Aurora to use
  during maintenance activities, including failover and compute scaling. For
  example, a range such as 10.0.0.0/24 and 10.0.1.0/24 is typically large
  enough.
- A VPC can have an _instance tenancy_ attribute of
  either _default_ or _dedicated_. All
  default VPCs have the instance tenancy attribute set to default, and a
  default VPC can support any DB instance class.

If you choose to have your DB cluster in a
dedicated VPC where the instance tenancy attribute is set to dedicated, the
DB instance class of your DB cluster must be
one of the approved Amazon EC2 dedicated instance types. For example, the
r5.large EC2 dedicated instance corresponds to the db.r5.large DB instance
class. For information about instance tenancy in a VPC, see [Dedicated instances](../../../AWSEC2/latest/UserGuide/dedicated-instance.md "../../../AWSEC2/latest/UserGuide/dedicated-instance.md")
in the _Amazon Elastic Compute Cloud User Guide_.

For more information about the instance types that can be in
a dedicated instance, see [Amazon EC2
dedicated instances](https://aws.amazon.com/ec2/purchasing-options/dedicated-instances/ "https://aws.amazon.com/ec2/purchasing-options/dedicated-instances/") on the Amazon EC2 pricing page.

###### Note

When you set the instance tenancy attribute to dedicated for a DB
cluster, it doesn't guarantee that
the DB cluster will run on a dedicated
host.

## VPC encryption control

VPC encryption controls allow you to enforce encryption-in-transit for all network traffic within your VPCs.
Use encryption control to meet regulatory compliance requirements by ensuring that only encryption-capable
Nitro-based hardware can be provisioned in designated VPCs. Encryption control also catches compatibility issues at
API request time rather than during provisioning. Your existing workloads continue operating
and only new incompatible requests are blocked.

Set your VPC encryption controls by setting the VPC control mode to :

- _disabled_ (default)
- _monitor_
- _enforced_

To check the current control mode for your VPC, use the AWS Management Console or
[DescribeVpcs](../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md") CLI or API command.

If your VPC enforces encryption, you can only provision
Nitro-based DB clusters that support encryption in transit in that VPC.
For more information see, [DB instance class types](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md"). For information about Nitro instances, see
[Instances built on the AWS Nitro System](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md") in the
_Amazon EC2 User Guide_.

###### Note

If you try to provision incompatible DB clusters
in an encryption-enforced VPC,
Aurora
returns a `VpcEncryptionControlViolationException` exception.

For Aurora Serverless for MySQL and PostreSQL, encryption control requires platform version 3 or higher.

## Working with DB subnet groups

_Subnets_ are segments of a VPC's IP address
range that you designate to group your resources based on security and operational
needs. A _DB subnet group_ is a collection of
subnets (typically private) that you create in a VPC and that you then designate for
your DB clusters. By using a DB subnet group, you can specify a particular VPC
when creating DB clusters using the AWS CLI or RDS API. If you use the
console, you can choose the VPC and subnet groups you want to use.

Each DB subnet group should have subnets in at least two Availability Zones in a
given AWS Region. When creating a DB cluster in a VPC, you
choose a DB subnet group for it. From the DB subnet group, Amazon Aurora chooses a subnet and an IP address within that subnet to
associate with the primary DB instance in your DB cluster. The DB uses the Availability
Zone that contains the subnet. Aurora
always assigns an IP address from a
subnet that has free IP address space.

The subnets in a DB subnet group are either public or private. The subnets are
public or private, depending on the configuration that you set for their network
access control lists (network ACLs) and routing tables. For a DB cluster to be publicly accessible, all of the subnets in its DB subnet
group must be public. If a subnet that's associated with a publicly accessible DB
cluster changes from public to private, it can affect DB cluster availability.

To create a DB subnet group that supports dual-stack mode, make sure that each
subnet that you add to the DB subnet group has an Internet Protocol version 6 (IPv6)
CIDR block associated with it. For more information, see [Amazon Aurora IP
addressing](#USER_VPC.IP_addressing "#USER_VPC.IP_addressing") and
[Migrating to IPv6](../../../vpc/latest/userguide/vpc-migrate-ipv6.md "../../../vpc/latest/userguide/vpc-migrate-ipv6.md") in the _Amazon VPC User Guide._

When Amazon Aurora creates a DB cluster in a VPC, it
assigns a network interface to your DB cluster by using an IP
address from your DB subnet group. However, we strongly recommend that you use the
Domain Name System (DNS) name to connect to your DB cluster. We recommend this
because the underlying IP address changes during failover.

###### Note

For each DB cluster that you run in a VPC, make sure to
reserve at least one address in each subnet in the DB subnet group for use by
Amazon Aurora for recovery actions.

## Shared subnets

You can create a DB cluster in a shared VPC.

Some considerations to keep in mind while using shared VPCs:

- You can move a DB cluster from a shared VPC subnet to a
  non-shared VPC subnet and vice-versa.
- Participants in a shared VPC must create a security group in the VPC to
  allow them to create a DB cluster.
- Owners and participants in a shared VPC can access the database by using
  SQL queries. However, only the creator of a resource can make any API calls
  on the resource.

## Amazon Aurora IP

addressing

IP addresses enable resources in your VPC to communicate with each other, and with
resources over the internet. Amazon Aurora supports both IPv4 and IPv6 addressing
protocols. By default, Amazon Aurora and Amazon VPC use the IPv4 addressing
protocol. You can't turn off this behavior. When you create a VPC, make sure to
specify an IPv4 CIDR block (a range of private IPv4 addresses). You can optionally
assign an IPv6 CIDR block to your VPC and subnets, and assign IPv6 addresses from
that block to DB clusters in your subnet.

Support for the IPv6 protocol expands the number of supported IP addresses. By
using the IPv6 protocol, you ensure that you have sufficient available addresses for
the future growth of the internet. New and existing RDS resources can use IPv4 and
IPv6 addresses within your VPC. Configuring, securing, and translating network
traffic between the two protocols used in different parts of an application can
cause operational overhead. You can standardize on the IPv6 protocol for Amazon RDS
resources to simplify your network configuration.

###### Topics

- [IPv4 addresses](#USER_VPC.IP_addressing.IPv4 "#USER_VPC.IP_addressing.IPv4")
- [IPv6 addresses](#USER_VPC.IP_addressing.IPv6 "#USER_VPC.IP_addressing.IPv6")
- [Dual-stack mode](#USER_VPC.IP_addressing.dual-stack-mode "#USER_VPC.IP_addressing.dual-stack-mode")

### IPv4 addresses

When you create a VPC, you must specify a range of IPv4 addresses for the VPC
in the form of a CIDR block, such as `10.0.0.0/16`. A _DB subnet group_ defines the range of IP addresses
in this CIDR block that a DB cluster can use. These
IP addresses can be private or public.

A private IPv4 address is an IP address that's not reachable over the
internet. You can use private IPv4 addresses for communication between your DB

cluster and other resources, such as Amazon EC2
instances, in the same VPC. Each DB cluster has a private
IP address for communication in the VPC.

A public IP address is an IPv4 address that's reachable from the
internet. You can use public addresses for communication between your DB
cluster and resources on the internet, such
as a SQL client. You control whether your DB
cluster receives a public IP address.

For a tutorial that shows you how to create a VPC with only private IPv4
addresses that you can use for a common Amazon Aurora scenario, see
[Tutorial: Create a VPC for use with a
DB cluster (IPv4 only)](CHAP_Tutorials.WebServerDB.md "CHAP_Tutorials.WebServerDB.md").

### IPv6 addresses

You can optionally associate an IPv6 CIDR block with your VPC and subnets, and
assign IPv6 addresses from that block to the resources in your VPC. Each IPv6
address is globally unique.

The IPv6 CIDR block for your VPC is automatically assigned from Amazon's pool
of IPv6 addresses. You can't choose the range yourself.

When connecting to an IPv6 address, make sure that the following conditions
are met:

- The client is configured so that client to database traffic over IPv6
  is allowed.
- RDS security groups used by the DB instance are configured correctly
  so that client to database traffic over IPv6 is allowed.
- The client operating system stack allows traffic on the IPv6 address,
  and operating system drivers and libraries are configured to choose the
  correct default DB instance endpoint (either IPv4 or IPv6).

For more information about IPv6, see [IP Addressing](../../../vpc/latest/userguide/vpc-ip-addressing.md "../../../vpc/latest/userguide/vpc-ip-addressing.md") in
the _Amazon VPC User Guide_.

### Dual-stack mode

When a DB cluster can communicate over both the IPv4 and
IPv6 addressing protocols, it's running in dual-stack mode. So, resources can
communicate with the DB cluster over IPv4, IPv6, or both. RDS disables
Internet Gateway access for IPv6 endpoints of private dual-stack mode DB
instances. RDS does this to ensure that your IPv6 endpoints are private and can
only be accessed from within your VPC.

###### Topics

- [Dual-stack mode and DB subnet groups](#USER_VPC.IP_addressing.dual-stack-db-subnet-groups "#USER_VPC.IP_addressing.dual-stack-db-subnet-groups")
- [Working
  with dual-stack mode DB instances](#USER_VPC.IP_addressing.dual-stack-working-with "#USER_VPC.IP_addressing.dual-stack-working-with")
- [Modifying
  IPv4-only DB clusters to use dual-stack mode](#USER_VPC.IP_addressing.dual-stack-modifying-ipv4 "#USER_VPC.IP_addressing.dual-stack-modifying-ipv4")
- [Availability of dual-stack network DB clusters](#USER_VPC.IP_addressing.dual-stack-availability "#USER_VPC.IP_addressing.dual-stack-availability")
- [Limitations
  for dual-stack network DB clusters](#USER_VPC.IP_addressing.dual-stack-limitations "#USER_VPC.IP_addressing.dual-stack-limitations")

For a tutorial that shows you how to create a VPC with both IPv4 and IPv6
addresses that you can use for a common Amazon Aurora scenario, see
[Tutorial: Create a VPC for use with a DB
cluster (dual-stack mode)](CHAP_Tutorials.md "CHAP_Tutorials.md").

#### Dual-stack mode and DB subnet groups

To use dual-stack mode, make sure that each subnet in the DB subnet group
that you associate with the DB cluster has an
IPv6 CIDR block associated with it. You can create a new DB subnet group or
modify an existing DB subnet group to meet this requirement. After a DB

cluster is in dual-stack mode, clients
can connect to it normally. Make sure that client security firewalls and RDS
DB instance security groups are accurately configured to allow traffic over
IPv6. To connect, clients use the DB cluster
primary instance's endpoint. Client applications can
specify which protocol is preferred when connecting to a database. In
dual-stack mode, the DB cluster detects
the client's preferred network protocol, either IPv4 or IPv6, and uses
that protocol for the connection.

If a DB subnet group stops supporting dual-stack mode because of subnet
deletion or CIDR disassociation, there's a risk of an incompatible network
state for DB instances that are associated with the DB subnet group. Also,
you can't use the DB subnet group when you create a new dual-stack mode DB
cluster.

To determine whether a DB subnet group supports dual-stack mode by using
the AWS Management Console, view the **Network type** on the details
page of the DB subnet group. To determine whether a DB subnet group supports
dual-stack mode by using the AWS CLI, run the [describe-db-subnet-groups](../../../cli/latest/reference/rds/describe-db-subnet-groups.md "../../../cli/latest/reference/rds/describe-db-subnet-groups.md") command and view
`SupportedNetworkTypes` in the output.

Read replicas are treated as independent DB instances and can have a
network type that's different from the primary DB instance. If you change
the network type of a read replica's primary DB instance, the read replica
isn't affected. When you are restoring a DB instance, you can restore it to
any network type that's supported.

#### Working

with dual-stack mode DB instances

When you create or modify a DB cluster, you can
specify dual-stack mode to allow your resources to communicate with your DB
cluster over IPv4, IPv6, or both.

When you use the AWS Management Console to create or modify a DB instance, you can
specify dual-stack mode in the **Network type** section.
The following image shows the **Network type** section in
the console.

![Network type section in the console with Dual-stack mode selected.](images/dual-stack-mode.png)

When you use the AWS CLI to create or modify a DB cluster, set the `--network-type` option to
`DUAL` to use dual-stack mode. When you use the RDS API to
create or modify a DB cluster, set the `NetworkType`
parameter to `DUAL` to use dual-stack mode. When you are
modifying the network type of a DB instance, downtime is possible. If
dual-stack mode isn't supported by the specified DB engine version or DB
subnet group, the `NetworkTypeNotSupported` error is
returned.

For more information about creating a DB cluster, see
[Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md"). For more information about
modifying a DB cluster, see [Modifying an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

To determine whether a DB cluster is in
dual-stack mode by using the console, view the **Network
type** on the **Connectivity & security**
tab for the DB cluster.

#### Modifying

IPv4-only DB clusters to use dual-stack mode

You can modify an IPv4-only DB cluster to use
dual-stack mode. To do so, change the network type of the DB cluster. The modification might result in downtime.

It is recommended that you change the network type of your
Amazon Aurora DB clusters during a
maintenance window. Currently, setting the network type of new instances to
dual-stack mode isn't supported. You can set network type manually by using
the
`modify-db-cluster` command.

Before modifying a DB cluster to use
dual-stack mode, make sure that its DB subnet group supports dual-stack
mode. If the DB subnet group associated with the DB cluster doesn't support dual-stack mode, specify a different
DB subnet group that supports it when you modify the DB cluster. Modifying the DB subnet group of a DB
cluster can cause downtime.

If you modify the DB subnet group of a DB
cluster before you change the DB
cluster to use dual-stack mode, make
sure that the DB subnet group is valid for the DB cluster before and after the change.

We recommend that you run the [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md")
API with only the `--network-type` parameter with value
`DUAL` to change the network of an Amazon Aurora cluster to
dual-stack mode. Adding other parameters along with the
`--network-type` parameter in the same API call could result
in downtime.

If you can't connect to the DB cluster after the
change, make sure that the client and database security firewalls and route
tables are accurately configured to allow traffic to the database on the
selected network (either IPv4 or IPv6). You might also need to modify
operating system parameter, libraries, or drivers to connect using an IPv6
address.

###### To modify an IPv4-only DB cluster to use

dual-stack mode

1. Modify a DB subnet group to support dual-stack mode, or create a
   DB subnet group that supports dual-stack mode:
   1. Associate an IPv6 CIDR block with your VPC.

   For instructions, see [Add an IPv6 CIDR block to your VPC](../../../vpc/latest/userguide/modify-vpcs.md#vpc-associate-ipv6-cidr "../../../vpc/latest/userguide/modify-vpcs.md#vpc-associate-ipv6-cidr") in the
   _Amazon VPC User Guide_. 2. Attach the IPv6 CIDR block to all of the subnets in your
   the DB subnet group.

   For instructions, see [Add an IPv6 CIDR block to your subnet](../../../vpc/latest/userguide/modify-subnets.md#subnet-associate-ipv6-cidr "../../../vpc/latest/userguide/modify-subnets.md#subnet-associate-ipv6-cidr") in the
   _Amazon VPC User Guide_. 3. Confirm that the DB subnet group supports dual-stack
   mode.

   If you are using the AWS Management Console, select the DB subnet
   group, and make sure that the **Supported network
   types** value is **Dual,
   IPv4**.

   If you are using the AWS CLI, run the [describe-db-subnet-groups](../../../cli/latest/reference/rds/describe-db-subnet-groups.md "../../../cli/latest/reference/rds/describe-db-subnet-groups.md") command, and make
   sure that the `SupportedNetworkType` value for
   the DB instance is `Dual, IPv4`.

2. Modify the security group associated with the DB cluster to allow IPv6 connections to
   the database, or create a new security group that allows IPv6
   connections.

For instructions, see [Security
group rules](../../../vpc/latest/userguide/security-group-rules.md "../../../vpc/latest/userguide/security-group-rules.md") in the
_Amazon VPC User Guide_. 3. Modify the DB cluster to
support dual-stack mode. To do so, set the **Network
type** to **Dual-stack mode**.

If you are using the console, make sure that the following
settings are correct:

    * **Network type** –
     **Dual-stack mode**



    ![Network type section in the console with Dual-stack mode selected.](images/dual-stack-mode.png)
    * **DB subnet group** – The DB
     subnet group that you configured in a previous step
    * **Security group** – The security
     that you configured in a previous step

If you are using the AWS CLI, make sure that the following settings
are correct:

    * `--network-type` –
     `dual`
    * `--db-subnet-group-name` – The DB subnet
     group that you configured in a previous step
    * `--vpc-security-group-ids` – The VPC
     security group that you configured in a previous step

For example:

```
aws rds modify-db-cluster --db-cluster-identifier my-cluster --network-type "DUAL"
```

4. Confirm that the DB cluster
   supports dual-stack mode.

If you are using the console, choose the **Configuration** tab for the DB
cluster. On that tab, make sure that
the **Network type** value is **Dual-stack
mode**.

If you are using the AWS CLI, run the [describe-db-clusters](../../../cli/latest/reference/rds/describe-db-clusters.md "../../../cli/latest/reference/rds/describe-db-clusters.md") command, and make sure that the
`NetworkType` value for the DB cluster is
`dual`.

Run the `dig` command on the writer DB instance endpoint to identify the IPv6
address associated with it.

```
dig `db-instance-endpoint` AAAA
```

Use the writer DB instance
endpoint, not the IPv6 address, to connect to the DB cluster.

#### Availability of dual-stack network DB clusters

Dual-stack network DB clusters are available in all AWS Regions except
for the following:

- Asia Pacific (Hyderabad)
- Asia Pacific (Malaysia)
- Asia Pacific (Melbourne)
- Asia Pacific (Thailand)
- Canada West (Calgary)
- Europe (Spain)
- Europe (Zurich)
- Israel (Tel Aviv)
- Mexico (Central)
- Middle East (UAE)

The following DB engine versions support dual-stack network DB
clusters:

- Aurora MySQL versions:

      + 3.02 and higher 3 versions
      + 2.09.1 and higher 2 versions

  For more information about Aurora MySQL versions, see the [_Release Notes for Aurora MySQL_](../AuroraMySQLReleaseNotes/Welcome.md "../AuroraMySQLReleaseNotes/Welcome.md").

- Aurora PostgreSQL versions:

      + 15.2 and all higher versions
      + 14.3 and higher 14 versions
      + 13.7 and higher 13 versions

  For more information about Aurora PostgreSQL versions, see the [_Release Notes for Aurora PostgreSQL_](../AuroraPostgreSQLReleaseNotes/Welcome.md "../AuroraPostgreSQLReleaseNotes/Welcome.md").

#### Limitations

for dual-stack network DB clusters

The following limitations apply to dual-stack network DB clusters:

- DB clusters can't use the IPv6
  protocol exclusively. They can use IPv4 exclusively, or they can use
  the IPv4 and IPv6 protocol (dual-stack mode).
- Amazon RDS doesn't support native IPv6 subnets.
- DB clusters that use dual-stack mode
  must be private. They can't be publicly accessible.
- You can't use RDS Proxy with dual-stack mode DB clusters.

## Hiding a DB cluster in a VPC from

the internet

One common Amazon Aurora scenario is to have a VPC in which you have an Amazon EC2
instance with a public-facing web application and a DB cluster with a database
that isn't publicly accessible. For example, you can create a VPC that has a public
subnet and a private subnet. EC2 instances that function as web servers can be
deployed in the public subnet. The DB clusters are deployed in
the private subnet. In such a deployment, only the web servers have access to the DB
clusters. For an illustration of this scenario, see [A DB cluster in a VPC
accessed by an Amazon EC2 instance in the same VPC](USER_VPC.md#USER_VPC.Scenario1 "USER_VPC.md#USER_VPC.Scenario1").

When you launch a DB cluster inside a VPC, the DB cluster has a private IP address for traffic inside the VPC. This
private IP address isn't publicly accessible. You can use the **Public
access** option to designate whether the DB cluster also has a public IP address in addition to the private IP
address. If the DB cluster is designated as publicly accessible, its
DNS endpoint resolves to the private IP address from within the VPC. It resolves to
the public IP address from outside of the VPC. Access to the DB cluster is ultimately controlled by the security group it uses. That
public access is not permitted if the security group assigned to the DB cluster doesn't include inbound rules that permit it. In addition, for
a DB cluster to be publicly accessible, the subnets in its DB subnet group
must have an internet gateway. For more information, see [Can't connect to Amazon RDS DB instance](CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting "CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting")

You can modify a DB cluster to turn on or off public accessibility by
modifying the **Public access** option. The following illustration
shows the **Public access** option in the **Additional
connectivity configuration** section. To set the option, open the
**Additional connectivity configuration** section in the
**Connectivity** section.

![Set your database Public access option in the Additional connectivity configuration section to No.](images/VPC-example4.png)

For information about modifying a DB instance to set the
**Public access** option, see [Modifying a DB instance in a DB cluster](Aurora.md#Aurora.Modifying.Instance "Aurora.md#Aurora.Modifying.Instance").

## Creating a DB cluster in a

VPC

The following procedures help you create a DB cluster in a VPC. To use
the default VPC, you can begin with step 2, and use the VPC and DB subnet group have
already been created for you. If you want to create an additional VPC, you can
create a new VPC.

###### Note

If you want your DB cluster in the VPC to be publicly accessible,
you must update the DNS information for the VPC by enabling the VPC attributes
_DNS hostnames_ and _DNS resolution_.
For information about updating the DNS information for a VPC instance, see
[Updating DNS support for your
VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md").

Follow these steps to create a DB instance in a VPC:

- [Step 1: Create a VPC](#USER_VPC.CreatingVPC "#USER_VPC.CreatingVPC")
- [Step 2: Create a DB subnet
  group](#USER_VPC.CreateDBSubnetGroup "#USER_VPC.CreateDBSubnetGroup")
- [Step 3: Create a VPC security
  group](#USER_VPC.CreateVPCSecurityGroup "#USER_VPC.CreateVPCSecurityGroup")
- [Step 4: Create a DB instance in
  the VPC](#USER_VPC.CreateDBInstanceInVPC "#USER_VPC.CreateDBInstanceInVPC")

### Step 1: Create a VPC

Create a VPC with subnets in at least two Availability Zones. You use these
subnets when you create a DB subnet group. If you have a default VPC, a subnet
is automatically created for you in each Availability Zone in the
AWS Region.

For more information, see [Create a VPC with
private and public subnets](CHAP_Tutorials.WebServerDB.md#CHAP_Tutorials.WebServerDB.CreateVPC.VPCAndSubnets "CHAP_Tutorials.WebServerDB.md#CHAP_Tutorials.WebServerDB.CreateVPC.VPCAndSubnets"), or see
[Create a
VPC](../../../vpc/latest/userguide/working-with-vpcs.md#Create-VPC "../../../vpc/latest/userguide/working-with-vpcs.md#Create-VPC") in the _Amazon VPC User Guide_.

### Step 2: Create a DB subnet

group

A DB subnet group is a collection of subnets (typically private) that you
create for a VPC and that you then designate for your DB clusters. A DB subnet group allows you to specify a particular VPC
when you create DB clusters using the AWS CLI or RDS API. If you use
the console, you can just choose the VPC and subnets you want to use. Each DB
subnet group must have at least one subnet in at least two Availability Zones in
the AWS Region. As a best practice, each DB subnet group should have at least
one subnet for every Availability Zone in the AWS Region.

For a DB cluster to be publicly accessible, the subnets
in the DB subnet group must have an internet gateway. For more information about
internet gateways for subnets, see [Connect to the internet using
an internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") in the _Amazon VPC User Guide_.

When you create a DB cluster in a VPC, you can choose a DB subnet
group. Amazon Aurora chooses a subnet and an IP address within that subnet to
associate with your DB cluster. If no DB subnet groups exist, Amazon Aurora creates a default subnet group when you create a DB
cluster. Amazon Aurora creates and associates an Elastic
Network Interface to your DB cluster with that IP
address. The DB cluster uses the Availability Zone that contains
the subnet.

In this step, you create a DB subnet group and add the subnets that you
created for your VPC.

###### To create a DB subnet group

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Subnet
   groups**.
3. Choose **Create DB Subnet Group**.
4. For **Name**, type the name of your DB subnet
   group.
5. For **Description**, type a description for your DB
   subnet group.
6. For **VPC**, choose the default VPC or the VPC that
   you created.
7. In the **Add subnets** section, choose the
   Availability Zones that include the subnets from **Availability
   Zones**, and then choose the subnets from
   **Subnets**.

![Create a DB subnet group.](images/RDSVPC101.png) 8. Choose **Create**.

Your new DB subnet group appears in the DB subnet groups list on the
RDS console. You can choose the DB subnet group to see details,
including all of the subnets associated with the group, in the details
pane at the bottom of the window.

### Step 3: Create a VPC security

group

Before you create your DB cluster, you can
create a VPC security group to associate with your DB cluster. If you don't create a VPC security group, you can use the
default security group when you create a DB cluster. For
instructions on how to create a security group for your DB cluster, see [Create a VPC
security group for a private DB cluster](CHAP_Tutorials.WebServerDB.md#CHAP_Tutorials.WebServerDB.CreateVPC.SecurityGroupDB "CHAP_Tutorials.WebServerDB.md#CHAP_Tutorials.WebServerDB.CreateVPC.SecurityGroupDB"), or
see [Control traffic to
resources using security groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the
_Amazon VPC User Guide_.

### Step 4: Create a DB instance in

the VPC

In this step, you create a DB cluster and use the
VPC name, the DB subnet group, and the VPC security group you created in the
previous steps.

###### Note

If you want your DB cluster in the VPC to be publicly
accessible, you must enable the VPC attributes _DNS
hostnames_ and _DNS resolution_. For more
information, see [DNS attributes for
your VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md") in the _Amazon VPC User Guide_.

For details on how to create a DB cluster, see [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

When prompted in the **Connectivity** section, enter the VPC
name, the DB subnet group, and the VPC security group.

###### Note

Updating VPCs isn't currently supported for Aurora DB clusters.
