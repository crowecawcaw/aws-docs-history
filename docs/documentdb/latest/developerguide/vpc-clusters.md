# DocumentDB clusters in a VPC

Your Amazon DocumentDB cluster is in a virtual private cloud (VPC).
A VPC is a virtual network that is logically isolated from other virtual networks in the AWS Cloud.
Amazon VPC makes it possible for you to launch AWS resources, such as an Amazon DocumentDB cluster or Amazon EC2 instance, into a VPC.
The VPC can either be a default VPC that comes with your account or one that you create. All VPCs are associated with your AWS account.

Your default VPC has three subnets that you can use to isolate resources inside the VPC.
The default VPC also has an internet gateway that can be used to provide access to resources inside the VPC from outside the VPC.

For scenarios involving Amazon DocumentDB clusters in a VPC and outside of a VPC, see [Accessing an Amazon DocumentDB cluster in a VPC](access-cluster-vpc.md "access-cluster-vpc.md").

###### Topics

- [Working with clusters in a VPC](#vpc-working-clusters "#vpc-working-clusters")
- [Working with subnet groups](#vpc-working-subnet-groups "#vpc-working-subnet-groups")
- [Amazon DocumentDB IP addressing](#vpc-docdb-ip-addressing "#vpc-docdb-ip-addressing")
- [Creating a cluster in a VPC](#vpc-creating-cluster "#vpc-creating-cluster")

## Working with clusters in a VPC

Here are some tips on working with a cluster in a VPC:

- Your VPC must have at least two subnets.
  These subnets must be in two different Availability Zones in the AWS Region where you want to deploy your cluster.
  A subnet is a segment of a VPC's IP address range that you can specify and that you can use to group clusters based on your security and operational needs.
- If you want your cluster in the VPC to be publicly accessible, make sure to turn on the VPC attributes `DNS hostnames` and `DNS resolution`.
- Your VPC must have a subnet group that you create.
  You create a subnet group by specifying the subnets you created.
  Amazon DocumentDB chooses a subnet and an IP address within that subnet group to associate with the primary instance in your cluster.
  The primary instance uses the Availability Zone that contains the subnet.
- Your VPC must have a VPC security group that allows access to the cluster.

For more information, see [Accessing an Amazon DocumentDB cluster in a VPC](access-cluster-vpc.md "access-cluster-vpc.md").

- The CIDR blocks in each of your subnets must be large enough to accommodate spare IP addresses for Amazon DocumentDB to use during maintenance activities, including failover and compute scaling.
  For example, a range such as 10.0.0.0/24 and 10.0.1.0/24 is typically large enough.
- A VPC can have an `instance tenancy` attribute of either `default` or `dedicated`.
  All default VPCs have the `instance tenancy` attribute set to default, and a default VPC can support any instance class.

If you choose to have your cluster in a dedicated VPC where the `instance tenancy` attribute is set to `dedicated`, the instance class of your cluster must be one of the approved Amazon EC2 dedicated instance types.
For example, the `r5.large` EC2 dedicated instance corresponds to the `db.r5.large` instance class.
For information about instance tenancy in a VPC, see [Amazon EC2 instances](../../../AWSEC2/latest/UserGuide/Instances.md "../../../AWSEC2/latest/UserGuide/Instances.md") in the _Amazon Elastic Compute Cloud User Guide_.

For more information about the instance types that can be in a dedicated instance, see [Amazon EC2 dedicated instances](https://aws.amazon.com/ec2/pricing/dedicated-instances/ "https://aws.amazon.com/ec2/pricing/dedicated-instances/") on the Amazon EC2 pricing page.

###### Note

When you set the `instance tenancy` attribute to `dedicated` for a cluster, it doesn't guarantee that the cluster will run on a dedicated host.

## Working with subnet groups

Subnets are segments of a VPC's IP address range that you designate to group your resources based on security and operational needs.
A subnet group is a collection of subnets (typically private) that you create in a VPC and that you then designate for your clusters.
By using a subnet group, you can specify a particular VPC when creating clusters using the AWS CLI or Amazon DocumentDB API.
If you use the console, you can choose the VPC and subnet groups you want to use.

Each subnet group should have subnets in at least two Availability Zones in a given AWS Region.
When creating a cluster in a VPC, you choose a subnet group for it.
From the subnet group, Amazon DocumentDB chooses a subnet and an IP address within that subnet to associate with the primary instance in your cluster.
The database uses the Availability Zone that contains the subnet.
DocumentDB always assigns an IP address from a subnet that has free IP address space.

The subnets in a subnet group are either public or private, depending on the configuration that you set for their network access control lists (network ACLs) and routing tables.
For a cluster to be publicly accessible, all of the subnets in its subnet group must be public.
If a subnet that's associated with a publicly accessible cluster changes from public to private, it can affect cluster availability.

To create a subnet group that supports dual-stack mode, make sure that each subnet that you add to the subnet group has an Internet Protocol version 6 (IPv6) CIDR block associated with it.
For more information, see [Amazon DocumentDB IP addressing](#vpc-docdb-ip-addressing "#vpc-docdb-ip-addressing") and [IPv6 support for your VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6.md "../../../vpc/latest/userguide/vpc-migrate-ipv6.md") in the _Amazon Virtual Private Cloud User Guide_.

When Amazon DocumentDB creates a cluster in a VPC, it assigns a network interface to the cluster by using an IP address from your subnet group.
However, we strongly recommend that you use the Domain Name System (DNS) name to connect to your cluster.
We recommend this because the underlying IP address changes during failover.

###### Note

For each cluster that you run in a VPC, make sure to reserve at least one address in each subnet in the subnet group for use by Amazon DocumentDB for recovery actions.

### Shared subnets

You can create a cluster in a shared VPC.

Some considerations to keep in mind while using shared VPCs:

- You can move a cluster from a shared VPC subnet to a non-shared VPC subnet and vice-versa.
- Participants in a shared VPC must create a security group in the VPC to allow them to create a cluster.
- Owners and participants in a shared VPC can access the database by using DocumentDB queries.
  However, only the creator of a resource can make any API calls on the resource.

## Amazon DocumentDB IP addressing

IP addresses enable resources in your VPC to communicate with each other, and with resources over the internet.
Amazon DocumentDB supports both IPv4 and IPv6 addressing protocols.
By default, Amazon DocumentDB and Amazon VPC use the IPv4 addressing protocol.
You can't turn off this behavior.
When you create a VPC, make sure to specify an IPv4 CIDR block (a range of private IPv4 addresses).
You can optionally assign an IPv6 CIDR block to your VPC and subnets, and assign IPv6 addresses from that block to clusters in your subnet.

###### Note

Dual-stack mode (IPv6 addressing) is only supported in Amazon DocumentDB versions 4.0 and 5.0.

Support for the IPv6 protocol expands the number of supported IP addresses.
By using the IPv6 protocol, you ensure that you have sufficient available addresses for the future growth of the internet.
New and existing DocumentDB resources can use IPv4 and IPv6 addresses within your VPC.
Configuring, securing, and translating network traffic between the two protocols used in different parts of an application can cause operational overhead.
You can standardize on the IPv6 protocol for Amazon DocumentDB resources to simplify your network configuration.

###### Topics

- [IPv4 addresses](#vpc-docdb-ipv4-addresses "#vpc-docdb-ipv4-addresses")
- [IPv6 addresses](#vpc-docdb-ipv6-addresses "#vpc-docdb-ipv6-addresses")
- [Dual-stack mode](#vpc-docdb-dual-stack "#vpc-docdb-dual-stack")

### IPv4 addresses

When you create a VPC, you must specify a range of IPv4 addresses for the VPC in the form of a CIDR block, such as `10.0.0.0/16`.
A subnet group defines the range of IP addresses in this CIDR block that a cluster can use.
These IP addresses can be private or public.

A private IPv4 address is an IP address that's not reachable over the internet.
You can use private IPv4 addresses for communication between your cluster and other resources, such as Amazon EC2 instances, in the same VPC.
Each cluster has a private IP address for communication in the VPC.

A public IP address is an IPv4 address that's reachable from the internet.
Public IP addressing is not allowed for your DocumentDB cluster.
Any public IP address should be resolved by the Internet gateway and by EC2 in the public subnet.

To see how to create a VPC with only private IPv4 addresses that you can use for a common Amazon DocumentDB scenario, see [Create an IPv4-only VPC for use with a DocumentDB cluster](docdb-vpc-create-ipv4.md "docdb-vpc-create-ipv4.md").

### IPv6 addresses

You can optionally associate an IPv6 CIDR block with your VPC and subnets, and assign IPv6 addresses from that block to the resources in your VPC.
Each IPv6 address is globally unique.

The IPv6 CIDR block for your VPC is automatically assigned from Amazon's pool of IPv6 addresses.
You can't choose the range yourself.

When connecting to an IPv6 address, make sure that the following conditions are met:

- The client is configured so that client to database traffic over IPv6 is allowed.
- DocumentDB security groups used by the cluster are configured correctly so that client to database traffic over IPv6 is allowed.
- The client operating system stack allows traffic on the IPv6 address, and operating system drivers and libraries are configured to choose the correct default cluster endpoint (either IPv4 or IPv6).

For more information about IPv6, see [IP Addressing](../../../vpc/latest/userguide/vpc-ip-addressing.md "../../../vpc/latest/userguide/vpc-ip-addressing.md") in the _Amazon Virtual Private Cloud User Guide_.

### Dual-stack mode

When a cluster can communicate over both the IPv4 and IPv6 addressing protocols, it's running in dual-stack mode.
So, resources can communicate with the cluster over IPv4, IPv6, or both.
DocumentDB disables Internet Gateway access for IPv6 endpoints of private dual-stack mode clusters.
DocumentDB does this to ensure that your IPv6 endpoints are private and can only be accessed from within your VPC.

###### Topics

- [Dual-stack mode and subnet groups](#dual-stack-subnet "#dual-stack-subnet")
- [Working with dual-stack mode clusters](#dual-stack-clusters "#dual-stack-clusters")
- [Modifying IPv4-only clusters to use dual-stack mode](#modify-ipv4-clusters "#modify-ipv4-clusters")
- [Dual-stack mode Region and version availability](#dual-stack-availability "#dual-stack-availability")
- [Limitations for dual-stack network clusters](#dual-stack-limitations "#dual-stack-limitations")

#### Dual-stack mode and subnet groups

To use dual-stack mode, make sure that each subnet in the subnet group that you associate with the cluster has an IPv6 CIDR block associated with it.
You can create a new subnet group or modify an existing subnet group to meet this requirement.
After a cluster is in dual-stack mode, clients can connect to it normally.
Make sure that client security firewalls and DocumentDB cluster security groups are accurately configured to allow traffic over IPv6.
To connect, clients use the cluster's endpoint.
Client applications can specify which protocol is preferred when connecting to a database.
In dual-stack mode, the cluster detects the client's preferred network protocol, either IPv4 or IPv6, and uses that protocol for the connection.

If a subnet group stops supporting dual-stack mode because of subnet deletion or CIDR disassociation, there's a risk of an incompatible network state for clusters that are associated with the subnet group.
Also, you can't use the subnet group when you create a new dual-stack mode cluster.

To determine whether a subnet group supports dual-stack mode by using the AWS Management Console, view the **Network type** on the details page of the subnet group.
To determine whether a subnet group supports dual-stack mode by using the AWS CLI, run the [`describe-db-subnet-groups`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-subnet-groups.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-subnet-groups.html") command and view `SupportedNetworkTypes` in the output.

Read replicas are treated as independent clusters and can have a network type that's different from the primary cluster.
If you change the network type of a read replica's primary cluster, the read replica isn't affected.
When you are restoring a cluster, you can restore it to any network type that's supported.

#### Working with dual-stack mode clusters

When you create or modify a cluster, you can specify dual-stack mode to allow your resources to communicate with your cluster over IPv4, IPv6, or both.

When you use the AWS Management Console to create or modify a cluster, you can specify dual-stack mode in the **Network type** section.
The following image shows the **Network type** section in the console:

![Network type section in the console with Dual-stack mode selected.](images/nw-type-dual-stack.png)

When you use the AWS CLI to create or modify a cluster, set the `--network-type` option to `DUAL` to use dual-stack mode.
When you use the DocumentDB API to create or modify a cluster, set the `NetworkType` parameter to `DUAL` to use dual-stack mode.
If dual-stack mode isn't supported by the specified DocumentDB engine version or subnet group, the `NetworkTypeNotSupported` error is returned.

For more information about creating a cluster, see [Creating an Amazon DocumentDB cluster](db-cluster-create.md "db-cluster-create.md").
For more information about modifying a cluster, see [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md "db-cluster-modify.md").

To determine whether a cluster is in dual-stack mode by using the console, view the **Network type** on the **Connectivity & security** tab for the cluster.

#### Modifying IPv4-only clusters to use dual-stack mode

You can modify an IPv4-only cluster to use dual-stack mode.
To do so, change the network type of the cluster.

It is recommended that you change the network type of your Amazon DocumentDB cluster during a maintenance window.
You can set network type manually by using the [`modify-db-cluster`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-cluster.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-cluster.html") command.

Before modifying a cluster to use dual-stack mode, make sure that its subnet group supports dual-stack mode.
If the subnet group associated with the cluster doesn't support dual-stack mode, specify a different subnet group that supports it when you modify the cluster.
Modifying the subnet group of a cluster can cause downtime.

If you modify the subnet group of a cluster before you change the cluster to use dual-stack mode, make sure that the subnet group is valid for the cluster before and after the change.

We recommend that you run the `ModifyDBCluster` call with only the `NetworkType` parameter set to `DUAL` to change the network to dual-stack mode.
Adding other parameters along with `NetworkType` in the same API call could result in downtime.
To modify multiple parameters, ensure that the network type modification is successfully completed before sending another `ModifyDBCluster` request with other parameters.

If you can't connect to the cluster after the change, make sure that the client and database security firewalls and route tables are accurately configured to allow traffic to the database on the selected network (either IPv4 or IPv6).
You might also need to modify operating system parameter, libraries, or drivers to connect using an IPv6 address.

**To modify an IPv4-only cluster to use dual-stack mode**

1. Modify a subnet group to support dual-stack mode, or create a subnet group that supports dual-stack mode:
   1. Associate an IPv6 CIDR block with your VPC.

   For instructions, see [Add or remove a CIDR block to your VPC](../../../vpc/latest/userguide/add-ipv4-cidr.md "../../../vpc/latest/userguide/add-ipv4-cidr.md") in the _Amazon VPC User Guide_. 2. Attach the IPv6 CIDR block to all of the subnets in your subnet group.

   For instructions, see [Add or remove an IPv6 CIDR block to your subnet](../../../vpc/latest/userguide/subnet-associate-ipv6-cidr.md "../../../vpc/latest/userguide/subnet-associate-ipv6-cidr.md") in the _Amazon Virtual Private Cloud User Guide_. 3. Confirm that the subnet group supports dual-stack mode.

   If you are using the AWS Management Console, select the subnet group, and make sure that the **Supported network types** value is **Dual**.

   If you are using the AWS CLI, run the [`describe-db-subnet-groups`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-subnet-groups.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-subnet-groups.html") command, and make sure that the `SupportedNetworkType` value for the cluster is `Dual`.

2. Modify the security group associated with the cluster to allow IPv6 connections to the database, or create a new security group that allows IPv6 connections.

For instructions, see [Security group rules](../../../vpc/latest/userguide/security-group-rules.md "../../../vpc/latest/userguide/security-group-rules.md") in the _Amazon Virtual Private Cloud User Guide_. 3. Modify the cluster to support dual-stack mode. To do so, set the **Network type** to **Dual-stack mode**.

If you are using the console, make sure that the following settings are correct:

    * **Network type** — **Dual-stack mode**



    ![Network type section in the console with Dual-stack mode selected.](images/nw-type-dual-stack.png)
    * **Subnet group** — The subnet group that you configured in a previous step
    * **Security group** — The security that you configured in a previous step

If you are using the AWS CLI, make sure that the following settings are correct:

    * `--network-type` — `dual`
    * `--db-subnet-group-name` — The subnet group that you configured in a previous step
    * `--vpc-security-group-ids` — The VPC security group that you configured in a previous step

For example:

```
aws docdb modify-db-cluster --db-cluster-identifier `<cluster-name>` --network-type "DUAL"
```

4. Confirm that the cluster supports dual-stack mode.

If you are using the console, choose the **Connectivity & security** tab for the cluster and make sure that the **Network type** value is **Dual-stack mode**.

If you are using the AWS CLI, run the `describe-db-cluster` command, and make sure that the `NetworkType` value for the cluster is `dual`.

Run the `dig` command on the cluster endpoint to identify the IPv6 address associated with it:

```
dig `<db-cluster-endpoint>` AAAA
```

Use the cluster endpoint, not the IPv6 address, to connect to the cluster.

#### Dual-stack mode Region and version availability

Feature availability and support varies across AWS Regions.

**Region support**

The following list identifies the AWS Regions that support dual-stack mode:

- US East (Ohio)
- US East (N. Virginia)
- US West (Oregon)
- Africa (Cape Town)
- South America (São Paulo)
- Asia Pacific (Hong Kong)
- Asia Pacific (Hyderabad)
- Asia Pacific (Malaysia)
- Asia Pacific (Mumbai)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Thailand)
- Asia Pacific (Tokyo)
- Canada (Central)
- China (Beijing)
- China (Ningxia)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Milan)
- Europe (Paris)
- Europe (Spain)
- Europe (Stockholm)
- Israel (Tel Aviv)
- Mexico (Central)
- Middle East (UAE)
- AWS GovCloud (US-West)
- AWS GovCloud (US-East)

**Version support**

Dual-stack mode is supported on Amazon DocumentDB version 4.0 and 5.0.
If you are unable to access dual-stack mode on either of these versions, please make sure that you are running the latest engine patch version on your cluster.

#### Limitations for dual-stack network clusters

The following limitations apply to dual-stack network clusters:

- Clusters can't use the IPv6 protocol exclusively. They can use IPv4 exclusively, or they can use the IPv4 and IPv6 protocol (dual-stack mode).
- Amazon DocumentDB doesn't support native IPv6 subnets.
- Clusters that use dual-stack mode must be private. They can't be publicly accessible.

## Creating a cluster in a VPC

The following procedures help you create a cluster in a VPC.
To use the default VPC, you can begin with step 2, and use the VPC and subnet group that have already been created for you.
You can also create additional VPCs, if needed.

###### Note

If you want your cluster in the VPC to be publicly accessible, you must update the DNS information for the VPC by enabling the VPC attributes `DNS hostnames` and `DNS resolution`.
For information about updating the DNS for a VPC instance, see [View and update DNS attributes for your VPC](../../../vpc/latest/userguide/vpc-dns-updating.md "../../../vpc/latest/userguide/vpc-dns-updating.md") in the _Amazon Virtual Private Cloud User Guide_.

Follow these steps to create a cluster in a VPC:

- [Step 1: Create a VPC](#step1-create-vpc "#step1-create-vpc")
- [Step 2: Create a subnet group](#step2-create-subnet-group "#step2-create-subnet-group")
- [Step 3: Create a VPC security group](#step3-create-security-group "#step3-create-security-group")
- [Step 4: Create a cluster in the VPC](#step4-create-vpc-cluster "#step4-create-vpc-cluster")

### Step 1: Create a VPC

Create a VPC with subnets in at least two Availability Zones.
You use these subnets when you create a subnet group.
If you have a default VPC, a subnet is automatically created for you in each Availability Zone in the AWS Region.

For more information, see [Create an IPv4-only VPC for use with a DocumentDB cluster](docdb-vpc-create-ipv4.md "docdb-vpc-create-ipv4.md"), or see [Create a VPC](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md") in the _Amazon Virtual Private Cloud User Guide_.

### Step 2: Create a subnet group

A subnet group is a collection of subnets (typically private) that you create for a VPC and that you then designate for your clusters.
A subnet group allows you to specify a particular VPC when you create clusters using the AWS CLI or DocumentDB API.
If you use the AWS Management Console, you can just choose the VPC and subnets you want to use.
Each subnet group must have at least one subnet in at least two Availability Zones in the AWS Region.
As a best practice, each subnet group should have at least one subnet for every Availability Zone in the AWS Region.

For a cluster to be publicly accessible, the subnets in the subnet group must have an internet gateway.
For more information about internet gateways for subnets, see [Enable internet access for a VPC using an internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") in the _Amazon Virtual Private Cloud User Guide_.

###### Note

The subnet group for a local zone can have only one subnet.

When you create a cluster in a VPC, you can choose a subnet group.
Amazon DocumentDB chooses a subnet and an IP address (within that subnet) to associate with your cluster.
If no subnet groups exist, Amazon DocumentDB creates a default subnet group when you create the cluster.
DocumentDB creates and associates an Elastic Network Interface to your cluster with that IP address.
The cluster uses the Availability Zone that contains the subnet.

In this step, you create a subnet group and add the subnets that you created for your VPC.

**To create a subnet group**

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Subnet groups**.
3. Choose **Create**.
4. For **Name**, type the name of your subnet group.
5. For **Description**, type a description for your subnet group.
6. In the **Add subnets** section, for **VPC**, choose the default VPC or the VPC that you created.
   Then choose the Availability Zones that include the subnets from **Availability Zones**, and then choose the subnets from **Subnets**.
7. Choose Create.

Your new subnet group appears in the **Subnet groups** list on the DocumentDB console.
You can choose the subnet group to see details, including all of the subnets associated with the group, in the details pane at the bottom of the window.

### Step 3: Create a VPC security group

Before you create your cluster, create a VPC security group to associate with it.
If you don't create a VPC security group, you can use the default security group when you create the cluster.
For instructions on how to create a security group for your cluster, see [Create an IPv4-only VPC for use with a DocumentDB cluster](docdb-vpc-create-ipv4.md "docdb-vpc-create-ipv4.md"), or see [Control traffic to your AWS resources using security groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md") in the _Amazon Virtual Private Cloud User Guide_.

### Step 4: Create a cluster in the VPC

In this step, you create a cluster using the VPC name, the subnet group, and the VPC security group you created in the previous steps.

###### Note

If you want your cluster in the VPC to be publicly accessible, you must enable the VPC attributes `DNS hostnames` and `DNS resolution`.
For more information, see [View and update DNS attributes for your VPC](../../../vpc/latest/userguide/vpc-dns-updating.md "../../../vpc/latest/userguide/vpc-dns-updating.md") in the _Amazon Virtual Private Cloud User Guide_.

For details on how to create a cluster, see [Creating an Amazon DocumentDB cluster](db-cluster-create.md "db-cluster-create.md").

When prompted in the **Connectivity** section, enter the VPC name, the subnet group, and the VPC security group.

###### Note

Updating VPCs isn't currently supported for DocumentDBDocumentDB clusters.
