# Best Practice 5.3 – Assess the need

for specific security controls for your SAP workloads

Based on the data classification, evaluate any controls that can help you to meet the
standards and requirements established in the previous best practices. These include
location, AWS account strategy and scrambling requirements for non-production SAP
workloads.

**Suggestion 5.3.1 - Assess any geographical location
requirements**

Your SAP workloads might be deployed in one or many AWS Regions and Availability
Zones (AZs). Each AWS Region consists of multiple, isolated, and physically separate AZs
within a geographic area. In addition to evaluating the Region for latency, resilience,
and sustainability specifications,
you should consider whether security and compliance requirements can be met. Examples of
isolated Regions with specific operating jurisdictions include:

- AWS GovCloud (US) - designed to host sensitive data, regulated workloads, and
  address the most stringent US government security and compliance requirements
- Amazon Web Services in China - AWS has collaborated with local partners to
  ensure China’s legal and regulatory requirements are met
  Some industries and countries will have data residency requirements that all customer
  content processed and stored in an IT system must remain within a specific country’s
  borders.

- AWS Documentation: [AWS Security blogs for data residency](https://aws.amazon.com/blogs/security/tag/data-residency/ "https://aws.amazon.com/blogs/security/tag/data-residency/")
  Before deciding on a location, review the availability of services for that AWS
  Region to ensure that the services that you require are available.

- AWS Documentation: [AWS Regional Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/")

**Suggestion 5.3.2 - Determine how your SAP workloads align with your
AWS account strategy and landing zone**

An important consideration when running SAP workloads in AWS is the AWS account
strategy and landing zone approach that you adopt to meet your organization’s security
controls. You should consider separating SAP from non-SAP workloads and having production workloads in
a separate account from non-production workloads.

Understand your organization’s existing AWS account management strategy, including
the use of the AWS Organizations and AWS Control Tower. Consider isolating security and log capabilities
into an isolated account. Refer to the following for additional details:

- Well-Architected Framework [Security]: [AWS Account Management and Separation](../security-pillar/aws-account-management-and-separation.md "../security-pillar/aws-account-management-and-separation.md")
- AWS Documentation: [Establishing your best practice AWS environment](https://aws.amazon.com/organizations/getting-started/best-practices/ "https://aws.amazon.com/organizations/getting-started/best-practices/")
- AWS Documentation: [Organizing Your AWS Environment Using Multiple Accounts](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md")
- AWS Documentation:[AWS multi-account strategy for your AWS Control Tower landing zone](../../../controltower/latest/userguide/aws-multi-account-landing-zone.md "../../../controltower/latest/userguide/aws-multi-account-landing-zone.md")
  The account strategy you adopt will also affect the network configuration within
  AWS. As part of determining the appropriate AWS account strategy for your SAP
  workloads you should consider the following:

- Requirements for cross-account access, such as the need for setting up [VPC
  Peering](../../../vpc/latest/userguide/vpc-peering.md "../../../vpc/latest/userguide/vpc-peering.md") or [Transit
  Gateway](../../../vpc/latest/tgw/tgw-transit-gateways.md "../../../vpc/latest/tgw/tgw-transit-gateways.md") to allow communication between non-production and production
  systems. For example, the movement of SAP transports through your landscape.
- Dependencies on shared services (such as directory management resources) and
  network management components that are deployed in different AWS accounts from your
  SAP workloads.
- In addition to the core security services, such as IAM and network controls,
  consider how AWS managed security services can help achieve security goals or uplift
  your security posture. AWS provides security services to assist with web application
  firewalls, traffic auditing, DDOS protection, CVE management, configuration auditing,
  and virus and threat detection.
- AWS Documentation: [AWS Foundational Security Best Practices Controls](../../../securityhub/latest/userguide/securityhub-standards-fsbp-controls.md "../../../securityhub/latest/userguide/securityhub-standards-fsbp-controls.md")

**Suggestion 5.3.3 - Review the controls for data scrambling (if
applicable)**

Many SAP customers rely on copies of production data for testing purposes, including
regression and performance testing. If creating a copy of production data, decide which
controls you must add to ensure that your production data is protected from unintended
access and modifications.

Consider the following options:

- Traditional data scrambling mechanisms provided by SAP or third-party
  providers
- The use of additional accounts or network controls to limit access during a copy
  of production data
- Use of a non-production account with the same controls as production
