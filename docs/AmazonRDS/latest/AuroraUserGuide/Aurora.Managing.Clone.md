# Cross-VPC cloning with Amazon Aurora

Suppose that you want to impose different network access controls on the original cluster and
the clone. For example, you might use cloning to make a copy of a production Aurora cluster in a
different VPC for development and testing. Or you might create a clone as part of a migration
from public subnets to private subnets, to enhance your database security.

The following sections demonstrate how to set up the network configuration for the clone so that
the original cluster and the clone can both access the same Aurora storage nodes, even from
different subnets or different VPCs. Verifying the network resources in advance can avoid errors
during cloning that might be difficult to diagnose.

If you aren't familiar with how Aurora interacts with VPCs, subnets, and DB subnet groups, see
[Amazon VPC and Amazon Aurora](USER_VPC.md "USER_VPC.md") first. You can work through the tutorials in that section to
create these kinds of resources in the AWS console, and understand how they fit together.

Because the steps involve switching between the RDS and EC2 services, the examples use AWS CLI
commands to help you understand how to automate such operations and save the output.

###### Topics

- [Before you begin](#before-you-begin "#before-you-begin")
- [Gathering information about the network environment](#gathering-information-about-the-network-environment "#gathering-information-about-the-network-environment")
- [Creating network resources for the clone](#creating-network-resources-for-the-clone "#creating-network-resources-for-the-clone")
- [Creating an Aurora clone with new network settings](#creating-an-aurora-clone-with-new-network-settings "#creating-an-aurora-clone-with-new-network-settings")
- [Moving a cluster from public subnets to private ones](#moving-a-cluster-from-public-subnets-to-private-ones "#moving-a-cluster-from-public-subnets-to-private-ones")
- [End-to-end example of creating a cross-VPC clone](#end-to-end-example-of-creating-a-cross-vpc-clone "#end-to-end-example-of-creating-a-cross-vpc-clone")

## Before you begin

Before you start setting up a cross-VPC clone, make sure to have the following resources:

- An Aurora DB cluster to use as the source for cloning. If this is your first time creating
  an Aurora DB cluster, consult the tutorials in
  [Getting started with Amazon Aurora](CHAP_GettingStartedAurora.md "CHAP_GettingStartedAurora.md")
  to set up a cluster using either the MySQL or PostgreSQL database engine.
- A second VPC, if you intend to create a cross-VPC clone. If you don't have a VPC to use
  for the clone, see
  [Tutorial: Create a VPC for use with a
  DB cluster (IPv4 only)](CHAP_Tutorials.WebServerDB.md "CHAP_Tutorials.WebServerDB.md") or
  [Tutorial: Create a VPC for use with a DB
  cluster (dual-stack mode)](CHAP_Tutorials.md "CHAP_Tutorials.md").

## Gathering information about the network environment

With cross-VPC cloning, the network environment can differ substantially between the original
cluster and its clone. Before you create the clone, collect and record information about the
VPC, subnets, DB subnet group, and AZs used in the original cluster. That way, you can
minimize the chances of problems. If a network problem does occur, you won't have to interrupt
any troubleshooting activities to search for diagnostic information. The following sections
show CLI examples to gather these types of information. You can save the details in whichever
format is convenient to consult while creating the clone and doing any troubleshooting.

- [Step 1: Check the Availability Zones of the original cluster](#cross-vpc-cloning-check-original-azs "#cross-vpc-cloning-check-original-azs")
- [Step 2: Check the DB subnet group of the original cluster](#cross-vpc-cloning-check-original-subnet-group "#cross-vpc-cloning-check-original-subnet-group")
- [Step 3: Check the subnets of the original cluster](#cross-vpc-cloning-check-original-subnets "#cross-vpc-cloning-check-original-subnets")
- [Step 4: Check the Availability Zones of the DB instances in the original cluster](#cross-vpc-cloning-check-original-instance-azs "#cross-vpc-cloning-check-original-instance-azs")
- [Step 5: Check the VPCs you can use for the clone](#cross-vpc-cloning-check-vpcs "#cross-vpc-cloning-check-vpcs")

### Step 1: Check the Availability Zones of the original cluster

Before you create the clone, verify which AZs the original cluster uses for its storage. As
explained in
[Amazon Aurora
storage](Aurora.Overview.md "Aurora.Overview.md"),
the storage for each Aurora cluster is associated with exactly three AZs. Because the
[Amazon Aurora DB clusters](Aurora.md "Aurora.md") takes advantage of the separation
of compute and storage, this rule is true regardless of how many instances are in the cluster.

For example, run a CLI command such as the following, substituting your own cluster name for
`my_cluster`. The following example produces a list sorted alphabetically
by the AZ name.

```
aws rds describe-db-clusters \
  --db-cluster-identifier `my_cluster` \
  --query 'sort_by(*[].AvailabilityZones[].{Zone:@},&Zone)' \
  --output text

```

The following example shows sample output from the preceding
`describe-db-clusters` command. It demonstrates that the storage for the
Aurora cluster always uses three AZs.

```
`us-east-1c
us-east-1d
us-east-1e`

```

To create a clone in a network environment that doesn't have all the resources in place to
connect to these AZs, you must create subnets associated with at least two of those AZs, and
then create a DB subnet group containing those two or three subnets. The following examples
show how.

### Step 2: Check the DB subnet group of the original cluster

If you want to use the same number of subnets for the clone as in the original cluster, you
can get the number of subnets from the DB subnet group of the original cluster. An Aurora DB
subnet group contains at least two subnets, each associated with a different AZ. Make a note
of which AZs the subnets are associated with.

The following example shows how to find the DB subnet group of the original cluster, and
then work backwards to the corresponding AZs. Substitute the name of your cluster for
`my_cluster` in the first command. Substitute the name of the DB subnet
group for `my_subnet` in the second command.

```
aws rds describe-db-clusters --db-cluster-identifier `my_cluster` \
  --query '*[].DBSubnetGroup' --output text

aws rds describe-db-subnet-groups --db-subnet-group-name `my_subnet_group` \
  --query '*[].Subnets[].[SubnetAvailabilityZone.Name]' --output text

```

Sample output might look similar to the following, for a cluster with a DB subnet group
containing containing two subnets. In this case, `two-subnets` is a name
that was specified when creating the DB subnet group.

```
`two-subnets

us-east-1d
us-east-1c`

```

For a cluster where the DB subnet group contains three subnets, the output might look
similar to the following.

```
`three-subnets

us-east-1f
us-east-1d
us-east-1c`

```

### Step 3: Check the subnets of the original cluster

If you need more details about the subnets in the original cluster, run AWS CLI commands
similar to the following. You can examine the subnet attributes such as IP address ranges,
owner, and so on. That way, you can determine whether to use different subnets in the same
VPC, or create subnets with similar characteristics in a different VPC.

Find the subnet IDs of all the subnets that are available in your VPC.

```
aws ec2 describe-subnets --filters Name=vpc-id,Values=`my_vpc` \
  --query '*[].[SubnetId]' --output text

```

Find the exact subnets used in your DB subnet group.

```
aws rds describe-db-subnet-groups --db-subnet-group-name `my_subnet_group` \
  --query '*[].Subnets[].[SubnetIdentifier]' --output text

```

Then specify the subnets that you want to investigate in a list, as in the following
command. Substitute the names of your subnets for `my_subnet_1` and so on.

```
aws ec2 describe-subnets \
  --subnet-ids '["`my_subnet_1`","`my_subnet2`","`my_subnet3`"]'

```

The following example shows partial output from such a `describe-subnets`
command. The output shows some of the important attributes you can see for each subnet, such
as its associated AZ and the VPC that it's part of.

```
{
    'Subnets': [
        {
            'AvailabilityZone': 'us-east-1d',
            'AvailableIpAddressCount': 54,
            'CidrBlock': '10.0.0.64/26',
            'State': 'available',
            'SubnetId': 'subnet-000a0bca00e0b0000',
            'VpcId': 'vpc-3f3c3fc3333b3ffb3',
            ...
        },
        {
            'AvailabilityZone': 'us-east-1c',
            'AvailableIpAddressCount': 55,
            'CidrBlock': '10.0.0.0/26',
            'State': 'available',
            'SubnetId': 'subnet-4b4dbfe4d4a4fd4c4',
            'VpcId': 'vpc-3f3c3fc3333b3ffb3',
            ...

```

### Step 4: Check the Availability Zones of the DB instances in the original cluster

You can use this procedure to understand the AZs used for the DB instances in the original
cluster. That way, you can set up the exact same AZs for the DB instances in the clone. You
can also use more or fewer DB instances in the clone depending on whether the clone is used
for production, development and testing, and so on.

For each instance in the original cluster, run a command such as the following. Make sure
that the instance has finished creating and is in the `Available` state
first. Substitute the instance identifier for `my_instance`.

```
aws rds describe-db-instances --db-instance-identifier `my_instance` \
  --query '*[].AvailabilityZone' --output text

```

The following example shows the output of running the preceding
`describe-db-instances` command. The Aurora cluster has four database
instances. Therefore, we run the command four times, substituting a different DB instance
identifier each time. The output shows how those DB instances are spread across a maximum of
three AZs.

```
`us-east-1a
us-east-1c
us-east-1d
us-east-1a`

```

After the clone is created and you are adding DB instances to it, you can specify these same
AZ names in the `create-db-instance` commands. You might do so to set up DB
instances in the new cluster configured for exactly the same AZs as in the original cluster.

### Step 5: Check the VPCs you can use for the clone

If you intend to create the clone in a different VPC than the original, you can get a list
of the VPC IDs available for your account. You might also do this step if you need to create
any additional subnets in the same VPC as the original cluster. When you run the command to
create a subnet, you specify the VPC ID as a parameter.

To list all the VPCs for your account, run the following CLI command:

```
aws ec2 describe-vpcs --query '*[].[VpcId]' --output text
```

The following example shows sample output from the preceding
`describe-vpcs` command. The output demonstrates that there are four VPCs
in the current AWS account that can be used as the source or the destination for cross-VPC
cloning.

```
`vpc-fd111111
vpc-2222e2cd2a222f22e
vpc-33333333a33333d33
vpc-4ae4d4de4a4444dad`

```

You can use the same VPC as the destination for the clone, or a different VPC. If the
original cluster and the clone are in the same VPC, you can reuse the same DB subnet group
for the clone. You can also create a different DB subnet group. For example, the new DB
subnet group might use private subnets, while the original cluster's DB subnet group might
use public subnets. If you create the clone in a different VPC, make sure that there are
enough subnets in the new VPC and that the subnets are associated with the right AZs from
the original cluster.

## Creating network resources for the clone

If while collecting the network information you discovered that additional network resources
are needed for the clone, you can create those resources before trying to set up the clone.
For example, you might need to create more subnets, subnets associated with specific AZs, or a
new DB subnet group.

- [Step 1: Create the subnets for the clone](#cross-vpc-cloning-create-clone-subnets "#cross-vpc-cloning-create-clone-subnets")
- [Step 2: Create the DB subnet group for the clone](#cross-vpc-cloning-create-subnet-group "#cross-vpc-cloning-create-subnet-group")

### Step 1: Create the subnets for the clone

If you need to create new subnets for the clone, run a command similar to the following. You
might need to do this when creating the clone in a different VPC, or when making some other
network change such as using private subnets instead of public subnets.

AWS automatically generates the ID of the subnet. Substitute the name of the clone's VPC
for `my_vpc`. Choose the address range for the
`--cidr-block` option to allow at least 16 IP addresses in the range. You
can include any other properties that you want to specify. Run the command
`aws ec2 create-subnet help` to see all the choices.

```
aws ec2 create-subnet --vpc-id `my_vpc` \
  --availability-zone `AZ_name` --cidr-block `IP_range`

```

The following example shows some important attributes of a newly created subnet.

```
`{
 'Subnet': {
 'AvailabilityZone': 'us-east-1b',
 'AvailableIpAddressCount': 59,
 'CidrBlock': '10.0.0.64/26',
 'State': 'available',
 'SubnetId': 'subnet-44b4a44f4e44db444',
 'VpcId': 'vpc-555fc5df555e555dc',
 ...
 }`
}

```

### Step 2: Create the DB subnet group for the clone

If you are creating the clone in a different VPC, or a different set of subnets within the
same VPC, then you create a new DB subnet group and specify it when creating the clone.

Make sure that you know all the following details. You can find all of these from the output
of the preceding examples.

1. VPC of the original cluster. For instructions, see
   [Step 3: Check the subnets of the original cluster](#cross-vpc-cloning-check-original-subnets "#cross-vpc-cloning-check-original-subnets").
2. VPC of the clone, if you are creating it in a different VPC. For instructions, see
   [Step 5: Check the VPCs you can use for the clone](#cross-vpc-cloning-check-vpcs "#cross-vpc-cloning-check-vpcs").
3. Three AZs associated with the Aurora storage for the original cluster. For instructions, see
   [Step 1: Check the Availability Zones of the original cluster](#cross-vpc-cloning-check-original-azs "#cross-vpc-cloning-check-original-azs").
4. Two or three AZs associated with the DB subnet group for the original cluster. For instructions, see
   [Step 2: Check the DB subnet group of the original cluster](#cross-vpc-cloning-check-original-subnet-group "#cross-vpc-cloning-check-original-subnet-group").
5. The subnet IDs and associated AZs of all the subnets in the VPC you intend to use for
   the clone. Use the same `describe-subnets` command as in
   [Step 3: Check the subnets of the original cluster](#cross-vpc-cloning-check-original-subnets "#cross-vpc-cloning-check-original-subnets"),
   substituting the VPC ID of the destination VPC.

Check how many AZs are both associated with the storage of the original cluster, and
associated with subnets in the destination VPC. To successfully create the clone, there must
be two or three AZs in common. If you have fewer than two AZs in common, go back to
[Step 1: Create the subnets for the clone](#cross-vpc-cloning-create-clone-subnets "#cross-vpc-cloning-create-clone-subnets").
Create one, two, or three new subnets that are associated with the AZs associated with the storage of the original cluster.

Choose subnets in the destination VPC that are associated with the same AZs as the Aurora
storage in the originally cluster. Ideally, choose three AZs. Doing so gives you the most
flexibility to spread the DB instances of the clone across multiple AZs for high
availability of compute resources.

Run a command similar to the following to create the new DB subnet group. Substitute the IDs
of your subnets in the list. If you specify the subnet IDs using environment variables, be careful to
quote the `--subnet-ids` parameter list in a way that preserves the double quotation marks around the IDs.

```
aws rds create-db-subnet-group --db-subnet-group-name `my_subnet_group` \
  --subnet-ids '["`my_subnet_1`","`my_subnet_2`","`my_subnet3`"]' \
  --db-subnet-group-description 'DB subnet group with 3 subnets for clone'

```

The following example shows partial output of the `create-db-subnet-group`
command.

```
`{
 'DBSubnetGroup': {
 'DBSubnetGroupName': '`my_subnet_group`',
 'DBSubnetGroupDescription': 'DB subnet group with 3 subnets for clone',
 'VpcId': 'vpc-555fc5df555e555dc',
 'SubnetGroupStatus': 'Complete',
 'Subnets': [
 {
 'SubnetIdentifier': '`my_subnet_1`',
 'SubnetAvailabilityZone': {
 'Name': 'us-east-1c'
 },
 'SubnetStatus': 'Active'
 },
 {
 'SubnetIdentifier': '`my_subnet_2`',
 'SubnetAvailabilityZone': {
 'Name': 'us-east-1d'
 },
 'SubnetStatus': 'Active'
 }
 ...
 ],
 'SupportedNetworkTypes': [
 'IPV4'
 ]
 }
}`

```

At this point, you haven't actually created the clone yet. You have created all the relevant
VPC and subnet resources so that you can specify the appropriate parameters to the
`restore-db-cluster-to-point-in-time` and
`create-db-instance` commands when creating the clone.

## Creating an Aurora clone with new network settings

Once you have made sure that the right configuration of VPCs, subnets, AZs, and subnet groups
is in place for the new cluster to use, you can perform the actual cloning operation. The
following CLI examples highlight the options such as
`--db-subnet-group-name`, `--availability-zone`, and
`--vpc-security-group-ids` that you specify on the commands to set up the
clone and its DB instances.

- [Step 1: Specify the DB subnet group for the clone](#cross-vpc-cloning-specify-clone-subnet-group "#cross-vpc-cloning-specify-clone-subnet-group")
- [Step 2: Specify network settings for instances in the clone](#cross-vpc-cloning-configure-clone-instance-network "#cross-vpc-cloning-configure-clone-instance-network")
- [Step 3: Establishing connectivity from a client system to a clone](#cross-vpc-cloning-connect-to-clone "#cross-vpc-cloning-connect-to-clone")

### Step 1: Specify the DB subnet group for the clone

When you create the clone, you can configure all the right VPC, subnet, and AZ settings by
specifying a DB subnet group. Use the commands in the preceding examples to verify all the
relationships and mappings that go into the DB subnet group.

For example, the following commands demonstrate cloning an original cluster to a clone. In
the first example, the source cluster is associated with two subnets and the clone is
associated with three subnets. The second example shows the opposite case, cloning from a
cluster with three subnets to a cluster with two subnets.

```
aws rds restore-db-cluster-to-point-in-time \
  --source-db-cluster-identifier cluster-with-3-subnets \
  --db-cluster-identifier cluster-cloned-to-2-subnets \
  --restore-type copy-on-write --use-latest-restorable-time \
  --db-subnet-group-name two-subnets

```

If you intend to use Aurora Serverless v2 instances in the clone, include a
`--serverless-v2-scaling-configuration` option when you create the clone,
as shown. Doing so lets you use the `db.serverless` class when creating DB
instances in the clone. You can also modify the clone later to add this scaling
configuration attribute. The capacity numbers in this example allow each Serverless v2
instance in the cluster to scale between 2 and 32 Aurora Capacity Units (ACUs). For
information about the Aurora Serverless v2 feature and how to choose the capacity range, see
[Using Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").

```
aws rds restore-db-cluster-to-point-in-time \
  --source-db-cluster-identifier cluster-with-2-subnets \
  --db-cluster-identifier cluster-cloned-to-3-subnets \
  --restore-type copy-on-write --use-latest-restorable-time \
  --db-subnet-group-name three-subnets \
  --serverless-v2-scaling-configuration 'MinCapacity=2,MaxCapacity=32'

```

Regardless of the number of subnets used by the DB instances, the Aurora storage for the
source cluster and the clone is associated with three AZs. The following example lists the
AZs associated with both the original cluster and the clone, for both of the
`restore-db-cluster-to-point-in-time` commands in the preceding examples.

```
aws rds describe-db-clusters --db-cluster-identifier cluster-with-3-subnets \
  --query 'sort_by(*[].AvailabilityZones[].{Zone:@},&Zone)' --output text

`us-east-1c
us-east-1d
us-east-1f`

aws rds describe-db-clusters --db-cluster-identifier cluster-cloned-to-2-subnets \
  --query 'sort_by(*[].AvailabilityZones[].{Zone:@},&Zone)' --output text

`us-east-1c
us-east-1d
us-east-1f`

aws rds describe-db-clusters --db-cluster-identifier cluster-with-2-subnets \
  --query 'sort_by(*[].AvailabilityZones[].{Zone:@},&Zone)' --output text

`us-east-1a
us-east-1c
us-east-1d`

aws rds describe-db-clusters --db-cluster-identifier cluster-cloned-to-3-subnets \
  --query 'sort_by(*[].AvailabilityZones[].{Zone:@},&Zone)' --output text

`us-east-1a
us-east-1c
us-east-1d`

```

Because at least two of the AZs overlap between each pair of original and clone clusters,
both clusters can access the same underlying Aurora storage.

### Step 2: Specify network settings for instances in the clone

When you create DB instances in the clone, by default they inherit the DB subnet group from
the cluster itself. That way, Aurora automatically assigns each instance to a particular
subnet, and creates it in the AZ that's associated with the subnet. This choice is
convenient, especially for development and test systems, because you don't have to keep
track of the subnet IDs or the AZs while adding new instances to the clone.

As an alternative, you can specify the AZ when you create an Aurora DB instance for the
clone. The AZ that you specify must be from the set of AZs that are associated with the
clone. If the DB subnet group you use for the clone only contains two subnets, then you can
only pick from the AZs associated with those two subnets. This choice offers flexibility and
resilience for highly available systems, because you can make sure that the writer instance
and the standby reader instance are in different AZs. Or if you add additional readers to
the cluster, you can make sure that they are spread across three AZs. That way, even in the
rare case of an AZ failure, you still have a writer instance and another reader instance in
two other AZs.

The following example adds a provisioned DB instance to a cloned Aurora PostgreSQL cluster
that uses a custom DB subnet group.

```
aws rds create-db-instance --db-cluster-identifier `my_aurora_postgresql_clone` \
  --db-instance-identifier `my_postgres_instance` \
  --db-subnet-group-name `my_new_subnet` \
  --engine aurora-postgresql \
  --db-instance-class db.t4g.medium

```

The following example shows partial output from such a command.

```
`{
 'DBInstanceIdentifier': '`my_postgres_instance`',
 'DBClusterIdentifier': '`my_aurora_postgresql_clone`',
 'DBInstanceClass': 'db.t4g.medium',
 'DBInstanceStatus': 'creating'
 ...`
}

```

The following example adds an Aurora Serverless v2 DB instance to an Aurora MySQL clone that
uses a custom DB subnet group. To be able to use Serverless v2 instances, make sure to
specify the `--serverless-v2-scaling-configuration` option for the
`restore-db-cluster-to-point-in-time` command, as shown in preceding
examples.

```
aws rds create-db-instance --db-cluster-identifier `my_aurora_mysql_clone` \
  --db-instance-identifier `my_mysql_instance` \
  --db-subnet-group-name `my_other_new_subnet` \
  --engine aurora-mysql \
  --db-instance-class db.serverless

```

The following example shows partial output from such a command.

```
`{
 'DBInstanceIdentifier': '`my_mysql_instance`',
 'DBClusterIdentifier': '`my_aurora_mysql_clone`',
 'DBInstanceClass': 'db.serverless',
 'DBInstanceStatus': 'creating'
 ...`
}

```

### Step 3: Establishing connectivity from a client system to a clone

If you are already connecting to an Aurora cluster from a client system, you might want to
allow the same type of connectivity to a new clone. For example, you might connect to the
original cluster from an Amazon Cloud9 instance or EC2 instance. To allow connections from
the same client systems, or new ones that you create in the destination VPC, set up
equivalent DB subnet groups and VPC security groups as in the VPC. Then specify the subnet
group and security groups when you create the clone.

The following examples set up an Aurora Serverless v2 clone. That configuration is based on
the combination of `--engine-mode provisioned` and
`--serverless-v2-scaling-configuration` when creating the DB cluster, and
then `--db-instance-class db.serverless` when creating each DB instance in
the cluster. The `provisioned` engine mode is the default, so you can omit
that option if you prefer.

```
aws rds restore-db-cluster-to-point-in-time \
  --source-db-cluster-identifier serverless-sql-postgres\
  --db-cluster-identifier serverless-sql-postgres-clone \
  --db-subnet-group-name 'default-vpc-1234' \
  --vpc-security-group-ids 'sg-4567' \
  --serverless-v2-scaling-configuration 'MinCapacity=0.5,MaxCapacity=16' \
  --restore-type copy-on-write \
  --use-latest-restorable-time

```

Then, when creating the DB instances in the clone, specify the same
`--db-subnet-group-name` option. Optionally, you can include the
`--availability-zone` option and specify one of the AZs associated with the
subnets in that subnet group. That AZ must also be one of the AZs associated with the
original cluster.

```
aws rds create-db-instance \
  --db-cluster-identifier serverless-sql-postgres-clone \
  --db-instance-identifier serverless-sql-postgres-clone-instance \
  --db-instance-class db.serverless \
  --db-subnet-group-name 'default-vpc-987zyx654' \
  --availability-zone 'us-east-1c' \
  --engine aurora-postgresql

```

## Moving a cluster from public subnets to private ones

You can use cloning to migrate a cluster between public and private subnets. You might do this
when adding additional layers of security to your application before deploying it to
production. For this example, you should already have the private subnets and NAT gateway set
up before starting the cloning process with Aurora.

For the steps involving Aurora, you can follow the same general steps as in the preceding
examples to
[Gathering information about the network environment](#gathering-information-about-the-network-environment "#gathering-information-about-the-network-environment") and
[Creating an Aurora clone with new network settings](#creating-an-aurora-clone-with-new-network-settings "#creating-an-aurora-clone-with-new-network-settings").
The main difference is that even if you have public subnets that map to all
the AZs from the original cluster, now you must verify that you have enough private subnets
for an Aurora cluster, and that those subnets are associated with all the same AZs that are
used for Aurora storage in the original cluster. Similar to other cloning use cases, you can
make the DB subnet group for the clone with either three or two private subnets that are
associated with the required AZs. However, if you use two private subnets in the DB subnet
group, you must have a third private subnet that's associated with the third AZ used for
Aurora storage in the original cluster.

You can consult this checklist to verify that all the requirements are in place to perform
this type of cloning operation.

- Record the three AZs that are associated with the original cluster. For instructions, see
  [Step 1: Check the Availability Zones of the original cluster](#cross-vpc-cloning-check-original-azs "#cross-vpc-cloning-check-original-azs").
- Record the three or two AZs that are associated with the public subnets in the DB subnet
  group for the original cluster. For instructions, see
  [Step 3: Check the subnets of the original cluster](#cross-vpc-cloning-check-original-subnets "#cross-vpc-cloning-check-original-subnets").
- Create private subnets that map to all three of the AZs that are associated with the
  original cluster. Also do any other networking setup, such as creating a NAT gateway, to
  be able to communicate with the private subnets. For instructions, see
  [Create a subnet](../../../vpc/latest/userguide/create-subnets.md "../../../vpc/latest/userguide/create-subnets.md")
  in the _Amazon Virtual Private Cloud User Guide_.
- Create a new DB subnet group containing three or two of the private subnets that are
  associated with the AZs from the first point. For instructions, see
  [Step 2: Create the DB subnet group for the clone](#cross-vpc-cloning-create-subnet-group "#cross-vpc-cloning-create-subnet-group").

When all the prerequisites are in place, you can pause database activity on the original
cluster while you create the clone and switch your application to use it. After the clone is
created and you verify that you can connect to it, run your application code, and so on, you
can discontinue use of the original cluster.

## End-to-end example of creating a cross-VPC clone

Creating a clone in a different VPC than the original uses the same general steps as in the
preceding examples. Because the VPC ID is a property of the subnets, you don't actually
specify the VPC ID as a parameter when running any of the RDS CLI commands. The main
difference is that you are more likely to need to create new subnets, new subnets mapped to
specific AZs, a VPC security group, and a new DB subnet group. That's especially true if this
is the first Aurora cluster that you create in that VPC.

You can consult this checklist to verify that all the requirements are in place to perform
this type of cloning operation.

- Record the three AZs that are associated with the original cluster. For instructions, see
  [Step 1: Check the Availability Zones of the original cluster](#cross-vpc-cloning-check-original-azs "#cross-vpc-cloning-check-original-azs").
- Record the three or two AZs that are associated with the subnets in the DB subnet group
  for the original cluster. For instructions, see
  [Step 2: Check the DB subnet group of the original cluster](#cross-vpc-cloning-check-original-subnet-group "#cross-vpc-cloning-check-original-subnet-group").
- Create subnets that map to all three of the AZs that are associated with the original
  cluster. For instructions, see
  [Step 1: Create the subnets for the clone](#cross-vpc-cloning-create-clone-subnets "#cross-vpc-cloning-create-clone-subnets").
- Do any other networking setup, such as setting up a VPC security group, for client
  systems, application servers, and so on to be able to communicate with the DB instances in
  the clone. For instructions, see
  [Controlling access with security
  groups](Overview.md "Overview.md").
- Create a new DB subnet group containing three or two of the subnets that are associated
  with the AZs from the first point. For instructions, see
  [Step 2: Create the DB subnet group for the clone](#cross-vpc-cloning-create-subnet-group "#cross-vpc-cloning-create-subnet-group").

When all the prerequisites are in place, you can pause database activity on the original
cluster while you create the clone and switch your application to use it. After the clone is
created and you verify that you can connect to it, run your application code, and so on, you
can consider whether to keep both the original and clones running, or discontinue use of the
original cluster.

The following Linux examples show the sequence of AWS CLI operations to clone an Aurora DB
cluster from one VPC to another. Some fields that aren't relevant to the examples aren't shown
in the command output.

First, we check the IDs of the source and destination VPCs. The descriptive name that you
assign to a VPC when you create it is represented as a tag in the VPC metadata.

```
`$` aws ec2 describe-vpcs --query '*[].[VpcId,Tags]'
`[
 [
 'vpc-0f0c0fc0000b0ffb0',
 [
 {
 'Key': 'Name',
 'Value': 'clone-vpc-source'
 }
 ]
 ],
 [
 'vpc-9e99d9f99a999bd99',
 [
 {
 'Key': 'Name',
 'Value': 'clone-vpc-dest'
 }
 ]
 ]
]`

```

The original cluster already exists in the source VPC. To set up the clone using the same set
of AZs for the Aurora storage, we check the AZs used by the original cluster.

```
`$` aws rds describe-db-clusters --db-cluster-identifier original-cluster \
  --query 'sort_by(*[].AvailabilityZones[].{Zone:@},&Zone)' --output text

`us-east-1c
us-east-1d
us-east-1f`

```

We make sure there are subnets that correspond to the AZs used by the original cluster:
`us-east-1c`, `us-east-1d`, and
`us-east-1f`.

```
`$` aws ec2 create-subnet --vpc-id vpc-9e99d9f99a999bd99 \
  --availability-zone us-east-1c --cidr-block 10.0.0.128/28
`{
 'Subnet': {
 'AvailabilityZone': 'us-east-1c',
 'SubnetId': 'subnet-3333a33be3ef3e333',
 'VpcId': 'vpc-9e99d9f99a999bd99',
 }
}`

`$` aws ec2 create-subnet --vpc-id vpc-9e99d9f99a999bd99 \
--availability-zone us-east-1d --cidr-block 10.0.0.160/28
`{
 'Subnet': {
 'AvailabilityZone': 'us-east-1d',
 'SubnetId': 'subnet-4eeb444cd44b4d444',
 'VpcId': 'vpc-9e99d9f99a999bd99',
 }
}`

`$` aws ec2 create-subnet --vpc-id vpc-9e99d9f99a999bd99 \
--availability-zone us-east-1f --cidr-block 10.0.0.224/28
`{
 'Subnet': {
 'AvailabilityZone': 'us-east-1f',
 'SubnetId': 'subnet-66eea6666fb66d66c',
 'VpcId': 'vpc-9e99d9f99a999bd99',
 }
}`

```

This example confirms that there are subnets that map to the necessary AZs in the destination
VPC.

````
aws ec2 describe-subnets --query 'sort_by(*[] | [?VpcId == `vpc-9e99d9f99a999bd99`] |
[].{SubnetId:SubnetId,VpcId:VpcId,AvailabilityZone:AvailabilityZone}, &AvailabilityZone)' --output table

`---------------------------------------------------------------------------
| DescribeSubnets | +------------------+----------------------------+-------------------------+
| AvailabilityZone | SubnetId | VpcId | +------------------+----------------------------+-------------------------+
| us-east-1a | subnet-000ff0e00000c0aea | vpc-9e99d9f99a999bd99 |
| us-east-1b | subnet-1111d111111ca11b1 | vpc-9e99d9f99a999bd99 |
| us-east-1c | subnet-3333a33be3ef3e333 | vpc-9e99d9f99a999bd99 |
| us-east-1d | subnet-4eeb444cd44b4d444 | vpc-9e99d9f99a999bd99 |
| us-east-1f | subnet-66eea6666fb66d66c | vpc-9e99d9f99a999bd99 | +------------------+----------------------------+-------------------------+` ``` Before creating an Aurora DB cluster in the VPC, you must have a DB subnet group with subnets that map to the AZs used for Aurora storage. When you create a regular cluster, you can use any set of three AZs. When you clone an existing cluster, the subnet group must match at least two of the three AZs that it uses for Aurora storage. ``` `$` aws rds create-db-subnet-group \ --db-subnet-group-name subnet-group-in-other-vpc \ --subnet-ids '["subnet-3333a33be3ef3e333","subnet-4eeb444cd44b4d444","subnet-66eea6666fb66d66c"]' \ --db-subnet-group-description 'DB subnet group with 3 subnets: subnet-3333a33be3ef3e333,subnet-4eeb444cd44b4d444,subnet-66eea6666fb66d66c' `{ 'DBSubnetGroup': { 'DBSubnetGroupName': 'subnet-group-in-other-vpc', 'DBSubnetGroupDescription': 'DB subnet group with 3 subnets: subnet-3333a33be3ef3e333,subnet-4eeb444cd44b4d444,subnet-66eea6666fb66d66c', 'VpcId': 'vpc-9e99d9f99a999bd99', 'SubnetGroupStatus': 'Complete', 'Subnets': [ { 'SubnetIdentifier': 'subnet-4eeb444cd44b4d444', 'SubnetAvailabilityZone': { 'Name': 'us-east-1d' } }, { 'SubnetIdentifier': 'subnet-3333a33be3ef3e333', 'SubnetAvailabilityZone': { 'Name': 'us-east-1c' } }, { 'SubnetIdentifier': 'subnet-66eea6666fb66d66c', 'SubnetAvailabilityZone': { 'Name': 'us-east-1f' } } ] } }` ``` Now the subnets and DB subnet group are in place. The following example shows the `restore-db-cluster-to-point-in-time` that clones the cluster. The `--db-subnet-group-name` option associates the clone with the correct set of subnets that map to the correct set of AZs from the original cluster. ``` `$` aws rds restore-db-cluster-to-point-in-time \ --source-db-cluster-identifier original-cluster \ --db-cluster-identifier clone-in-other-vpc \ --restore-type copy-on-write --use-latest-restorable-time \ --db-subnet-group-name subnet-group-in-other-vpc `{ 'DBClusterIdentifier': 'clone-in-other-vpc', 'DBSubnetGroup': 'subnet-group-in-other-vpc', 'Engine': 'aurora-postgresql', 'EngineVersion': '15.4', 'Status': 'creating', 'Endpoint': 'clone-in-other-vpc.cluster-c0abcdef.us-east-1.rds.amazonaws.com' }` ``` The following example confirms that the Aurora storage in the clone uses the same set of AZs as in the original cluster. ``` `$` aws rds describe-db-clusters --db-cluster-identifier clone-in-other-vpc \ --query 'sort_by(*[].AvailabilityZones[].{Zone:@},&Zone)' --output text `us-east-1c us-east-1d us-east-1f` ``` At this point, you can create DB instances for the clone. Make sure that the VPC security group associated with each instance allows connections from the IP address ranges you use for the EC2 instances, application servers, and so on that are in the destination VPC.
````
