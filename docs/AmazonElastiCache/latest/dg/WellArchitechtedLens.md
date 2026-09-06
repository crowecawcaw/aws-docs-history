

# Using the Amazon ElastiCache Well-Architected Lens
<a name="WellArchitechtedLens"></a>

This section describes the Amazon ElastiCache Well-Architected Lens, a collection of design principles and guidance for designing well-architected ElastiCache workloads.
+ The ElastiCache Lens is additive to the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).
+ Each Pillar has a set of questions to help start the discussion around an ElastiCache Architecture.
  + Each question has a number of leading practices along with their scores for reporting.
    + *Required* - Necessary before going to prod (absent being a high risk)
    + *Best* - Best possible state a customer could be
    + *Good* - What we recommend customers to have (absent being a medium risk)
+ Well-Architected terminology
  + [Component](https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.html) – Code, configuration and AWS Resources that together deliver against a requirement. Components interact with other components, and often equate to a service in microservice architectures.
  + [Workload](https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.html) - A set of components that together deliver business value. Examples of workloads are marketing websites, e-commerce websites, the back-ends for a mobile app, analytic platforms, etc.

**Note**  
This guide has not been updated to include information on ElastiCache serverless caching and the new Valkey engine.

**Topics**
+ [Amazon ElastiCache Well-Architected Lens Operational Excellence Pillar](OperationalExcellencePillar.md)
+ [Amazon ElastiCache Well-Architected Lens Security Pillar](SecurityPillar.md)
+ [Amazon ElastiCache Well-Architected Lens Reliability Pillar](ReliabilityPillar.md)
+ [Amazon ElastiCache Well-Architected Lens Performance Efficiency Pillar](PerformanceEfficiencyPillar.md)
+ [Amazon ElastiCache Well-Architected Lens Cost Optimization Pillar](CostOptimizationPillar.md)