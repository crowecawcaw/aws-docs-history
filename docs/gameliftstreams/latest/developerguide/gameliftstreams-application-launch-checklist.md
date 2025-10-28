# Amazon GameLift Streams launch checklist

Preparing for a successful launch on Amazon GameLift Streams involves planning and coordination. Follow this detailed checklist to ensure a smooth
experience in the weeks leading up to your event.

## Notify the Amazon GameLift Streams team

**Action:** At least 8 weeks in advance, inform your technical account manager, your account team, or
your account solution architect about your launch timeline and expected peak concurrent streams.

**Reason:** Understanding the scale of your production workload helps us ensure that your service limits
are adequate, and adjust them if necessary. We also provide guidance on capacity availability and recommendations for the launch.

## Compatibility and performance testing

**Action:** Test your application at scale, and in all of the locations where you have capacity, to confirm
a positive customer experience. Amazon GameLift Streams offers NVIDIA based stream classes with different levels of performance and runtimes
supported.

**Reason:** Thorough testing helps identify and resolve any potential compatibility and performance issues
before the launch. Keep in mind the following about stream classes:

- The "high" stream classes support multi-tenancy, allowing two applications to run concurrently on a single instance. If you're
  using the "high" stream class, test with at least 2 concurrent streams to see how your application performs with shared resources,
  such as the CPU, GPU, and memory.

## Capacity reservation

**Action:** At least 8 weeks before launch, reach out to your account team to reserve capacity, especially
if you anticipate a critical, large-scale need. Decide on the stream classes and streaming locations based on your compatibility testing,
performance requirements, and budget. Provide the start/end times and the required capacity. AWS requires that all capacity reservations
be finalized 6-8 weeks before the reservation need-by date.

**Reason:** Amazon GameLift Streams operates on a first-come, first-serve basis using on-demand capacity. Reservations are
essential to guarantee the necessary capacity.

## Performance testing at scale

**Action:** Conduct thorough load testing of your APIs and your Amazon GameLift Streams configurations to observe its
performance under load (latency, resolution, and frame rate). Be sure to check the [Amazon GameLift Streams API rate limits](api-rate-limits.md "api-rate-limits.md") to ensure that you have sufficient headroom for your launch and beyond. If you believe you will need
a limit increase, you should reach out to your account manager or submit a support ticket.

**Reason:** Load-testing reveals how your application and Amazon GameLift Streams configurations will perform under stress
before the launch. This is crucial to ensure smooth performance at scale.

## Pre-launch setup

**Action:** At least 2-3 days before launch, create your final application resources and stream groups.
Validate streaming performance and scale up capacity as needed.

**Reason:** This ensures that all components are working as expected, minimizing the risk of unexpected
issues and allowing for easier diagnosis and recovery during the event.

## Additional tips

- **Consistency is key**: Using the same existing stream groups throughout a launch event maintains
  consistency in the Amazon GameLift Streams backend, simplifying troubleshooting.
- **Monitor closely**: Closely monitor performance and user feedback to quickly address any issues.
  Build an operational dashboard. Monitor stream capacity, usage, and performance using Amazon CloudWatch (see [Monitor with CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md") for details). Refer to the [Well-Architected
  Framework](../../../wellarchitected/latest/operational-excellence-pillar/welcome.md "../../../wellarchitected/latest/operational-excellence-pillar/welcome.md") for additional guidance.

## Need Further Assistance?

If you have any questions or require further support, don't hesitate to reach out to us at [Amazon GameLift Streams support](mailto:gamelift-streams-support@amazon.com "mailto:gamelift-streams-support@amazon.com"). We're here to
help ensure your launch is successful and seamless.
