

# ADVCOST05-BP01 Design fraud detection pipelines to minimize redundant processing and optimize inference costs

 Design fraud detection workflows that avoid repeated evaluations. Cache known outcomes, filter threats as early as possible, and run only the necessary inference steps on cost-efficient compute resources. 

 **Desired outcome:** 
+  Your fraud detection pipeline processes each unique signal only once, caches the result for repeated encounters, and applies progressively more expensive evaluation steps only to traffic that passes cheaper upstream filters. 
+  Known-bad traffic is blocked at the edge, known-good traffic bypasses deep inspection, and ML inference runs only on ambiguous cases. 

 **Common anti-patterns:** 
+  Running full ML inference on every bid request without first checking whether the creative, IP, or device ID has already been evaluated and cached. 
+  Implementing filtering logic only at the application layer rather than at the network layer, consuming compute for traffic that could be filtered out upstream. 
+  Training fraud detection models on On-Demand instances when the workload is interruptible and suitable for Spot pricing. 

 **Benefits of establishing this best practice:** 
+  Lower inference costs from avoiding repeated evaluation of previously seen inputs. 
+  Lower overall compute spend by blocking threats at the cheapest layer before they reach expensive processing stages. 
+  Early detection of cost anomalies caused by fraud attacks driving up evaluation volume. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A threat actor pays almost nothing to generate fraudulent traffic, while your cost to evaluate each request scales linearly with volume. A flat architecture that gives every request the same evaluation depth becomes economically unsustainable during attack surges. Progressive filtering orders evaluation stages by increasing cost, so cheap upstream filters remove traffic before it reaches expensive downstream stages. 

 The progressive funnel pattern assigns each detection technique to the cheapest layer that can run it. Network-layer rules at the edge ([AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html)) cost fractions of a cent per million evaluations because they execute on infrastructure already in the request path. Cached verdict lookups ([Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html)) add microseconds of latency and sub-cent costs per lookup. Rule-based heuristics require application compute but avoid ML inference overhead. ML inference is the most expensive stage, costing orders of magnitude more per evaluation than any upstream layer. Run inference only on cases the cheaper stages cannot resolve. 

 Cache effectiveness depends on how repetitive your traffic is. Advertising fraud often reuses the same creative IDs, device fingerprints, or IP ranges across millions of requests. A verdict cache converts the first evaluation of each unique input into an amortized cost across all subsequent encounters. Cache hit rates above 80% are typical for stable creative and device populations. Caches also go stale. If a previously legitimate creative becomes compromised after you cache it, the clean verdict persists until the TTL expires. Choose the TTL to balance cost savings (longer TTL, higher hit rate) against detection freshness (shorter TTL, faster response to newly compromised inputs). 

 Fraud attacks cause cost spikes because they inflate evaluation volume unpredictably. Without anomaly detection at the pipeline level, a sudden traffic surge can generate thousands of dollars in inference costs before you detect it. [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) operates on historical spending patterns and reports deviations, but it has detection lag. Teams that rely only on billing alerts might discover cost spikes hours after they begin. 

 Model training workloads tolerate interruption. Inference does not. A training job that loses its instance mid-epoch can resume from a checkpoint without losing prior computation. This makes training eligible for [Spot pricing](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html) at 60 to 90 percent lower cost than On-Demand. Spot Instances can be interrupted and delayed, so training schedules must tolerate non-deterministic duration. For fraud model retraining cadences of weekly or longer, that variability rarely matters. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement edge-level bot detection using AWS WAF Bot Control:** Deploy WAF Bot Control managed rules on bid request endpoints. Configure rate-based rules per SSP IP range. Start in Count mode to assess traffic composition, then transition to Block mode for clearly fraudulent traffic categories. This avoids compute costs for obvious threats before they reach your application. 

1.  **Deploy caching for fraud evaluation results:** Implement a cache-aside pattern using ElastiCache Redis keyed on creative ID, source IP, and device ID fingerprint. Before invoking ML inference, check the cache: if the input was evaluated within the TTL window, return the cached verdict immediately. Target 80%\+ cache hit rate for stable creative and device populations. 

1.  **Structure the fraud detection pipeline as a progressive funnel:** Configure processing stages in order: WAF rules (block known-bad at edge) → cached lookups (return known verdicts) → lightweight rule-based checks (known patterns) → ML inference (for genuinely ambiguous cases only). Measure what percentage of traffic reaches each stage. High volumes reaching ML inference may indicate overly permissive upstream filters. 

1.  **Use Spot Instances for fraud model training:** Configure SageMaker AI training jobs with Managed Spot Training enabled. Implement checkpointing so interrupted training resumes from the last checkpoint rather than restarting. Configure alarms on Cost Anomaly Detection for the SageMaker AI training service to detect unexpected cost spikes. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [AWS WAF Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html) 
+  [SageMaker AI Managed Spot Training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html) 

 **Related services:** 
+  [AWS WAF](https://aws.amazon.com/waf/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) 