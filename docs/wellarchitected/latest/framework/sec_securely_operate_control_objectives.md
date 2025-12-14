# SEC01-BP03 Identify and validate control objectives

Based on your compliance requirements and risks identified from your threat model, derive and validate the control objectives and controls that you need to apply to your workload. Ongoing validation of control objectives and controls help you measure the effectiveness of risk mitigation.

**Desired outcome:** The security control objectives of your business are well-defined and aligned to your compliance requirements. Controls are implemented and enforced through automation and policy and are continually evaluated for their effectiveness in achieving your objectives. Evidence of effectiveness at both a point in time and over a period of time are readily reportable to auditors.

**Common anti-patterns:**

- Regulatory requirements, market expectations, and industry standards for assurable security are not well-understood for your business
- Your cybersecurity frameworks and control objectives are misaligned to the requirements of your business
- The implementation of controls does not strongly align to your control objectives in a measurable way
- You do not use automation to report on the effectiveness of your controls

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

There are many common cybersecurity frameworks that can form the basis for your security control objectives. Consider the regulatory requirements, market expectations, and industry standards for your business to determine which frameworks best supports your needs. Examples include [AICPA SOC 2](https://aws.amazon.com/compliance/soc-faqs/ "https://aws.amazon.com/compliance/soc-faqs/"), [HITRUST](https://aws.amazon.com/compliance/hitrust/ "https://aws.amazon.com/compliance/hitrust/"), [PCI-DSS](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/ "https://aws.amazon.com/compliance/pci-dss-level-1-faqs/"), [ISO 27001](https://aws.amazon.com/compliance/iso-27001-faqs/ "https://aws.amazon.com/compliance/iso-27001-faqs/"), and [NIST SP 800-53](https://aws.amazon.com/compliance/nist/ "https://aws.amazon.com/compliance/nist/").

For the control objectives you identify, understand how AWS services you consume help you to achieve those objectives. Use [AWS Artifact](https://aws.amazon.com/artifact/ "https://aws.amazon.com/artifact/") to find documentation and reports aligned to your target frameworks that describe the scope of responsibility covered by AWS and guidance for the remaining scope that is your responsibility. For further service-specific guidance as they align to various framework control statements, see [AWS Customer Compliance Guides](https://d1.awsstatic.com/whitepapers/compliance/AWS_Customer_Compliance_Guides.pdf "https://d1.awsstatic.com/whitepapers/compliance/AWS_Customer_Compliance_Guides.pdf").

As you define the controls that achieve your objectives, codify enforcement using preventative controls, and automate mitigations using detective controls. Help prevent non-compliant resource configurations and actions across your AWS Organizations using [service control policies (SCP)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md"). Implement rules in [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") to monitor and report on non-compliant resources, then switch rules to an enforcement model once confident in their behavior. To deploy sets of pre-defined and managed rules that align to your cybersecurity frameworks, evaluate the use of [AWS Security Hub CSPM standards](../../../securityhub/latest/userguide/standards-reference.md "../../../securityhub/latest/userguide/standards-reference.md") as your first option. The AWS Foundational Service Best Practices (FSBP) standard and the CIS AWS Foundations Benchmark are good starting points with controls that align to many objectives that are shared across multiple standard frameworks. Where Security Hub CSPM does not intrinsically have the control detections desired, it can be complemented using [AWS Config conformance packs](../../../config/latest/developerguide/conformance-packs.md "../../../config/latest/developerguide/conformance-packs.md").

Use [APN Partner Bundles](https://aws.amazon.com/partners/programs/gsca/bundles/ "https://aws.amazon.com/partners/programs/gsca/bundles/") recommended by the AWS Global Security and Compliance Acceleration (GSCA) team to get assistance from security advisors, consulting agencies, evidence collection and reporting systems, auditors, and other complementary services when required.

### Implementation steps

1. Evaluate common cybersecurity frameworks, and align your control objectives to the ones chosen.
2. Obtain relevant documentation on guidance and responsibilities for your framework using AWS Artifact. Understand which parts of compliance fall on the AWS side of the shared responsibility model and which parts are your responsibility.
3. Use SCPs, resource policies, role trust policies, and other guardrails to prevent non-compliant resource configurations and actions.
4. Evaluate deploying Security Hub CSPM standards and AWS Config conformance packs that align to your control objectives.

## Resources

**Related best practices:**

- [SEC03-BP01
  Define access requirements](sec_permissions_define.md "sec_permissions_define.md")
- [SEC04-BP01 Configure
  service and application logging](sec_detect_investigate_events_app_service_logging.md "sec_detect_investigate_events_app_service_logging.md")
- [SEC07-BP01
  Understand your data classification scheme](sec_data_classification_identify_data.md "sec_data_classification_identify_data.md")
- [OPS01-BP03
  Evaluate governance requirements](ops_priorities_governance_reqs.md "ops_priorities_governance_reqs.md")
- [OPS01-BP04
  Evaluate compliance requirements](ops_priorities_compliance_reqs.md "ops_priorities_compliance_reqs.md")
- [PERF01-BP05
  Use policies and reference architectures](perf_architecture_use_policies_and_reference_architectures.md "perf_architecture_use_policies_and_reference_architectures.md")
- [COST02-BP01
  Develop policies based on your organization
  requirements](cost_govern_usage_policies.md "cost_govern_usage_policies.md")

**Related documents:**

- [AWS Customer Compliance Guides](https://d1.awsstatic.com/whitepapers/compliance/AWS_Customer_Compliance_Guides.pdf "https://d1.awsstatic.com/whitepapers/compliance/AWS_Customer_Compliance_Guides.pdf")

**Related tools:**

- [AWS Artifact](https://aws.amazon.com/artifact/ "https://aws.amazon.com/artifact/")
