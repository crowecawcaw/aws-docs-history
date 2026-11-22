

# Optimize and verify HCX migration

After you prepare your Amazon Elastic VMware Service environment, you can turn on optional VMware Hybrid Cloud Extension (HCX) features that improve migration traffic, and then verify HCX connectivity. You do these steps in HCX and NSX, using the Broadcom documentation for each feature.

## Before you begin
<a name="hcx-optimize-verify-prereqs"></a>
+ You have completed the checks and created the HCX uplink port group. For instructions, see [Prepare for HCX migration](hcx-prepare.md).

## (Optional) Set up HCX WAN Optimization
<a name="hcx-wan-optimization"></a>

If your HCX version includes the HCX WAN Optimization service (HCX-WO), you can use it to improve migration performance over private lines or the internet. HCX-WO applies WAN optimization techniques such as data reduction and WAN path conditioning. It is deployed with the HCX Interconnect (HCX-IX) appliance, which replicates data between your on-premises environment and the Amazon EVS environment.

HCX-WO helps most on deployments that can’t dedicate 10 Gbit paths to migrations. On 10 Gbit, low-latency deployments, it might not improve migration performance.

To use HCX-WO with Amazon EVS, use a distributed port group on the HCX VLAN subnet. Use the port group that you created in [Step 5. Create a distributed port group with the HCX uplink VLAN ID](hcx-prepare.md#hcx-create-port-group).

## (Optional) Turn on HCX Mobility Optimized Networking
<a name="hcx-mon"></a>

HCX Mobility Optimized Networking (MON) is a feature of the HCX Network Extension service. MON-enabled network extensions route traffic for migrated VMs within your Amazon EVS environment, instead of on a long round-trip path through the source gateway. This applies when you stretch Layer 2 networks. MON is available for all Amazon EVS deployments.

Before you turn on HCX MON, do the following:
+ Read the restrictions in [Restrictions and Limitations for Network Extension](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10/vmware-hcx-user-guide-4-10/extending-networks-with-vmware-hcx/about-vmware-hcx-network-extension/restrictions-and-limitations-for-network-extension.html) and [Restrictions and Limitations for Mobility Optimized Networking Topologies](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10/vmware-hcx-user-guide-4-10/extending-networks-with-vmware-hcx/hcx-network-extension-with-mobility-optimized-networking/limitations-for-mobility-optimized-networking.html) in the Broadcom documentation.
+ In NSX, configure route redistribution for the destination network CIDR. For more information, see [Configure BGP and Route Redistribution](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/nsxt-dc/3-2/administration-guide/nsx-cloud-overview/nsx-t-supported-features-for-nsx-cloud/service-insertion-for-your-public-cloud/task-set-up-bgp-on-the-vpn-tunnel.html) in the Broadcom documentation.

In HCX, turn on MON for the network extension by following [Configuring Mobility Optimized Networking](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10/vmware-hcx-user-guide-4-10/extending-networks-with-vmware-hcx/hcx-network-extension-with-mobility-optimized-networking/configuring-hcx-mobility-optimized-networking.html) in the Broadcom documentation.

## Verify HCX connectivity
<a name="hcx-step-10"></a>

VMware HCX includes diagnostic tools that test connectivity. To run them, follow [VMware HCX Troubleshooting](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10/vmware-hcx-user-guide-4-10/vmware-hcx-troubleshooting.html) in the Broadcom documentation.

If the checks fail, review the HCX VLAN subnet, network ACL, and route table checks in [Prepare for HCX migration](hcx-prepare.md). For internet connectivity, also check the Elastic IP address associations in [Configure HCX public internet connectivity](evs-env-hcx-internet-access.md). For other network issues, see [Troubleshoot networking](troubleshoot-networking.md).

You have verified HCX connectivity, and you can start migrating workloads.