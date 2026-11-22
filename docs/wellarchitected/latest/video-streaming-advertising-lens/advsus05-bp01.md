

# ADVSUS05-BP01 Optimize privacy workload processing patterns and resource allocation for sustainability

 Privacy-enhanced collaboration introduces sustainability considerations for advertising workloads that combine first-party and third-party customer data. The processing patterns and resource allocation you choose for data matching and cleansing influence the energy and carbon footprint of the workload. 

 **Desired outcome:** 
+  Privacy-preserving data collaboration workloads run on right-sized, energy-efficient compute that scales with actual demand. 
+  Compute-intensive matching and cleansing operations are scheduled and located to minimize energy use and data movement. 
+  Data is stored and exchanged in compact, columnar formats that reduce processing and transfer overhead. 

 **Common anti-patterns:** 
+  Running privacy computations continuously on persistent, over-provisioned instances regardless of collaboration demand. 
+  Processing raw, uncompressed, row-oriented data and moving full datasets across Regions before any aggregation. 
+  Defaulting to general-purpose x86 instances without evaluating energy-efficient processor options for matching workloads. 

 **Benefits of establishing this best practice:** 
+  Lower energy consumption and carbon footprint for privacy-enhanced collaboration workloads. 
+  Reduced cost through right-sized, demand-driven compute and lower data transfer volumes. 
+  Improved processing efficiency from compact data formats and purpose-fit compute. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 With privacy-enhanced collaboration, advertisers and publishers derive shared insight from combined first-party and third-party customer data without exposing individual records. In video-streaming advertising, this collaboration underpins audience overlap analysis, suppression, and campaign measurement, and its role is growing as third-party identifiers decline and more targeting relies on matched first-party signals. 

 The work is a chain of operations: 
+  Matching resolves and conglomerates the records that describe the same person or household across parties 
+  Cleansing normalizes, deduplicates, and discards invalid records 
+  Aggregation organizes detail into non-identifying groups 

 Each stage is data-intensive and bursty, driven by campaign planning and reporting cycles rather than a steady stream of viewer requests. Infrastructure provisioned for constant demand spends most of its life idle, generating carbon emissions with no delivered output. 

 This workload's results are consumed on analysis and reporting timescales, not in the request path of ad delivery. A planner sizing a campaign or an analyst studying audience overlap tolerates minutes or hours of latency, a different constraint from the milliseconds an ad-serving decision allows. That latency tolerance is the main sustainability opportunity, because deferrable work can be shifted in time and consolidated instead of held ready on standby. Grid carbon intensity varies by hour and by location, so the same computation finished during a cleaner window or in a lower-carbon Region has a smaller estimated footprint for identical output. Treating deferrable work as latency-critical prevents time-shifting and requires continuously running, over-provisioned capacity. 

 A collaboration cycle's energy use depends as much on how much data it touches and how far that data travels as on the algorithm it runs. Privacy rules heighten the trade-off by constraining where records may reside and how they must be transformed. This can force less efficient data movement or replication. Instrument the resource-utilization proxies you can see, such as compute time, bytes transferred, and storage footprint. Base decisions on those proxies, treating a reduction in them as a reduction in estimated energy cost. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Schedule for lower carbon intensity:** Run intensive privacy computations as scheduled, time-shiftable batch jobs rather than continuously, and prefer lower-carbon AWS Regions. To target genuinely lower-carbon periods, drive scheduling from a carbon-intensity data source (a third-party grid carbon-intensity API or published Region-level carbon data), since AWS doesn't expose a built-in real-time grid carbon-intensity signal. 

1.  **Use batch processing:** Process data cleansing and matching operations as batch jobs to avoid persistent resource consumption. 

1.  **Adopt efficient data formats:** Implement efficient data compression and use compact columnar formats such as Parquet for processing and exchange. 

1.  **Use energy-efficient compute:** Run matching and cleansing workloads on AWS Graviton processors to lower energy use per operation. 

1.  **Prefer serverless for matching:** Use serverless architectures for matching operations where possible to reduce idle capacity. 

1.  **Scale to actual demand:** Implement auto scaling driven by actual collaboration workload patterns so capacity tracks real usage. 

1.  **Aggregate data regionally first:** Configure Regional data aggregation before central processing to reduce cross-Region data transfer needs. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS05-BP02 Optimize fraud detection systems for resource efficiency](advsus05-bp02.md) 
+  [ADVSUS05-BP03 Optimize content moderation systems for sustainable operation](advsus05-bp03.md) 

 **Related documents:** 
+  [Hardware and services](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/hardware-and-services.html) 
+  [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html) 

 **Related services:** 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [AWS Graviton](https://aws.amazon.com/ec2/graviton/) 
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) 