

# ADVSUS03-BP03 Shed predictably low-value traffic at the network layer to reduce the compute footprint

 Built-in network-layer modules can filter unwanted traffic without additional infrastructure. Filtering low-value requests early reduces compute resource demand and energy consumption. 

 **Desired outcome:** 
+  Predictably low-value bid requests are filtered at the network layer and never reach your bidding compute. 
+  Compute provisioned for real-time bidding is sized to traffic you actually act on, rather than to traffic you reliably discard. 
+  Traffic spikes are absorbed before they propagate to downstream systems, avoiding reactive over-provisioning. 
+  Resource consumption per bid opportunity worth acting on trends downward over time as a proxy for energy efficiency. 

 **Common anti-patterns:** 
+  Accepting every inbound bid request into the application tier and deciding no-bid in application code, paying full compute and energy cost for discarded traffic. 
+  Scaling out bidding compute to handle traffic volume without first measuring how much of that traffic results in a no-bid. 
+  Deploying aggressive network-layer filters directly to production without validating filter accuracy, and dropping requests that would have produced a bid with no signal that it happened. 
+  Treating traffic spikes as a capacity problem to be solved with more instances rather than shaping or rate-limiting the traffic at ingress. 

 **Benefits of establishing this best practice:** 
+  Lower compute footprint and energy consumption by avoiding processing of traffic you would reject anyway. 
+  Reduced infrastructure required to absorb spikes, improving the resource efficiency of the overall fleet. 
+  Improved stability of downstream systems through ingress rate limiting. 
+  Reduced compute utilization attributable to filtering decisions, which is a proxy for energy savings. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 In real-time bidding, every inbound request forces a bid or no-bid decision, and a large fraction of that traffic is predictably unactionable. Its outcome is fixed by attributes the request already carries, independent of the specific auction. When you admit such a request into your application tier, you pay the full compute and energy cost of deserializing and evaluating it only to decline it. Even when it produces no bid, the request consumes capacity you must provision, power, and cool. In video-streaming advertising, a single ad break can fan out to high request volumes across many supply partners. The aggregate cost of processing traffic you reject anyway becomes a meaningful share of your footprint. 

 Shedding this traffic at the network layer moves the no-bid decision upstream, out of your application tier and toward the point where requests arrive. Per-request compute drops because the request never reaches your bidding servers. Steady-state fleet size drops too, often more than the per-request savings. You provision capacity for real-time bidding against peak request volume, so a fleet that never admits predictable no-bid traffic runs smaller and cuts baseline and idle energy draw. The return scales with the fraction of admitted traffic you never act on, so the practice matters most where accepted volume far exceeds acted-on volume. 

 Over-filtering is the main risk, where you shed requests you normally would have bid on. This trades efficiency for lost revenue, and it is easy to miss because a filter that discards traffic without recording it also removes the observations you would use to determine if it is calibrated correctly. Reach enforcement at the end of a rollout, so you can watch a filter's intended decisions against live traffic before enforcement. For traffic spikes, limit or queue requests at ingress rather than scaling the fleet for peak load. Adding instances leaves that capacity idle most of the time, while shaping traffic at ingress keeps the fleet sized for sustained load. You reason from resource signals such as compute utilization and fleet size. \#\#\# Implementation steps 

1.  **Measure your no-bid ratio:** Analyze your historical bid/no-bid ratio to quantify how much admitted traffic you discard. A high no-bid ratio (for example, no-bidding on the majority of requests) indicates significant opportunity to filter at the network layer. 

1.  **Filter predictable no-bid traffic at the network layer:** Use the OpenRTB Attribute Module to shed predictable no-bid traffic before it reaches your compute, configuring filters on attributes such as geo, device type, COPPA flags, or domain. Filtered requests receive an automatic no-bid response without hitting your servers, avoiding their compute and energy consumption. 

1.  **Validate filter accuracy with a holdback:** Start with a high holdbackPercentage (for example, 90%) and gradually decrease it as you confirm the filter is rejecting only traffic you intended to reject. 

1.  **A/B test before committing to no-bid actions:** Use the headerTag action to tag requests non-destructively for A/B testing, observing filter behavior before switching to noBid actions. 

1.  **Rate limit to protect downstream systems:** Where spikes are the concern rather than attribute-based value, apply per-partner rate limiting as defined in [ADVSUS02-BP02 Apply rate limiting to control inbound request volume per partner](advsus02-bp02.md) (the primary home for the Rate Limiter Module), which caps TPS per link to absorb bursts at ingress instead of scaling compute to handle them. 

1.  **Track filtering effectiveness:** Monitor the volume of traffic shed at the network layer and the corresponding reduction in compute utilization to confirm the practice is delivering efficiency gains and to inform further tuning. Read the shed volume against total inbound volume so the figure reflects efficiency rather than a change in traffic. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS02-BP01 Reject non-actionable bid requests before they draw compute energy](advsus02-bp01.md) 
+  [ADVSUS02-BP03 Suppress low-probability outbound bid requests to avoid needless compute and network draw](advsus02-bp03.md) 
+  [ADVSUS02-BP04 Reduce no-bid response volume to lower infrastructure demand and energy draw](advsus02-bp04.md) 

 **Related documents:** 
+  [AWS RTB Fabric modules](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/modules.html) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [AWS Sustainability service](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) 