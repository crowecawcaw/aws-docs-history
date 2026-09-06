

# Working with a Neptune DB cluster in dual-stack mode
<a name="neptune-dualstack-db-cluster"></a>

When you create or modify a Neptune DB cluster, you can specify *dual-stack mode* to allow your resources to communicate with the DB cluster over IPv4, IPv6, or both. A DB cluster in dual-stack mode supports both Internet Protocol version 4 (IPv4) and Internet Protocol version 6 (IPv6) addressing.

## Overview of dual-stack mode
<a name="neptune-dualstack-overview"></a>

A Neptune DB cluster runs in dual-stack mode when it can communicate over both the IPv4 and IPv6 addressing protocols. Resources can then communicate with the DB cluster using either IPv4, IPv6, or both protocols. Private dual-stack mode DB clusters have IPv6 endpoints that are restricted to VPC access only, ensuring your IPv6 endpoints remain private. Public dual-stack mode DB clusters provide both IPv4 and IPv6 endpoints that you can access from the internet.

## Dual-stack mode and DB subnet groups
<a name="neptune-dualstack-subnet-groups"></a>

To use dual-stack mode, each subnet in the DB subnet group must have an IPv6 CIDR block associated with it.

Because Neptune does not allow changing the DB subnet group after cluster creation, you must either create the cluster with a dual-stack-capable subnet group, or add IPv6 CIDR blocks to the existing subnets before modifying the cluster to dual-stack mode.

After a DB cluster is in dual-stack mode, clients can connect to it normally. Ensure that client security firewalls and Neptune DB cluster security groups allow traffic over IPv6. To connect, clients use the DB cluster's endpoint. The DB cluster detects the client's preferred network protocol and uses that protocol for the connection.

If a DB subnet group stops supporting dual-stack mode, there's a risk of an incompatible network state for associated DB clusters. This can happen because of subnet deletion or CIDR disassociation. Also, you can't use that DB subnet group to create a new dual-stack mode DB cluster.

## Creating and modifying dual-stack mode DB clusters
<a name="neptune-dualstack-working-with"></a>

When you create or modify a DB cluster, you can specify dual-stack mode to allow your resources to communicate with your DB cluster over IPv4, IPv6, or both.

When you use the AWS Management Console to create or modify a DB cluster, you can specify dual-stack mode in the **Network type** section.

When you use the AWS Command Line Interface (AWS CLI) to create a DB cluster, set the `--network-type` option to `DUAL` to use dual-stack mode:

```
aws neptune create-db-cluster \
    --db-cluster-identifier my-dual-stack-cluster \
    --engine neptune \
    --db-subnet-group-name my-dual-stack-subnet-group \
    --network-type DUAL
```

When you use the AWS CLI to modify an existing DB cluster to use dual-stack mode:

```
aws neptune modify-db-cluster \
    --db-cluster-identifier my-cluster \
    --network-type DUAL \
    --apply-immediately
```

When you use the Neptune API to create or modify a DB cluster, set the `NetworkType` parameter to `DUAL` to use dual-stack mode.

## Modifying IPv4-only DB clusters to use dual-stack mode
<a name="neptune-dualstack-modifying"></a>

You can modify an IPv4-only DB cluster to use dual-stack mode. To do so, change the network type of the DB cluster.

Before modifying a DB cluster to use dual-stack mode, ensure that its DB subnet group supports dual-stack mode. Because you cannot change the DB subnet group after the cluster is created, you must add IPv6 CIDR blocks to the existing subnets in the cluster's subnet group.

**To modify an IPv4-only DB cluster to use dual-stack mode**

1. Add IPv6 support to the existing DB subnet group's subnets:

   1. Associate an IPv6 CIDR block with your VPC. For instructions, see [Add an IPv6 CIDR block to your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/modify-vpcs.html#vpc-associate-ipv6-cidr) in the *Amazon VPC User Guide*.

   1. Attach the IPv6 CIDR block to all of the subnets in your DB subnet group. For instructions, see [Add an IPv6 CIDR block to your subnet](https://docs.aws.amazon.com/vpc/latest/userguide/modify-subnets.html#subnet-associate-ipv6-cidr) in the *Amazon VPC User Guide*.

   1. Confirm that the DB subnet group supports dual-stack mode. Using the AWS CLI, run the `describe-db-subnet-groups` command and check `SupportedNetworkTypes` in the output.

1. Modify the DB cluster to use dual-stack mode. Using the AWS CLI:

   ```
   aws neptune modify-db-cluster \
       --db-cluster-identifier my-cluster \
       --network-type DUAL \
       --apply-immediately
   ```

1. Confirm the DB cluster is in dual-stack mode by checking the `NetworkType` in the output of `describe-db-clusters`.

If you can't connect to the DB cluster after the change, ensure that the client and database security firewalls and route tables allow traffic to the database on the selected network (either IPv4 or IPv6).

## Limitations for dual-stack network DB clusters
<a name="neptune-dualstack-limitations"></a>

The following limitations apply to dual-stack network Neptune DB clusters:
+ The network type is set at the DB cluster level. All DB instances in the cluster inherit the cluster's network type. You cannot set a different network type for individual instances.
+ DB clusters can't use the network type `IPV6` exclusively. They can use `IPV4` exclusively or dual-stack mode (`DUAL`).
+ Neptune doesn't support native IPv6 subnets (IPv6-only subnets). DB cluster subnets must support both IPv4 and IPv6 to use dual-stack mode.