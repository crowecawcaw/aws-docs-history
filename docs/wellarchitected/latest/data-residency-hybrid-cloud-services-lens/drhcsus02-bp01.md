# DRHCSUS02-BP01 When using Local Zones, monitor and scale your workloads to match demand, and use only the minimum required resources

Resources and services in AWS Local Zones, like those in AWS Regions, can be scaled dynamically to match measured demand,
minimizing energy consumption.

**Desired outcome:** The number and type of Amazon EC2 instances deployed will be optimized to support workload requirements while adhering to sustainability goals

**Benefits of establishing this best
practice:** Resource utilization can be reduced to
minimize energy consumption and support your sustainability
objectives.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Although Local Zones provide only a subset of the Amazon EC2
instance families and types available in an AWS Region, you
should still use AWS capabilities that support elasticity to
monitor and scale workloads to meet the measured demand and
improve sustainability.

Services such as
[Auto
Scaling groups](../../../autoscaling/ec2/userguide/auto-scaling-groups.md "../../../autoscaling/ec2/userguide/auto-scaling-groups.md"),
[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md"), and
[AWS Compute Optimizer](../../../compute-optimizer/latest/ug/what-is-compute-optimizer.md "../../../compute-optimizer/latest/ug/what-is-compute-optimizer.md") can be used to optimize the number and
sizes of EC2 instances to meet workload demands. For
[Amazon EKS](../../../eks/latest/userguide/what-is-eks.md "../../../eks/latest/userguide/what-is-eks.md") workloads, consider using
[Karpenter](https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/ "https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/")
to automatically scale Kubernetes clusters to match
instantaneous demand using instances aligned exactly to compute
demands. For more detail on scaling for sustainability, see
[SUS02-BP01
Scale workload infrastructure dynamically](../sustainability-pillar/sus_sus_user_a2.md "../sustainability-pillar/sus_sus_user_a2.md") and
[SUS02-BP03
Stop the creation and maintenance of unused assets](../sustainability-pillar/sus_sus_user_a4.md "../sustainability-pillar/sus_sus_user_a4.md")
_._
