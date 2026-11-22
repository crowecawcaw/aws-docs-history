

# ADVCOST05-BP06 Use provisioned throughput for steady-state agents and on-demand pricing for variable workloads

 Provisioned throughput can provide the lowest cost per token for steady-state advertising agents. For unpredictable advertising workloads, on-demand pricing costs less by avoiding idle capacity charges. To reduce cost, match the pricing model to the invocation pattern. 

 **Desired outcome:** 
+  Each advertising agent uses the most cost-effective inference pricing model matched to its traffic pattern. 
+  Non-real-time advertising workloads use batch inference for lower per-token pricing. 
+  AWS Lambda functions for action groups are right-sized using AWS Lambda Power Tuning. 

 **Common anti-patterns:** 
+  Using on-demand pricing for all agents regardless of volume, so steady-state agents like brand safety monitoring keep paying on-demand rates even at continual invocation rates above the Provisioned Throughput break-even point. 
+  Purchasing Provisioned Throughput commitments based on peak volume rather than sustained baseline, which pays for unused capacity during off-peak periods for bursty agents like campaign planning. 
+  Running non-real-time workloads (reporting, bulk segmentation, historical analytics) through on-demand inference when batch inference offers lower per-token pricing for latency-tolerant tasks. 
+  Over-provisioning Lambda memory for action group functions without performance testing, so compute capacity that doesn't improve execution time keeps accruing charges. 
+  Setting static budget thresholds that don't account for seasonal advertising cycles, which generates false alarms during expected peaks or misses anomalies during off-peak periods. 

 **Benefits of establishing this best practice:** 
+  Lowest achievable per-token cost for each agent by matching pricing model to actual utilization patterns. 
+  Elimination of idle compute costs for action groups through pay-per-invocation Lambda pricing. 
+  Additional savings for latency-tolerant workloads through batch inference pricing. 
+  Budget alerts that reflect business reality, detecting true anomalies without noise from expected seasonal variation. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 [Amazon Bedrock](https://aws.amazon.com/bedrock/) has three pricing models for inference: on-demand (pay per token with no commitment), Provisioned Throughput (reserved capacity at a lower per-token rate with time-based commitment), and batch inference (lowest per-token rate for asynchronous, latency-tolerant workloads). If you pick the wrong model for an agent's pattern, you risk overpaying either through idle reserved capacity or through premium on-demand rates on steady-state volume. 

 The break-even calculation for Provisioned Throughput compares the committed hourly rate against what the same invocation volume would cost on-demand. Agents with consistent, predictable volume that exceeds this threshold (brand safety monitors running around the clock and constant content classification) benefit from Provisioned Throughput. Agents with spiky, unpredictable patterns (campaign planning that surges during launch cycles and seasonal creative generation) typically cost less on-demand because the idle hours during low-demand periods would waste reserved capacity. Provisioned Throughput is available with no commitment (hourly), 1-month, or 6-month terms. Teams can start with the no-commitment option to validate utilization before locking into term discounts. 

 Batch eligibility depends on whether a workload can be deferred. If an inference consumer reads the result hours after it is produced, it is paying for an unused low-latency guarantee. [Amazon Bedrock batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html) prices that difference by queuing requests and processing them when capacity is available, at lower per-token rates. 

 The completion window for batch inference is a range, not a guaranteed deadline. A downstream consumer that assumes a fixed completion time treats an occasional slow batch as a missing-data incident. Batch jobs can't support conversational or tool-calling interactions, so a workflow that mixes deferrable analysis with interactive steps must be split at that boundary. 

 Action group functions on [AWS Lambda](https://aws.amazon.com/lambda/) are a separate cost that compounds with inference costs. Each agent invocation might trigger multiple Lambda calls for tool use (such as database lookups, API calls, and calculations). Lambda charges for both invocation count and duration multiplied by allocated memory. Over-provisioned memory increases cost without reducing execution time when the function is I/O-bound rather than compute-bound. [AWS Lambda Power Tuning](https://docs.aws.amazon.com/lambda/latest/operatorguide/profile-functions.html) tests memory configurations to find the point where additional memory stops improving performance, the minimum cost configuration for each function's workload. 

 Budget management for agentic AI workloads differs from traditional AWS services because advertising spend is seasonal. Events like holiday campaigns and sporting events create spend spikes. If you only set static budget thresholds, you might receive alarms during expected peaks (which can create alert fatigue) and not during quiet periods (which can miss actual anomalies). [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) supports time-varying thresholds that match campaign calendars, so teams can set higher allowances during known peak periods while keeping tighter controls during baseline operations. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Analyze invocation patterns for all advertising agents over 30 days:** Use Bedrock CloudWatch metrics to calculate per-agent invocation counts, peak periods, and average daily volumes. Classify each agent as steady-state, bursty, or scheduled based on this analysis. 

1.  **Calculate break-even for Provisioned Throughput:** For steady-state agents, calculate the daily invocation volume at which Provisioned Throughput cost equals on-demand cost. If your agent consistently exceeds this threshold, purchase Provisioned Throughput without a commitment term first to validate utilization, then move to a 1-month or 6-month commitment for the discount once utilization is proven. 

1.  **Configure batch inference for non-real-time workloads:** For campaign performance reports, historical analytics, and bulk audience segmentation, configure Amazon Bedrock batch inference jobs scheduled through EventBridge and Step Functions during off-peak hours. Batch inference offers lower per-token pricing than on-demand. 

1.  **Right-size Lambda action group functions:** Run AWS Lambda Power Tuning on each action group function to find the optimal memory configuration that balances execution time against cost. Functions over-provisioned with memory consume more energy without proportional latency improvement. 

1.  **Configure AWS Budgets aligned to campaign cycles:** Set budget thresholds with higher allowances during campaign launch periods and seasonal peaks. Configure alerts when Bedrock spending approaches thresholds to catch runaway agent invocations before they accumulate significant cost. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST05-BP07 Continuously evaluate new models, features, and pricing options to optimize agentic AI advertising costs over time](advcost05-bp07.md) 

 **Related documents:** 
+  [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) 
+  [Optimizing cost for generative AI with AWS](https://aws.amazon.com/blogs/aws-cloud-financial-management/optimizing-cost-for-generative-ai-with-aws/) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) 