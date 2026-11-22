

# ADVSUS02-BP03 Suppress low-probability outbound bid requests to avoid needless compute and network draw

 You can predict which requests will likely receive bids by mining historical bid and no-bid patterns per DSP. Suppressing them before transmission cuts unnecessary infrastructure use and energy expenditure. 

 **Desired outcome:** You shape outbound bid request traffic before it leaves your infrastructure, so that requests with a low predicted probability of receiving a bid are suppressed rather than transmitted and processed. 
+  Per-DSP bid probability models inform a pre-send decision on every request. 
+  Requests below a defined probability threshold are dropped before they consume transmission, serialization, and downstream compute resources. 
+  Suppression rates and the associated compute, network, and energy savings are measured and reported. 

 **Common anti-patterns:** 
+  Broadcasting every incoming request to every connected DSP regardless of historical bid behavior. 
+  Treating all DSPs and inventory uniformly instead of profiling bid rates by inventory type, geo, device, and time of day. 
+  Setting suppression thresholds once and never re-calibrating as DSP behavior shifts. 
+  Measuring only revenue and fill rate while ignoring the resource and energy cost of unbid requests. 

 **Benefits of establishing this best practice:** 
+  Reduced compute, network, and energy consumption from avoiding requests that were never likely to be bid on. 
+  Lower carbon footprint for the bidding pipeline without a meaningful loss of bid opportunities. 
+  More headroom on existing infrastructure, deferring or avoiding capacity growth. 
+  Clearer visibility into which traffic actually drives value across the DSP fleet. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 In a real-time bidding pipeline, the cost of an outbound bid request is committed the instant it leaves your infrastructure. Serialization, network egress, and downstream processing are consumed whether a bid ever comes back, and that cost falls on both the sender and the receiving DSP. A request that was never going to win a bid is therefore waste. Because that waste is spent at the moment of transmission, the only place to recover it is before the request is sent. Pre-send suppression uses a cheap prediction to avoid a larger, near-certain cost. It pays off only when the estimated bid probability is reliable, and the declined requests are worth less than the resources they would have consumed. 

 A single blended bid rate for a DSP is misleading, because a buyer's willingness to bid is conditional. Interest concentrates in the inventory a buyer's active campaigns target and falls away elsewhere. An aggregate rate therefore averages together pockets of strong demand and pockets of almost none. Suppressing against that average forces a poor compromise. Instead, set the threshold based on the observed distribution of traffic, high enough to remove clearly wasteful traffic without discarding valuable traffic. The safety of suppression depends on the resolution at which bid probability can be estimated. The more finely the prediction conditions on the attributes that drive a buyer's interest, the more low-probability traffic you can drop without disturbing the requests that produce fill and revenue. 

 Pre-send suppression is fragile because the bidding environment shifts constantly. Campaigns launch and exhaust budgets, buyers retarget, and demand shifts seasonally, so a probability model that was accurate when built decays on its own. The drift is asymmetric and invisible, where a stale model begins suppressing traffic a buyer would now bid on and the lost value never appears in a revenue report. This drift is also self-reinforcing, because suppression censors its own training signal. You observe bid and no-bid outcomes only for the requests you send. Suppressed traffic yields no fresh evidence, so a neglected model continues to suppress a DSP that has since resumed bidding. To keep drift from eroding value unnoticed, treat model accuracy as time-limited and re-establish it from current behavior. Preserve some visibility into the traffic you would otherwise drop. 

 Because the benefit of this practice is a cost that never occurs, it must be inferred. Estimate it from the compute, serialization, and network the suppressed requests would have consumed. Keeping that proxy honest matters, because a healthy-looking suppression rate can mask over-suppression of traffic that would have converted. To distinguish trading waste for sustainability gains from trading away demand, read the estimated resource savings alongside the fill and revenue that survived suppression. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Build per-DSP bid rate profiles:** Segment historical bid and no-bid data by inventory type, geo, device, and time of day to model each DSP's interest. 

1.  **Set predicted bid probability thresholds:** Define a minimum predicted bid probability per link and suppress requests that fall below the threshold before transmission. 

1.  **Enforce per-link rate limits:** Apply per-link QPS caps using the AWS RTB Fabric rate limiter module, aligned to each DSP's actual capacity and interest, following the per-partner rate-limiting approach defined in [ADVSUS02-BP02 Apply rate limiting to control inbound request volume per partner](advsus02-bp02.md). Here it is applied on the SSP-side outbound path. 

1.  **Re-calibrate models weekly:** Retrain the bid probability models using recent no-bid response data to keep predictions accurate as DSP behavior shifts. 

1.  **Track resource savings:** Measure the compute, serialization, and transmission the suppressed traffic would have consumed, using Athena over bid and no-bid logs together with CloudWatch. Read the suppressed share against total outbound volume so the saving is distinguishable from a drop in demand. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS02-BP01 Reject non-actionable bid requests before they draw compute energy](advsus02-bp01.md) 
+  [ADVSUS02-BP04 Reduce no-bid response volume to lower infrastructure demand and energy draw](advsus02-bp04.md) 
+  [ADVSUS03-BP03 Shed predictably low-value traffic at the network layer to reduce the compute footprint](advsus03-bp03.md) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) (rate limiter module) 
+  [Amazon S3](https://aws.amazon.com/s3/) (bid and no-bid log storage) 
+  [Amazon Athena](https://aws.amazon.com/athena/) (historical bid pattern analysis) 
+  [AWS Graviton](https://aws.amazon.com/ec2/graviton/) (for energy-efficient analytics) 
+  [AWS Sustainability service](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) 