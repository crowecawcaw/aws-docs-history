# Setting up network prerequisites for RDS Proxy

Using RDS Proxy requires you to have a common virtual private cloud (VPC) between your
RDS DB instance and RDS Proxy. This VPC should have a minimum of two subnets that are in
different Availability Zones. Your account can either own these subnets or share them with
other accounts. For information about VPC sharing, see [Work with shared VPCs](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md").

For IPv6 support, additional network configuration is required:

- **IPv6 endpoint network types** – Your VPC and subnets must be configured to support IPv6. This includes having IPv6 CIDR blocks assigned to your VPC and subnets.
- **Dual-stack endpoint network types** – Your VPC and subnets must support both IPv4 and IPv6 addressing.
- **IPv6 target connection network types** – Your database must be configured for dual-stack mode to support IPv6 connections from the proxy.
  Your client application resources such as Amazon EC2, Lambda, or Amazon ECS can be in
  the same VPC as the proxy. Or they can be in a separate VPC from the proxy. If you
  successfully connected to any RDS DB instances
  , you already have the
  required network resources.

###### Topics

- [Getting information about your subnets](#rds-proxy-network-prereqs.subnet-info "#rds-proxy-network-prereqs.subnet-info")
- [Planning for IP address capacity](#rds-proxy-network-prereqs.plan-ip-address "#rds-proxy-network-prereqs.plan-ip-address")

## Getting information about your subnets

To create a proxy, you must provide the subnets and the VPC that the proxy operates within.
The following Linux example shows AWS CLI commands that examine the VPCs and subnets owned by your
AWS account. In particular, you pass subnet IDs as parameters when you create a proxy using the CLI.

```
aws ec2 describe-vpcs
aws ec2 describe-internet-gateways
aws ec2 describe-subnets --query '*[].[VpcId,SubnetId]' --output text | sort

```

The following Linux example shows AWS CLI commands to determine the subnet IDs
corresponding to a specific RDS DB instance. Find the VPC ID for the DB instance. Examine the VPC to
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

An RDS Proxy automatically adjusts its capacity as needed based on the size and number
of DB instances registered with it. Certain operations might also require additional proxy
capacity such as increasing the size of a registered database or internal
RDS Proxy maintenance operations. During these operations, your proxy might
need more IP addresses to provision the extra capacity. These
additional addresses allow your proxy to scale without affecting your workload. A lack of
free IP addresses in your subnets prevents a proxy from scaling up. This can lead to
higher query latencies or client connection failures.

RDS notifies you through event `RDS-EVENT-0243` when there aren't enough free IP addresses in your subnets.
For information about this event, see [Working with RDS Proxy events](rds-proxy.md "rds-proxy.md").

###### Note

RDS Proxy doesn't consume more than 215 IP addresses for each proxy in a
VPC.

Reserve the following minimum numbers of free IP addresses in your subnets for your
proxy, based on DB instance class sizes.

| DB instance class       | Minimum free IP addresses |
| ----------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| db.\*.xlarge or smaller | 10                        |
| db.\*.2xlarge           | 15                        |
| db.\*.4xlarge           | 25                        |
| db.\*.8xlarge           | 45                        |
| db.\*.12xlarge          | 60                        |
| db.\*.16xlarge          | 75                        |
| db.\*.24xlarge          | 110                       | These recommended numbers of IP addresses are estimates for a proxy with only the default endpoint. A proxy with additional endpoints or read replicas might need more free IP addresses. For each additional endpoint, we recommend that you reserve three more IP addresses. For each read replica, we recommend that you reserve additional IP addresses as specified in the table based on that read replica's size. |
