# Standards reference for Security Hub CSPM

In AWS Security Hub CSPM, a _security standard_ is a set of
requirements that's based on regulatory frameworks, industry best practices, or company
policies. Security Hub CSPM maps these requirements to controls, and runs security checks on the
controls to assess whether the requirements of a standard are being met. Each standard
includes multiple controls.

Security Hub CSPM currently supports the following standards:

- **AWS Foundational Security Best Practices**
  – Developed by AWS and industry professionals, this standard is a
  compilation of security best practices for organizations, regardless of sector or
  size. It provides a set of controls that detect when your AWS accounts and
  resources deviate from security best practices. It also provides prescriptive
  guidance about how to improve and maintain your security posture.
- **AWS Resource Tagging** – Developed by
  Security Hub CSPM, this standard can help you determine whether your AWS resources have tags.
  A _tag_ is a key-value pair that acts as metadata
  for an AWS resource. Tags can help you identify, categorize, manage, and search
  for AWS resources. For example, you can use tags to categorize resources by
  purpose, owner, or environment.
- **CIS AWS Foundations Benchmark** –
  Developed by the Center for Internet Security (CIS), this standard provides secure
  configuration guidelines for AWS. It specifies a set of security configuration
  guidelines and best practices for a subset of AWS services and resources, with an
  emphasis on foundational, testable, and architecture agnostic settings. The
  guidelines include clear, step-by-step implementation and assessment
  procedures.
- **NIST SP 800-53 Revision 5** – This standard aligns
  with National Institute of Standards and Technology (NIST) requirements for
  protecting the confidentiality, integrity, and availability of information systems
  and critical resources. The associated framework generally applies to U.S. federal
  agencies or organizations that work with U.S. federal agencies or information
  systems. However, private organizations can also use the requirements as a guiding
  framework.
- **NIST SP 800-171 Revision 2** – This standard aligns
  with NIST security recommendations and requirements for protecting the
  confidentiality of Controlled Unclassified Information (CUI) in systems and
  organizations that aren't part of the U.S. federal government. _CUI_ is information that doesn't meet government
  criteria for classification, but is considered sensitive and is created or possessed
  by the U.S. federal government or other entities on behalf of the U.S. federal
  government.
- **PCI DSS** – This standard aligns with the
  Payment Card Industry Data Security Standard (PCI DSS) compliance framework defined
  by the PCI Security Standards Council (SSC). The framework provides a set of rules
  and guidelines for safely handling credit and debit card information. The framework
  generally applies to organizations that store, process, or transmit cardholder
  data.
- **Service-managed standard, AWS Control Tower** –
  This standard helps you configure the proactive controls provided by AWS Control Tower
  alongside the detective controls provided by Security Hub CSPM. AWS Control Tower offers a
  straightforward way to set up and govern an AWS multi-account environment,
  following prescriptive best practices. By enabling both proactive and detective
  controls for your AWS environment, you can enhance your security posture at
  different development stages.
  Security Hub CSPM standards and controls don't guarantee compliance with any regulatory frameworks or
  audits. Instead, they provide a way to evaluate and monitor the state of your AWS accounts
  and resources. We recommend enabling each standard that's relevant to your business needs,
  industry, or use case.

Individual controls can apply to more than one standard. If you enable multiple standards,
we recommend that you also enable consolidated control findings. If you do this, Security Hub CSPM
generates a single finding for each control, even if the control applies to more than one
standard. If you don't turn on consolidated control findings, Security Hub CSPM generates a separate
finding for each enabled standard that a control applies to. For example, if you enable two
standards and a control applies to both of them, you receive two separate findings for the
control, one for each standard. If you enable consolidated control findings, you receive
only one finding for the control. For more information, see [Consolidated control findings](controls-findings-create-update.md#consolidated-control-findings "controls-findings-create-update.md#consolidated-control-findings").

###### Detailed reference by standard

- [AWS Foundational Security Best Practices](fsbp-standard.md "fsbp-standard.md")
- [AWS Resource Tagging](standards-tagging.md "standards-tagging.md")
- [CIS AWS Foundations Benchmark](cis-aws-foundations-benchmark.md "cis-aws-foundations-benchmark.md")
- [NIST SP 800-53 Revision 5](standards-reference-nist-800-53.md "standards-reference-nist-800-53.md")
- [NIST SP 800-171 Revision 2](standards-reference-nist-800-171.md "standards-reference-nist-800-171.md")
- [PCI DSS](pci-standard.md "pci-standard.md")
- [Service-managed standards](service-managed-standards.md "service-managed-standards.md")
