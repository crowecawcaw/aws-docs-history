# Create a Regional IPv6 address pool in your IPAM

Follow the steps in this section to create an IPv6 regional IPAM pool. When you provision
an Amazon-provided IPv6 CIDR block to a pool, it must be provisioned to a pool with a locale
(AWS Region) selected. When you create the pool, you can provision a CIDR for the pool to
use or add it later. You then assign that space to an allocation. An allocation is a CIDR
assignment from an IPAM pool to another IPAM pool or to a resource.

The following example shows the hierarchy of the pool structure that you can create with
instructions in this guide. At this step, you are creating the IPv6 regional IPAM pool:

- IPAM operating in AWS Region 1 and AWS Region 2

      + Scope




      	- **Regional pool in AWS Region 1 (2001:db8::/52)**




      		* Development pool (2001:db8::/54)




      			+ Allocation for a VPC (2001:db8::/56)

  In the preceding example, the CIDRs that are used are examples only. They illustrate that
  each pool within the IPv6 regional pool is provisioned with a portion of the IPv6 regional
  CIDR.

When you create an IPAM pool, you can configure rules for the allocations that are made within the IPAM pool.

Allocation rules enable you to configure the following:

- The required netmask length for allocations within the pool
- The required tags for resources within the pool
- The required locale for resources within the pool. The locale is the AWS Region
  where an IPAM pool is available for allocations.
  Allocation rules determine whether resources are compliant or noncompliant. For additional
  information about compliance, see [Monitor CIDR usage by resource](monitor-cidr-compliance-ipam.md "monitor-cidr-compliance-ipam.md").

###### Note

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
an IPAM pool.

###### Note

- This topic covers how to create an IPv6 regional pool with an IPv6 address range provided by
  AWS or with a private IPv6 range. If you want to bring your own public IPv4 or
  IPv6 IP address ranges to AWS (BYOIP), there are prerequisites. For more
  information, see [Tutorial: Bring your IP addresses to IPAM](tutorials-byoip-ipam.md "tutorials-byoip-ipam.md").
- If you are creating an IPv6 pool in a private scope, you can use a private
  IPv6 GUA or ULA range. To use a private GUA range, you have to have first
  enabled the option on your IPAM (see [Enable provisioning private IPv6 GUA CIDRs](enable-prov-ipv6-gua.md "enable-prov-ipv6-gua.md")).

AWS Management Console

###### To create a pool

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. Choose **Create pool**.
4. Under **IPAM scope**, choose a private or public
   scope. If you want your private networks to support IPv6 and have no
   intention of routing traffic from these addresses to the internet,
   choose a private scope. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").

By default, when you create a pool, the default private scope is
selected. 5. (Optional) Add a **Name tag** for the pool and a description for the pool. 6. Under **Source**, choose **IPAM
scope**. 7. For **Address family**, select
**IPv6**. If you're creating this pool in the
public scope, all CIDRs in this pool will be publicly
advertisable. 8. Under **Resource planning**, leave **Plan IP
space within the scope** selected. For more information
about using this option to plan for subnet IP space within a VPC, see
[Tutorial: Plan VPC IP address space for subnet IP allocations](tutorials-subnet-planning.md "tutorials-subnet-planning.md"). 9. Choose the **Locale** for the pool. If you want to
provision an Amazon-provided IPv6 CIDR block to a pool, it must be
provisioned to a pool with a locale (AWS Region) selected. Choosing a
locale ensures there are no cross-region dependencies between your pool
and the resources allocating from it. The available options come from
the operating Regions that you chose for the IPAM when you created it.
You can add additional operating Regions at any time.

The locale is the AWS Region where you want this IPAM pool to be available for allocations. For example, you can only allocate a CIDR for a VPC from an IPAM pool that shares a locale with the VPC’s Region. Note that when you have chosen a locale for a pool, you cannot modify it. If the home Region of the IPAM is unavailable due to an outage and the pool has a locale different than the home Region of the IPAM, the pool can still be used to allocate IP addresses.

###### Note

