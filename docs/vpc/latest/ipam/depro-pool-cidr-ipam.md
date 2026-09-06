

# Deprovision CIDRs from a pool
<a name="depro-pool-cidr-ipam"></a>

You may want to deprovision a pool CIDR to free up IP address space, simplify IP address management, prepare for network changes, or meet compliance requirements. Deprovisioning a pool CIDR allows for better control and optimization of your IP address allocations within IPAM, while ensuring unused IP space is reclaimed and made available for future use. You can't deprovision the CIDR if there are allocations in the pool. To remove allocations, see [Release an allocation](release-alloc-ipam.md).

Follow the steps in this section to deprovision CIDRs from an IPAM pool. When you deprovision all pool CIDRs, the pool can no longer be used for allocations. You must first provision a new CIDR to the pool before you can use the pool for allocations.

------
#### [ AWS Management Console ]

**To deprovision a pool CIDR**

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the navigation pane, choose **Pools**.

1. From the dropdown menu at the top of the content pane, choose the scope that you want to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md).

1. In the content pane, choose the pool whose CIDRs you want to deprovision.

1. Choose the **CIDRs** tab.

1. Select one or more CIDRs and choose **Deprovision CIDRs**.

1. Choose **Deprovision CIDR**.

------
#### [ Command line ]

The commands in this section link to the *AWS CLI Command Reference*. The documentation provides detailed descriptions of the options that you can use when you run the commands.

Use the following AWS CLI commands to deprovision a pool CIDR:

1. Get an IPAM pool ID: [describe-ipam-pools](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-pools.html)

1. View your current CIDRs for the pool: [get-ipam-pool-cidrs](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-pool-cidrs.html)

1. Deprovision CIDRs: [deprovision-ipam-pool-cidr](https://docs.aws.amazon.com/cli/latest/reference/ec2/deprovision-ipam-pool-cidr.html)

1. View your updated CIDRs: [get-ipam-pool-cidrs](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-pool-cidrs.html)

------

To provision a new CIDR to the pool, see [Deprovision CIDRs from a pool](#depro-pool-cidr-ipam). If you want to delete the pool, see [Delete a pool](delete-pool-ipam.md).