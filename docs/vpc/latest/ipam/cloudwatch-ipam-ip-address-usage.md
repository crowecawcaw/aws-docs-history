# IPAM metrics

IPAM publishes data about your IPAM, pools, and scopes to Amazon CloudWatch. You can use these
metrics to create alarms for IPAM pools to notify you if the address pools are nearing
exhaustion or if resources fail to comply with allocation rules set on a pool. Creating
alarms and setting up notifications with Amazon CloudWatch is outside the scope of this section.
For more information, see [Using
Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_.

The metrics and dimensions that IPAM sends to Amazon CloudWatch are listed below.

## IPAM metrics

The `AWS/IPAM` namespace includes the following IPAM metrics.

| Metric name        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TotalActiveIpCount | The total active IP count is the number of active IP<br>addresses in your IPAM that you would be charged if you switched from the Free Tier<br>to the Advanced Tier. An active IP address is defined as an IP address or a prefix associated with an Elastic Network Interface (ENI) that is attached to a resource such as an EC2 Instance.<br>• This metric is only available to customers in the Free Tier.<br>• If your IPAM is [integrated with AWS Organizations](enable-integ-ipam.md "enable-integ-ipam.md"), the active IP count covers all the Organization accounts.<br>• You cannot view a breakdown of the active IP count by IP type (public/private) or class (IPv4/IPv6).<br>• IPAM only counts IPs from ENIs owned by monitored accounts. The count may be inaccurate for shared subnets. IP addresses are excluded if the subnet owner or ENI owner is not covered by IPAM. |

## IPAM pool metrics

The `AWS/IPAM` namespace includes the following pool metrics for IPAM.

| Metric name               | Description                                                                                                                                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CompliantResourceCidrs    | The number of managed resource CIDRs that comply with the allocation rules of the IPAM pool. For more information about allocation rules, see [Create a top-level IPv4 pool](create-top-ipam.md "create-top-ipam.md").        |
| NoncompliantResourceCidrs | The number of managed resource CIDRs that do not comply with the allocation rules of the IPAM pool. For more information about allocation rules, see [Create a top-level IPv4 pool](create-top-ipam.md "create-top-ipam.md"). |
| PercentAllocated          | The percentage of a pool's IP space that has been allocated to other pools.                                                                                                                                                   |
| PercentAssigned           | The percentage of a pools IP space that has been allocated to resources, including manual allocations.                                                                                                                        |
| PercentAvailable          | The percentage of a pool's IP space that has not been allocated to other pools or resources.                                                                                                                                  |

## IPAM scope metrics

The `AWS/IPAM` namespace includes the following scope metrics for IPAM.

| Metric name               | Description                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| CompliantResourceCidrs    | The number of resource CIDRs that comply with the allocation rules for IPAM pools in the scope.                                      |
| ManagedResourceCidrs      | The number of resource CIDRs for manageable resources (VPCs or public IPv4 pools) that are allocated from an IPAM pool in the scope. |
| NoncompliantResourceCidrs | The number of resource CIDRs that do not comply with the allocation rules for the IPAM pools in the scope.                           |
| OverlappingResourceCidrs  | The number of resource CIDRs that overlap in the scope.                                                                              |
| UnmanagedResourceCidrs    | The number of resource CIDRs in the scope that are currently associated with manageable resources but are not managed by IPAM.       |

## IPAM public IP metrics

The `AWS/IPAM` namespace includes the following public IP metrics for IPAM.

| Metric name                      | Description                                                                                                                                                                                 |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AmazonOwnedContigIPs             | The number of IP addresses within CIDRs that are provisioned to<br>Amazon-provided contiguous public IPv4 pools owned by the IPAM.                                                          |
| AllocatedAmazonOwnedContigIPs    | The number of IP addresses that have been allocated from an<br>Amazon-provided contiguous public IPv4 pool CIDR block.                                                                      |
| UnallocatedAmazonOwnedContigIPs  | The number of IP addresses within the Amazon-provided contiguous<br>public IPv4 pool CIDR block owned by the IPAM.                                                                          |
| AssociatedAmazonOwnedContigIPs   | The number of Elastic IP addresses that have been allocated from an<br>Amazon-provided contiguous public IPv4 pool CIDR block that are<br>associated with an elastic network interface.     |
| UnassociatedAmazonOwnedContigIPs | The number of Elastic IP addresses that have been allocated from an<br>Amazon-provided contiguous public IPv4 pool CIDR block that are not<br>associated with an elastic network interface. |

## IPAM prefix list resolver metrics

We encourage you to set CloudWatch alarms on failure metrics as you may need to reassess and adjust [IPAM prefix list resolver rules](automate-prefix-list-updates.md "automate-prefix-list-updates.md") to stay within the limits for version and prefix list size.

| Metric name                                  | Description                                                                                                                                                                                                                                  |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IpamPrefixListResolverSyncFailure            | Prefix list resolver failed to sync with target. This may happen if a quota such as 'CIDR entries per prefix list resolver version' is exceeded, the target prefix list is not found, or sync is disabled on the target managed prefix list. |
| IpamPrefixListResolverSyncSuccess            | Prefix list resolver successfully synced with target.                                                                                                                                                                                        |
| IpamPrefixListResolverVersionCreationSuccess | Version creation succeeded.                                                                                                                                                                                                                  |
| IpamPrefixListResolverVersionCreationFailure | Version creation failed. This may happen if you've reached your 'CIDR entries per prefix list resolver version' quota.                                                                                                                       |

## Metric dimensions

To filter the IPAM metrics, use the following dimensions.

| Dimension     | Description                                                     |
| ------------- | --------------------------------------------------------------- |
| AddressFamily | The IP address family for resource CIDRs (IPv4 or IPv6).        |
| Locale        | The AWS Region where an IPAM pool is available for allocations. |
| PoolID        | The ID of a pool.                                               |
| ScopeID       | The ID of a scope.                                              |

For information about monitoring VPCs with Amazon CloudWatch, see [CloudWatch metrics for your VPCs](../userguide/vpc-cloudwatch.md "../userguide/vpc-cloudwatch.md") in the
_Amazon Virtual Private Cloud User Guide_.
