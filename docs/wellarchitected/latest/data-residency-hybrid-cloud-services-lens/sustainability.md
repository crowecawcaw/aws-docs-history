# Sustainability

The sustainability pillar includes the ability to deliver business
value while minimizing resource usage, environmental impacts, and
energy consumption. This section provides you with an overview of
sustainability design principles, best
practices, and questions. You can find implementation
guidance in the
[Sustainability
Pillar whitepaper](../sustainability-pillar/sustainability-pillar.md "../sustainability-pillar/sustainability-pillar.md").

## Definitions

This whitepaper covers sustainability in the cloud, describing best practices in the following areas:

- Region selection
- Alignment to demand
- Software and architecture patterns
- Data management
- Hardware and services

## Design principles

The Well-Architected Framework identifies a set of general design
principles to facilitate sustainability while deploying hybrid
services and workloads:

- **Consider workload
  placement:** It is always a best practice to use AWS Regions when building workloads, as Regions offer tools for
  managing service and instance elasticity. If a workload has
  latency or data residency requirements that cannot be
  addressed in a Region, consider using an AWS Local Zone where
  workload elasticity is still easily achieved with Amazon EC2.
  If a Local Zone cannot meet workload requirements, consider
  using AWS Outposts, where capacity must be more precisely
  matched with requirements.
- **Characterize workload
  requirements:** Before using AWS hybrid services,
  fully assess and understand your workload resource
  requirements. Always engage an AWS migration specialist, and
  use the AWS Migration Evaluator to capture workload resource
  utilization to make a data-driven decision on which hybrid
  services to use and how much capacity to deploy.
- **Match EC2 instance size to measured
  load:** Use tools such as Amazon CloudWatch and AWS Compute Optimizer to track EC2 instance resource utilization
  and right-size instances based on data-driven recommendations.
