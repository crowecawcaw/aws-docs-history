# EC2-Instances (Elastic Compute Cloud) resource-level

data at hourly granularity

In Cost Explorer, you can enable EC2 resource-level data at hourly granularity
for the past 14 days. Using this data, you can view your hourly cost and usage at
each EC2 instance level in Cost Explorer. This helps you to understand cost and
usage driven by each EC2 instance by grouping on resource and filtering your
Cost Explorer view for the EC2 service.

Such data can help you analyze for variances or anomalies. For example, if you see
a spike in your EC2 cost, you can use hourly granularity to pinpoint the hour when
the variance started, and then group your cost by resource to understand which
specific EC2 instance is causing the spike. The ability to identify the source of
variance to the exact hour can help your developers understand which specific
changes in their architecture caused this variance, or if this is an actual anomaly
or valid spike due to increased traffic. If you’re thinking about how many EC2
Reserved Instances you should buy, understanding the number and type of instances
running each hour can be useful, as you can make an informed decision to ensure you
get the maximum Reserved Instances utilization. If you currently have Savings Plans or
Reserved Instances, enable EC2 resource-level data at hourly granularity to
understand which specific instances used your Savings Plans or Reserved Instances.

Once enabled, EC2 resource-level data at hourly granularity is available within 48
hours. This data is not available for Savings Plans and Reservations utilization and
coverage reports.
