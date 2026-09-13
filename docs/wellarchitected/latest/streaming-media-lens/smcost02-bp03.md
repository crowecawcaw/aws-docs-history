

# SMCOST02-BP03 Optimize AWS Elemental Media Services pricing models
<a name="smcost02-bp03"></a>

AWS Elemental Media Services offer multiple pricing models that deliver significant savings over on-demand rates when matched to appropriate workload patterns. Organizations that run all workloads at on-demand rates without evaluating reservations, tier selection, or infrastructure lifecycle management leave substantial savings unrealized. Selecting the right pricing model for each workload pattern requires understanding usage characteristics and commitment trade-offs.

**Desired outcome:**
+ You have matched each media processing workload to the pricing model that delivers the lowest total cost for its usage pattern.
+ You have reserved capacity only for workloads with consistent utilization that exceeds the break-even threshold, and use on-demand for variable or unpredictable workloads.
+ You have infrastructure lifecycle automation that deploys and destroys event-based streaming resources so you pay only for active event time.

**Common anti-patterns:**
+ Running persistent live channels at on-demand rates without evaluating whether reservation pricing would reduce costs for predictable workloads.
+ Purchasing reservations without analyzing historical channel usage, resulting in reserved capacity that sits idle below the break-even utilization threshold.
+ Using Professional tier transcoding features for jobs that don't require them, paying higher per-minute rates for capabilities that produce no quality benefit for that content.
+ Leaving event-based live streaming infrastructure running after events conclude, paying for idle channels, inputs, and endpoints between events.

**Benefits of establishing this best practice:**
+ Encoding costs for predictable workloads decrease because term commitments provide lower rates than on-demand pricing for channels that run consistently.
+ Transcoding costs decrease for standard content because Standard tier pricing applies to jobs that don't require Professional tier features.
+ Event-based streaming costs match actual event duration because infrastructure exists only while the event is live.
+ Budget predictability improves because reserved capacity has a known monthly cost regardless of usage fluctuations.

**Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

Three services dominate media processing costs: MediaLive for live encoding, MediaConvert for file-based transcoding, and MediaPackage for packaging and origination. Each has distinct pricing models with different commitment and utilization trade-offs. Applying the wrong model to a workload either leaves savings unrealized (on-demand for steady-state) or creates waste (reservations for sporadic usage).

MediaLive charges based on channel state (running or idle), input characteristics, and output characteristics. A channel that runs 24x7 at on-demand rates accumulates the highest possible cost for that configuration. A one-year reservation for the same channel configuration provides a discounted hourly rate. The break-even point depends on the specific channel configuration, but reservations typically become cost-effective when a channel runs more than 40-60% of the term duration. Channels that run less than that cost more under a reservation than on-demand because you pay the reservation rate whether the channel runs or not.

MediaLive also offers single-pipeline channels. Standard channels run dual pipelines for pipeline-level redundancy. Workloads that don't require this redundancy (development environments, non-critical streams, or workloads with application-level failover) can run single-pipeline at roughly half the cost. Input switching on a single channel can also reduce costs by consolidating scheduled content that would otherwise require multiple running channels.

MediaConvert uses a per-minute output pricing model with two tiers. Standard tier covers the majority of transcoding needs at base rates. Professional tier applies automatically when jobs use premium features (accelerated transcoding, Dolby audio processing, XAVC codec). Jobs that use Professional tier features pay a higher per-minute rate for all outputs in that job. Auditing job templates to identify which jobs genuinely require Professional tier features and which can use Standard tier removes unnecessary cost uplift. Reserved transcoding slots offer an alternative model: fixed monthly capacity for high-volume steady-state transcoding where per-minute billing would exceed the reservation cost.

Event-based live streaming (concerts, sporting events, product launches) has a fundamentally different cost profile than persistent channels. The infrastructure is needed for hours or days, not months. Deploying the full stack (MediaLive channel, MediaPackage channel, CloudFront distribution) through infrastructure as code and destroying it after the event means you pay only for the active streaming period. The operational overhead of stack creation and deletion is minimal compared to the cost of idle infrastructure between events.

### Implementation steps
<a name="implementation-steps"></a>

1. **Analyze historical MediaLive channel utilization:** Review channel runtime data over three to six months in [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html). Identify channels that run consistently (24x7 or on a recurring schedule) compared to channels with sporadic or event-driven usage. Calculate monthly runtime hours for each channel configuration.

1. **Calculate reservation break-even and purchase for qualifying channels:** Determine the utilization percentage at which the reservation hourly rate multiplied by total term hours equals the on-demand rate multiplied by expected runtime hours. Purchase [MediaLive reservations](https://docs.aws.amazon.com/medialive/latest/ug/reservations.html) for channels that exceed the break-even threshold. Reserve only baseline capacity and keep burst capacity on-demand.

1. **Evaluate single-pipeline channels for non-critical workloads:** Identify channels where pipeline-level redundancy isn't required:
+ Development
+ Testing
+ Non-production preview streams
+ Workloads with application-level redundancy

Reconfigure these as [single-pipeline channels](https://docs.aws.amazon.com/medialive/latest/ug/channel-class.html) to reduce input and output charges.

1. **Audit MediaConvert job templates for tier optimization:** Review your [MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html) job templates and identify the features that trigger Professional tier pricing. For jobs that don't use accelerated transcoding, Dolby audio, or other Professional tier features, verify they are running at Standard tier rates. Remove unused Professional tier feature configurations from templates where the output quality doesn't benefit.

1. **Implement event-based infrastructure lifecycle:** Create [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) templates or CDK constructs for your live streaming stack. Deploy the stack before an event, configure it, stream for the event duration, then delete the stack after the event concludes. Automate deployment and teardown with scheduling if events are recurring and predictable.

1. **Monitor reservation utilization and set expiration alerts:** Track reserved channel utilization in [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html). Set alarms for sustained under-utilization that indicates the reservation isn't cost-effective. Configure calendar reminders 60 days before reservation expiration to evaluate renewal based on current and projected usage patterns.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMCOST02-BP01 Establish baseline metrics for media processing tasks](smcost02-bp01.html)
+ [SMCOST02-BP02 Implement parallel processing for media tasks](smcost02-bp02.html)

**Related documents**
+ [Pricing and reservations in MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/pricing-and-reservations.html)
+ [AWS Elemental MediaConvert pricing](https://aws.amazon.com/mediaconvert/pricing/)
+ [AWS Elemental MediaLive pricing](https://aws.amazon.com/medialive/pricing/)

**Related examples**
+ [Live Streaming on AWS](https://aws.amazon.com/solutions/implementations/live-streaming-on-aws/)

**Related services**
+ [AWS Elemental MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/what-is.html)
+ [AWS Elemental MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html)
+ [AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/what-is.html)
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)