# VPC peering network configurations

With AWS DMS, you can create a serverless environment for homogeneous data migrations in a virtual private
cloud (VPC) based on the Amazon VPC service. When you create your instance profile, you
specify the VPC to use. You can use your default VPC for your account and AWS Region,
or you can create a new VPC.

For each data migration, AWS DMS establishes a VPC peering connection with the VPC that
you use for your instance profile. Next, AWS DMS adds the CIDR block in the security group
that is associated with your instance profile. Because AWS DMS attaches a public IP
address to your instance profile, all your data migrations that use the same instance
profile have the same public IP address. When your data migration stops or fails, AWS DMS
deletes the VPC peering connection.

To avoid CIDR block overlapping with the VPC of your instance profile VPC, AWS DMS uses
the `/24` prefix from one of the following CIDR blocks:
`10.0.0.0/8`, `172.16.0.0/12`, and
`192.168.0.0/16`. For example, if you run three data migrations in parallel,
AWS DMS uses the following CIDR blocks to establish a VPC peering connection.

- `192.168.0.0/24` – for the first data migration
- `192.168.1.0/24` – for the second data migration
- `192.168.2.0/24` – for the third data migration
  You can use different network configurations to set up interaction between your source
  and target databases with AWS DMS. Also, for ongoing data replication, you must set up
  interaction between your source and target databases. These configurations depend on the
  location of your source data provider and your network settings. The following sections
  provide descriptions of common network configurations.

###### Topics

- [Configuring a network using a single virtual
  private cloud (VPC)](#vpc-peering-one-vpc "#vpc-peering-one-vpc")
- [Configuring a network using different
  virtual private clouds (VPCs)](#vpc-peering-different-vpc "#vpc-peering-different-vpc")
- [Using an on-premises source data
  provider](#vpc-peering-on-premesis "#vpc-peering-on-premesis")
- [Configuring ongoing data
  replication](#vpc-peering-ongoing-replication "#vpc-peering-ongoing-replication")

## Configuring a network using a single virtual

private cloud (VPC)

In this configuration, AWS DMS connects to your source and target data providers
within the private network.

###### To configure a network when your source and target data providers are in the

same VPC

1. Create the subnet group in the AWS DMS console with the VPC and subnets that
   your source and target data providers use. For more information, see [Creating a subnet group](subnet-group.md "subnet-group.md").
2. Create the instance profile in the AWS DMS console with the VPC and the
   subnet group that you created. Also, choose VPC security groups that your
   source and target data providers use. For more information, see [Creating instance profiles](instance-profiles.md "instance-profiles.md").

This configuration doesn't require you to use the public IP address for data
migrations.

## Configuring a network using different

virtual private clouds (VPCs)

In this configuration, AWS DMS uses a private network to connect to your source or
target data provider. For another data provider, AWS DMS uses a public network.
Depending on which data provider you have in the same VPC as your instance profile,
choose one of the following configurations.

###### To configure a private network for your source data provider and a public

network for your target data provider

1. Create the subnet group in the AWS DMS console with the VPC and subnets that
   your source data provider uses. For more information, see [Creating a subnet group](subnet-group.md "subnet-group.md").
2. Create the instance profile in the AWS DMS console with the VPC and the
   subnet group that you created. Also, choose VPC security groups that your
   source data provider uses. For more information, see [Creating instance profiles](instance-profiles.md "instance-profiles.md").
3. Open your migration project. On the **Data migrations**
   tab, choose your data migration. Take a note of the **public IP
   address** under **Connectivity and security**
   on the **Details** tab.
4. Allow access from the public IP address of your data migration in your
   target database security group. For more information, see [Controlling access with security groups](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md") in the _Amazon Relational Database Service User
   Guide_.

###### To configure a public network for your source data provider and a private

network for your target data provider

1. Create the subnet group in the AWS DMS console with the VPC and subnets that
   your target data provider uses. For more information, see [Creating a subnet group](subnet-group.md "subnet-group.md").
2. Create the instance profile in the AWS DMS console with the VPC and the
   subnet group that you created. Also, choose VPC security groups that your
   target data provider uses. For more information, see [Creating instance profiles](instance-profiles.md "instance-profiles.md").
3. Open your migration project. On the **Data migrations**
   tab, choose your data migration. Take a note of the **public IP
   address** under **Connectivity and security**
   on the **Details** tab.
4. Allow access from the public IP address of your data migration in your
   source database security group. For more information, see [Controlling access with security groups](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md") in the _Amazon Relational Database Service User
   Guide_.

## Using an on-premises source data

provider

In this configuration, AWS DMS connects to your source data provider within the
public network. AWS DMS uses a private network to connect to your target data
provider.

###### Note

For homogeneous data migrations, AWS DMS connects to your source database within
the public network. However, connectivity to a source database within a public
network is not always possible. For more information, see [Migrate an on-premises MySQL database to Amazon Aurora MySQL over a
private network using AWS DMS homogeneous data migration and Network Load
Balancer](https://aws.amazon.com/blogs/database/migrate-an-on-premises-mysql-database-to-amazon-aurora-mysql-over-a-private-network-using-aws-dms-homogeneous-data-migration-and-network-load-balancer/ "https://aws.amazon.com/blogs/database/migrate-an-on-premises-mysql-database-to-amazon-aurora-mysql-over-a-private-network-using-aws-dms-homogeneous-data-migration-and-network-load-balancer/") .

###### To configure a network for your source on-premises data provider

1. Create the subnet group in the AWS DMS console with the VPC and subnets that
   your target data provider uses. For more information, see [Creating a subnet group](subnet-group.md "subnet-group.md").
2. Create the instance profile in the AWS DMS console with the VPC and the
   subnet group that you created. Also, choose VPC security groups that your
   target data provider uses. For more information, see [Creating instance profiles](instance-profiles.md "instance-profiles.md").
3. Open your migration project. On the **Data migrations**
   tab, choose your data migration. Take a note of the **public IP
   address** under **Connectivity and security**
   on the **Details** tab.
4. Allow access to your source database from the public IP address of your
   data migration in AWS DMS.

AWS DMS creates inbound or outbound rules in in VPC security groups. Make sure that
you don't delete these rules because this action can lead to a failure of your data
migration. You can configure your own rules in VPC security groups. We recommended
that you add a description to your rules so that you can manage them.

## Configuring ongoing data

replication

To run data migrations of the **Full load and change data capture
(CDC)** or **Change data capture (CDC)** type, you
must allow connection between your source and target databases.

###### To configure a connection between your publicly accessible source and target

databases

1. Take a note of the public IP addresses of your source and target
   databases.
2. Allow access to your source database from the public IP address of your
   target database.
3. Allow access to your target database from the public IP address of your
   source database.

###### To configure a connection between your source and target databases that are

privately accessible in a single VPC

1. Take a note of the private IP addresses of your source and target
   databases.

###### Important

If your source and target databases are in different VPCs or in
different networks, then you can only use public IP addresses for your
source and target databases. You can only use public hostnames or IP
addresses in data providers. 2. Allow access to your source database from the security group of your
target database. 3. Allow access to your target database from the security group of your
source database.
