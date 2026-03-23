# [AG.DEP.1] Establish a controlled, multi-environment landing zone

**Category:** FOUNDATIONAL

Establish a multi-environment landing zone as a controlled foundation which
encompasses all of the environments that workloads run in. A landing zone acts as a
centralized base from which you can deploy workloads and applications across multiple
environments. In AWS, it is common to run each environment in a separate AWS account,
leading to hundreds or thousands of accounts being provisioned. Landing zones allow you to
scale and securely manage those accounts, services, and resources within.

Operate the landing zone using platform teams and the _X as a
Service_ (XaaS) interaction mode, as detailed in the [Team Topologies](https://teamtopologies.com/ "https://teamtopologies.com/") book by Matthew Skelton and
Manuel Pais. This enables teams to request or create resources within the landing zone using
infrastructure as code (IaC), API calls, and other developer tooling.

The landing zone has the benefit of maintaining consistency across multiple
environments through centrally-applied policies and service-level configurations. This
approach allows the governing platform teams to provision and manage resources, apply common
overarching policies, monitor and helps ensure compliance with governance and compliance
standards, manage permissions, and implement guardrails to enforce access control
guidelines, across all of the environments with minimal overhead.

It's a best practice within the landing zone to separate environments, such as
non-production and production, to allow for safer testing and deployments of systems. The
landing zone often includes processes for managing network connectivity and security,
application security, service onboarding, financial management, change management
capabilities, and developer experience and tools.

For most organizations, a single landing zone that includes
all environments for all workloads should suffice. Only under
special circumstances, such as acquisitions, divestments,
management of exceptionally large environments, specific
billing requirements, or varying classification levels for
government applications, might an organization need to manage
multiple landing zones.

Manage the landing zone and all changes to it as code. This
approach simplifies management, makes auditing easier, and
facilitates rollback of changes when necessary.

**Related information:**

- [AWS Well-Architected Cost Optimization Pillar: COST02-BP03
  Implement an account structure](../cost-optimization-pillar/cost_govern_usage_account_structure.md "../cost-optimization-pillar/cost_govern_usage_account_structure.md")
- [Cloud
  Security Governance - AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- [Landing
  zone - AWS Prescriptive Guidance](../../../prescriptive-guidance/latest/strategy-migration/aws-landing-zone.md "../../../prescriptive-guidance/latest/strategy-migration/aws-landing-zone.md")
- [Benefits
  of using multiple AWS accounts](../../../whitepapers/latest/organizing-your-aws-environment/benefits-of-using-multiple-aws-accounts.md "../../../whitepapers/latest/organizing-your-aws-environment/benefits-of-using-multiple-aws-accounts.md")
- [AWS Security Reference Architecture (AWS SRA)](../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md "../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md")
- [AWS Control Tower and AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-CTower.md "../../../organizations/latest/userguide/services-that-can-integrate-CTower.md")
- [Establishing
  Your Cloud Foundation on AWS](../../../whitepapers/latest/establishing-your-cloud-foundation-on-aws/welcome.md "../../../whitepapers/latest/establishing-your-cloud-foundation-on-aws/welcome.md")
- [Provision
  and manage accounts with Account Factory](../../../controltower/latest/userguide/account-factory.md "../../../controltower/latest/userguide/account-factory.md")
- [AWS Account Factory Email: Many AWS Accounts, one email
  address](https://github.com/aws-samples/aws-account-factory-email "https://github.com/aws-samples/aws-account-factory-email")
