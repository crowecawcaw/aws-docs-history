# Deprovision CIDRs from a pool

You may want to deprovision a pool CIDR to free up IP address space, simplify IP address
management, prepare for network changes, or meet compliance requirements. Deprovisioning a pool CIDR allows for better control and optimization of your IP address
allocations within IPAM, while ensuring unused IP space is reclaimed and made available for
future use. You can't deprovision the CIDR if there are allocations in the pool. To remove allocations,
see [Release an allocation](release-alloc-ipam.md "release-alloc-ipam.md").

Follow the steps in this section to deprovision CIDRs from an IPAM pool.
When you deprovision all pool CIDRs, the pool can no longer be used for allocations.
You must first provision a new CIDR to the pool before you can use the pool for allocations.

AWS Management Console

###### To deprovision a pool CIDR

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. From the dropdown menu at the top of the content pane, choose the
   scope that you want to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
4. In the content pane, choose the pool whose CIDRs you want to deprovision.
5. Choose the **CIDRs** tab.
6. Select one or more CIDRs and choose **Deprovision CIDRs**.
7. Choose **Deprovision CIDR**.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to deprovision a pool CIDR:

1. Get an IPAM pool ID: [describe-ipam-pools](../../../cli/latest/reference/ec2/describe-ipam-pools.md "../../../cli/latest/reference/ec2/describe-ipam-pools.md")
2. View your current CIDRs for the pool: [get-ipam-pool-cidrs](../../../cli/latest/reference/ec2/get-ipam-pool-cidrs.md "../../../cli/latest/reference/ec2/get-ipam-pool-cidrs.md")
3. Deprovision CIDRs: [deprovision-ipam-pool-cidr](../../../cli/latest/reference/ec2/deprovision-ipam-pool-cidr.md "../../../cli/latest/reference/ec2/deprovision-ipam-pool-cidr.md")
4. View your updated CIDRs: [get-ipam-pool-cidrs](../../../cli/latest/reference/ec2/get-ipam-pool-cidrs.md "../../../cli/latest/reference/ec2/get-ipam-pool-cidrs.md")

To provision a new CIDR to the pool, see Deprovision CIDRs from a pool. If you want to delete the pool, see [Delete a pool](delete-pool-ipam.md "delete-pool-ipam.md").
