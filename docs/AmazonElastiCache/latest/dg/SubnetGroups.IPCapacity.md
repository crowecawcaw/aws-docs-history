

# IP address capacity for scaling operations
<a name="SubnetGroups.IPCapacity"></a>

When you scale out a cluster by adding shards or replicas, Amazon ElastiCache provisions new nodes. Each node requires an available IP address in a subnet within the target Availability Zone. If the subnets in an Availability Zone don't have enough free IP addresses, the scaling operation fails.

To avoid this issue, review the available IP address capacity of your subnet group's subnets before you scale. To check the number of available IP addresses for each subnet, use the Amazon Elastic Compute Cloud (Amazon EC2) `DescribeSubnets` API. You can also view this information in the Amazon VPC console.

If a subnet is approaching IP address exhaustion, take one of the following actions before you scale:
+ Add a subnet with sufficient available IP addresses to the subnet group in the same Availability Zone.
+ Remove unused resources, such as unattached network interfaces, to free IP addresses in the existing subnet.
+ Replace the subnet with one that uses a larger CIDR block.