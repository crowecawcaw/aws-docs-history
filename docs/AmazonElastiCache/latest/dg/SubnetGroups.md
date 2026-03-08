# Creating a subnet group

A _cache subnet group_ is a collection of subnets that you may want
to designate for your caches in a VPC. When launching a cache in a VPC,
you need to select a cache subnet group. Then ElastiCache uses that cache subnet group to
assign IP addresses within that subnet to each cache node in the cache.

When you create a new subnet group, note the number of available
IP addresses. If the subnet has very few free IP addresses, you might be
constrained as to how many more nodes you can add to a cluster. To
resolve this issue, you can assign one or more subnets to a subnet group
so that you have a sufficient number of IP addresses in your cluster's
Availability Zone. After that, you can add more nodes to your
cluster.

If you choose IPV4 as your network type, a default subnet group will be available or you can choose to create a new one. ElastiCache uses that subnet group to choose a subnet and IP addresses within that subnet to associate with your nodes.

If you choose dual-stack or IPV6, you will be directed to create dual-stack or IPV6 subnets. For more information on network types, see [Choosing a network type in ElastiCache](network-type.md "network-type.md").
For more information, see [Create a subnet in your VPC](../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet "../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet").

The following procedures show you how to create a subnet group called
`mysubnetgroup` (console), the AWS CLI, and the
ElastiCache API.

## Creating a subnet group (Console)

The following procedure shows how to create a subnet group (console).

###### To create a subnet group (Console)

1. Sign in to the AWS Management Console, and open the ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. In the navigation list, choose **Subnet groups**.
3. Choose **Create subnet group**.
4. In the **Create subnet group** wizard,
   do the following.
   When all the settings are as you want them, choose **Create**.
   1. In the **Name** box,
      type a name for your subnet group.
   2. In the **Description** box,
      type a description for your subnet group.
   3. In the **VPC ID** box,
      choose your Amazon VPC.
   4. All subnets are chosen by default. In the **Selected subnets** panel,
      click **Manage** and select the Availability Zones or
      [Local Zones](Local_zones.md "Local_zones.md") and IDs of your private subnets,
      and then choose **Choose**.

5. In the confirmation message that appears, choose **Close**.

Your new subnet group appears in the **Subnet Groups** list of
the ElastiCache console. At the bottom of the window you can choose the subnet group to see details,
such as all of the subnets associated with this group.

## Creating a subnet group (AWS CLI)

At a command prompt, use the command `create-cache-subnet-group` to create a subnet group.

For Linux, macOS, or Unix:

```
aws elasticache create-cache-subnet-group \
    --cache-subnet-group-name `mysubnetgroup` \
    --cache-subnet-group-description `"Testing"` \
    --subnet-ids `subnet-53df9c3a`
```

For Windows:

```
aws elasticache create-cache-subnet-group ^
    --cache-subnet-group-name `mysubnetgroup` ^
    --cache-subnet-group-description `"Testing"` ^
    --subnet-ids `subnet-53df9c3a`
```

This command should produce output similar to the following:

```
{
    "CacheSubnetGroup": {
        "VpcId": "vpc-37c3cd17",
        "CacheSubnetGroupDescription": "Testing",
        "Subnets": [
            {
                "SubnetIdentifier": "subnet-53df9c3a",
                "SubnetAvailabilityZone": {
                    "Name": "us-west-2a"
                }
            }
        ],
        "CacheSubnetGroupName": "mysubnetgroup"
    }
}
```

For more information, see the AWS CLI topic create-cache-subnet-group.
