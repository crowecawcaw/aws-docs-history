

# SMSUS07-BP01 use energy-efficient computing resources
<a name="smsus07-bp01"></a>

Run each streaming workload on the most energy-efficient hardware that can do the job. Media processing is compute-intensive, so the processor family, accelerator, and instance type you select directly determine how much energy a given amount of transcoding, inference, or delivery work consumes.

**Desired outcome:**
+ General-purpose and media-processing workloads run on the most efficient processor family that supports them.
+ Specialized work uses purpose-built hardware such as media-processing services and machine learning (ML) accelerators rather than general-purpose compute.
+ Interruption-tolerant batch work runs on spare, already-provisioned capacity rather than dedicated persistent instances.

**Common anti-patterns:**
+ Running media and general-purpose workloads on older or default instance families when a more efficient processor family would run them with no functional change.
+ Building and operating self-managed transcoding on general-purpose compute instead of using purpose-built media services, paying a higher energy cost for the same output.
+ Running machine learning inference and training on general-purpose instances rather than purpose-built accelerators.
+ Over-allocating graphics processing units (GPUs) to transcoding tasks that don't need them, leaving expensive, power-hungry hardware underused.

**Benefits of establishing this best practice:**
+ Lower energy per unit of work, because workloads run on processors with higher performance per watt.
+ Reduced resource consumption for specialized tasks, because purpose-built hardware does the same work more efficiently than general-purpose compute.
+ Higher utilization of already-provisioned capacity, because interruption-tolerant batch runs on spare capacity rather than dedicated instances.
+ Adoption of future efficiency gains, because workloads designed to move across instance families can take up newer, more efficient generations as they ship.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Hardware selection is one of the most direct sustainability levers available, because the same workload run on a more efficient processor consumes less energy for the same output. AWS Graviton processors deliver higher performance per watt than comparable x86 families for many media and general-purpose workloads, so moving eligible workloads to Graviton reduces energy intensity without changing what the workload does. Porting effort is the main consideration. Interpreted and just-in-time (JIT) compiled runtimes move without change, while media libraries may carry processor-specific assumptions that need validation. Prioritize the largest, longest-running workloads where the efficiency gain repays the testing.

Self-managed transcoding on general-purpose compute does the same job as a purpose-built media service but at a higher energy cost, because the managed service runs on hardware and software optimized for the task. The same logic applies to machine learning. Inference and training on purpose-built accelerators consume far less energy than the equivalent work on general-purpose instances. GPUs are powerful but power-hungry, so reserve them for tasks that genuinely benefit and right-size their allocation rather than defaulting to them for transcoding that a more efficient path can handle.

Interruption-tolerant batch work such as overnight transcoding, catalog re-encodes, and analytics can run on spare capacity that is already provisioned and powered, rather than triggering dedicated persistent instances. This ties efficiency directly to utilization. Energy use isn't measurable per task, so use resource proxies such as compute hours by instance family and the share of work on efficient processors and accelerators. Read account-level carbon impact per Region from the AWS Customer Carbon Footprint Tool, which publishes monthly.

### Implementation steps
<a name="implementation-steps"></a>

1. **Migrate eligible workloads to Graviton:** Validate media-processing and general-purpose workloads on AWS Graviton instances and move those that pass, prioritizing the largest and longest-running workloads where the performance-per-watt gain repays the porting effort.

1. **Use purpose-built media services for transcoding:** Run file-based and live transcoding on AWS Elemental services rather than self-managed encoding on general-purpose compute, so the work runs on hardware optimized for it.

1. **Run ML on purpose-built accelerators:** Use AWS Inferentia for inference and AWS Trainium for training on machine learning workloads such as the following, instead of general-purpose instances.
+ Recommendation
+ Content analysis
+ Moderation

1. **Right-size GPU and accelerator usage:** Allocate GPUs only to tasks that benefit from them, and size the allocation to the workload so power-hungry accelerators are not left underused.

1. **Run interruption-tolerant batch on spare capacity:** Schedule overnight transcoding, catalog re-encodes, and similar batch work on Amazon EC2 Spot capacity so it draws from already-provisioned resources rather than dedicated persistent instances.

1. **Measure hardware efficiency:** Track compute hours by instance family and the proportion of work running on efficient processors and accelerators, and review against the monthly account-level figures from the AWS Customer Carbon Footprint Tool.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSUS02-BP01 Implement adaptive infrastructure scaling based on viewer patterns](smsus02-bp01.html)
+ [SMSUS08-BP01 Leverage AWS managed services for efficient resource utilization](smsus08-bp01.html)

**Related documents**
+ [Optimizing Streaming Media Workflows to Reduce Your Carbon Footprint, Part II, Codecs and Implementation](https://aws.amazon.com/blogs/media/optimizing-streaming-media-workflows-to-reduce-your-carbon-footprint-part-ii-codecs-and-implementation/)
+ [Sustainability Pillar, Hardware and services](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/hardware-and-services.html)

**Related services**
+ [AWS Graviton](https://aws.amazon.com/ec2/graviton/)
+ [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/)
+ [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/)