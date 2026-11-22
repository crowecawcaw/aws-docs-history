

# TELCOOPS04-BP01 Manage User Equipment (UE) IP address pools using cloud-based IPAM integrated with 5G core network functions

 In a 5G network, the Session Management Function (SMF) allocates user equipment (UE) IP addresses during session establishment, not the cloud provider's networking layer. The cloud infrastructure routes traffic to and from those addresses without interfering with the pools the SMF owns. Confusing the two addressing domains causes routing conflicts and standards violations. 

 **Desired outcome:** 
+  UE IP address pools are managed by the SMF as defined in 3GPP specifications, with the cloud infrastructure configured to route traffic to these pools without interference. 
+  VPC CIDR ranges and UE IP pools don't overlap, and routing tables correctly direct UPF-bound traffic. 
+  Monitoring of UE IP pool usage feeds into capacity planning without requiring changes to the SMF's native pool management. 

 **Common anti-patterns:** 
+  Attempting to manage UE IP allocation through cloud IPAM or Bring Your Own IP (BYOIP) instead of letting the SMF handle it per 3GPP standards. 
+  Configuring VPC CIDRs that overlap with UE IP pools, causing routing conflicts when traffic traverses the N6 interface. 
+  Not accounting for UE IP pool growth when sizing VPC route table entries and subnet capacity. 
+  Treating UE pool addresses as cloud-managed addresses, which leads to changes being made in the wrong system. 

 **Benefits of establishing this best practice:** 
+  Ownership of each address domain is unambiguous, so changes are made in the system that owns them. 
+  Standards-compliant pool management keeps the deployment interoperable with 3GPP-conformant network functions. 
+  Non-overlapping ranges and correct routing prevent subscriber traffic from being misrouted at the user-plane boundary. 
+  Pool-usage monitoring feeds capacity planning without disturbing the SMF's native allocation. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Keep the UE IP pool and the cloud infrastructure address space as two separate addressing domains. During PDU session establishment, the SMF allocates addresses to user equipment from pools the operator configures. These pools stay within the mobile core. The VPC that hosts the network functions has its own addressing for Elastic Network Interfaces (ENIs), subnets, and services. If you plan the two domains independently, overlapping ranges produce routing conflicts that appear only when subscriber traffic traverses the N6 interface toward external networks. Do not use AWS BYOIP to bring UE ranges into the VPC. BYOIP advertises public IP prefixes through AWS edge locations. UE pools are private addressing managed within the mobile core, not a BYOIP use case. Forcing UE pools into cloud IPAM or BYOIP violates the 3GPP model and creates two systems allocating the same addresses. The cloud infrastructure never allocates UE addresses. It routes UE-destined traffic to the correct User Plane Function (UPF) and carries return traffic from UEs to external networks. Connect the two domains with static routes pointing UE IP prefixes to the UPF's N6 or SGi interface, or BGP peering through a transit gateway. Design those routes as summary routes, such as a /16 covering many /24 pools. The SMF can then expand pools without forcing a VPC route-table change on every expansion. 

### Implementation steps
<a name="implementation-steps"></a>
+  Document all UE IP pools configured in the SMF, their sizes, and growth projections. Confirm these ranges don't overlap with any VPC CIDR in the deployment, and record that the SMF is the system of record for them. 
+  Configure VPC routing for UE IP traffic by adding static routes or BGP-learned routes in the VPC and AWS Transit Gateway route tables that direct UE-destined traffic toward the UPF's data-plane interface (N6/SGi). 
+  Plan for pool expansion with summary routes, such as a /16 covering multiple /24 pools, so the SMF can expand pools without requiring VPC route-table updates. 
+  Monitor pool usage for capacity planning by configuring the SMF to export pool-usage metrics (allocated compared to available) to Amazon CloudWatch, with alerts at 80% usage to trigger a capacity review. 

## Resources
<a name="resources"></a>

 **Key AWS services:** 
+  [Amazon VPC](https://aws.amazon.com/vpc/) 
+  [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 