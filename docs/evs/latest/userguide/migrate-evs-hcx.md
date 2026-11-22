

# Migrate workloads with HCX

After you deploy Amazon Elastic VMware Service, you can use VMware Hybrid Cloud Extension (HCX) to migrate workloads to your environment. You can use HCX over private connectivity or over the public internet. For how HCX works, see [Getting Started with VMware HCX](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10/getting-started-with-vmware-hcx-4-10.html) in the Broadcom documentation.

## Migration workflow
<a name="migrate-evs-hcx-workflow"></a>

To migrate workloads with HCX, complete these steps in order.

1. Choose private or internet connectivity before you create the environment. For more information, see [Plan HCX connectivity](plan-hcx-connectivity.md).

1. For internet connectivity, create the IPAM pool, Elastic IP addresses, and VPC CIDR block before you create the environment. After you create the environment, associate the Elastic IP addresses with the public HCX VLAN subnet. For instructions, see [Configure HCX public internet connectivity](evs-env-hcx-internet-access.md).

1. Install and activate HCX in the environment. For the requirements, see [Plan HCX connectivity](plan-hcx-connectivity.md).

1. Check the HCX VLAN subnet, network ACL, route table association, and uplink port group. For instructions, see [Prepare for HCX migration](hcx-prepare.md).

1. Turn on the optional HCX features that you need and verify HCX connectivity. For instructions, see [Optimize and verify HCX migration](hcx-optimize-verify.md).

## HCX connectivity options
<a name="migrate-evs-hcx-connectivity"></a>

For a comparison of private and internet connectivity and the two architectures, see [Plan HCX connectivity](plan-hcx-connectivity.md).

## HCX migration setup
<a name="hcx-migration-setup"></a>

For the checks before you migrate, see [Prepare for HCX migration](hcx-prepare.md). For WAN optimization, Mobility Optimized Networking, and connectivity checks, see [Optimize and verify HCX migration](hcx-optimize-verify.md).

**Topics**