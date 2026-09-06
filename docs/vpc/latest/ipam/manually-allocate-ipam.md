

# Manually allocate a CIDR to a pool to reserve IP address space
<a name="manually-allocate-ipam"></a>

Follow the steps in this section to manually allocate a CIDR to a pool. You might do this to reserve a CIDR within an IPAM pool for later use. You can also reserve space in your IPAM pool to represent an on-premises network. IPAM manages that reservation for you and indicates if any CIDRs overlap with your on-premises IP space.

------
#### [ AWS Management Console ]

**To manually allocate a CIDR**

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the navigation pane, choose **Pools**.

1. By default, the default private scope is selected. If you don't want to use the default private scope, from the dropdown menu at the top of the content pane, choose the scope you want to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md).

1. In the content pane, choose a pool.

1. Choose **Actions** > **Create custom allocation**.

1. Choose whether to add a specific CIDR to allocate (for example, `10.0.0.0/24` for IPv4 or `2001:db8::/52` for IPv6) or add a CIDR by size by choosing the netmask length only (for example, `/24` for IPv4 or `/52` for IPv6).

1. (Optional) To tag the allocation, expand the **Tags** section and enter the key and value for each tag you want to add.

1. Choose **Allocate**.

1. You can view the allocation in IPAM by choosing **Pools** in the navigation pane, choosing a pool, and viewing the **Allocations** tab for the pool.

------
#### [ Command line ]

The commands in this section link to the *AWS CLI Command Reference*. The documentation provides detailed descriptions of the options that you can use when you run the commands.

Use the following AWS CLI commands to manually allocate a CIDR to a pool:

1. Get the ID of the IPAM pool that you want to create the allocation in: [describe-ipam-pools](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-pools.html).

1. Create the allocation: [allocate-ipam-pool-cidr](https://docs.aws.amazon.com/cli/latest/reference/ec2/allocate-ipam-pool-cidr.html). (Optional) To tag the allocation at creation, include the `--tag-specifications` parameter. For example:

   ```
   aws ec2 allocate-ipam-pool-cidr --ipam-pool-id {{ipam-pool-0533048da7eba92f6}} --netmask-length {{24}} --tag-specifications 'ResourceType=ipam-pool-allocation,Tags=[{Key={{Environment}},Value={{Production}}}]'
   ```

1. View the allocation: [get-ipam-pool-allocations](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-pool-allocations.html).

------

To release a manually allocated CIDR, see [Release an allocation](release-alloc-ipam.md).