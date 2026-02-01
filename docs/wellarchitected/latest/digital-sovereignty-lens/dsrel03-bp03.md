# DSREL03-BP03 Design for code, config, and data portability

across primary and disaster recovery (DR) sites

In highly regulated industries, designing for workload portability
across primary and disaster recovery sites is both a regulatory
mandate and business necessity. This approach provides seamless
failover capabilities while maintaining regulatory requirements,
minimizing recovery times, and reducing dependencies on specific
services or regions, ultimately protecting against both operational
disruptions and vendor lock-in risks.

**Desired outcome:** Code,
configurations, and data can be deployed and recovered consistently
across primary and disaster recovery sites, maintaining compliance
requirements and operational continuity during failover scenarios.

**Common anti-patterns:**

- Hard-coding region-specific resources (for example, Amazon
  Machine Image (AMI) IDs, Amazon Resource Names (ARNs),
  endpoints) in application code or infrastructure templates.
- Relying on manual processes for configuration management and
  deployments without version control or automated pipelines.
- Creating Region-dependent storage patterns and failing to
  account for cross-region replication requirements.
- Storing environment-specific secrets and parameters within
  application code rather than using centralized parameter stores.
- Implementing DR as an afterthought and neglecting regular
  testing of failover procedures.
- Using single-region Domain Name System (DNS) and networking
  configurations that create bottlenecks during failover
  scenarios.
- Ignoring encryption and compliance requirements during
  cross-region data transfers.

**Benefits of establishing this best
practice:**

- Reduced Recovery Time Objective (RTO) and Recovery Point
  Objective (RPO) through automated failover, replication, and
  consistent infrastructure provisioning across Regions.
- Demonstrated robust DR capabilities meeting regulatory
  requirements while enabling quick response to regional outages.
- Reduced human error and configuration drift through automated
  processes and infrastructure as code practices.
- Faster development cycles with portable code and simplified DR
  validation through consistent environments.
- Efficient resource utilization through automated scaling and
  ability to use multiple regions for active-active scenarios.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Design a portable architecture that separates application logic,
infrastructure, and data management using AWS services.

### Implementation steps

1. Establish an infrastructure as code foundation using
   [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") and
   [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/") for consistent, Region-agnostic deployments,
   creating base templates, Regional variations, parameter
   files, and resource mappings.
2. Set up configuration management with
   [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") Parameter Store and
   [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/ "https://aws.amazon.com/secrets-manager/") for parameter hierarchies,
   environment configs, and Regional settings.
3. Deploy containerized applications using
   [Amazon ECS](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/") and
   [Amazon EKS](https://aws.amazon.com/eks/ "https://aws.amazon.com/eks/") for consistent runtime environments, configuring
   task definitions, service discovery, auto scaling, and load
   balancing.
4. Configure automated cross-Region data replication with
   [Amazon RDS](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/") read replicas,
   [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") cross-Region replication,
   [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") global tables, and
   [AWS DMS](https://aws.amazon.com/dms/ "https://aws.amazon.com/dms/").
5. Establish consistent governance framework using
   [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/"),
   [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/") for service control policies, tag
   policies, and backup policies, and configure
   [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") for compliance monitoring.
6. Create CI/CD pipelines using
   [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/"),
   [AWS CodeBuild](https://aws.amazon.com/codebuild/ "https://aws.amazon.com/codebuild/"), and
   [AWS CodeDeploy](https://aws.amazon.com/codedeploy/ "https://aws.amazon.com/codedeploy/") for multi-Region deployment with
   environment-specific parameters.
7. Implement comprehensive cross-Region health checks and
   monitoring using
   [Amazon Route 53](https://aws.amazon.com/route53/ "https://aws.amazon.com/route53/"),
   [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/ "https://aws.amazon.com/global-accelerator/"), and
   [AWS Health](https://aws.amazon.com/premiumsupport/technology/aws-health/ "https://aws.amazon.com/premiumsupport/technology/aws-health/").

#### Resources

**Related best practices:**

- [GENREL05-BP02
  Replicate embedding data across all regions of
  availability](../generative-ai-lens/genrel05-bp02.md "../generative-ai-lens/genrel05-bp02.md")
- [DRHCOPS03-BP02
  Understand factors that determine your data replication
  strategy](../data-residency-hybrid-cloud-services-lens/drhcops03-bp02.md "../data-residency-hybrid-cloud-services-lens/drhcops03-bp02.md")

**Related services:**

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/")
- [AWS CodeBuild](https://aws.amazon.com/codebuild/ "https://aws.amazon.com/codebuild/")
- [AWS CodeDeploy](https://aws.amazon.com/codedeploy/ "https://aws.amazon.com/codedeploy/")
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS DMS](https://aws.amazon.com/dms/ "https://aws.amazon.com/dms/")
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/")
- [Amazon ECS](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/")
- [Amazon EKS](https://aws.amazon.com/eks/ "https://aws.amazon.com/eks/")
- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [Amazon RDS](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/ "https://aws.amazon.com/secrets-manager/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
