# Create a Regional IPv4 pool

Follow the steps in this section to create a Regional pool within your top-level pool. If
you need only a top-level pool, and don't need additional Regional and development pools,
skip to [Allocate CIDRs from an IPAM pool](allocate-cidrs-ipam.md "allocate-cidrs-ipam.md").

###### Note

The pool creation process is different for pools in public and private scopes. This section
includes steps for creating a regional pool in the private scope. For BYOIP and BYOASN
tutorials, see [Tutorials](tutorials-ipam.md "tutorials-ipam.md").

The following example shows the hierarchy of the pool structure that you create by
following the instructions in this guide. At this step, you are creating the Regional IPAM
pool:

- IPAM operating in AWS Region 1 and AWS Region 2

      + Private scope




      	- Top-level pool (10.0.0.0/8)




      		* **Regional pool in AWS Region 1
      		 (10.0.0.0/16)**




      			+ Development pool for non-production VPCs
      			 (10.0.0.0/24)




      				- Allocation for a VPC (10.0.0.0/25)

  In the preceding example, the CIDRs that are used are examples only. They illustrate that
  each pool within the top-level pool is provisioned with a portion of the top-level
  CIDR.

AWS Management Console

###### To create a Regional pool within a top-level pool

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. Choose **Create pool**.
4. Under **IPAM scope**, choose the
   same scope that you used when you created the top-level pool. For more
   information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
5. (Optional) Add a **Name tag** for the pool and a description for the pool.
6. Under **Source**, choose **IPAM
   pool**. Then choose the top-level pool that you created in
   the previous section.
7. If you are creating this pool in the public scope, you'll see an
   option for **Address family**. Choose
   **IPv4**.
8. Under **Resource planning**, leave **Plan IP
   space within the scope** selected. For more information
   about using this option to plan for subnet IP space within a VPC, see
   [Tutorial: Plan VPC IP address space for subnet IP allocations](tutorials-subnet-planning.md "tutorials-subnet-planning.md").
9. Choose the locale for the pool. Choosing a locale ensures there are no cross-region dependencies between your pool and the resources allocating from it. The available options come from the
   operating Regions that you chose when you created your IPAM.

The locale is the AWS Region where you want this IPAM pool to be available for allocations. For example, you can only allocate a CIDR for a VPC from an IPAM pool that shares a locale with the VPC’s Region. Note that when you have chosen a locale for a pool, you cannot modify it. If the home Region of the IPAM is unavailable due to an outage and the pool has a locale different than the home Region of the IPAM, the pool can still be used to allocate IP addresses.

###### Note

If you are creating a pool in the Free Tier, you can only choose the locale that matches the
home Region of your IPAM. To use all IPAM features across locales,
[upgrade to the Advanced
Tier](mod-ipam-tier.md "mod-ipam-tier.md"). 10. If you are creating this pool in the public scope, you'll see an
option for **Service**. Choose **EC2
(EIP/VPC)**. The service you select determines the AWS
service where the CIDR will be advertisable. Currently, the only option
is **EC2 (EIP/VPC)**, which means that the CIDRs
allocated from this pool will be advertisable for the Amazon EC2 service
(for Elastic IP addresses) and the Amazon VPC service (for CIDRs
associated with VPCs). 11. (Optional) Choose a CIDR to provision for the pool. You can create a pool without a CIDR, but you won’t be able to use the pool
for allocations until you’ve provisioned a CIDR for it. You can add CIDRs to a pool at any time by editing the pool. 12. You have the same allocation rule options here as you did when you
created the top-level pool. See [Create a top-level IPv4 pool](create-top-ipam.md "create-top-ipam.md") for an explanation of the options
that are available when you create pools. The allocation rules for the
Regional pool are not inherited from the top-level pool. If you do not
apply any rules here, there will be no allocation rules set for the
pool. 13. (Optional) Choose **Tags** for the pool. 14. When you’ve finished configuring your pool, choose **Create
pool**. 15. See [Create a development IPv4 pool](create-dev-ipam.md "create-dev-ipam.md").

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to create a Regional pool in your
IPAM:

1. Get the ID of the scope that you want to create the pool in: [describe-ipam-scopes](../../../cli/latest/reference/ec2/describe-ipam-scopes.md "../../../cli/latest/reference/ec2/describe-ipam-scopes.md")
2. Get the ID of the pool that you want to create the pool in: [describe-ipam-pools](../../../cli/latest/reference/ec2/describe-ipam-pools.md "../../../cli/latest/reference/ec2/describe-ipam-pools.md")
3. Create the pool: [create-ipam-pool](../../../cli/latest/reference/ec2/create-ipam-pool.md "../../../cli/latest/reference/ec2/create-ipam-pool.md")
4. View the new pool: [describe-ipam-pools](../../../cli/latest/reference/ec2/describe-ipam-pools.md "../../../cli/latest/reference/ec2/describe-ipam-pools.md")

Repeat these steps to create additional pools within the top-level pool, as needed.
