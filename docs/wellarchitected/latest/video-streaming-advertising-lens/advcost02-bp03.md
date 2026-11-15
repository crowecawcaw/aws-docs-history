

# ADVCOST02-BP03 Use provisioned resource allocation for campaigns with predictable capacity, and use dynamic allocation for unexpected capacity
<a name="advcost02-bp03"></a>

 Provisioned and on-demand pricing give advertising workloads different cost profiles. Provisioned capacity reserves dedicated resources at a lower cost for each unit and suits predictable workloads. On-demand and serverless capacity cost more per unit but scale freely, which suits unpredictable workloads. Match each component to a suitable model to avoid both overspending and under-provisioning. 

 **Desired outcome:** 
+  Each component of your RTB architecture uses the capacity model best suited to its traffic pattern. 
+  The combination of provisioned, on-demand, and serverless results in optimized costs without sacrificing performance or availability. 

 **Common anti-patterns:** 
+  Using on-demand capacity for all services by default, which raises costs significantly for components with predictable, sustained traffic patterns. 
+  Over-provisioning capacity to handle peak loads without using auto scaling for burst absorption. 
+  Treating the capacity model as a one-time decision rather than re-evaluating as traffic patterns evolve with new campaigns. 

 **Benefits of establishing this best practice:** 
+  Significant cost reduction by matching pricing models to actual usage patterns across all RTB components. 
+  Improved ability to absorb traffic spikes without over-provisioning for steady-state workloads. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Provisioned capacity charges for the reservation whether you consume it or not. On-demand capacity bills only for what you use. 

 Utilization determines the breakeven point between capacity models. Provisioned capacity becomes cheaper than on-demand once sustained utilization exceeds 60 to 70 percent of the provisioned amount. The exact threshold varies by service. 

 Advertising workloads can display both patterns, sometimes in the same workload. Bid evaluation fleets and user profile lookups hold steady throughput during business hours across active campaign markets. Campaign launches, seasonal events, and month-end advertiser budget flushes create unpredictable spikes that can exceed baseline by three to five times within minutes. 

 Use a hybrid pattern, a provisioned baseline with on-demand burst, to handle both patterns. [Amazon DynamoDB auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html) adjusts provisioned throughput within defined bounds, but it reacts to sustained load changes over minutes rather than instantaneous spikes. [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/how-do-i-size-a-stream.html) offers both provisioned and on-demand modes, though switching between them requires understanding the resharding delay and its effect on consumer applications. [AWS Lambda provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) avoids cold starts for a fixed cost, which matters for bid evaluation functions where cold start latency exceeds exchange response deadlines. 

 Campaign portfolios shift quarterly, new advertiser verticals bring different traffic shapes, and seasonal patterns differ from year to year. A table set to provisioned during a stable campaign period might need on-demand mode during an unpredictable product launch. When you leave a capacity mode static, cost drifts as real traffic diverges from the original configuration. 

 When the infrastructure team sets capacity modes but the campaign operations team controls traffic patterns, the two teams can fall out of sync. The campaign team launches a high-traffic campaign without notifying the infrastructure team, provisioned capacity falls short, throttling starts, and bids are lost. Establish a feedback loop between the teams that control demand and the teams that control supply. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory all AWS services and categorize by traffic pattern:** Classify each service as consistent baseline, predictable peaks, variable or bursty, or short-lived and temporary. Document the classification and use it to guide capacity model selection. 

1.  **Apply provisioned capacity to stable baseline workloads:** Configure DynamoDB provisioned throughput with auto scaling for user profile and frequency cap tables with consistent read/write patterns. Use Kinesis Data Streams provisioned capacity for steady ingestion rates. Configure Lambda provisioned concurrency for latency-sensitive bid evaluation functions that must respond without cold starts. 

1.  **Apply on-demand or serverless capacity to unpredictable workloads:** Switch DynamoDB tables with variable, campaign-driven traffic to on-demand mode. Use Kinesis on-demand mode for fluctuating event volumes during campaign launches. Use Amazon Athena on-demand capacity for ad-hoc analytics queries. 

1.  **Implement a hybrid approach with auto scaling for burst handling:** Configure auto scaling on provisioned DynamoDB capacity with target utilization thresholds. Set minimum provisioned capacity at the predictable baseline and maximum at 150% of expected peak. Use AWS Cost Explorer monthly to compare actual spend against alternative models and adjust configurations as campaign patterns evolve. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Choose the data stream capacity mode (Kinesis)](https://docs.aws.amazon.com/streams/latest/dev/how-do-i-size-a-stream.html) 
+  [Serverless on AWS](https://aws.amazon.com/serverless/) 
+  [Pricing for Provisioned Capacity](https://aws.amazon.com/dynamodb/pricing/provisioned/) 
+  [Configuring provisioned concurrency for a function](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) 

 **Related services:** 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 