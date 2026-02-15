# Create a top-level IPv4 pool

Follow the steps in this section to create an IPv4 top-level IPAM pool. When you create
the pool, you provision a CIDR for the pool to use. You then assign that space to an
allocation. An allocation is a CIDR assignment from an IPAM pool to another IPAM pool or to
a resource.

The following example shows the hierarchy of the pool structure that you can create with
instructions in this guide. At this step, you are creating the top-level IPAM pool:

- IPAM operating in AWS Region 1 and AWS Region 2

      + Private scope




      	- **Top-level pool
      	 (10.0.0.0/8)**




      		* Regional pool in AWS Region 1 (10.0.0.0/16)




      			+ Development pool for non-production VPCs
      			 (10.0.0.0/24)




      				- Allocation for a VPC (10.0.0.0/25)

  In the preceding example, the CIDRs that are used are examples only. They illustrate that
  each pool within the top-level pool is provisioned with a portion of the top-level
  CIDR.

When you create an IPAM pool, you can configure rules for the allocations that are made within the IPAM pool.

Allocation rules enable you to configure the following:

- Whether IPAM should automatically import CIDRs into the IPAM pool if it finds them within this
  pool's CIDR range
- The required netmask length for allocations within the pool
- The required tags for resources within the pool
- The required locale for resources within the pool. The locale is the AWS Region
  where an IPAM pool is available for allocations.
  Allocation rules determine whether resources are compliant or noncompliant. For additional
  information about compliance, see [Monitor CIDR usage by resource](monitor-cidr-compliance-ipam.md "monitor-cidr-compliance-ipam.md").

###### Important

There is an additional implicit rule that is not displayed in the allocation rules. If the
resource is in an IPAM pool that is a shared resource in AWS Resource Access Manager
(RAM), the resource owner must be configured as a principal in AWS RAM. For more
information about sharing pools with RAM, see [Share an IPAM pool using AWS RAM](share-pool-ipam.md "share-pool-ipam.md").

The following example shows how you might use allocation rules to control access to an
IPAM pool:

###### Example

When you create your pools based on routing and security needs, you might want to allow only
certain resources to use a pool. In such cases, you can set an allocation rule stating
that any resource that wants a CIDR from this pool must have a tag that matches the
allocation rule tag requirements. For example, you could set an allocation rule stating
that only VPCs with the tag _prod_ can get CIDRs from
an IPAM pool. You could also set a rule stating that CIDRs allocated from this pool can
be no larger than /24. In this case, creating a resource using a CIDR larger than /24
from this pool violates an allocation rule on the pool and creation fails. Existing
resources with a CIDR larger than /24 are flagged as noncompliant.

###### Important

This topic covers how to create a top-level IPv4 pool with an IP address range provided by
AWS. If you want to bring your own IPv4 address range to AWS (BYOIP), there are
prerequisites. For more information, see [Tutorial: Bring your IP addresses to IPAM](tutorials-byoip-ipam.md "tutorials-byoip-ipam.md").

AWS Management Console

###### To create a pool

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. Choose **Create pool**.
4. Under **IPAM scope**, choose the private scope you
   want to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").

By default, when you create a pool, the default private scope is
selected. Pools in the private scope must be IPv4 pools. Pools in the public scope can be IPv4 or IPv6 pools.
The public scope is intended for all
public space. 5. (Optional) Add a **Name tag** for the pool and a description for the pool. 6. Under **Source**, choose **IPAM
scope**. 7. Under **Address family**, choose
**IPv4**. 8. Under **Resource planning**, leave **Plan IP
space within the scope** selected. For more information
about using this option to plan for subnet IP space within a VPC, see
[Tutorial: Plan VPC IP address space for subnet IP allocations](tutorials-subnet-planning.md "tutorials-subnet-planning.md"). 9. For the **Locale**, choose **None**.
You will set the locale on the Regional pool.

