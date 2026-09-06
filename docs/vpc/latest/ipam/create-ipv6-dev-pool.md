

# Create a development IPv6 address pool in your IPAM
<a name="create-ipv6-dev-pool"></a>

Follow the steps in this section to create a development pool within your IPv6 Regional pool. If you only need a Regional pool and don't need development pools, skip to [Allocate CIDRs from an IPAM pool](allocate-cidrs-ipam.md).

The following example shows the hierarchy of the pool structure that you can create with the instructions in this guide. At this step, you are creating a development IPAM pool:
+ IPAM operating in AWS Region 1 and AWS Region 2
  + Scope
    + Regional pool in AWS Region 1 (2001:db8::/52)
      + **Development pool (2001:db8::/54)**
        +  Allocation for a VPC (2001:db8::/56)

In the preceding example, the CIDRs that are used are examples only. They illustrate that each pool within the top-level pool is provisioned with a portion of the top-level CIDR.

------
#### [ AWS Management Console ]

**To create a development pool within an IPv6 Regional pool**

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the navigation pane, choose **Pools**.

1. Choose **Create pool**.

1. Under **IPAM scope**, choose a scope. For more information about scopes, see [How IPAM works](how-it-works-ipam.md).

1. (Optional) Add a **Name tag** for the pool and a description for the pool.

1. Under **Source**, choose **IPAM pool**. Then, under **Source pool**, choose the IPv6 Regional pool.

1. Under **Resource planning**, leave **Plan IP space within the scope** selected. For more information about using this option to plan for subnet IP space within a VPC, see [Tutorial: Plan VPC IP address space for subnet IP allocations](tutorials-subnet-planning.md).

1. (Optional) Choose a CIDR to provision for the pool. You can only provision a CIDR that was provisioned to the top-level pool. You can create a pool without a CIDR, but you won't be able to use the pool for allocations until you've provisioned a CIDR for it. You can add CIDRs to a pool at any time by editing the pool.

1. You have the same allocation rule options here as you did when you created the IPv6 Regional pool. See [Create a Regional IPv6 address pool in your IPAM](create-ipv6-reg-pool.md) for an explanation of the options that are available when you create pools. The allocation rules for the pool are not inherited from the pool above it in the hierarchy. If you do not apply any rules here, no allocation rules will be set for the pool.

1. (Optional) Choose **Tags** for the pool.

1. When you've finished configuring your pool, choose **Create pool**.

1. See [Allocate CIDRs from an IPAM pool](allocate-cidrs-ipam.md).

------
#### [ Command line ]

The commands in this section link to the *AWS CLI Command Reference*. The documentation provides detailed descriptions of the options that you can use when you run the commands.

Use the following AWS CLI commands to create an IPv6 Regional pool in your IPAM:

1. Get the ID of the scope that you want to create the pool in: [describe-ipam-scopes](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-scopes.html)

1. Get the ID of the pool that you want to create the pool in: [describe-ipam-pools](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-pools.html)

1. Create the pool: [create-ipam-pool](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-ipam-pool.html)

1. View the new pool: [describe-ipam-pools](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-pools.html)

------

Repeat these steps to create additional development pools within the IPv6 Regional pool, as needed.