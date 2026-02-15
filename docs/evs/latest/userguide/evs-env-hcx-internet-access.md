# Configure HCX public internet connectivity

You can configure public internet access for your HCX public VLAN by associating Elastic IP addresses with your VLAN.
This enables direct internet connectivity for VMware HCX appliances and workloads that require internet access for migration operations.

## Related topics

This topic covers managing internet access for HCX public VLAN. For complete implementation:

1. Complete prerequisites in [Setting up Amazon Elastic VMware Service](setting-up.md "setting-up.md").
2. Configure initial setup in [Getting started with Amazon Elastic VMware Service](getting-started.md "getting-started.md").
3. Configure internet access (this topic).

## About HCX VLAN internet access

You can configure internet access for VMware HCX appliances, allowing you to perform HCX migration of your workloads to Amazon EVS over the internet.

This approach:

- Enables virtual machine migrations without requiring dedicated private connectivity.
- Provides a flexible, cost-effective solution for migration.

###### Important

HCX internet-based migration is generally not recommended for:

- Applications sensitive to network jitter or latency.
- Time-critical vMotion operations.
- Large-scale migrations with strict performance requirements.
  For these scenarios, we recommend using HCX private connectivity.
  A private dedicated connection offers more reliable performance compared to internet-based connections.

## Internet connectivity overview

Review the following considerations.

### HCX networking requirements and DNAT

HCX has specific networking constraints that affect how you set up public internet access.

HCX does not support Destination Network Address Translation (DNAT).
Instead, HCX requires the uplink network to be routable with a default gateway IP address.

Amazon EVS VLAN subnets include a default gateway IP address like other VPC subnets.
However, these subnets are always private subnets, even when you use CIDR blocks outside the RFC1918 address range.

#### Enabling HCX internet connectivity

To enable internet connectivity without DNAT, Amazon EVS uses a specific CIDR configuration approach:

- **Internet routable CIDR requirement**: Amazon EVS requires an internet routable CIDR that matches your HCX VLAN subnet CIDR.
- **IPAM allocation**: Amazon EVS uses a public IPAM-allocated CIDR with a minimum netmask length of /28 as the internet routable CIDR.
- **VPC configuration**: You must manually add the public IPAM-allocated CIDR to your VPC as a secondary VPC CIDR.
- **VLAN subnet deployment**: After IPAM and VPC are configured, you can use the public IPAM-allocated CIDR in the HCX VLAN subnet during Amazon EVS deployment.
- **Elastic IP configuration**: Amazon EVS requires the following configuration:
  - **Allocate Elastic IPs**: You allocate Elastic IPs from the IPAM allocated CIDR.
    You must allocate at least two Elastic IP addresses (EIPs) from the IPAM pool for the HCX Manager and HCX Interconnect (HCX-IX) appliances.
    Allocate an additional Elastic IP address for each HCX network appliance that you need to deploy.
  - **Associate with VLAN**: You associate each Elastic IP that you want to use with an HCX appliance to the HCX VLAN subnet. Use the Amazon EVS console or AWS CLI for this association.
  - **Configure gateway address**: The first usable address from the CIDR becomes the gateway address that you configure in your HCX appliance.
  - **Traffic routing**: Traffic for each associated Elastic IP routes directly to the destination HCX appliance with the same IP address, without DNAT.

For steps to configure HCX with internet connectivity for Amazon EVS environment deployment, see [Setting up Amazon Elastic VMware Service](setting-up.md "setting-up.md") and [Getting started with Amazon Elastic VMware Service](getting-started.md "getting-started.md").

### Operation considerations

- The HCX public VLAN CIDR block must have a /28 netmask length.
- EIPs can be associated with or disassociated from the HCX public VLAN after deployment using the Amazon EVS console or AWS CLI, but they must be from the same IPAM pool.
- Each EIP association has its own unique association ID.
- You can have up to 13 EIPs from a public IPAM pool associated with the /28 HCX public VLAN.
  You cannot associate the first two EIPs or the last EIP from the public IPAM-allocated CIDR block with the HCX public VLAN subnet.
  These EIPs are reserved as network, default gateway, and broadcast addresses.
  Amazon EVS throws a validation error if you attempt to associate these EIPs with the VLAN.

### Security considerations

- Network access control lists (ACLs) still apply to traffic flowing through the HCX public VLAN subnet.
- Security group rules do not apply to traffic on HCX public VLAN subnets. Use network ACLs for traffic control.

###### Important

If you are connecting over the internet, associating an Elastic IP address with a VLAN provides direct internet access to all resources on that VLAN.
Ensure that you have appropriate network access control lists configured to restrict access as needed for your security requirements.

## Managing Elastic IP addresses for VLANs

You can associate and disassociate Elastic IP addresses with an HCX public VLAN using the Amazon EVS console or AWS CLI.

###### Note

Amazon EVS only supports associating and disassociating Elastic IP address with an HCX public VLAN at this time.

### Associate an Elastic IP address with a VLAN

#### Prerequisites

Ensure that you have the following:

- Elastic IP address is allocated from the Amazon-owned public IPAM pool.
- Amazon EVS environment is already created.

###### Example

Amazon EVS console

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs "https://console.aws.amazon.com/evs").
2. On the navigation menu, choose **Environments**.
3. Select the environment.
4. Under the **Networks and connectivity** tab, select the HCX public VLAN.

###### Note

Amazon EVS only supports associating EIPs with the HCX VLAN at this time. 5. Choose **Associate EIP to VLAN**. 6. Select the Elastic IP address(es) to associate with the HCX public VLAN. 7. Choose **Associate EIPs**. You can have up 13 EIPs associated with the HCX public VLAN.

###### Note

