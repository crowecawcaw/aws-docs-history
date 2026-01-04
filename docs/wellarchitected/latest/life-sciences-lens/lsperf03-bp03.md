# LSPERF03-BP03 Tailored service configuration by use

case

Customize infrastructure and service configurations to align with
the specific requirements of each workload category. Fine-tune
compute, storage, and networking parameters for research
environments to maximize throughput and processing efficiency, while
configuring clinical environments with emphasis on consistent
performance, redundancy, and predictable behavior under each
condition.

**Desired outcome:** Implement
tailored infrastructure configurations that precisely match the
unique requirements of research and clinical workloads.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Customizing infrastructure and service configurations for
different workload categories is essential for optimizing both
performance and cost efficiency in generative AI deployments.
Begin by conducting a detailed workload assessment using AWS Well-Architected Tool with the
[Generative
AI Lens](https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/generative-ai-lens/generative-ai-lens.json "https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/generative-ai-lens/generative-ai-lens.json") to identify the specific requirements and
characteristics of each workload category. This assessment
establishes clear performance targets, reliability requirements,
and cost constraints that will guide your configuration decisions.

For research environments focused on model development and
experimentation, prioritize compute flexibility and processing
efficiency. Configure Amazon EC2 instances with the latest
generation of accelerators like AWS Trainium for training
workloads. Implement Amazon FSx for Lustre configured with high
throughput capabilities to support efficient data processing
during training. Use Amazon SageMaker AI with managed spot training
to reduce costs for non-time-sensitive workloads while maintaining
the ability to scale compute resources during intensive
experimentation phases.

For clinical or production environments where consistent
performance is critical, implement multi-AZ deployments across
infrastructure components using AWS CloudFormation or AWS CDK.
Configure Amazon RDS with multi-AZ deployments and provisioned
IOPS for consistent database performance. Implement Amazon ElastiCache with reserved nodes to provide stable, predictable
caching performance. Deploy inference endpoints using Amazon SageMaker AI with auto scaling configured based on predictable
traffic patterns rather than reactive scaling, providing
consistent latency even during traffic variations.

Tailor networking configurations to each environment's specific
needs using advanced VPC features. For research environments,
implement AWS Transit Gateway with increased bandwidth allocations
to support large data transfers. For clinical environments,
implement AWS Global Accelerator to provide consistent network
performance and AWS Shield Advanced for enhanced protection
against availability-impacting events.

Implement comprehensive monitoring tailored to each environment
using Amazon CloudWatch with custom metrics and dashboards. For
research environments, focus monitoring on resource utilization
and throughput metrics. For clinical environments, prioritize
monitoring of latency percentiles, error rates, and availability
metrics with automated alerting through Amazon SNS when
performance deviates from established baselines.

### Implementation steps

1. Assess workloads using AWS Well-Architected Tool.
2. Deploy research models on SageMaker AI with spot instances.
3. Configure clinical systems with Multi-AZ architecture.
4. Implement FSx for Lustre for high-throughput processing.
5. Create CloudWatch dashboards for environment monitoring.
