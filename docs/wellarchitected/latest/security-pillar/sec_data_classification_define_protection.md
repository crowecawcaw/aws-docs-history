# SEC07-BP02 Apply data protection controls based on data sensitivity

Apply data protection controls that provide an appropriate level of
control for each class of data defined in your classification
policy.  This practice can allow you to protect sensitive data from
unauthorized access and use, while preserving the availability and
use of data.

**Desired outcome:** You have a
classification policy that defines the different levels of
sensitivity for data in your organization.  For each of these
sensitivity levels, you have clear guidelines published for approved
storage and handling services and locations, and their required
configuration.  You implement the controls for each level according
to the level of protection required and their associated costs.  You
have monitoring and alerting in place to detect if data is present
in unauthorized locations, processed in unauthorized environments,
accessed by unauthorized actors, or the configuration of related
services becomes non-compliant.

**Common anti-patterns:**

- Applying the same level of protection controls across all data.
  This may lead to over-provisioning security controls for
  low-sensitivity data, or insufficient protection of highly
  sensitive data.
- Not involving relevant stakeholders from security, compliance,
  and business teams when defining data protection controls.
- Overlooking the operational overhead and costs associated with
  implementing and maintaining data protection controls.
- Not conducting periodic data protection control reviews to
  maintain alignment with classification policies.
- Not having a complete inventory of where data resides at rest
  and in transit.

**Benefits of establishing this best
practice:** By aligning your controls to the classification
level of your data, your organization can invest in higher levels of
control where needed. This can include increasing resources on
securing, monitoring, measuring, remediating, and reporting.  Where
fewer controls are appropriate, you can improve the accessibility
and completeness of data for your workforce, customers, or
constituents.  This approach gives your organization the most
flexibility with data usage, while still adhering to data protection
requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing data protection controls based on data sensitivity
levels involves several key steps. First, identify the different
data sensitivity levels within your workload architecture (such as
public, internal, confidential, and restricted) and evaluate where
you store and process this data. Next, define isolation boundaries
around data based on its sensitivity level. We recommend you
separate data into different AWS accounts, using
[service
control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") (SCPs) to restrict services and actions
allowed for each data sensitivity level. This way, you can create
strong isolation boundaries and enforce the principle of least
privilege.

After you define the isolation boundaries, implement appropriate
protection controls based on the data sensitivity levels. Refer to
best practices for [Protecting
data at rest](protecting-data-at-rest.md "protecting-data-at-rest.md") and
[Protecting data in
transit](protecting-data-in-transit.md "protecting-data-in-transit.md") to implement relevant controls like encryption,
access controls, and auditing. Consider techniques like
tokenization or anonymization to reduce the sensitivity level of
your data. Simplify applying consistent data policies across your
business with a centralized system for tokenization and
de-tokenization.

Continuously monitor and test the effectiveness of the implemented
controls. Regularly review and update the data classification
scheme, risk assessments, and protection controls as your
organization's data landscape and threats evolve. Align the
implemented data protection controls with relevant industry
regulations, standards, and legal requirements. Further, provide
security awareness and training to help employees understand the
data classification scheme and their responsibilities in handling
and protecting sensitive data.

### Implementation steps

1. Identify the classification and sensitivity levels of data
   within your workload.
2. Define isolation boundaries for each level and determine an
   enforcement strategy.
3. Evaluate the controls you define that govern access,
   encryption, auditing, retention, and others required by your
   data classification policy.
4. Evaluate options to reduce the sensitivity level of data where
   appropriate, such as using tokenization or anonymization.
5. Verify your controls using automated testing and monitoring of
   your configured resources.

## Resources

**Related best practices:**

- [PERF03-BP01
  Use a purpose-built data store that best supports your data
  access and storage requirements](../framework/perf_data_use_purpose_built_data_store.md "../framework/perf_data_use_purpose_built_data_store.md")
- [COST04-BP05
  Enforce data retention policies](../framework/cost_decomissioning_resources_data_retention.md "../framework/cost_decomissioning_resources_data_retention.md")

**Related documents:**

- [Data
  Classification whitepaper](../../../whitepapers/latest/data-classification/data-classification.md "../../../whitepapers/latest/data-classification/data-classification.md")
- [Best
  Practices for Security, Identify, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all "https://aws.amazon.com/architecture/security-identity-compliance/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all")
- [AWS KMS Best Practices](../../../kms/latest/developerguide/best-practices.md "../../../kms/latest/developerguide/best-practices.md")
- [Encryption
  best practices and features for AWS services](../../../prescriptive-guidance/latest/encryption-best-practices/welcome.md "../../../prescriptive-guidance/latest/encryption-best-practices/welcome.md")

**Related examples:**

- [Building
  a serverless tokenization solution to mask sensitive
  data](https://aws.amazon.com/blogs/compute/building-a-serverless-tokenization-solution-to-mask-sensitive-data/ "https://aws.amazon.com/blogs/compute/building-a-serverless-tokenization-solution-to-mask-sensitive-data/")
- [How
  to use tokenization to improve data security and reduce
  audit scope](https://aws.amazon.com/blogs/security/how-to-use-tokenization-to-improve-data-security-and-reduce-audit-scope/ "https://aws.amazon.com/blogs/security/how-to-use-tokenization-to-improve-data-security-and-reduce-audit-scope/")

**Related tools:**

- [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [AWS CloudHSM](https://aws.amazon.com/cloudhsm/ "https://aws.amazon.com/cloudhsm/")
- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
