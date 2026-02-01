# DSPERF01-BP02 Optimize applications while maintaining data

sovereignty

Maintaining data sovereignty while optimizing application
performance is crucial for compliance and operational efficiency. By
minimizing external data transfers and processing data within the
cloud, organizations can reduce their compliance footprint and
third-party dependencies. This approach improves adherence to strict
data governance requirements while maintaining optimal performance
and simplified auditability.

**Desired outcome:** Deliver
high-performance applications using cloud-based optimization
services. Maintain data sovereignty by removing external service
dependencies.

**Common anti-patterns:**

- Over-relying on external CDNs, third-party optimization
  services, or APIs that require data to leave the controlled AWS
  environment.
- Implementing synchronous processing patterns instead of
  optimizing through asynchronous workflows and queuing
  mechanisms.
- Neglecting application-level caching strategies and efficient
  database query optimization.
- Using inefficient serialization formats and failing to implement
  compression for internal data transfers.
- Deploying monolithic architectures that block granular scaling
  and optimization of individual components.
- Failing to implement connection pooling, resource reuse
  patterns, and parallel processing opportunities.
- Storing sensitive data in unencrypted logs.
- Over-provisioning resources instead of optimizing code
  efficiency.

**Benefits of establishing this best
practice:**

- Improved regulatory adherence and data privacy by keeping the
  optimization processes and data within the controlled AWS
  environments.
- Improved application performance and reduced latency through
  strategic caching, compression, and resource optimization
  techniques.
- Reduced operational costs and risks by lowering dependencies on
  external services, minimizing data egress fees, and optimizing
  resource utilization.
- Increased system reliability and security posture by maintaining
  complete control over data flow and processing locations.
- Simplified audit trails and compliance verification with AWS
  tools.
- Greater scalability and flexibility through AWS service
  integration and auto scaling capabilities.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Optimize applications through internal caching, compression,
asynchronous processing, and intelligent resource management,
while maintaining data within controlled boundaries. Implement
multi-layered optimization strategies using AWS services for
compute, storage, and data processing, with data isolation
implemented through encryption and VPC controls.

Key implementation components:

- Deploy comprehensive caching strategies using Amazon ElastiCache and application-level caches
- Optimize database performance through connection pooling and
  query optimization with Amazon DynamoDB
- Implement asynchronous processing using AWS Lambda and
  messaging services
- Configure auto scaling and container orchestration for dynamic
  resource optimization
- Use Amazon S3 for internal data storage with AWS KMS
  encryption
- Use VPC controls and network isolation for secure data
  processing
- Refactor applications to remove external service dependencies
  and APIs
- Implement serverless architectures for event-driven
  optimizations within VPC boundaries

### Implementation steps

1. Deploy comprehensive caching using
   [Amazon ElastiCache](../../../elasticache.md "../../../elasticache.md") and
   [DynamoDB
   Accelerator (DAX)](../../../amazondynamodb/latest/developerguide/DAX.md "../../../amazondynamodb/latest/developerguide/DAX.md") within
   [Amazon VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") private subnets to reduce database load. This
   improves application response times while maintaining data
   isolation and remove dependencies on external caching
   services.
2. Implement asynchronous processing with
   [AWS Lambda](../../../lambda.md "../../../lambda.md"),
   [Amazon SQS](../../../sqs.md "../../../sqs.md"), and
   [Amazon SNS](../../../sns.md "../../../sns.md") configured within VPC boundaries to decouple
   application components, improve scalability, and handle
   workload spikes without relying on external messaging
   services or APIs.
3. Configure auto scaling using
   [Amazon ECS](../../../ecs.md "../../../ecs.md") with
   [AWS Auto Scaling policies](../../../autoscaling.md "../../../autoscaling.md"), and optimize database
   performance through
   [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/Introduction.md "../../../amazondynamodb/latest/developerguide/Introduction.md") partition design to dynamically adjust
   resources based on demand while maintaining cost efficiency
   and performance within controlled infrastructure.
4. Establish secure storage using
   [Amazon S3](../../../s3.md "../../../s3.md") with
   [AWS KMS](../../../kms.md "../../../kms.md") encryption. Implement
   [AWS PrivateLink](../../../whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.md "../../../whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.md") with VPC endpoints to keep traffic within
   AWS boundaries. Consider reducing external service
   dependencies and maintain regulatory adherence through
   network isolation. Always apply encryption at rest and in
   transit.

## Resources

**Related best practices:**

- [Performance
  Efficiency Pillar - AWS Well-Architected Framework](../performance-efficiency-pillar/welcome.md "../performance-efficiency-pillar/welcome.md")

**Related documents:**

- [Building
  event-driven architectures with Amazon SNS FIFO](https://aws.amazon.com/blogs/compute/building-event-driven-architectures-with-amazon-sns-fifo/ "https://aws.amazon.com/blogs/compute/building-event-driven-architectures-with-amazon-sns-fifo/")

**Related videos:**

- [AWS re:Invent 2023 - Simplifying modern data pipelines with
  zero-ETL architectures on AWS (PEX203)](https://www.youtube.com/watch?v=g2dJAuRRDIo "https://www.youtube.com/watch?v=g2dJAuRRDIo")
- [AWS re:Invent 2023: Embracing Change and Innovation with AWS
  Databases for Future-Proof Applications](https://aws.amazon.com/awstv/watch/7a66457631d/ "https://aws.amazon.com/awstv/watch/7a66457631d/")
- [Mastering
  Serverless: Advanced Best Practices for Building Scalable and
  Efficient Applications on AWS](https://aws.amazon.com/awstv/watch/318a3d82d43/ "https://aws.amazon.com/awstv/watch/318a3d82d43/")

**Related services:**

- [Amazon ElastiCache](../../../elasticache.md "../../../elasticache.md")
- [AWS Lambda](../../../lambda.md "../../../lambda.md")
- [Amazon DynamoDB](../../../amazondynamodb.md "../../../amazondynamodb.md")
- [AWS Auto Scaling](../../../autoscaling.md "../../../autoscaling.md")
