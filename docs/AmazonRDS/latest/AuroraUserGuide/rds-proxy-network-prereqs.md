# Setting up network prerequisites for RDS Proxy

Using RDS Proxy requires you to have a common virtual private cloud (VPC) between your
Aurora DB
cluster and RDS Proxy. This VPC should have a minimum of two subnets that are in
different Availability Zones. Your account can either own these subnets or share them with
other accounts. For information about VPC sharing, see [Work with shared VPCs](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md").

For IPv6 support, additional network configuration is required:

- **IPv6 endpoint network types** – Your VPC and subnets must be configured to support IPv6. This includes having IPv6 CIDR blocks assigned to your VPC and subnets.
- **Dual-stack endpoint network types** – Your VPC and subnets must support both IPv4 and IPv6 addressing.
- **IPv6 target connection network types** – Your database must be configured for dual-stack mode to support IPv6 connections from the proxy.
  Your client application resources such as Amazon EC2, Lambda, or Amazon ECS can be in
  the same VPC as the proxy. Or they can be in a separate VPC from the proxy. If you
  successfully connected to any
  Aurora DB clusters, you already have the
  required network resources.

###### Topics

- [Getting information about your subnets](#rds-proxy-network-prereqs.subnet-info "#rds-proxy-network-prereqs.subnet-info")
- [Planning for IP address capacity](#rds-proxy-network-prereqs.plan-ip-address "#rds-proxy-network-prereqs.plan-ip-address")

## Getting information about your subnets

If you're just getting started with Aurora, you can learn the basics
of connecting to a database by following the procedures in
[Setting up your environment for Amazon Aurora](CHAP_SettingUp_Aurora.md "CHAP_SettingUp_Aurora.md"). You can also follow the
tutorial in [Getting started with Amazon Aurora](CHAP_GettingStartedAurora.md "CHAP_GettingStartedAurora.md").

To create a proxy, you must provide the subnets and the VPC that the proxy operates within.
The following Linux example shows AWS CLI commands that examine the VPCs and subnets owned by your
AWS account. In particular, you pass subnet IDs as parameters when you create a proxy using the CLI.

```
aws ec2 describe-vpcs
aws ec2 describe-internet-gateways
aws ec2 describe-subnets --query '*[].[VpcId,SubnetId]' --output text | sort

```

The following Linux example shows AWS CLI commands to determine the subnet IDs
corresponding to a specific Aurora DB cluster.

For an Aurora cluster, first
you find the ID for one of the associated DB instances. You can extract the subnet IDs used
by that DB instance. To do so, examine the nested fields within the
`DBSubnetGroup` and `Subnets` attributes in the describe output for
the DB instance. You specify some or all of those subnet IDs when setting up a proxy for
that database server.

```
`$` # Find the ID of any DB instance in the cluster.
`$`  aws rds describe-db-clusters --db-cluster-identifier `my_cluster_id` --query '*[].[DBClusterMembers]|[0]|[0][*].DBInstanceIdentifier' --output text

```

```
``my_instance_id`
`instance_id_2`
`instance_id_3``
```

After finding the DB instance identifier, examine the associated VPC to
find its subnets. The following Linux example shows how.

```
`$` #From the DB instance, trace through the DBSubnetGroup and Subnets to find the subnet IDs.
$ aws rds describe-db-instances --db-instance-identifier `my_instance_id` --query '*[].[DBSubnetGroup]|[0]|[0]|[Subnets]|[0]|[*].SubnetIdentifier' --output text

```

```
``subnet_id_1`
`subnet_id_2`
`subnet_id_3`
...`
```

```
`$` #From the DB instance, find the VPC.
`$` aws rds describe-db-instances --db-instance-identifier `my_instance_id` --query '*[].[DBSubnetGroup]|[0]|[0].VpcId' --output text

```

```
`my_vpc_id`
```

```
`$` aws ec2 describe-subnets --filters Name=vpc-id,Values=`my_vpc_id` --query '*[].[SubnetId]' --output text
```

```
``subnet_id_1`
`subnet_id_2`
`subnet_id_3`
`subnet_id_4`
`subnet_id_5`
`subnet_id_6``

```

## Planning for IP address capacity

RDS Proxy automatically adjusts its capacity based on the configuration of DB instances
registered with it. For provisioned instances, this is determined by the instance
size and for Aurora Serverless v2 instances, this is
determined by the maximum ACU capacity. Certain operations might also require
additional capacity such as increasing the size of a registered database or internal
RDS Proxy maintenance operations. During these operations, your proxy might need more IP
addresses to provision the extra capacity. These additional addresses allow your proxy to
scale without affecting your workload. A lack of free IP addresses in your subnets
prevents a proxy from scaling up. This can lead to higher query latencies or client
connection failures. RDS notifies you through event `RDS-EVENT-0243` when there
aren't enough free IP addresses in your subnets. For information about this event, see
[Working with RDS Proxy events](rds-proxy.md "rds-proxy.md").

Reserve the following minimum numbers of free IP addresses in your subnets for your
proxy, based on DB instance class sizes.

| DB instance class       | Minimum free IP addresses |
| ----------------------- | ------------------------- |
| db.\*.xlarge or smaller | 10                        |
| db.\*.2xlarge           | 15                        |
| db.\*.4xlarge           | 25                        |
| db.\*.8xlarge           | 45                        |
| db.\*.12xlarge          | 60                        |
| db.\*.16xlarge          | 75                        |
| db.\*.24xlarge          | 110                       |

For Aurora Serverless v2, reserve the following minimum numbers of
free IP addresses in your subnets for your proxy, based on maximum ACU capacity.

| `Maximum ACU Capacity` | Minimum free IP addresses |
| ---------------------- | ------------------------- |
| 16 or smaller          | 10                        |
| 32                     | 15                        |
| 64                     | 25                        |
| 96                     | 30                        |
| 128                    | 40                        |
| 160                    | 50                        |
| 192                    | 55                        |
| 224                    | 65                        |
| 256                    | 75                        |

###### Note

RDS Proxy doesn't consume more than 215 IP addresses for each proxy in a
VPC.

RDS Proxy requires a minimum of 10 IP addresses for your Aurora database. These recommended numbers of IP addresses are estimates for a
proxy with only the default endpoint. For each additional custom endpoint, we recommend
reserving three more IP addresses. For each Aurora
reader instance, we recommend that you reserve additional IP addresses as specified in the table based on that
reader’s maximum ACUs for Aurora Serverless v2 target
or DB instance size for a provisioned target.

To estimate the required IP addresses for a proxy that's associated with
an Aurora DB cluster with:

- 1 provisioned writer instance of size `db.r5.8xlarge`
  and 1 provisioned reader instance of size `db.r5.2xlarge`.
- The proxy attached to this cluster has a default endpoint and a custom endpoint with the read-only role.

In this case, the proxy needs approximately 63 free IP addresses (45 for the writer instance, 15
for reader instance, and 3 for the additional custom endpoint).

To estimate the required IP addresses for a proxy that's associated with an Aurora DB cluster that has:

- 1 Aurora Serverless v2 writer instance
  with maximum capacity of 256 ACUs and 1 Serverless v2 reader instance with maximum capacity of 192 ACUs.
- The proxy that's attached to this cluster has the default endpoint and 1 custom endpoint with the read-only role.

In this case, the proxy needs approximately
133 free IP addresses (75 for the writer instance, 55 for reader instance, and 3 for the additional custom endpoint).

To estimate the required IP addresses for a proxy that's associated with an Aurora cluster that has:

- 1 provisioned writer instance with DB instance size of db.r5.4xlarge and 1 Serverless v2 reader instance with maximum capacity of 64 ACUs.
- The proxy that's attached to this cluster has the default endpoint and 1 custom endpoint with the read-only role.
  In this case, the proxy needs approximately 53 free IP addresses (25 for the writer instance, 25 for reader instance, and 3 for the additional custom endpoint).

To estimate the required IP addresses for a proxy that's associated with an Aurora DB cluster that has:

- 1 provisioned writer instance of size db.r5.24xlarge and 3
  provisioned reader instance of size db.r5.8xlarge.
- The proxy that's attached to this DB cluster has the default endpoint and 1 custom endpoint with the read-only role.

In this case, the proxy needs 215 free IP addresses. While calculations suggest 248 IPs (110 + (3\*45) + 3), RDS Proxy doesn't consume more than 215 IP addresses for each proxy in a VPC.
