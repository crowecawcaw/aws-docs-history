

# SMSUS01-BP01 Optimize regional distribution of streaming workloads to reduce waste, unnecessary use of resources and use of non-renewable energy
<a name="smsus01-bp01"></a>

Place streaming workloads in the Regions that best balance proximity to viewers against the carbon intensity of the location. Region selection sets a floor on the environmental cost of a streaming service, because the energy mix of the Region and the distance content travels to viewers are decided before any other optimization takes effect.

**Desired outcome:**
+ Compute-intensive workloads run in Regions chosen with carbon intensity and renewable energy as explicit selection criteria.
+ Content is served close to its largest viewer populations to minimize transfer distance and the energy it consumes.
+ Multi-Region footprint is sized to genuine redundancy and latency requirements rather than adopted by default.

**Common anti-patterns:**
+ Selecting Regions on cost and latency alone, with no consideration of carbon intensity or renewable energy availability.
+ Deploying to many Regions for resilience that the workload doesn't require, multiplying the infrastructure footprint without a matching availability need.
+ Serving a global audience from a single distant Region, so content travels long distances and consumes more transfer energy than a regional design would.
+ Placing compute-intensive transcoding in a high-carbon Region for convenience when an equally suitable lower-carbon Region is available.

**Benefits of establishing this best practice:**
+ Reduced carbon footprint, because compute runs in lower-carbon Regions and content travels shorter distances.
+ Lower data-transfer energy and cost through placement aligned with viewer geography.
+ A footprint matched to real requirements, because multi-Region deployment follows redundancy and latency needs rather than habit.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Region selection involves a genuine tension between two sustainability goals that don't consistently point to the same place. Serving viewers from a nearby Region minimizes transfer distance and the energy spent moving content, while choosing a lower-carbon Region minimizes the emissions of the compute itself, and the greenest Region isn't necessarily the closest one. Resolve this per workload. Latency-sensitive delivery should stay close to viewers, while compute-intensive batch work such as transcoding and encoding, which is less latency-sensitive, can be placed in a lower-carbon Region even if it is farther away. Treat carbon intensity as a first-class selection criterion alongside cost and performance rather than an afterthought.

Multi-Region architecture is the second decision, and it carries a direct footprint cost. Each additional Region a workload runs in multiplies its infrastructure footprint, so multi-Region designs should follow a real redundancy or latency requirement rather than being adopted as a default posture. Where global reach is the goal, a content delivery network and regional caching often serve viewers close to home without replicating the full processing stack into every Region, which delivers the proximity benefit at a fraction of the footprint.

Energy use isn't measurable per workload, so use resource proxies such as compute hours by Region, data-transfer distance, and cache hit ratio. Read account-level carbon impact per Region from the AWS Customer Carbon Footprint Tool, which publishes monthly. The per-Region breakdown is particularly useful here, because it shows directly whether placement decisions are moving emissions in the intended direction.

### Implementation steps
<a name="implementation-steps"></a>

1. **Map viewer demand by geography:** Analyze viewer demographics and access patterns to identify the primary audience locations that should anchor placement and caching decisions.

1. **Evaluate Regions on carbon intensity:** Assess candidate AWS Regions on renewable energy availability and carbon intensity alongside cost and latency, and record carbon intensity as an explicit selection criterion.

1. **Place compute-intensive work in lower-carbon Regions:** Locate latency-tolerant workloads such as transcoding and encoding in lower-carbon Regions, accepting additional distance where the work doesn't require proximity to viewers.

1. **Serve viewers through regional caching:** Use a content delivery network and regional caching to deliver content close to viewers without replicating the full processing stack into every Region.

1. **Size multi-Region footprint to requirements:** Deploy to additional Regions only where a redundancy or latency requirement justifies the added footprint, rather than as a default.

1. **Review placement against per-Region carbon data:** Track compute hours by Region and transfer distance, and review against the per-Region monthly figures from the AWS Customer Carbon Footprint Tool to confirm placement decisions reduce emissions.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSUS02-BP01 Implement adaptive infrastructure scaling based on viewer patterns](smsus02-bp01.html)
+ [SMSUS06-BP01 Optimize data flow and caching strategies](smsus06-bp01.html)

**Related documents**
+ [Optimizing Streaming Media Workflows to Reduce Your Carbon Footprint, Part I](https://aws.amazon.com/blogs/media/optimizing-streaming-media-workflows-to-reduce-your-carbon-footprint-part-i/)
+ [Optimizing Streaming Media Workflows to Reduce Your Carbon Footprint, Part II, Codecs and Implementation](https://aws.amazon.com/blogs/media/optimizing-streaming-media-workflows-to-reduce-your-carbon-footprint-part-ii-codecs-and-implementation/)

**Related services**
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/)
+ [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)