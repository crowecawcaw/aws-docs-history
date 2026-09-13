

# SMCOST02-BP01 Establish baseline metrics for media processing tasks
<a name="smcost02-bp01"></a>

Consumer demand for more content at higher resolution and quality puts ongoing pressure on processing infrastructure. As transcoding, quality control, and packaging workloads grow, so do their costs. Without measured baselines, teams can't distinguish between expected cost growth and inefficiency, can't forecast accurately, and can't evaluate whether infrastructure changes improve or degrade cost performance.

**Desired outcome:**
+ You have a cost-per-hour-of-content metric for each processing task type that combines compute cost with measured processing speed.
+ You have resource utilization profiles that reveal whether instances are right-sized for their processing workloads.
+ You have trend monitoring that detects processing efficiency regressions before they materially affect monthly spend.

**Common anti-patterns:**
+ Provisioning compute resources based on assumptions rather than measured workload baselines, leading to persistent over-provisioning or under-provisioning.
+ Running media processing jobs without tracking real-time factor or resource utilization, making it impossible to identify inefficiencies or forecast costs accurately.
+ Using the same instance types for all processing tasks without benchmarking different options against actual workload characteristics.
+ Estimating processing costs based on content duration alone without accounting for complexity, resolution, or codec differences.

**Benefits of establishing this best practice:**
+ Cost forecasting accuracy improves because projections are derived from measured processing speed and resource cost rather than rough estimates.
+ Right-sizing opportunities become visible because utilization data reveals which resource dimensions (CPU, memory, or GPU) are over-allocated for each task type.
+ Efficiency regressions are caught early because trend monitoring detects changes in processing speed before they compound into significant cost increases.
+ Capacity planning becomes data-driven because you can calculate exactly how much infrastructure a given content volume requires.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

The primary metric for understanding processing speed in media workloads is the real-time factor (RTF). Calculate RTF by dividing task execution time by source duration. An RTF below 1.0 means content processes faster than it plays back. An RTF above 1.0 means it processes slower. A video transcoding task that takes 45 minutes to process a one-hour source has an RTF of 0.75. A 4K HDR transcode that takes three hours for a one-hour source has an RTF of 3.0 and requires three times the processing capacity to keep pace with real-time ingest.

RTF alone isn't useful for cost optimization. Combined with instance cost, it becomes a cost-per-hour-of-content metric. Instance cost per hour multiplied by RTF, divided by the number of parallel tasks per instance. This metric helps you compare alternatives. If a GPU instance has a higher hourly cost but a lower RTF, the cost-per-hour-of-content may be lower than a cheaper CPU instance that processes slowly. For managed services where you don't choose instance types, derive the equivalent metric from per-minute output pricing.

Processing time varies with content complexity even within the same resolution tier. A static talking-head video transcodes faster than a fast-motion sports broadcast at identical resolution. Running baselines on a single sample produces misleading numbers. You need mean and variance across representative content samples covering the complexity range your pipeline handles. Without variance data, capacity planning will under-provision for complex content or over-provision for low-complexity content.

Resource utilization during processing reveals right-sizing opportunities that RTF alone can't. High CPU with low memory usage suggests a compute-optimized instance family would cost less than a general-purpose instance. High GPU utilization with low CPU suggests the GPU is the bottleneck and adding CPU would not help. These metrics also reveal when processing is I/O bound rather than compute bound, which shifts the optimization target to storage throughput.

Baselines are not static. Encoder software updates, new codec versions, and infrastructure changes all affect processing efficiency. A quarterly re-baseline against the same representative content set detects drift. Comparing measured RTF trends against actual billing data validates that forecasting models remain accurate.

### Implementation steps
<a name="implementation-steps"></a>

1. **Define your processing task taxonomy:** Identify distinct task types in your pipeline:
+ SD transcode
+ HD transcode
+ 4K transcode
+ Audio normalization
+ Quality control
+ Thumbnail generation
+ Packaging

Document the input characteristics for each.
+ Resolution
+ Codec
+ Frame rate
+ Duration range
+ Whether the task is compute-bound, I/O-bound, or GPU-bound

1. **Calculate RTF across representative content samples:** Run each task type against 10-20 content samples spanning the complexity range (low-motion through high-motion, short through long duration). Record source duration, processing time, and instance type. Calculate mean RTF and standard deviation for each task-instance combination.

1. **Capture resource utilization during processing:** Deploy [Amazon CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) on processing instances to collect the following at one-minute granularity:
+ CPU
+ Memory
+ Disk I/O
+ Network throughput

For GPU-accelerated workloads, collect GPU utilization and GPU memory metrics. Record peak and average utilization to understand both sustained load and headroom.

1. **Calculate cost-per-hour-of-content for each task type:** Compute the metric: (instance cost per hour multiplied by RTF) divided by parallel tasks per instance. For [AWS Elemental MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html) jobs, derive from per-minute output pricing multiplied by 60 and divided by output-to-source duration ratio. Document these as your forecasting baselines.

1. **Evaluate right-sizing opportunities:** Feed utilization data into [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) for automated right-sizing recommendations. Compare your RTF and cost-per-hour-of-content across instance families. Test compute-optimized instances for CPU-bound tasks and memory-optimized instances for tasks with large intermediate buffers.

1. **Establish trend monitoring and alerting:** Create [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) dashboards showing RTF trends over time for each task type. Set alarms for RTF increases beyond one standard deviation from baseline. Validate forecasts against actual [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) data monthly. Re-baseline quarterly or after infrastructure changes.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMCOST02-BP02 Implement parallel processing for media tasks](smcost02-bp02.html)
+ [SMCOST02-BP03 Optimize AWS Elemental Media Services pricing models](smcost02-bp03.html)

**Related documents**
+ [Identifying opportunities to right-size](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/identifying-opportunities-to-right-size.html)
+ [AWS Elemental MediaConvert pricing](https://aws.amazon.com/mediaconvert/pricing/)
+ [Collecting metrics with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)

**Related videos**
+ [re:Invent 2019 - Containerizing video: the next generation video transcoding pipeline](https://www.youtube.com/watch?v=tfoFilopvR0)

**Related services**
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+ [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)
+ [AWS Elemental MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html)
+ [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)