# MIDASUS05-BP01 Implement optimized compute, storage and networking hardware

Manufacturing workloads have diverse requirements - from compute intensive simulations,
storage to real time shop floor systems. Choosing the right hardware architecture and service
models helps minimize environmental impact while meeting manufacturing performance
demands.

**Desired outcome:** Manufacturing workloads running on optimally sized and energy-efficient infrastructure
that minimizes waste and carbon footprint while meeting performance requirements for critical
operations, resulting in quantifiable sustainability improvements without compromising
production reliability.

**Benefits of establishing this best practice:**

1. Reduced energy consumption and carbon emissions through removal of over provisioning
   and inefficient hardware choices.
2. Lower operational costs through optimized resource utilization.
3. Improved sustainability reporting metrics that demonstrate concrete steps toward
   environmental goals without sacrificing manufacturing performance.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Analyze hardware requirements for manufacturing workloads including PLM (Product
Lifecycle Management), MES (Manufacturing Execution Systems), and ERP (Enterprise
Resource Planning) applications based on vendor specifications and performance needs,
selecting minimal resources necessary to meet functional requirements.

Implement right sizing strategies for all compute resources supporting
manufacturing operations, verifying that production systems use the most efficient
configurations based on actual workload demands rather than over-provisioned
specifications.

Deploy storage tiering mechanisms to align manufacturing data accessibility
requirements with appropriate storage technologies, moving infrequently accessed
historical production data to more energy efficient storage options.

Use hardware sharing approaches where possible across manufacturing systems to
increase utilization rates of deployed resources, improving efficiency through
consolidated infrastructure and reducing the total environmental footprint.

### Implementation steps

**Manufacturing application resource assessment:**

- Conduct workload profiling of PLM, MES, and ERP systems using AWS Compute Optimizer to identify optimization opportunities
- Implement instance rightsizing recommendations, prioritizing Graviton based instances for better performance and efficiency

**Business application resource scheduling:**

- Configure Amazon EC2 Auto Scaling with scheduled actions aligned to manufacturing business hours and usage patterns
- Implement hibernation policies for non-production environments during off-hours to reduce idle resource consumption

**Manufacturing data storage tiering:**

- Configure Amazon S3 Lifecycle policies to automatically transition production data to appropriate storage classes based on access patterns
- Implement intelligent tiering for files, documentation, and historical manufacturing data to optimize storage costs and efficiency

**Engineering workload optimization:**

- Deploy AWS Batch for compute-intensive manufacturing simulations with job queuing that maximizes resource utilization
- Deploy AWS ParallelCluster for high performance computing needs like CFD, FEA, and engineering simulations

**Edge computing optimization:**

- Deploy AWS IoT Greengrass for local processing of shop floor data to minimize unnecessary data transfer

## Key AWS services

- AWS Compute Optimizer
- AWS Graviton processors
- AWS IoT Greengrass
- AWS Batch
- AWS ParallelCluster
- Amazon EC2 Auto Scaling
- Amazon S3

## Resources

- [AWS Compute Optimizer](../../../compute-optimizer/latest/ug/what-is-compute-optimizer.md "../../../compute-optimizer/latest/ug/what-is-compute-optimizer.md")
- [AWS Graviton Processors](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/")
- [AWS IoT Greengrass](../../../greengrass/v2/developerguide/what-is-iot-greengrass.md "../../../greengrass/v2/developerguide/what-is-iot-greengrass.md")
- [AWS Batch](../../../batch/latest/userguide/what-is-batch.md "../../../batch/latest/userguide/what-is-batch.md")
- [High-Performance Computing with AWS ParallelCluster](../../../parallelcluster/latest/ug/what-is-aws-parallelcluster.md "../../../parallelcluster/latest/ug/what-is-aws-parallelcluster.md")
