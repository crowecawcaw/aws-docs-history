# DSSEC01-BP01 Establish secure foundations aligned with

regulatory requirements

Establish secure foundations aligned with cybersecurity standards
using proven, compliant architectural baselines that meet security
and regulatory requirements from day one. A well-architected
security foundation provides the necessary guardrails and automated
controls to protect sensitive data and maintain regulatory adherence
across multi-account environments.

**Desired outcome:** Security and
compliance are built-in from day one, with automated guardrails,
continuous monitoring, and comprehensive logging aligned with
regulatory requirements.

**Common anti-patterns:**

- Implementing security controls as an afterthought rather than
  building them into the foundational architecture.
- Using ad-hoc security configurations without standardized
  baselines or compliance frameworks.
- Relying on manual security processes instead of automated,
  policy-driven controls.
- Implementing security controls that don't align with regulatory
  requirements.
- Implementing security architectures without considering the full
  lifecycle of compliance and audit requirements.

**Benefits of establishing this best
practice:**

- Accelerates deployment timelines by providing pre-configured
  security controls and compliance frameworks.
- Maintains consistent security posture across accounts and
  workloads through automated governance.
- Simplifies audit and compliance reporting through built-in
  monitoring and logging capabilities.
- Provides data sovereignty controls that meet regulatory
  requirements for data residency and privacy.
- Enables scalable security operations through centralized
  management and automated remediation.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Organizations in highly regulated industries must establish
security foundations that demonstrate compliance from day one
while enabling business agility.

The
[AWS Security Reference Architecture (SRA)](../../../prescriptive-guidance/latest/security-reference-architecture/architecture.md "../../../prescriptive-guidance/latest/security-reference-architecture/architecture.md") provides the
architectural blueprint for implementing security controls across
your infrastructure layers. By following proven patterns and using
solution accelerators (pre-built, tested solutions that speed up
implementation of common security and compliance requirements)
organizations can implement security controls that align with
frameworks such as NIST, ISO 27001, SOC 2, and industry-specific
regulations while maintaining the flexibility to adapt to evolving
requirements.

