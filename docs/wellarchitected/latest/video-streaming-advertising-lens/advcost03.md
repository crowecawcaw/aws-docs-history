

# RTB connectivity, traffic, and compute cost
<a name="advcost03"></a>

 Communication between SSPs and DSPs can be significant and can lead to high communication costs. Cross-AZ data transfer charges, internet egress fees, and NAT Gateway processing charges accumulate rapidly at RTB scale. Using private communication channels, co-locating SSP and DSP platforms, and co-locating bidder and database nodes reduces these costs while also improving latency. Beyond connectivity architecture, filtering invalid or non-matching bid requests at the network layer before they reach application compute avoids wasted processing costs. SSPs can shape outbound traffic to suppress requests unlikely to generate bids, and DSPs can optimize no-bid response handling to reduce infrastructure demand. AWS RTB Fabric provides purpose-built infrastructure with transaction-based pricing, built-in traffic filtering modules, Availability Zone affinity, and auto-scaling compute that compounds these savings. 


|  ADVCOST03: How do you minimize data transfer and communication costs between advertising platform components?  | 
| --- | 
| [ADVCOST03-BP01 Consider private communication channels between SSP and DSP](advcost03-bp01.md) | 
| [ADVCOST03-BP02 Implement Availability Zone affinity across the RTB data path](advcost03-bp02.md) | 
| [ADVCOST03-BP03 Filter inbound bid requests at the network layer to reduce compute costs](advcost03-bp03.md) | 
| [ADVCOST03-BP04 Shape outbound traffic and optimize no-bid handling](advcost03-bp04.md) | 
| [ADVCOST03-BP05 Replace per-gigabyte egress with transaction-priced partner connectivity](advcost03-bp05.md) | 
| [ADVCOST03-BP06 Maximize partner traffic routed inside a managed connectivity fabric](advcost03-bp06.md) | 
| [ADVCOST03-BP07 Optimize bid request and response payload sizes to reduce data transfer costs](advcost03-bp07.md) | 
| [ADVCOST03-BP08 Use volume-tier pricing by consolidating traffic](advcost03-bp08.md) | 
| [ADVCOST03-BP09 Use built-in fabric load balancing instead of dedicated load balancers](advcost03-bp09.md) | 
| [ADVCOST03-BP10 Right-size compute with auto-scaling and serverless containers](advcost03-bp10.md) | 

## Capability intent
<a name="advcost03-capability-intent"></a>
+  SSP-to-DSP bid traffic flows over private network paths rather than the public internet, reducing internet egress charges while improving latency and security. 
+  SSP and DSP components are deployed in the same Availability Zones with zone-aware load balancing, avoiding cross-AZ data transfer charges on the high-volume bid path. 
+  Bidder nodes communicate with database nodes within the same Availability Zone, avoiding cross-AZ transfer charges for the high-frequency queries that characterize bid evaluation. 
+  Invalid and predictably non-matching bid requests are rejected at the network layer before they consume application compute resources, with filter rules iterated weekly based on no-bid analysis. 
+  Only bid requests with a meaningful probability of receiving a bid are sent to each DSP, avoiding wasted costs on requests that would predictably result in no-bid responses. 
+  No-bid response volume is minimized through upstream traffic quality improvements and network-layer handling. 
+  RTB partner traffic routes through transaction-based connectivity (RTB Fabric) instead of per-GB NAT Gateways, reducing networking costs by up to 80%. 
+  The majority of RTB partner traffic flows within the shared RTB Fabric connectivity, maximizing the cost differential between internal and external routing. 
+  Built-in modules (such as OpenRTB Filter or Rate Limiter) shed low-value traffic at the network layer without additional cost, reducing compute and networking costs by 30-70%. 
+  Average transaction size is kept under 2 KiB to minimize data transfer overhead. 
+  Availability Zone affinity avoids cross-AZ data transfer charges by co-locating all RTB infrastructure components within the same Availability Zone. 
+  RTB compute scales automatically with traffic demand using serverless containers and dual-metric auto-scaling, reducing idle compute during off-peak periods. 

## Common issues to watch for
<a name="advcost03-common-issues-to-watch-for"></a>
+  Using NAT Gateways for all traffic to AWS services that support VPC endpoints, adding both cost ($0.045/GB) and latency unnecessarily. 
+  Deploying SSP and DSP components across Availability Zones without zone-aware routing, causing all traffic to incur cross-AZ transfer charges. 
+  Querying database nodes in a different Availability Zone from the bidder, generating cross-AZ charges on every bid evaluation database lookup. 
+  Deploying filter rules without gradual rollout (holdbackPercentage), risking accidental filtering of commercially viable bid requests. 
+  Building bid probability models on aggregate data rather than segmented dimensions, missing granular patterns where a DSP bids on specific inventory types but never on others. 
+  Treating all no-bid responses as equivalent regardless of cause, when a no-bid from targeting mismatch is straightforward to address but a no-bid from budget exhaustion requires campaign coordination. 
+  Maintaining dedicated NAT Gateways for RTB traffic after migrating to RTB Fabric, paying hourly fees for unused gateways. 
+  Bid payload sizes consistently exceeding the 2 KiB no-charge data threshold, generating excess data transfer charges on every transaction. 
+  Enabling cross-zone load balancing by default, incurring round-trip cross-AZ charges on every bid request at million-QPS scale. 
+  Fixed compute capacity sized for peak RTB traffic, wasting cost during overnight low-traffic periods. 
+  Fan-out to all demand partners regardless of win rate, consuming compute and networking for low-yield adapters. 