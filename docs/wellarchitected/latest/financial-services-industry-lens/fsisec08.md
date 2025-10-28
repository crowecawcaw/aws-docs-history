# FSISEC08: How do you isolate your software development lifecycle (SDLC) environments (like development, test, and production)?

We recommend that you separate production workloads from
non-production workloads. Maintaining resource isolation between
software development lifecycle (SDLC) environments reduces the
chance of misuse and accidents in production environments. This
is an important guidance for all financial institutions, including those that are subject to Payment Card
Industry Data Security Standard (PCI DSS).

## FSISEC08-BP01 Implement a multi-account strategy

Using multiple AWS accounts to help isolate and manage your
business applications and data can help you optimize across
most of the
[AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/") pillars,
including operational excellence, security, reliability, and
cost optimization. We recommend organizing your overall AWS environment with a
[multi-account
strategy](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md"). The extent to which you use these
best practices depends on your stage of the cloud adoption
journey and specific business needs.

We recommend that you isolate production workload environments
and data in production accounts housed within production OUs,
under your top-level workload-oriented OUs. Apart from
production OUs, we recommend that you define one or more
non-production OUs that contain accounts and workload
environments that are used to develop and test workloads.

Having different accounts dedicated to different SDLC
environments provides a natural isolation in managing
privileges in IAM. AWS Organizations facilitates the
management of account hierarchy. Define service control
policies (SCPs) to limit the actions a user can perform inside
these accounts. For example, you could minimize changes in
production to CloudTrail logging, help prevent internet
gateways set up in a VPC, or help prevent modifying AWS Config
tracking.

To offer a straightforward way to set up and govern an AWS
multi-account environment that follows prescriptive best
practices, AWS has created
[AWS Control Tower](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md"), which extends the
capabilities of AWS Organizations. To help keep your
organizations and accounts from _drift_, or
divergence from best practices, AWS Control Tower applies
[comprehensive
controls](https://aws.amazon.com/blogs/aws/new-for-aws-control-tower-comprehensive-controls-management-preview/ "https://aws.amazon.com/blogs/aws/new-for-aws-control-tower-comprehensive-controls-management-preview/") (sometimes called
_guardrails_). For more detail, see

[Limitations
and quotas in AWS Control Tower](../../../controltower/latest/userguide/limits.md "../../../controltower/latest/userguide/limits.md").

## FSISEC08-BP02 Enforce network isolation

Some financial industry regulators require the implementation
of techniques such as
[Zero
Trust](https://aws.amazon.com/security/zero-trust/ "https://aws.amazon.com/security/zero-trust/") or microsegmentation in their
regulated entities. In addition to IAM isolation, enforce
clear separation of resources between production and
non-production environments. Using different accounts helps create the highest form of isolation possible on AWS. However,
you may need to reach resources across accounts, especially
when accessing shared services such as logging and security
services.

[VPC
Peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") connects resources in two VPCs (in
the same account or between different accounts) without the
need of additional gateways or VPN connections, and it makes
the peered network visible to each other. This requires complete network trust between
the two VPCs, and better alternatives exist depending on your
use case. If the objective is to access only a few services in
the other VPC, use
[AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md"), which provides connectivity
over an internal network without VPN and limits network exposure. Service publishers also have to specify which IAM
principals can consume these endpoints and attach an IAM
resources policy specifying what actions are allowed. If more
extensive cross-VPC access is needed, separation and private
connectivity can be also established with
[AWS Transit Gateways](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md").

## Resources

**Related documents:**

- [Best Practices for Organizational Units with AWS Organizations](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/ "https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/")
- [Supporting Data Residency Requirements by Extending AWS Control Tower Governance to Non-supported
  Regions](https://aws.amazon.com/blogs/mt/supporting-data-residency-requirements-by-extending-aws-control-tower-governance-to-non-supported-regions/ "https://aws.amazon.com/blogs/mt/supporting-data-residency-requirements-by-extending-aws-control-tower-governance-to-non-supported-regions/")
- [The
  AWS Security Reference Architecture](../../../prescriptive-guidance/latest/security-reference-architecture/architecture.md "../../../prescriptive-guidance/latest/security-reference-architecture/architecture.md")
- [Zero
  Trust architectures: An AWS perspective](https://aws.amazon.com/blogs/security/zero-trust-architectures-an-aws-perspective/ "https://aws.amazon.com/blogs/security/zero-trust-architectures-an-aws-perspective/")

**Related videos:**

- [AWS Summit DC 2022 - Integrating AWS services and Zero Trust networks](https://www.youtube.com/watch?v=4sWFKtoAMsI&ab_channel=AWSEvents "https://www.youtube.com/watch?v=4sWFKtoAMsI&ab_channel=AWSEvents")
- [AWS re:Invent 2020: Zero Trust: An AWS perspective](https://www.youtube.com/watch?v=O33LPy4M4vA&ab_channel=AWSEvents "https://www.youtube.com/watch?v=O33LPy4M4vA&ab_channel=AWSEvents")
