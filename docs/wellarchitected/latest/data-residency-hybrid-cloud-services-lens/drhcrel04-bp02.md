# DRHCREL04-BP02 Implement proper monitoring and observability practices to track resource utilization, capacity availability, and application health

Plan and monitor AWS Outposts capacity proactively through
right-sizing, forecasting, and CloudWatch metrics to ensure
sufficient N+M capacity for high availability.

**Desired outcome:** Achieve
comprehensive observability over hybrid infrastructure and
applications, which provides efficient resource allocation, high
availability, and consistent adherence to data residency
requirements.

**Benefits of establishing this best
practice:** Following observability best practices
enables early detection of potential issues and high availability
across hybrid environments while maintaining data residency
compliance.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

AWS Outposts on-premises has finite capacity. For your workloads
to run with high availability, plan your compute and storage
capacity ahead of time. Some workloads can also require high
network bandwidth or packets per second, which would also
require planning to avoid bottlenecks. We recommend
right-sizing, benchmarking, and forecasting capacity ahead of
time. For guidance on monitoring Outposts capacity, see
[Monitoring
AWS Outposts capacity](https://aws.amazon.com/blogs/compute/monitoring-aws-outposts-capacity/ "https://aws.amazon.com/blogs/compute/monitoring-aws-outposts-capacity/").

AWS Cloud specialists and Support can assist with
right-sizing. The approaches for monitoring Local Zones are the
same as Availability Zones in the Region.

For high availability, you can provision additional built-in and
always-active capacity on Outposts Rack. Outpost capacity
configurations are designed to operate in production
environments and support N+M instances for each instance family,
where N is the required number of hosts and M is the number of
spare hosts provisioned to accommodate failures.

AWS recommends that you allocate sufficient additional capacity
for your mission-critical applications to enable recovery and
failover if there is an underlying host issue. As a result,
capacity planning is very important during the design process.
Similarly, it's important to have the right observability in
place to allow for fast failover across your resources. You can
use Amazon CloudWatch capacity availability metrics and set
alarms to monitor the health of your applications, create
CloudWatch actions to configure automatic recovery options, and
monitor the capacity utilization of your Outposts over time.

Due to the on-premises nature of Outposts, it is important to
monitor capacity utilization of both Amazon EC2 and Amazon EBS
resources across the Outposts to manage capacity, especially if
multiple teams are using the Outpost. In addition to the
individual resource level capacity CloudWatch metrics, Capacity
Exceptions are also populated and detailed in
[CloudWatch
metrics for AWS Outposts](../../../outposts/latest/userguide/outposts-cloudwatch-metrics.md "../../../outposts/latest/userguide/outposts-cloudwatch-metrics.md").

CloudWatch dashboards are customizable home pages in the
CloudWatch console that you can use to monitor your resources in
a single view. These dashboards are useful for regular reviews
of metrics (for example, weekly) to review trends, which is a
best practice highlighted in the
[Well
Architected Framework's Operational Excellence Pillar](../operational-excellence-pillar/ops_evolve_ops_metrics_review.md "../operational-excellence-pillar/ops_evolve_ops_metrics_review.md").
For an Outposts-specific CloudWatch dashboard, see
[Deploying
an automated Amazon CloudWatch dashboard for AWS Outposts using
AWS CDK](https://aws.amazon.com/blogs/compute/deploying-an-automated-amazon-cloudwatch-dashboard-for-aws-outposts-using-aws-cdk/ "https://aws.amazon.com/blogs/compute/deploying-an-automated-amazon-cloudwatch-dashboard-for-aws-outposts-using-aws-cdk/").
