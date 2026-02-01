# DSREL04-BP01 Design systems with clear boundaries between the

core solution and its regional implementations

Establish clear architectural boundaries between core solution and regional implementations
to effectively manage regulatory requirements across multiple jurisdictions while maintaining
operational efficiency. This separation enables organizations to adapt to legal requirements and
local regulatory requirements, particularly data sovereignty laws and privacy regulations. This
approach reduces the risk of compromising foundational system integrity or risking cross-region
data leakage.

This structured approach also enables faster regional expansion and reduced operational
complexity. It maintains centralized governance and security standards while supporting
compliance with diverse regulatory frameworks.

**Desired outcome:** Regional data remains within designated
geographic boundaries to satisfy data sovereignty requirements, while core services apply
consistent security policies across regions. Regional teams independently deploy features and
scale workloads without impacting other regions, and regional failures remain isolated. New
regions are onboarded using standardized templates, and compliance audits can be scoped to
individual region.

**Common anti-patterns:**

- Deploying monolithic applications across regions without separating core services from
  region-specific components, leading to unnecessary complexity and compliance risks.
- Embedding region-specific configurations, business rules, and compliance requirements
  directly into core application code rather than maintaining modular separation.
- Creating direct dependencies between regions through shared databases, overlapping
  IAM roles, or tight coupling of resources that prevent independent operation.
- Implementing inconsistent API contracts and interfaces across regions, breaking
  interoperability and complicating maintenance.
- Relying on manual deployment processes without automated pipelines, resulting in
  configuration drift and inconsistent implementations.
- Failing to properly segment networks and isolate regional workloads using appropriate
  AWS account structures, VPCs, and subnets.
- Centralizing sensitive data without appropriate filtering or controls, such as
  aggregating regional logs into a single global bucket.

**Benefits of establishing this best practice:**

- Supports adherence to region-specific regulations while maintaining consistent security
  controls across the core solution and regions.
- Reduces time to onboard new regions by reusing core service components, standardizing
  deployment processes, and allowing region-specific feature deployment without impacting the
  solution.
- Isolates regional failures to prevent cascading effects on other regions or core
  services, limiting the blast radius during outages.
- Enables independent solution updates, right-sizing of resources per region based on
  local demand, and transparent allocation of expenses to regional cost centers.
- Maintains uniform functionality across regions while accommodating local requirements,
  preferences, and customizations.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Architecting applications for multi-regional deployment in regulated industries requires
a thoughtful hub-and-spoke approach that balances global consistency with local compliance
requirements. Organizations should establish a central hub for core services (authentication,
business logic, and configuration management) while implementing spoke regions that handle
local data processing and compliance-specific workflows. This separation is best achieved
through AWS organizational units (OUs) through AWS service organizations, dedicated
accounts, and proper networking constructs that enforce both logical and physical boundaries.
By using well-defined APIs and event-driven patterns, organizations can establish loose
coupling between components while maintaining consistent deployment pipelines that adapt core
services to regional requirements without modifying the underlying code base.

Key implementation elements:

- Use separate AWS accounts for core and regional workloads.
- Implement infrastructure as code (IaC) with region-specific parameters.
- Enforce network traffic controls (for example, VPC peering or AWS Transit Gateway).
- Establish a central hub region for core services.
- Design standardized APIs for communication between core and regional components.
- Implement region-specific configuration management. Use event-driven architecture to
  achieve loose coupling.

### Implementation steps

1. Establish an [AWS Organization
   Structure](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") with [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md"), creating
   OUs for core and regional workloads. Implement SCPs for compliance, and configure tag
   policies for resource management, while also implementing [AWS Control Tower](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md")
   for governance.
2. Separate accounts by creating separate AWS accounts for core services, regional
   workloads, and shared services. Implement [AWS IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") for centralized
   access management.
3. Develop infrastructure as code (IaC) using [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") or [AWS CDK](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md"). Create core and
   regional infrastructure templates with parameterized configurations for region-specific
   settings.
4. Design network architecture using [Amazon VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") with a hub VPC for
   core services and spoke VPCs for regional workloads. Use [AWS Transit Gateway](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md") for traffic
   control and network segmentation. Alternatively, set up [VPC Peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") where
   appropriate.
5. Deploy core services in the central hub region. Use [AWS Resource Access Manager (RAM)](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md") to
   share resources within an AWS Region. Consider [Transit Gateway inter-Region peering](../../../solutions/latest/network-orchestration-aws-transit-gateway/transit-gateway-inter-region-peering.md "../../../solutions/latest/network-orchestration-aws-transit-gateway/transit-gateway-inter-region-peering.md") to share access if required.
6. Implement an API layer using [Amazon API Gateway](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md"), designing
   standardized APIs for core-regional communication. Implement API versioning, configure
   regional endpoints, and use [AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") to secure
   API access.

## Resources

**Related best practices:**

- [REL08-BP04 Deploy using immutable infrastructure](../reliability-pillar/rel_tracking_change_management_immutable_infrastructure.md "../reliability-pillar/rel_tracking_change_management_immutable_infrastructure.md")
- [DRHCOPS07-BP01 Use AWS services and tools for automation and infrastructure as code
  (IaC) across hybrid and edge environments](../data-residency-hybrid-cloud-services-lens/drhcops07-bp01.md "../data-residency-hybrid-cloud-services-lens/drhcops07-bp01.md")

**Related documents:**

- [Organizing Your AWS Environment Using Multiple Accounts](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md")
- [Reliability Pillar - AWS
  Well-Architected Framework](../reliability-pillar/welcome.md "../reliability-pillar/welcome.md")
-
- [AWS Control Tower User
  Guide](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md")

**Related videos:**

- [AWS re:Invent 2024 - Anatomy of
  an AWS Region (ARC204)](https://www.youtube.com/watch?v=PAr1DY82ymE "https://www.youtube.com/watch?v=PAr1DY82ymE")
- [AWS re:Invent 2024 - Best
  practices for creating multi-Region architectures on AWS (ARC323)](https://www.youtube.com/watch?v=CbkqQznZS9Y "https://www.youtube.com/watch?v=CbkqQznZS9Y")

**Related tools:**

- [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/")
- [Amazon Cognito](https://aws.amazon.com/cognito/ "https://aws.amazon.com/cognito/")
- [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/")
- [VPC
  Peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md")
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/")
- [AWS Systems Manager
  Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md")
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/")
- [AWS Organization Structure](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")
- [AWS CDK](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md")
