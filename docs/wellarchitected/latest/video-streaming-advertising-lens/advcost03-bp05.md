

# ADVCOST03-BP05 Replace per-gigabyte egress with transaction-priced partner connectivity
<a name="advcost03-bp05"></a>

 NAT Gateways charge per GB of data processed plus an hourly fee, and that cost compounds at RTB scale. RTB Fabric prices by transaction instead, which matches how RTB revenue works and can cut networking costs by up to 80% compared to NAT Gateway-based architectures. Workloads that keep most of their traffic inside the fabric can save at the top of that range or beyond, depending on traffic mix and average bid payload size. 

 **Desired outcome:** 
+  RTB partner traffic flows through transaction-based connectivity that removes per-GB charges. 
+  NAT Gateways dedicated to RTB traffic are decommissioned, removing their hourly fees. 
+  Infrastructure as code is updated to guard against recreation of NAT Gateways for RTB traffic. 

 **Common anti-patterns:** 
+  Routing all RTB partner traffic through NAT Gateways by default, so per-GB data processing charges accrue on millions of lightweight bid requests where aggregate byte volume, not per-transaction business value, drives cost. 
+  Assuming private connectivity options (such as AWS PrivateLink or Direct Connect) are the only alternatives to NAT Gateways without evaluating transaction-based pricing models purpose-built for high-QPS, low-payload RTB traffic patterns. 
+  Optimizing bid payload size to reduce NAT Gateway costs rather than addressing the underlying pricing model mismatch. 
+  Maintaining dedicated NAT Gateways for RTB traffic after migrating to transaction-based connectivity, which continues to charge hourly fees for unused gateways. 
+  Migrating to transaction-based connectivity without first comparing against existing private pricing agreements (EDP, PPA), so scenarios where negotiated discounts already reduce the per-GB cost below the transaction-based alternative get missed. 

 **Benefits of establishing this best practice:** 
+  Up to 80% reduction in networking costs for RTB partner traffic, higher for predominantly inside-fabric traffic mixes. 
+  Predictable per-transaction pricing aligned with RTB business metrics. 
+  Elimination of hourly NAT Gateway fees dedicated to RTB traffic. 
+  Simplified cost modeling tied to QPS rather than bid payload volume. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 NAT Gateways charge both an hourly fee per gateway and a per-GB data processing fee on all traffic that traverses them. RTB workloads send millions of small requests (typically 1 to 4 KiB each), so the aggregate byte volume grows linearly with QPS even though individual payloads carry little data. [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) charges per billion transactions instead, which removes the per-GB component and ties cost to the number of transactions. 

 Before migrating, compare your effective NAT Gateway rate against the RTB Fabric per-transaction rate. Organizations with Enterprise Discount Programs (EDPs) or Private Pricing Addendums (PPAs) might already receive discounts on data processing charges. If your negotiated per-GB rate, multiplied by average bid payload size and monthly transaction count, produces a lower figure than RTB Fabric's per-billion-transaction price, the migration saves nothing. Run this comparison at current volume and at projected growth. 

 Each partner link carries live auction traffic, and misrouting during cutover can drop bid requests or increase latency beyond the exchange's timeout window (typically 100 to 150 ms). Migrate one partner at a time. If routing fails for one partner, only that partner's traffic is affected while others stay on the existing path. VPC Flow Logs confirm that traffic has shifted. [CloudWatch](https://aws.amazon.com/cloudwatch/) metrics on the new RTB Fabric link show that traffic is arriving, but only Flow Logs show that it has stopped traversing the old NAT Gateway. 

 RTB Fabric gateways operate within specific Availability Zones. Placing them in different Availability Zones from your bidder fleet adds cross-AZ data transfer charges and 1 to 2 ms of network latency. Put gateways in the same Availability Zones as your compute instances to avoid both. If you run bidders across multiple Availability Zones, you need a gateway in each Availability Zone that hosts compute. 

 Infrastructure as code templates that provisioned NAT Gateways for RTB traffic recreate them on the next deployment. The hourly fees resume as soon as a gateway is created, whether or not traffic flows through it. Handle the IaC cleanup as part of the migration rather than a follow-up task, so the cost does not regress. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Analyze VPC Flow Logs to quantify NAT Gateway RTB costs:** Identify all outbound RTB partner traffic from VPC Flow Logs filtered by partner IP ranges. Calculate current monthly per-GB processing charges and hourly gateway fees for RTB-specific traffic. 

1.  **Provision RTB Fabric gateways colocated with your VPC:** Create RTB Fabric requester or responder gateways (or both) in the same Availability Zones as your bidder infrastructure. Select the appropriate role (requester for sending bid requests, responder for receiving them). 

1.  **Migrate partner traffic to RTB Fabric links one at a time:** For each partner, create an RTB Fabric link and update routing to use the fabric endpoint. Validate traffic flow using CloudWatch RTB Fabric metrics before proceeding to the next partner. 

1.  **Decommission RTB-dedicated NAT Gateways:** After all RTB partner traffic is migrated, confirm using VPC Flow Logs that no RTB traffic traverses the NAT Gateways. Delete unused NAT Gateways and update infrastructure as code to guard against recreation. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST03-BP01 Consider private communication channels between SSP and DSP](advcost03-bp01.md) 
+  [ADVCOST03-BP06 Maximize partner traffic routed inside a managed connectivity fabric](advcost03-bp06.md) 

 **Related documents:** 
+  [AWS RTB Fabric Pricing](https://aws.amazon.com/rtb-fabric/pricing/) 
+  [Prebid Server Deployment on AWS Cost](https://aws.amazon.com/solutions/implementations/prebid-server-deployment-on-aws/) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 