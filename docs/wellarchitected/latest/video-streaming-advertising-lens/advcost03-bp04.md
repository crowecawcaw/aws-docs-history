

# ADVCOST03-BP04 Shape outbound traffic and optimize no-bid handling

 SSPs pay for every bid request sent regardless of whether a DSP responds with a bid. DSPs pay for every no-bid response returned. Both costs are avoidable when historical data can predict which requests will not generate bids. Shape outbound request traffic by suppressing low-probability requests before transmission, and coordinate with partners to reduce non-viable traffic volume at the source. 

 **Desired outcome:** 
+  Only bid requests with a meaningful probability of receiving a bid are sent to each DSP, avoiding wasted costs on predictably non-converting traffic. 
+  Per-DSP bid rate profiles are segmented by inventory type, geo, device, and time of day, and recalibrated weekly. 
+  No-bid response volume is minimized through upstream traffic quality improvements and network-layer handling of predictable no-bid scenarios. 
+  The most common no-bid reasons per SSP link are identified, quantified, and shared with partners to drive traffic quality improvements. 

 **Common anti-patterns:** 
+  Treating all DSP links equally without per-partner traffic shaping, so investment continues in connections that generate minimal revenue return per request sent. 
+  Suppressing traffic based on static rules without ongoing recalibration, which allows models to drift as DSP buying patterns shift with campaign flights, budget pacing, and seasonal demand. 
+  Ignoring no-bid response costs as inherent RTB overhead without analyzing which links generate disproportionate no-bid volume. 
+  Processing all inbound requests through the full bidding stack before deciding to no-bid, when many no-bid decisions could be made at the network layer based on predictable attributes. 
+  Asking partners to send better traffic without providing specific data on which segments produce zero bids and what targeting filters would suppress them. 

 **Benefits of establishing this best practice:** 
+  Reduce outbound request volume by 30-60% per DSP while maintaining bid revenue. 
+  Lower transaction and networking costs proportional to suppressed request volume. 
+  Reduce no-bid response costs by addressing the highest-volume non-viable traffic sources. 
+  Improve partner relationships through respectful traffic volumes aligned with buying interest and shared cost reduction data. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 SSPs send bid requests to DSPs on a per-impression basis. Each outbound request consumes networking, serialization, and connection resources regardless of whether the DSP responds with a bid. On the DSP side, no-bid responses consume the same infrastructure resources as winning bids through most of the processing pipeline. Both costs come from traffic that produces no revenue for either side. Address them together: outbound suppression on the SSP side and no-bid root cause analysis on the DSP side. 

 A bid rate profile shows how request attributes (inventory type, geography, device, and time of day) map to bid probability for a specific DSP. DSPs buy different inventory based on their active campaign portfolios. One DSP might bid heavily on mobile video in North America and never bid on desktop display in APAC. You can find these patterns in historical bid and no-bid response data. They stay stable within a campaign flight window (typically one to four weeks). Use [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) to calculate bid rate profiles across these dimensions at scale, and use [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) to store the bid event logs that feed the analysis. 

 Suppression saves infrastructure cost, but suppressing a request that would have received a bid loses more revenue than the savings. The right threshold depends on average bid value per segment, not just bid rate. A segment with 3% bid rate and high average CPM can generate more revenue per request sent than one with 15% bid rate and low CPMs. 

 DSP buying patterns shift as campaigns start, end, and pace their budgets. A segment with zero bid probability this week can become active next week when a new campaign targets that inventory. Without recalibration, static suppression rules drift from current DSP behavior and lose revenue over time. Recalibrate weekly with fresh bid response data to catch these shifts before they compound. Because you can't observe bids you never solicited, revenue loss from a stale model stays invisible. 

 No-bid causes are either addressable or non-addressable: 
+  Addressable causes are request attributes that could be filtered upstream before the request reaches the bidder: geographies the DSP never targets, ad formats it doesn't support, or floor prices above its maximum bid range. 
+  Non-addressable causes are decisions that require full bidder evaluation: frequency cap exhaustion, budget pacing limits, or real-time audience segment mismatches. 

 Only addressable causes can be handled by outbound suppression or at the network layer. To distinguish them, analyze the top no-bid reasons for each partner link. 

 Coordinate with partners to reduce no-bid volume at the source. SSPs pay transmission costs on every request, so reducing non-viable volume benefits both parties. Effective coordination requires specific data: which segments produce zero bids, what volume they represent, and what targeting filters would suppress them. For predictable no-bid scenarios on the DSP side, configure RTB Fabric filtering modules to return no-bid responses at the network layer. This avoids compute cost and maintains the correct protocol response. 

 Per-link rate limiting is a coarser mechanism that complements attribute-based shaping. Cap QPS at the volume where bid rate stays above a minimum threshold to avoid over-sending to DSPs that can't evaluate more volume. DSPs prefer targeted traffic over undifferentiated volume that strains their evaluation capacity. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable bid and no-bid response logging to S3:** Configure bid event logging that captures request attributes (inventory type, geo, device type, and time of day) alongside the bid or no-bid outcome for each request sent. Write to S3 in a queryable format (Parquet partitioned by date and DSP). This is the data foundation for both outbound shaping and no-bid analysis. 

1.  **Build per-DSP bid rate profiles using Athena:** Run Athena queries against 30 days of historical bid logs to calculate bid rates segmented by (DSP x inventory type x geo x device type x time of day). Identify attribute combinations where bid probability falls below your minimum threshold (typically 5%). Document the traffic volume these low-probability segments represent. 

1.  **Implement attribute-based traffic shaping rules on outbound links:** Configure RTB Fabric filtering modules on each link to suppress requests matching low-bid-probability segments. Start conservatively with only the lowest-probability segments (under 2% bid rate). Use holdback testing to validate that suppressed traffic produces no bids. Gradually expand filtering coverage as accuracy is confirmed. 

1.  **Configure per-link rate limiting aligned to DSP capacity:** Set per-link QPS caps at the volume where bid rate remains above your minimum threshold. This helps avoid over-sending to DSPs that can't meaningfully evaluate additional volume, reducing wasted costs while maintaining the partner relationship. 

1.  **Analyze no-bid reasons for the highest-cost partner links:** Categorize why bids are not placed for the top-5 highest-cost links: unsupported geographies, floor prices above bid range, incompatible ad formats, and inventory types outside buying interest. Document which causes are addressable and which are not. For addressable causes, configure network-layer no-bid responses to avoid compute cost while maintaining protocol correctness. 

1.  **Engage partners with specific traffic quality data:** Share quantified savings opportunity with partners. For SSP-to-DSP: provide the specific segments where your bid rate is effectively zero as the targeting filter specification. For DSP-to-SSP: share per-link rejection rates and request that partners apply targeting filters to reduce non-viable requests. Track adoption and savings over time. 

1.  **Schedule weekly recalibration of bid rate profiles and shaping rules:** Automate weekly Athena queries that recalculate per-DSP bid rate profiles. Alert when bidding patterns shift significantly (indicating campaign flight changes). Update traffic shaping configurations. Review filter effectiveness monthly by comparing expected against actual no-bid rates on filtered attributes. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST03-BP03 Filter inbound bid requests at the network layer to reduce compute costs](advcost03-bp03.md) 

 **Related documents:** 
+  [AWS RTB Fabric Modules Documentation](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/modules.html) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 