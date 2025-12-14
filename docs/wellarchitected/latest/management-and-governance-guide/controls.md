# Controls

A _control_ is a means of mitigating or detecting
an issue that is a consequence of risk being realized, while
_guardrails_ are a technical implementation to
meet those controls. More specifically, controls provide instruction
for configuring resources to mitigate or address specific risks. We
recommend you start their multi-account environment with AWS Control Tower, which
offers predefined baseline preventive and detective
guardrails that can be enabled at an environment, resource, account,
or Organizational Unit (OU) level. Guardrails are an essential part
of managing your AWS environments as they provide an automated way
to deliver on policy intentions. Two kinds of guardrails exist:
preventive and detective.

Preventive guardrails enforce specific policies to help ensure that
your accounts operate in alignment to compliance standards, and
disallow actions that lead to policy violations. Control what your
AWS accounts can do by only permitting specific services, Regions,
and service actions at the appropriate level. AWS Organizations
provides service control policies (SCPs) to apply permission
guardrails at the organization, organizational unit, or account
level. For example, you can apply an SCP that restricts users from
launching resources in Regions that you have not explicitly allowed.
Or, you can create an SCP to
Disallow
creation of access keys for the root user. This would help
secure your AWS accounts by disallowing creation of access keys for
the root user, thereby reducing risk of unrestricted access to all
resources in the account. 

Detective guardrails detect and alert on unexpected activity and
noncompliance of resources within your accounts, such as policy
violations. These are helpful in alerting when something requires
remediation (either manual or automated). For example, you can
create an AWS Config rule to
Detect
whether public write access to Amazon S3 Buckets is allowed.
This rule detects whether public write access is permitted to Amazon S3 buckets. You can use this alert to initiate remediation with a
Systems Manager automation document, or a procedure outlined in your
ITSM tools.

Selecting the right guardrails for your environments is an important
step in managing and governing your resources across AWS. Managing
configuration compliance for any IT service is typically required to
ensure security (confidentiality, integrity, and availability) of
your data. This includes reference to standards and regulatory
requirements, individual policy definitions, risk management
processes, remediation workflows, and exception procedures. To
select the correct guardrails, we recommend building a portfolio
from compliance frameworks, risk management processes, and AWS Best
Practices to match the needs of your specific organization.

Compliance-based controls are often included in the compliance and
framework specifications. As a reference, you can identify
risk-based controls with guidance from the
[National
Institute of Standards and Technology (NIST) CyberSecurity
Framework](https://www.nist.gov/cyberframework "https://www.nist.gov/cyberframework"). The
[NIST
Risk Management Framework (RMF)](https://csrc.nist.gov/projects/risk-management/about-rmf "https://csrc.nist.gov/projects/risk-management/about-rmf") defines an approach for how
to select controls, and the
[Factor
Analysis of Information Risk](https://www.fairinstitute.org/fair-risk-management "https://www.fairinstitute.org/fair-risk-management") (FAIR) defines a process for how
to calculate your risk profile and measure risk reduction efforts
related to controls.

We recommend aggregating the detective guardrails implemented
through AWS Config Rules into conformance packs so that they can be
easily provisioned across your AWS environments. A key feature of
conformance packs is that they are immutable—individual rules cannot
be changed outside of the pack in which they were deployed,
regardless of access or account permissions. In addition, if the
pack is deployed by an organization’s management account, it cannot
be modified by the organization’s member accounts. This approach
provides you with an additional level of security and certainty when
managing compliance across your environments. It also enables
aggregated reporting, as compliance summaries can be reported at the
pack level. You can start with the
[AWS Config conformance samples](../../../config/latest/developerguide/conformancepack-sample-templates.md "../../../config/latest/developerguide/conformancepack-sample-templates.md") we provide, and customize as you
see fit. When using multiple conformance packs, determine if
duplicate rules are being used as this might have cost implications
across your environments.

AWS has provided a sample
[set
of Config Conformance Packs](../../../config/latest/developerguide/conformancepack-sample-templates.md "../../../config/latest/developerguide/conformancepack-sample-templates.md") that align to specific services
and compliance frameworks. The sample templates, including those
related to compliance standards and industry benchmarks, are not
designed to ensure your compliance with a specific governance
standard, but rather are designed to help you form part of it. They
cannot replace your internal efforts or ensure that you will pass a
compliance assessment.

AWS Control Tower offers a simplified way to automate the
provisioning of accounts that are preconfigured with baseline
guardrails. Preventive guardrails deployed by AWS Control Tower are
implemented via service control policies (SCPs). Detective
guardrails deployed by AWS Control Tower are implemented using AWS Config Rules and AWS Lambda functions. In addition to the baseline
guardrails found in SCPs and AWS Config Rules, guardrails can also
be found in other M&G Guide capabilities. Some examples would be
IAM policies, network security groups, NACLs, budget alarms, and
constraints on Service Catalog products.

######

BPX Energy, a BP company, used AWS Control Tower to establish their
AWS environment with controls enabling them to deploy
detective controls with AWS Config and preventive controls with AWS Organizations SCPs via AWS Control Tower. _“The key
benefits of adopting AWS Control Tower included enhancing BPX
Energy’s security posture, enabling enterprise governance at scale,
and providing increased scalability.”_ Grant Matthews,
Chief Technology Officer, BPX Energy. Learn how BPX’s implementation
further aligns to the controls function described in
this M&G Guide by reviewing their
[case
study](https://aws.amazon.com/solutions/case-studies/bpx-energy/ "https://aws.amazon.com/solutions/case-studies/bpx-energy/").

Both AWS Control Tower and AWS Security Hub CSPM continually evaluate all
of your AWS accounts and workloads and provide dashboards so you can
quickly identify areas of deviation from established guardrails.
These insights can be used to improve and maintain your security
posture across your AWS environments. For instance, AWS Control Tower applies a mandatory set of guardrails during the provisioning
and management of your landing zone that indicate how your landing
zone is compliant with best practices. AWS Security Hub CSPM provides a
mechanism to deploy and categorize security-focused detective
guardrails. This mechanism allows you to aggregate, organize,
prioritize, and automate the remediation of the findings across your
multi-account environment. There is an inclusive set of Security Hub CSPM
standards that can be used to align to your specific compliance and
security framework. These include
[AWS Foundational Security Best Practices](../../../securityhub/latest/userguide/securityhub-standards-fsbp.md "../../../securityhub/latest/userguide/securityhub-standards-fsbp.md"), the
[CIS
AWS Foundations Benchmark](../../../securityhub/latest/userguide/securityhub-standards-cis.md "../../../securityhub/latest/userguide/securityhub-standards-cis.md"), and the
[Payment
Card Industry Data Security Standard (PCI DSS)](../../../securityhub/latest/userguide/securityhub-standards-pcidss.md "../../../securityhub/latest/userguide/securityhub-standards-pcidss.md"). You can
investigate findings via the AWS Security Hub CSPM integration with
Amazon Detective, and you can build automated or semiautomated
remediation actions using the Amazon EventBridge integration.

Review your use of detective guardrails to identify and remove
duplicative detection efforts when using one or more of these
frameworks. Also, as you use AWS services, remain aware of the
inherent quotas being imposed. For example, AWS Control Tower
describes its
[limitations
and service quotas within the service documentation](../../../controltower/latest/userguide/limits.md "../../../controltower/latest/userguide/limits.md"). When you review
these quotas, it is important to choose where to use preventive
versus detective guardrails to work within the service quotas while
still meeting your compliance needs.
