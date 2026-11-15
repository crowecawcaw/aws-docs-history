

# RTB Fabric infrastructure efficiency
<a name="advsus03"></a>

 Network infrastructure is a major energy consumer for RTB workloads given the transaction volumes exchanged between AdTech partners. AWS RTB Fabric provides purpose-built infrastructure that can reduce resource consumption compared to standard cloud networking. 


|  ADVSUS03: How do you improve infrastructure efficiency when using AWS RTB Fabric for your real-time bidding workloads?  | 
| --- | 
| [ADVSUS03-BP01 Align partner connectivity capacity with bid activity to reduce idle energy draw](advsus03-bp01.md) | 
| [ADVSUS03-BP02 Route more partner traffic internally to share infrastructure and energy savings](advsus03-bp02.md) | 
| [ADVSUS03-BP03 Shed predictably low-value traffic at the network layer to reduce the compute footprint](advsus03-bp03.md) | 
| [ADVSUS03-BP04 Carry only the OpenRTB fields the bidding logic uses to reduce bytes on the wire](advsus03-bp04.md) | 
| [ADVSUS03-BP05 Remove dedicated load balancers from the bid path to reduce their idle energy draw](advsus03-bp05.md) | 
| [ADVSUS03-BP06 Continuously measure fabric utilization and retire unjustified capacity](advsus03-bp06.md) | 

## Capability intent
<a name="advsus03-capability-intent"></a>
+  Partner connectivity flows over AWS RTB Fabric's transaction-oriented model rather than persistent NAT gateways, so connectivity energy and resource consumption scale with bid activity instead of remaining constant. 
+  A high and growing share of real-time bidding traffic stays inside RTB Fabric between participating partners, capturing efficiency gains that are shared across all partners rather than by a single party. 
+  Predictably low-value bid requests are shed at the network layer before they reach bidding compute, so capacity is sized to the traffic the organization actually acts on rather than to traffic it reliably discards. 
+  RTB partner traffic is distributed through RTB Fabric's built-in DNS-based routing and carried in compact OpenRTB payloads kept at or below the 2 KiB target, minimizing persistent infrastructure and per-transaction data-transfer overhead. 
+  Resource consumption is measured continuously against paired efficiency and campaign KPIs, and allocation is adjusted as demand and partner mix shift so provisioned capacity stays aligned with the actual bidding workload. 

## Common issues to watch for
<a name="advsus03-common-issues-to-watch-for"></a>
+  Running persistent NAT gateways and dedicated load balancers for bursty RTB traffic, leaving idle infrastructure consuming energy regardless of bid volume, and leaving it provisioned after traffic has migrated to a more efficient path. 
+  Routing bid traffic over external paths by default even when both the requester and responder are already RTB Fabric customers, and not measuring the split between inside and external traffic. 
+  Admitting every inbound bid request into the application tier and deciding no-bid in application code, paying full compute and energy cost for discarded traffic. The opposite failure also applies. Over-filtering at the network layer drops requests that would have produced a bid. 
+  Sending verbose OpenRTB payloads that include fields no downstream system reads, and treating payload size as a one-time tuning task rather than a continuously monitored metric. 
+  Provisioning capacity for peak bidding volume once and leaving it fixed, and monitoring only campaign performance while ignoring resource-efficiency signals such as compute utilization per thousand bid requests or resource-per-impression. 