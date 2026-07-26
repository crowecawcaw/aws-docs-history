# Ensuring sufficient IP addresses for scaling operations

When you scale out a cluster by adding shards or replicas, MemoryDB provisions new nodes. Each node requires an available IP address in a subnet within the target Availability Zone. If the subnets in an Availability Zone do not have enough free IP addresses, the scaling operation can fail.

To avoid this issue, review the available IP address capacity of your subnet group's subnets before you scale. You can check the number of available IP addresses for each subnet with the Amazon EC2 `DescribeSubnets` API or in the Amazon VPC console.

If a subnet is approaching IP address exhaustion, take one of the following actions before you scale:

- Add a subnet with sufficient available IP addresses to the subnet group in the same Availability Zone.
- Free IP addresses in the existing subnet by removing unused resources such as unattached network interfaces.
- Replace the subnet with one that uses a larger CIDR block.
