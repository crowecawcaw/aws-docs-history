# DRHCPERF04-BP01 Establish hybrid edge workload health KPIs

Demonstrate your workload is meeting your business requirements.

**Desired outcome:** You can
illustrate you are meeting your business requirements for the
workload.

**Benefits of establishing this best
practice:** Metrics can provide data for continuous
workload improvement.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

You should develop
[key
performance indicators (KPIs)](https://aws.amazon.com/blogs/mt/the-importance-of-key-performance-indicators-kpis-for-large-scale-cloud-migrations/ "https://aws.amazon.com/blogs/mt/the-importance-of-key-performance-indicators-kpis-for-large-scale-cloud-migrations/") to show how effectively
you're achieving objectives applicable to your workload.
[AWS Outposts](../../../outposts/latest/userguide/outposts-cloudwatch-metrics.md "../../../outposts/latest/userguide/outposts-cloudwatch-metrics.md") has additional metrics that should be monitored.
Determine the application KPI's to monitor to provide the
optimal user experience.

Instrument your code using a tool such as
[AWS X-Ray](https://aws.amazon.com/xray/ "https://aws.amazon.com/xray/"), and use
[Amazon CloudWatch](../../../outposts/latest/userguide/outposts-cloudwatch-metrics.md "../../../outposts/latest/userguide/outposts-cloudwatch-metrics.md") to monitor in-Region dependencies. You should
monitor service link
[bandwidth
and round trip latency](../../../outposts/latest/userguide/region-connectivity.md#sl-bandwidth-recommendations "../../../outposts/latest/userguide/region-connectivity.md#sl-bandwidth-recommendations") to provide optimal performance.
Hybrid edge services must meet unique minimum requirements as
defined in the User Guide for Outposts racks and
[servers](../../../outposts/latest/server-userguide/region-connectivity.md "../../../outposts/latest/server-userguide/region-connectivity.md").