Consider using solution accelerators to set up foundational
landing zone capabilities. The
[Landing
Zone Accelerator (LZA) on AWS](../../../solutions/latest/landing-zone-accelerator-on-aws/solution-overview.md "../../../solutions/latest/landing-zone-accelerator-on-aws/solution-overview.md") extends
[AWS Control Tower](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md") by automating the deployment of additional
security controls, compliance frameworks, and governance policies.
It provides infrastructure-as-code templates that implement
security best practices and regulatory requirements across your
multi-account environment.

You can find additional partner built Landing Zone Accelerator
solutions from the
[AWS Digital Sovereignty Marketplace](https://aws.amazon.com/marketplace/solutions/digital-sovereignty "https://aws.amazon.com/marketplace/solutions/digital-sovereignty").

### Implementation steps

1. **Deploy foundational landing zone
   with AWS Control Tower**: Enable Control Tower in
   your management account to establish organizational units
   (OUs), baseline security controls, and centralized logging.
   This creates the foundation for multi-account governance.
2. **Enhance security capabilities with
   Landing Zone Accelerators**:
   - Deploy
     [Landing
     Zone Accelerator (LZA) on AWS](../../../solutions/latest/landing-zone-accelerator-on-aws/solution-overview.md "../../../solutions/latest/landing-zone-accelerator-on-aws/solution-overview.md") or equivalent
     partner solutions to automate deployment of additional
     security controls beyond Control Tower's baseline.
   - Select and customize compliance frameworks specific to
     your regulatory requirements (NIST, ISO 27001, PCI DSS,
     HIPAA). For the AWS LZA, review the
     [sample
     configurations](https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/release/v1.13.0/reference/sample-configurations "https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/release/v1.13.0/reference/sample-configurations") on GitHub and adapt them to your
     organization's needs.
   - For region-specific compliance requirements, review
     these regional landing zone implementations:
     - [Baseline
       Informatiebeveiliging Overheid (BIO) for the Dutch
       Public Sector](https://aws.amazon.com/contract-center/bio-for-the-dutch-public-sector/ "https://aws.amazon.com/contract-center/bio-for-the-dutch-public-sector/").
     - [Spain's
       National Security Framework (ENS)](https://aws.amazon.com/blogs/security/ccn-releases-guide-for-spains-ens-landing-zones-using-landing-zone-accelerator-on-aws/ "https://aws.amazon.com/blogs/security/ccn-releases-guide-for-spains-ens-landing-zones-using-landing-zone-accelerator-on-aws/").
     - [Germany's
       Cloud Computing Compliance Criteria Catalogue
       (C5)](https://aws.amazon.com/blogs/security/introducing-new-regional-implementations-of-landing-zone-accelerator-on-aws-to-support-digital-sovereignty/ "https://aws.amazon.com/blogs/security/introducing-new-regional-implementations-of-landing-zone-accelerator-on-aws-to-support-digital-sovereignty/").

   - Configure data sovereignty controls including encryption
     at rest and in transit, centralized key management with
     [AWS KMS](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md"), and data residency policies. Enable controls
     from the
     "[Digital
     Sovereignty group](../../../controltower/latest/controlreference/digital-sovereignty-controls.md "../../../controltower/latest/controlreference/digital-sovereignty-controls.md")" in Control Tower to
     enforce data residency requirements.

3. **Implement security best practices
   and patterns**:
   - Deploy security controls across network, identity, data,
     and application layers. Implement network segmentation,
     [VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md")
     isolation, and centralized egress controls following the
     [perimeter
     security](../../../prescriptive-guidance/latest/security-reference-architecture/perimeter-security.md "../../../prescriptive-guidance/latest/security-reference-architecture/perimeter-security.md") guidance in the AWS SRA.
   - Establish data perimeters using identity-based,
     network-based, and resource-based controls to block
     unauthorized access and accidental data exposure. Follow
     [Data
     Perimeter on AWS](https://aws.amazon.com/identity/data-perimeters-on-aws/ "https://aws.amazon.com/identity/data-perimeters-on-aws/") and implement
     [data
     perimeter policy examples](https://github.com/aws-samples/data-perimeter-policy-examples "https://github.com/aws-samples/data-perimeter-policy-examples") using service control
     policies and resource policies.
   - For workloads processing personal data, implement the
     [AWS Privacy Reference Architecture (AWS PRA)](../../../prescriptive-guidance/latest/security-reference-architecture/pra.md "../../../prescriptive-guidance/latest/security-reference-architecture/pra.md").
     Consider creating a dedicated personal data (PD)
     organizational unit with enhanced controls for
     collecting, storing, and processing personal data, as
     detailed in the
     [PRA
     organization account structure](../../../prescriptive-guidance/latest/privacy-reference-architecture/organization-account-structure.md "../../../prescriptive-guidance/latest/privacy-reference-architecture/organization-account-structure.md").

4. **Apply industry-specific best
   practices**:
   - Review and implement industry-specific guidance from AWS
     Well-Architected Lenses that address unique regulatory
     and security requirements for your sector:
     - [Healthcare
       Industry Lens](../healthcare-industry-lens/healthcare-industry-lens.md "../healthcare-industry-lens/healthcare-industry-lens.md") for HIPAA and healthcare data
       protection
     - [Financial
       Services Industry Lens](../financial-services-industry-lens/financial-services-industry-lens.md "../financial-services-industry-lens/financial-services-industry-lens.md") for financial
       regulations and data security
     - [Government
       Lens](../government-lens/government-lens.md "../government-lens/government-lens.md") for public sector compliance
       requirements

   - For specialized use cases or additional implementation
     guidance, explore
     [Prescriptive
     Guides](https://aws.amazon.com/prescriptive-guidance/?achp_navlib3 "https://aws.amazon.com/prescriptive-guidance/?achp_navlib3"),
     [Reference
     Architectures](https://aws.amazon.com/architecture/reference-architecture-diagrams/?achp_navlib4 "https://aws.amazon.com/architecture/reference-architecture-diagrams/?achp_navlib4"), and
     [Solution
     Accelerators](https://aws.amazon.com/solutions/ "https://aws.amazon.com/solutions/") on the
     [AWS Architecture Center](https://aws.amazon.com/architecture/ "https://aws.amazon.com/architecture/") that provide detailed
     implementation patterns for specific scenarios.

## Resources

**Related best practices:**

- [SEC01-BP01
  Separate workloads using accounts](../security-pillar/sec_securely_operate_multi_accounts.md "../security-pillar/sec_securely_operate_multi_accounts.md")
- [SEC01-BP03
  Identify and validate control objectives](../security-pillar/sec_securely_operate_control_objectives.md "../security-pillar/sec_securely_operate_control_objectives.md")
- [SEC03-BP05
  Define permission guardrails for your organization](../security-pillar/sec_permissions_define_guardrails.md "../security-pillar/sec_permissions_define_guardrails.md")
- [SEC01-BP06
  Automate deployment of standard security controls](../security-pillar/sec_securely_operate_automate_security_controls.md "../security-pillar/sec_securely_operate_automate_security_controls.md")

**Related documents:**

- [AWS Security Reference Architecture](../../../prescriptive-guidance/latest/security-reference-architecture/architecture.md "../../../prescriptive-guidance/latest/security-reference-architecture/architecture.md")
- [Landing
  Zone Accelerator on AWS Implementation Guide](../../../solutions/latest/landing-zone-accelerator-on-aws/solution-overview.md "../../../solutions/latest/landing-zone-accelerator-on-aws/solution-overview.md")
- [AWS Control Tower User Guide](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md")
- [AWS Well-Architected Security Pillar](../security-pillar/welcome.md "../security-pillar/welcome.md")
- [AWS Compliance Center](https://aws.amazon.com/compliance/ "https://aws.amazon.com/compliance/")

**Related videos:**

- [Establishing
  a Data Perimeter on AWS, RSA Conference](https://www.youtube.com/watch?v=sk0wU3rHV10 "https://www.youtube.com/watch?v=sk0wU3rHV10")
- [AWS re:Invent 2025 - Building Sovereign Cloud Environments
  (COP409)](https://www.youtube.com/watch?v=zxvDiXPl6_Q "https://www.youtube.com/watch?v=zxvDiXPl6_Q")
- [AWS re:Invent 2025 - Advanced AI Security: Architecting
  Defense-in-Depth for AI Workloads (SEC410)](https://www.youtube.com/watch?v=2sWNBNLxBlc "https://www.youtube.com/watch?v=2sWNBNLxBlc")
- [AWS re:Invent 2025 - AWS Security Hub: Unifying & simplifying
  security operations at scale (SEC228)](https://www.youtube.com/watch?v=mYyBQYIeJzk "https://www.youtube.com/watch?v=mYyBQYIeJzk")
- [AWS Security Reference Architecture: Visualize your security - NDC
  Security 2024](https://www.youtube.com/watch?v=jGxS-7s-0sE "https://www.youtube.com/watch?v=jGxS-7s-0sE")

**Related examples:**

- [Landing
  Zone Accelerator Sample Configurations](https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/main/reference/sample-configurations "https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/main/reference/sample-configurations")
- [AWS Security Reference Architecture GitHub Repository](https://github.com/aws-samples/aws-security-reference-architecture-examples "https://github.com/aws-samples/aws-security-reference-architecture-examples")
- [AWS Well-Architected Labs - Security](https://wellarchitectedlabs.com/security/ "https://wellarchitectedlabs.com/security/")

**Related services:**

- [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/")
- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/")
- [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
