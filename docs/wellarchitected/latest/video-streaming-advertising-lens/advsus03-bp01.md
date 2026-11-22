

# ADVSUS03-BP01 Align partner connectivity capacity with bid activity to reduce idle energy draw

 NAT gateways continuously process data and consume energy regardless of traffic quality. A transaction-oriented connectivity model matches real-time bidding (RTB) patterns and is more resource-efficient for connectivity to AdTech partners. 

 **Desired outcome:** 
+  RTB traffic to AdTech partners flows over a transaction-oriented connectivity fabric rather than persistent NAT gateways. 
+  Resource consumption attributable to partner connectivity, and the energy associated with it, scales with bid activity instead of remaining constant. 
+  NAT gateways dedicated solely to RTB traffic are decommissioned once partner traffic has migrated. 

 **Common anti-patterns:** 
+  Routing high-volume, bursty RTB traffic through NAT gateways that run and consume energy continuously even when bid volume is low. 
+  Treating partner connectivity as a fixed networking cost and never auditing which traffic paths actually require a NAT gateway. 
+  Leaving NAT gateways provisioned after partner traffic has been migrated to a more efficient path. 

 **Benefits of establishing this best practice:** 
+  Reduced idle energy consumption by aligning connectivity capacity with actual bid traffic. 
+  Improved resource efficiency for the connectivity layer of the RTB workload. 
+  Fewer persistent connectivity components, which simplifies reasoning about the sustainability impact of partner connectivity. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 RTB connectivity has a distinctive traffic profile. It exchanges short-lived, high-frequency bid transactions with AdTech partners, often with peaks tied to ad inventory availability. NAT gateways are provisioned and billed as persistent infrastructure that processes and meters data continuously. The resources and energy consumed by partner connectivity remain largely fixed regardless of whether bid volume is high, low, or idle. The mismatch between a steady-state connectivity component and a bursty workload is the underlying inefficiency this best practice addresses. 

 The gain from a transaction-oriented model is not uniform across your system, and knowing where it concentrates helps you avoid wasting migration effort. A NAT gateway dedicated to RTB egress is pure overhead once that traffic has a better path. A NAT gateway shared with non-RTB egress can't be retired at all. Migrating its RTB share reduces data processed without removing the persistent component that accounts for most of the energy. Evaluate progress by the number of NAT gateways retired. A migration that touches many NAT gateways but retires none has spent effort without reducing background consumption. Each partner link only moves when the counterparty terminates it, so a long tail of unmigrated partners keeps the legacy path in service. 

 While old and new paths run in parallel, the workload consumes more connectivity resources than before the migration started. A stalled migration is a net sustainability loss even as metrics show progress. Removing a NAT gateway while an overlooked dependency still routes through it causes an availability outage, so trigger retirement on verified traffic drainage. The defensible evidence is the count of retired persistent components and the shift in transfer volume. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Audit current RTB traffic paths:** Identify traffic flowing through NAT gateways to AdTech partners and map which connectivity paths are dedicated to RTB. 

1.  **Provision RTB Fabric gateways:** Create AWS RTB Fabric requester and responder gateways colocated with your VPC. 

1.  **Establish partner links over RTB Fabric:** Connect to your AdTech partners through AWS RTB Fabric instead of public internet paths. 

1.  **Decommission redundant NAT gateways:** Remove NAT gateways dedicated to RTB traffic once the migration is complete and verified. 

1.  **Monitor the sustainability improvement:** Track the reduction in persistent connectivity infrastructure using concrete signals you can attribute directly: retired NAT gateway count, data-transfer GB, and RTB Fabric billed transaction volume. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS03-BP02 Route more partner traffic internally to share infrastructure and energy savings](advsus03-bp02.md) 
+  [ADVSUS03-BP05 Remove dedicated load balancers from the bid path to reduce their idle energy draw](advsus03-bp05.md) 
+  [ADVSUS03-BP06 Continuously measure fabric utilization and retire unjustified capacity](advsus03-bp06.md) 

 **Related documents:** 
+  [Prebid Server overview](https://docs.prebid.org/prebid-server/overview/prebid-server-overview.html) 
+  [AWS RTB Fabric pricing](https://aws.amazon.com/rtb-fabric/pricing/) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [AWS Sustainability service](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) 