

# DRHCPERF04-BP01 Establish hybrid edge workload health KPIs
<a name="drhcperf04-bp01"></a>

 Demonstrate your workload is meeting your business requirements. 

 **Desired outcome:** You can illustrate you are meeting your business requirements for the workload. 

 **Benefits of establishing this best practice:** Metrics can provide data for continuous workload improvement. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-46"></a>

 You should develop [key performance indicators (KPIs)](https://aws.amazon.com/blogs/mt/the-importance-of-key-performance-indicators-kpis-for-large-scale-cloud-migrations/) to show how effectively you're achieving objectives applicable to your workload. [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-cloudwatch-metrics.html) has additional metrics that should be monitored. Determine the application KPI's to monitor to provide the optimal user experience. 

 Instrument your code using a tool such as [AWS X-Ray](https://aws.amazon.com/xray/), and use [Amazon CloudWatch](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-cloudwatch-metrics.html) to monitor in-Region dependencies. You should monitor service link [bandwidth and round trip latency](https://docs.aws.amazon.com/outposts/latest/userguide/region-connectivity.html#sl-bandwidth-recommendations) to provide optimal performance. Hybrid edge services must meet unique minimum requirements as defined in the User Guide for Outposts racks and [servers](https://docs.aws.amazon.com/outposts/latest/server-userguide/region-connectivity.html). 