# DRHCSUS03-BP01 Monitor workload and component resource utilization to identify any that are unneeded or over-provisioned when using Local Zones

Monitoring workload utilization is critical to identifying those
which are overprovisioned and can be scaled down to reduce energy
consumption.

**Desired outcome:** Workloads are
deployed on Amazon EC2 instances that are aligned to requirements
and provide optimal performance.

**Benefits of establishing this best
practice:** Workloads and resources which are
overprovisioned can be scaled down to reduce energy consumption
and support sustainability objectives.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Monitor and capture workload metrics such as CPU utilization,
memory utilization, network connections, and network throughput
using
[Amazon CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") to identify workloads or components
that are no longer used or are under-utilized. Routinely review
the recommendations made by
[AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/") to identify instances that have been
over-provisioned, and adjust as necessary to match instance type
and size to the workload requirements. With AWS Local Zones, it
is possible to maximize sustainability by using the large
variety of Amazon EC2 instances to match resource consumption to
workload requirements.
