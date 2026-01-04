# LSPERF03-BP02 Environment isolation by workload

type

Implement clear separation between research and clinical
environments based on their fundamentally different requirements.
Establish a dedicated infrastructure for computationally-intensive
research pipelines with burst capacity for parallel processing,
while maintaining separate, highly-available environments for
clinical applications where consistency and reliability are
paramount.

**Desired outcome:** Create distinct
infrastructure environments optimized for the unique requirements of
research computing and clinical applications.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing clear separation between research and clinical
environments is essential for organizations working with
generative AI in healthcare and life sciences. Begin by
establishing distinct AWS accounts for each environment using AWS Organizations with service control policies (SCPs) that enforce
appropriate guardrails. This separation creates natural boundaries
for access controls, resource allocation, and regulatory
requirements while still enabling cross-account data sharing when
necessary through services like AWS RAM.

For research environments, prioritize flexibility and
computational power by implementing Amazon SageMaker AI with its
comprehensive ML development capabilities. Configure auto scaling
compute resources using Amazon EC2 Auto Scaling groups with
GPU-accelerated instances like P4d or G5g to support
computationally intensive workloads. Implement AWS Batch for
efficiently managing parallel processing jobs with spot instances
to optimize costs during model training and experimentation
phases. This approach provides researchers with the burst capacity
needed for iterative development while maintaining cost
efficiency.

For clinical environments, focus on high availability and
consistency by deploying infrastructure across multiple
Availability Zones using AWS CloudFormation or AWS CDK with
immutable patterns. Implement Amazon RDS multi-AZ deployments for
database reliability and Amazon ElastiCache for consistent
performance. Configure detailed monitoring with Amazon CloudWatch
and AWS X-Ray for predictable performance characteristics critical
for clinical applications. Implement AWS Config rules to enforce
configuration adherence with regulatory requirements like HIPAA or
GxP.

Establish controlled pathways for promoting validated models from
research to clinical environments using AWS CodePipeline with
approval gates and validation tests. Store model artifacts in
Amazon S3 with versioning enabled and implement AWS Lambda
functions to validate model metadata before clinical deployment.
Use Service Catalog to create standardized, pre-approved
deployment patterns that clinical teams can use without
compromising governance requirements.

### Implementation steps

1. Create account separation using AWS Organizations.
2. Deploy research workloads on SageMaker AI with GPU instances.
3. Build clinical systems with Multi-AZ RDS deployments.
4. Implement CodePipeline for controlled model promotion.
5. Configure CloudWatch dashboards for environment monitoring.
