# Provision CIDRs to a pool

Follow the steps in this section to provision CIDRs to a pool. If you already provisioned
a CIDR when you created the pool, you might need to provision additional CIDRs if a pool is
nearing full allocation. To monitor pool usage, see [Monitor CIDR usage with the IPAM dashboard](monitor-cidr-usage-ipam.md "monitor-cidr-usage-ipam.md").

###### Note

The terms _provision_ and _allocate_ are used throughout this user guide and the IPAM console.
_Provision_ is used when you add a CIDR to an IPAM
pool. _Allocate_ is used when you associate a CIDR from
an IPAM pool with a VPC or Elastic IP address.

AWS Management Console

###### To provision CIDRs to a pool

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. By default, the default private scope is selected. If you don’t want to use the default
   private scope, from the dropdown menu at the top of the content pane, choose the scope you want to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
4. In the content pane, choose the pool that you want to add a CIDR
   to.
5. Choose **Actions** > **Provision
   CIDRs**.
6. Do one of the following:
   - If you are provisioning a CIDR to a pool in the public scope,
     enter the **Netmask**.
   - If you are provisioning a CIDR to an IPv4 pool in the private
     scope, enter the **CIDR**.
   - If you are provisioning a CIDR to an IPv6 pool in the private scope, note the
     following:
     - For important details about private IPv6 addressing,
       see [Private IPv6 addresses](../userguide/vpc-ip-addressing.md#vpc-ipv6-addresses-private "../userguide/vpc-ip-addressing.md#vpc-ipv6-addresses-private") in the
       _Amazon VPC User Guide_.
     - To use a private IPv6 ULA range, under **CIDRs
       to provision**, choose **Add ULA
       CIDR by netmask** and choose a netmask size
       or choose **Input private IPv6 CIDR**
       and enter a ULA range. Valid ranges for private IPv6 ULA
       are /9 to /60 starting with fd80::/9.
     - To use a private IPv6 GUA range, you have to have
       first enabled the option on your IPAM (see [Enable provisioning private IPv6 GUA CIDRs](enable-prov-ipv6-gua.md "enable-prov-ipv6-gua.md")). Once you have
       enabled private IPv6 GUA CIDRs, enter an IPv6 GUA in
       **Input private IPv6 CIDR**.

###### Note

    * By default, you can add one Amazon-provided IPv6 CIDR
     block to a Regional pool. For information on increasing the
     default limit, see [Quotas for your IPAM](quotas-ipam.md "quotas-ipam.md").
    * The CIDR you want to provision must be available in the scope.
    * If you are provisioning CIDRs to a pool within a pool, then the CIDR space you want to
     provision must be available in the pool.

7. Choose **Provision**.
8. You can view the CIDR in IPAM by choosing **Pools**
   in the navigation pane, choosing a pool, and viewing the CIDRs tab for
   the pool.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to provision CIDRs to a pool:

1. Get the ID of an IPAM pool: [describe-ipam-pools](../../../cli/latest/reference/ec2/describe-ipam-pools.md "../../../cli/latest/reference/ec2/describe-ipam-pools.md")
2. Get the CIDRs that are provisioned to the pool: [get-ipam-pool-cidrs](../../../cli/latest/reference/ec2/get-ipam-pool-cidrs.md "../../../cli/latest/reference/ec2/get-ipam-pool-cidrs.md")
3. Provision a new CIDR to the pool: [provision-ipam-pool-cidr](../../../cli/latest/reference/ec2/provision-ipam-pool-cidr.md "../../../cli/latest/reference/ec2/provision-ipam-pool-cidr.md")
4. Get the CIDRs that are provisioned to the pool and view the new CIDR:
   [get-ipam-pool-cidrs](../../../cli/latest/reference/ec2/get-ipam-pool-cidrs.md "../../../cli/latest/reference/ec2/get-ipam-pool-cidrs.md")