You cannot associate the first two EIPs from the public IPAM CIDR block to the VLAN subnet.
These EIPs are reserved as network and default gateway addresses. 8. Check the **EIP associations** to confirm that the EIPs have been associated with the HCX public VLAN.

AWS CLI

1. To associate an Elastic IP address with a VLAN, use the example `associate-eip-to-vlan` command.
   - `environment-id` - The ID of your Amazon EVS environment.
   - `vlan-name` - Must be `hcx`. Amazon EVS only supports EIP association with the HCX VLAN at this time.
   - `allocation-id` - The allocation ID of the Elastic IP address.

   ```
   aws evs associate-eip-to-vlan \
     --environment-id "env-605uove256" \
     --vlan-name "hcx" \
     --allocation-id "eipalloc-0429268f30c4a34f7"
   ```

   The command returns details about the VLAN, including the new EIP association:

   ```
   {
       "vlan": {
           "vlanId": 80,
           "cidr": "18.97.137.0/28",
           "availabilityZone": "us-east-2c",
           "functionName": "hcx",
           "subnetId": "subnet-02f9a4ee9e1208cfc",
           "createdAt": "2025-08-22T23:42:16.200000+00:00",
           "modifiedAt": "2025-08-23T13:42:28.155000+00:00",
           "vlanState": "CREATED",
           "stateDetails": "VLAN successfully created",
           "eipAssociations": [
               {
                   "associationId": "eipassoc-09e966faad7ecc58a",
                   "allocationId": "eipalloc-0429268f30c4a34f7",
                   "ipAddress": "18.97.137.2"
               }
           ],
           "isPublic": true,
           "networkAclId": "acl-02fa8ab4ad3ddfb00"
       }
   }
   ```

   The `eipAssociations` array shows the new association, including:
   - `associationId` - The unique ID for this EIP association, used for disassociation.
   - `allocationId` - The allocation ID of the associated Elastic IP address.
   - `ipAddress` - The IP address assigned to the VLAN.

2. Repeat the step to associate additional EIPs.
   You can have up 13 EIPs associated with the HCX public VLAN.

### Disassociate an Elastic IP address from a VLAN

#### Prerequisites

Ensure that you have the following:

- Amazon EVS environment is already created.
- EIP is associated with the Amazon EVS environment.

###### Example

Amazon EVS console

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs "https://console.aws.amazon.com/evs").
2. On the navigation menu, choose **Environments**.
3. Select the environment.
4. Under the **Networks and connectivity** tab, select the HCX public VLAN.
5. Choose **Disassociate EIP from VLAN**.
6. Select the Elastic IP address(es) to disassociate from the HCX public VLAN.

###### Important

Disassociating EIPs may cause a loss of internet connectivity for appliances that use public VLAN subnets. 7. Choose **Disassociate EIPs**. 8. Check the **EIP associations** to confirm that the EIPs have been disassociated from the HCX public VLAN.

AWS CLI

To disassociate an Elastic IP address from a VLAN, use the example `disassociate-eip-from-vlan` command.

- `environment-id` - The ID of your Amazon EVS environment.
- `vlan-name` - Must be `hcx`. Amazon EVS only supports EIP association with the HCX VLAN at this time.
- `association-id` - The association ID of the EIP association to remove.

###### Important

Disassociating EIPs may cause a loss of internet connectivity for appliances that use public VLAN subnets.

```
aws evs disassociate-eip-from-vlan \
  --environment-id "env-605uove256" \
  --vlan-name "hcx" \
  --association-id "eipassoc-09e966faad7ecc58a"
```

The command returns details about the VLAN with the EIP association removed:

```
{
    "vlan": {
        "vlanId": 80,
        "cidr": "18.97.137.0/28",
        "availabilityZone": "us-east-2c",
        "functionName": "hcx",
        "subnetId": "subnet-02f9a4ee9e1208cfc",
        "createdAt": "2025-08-22T23:42:16.200000+00:00",
        "modifiedAt": "2025-08-23T13:48:49.846000+00:00",
        "vlanState": "CREATED",
        "stateDetails": "VLAN successfully created",
        "eipAssociations": [],
        "isPublic": true,
        "networkAclId": "acl-02fa8ab4ad3ddfb00"
    }
}
```

The empty `eipAssociations` array confirms that the Elastic IP address has been successfully disassociated from the VLAN.

## About HCX WAN Optimization for internet-based migrations

###### Note

The WAN optimization feature is no longer available in HCX 4.11.3.
For more information, see the [HCX 4.11.3 Release Notes](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/hcx-4-11-release-notes/vmware-hcx-4113-release-notes.html "https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/hcx-4-11-release-notes/vmware-hcx-4113-release-notes.html").

When performing migrations over the internet, HCX WAN Optimization (HCX-WO) can improve migration performance.
The service works in conjunction with the HCX Interconnect appliance (HCX-IX) to:

- Apply data reduction techniques to minimize bandwidth usage.
- Implement WAN path conditioning to optimize network performance.
- Improve migration speeds over high-latency internet connections.
- Enhance the reliability of internet-based migrations.

HCX WAN Optimization is particularly useful for internet-based migrations where:

- Network latency may be higher than private connectivity options.
- Available bandwidth may be limited or variable.
- Network conditions may fluctuate due to internet traffic patterns.

For detailed instructions on setting up HCX WAN Optimization after configuring internet connectivity, see [(Optional) Set up HCX WAN Optimization](migrate-evs-hcx.md#hcx-wan-optimization "migrate-evs-hcx.md#hcx-wan-optimization").

###### Note

While WAN Optimization can significantly improve internet-based migration performance, it may not provide additional benefits in environments with dedicated 10Gbit, low-latency connections.
Consider your network characteristics when deciding whether to enable this feature.
