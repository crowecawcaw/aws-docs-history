# DSREL03-BP02 Design workloads to be interoperable across

primary and disaster recovery (DR) sites

In highly regulated industries, workloads must be designed for
seamless interoperability across primary and disaster recovery sites
to maintain both operational continuity and regulatory requirements.
Customers must aim for reduction in disruption during failovers
while meeting regulatory demands for data integrity, maintaining
audit trails, and meeting recovery objectives.

**Desired outcome:** Workloads
operate consistently across primary and disaster recovery sites,
maintaining performance, security controls, and regulatory
requirements during normal operations and failover scenarios.

**Common anti-patterns:**

- Hard-coding Region-specific configurations and creating
  dependencies that block applications from running identically
  across sites.
- Using different security policies, Identity and Access
  Management (IAM) configurations, and compliance controls between
  primary and DR environments.
- Relying on human intervention for failover and deployments,
  increasing risk of errors and recovery time.
- Creating tightly coupled architectures and data silos that don't
  account for cross-region requirements.
- Inadequately testing DR functionality and treating it as a cold
  standby rather than a fully validated environment.

**Benefits of establishing this best
practice:**

- Reduced Recovery Time Objective (RTO) through consistent
  configurations and automated failover, minimizing downtime
  during outages.
- Uniform controls, audit capabilities, and configurations across
  environments meeting data redundancy requirements.
- Improved confidence through regularly validated DR capabilities,
  automated processes, and simplified maintenance.
- Efficient resource utilization through automated scaling and
  ability to use DR sites for testing and development.
- Demonstrated interoperability across regions with validated
  performance under various failure scenarios.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Design containerized or serverless workloads using environment
agnostic architectures and infrastructure as code (IaC) to
maintain consistency across primary and DR sites.

Key implementation elements:

- Deploy containerized or serverless architectures that abstract
  infrastructure dependencies
- Use parameter stores and configuration management for
  environment-specific, jurisdiction-aware settings
- Implement automated CI/CD pipelines for identical deployments
  across regions
- Configure automated data replication and synchronization
  between sites
- Establish comprehensive health checks, monitoring, and logging
  across regions
- Regularly test DR plans and automated failover mechanisms

This approach improves workload portability while maintaining
operational consistency and reliability across environments.

### Implementation steps

1. Implement a containerization strategy depending on knowledge
   using [Amazon ECS](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/") and if kubernetes knowledge exists using
   [Amazon EKS](https://aws.amazon.com/eks/ "https://aws.amazon.com/eks/") to configure container registries, orchestration,
   scaling policies, and health checks.
2. Deploy serverless applications using
   [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/"),
   [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/"), and
   [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/"), configuring regional endpoints.
3. Set up configuration management with
   [AWS Systems Manager Parameter Store](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") for environment
   variables, application configs, secrets management, and
   regional settings.
4. Develop infrastructure as code using
   [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") and
   [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/"), including environment parameters, regional
   configurations, resource definitions, and dependencies.
5. Configure a CI/CD pipeline with
   [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/") for source control integration, build
   processes, testing frameworks, and deployment stages, and
   implement
   [AWS CodeBuild](https://aws.amazon.com/codebuild/ "https://aws.amazon.com/codebuild/").
6. Implement data replication using
   [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") replication,
   [Amazon RDS](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/") read replicas, and
   [AWS DMS](https://aws.amazon.com/dms/ "https://aws.amazon.com/dms/"), configuring synchronization, monitoring, and
   failover.

## Resources

**Related best practices:**

- [DRHCOPS03-BP02
  Understand factors that determine your data replication
  strategy](../data-residency-hybrid-cloud-services-lens/drhcops03-bp02.md "../data-residency-hybrid-cloud-services-lens/drhcops03-bp02.md")

**Related videos:**

- [Mastering
  Observability: Building Resilient Systems on AWS with
  CloudWatch and X-Ray](https://aws.amazon.com/awstv/watch/f6a3e1f43b5/ "https://aws.amazon.com/awstv/watch/f6a3e1f43b5/")
- [AWS re:Invent 2025 - Architecting resilient multicloud operations,
  feat. Monzo Bank (HMC201)](https://www.youtube.com/watch?v=oDroYE4unmY "https://www.youtube.com/watch?v=oDroYE4unmY")
- [AWS re:Invent 2025 - Build and optimize edge architecture for
  resiliency with AI (HMC403)](https://www.youtube.com/watch?v=O_fCw4zH88U "https://www.youtube.com/watch?v=O_fCw4zH88U")
- [AWS re:Invent 2025 - Digital sovereignty and data residency w/ AWS
  Hybrid and Edge services (HMC310)](https://www.youtube.com/watch?v=CxkRvW42Hgc "https://www.youtube.com/watch?v=CxkRvW42Hgc")

**Related services:**

- [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/")
- [Amazon ECS](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/")
- [Amazon EKS](https://aws.amazon.com/eks/ "https://aws.amazon.com/eks/")
- [Amazon RDS](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
- [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/")
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CodeBuild](https://aws.amazon.com/codebuild/ "https://aws.amazon.com/codebuild/")
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/")
- [AWS DMS](https://aws.amazon.com/dms/ "https://aws.amazon.com/dms/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
- [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/")
- [AWS Systems Manager Parameter Store](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