If you are creating a pool in the Free Tier, you can only choose the locale that matches the
home Region of your IPAM. To use all IPAM features across locales,
[upgrade to the Advanced
Tier](mod-ipam-tier.md "mod-ipam-tier.md"). 10. (Optional) If you are creating an IPv6 pool in the public scope, under
**Service**, choose **EC2
(EIP/VPC)**. The service you select determines the AWS
service where the CIDR will be advertisable. Currently, the only option
is **EC2 (EIP/VPC)**, which means that the CIDRs
allocated from this pool will be advertisable for the Amazon EC2 service
(for Elastic IP addresses) and the Amazon VPC service (for CIDRs
associated with VPCs). 11. (Optional) If you are creating an IPv6 pool in the public scope, under
**Public IP source** option, choose
**Amazon owned** to have AWS provide an IPv6
address range for this pool. As noted at the top of this page, this
topic covers how to create an IPv6 regional pool with an IP address
range provided by AWS. If you want to bring your own IPv4 or IPv6
address range to AWS (BYOIP), there are prerequisites. For more
information, see [Tutorial: Bring your IP addresses to IPAM](tutorials-byoip-ipam.md "tutorials-byoip-ipam.md"). 12. (Optional) You can create a pool without a CIDR, but you won’t be able
to use the pool for allocations until you've provisioned a CIDR for it.
To provision a CIDR, do one of the following:

    * If you are creating an IPv6 pool in the public scope with **Public IP source Amazon-owned**, to
     provision a CIDR, under **CIDRs to provision**,
     choose **Add Amazon-owned CIDR** and choose the
     netmask size between /40 and /52 for the CIDR. When you choose a
     netmask length in the dropdown menu, you see the netmask length
     as well as the number of /56 CIDRs that the netmask represents.
     By default, you can add one Amazon-provided IPv6 CIDR block to
     the Regional pool. For information on increasing the default
     limit, see [Quotas for your IPAM](quotas-ipam.md "quotas-ipam.md").
    * If you are creating an IPv6 pool in a private scope, you can
     use a private IPv6 GUA or ULA range:




    	+ For important details about private IPv6 addressing,
    	 see [Private IPv6 addresses](../userguide/vpc-ip-addressing.md#vpc-ipv6-addresses-private "../userguide/vpc-ip-addressing.md#vpc-ipv6-addresses-private") in the
    	 *Amazon VPC User Guide*.
    	+ To use a private IPv6 ULA range, under **CIDRs
    	 to provision**, choose **Add ULA
    	 CIDR by netmask** and choose a netmask size
    	 or choose **Input private IPv6 CIDR**
    	 and enter a ULA range. Valid IPv6 ULA space is anything under fd00::/8 that does not overlap with the Amazon reserved range fd00::/16.
    	+ To use a private IPv6 GUA range, you have to have
    	 first enabled the option on your IPAM (see [Enable provisioning private IPv6 GUA CIDRs](enable-prov-ipv6-gua.md "enable-prov-ipv6-gua.md")). Once you've
    	 enabled private IPv6 GUA CIDRs, enter an IPv6 GUA in
    	 **Input private IPv6 CIDR**.

13. Choose optional allocation rules for this pool:
    - **Minimum netmask length**: The minimum netmask length required
      for CIDR allocations in this IPAM pool to be compliant and the
      largest size CIDR block that can be allocated from the pool. The
      minimum netmask length must be less than the maximum netmask
      length. Possible netmask lengths for IPv6 addresses are 0 - 128.
    - **Default netmask length**: A default netmask length for
      allocations added to this pool. For example, if the CIDR that's
      provisioned to this pool is `2001:db8::/52`
      and you enter 56 here, any new
      allocations in this pool will default to a netmask length of
      /56.
    - **Maximum netmask length**: The maximum netmask length that will
      be required for CIDR allocations in this pool. This value
      dictates the smallest size CIDR block that can be allocated from
      the pool. For example, if you enter /56 here, the smallest
      netmask length that can be allocated for CIDRs from this pool is
      /56.
    - **Tagging requirements**: The tags that are required for
      resources to allocate space from the pool. If the resources have their tags changed after they have allocated space or if the
      allocation tagging rules are changed on the pool, the resource may be marked as noncompliant.
    - **Locale**: The locale that will be required for
      resources that use CIDRs from this pool. Automatically imported resources
      that do not have this locale will be marked noncompliant. Resources that are not
      automatically imported into the pool will not be allowed to allocate space from
      the pool unless they are in this locale.

14. (Optional) Choose **Tags** for the pool.
15. Choose **Create pool**.
16. See [Create a development IPv6 address pool in your IPAM](create-ipv6-dev-pool.md "create-ipv6-dev-pool.md").

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to create or edit an IPv6 regional pool in your IPAM:

1. If you want to enable provisioning private IPv6 GUA CIDRs, modify the
   IPAM with [modify-ipam](../../../cli/latest/reference/ec2/modify-ipam.md "../../../cli/latest/reference/ec2/modify-ipam.md") and include the option to
   `enable-private-gua`. For more information, see [Enable provisioning private IPv6 GUA CIDRs](enable-prov-ipv6-gua.md "enable-prov-ipv6-gua.md").
2. Create a pool with [create-ipam-pool](../../../cli/latest/reference/ec2/create-ipam-pool.md "../../../cli/latest/reference/ec2/create-ipam-pool.md").
3. Provision a CIDR to the pool: [provision-ipam-pool-cidr](../../../cli/latest/reference/ec2/provision-ipam-pool-cidr.md "../../../cli/latest/reference/ec2/provision-ipam-pool-cidr.md").
4. Edit the pool after you create it to modify the allocation rules: [modify-ipam-pool](../../../cli/latest/reference/ec2/modify-ipam-pool.md "../../../cli/latest/reference/ec2/modify-ipam-pool.md").
