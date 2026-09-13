

# SMCOST02-BP02 Implement parallel processing for media tasks
<a name="smcost02-bp02"></a>

Media processing tasks are inherently parallelizable. Video content can be split on I-frame boundaries, processed as independent segments, and reassembled. Sequential processing on vertically-scaled instances limits you to expensive large instance types and means a single interruption wastes the entire job. Parallel processing across many smaller workers accesses cheaper compute, completes faster, and limits the scope of impact of any single failure.

**Desired outcome:**
+ You have processing pipelines that split media into independent segments, distribute them across a fleet, and reassemble completed outputs automatically.
+ You have access to the lowest-cost compute available because granular tasks can be placed across diverse instance types and pricing models.
+ You have interruption handling that re-queues only the affected segment rather than restarting entire jobs from the beginning.

**Common anti-patterns:**
+ Processing large media files sequentially on a single instance when the workload can be split across multiple workers for faster completion and lower cost.
+ Using only On-Demand instances for batch media processing without evaluating Spot Instances for fault-tolerant parallel workloads.
+ Lacking job orchestration to manage segment dependencies, leading to idle resources waiting for upstream tasks to complete.
+ Choosing segment sizes without considering the trade-off between parallelism gains and orchestration overhead.

**Benefits of establishing this best practice:**
+ Processing completes faster because work is distributed across many workers simultaneously rather than executed sequentially.
+ Compute costs decrease because smaller tasks can run on Spot Instances where interruption impact is limited to re-processing a short segment rather than an entire file.
+ Resource utilization improves because a heterogeneous fleet of smaller instances can be fully utilized, unlike a single large instance where some dimensions sit idle.
+ Pipeline resilience increases because segment-level retries recover from interruptions without discarding completed work.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Split-and-stitch parallelization works because video codecs organize content into independently decodable groups of pictures (GOPs) delimited by I-frames. Splitting on these boundaries produces segments that can be transcoded without reference to adjacent segments. The segments are processed independently and concatenated in order once all complete. Boundary validation after stitching confirms there are no discontinuities in timestamps, audio sync, or visual artifacts at splice points.

The cost advantage comes from two directions simultaneously. First, many small tasks can run on Spot Instances. Spot pricing provides significant savings over On-Demand for interruptible workloads. Second, small tasks complete quickly, so a Spot interruption wastes only the processing time for one segment (typically 30-120 seconds of content) rather than an entire multi-hour job. Re-processing a two-minute segment costs almost nothing compared to re-processing an hour-long source from the beginning.

Fleet diversity is central to Spot availability. Requesting a single instance type in a single Availability Zone competes in a narrow capacity pool and increases interruption frequency. Defining a broad list of acceptable instance types across multiple families (compute-optimized and general-purpose of similar vCPU count) and using capacity-optimized allocation draws from the deepest pools and minimizes interruptions. The processing task doesn't care which specific instance type runs it as long as the instance meets minimum CPU and memory requirements.

Segment size is a tuning parameter with opposing forces. Smaller segments create more parallelism (faster completion, better Spot fit) but introduce more orchestration overhead (more API calls, more stitching operations, more state to track). Larger segments reduce orchestration overhead but increase the cost of any single interruption and limit how finely you can distribute load. Most media processing workloads find an optimum between 30 and 120 seconds of content duration per segment. Benchmark both extremes with your specific workload to find the balance point.

For jobs that can't tolerate delays from Spot interruptions (time-sensitive live-to-VOD processing, breaking news clips), a fallback to On-Demand capacity preserves SLA compliance. The fleet configuration should use Spot as the default with automatic On-Demand fallback rather than requiring manual intervention when Spot capacity is unavailable.

### Implementation steps
<a name="implementation-steps"></a>

1. **Implement segment splitting on I-frame boundaries:** Build or configure a splitting stage that analyzes source content for I-frame positions, divides the source into segments of your target duration, and registers each segment as an independent processing task. Validate that each segment begins with an I-frame so it can be decoded independently.

1. **Configure orchestration for fan-out and fan-in:** Use [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) Map state for workflow-based fan-out with per-segment error handling, [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) array jobs for managed job scheduling with Spot support, or [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) with Spot capacity providers for container-based processing. Configure the fan-in stage to trigger stitching only after all segments report completion.

1. **Configure a diverse Spot fleet:** Define at least six instance types across two or more instance families with similar compute characteristics (for example, c5.2xlarge, c5a.2xlarge, c6i.2xlarge, c6a.2xlarge, m5.2xlarge, m6i.2xlarge for compute-bound tasks). Use [capacity-optimized allocation strategy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-allocation-strategy.html) to select from the deepest capacity pools. Span at least two Availability Zones.

1. **Implement interruption handling and segment-level retry:** Configure [Spot interruption notifications](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-instance-termination-notices.html) (two-minute warning) to checkpoint segment progress and persist partial output. Configure the orchestrator to re-queue interrupted segments automatically. Set a maximum retry count to escalate to On-Demand after repeated interruptions on the same segment.

1. **Implement stitching and boundary validation:** Build a concatenation stage that performs the following:
+ Assembles completed segments in order
+ Validates timestamp continuity across boundaries
+ Checks audio sync at splice points
+ Produces the final output

Flag any boundary discontinuities for manual review rather than publishing content with splice artifacts.

1. **Monitor pipeline throughput and cost efficiency:** Track the following metrics:
+ Per-segment status
+ Spot interruption rate
+ Effective savings compared to On-Demand equivalent
+ Overall pipeline throughput (hours of content processed per clock hour)

Use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) dashboards to visualize these metrics and alert on throughput drops that indicate capacity or configuration problems.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMCOST02-BP01 Establish baseline metrics for media processing tasks](smcost02-bp01.html)
+ [SMCOST02-BP03 Optimize AWS Elemental Media Services pricing models](smcost02-bp03.html)

**Related documents**
+ [EC2 Spot Instance best practices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html)
+ [AWS Step Functions Map state](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-map-state.html)

**Related videos**
+ [re:Invent 2019 - Containerizing video: the next generation video transcoding pipeline](https://www.youtube.com/watch?v=tfoFilopvR0)

**Related examples**
+ [Video on Demand on AWS](https://aws.amazon.com/solutions/implementations/video-on-demand-on-aws/)

**Related services**
+ [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
+ [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)
+ [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)