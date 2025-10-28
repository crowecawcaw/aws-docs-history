# Best practice 11.2 – Plan and provision capacity for predictable workload usage

For well-defined workloads, planning capacity ahead based on
average usage pattern helps improve resource utilization and
avoid over provisioning. For a spiky workload, set up
automatic scaling to meet user and workload demand.

## Suggestion 11.2.1 – Choose the right instance type based on workload pattern and growth ratio

Consider resource needs, such as CPU, memory, and
networking that meet the performance requirements of your
workload. Choose the right instance type and avoid
overprovisioning. An optimized EC2 instance runs your
workloads with optimal performance and infrastructure
cost. For example, choose the smaller instance if your
growth ratio is low as this allows more granular
incremental change.

## Suggestion 11.2.2 – Choose the right sizing based on average or medium workload usage

Right sizing is the process of matching instance types and
sizes to your workload performance and capacity
requirements at the lowest possible cost. It’s also the
process of looking at deployed instances and identifying
opportunities to downsize without compromising capacity or
other requirements that will result in lower costs.

## Suggestion 11.2.3 – Use automatic scaling capability to meet the peak demand instead of over provisioning

Analytics services can scale dynamically to meet demand. Then, after the demand has dropped below a certain threshold, the service will remove the resources that are no longer needed. The automatic scaling of serverless services enables applications to handle sudden traffic spikes without capacity planning, reducing costs and improving availability.

There are a number of services that can automatically scale, and other services that you need to configure the scaling for. For example, AWS services like Amazon EMR, AWS Glue, and Amazon Kinesis can auto-scale seamlessly in response to usage spikes and remove resources without any configuration.
