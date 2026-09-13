

# SMSUS08-BP01 use AWS managed services for efficient resource utilization
<a name="smsus08-bp01"></a>

Use managed services in place of self-operated equivalents wherever a workload fits one. Managed services share infrastructure across many customers and scale with demand, so they reach a far higher average utilization than a self-managed component that each team provisions for its own peak and leaves idle the rest of the time.

**Desired outcome:**
+ Capabilities that AWS offers as managed services are consumed as managed services rather than rebuilt on self-operated infrastructure.
+ Workloads scale with demand and don't hold idle capacity for peaks that occur rarely.
+ Engineering effort goes to streaming-specific differentiation rather than operating commodity infrastructure at low utilization.

**Common anti-patterns:**
+ Building and operating bespoke transcoding, analytics, or recommendation infrastructure when a managed service provides the same capability at higher shared utilization.
+ Provisioning standing clusters sized for peak load to run intermittent analytics or processing, leaving them powered and idle between jobs.
+ Self-hosting machine learning for content moderation or recommendations on persistent instances rather than using managed inference that scales with request volume.
+ Running self-managed monitoring infrastructure that must itself be provisioned and maintained instead of using a managed observability service.

**Benefits of establishing this best practice:**
+ Higher infrastructure utilization, because managed services share capacity across customers rather than each team provisioning its own peak.
+ Reduced idle capacity, because managed services scale with demand instead of holding standing resources.
+ Lower operational resource overhead, because the supporting infrastructure for monitoring, scaling, and patching is shared rather than duplicated per workload.
+ More engineering capacity directed at streaming differentiation rather than operating commodity components.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

A self-managed component is provisioned by a single team for its own peak demand and runs below that peak, often far below, the rest of the time, so the gap between provisioned and used capacity is powered and idle. A managed service aggregates demand across many customers and scales capacity to match, so the same workload runs at a much higher average utilization and the idle headroom each team would otherwise hold is removed. For intermittent media workloads such as batch transcoding or periodic analytics, this difference is large, because the self-managed alternative is idle most of the time.

The decision isn't unconditional, and treating "managed is unconditionally better" as a rule is how this practice is misapplied. Managed services trade a degree of control and portability for efficiency and reduced operations, and some workloads have requirements such as specific codec configurations, data residency, or latency characteristics that a managed service doesn't meet. The right approach is to default to the managed service where the workload fits and reserve self-managed infrastructure for the cases that genuinely require it, rather than rebuilding commodity capabilities by habit.

Apply the same reasoning across the stack. The following all have managed options that run at higher utilization than self-hosted equivalents.
+ File-based transcoding
+ Streaming analytics
+ Recommendation
+ Content moderation
+ Observability

Energy use isn't measurable per request, so use resource proxies such as the share of workloads on managed compared to self-managed infrastructure, and the idle capacity removed by the shift. Read account-level carbon impact per Region from the AWS Customer Carbon Footprint Tool, which publishes monthly.

### Implementation steps
<a name="implementation-steps"></a>

1. **Inventory self-managed components against managed equivalents:** List the self-operated infrastructure in the streaming workload and identify which capabilities have a managed AWS equivalent, flagging those running at low average utilization as the highest-value candidates.

1. **Move file-based transcoding to a managed service:** Replace self-managed encoding with AWS Elemental MediaConvert so transcoding runs on shared, demand-scaled infrastructure rather than standing capacity.

1. **Use managed analytics for intermittent processing:** Run streaming analytics through managed services such as Amazon Managed Service for Apache Flink or Amazon Kinesis rather than standing clusters provisioned for peak.

1. **Use managed inference for recommendation and moderation:** Adopt Amazon Personalize for recommendations and Amazon Rekognition for content analysis and moderation instead of self-hosting models on persistent instances.

1. **Use managed observability:** Consolidate monitoring on Amazon CloudWatch rather than operating self-managed monitoring infrastructure that must itself be provisioned and scaled.

1. **Measure the utilization shift:** Track the proportion of workloads on managed services and the idle capacity removed, and review against the monthly account-level figures from the AWS Customer Carbon Footprint Tool.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSUS02-BP01 Implement adaptive infrastructure scaling based on viewer patterns](smsus02-bp01.html)
+ [SMSUS07-BP01 Leverage energy-efficient computing resources](smsus07-bp01.html)

**Related documents**
+ [Optimizing Streaming Media Workflows to Reduce Your Carbon Footprint, Part I](https://aws.amazon.com/blogs/media/optimizing-streaming-media-workflows-to-reduce-your-carbon-footprint-part-i/)
+ [Sustainability Pillar, Hardware and services](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/hardware-and-services.html)

**Related services**
+ [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/)
+ [Amazon Personalize](https://aws.amazon.com/personalize/)
+ [Amazon Rekognition](https://aws.amazon.com/rekognition/)