The locale is the AWS Region where you want this IPAM pool to be available for allocations. For example, you can only allocate a CIDR for a VPC from an IPAM pool that shares a locale with the VPC’s Region. Note that when you have chosen a locale for a pool, you cannot modify it. If the home Region of the IPAM is unavailable due to an outage and the pool has a locale different than the home Region of the IPAM, the pool can still be used to allocate IP addresses. 10. (Optional) You can create a pool without a CIDR, but you won’t be able
to use the pool for allocations until you’ve provisioned a CIDR for it.
To provision a CIDR, choose **Add new CIDR**. Enter an
IPv4 CIDR to provision for the pool. If you want to bring your own IPv4
or IPv6 IP address range to AWS there are prerequisites. For more
information, see [Tutorial: Bring your IP addresses to IPAM](tutorials-byoip-ipam.md "tutorials-byoip-ipam.md"). 11. Choose optional allocation rules for this pool:

    * **Automatically import discovered resources**: This option is not available if the **Locale** is set to **None**. If selected, IPAM will continuously look for resources within the CIDR range of this pool
     and automatically import them as allocations into your IPAM. Note the following:




    	+ The CIDRs that will be allocated for
    	 these resources must not already be allocated to other resources in order for the import to succeed.
    	+ IPAM will import
    	 a CIDR regardless of its compliance with the pool's allocation rules, so a resource might be imported and subsequently
    	 marked as noncompliant.
    	+ If IPAM discovers multiple CIDRs that overlap, IPAM will import the largest CIDR only.
    	+ If IPAM discovers multiple CIDRs with matching CIDRs, IPAM will randomly import one of them only.
    ###### Warning



    	+ After you create an IPAM, when you create a VPC,
    	 choose the IPAM-allocated CIDR block option. If you
    	 do not, the CIDR you choose for your VPC may overlap with an IPAM CIDR allocation.
    	+ If you have a VPC already
    	 allocated in an IPAM pool, a VPC with an overlapping CIDR cannot be automatically imported. For
    	 example, if you have a VPC with a 10.0.0.0/26 CIDR allocated
    	 in an IPAM pool, a VPC with a 10.0.0.0/23 CIDR (that would
    	 cover the 10.0.0.0/26 CIDR) cannot be
    	 imported.
    	+ It takes some time for existing VPC CIDR allocations to be auto-imported into IPAM.
    * **Minimum netmask length**: The minimum netmask length required for
     CIDR allocations in this IPAM pool to be compliant and the largest size CIDR block that can be allocated from the pool. The minimum netmask length must be less than the maximum
     netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses
     are 0 - 128.
    * **Default netmask length**: A default netmask length for
     allocations added to this pool. For example, if the CIDR that's
     provisioned to this pool is `10.0.0.0/8`
     and you enter `16` here, any new
     allocations in this pool will default to a netmask length of
     /16.
    * **Maximum netmask length**: The maximum netmask length that will
     be required for CIDR allocations in this pool. This value
     dictates the smallest size CIDR block that can be allocated from
     the pool.
    * **Tagging requirements**: The tags that are required for
     resources to allocate space from the pool. If the resources have their tags changed after they have allocated space or if the
     allocation tagging rules are changed on the pool, the resource may be marked as noncompliant.
    * **Locale**: The locale that will be required for
     resources that use CIDRs from this pool. Automatically imported resources
     that do not have this locale will be marked noncompliant. Resources that are not
     automatically imported into the pool will not be allowed to allocate space from
     the pool unless they are in this locale.

###### Note

Allocation rules apply only to the [managed resources](monitor-cidr-compliance-ipam.md "monitor-cidr-compliance-ipam.md") within that pool. The rules do not apply to resources in pools within a pool. 12. (Optional) Choose **Tags** for the pool. 13. Choose **Create pool**. 14. See [Create a Regional IPv4 pool](create-reg-ipam.md "create-reg-ipam.md").

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to create or edit a top-level pool in your IPAM:

1. Create a pool: [create-ipam-pool](../../../cli/latest/reference/ec2/create-ipam-pool.md "../../../cli/latest/reference/ec2/create-ipam-pool.md").
2. Edit the pool after you create it to modify the allocation rules: [modify-ipam-pool](../../../cli/latest/reference/ec2/modify-ipam-pool.md "../../../cli/latest/reference/ec2/modify-ipam-pool.md").
