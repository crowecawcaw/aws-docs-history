# Create a development IPv4 pool

Follow the steps in this section to create a development pool within your Regional pool.
If you need only a top-level and Regional pool, and don't need development pools, skip to
[Allocate CIDRs from an IPAM pool](allocate-cidrs-ipam.md "allocate-cidrs-ipam.md").

The following example shows the hierarchy of the pool structure that you can create with
the instructions in this guide. At this step, you are creating a development IPAM
pool:

- IPAM operating in AWS Region 1 and AWS Region 2

      + Private scope




      	- Top-level pool (10.0.0.0/8)




      		* Regional pool in AWS Region 1 (10.0.0.0/16)




      			+ **Development pool for
      			 non-production VPCs
      			 (10.0.0.0/24)**




      				- Allocation for a VPC (10.0.1.0/25)

  In the preceding example, the CIDRs that are used are examples only. They illustrate that
  each pool within the top-level pool is provisioned with a portion of the top-level
  CIDR.

AWS Management Console

###### To create a development pool within a Regional pool

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. Choose **Create pool**.
4. Under **IPAM scope**, choose the
   same scope that you used when you created the top-level and Regional pools.
   For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
5. (Optional) Add a **Name tag** for the pool and a description for the pool.
6. Under **Source**, choose **IPAM pool**. Then choose the Regional
   pool.
7. Under **Resource planning**, leave **Plan IP
   space within the scope** selected. For more information
   about using this option to plan for subnet IP space within a VPC, see
   [Tutorial: Plan VPC IP address space for subnet IP allocations](tutorials-subnet-planning.md "tutorials-subnet-planning.md").
8. (Optional) Choose a CIDR to provision for the pool. You can only provision a CIDR
   that was provisioned to the top-level pool. You can create a pool
   without a CIDR, but you won’t be able to use the pool for allocations
   until you’ve provisioned a CIDR for it. You can add CIDRs to a pool at
   any time by editing the pool.
9. You have the same allocation rule options here as you did when you
   created the top-level and Regional pool. See [Create a top-level IPv4 pool](create-top-ipam.md "create-top-ipam.md") for an
   explanation of the options that are available when you create pools. The
   allocation rules for the pool are not inherited from the pool above it
   in the hierarchy. If you do not apply any rules here, no allocation
   rules will be set for the pool.
10. (Optional) Choose **Tags** for the pool.
11. When you’ve finished configuring your pool, choose **Create
    pool**.
12. See [Allocate CIDRs from an IPAM pool](allocate-cidrs-ipam.md "allocate-cidrs-ipam.md").

Command line
The commands in this section link to the _AWS CLI Command Reference_. The
documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to create a Regional pool in your IPAM:

1. Get the ID of the scope that you want to create the pool in: [describe-ipam-scopes](../../../cli/latest/reference/ec2/describe-ipam-scopes.md "../../../cli/latest/reference/ec2/describe-ipam-scopes.md")
2. Get the ID of the pool that you want to create the pool in: [describe-ipam-pools](../../../cli/latest/reference/ec2/describe-ipam-pools.md "../../../cli/latest/reference/ec2/describe-ipam-pools.md")
3. Create the pool: [create-ipam-pool](../../../cli/latest/reference/ec2/create-ipam-pool.md "../../../cli/latest/reference/ec2/create-ipam-pool.md")
4. View the new pool: [describe-ipam-pools](../../../cli/latest/reference/ec2/describe-ipam-pools.md "../../../cli/latest/reference/ec2/describe-ipam-pools.md")

Repeat these steps to create additional development pools within the Regional pool, as
needed.
