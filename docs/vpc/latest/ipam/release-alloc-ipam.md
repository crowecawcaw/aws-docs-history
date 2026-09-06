

# Release an allocation
<a name="release-alloc-ipam"></a>

If you are planning to delete a pool, you might need to release a pool allocation. An allocation is a CIDR assignment from an IPAM pool to another resource or IPAM pool.

You cannot delete pools if the pools have CIDRs provisioned, and you cannot deprovision CIDRs if the CIDRs are allocated to resources.

**Note**  
To release a manual allocation, use the steps in this section or call the [ReleaseIpamPoolAllocation API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReleaseIpamPoolAllocation.html). 
To release an allocation in a private scope, you must ignore or delete the resource CIDR. For more information, see [Change the monitoring state of VPC CIDRs](change-monitoring-state-ipam.md). After some time, Amazon VPC IPAM will automatically release the allocation on your behalf.  

**Example**  
**Example**  
If you have a VPC CIDR in a private scope, to release the allocation you must either ignore or delete the VPC CIDR. After some time, Amazon VPC IPAM will automatically release the VPC CIDR allocation from the IPAM pool.
To release an allocation in a public scope, you must delete the resource CIDR. You cannot ignore public resource CIDRs. For more information, see *Cleanup* in [Bring your own public IPv4 CIDR to IPAM using only the AWS CLI](tutorials-byoip-ipam-ipv4.md) or *Cleanup* in [Bring your own IPv6 CIDR to IPAM using only the AWS CLI](tutorials-byoip-ipam-ipv6.md). After some time, Amazon VPC IPAM will automatically release the allocation on your behalf.
For Amazon VPC IPAM to release allocations on your behalf, all account permissions must be properly configured for either [single-account use](enable-single-user-ipam.md) or [multi-account use](enable-integ-ipam.md).

When you release a CIDR that's managed by your IPAM, Amazon VPC IPAM recycles the CIDR back into an IPAM pool. If you are using IPAM in the Advanced Tier, it takes a few minutes for the CIDR to become available for future allocations. If you are using IPAM in the Free Tier, it will take up to 48 hours for the CIDR to become available for future allocations. For more information about pools and allocations, see [How IPAM works](how-it-works-ipam.md).

**Warning**  
When you release an allocation, all tags associated with the allocation are permanently deleted. You can't recover deleted tags.

------
#### [ AWS Management Console ]

**To release a pool allocation**

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the navigation pane, choose **Pools**.

1. From the dropdown menu at the top of the content pane, choose the scope you want to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md).

1. In the content pane, choose the pool that the allocation is in.

1. Choose the **Allocations** tab.

1. Select one or more allocations. You can identify allocations by their **Resource type**:
   + **custom**: A custom allocation.
   + **vpc**: A VPC allocation.
   + **ipam-pool**: An IPAM pool allocation.
   + **ec2-public-ipv4-pool**: A public IPv4 pool allocation.
   + **subnet**: A subnet allocation.

1. Choose **Actions** > **Release custom allocation**.

1. Choose **Deallocate CIDR**.

------
#### [ Command line ]

The commands in this section link to the *AWS CLI Command Reference*. The documentation provides detailed descriptions of the options that you can use when you run the commands.

Use the following AWS CLI commands to release a pool allocation:

1. Get an IPAM pool ID: [describe-ipam-pools](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-pools.html)

1. View your current allocations in the pool: [get-ipam-pool-allocations](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-pool-allocations.html)

1. Release an allocation: [release-ipam-pool-allocation](https://docs.aws.amazon.com/cli/latest/reference/ec2/release-ipam-pool-allocation.html)

1. View your updated allocations: [get-ipam-pool-allocations](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-pool-allocations.html)

------

To add a new allocation, see [Allocate CIDRs from an IPAM pool](allocate-cidrs-ipam.md). To delete the pool after releasing allocations, you must first [Deprovision CIDRs from a pool](depro-pool-cidr-ipam.md).