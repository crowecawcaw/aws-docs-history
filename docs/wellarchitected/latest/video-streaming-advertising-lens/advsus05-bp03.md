

# ADVSUS05-BP03 Optimize content moderation systems for sustainable operation
<a name="advsus05-bp03"></a>

 As an organization's content library grows, optimizing content moderation systems improves sustainability-related KPIs. Build architectures that use efficient machine learning models, automated scaling, and optimized storage patterns so that moderation capacity tracks demand instead of running continuously at peak. 

 **Desired outcome:** 
+  Content moderation runs on right-sized, energy-efficient infrastructure that scales with actual moderation demand. 
+  Machine learning inference uses purpose-built, high-efficiency hardware, non-urgent workloads are processed in batches, and moderation data is stored and tiered according to access patterns. 
+  Moderation compute and storage scale up and down with demand rather than remaining provisioned for peak load. 
+  Machine learning inference for content classification runs on hardware selected for performance per watt. 
+  Non-real-time moderation work is batched and scheduled to improve resource utilization. 
+  Moderation results and audit trails are stored on storage classes matched to their access frequency. 

 **Common anti-patterns:** 
+  Running content moderation fleets at fixed peak capacity regardless of actual content volume. 
+  Performing every moderation task synchronously in real time, including work that has no latency requirement. 
+  Running inference on general-purpose compute when purpose-built, higher-efficiency hardware is available for the workload. 
+  Retaining moderation results and audit trails on a single high-performance storage tier indefinitely with no lifecycle management. 

 **Benefits of establishing this best practice:** 
+  Reduced energy consumption and provisioned-but-idle capacity for moderation workloads. 
+  Lower cost and improved utilization through demand-based scaling and batch processing. 
+  Improved performance per watt by matching workloads to efficient compute and storage options. 
+  Better visibility into moderation resource use, enabling continued optimization over time. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Content moderation demand tracks how fast the catalog grows and how often assets are ingested, re-ingested, and re-scanned. When you provision the pipeline for peak volume and leave it running, provisioned capacity exceeds actual volume most of the time. That idle capacity still draws power. Waste appears as low utilization and high instance-hours. 

 Moderation work varies in latency requirements. Some decisions are latency-sensitive, such as gating an asset before it goes live, and their service-level objective sizes the real-time tier. Other work, such as re-scanning archived content, producing audit data, or reprocessing a back catalog under updated policies, has no immediate deadline. Sort work into these two classes so the real-time tier stays small while deferrable work accumulates into higher-utilization runs. Misclassifying latency-sensitive work as deferrable leaves a policy-violating asset live longer, which is a brand-safety and compliance failure. 

 Machine learning inference dominates the compute in a moderation system, so the efficiency of the inference hardware determines much of the workload's estimated footprint. Performance per watt varies across compute families, and purpose-built inference accelerators can do the same classification for far less energy than general-purpose instances. This efficiency has constraints. A model must be compatible with, and is often recompiled or optimized for, a given accelerator. The gain depends on the model as much as the silicon, and a blanket migration can regress on workloads that cannot target the accelerator. Media location is a further constraint. Moderation operates on large assets, and shuttling them between Regions to reach compute consumes energy that analyzing content near where it resides avoids. 

 Moderation also produces durable outputs, classification results and audit trails. Their storage footprint compounds as the catalog grows, and access frequency drops sharply once a decision is settled. Held on a single high-performance tier, that data keeps consuming resources long after access falls to near zero. Sustaining any of these gains depends on measurement. Judge progress from utilization and throughput metrics. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select efficient inference hardware:** Use efficient machine learning models for content classification, and run inference on AWS Inferentia chips when possible for improved performance per watt. 

1.  **Batch non-real-time work:** Implement batch processing for moderation tasks that don't have real-time latency requirements, grouping them to improve resource utilization. 

1.  **Localize content analysis:** Configure Regional content analysis to minimize movement of large media assets between Regions. 

1.  **Cache frequently accessed rules:** Use caching strategies for frequently accessed moderation rules to avoid redundant lookups and recomputation. 

1.  **Use energy-efficient compute:** Use energy-efficient computing resources, such as AWS Graviton, for moderation workloads. 

1.  **Scale with demand:** Implement automated scaling based on moderation demand using auto scaling rules and Amazon CloudWatch metrics. 

1.  **Optimize moderation storage:** Optimize storage patterns for moderation results and audit trails. For workloads using Amazon S3, use S3 Storage Lens for insights and recommendations to optimize storage use. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS05-BP02 Optimize fraud detection systems for resource efficiency](advsus05-bp02.md) 
+  [ADVSUS01-BP07 Classify content once at ingest to remove repeat inference from the auction path](advsus01-bp07.md) 
+  [ADVSUS04-BP02 Match model capability to task complexity to reduce agent fleet energy use](advsus04-bp02.md) 

 **Related documents:** 
+  [AWS Well-Architected Framework Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) 

 **Related services:** 
+  [Amazon Rekognition](https://aws.amazon.com/rekognition/) 
+  [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/) 
+  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) 
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html) 