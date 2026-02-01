# DSOPS02-BP01 Baseline your compliance requirements

Baselining your compliance requirements is crucial for making sure
that your organization maintains a consistent and secure posture. It
assists in proactively identifying gaps, reducing risks, and
maintaining adherence to regulatory standards.

**Desired outcome:** Your
organization has a clear, authoritative understanding of compliance
requirements that guides design decisions, accelerates workload
deployment, and reduces risk across AWS environments.

**Common anti-patterns:**

- Making decisions based on informal understanding rather than
  documented requirements.
- Applying the same compliance controls across workloads without
  considering specific regulatory requirements.
- Only identifying requirements after a compliance issue or audit
  finding occurs.
- Creating compliance baselines once and rarely updating them as
  regulations evolve.

**Benefits of establishing this best
practice:**

- Risk reduction through proactive identification and mitigation
  of compliance gaps.
- Cost optimization by implementing appropriate controls without
  over-engineering solutions.
- Faster deployment of compliant workloads using pre-approved
  architectural patterns.
- Improved audit readiness with clear documentation and evidence
  of compliance consideration.
- Enhanced stakeholder confidence through demonstrated commitment
  to regulatory adherence.
- Streamlined decision-making with clear compliance criteria for
  design choices.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Begin by conducting a comprehensive assessment of your
organization's compliance landscape, including industry-specific
regulations, jurisdictional requirements, and internal policies.
Engage legal, compliance, and business stakeholders to
holistically cover applicable requirements. Document each
requirement with sufficient detail to enable technical
implementation decisions, including specific controls, evidence
requirements, and assessment criteria.

### Implementation steps

1. **Define a compliance
   matrix**: Create a compliance matrix, mapping
   regulatory requirements to specific technical controls and
   processes. As examples, refer to the
   [Secure
   Controls Framework (SCF)](https://github.com/securecontrolssecurity-pillar/securecontrolsframework/tree/main "https://github.com/securecontrolssecurity-pillar/securecontrolsframework/tree/main") and download the latest
   secure-controls-framework-scf-[version].xlsx
   file. Use the
   [AWS Customer Compliance Guides (CCGs)](https://d1.awsstatic.com/whitepapers/compliance/AWS_Customer_Compliance_Guides.pdf "https://d1.awsstatic.com/whitepapers/compliance/AWS_Customer_Compliance_Guides.pdf") and the attached
   excel file in the document to find a full complement of AWS
   built controls categorized by services, compliance
   standards, and security topics. The two resources could
   serve as a potential starting point to map named compliance
   frameworks to equivalent preventative, proactive, and
   detective controls listed under
   [AWS Control Tower](../../../controltower/latest/controlreference/controls-reference.md "../../../controltower/latest/controlreference/controls-reference.md"), controls managed by
   [AWS Security Hub CSPM](../../../securityhub/latest/userguide/controls-view-manage.md "../../../securityhub/latest/userguide/controls-view-manage.md") and managed rules provided by
   [AWS Config](../../../config/latest/developerguide/managed-rules-by-aws-config.md "../../../config/latest/developerguide/managed-rules-by-aws-config.md").

The following table is an example of a compliance mapping
matrix. The first four columns state the
_organization control id_,
_framework control id_,
_category_ and
_subcategory_. The _policy
directive_ column translates a framework
requirement (known as Complementary Customer Criteria in C5
terminology) to instructions describing how this requirement
should be met when using a specific technology capability.
The technology capability in this example is object storage.
Relational database, message queue, volume storage, and
network attached storage are few of the other examples. The
_candidate controls_ column list the
technical controls (expressed as policy as code) required to
meet the policy directive. The control mapping shown below
is only for illustration purposes. It is not accurate and is
just one among several possible interpretations. The
_validation rules_ column informs
developers on the pass criteria.

For illustration, the example uses the
[Cloud
Computing Compliance Criteria Catalogue – C5](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/CloudComputing/ComplianceControlsCatalogue/2020/C5_2020.pdf "https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/CloudComputing/ComplianceControlsCatalogue/2020/C5_2020.pdf")
published in 2020 by the Federal Office for Information
Security (BSI) of Germany. C5 serves as a foundation in the
area of cloud security for providers, customers, and
auditors. In the example shown here, a compliance
requirement is named CRY-03. For full text refer to Section
5.8, CRY-03 of
[Criteria
Catalogue C5:2020](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/CloudComputing/ComplianceControlsCatalogue/2020/C5_2020.pdf "https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/CloudComputing/ComplianceControlsCatalogue/2020/C5_2020.pdf").

| Organization Control Id | C5-Control Id                                   | Category           | Subcategory    | Policy Directive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Candidate Controls                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Validation Rules                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------- | ----------------------------------------------- | ------------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ENC-001-R               | CRY-03 Encryption of sensitive data for storage | Encryption at rest | Object storage | **(1)\*<br>• Do not<br>configure object storage solutions with default<br>cloud provider managed encryption keys.<br>**(2)\*<br>• Generate key<br>material outside of the cloud provider's environment<br>using an independent toolchain. Use the cloud<br>provider's key management tools and the key material<br>you built, to generate new keys. Save the generated<br>keys to the cloud provider's key vault. Validate<br>that the key vault is at least FIPS 140-3 Level 3<br>compliant. Also use secure channels during key<br>exchanges. **(3)**<br>Consider using dedicated HSMs and external key<br>stores for data classified confidential or above.<br>This allows you to store keys outside of cloud<br>provider's key vault and specify where the<br>encryption/decryption operations are performed. | [CT.S3.PR.10](../../../controltower/latest/controlreference/s3-rules.md#ct-s3-pr-10-description "../../../controltower/latest/controlreference/s3-rules.md#ct-s3-pr-10-description"):<br>Require an Amazon S3 bucket to have server-side<br>encryption configured using an AWS KMS key.<br>[CT.S3.PV.6](../../../controltower/latest/controlreference/list-of-rcp-controls.md#ct-s3-pv-6 "../../../controltower/latest/controlreference/list-of-rcp-controls.md#ct-s3-pv-6"):<br>Require object uploads to Amazon S3 buckets to use<br>server-side encryption with an AWS KMS key<br>(SSE-KMS).[SH.S3.17](../../../securityhub/latest/userguide/s3-controls.md#s3-17 "../../../securityhub/latest/userguide/s3-controls.md#s3-17"):<br>S3 buckets should be encrypted at rest with AWS KMS<br>keys. Add more controls | For up to restricted data sensitivity levels, the<br>following rules apply:<br>**(1)\*<br>• SSE-KMS is<br>enabled as default.<br>**(2)_<br>• KMS key used<br>was built using<br>[imported<br>key material](../../../kms/latest/developerguide/importing-keys-conceptual.md "../../../kms/latest/developerguide/importing-keys-conceptual.md").<br>\*\*(3)_<br>• Users pass<br>the<br>x-amz-server-side-encryption-aws-kms-key-id<br>header element during<br>s3:PutObject operations for<br>buckets which are not configured with SSE-KMS. For<br>confidential and highly-confidential data<br>sensitivity levels, follow separate guidance on<br>provided with ENC-001-CH |

    * CT.S3.PR.10 is a proactive control implemented in the
     form of an
     [AWS CloudFormation guard rule](../../../cfn-guard/latest/ug/writing-rules.md "../../../cfn-guard/latest/ug/writing-rules.md"). It acts as a
     check-point during resource provisioning and is invoked
     when you use CloudFormation templates or the
     CloudFormation CDK to provision S3 buckets. However, if
     your aim is to block non-compliant S3 buckets from being
     provisioned when using other infrastructure as code
     (IaC) tools, this control alone would not be sufficient.
     To achieve a similar outcome, first build a
     [CloudFormation
     hook](../../../cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.md "../../../cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.md") and add the
     [guard
     rule specification](../../../controltower/latest/controlreference/s3-rules.md#ct-s3-pr-10-rule "../../../controltower/latest/controlreference/s3-rules.md#ct-s3-pr-10-rule") described as part of
     CT.S3.PR.10. Then provision your S3 bucket using an IaC
     provider such as
     [Terraform](https://registry.terraform.io/providers/hashicorp/awscc/latest "https://registry.terraform.io/providers/hashicorp/awscc/latest"),
     or
     [Pulumi](https://www.pulumi.com/registry/packages/aws-native/api-docs/ "https://www.pulumi.com/registry/packages/aws-native/api-docs/")
     that supports the
     [AWS Cloud Control API (CCAPI)](https://aws.amazon.com/cloudcontrolapi/ "https://aws.amazon.com/cloudcontrolapi/"). For more detail, see
     [Introducing
     AWS CloudFormation Hooks invoked via AWS Cloud Control
     API (CCAPI)](https://aws.amazon.com/blogs/devops/introducing-aws-cloudformation-hooks-invoked-via-aws-cloud-control-api-ccapi/ "https://aws.amazon.com/blogs/devops/introducing-aws-cloudformation-hooks-invoked-via-aws-cloud-control-api-ccapi/").
    * CT.S3.PV.6 is a resource control policy (RCP). It
     requires users to supply a KMS key ID as part of the
     header in S3:PutObject requests for
     buckets that do not have SSE-KMS configured as the
     default encryption mode. SH.S3.17 is an AWS Config
     managed rule that checks whether an S3 bucket is
     encrypted with an KMS key (SSE-KMS or DSSE-KMS). All
     three controls can be enabled at an Organization Unit
     (OU) or an account level using AWS Control Tower.

Developing and keeping compliance mapping matrix documents
and databases up to date requires input from more than a one
team. In the example shown here, security and compliance
SMEs may be providing inputs for the organization control
id, framework control id, category, subcategory, and policy
directives columns while SecOps and DevSecOps teams may be
responsible for filling up the candidate controls and
validation rules columns. 2. **Document jurisdiction specific
requirements**: Document jurisdiction specific (for
example, regional union, country, trading bloc, province)
cybersecurity, data privacy and data export controls
requirements. Incorporate these additional requirements into
your compliance matrix.

    * Document guidelines around data export controls. This
     includes bi-lateral or multi-lateral
     [adequacy
     arrangements](https://ico.org.uk/for-organisations/data-protection-and-the-eu/data-protection-and-the-eu-in-detail/adequacy/ "https://ico.org.uk/for-organisations/data-protection-and-the-eu/data-protection-and-the-eu-in-detail/adequacy/") you may need to adhere to.
    * Document legal requirements for workforce location and
     citizenship-related restrictions. Operational roles in
     domains such as defence, military and law enforcement
     may require additional vetting.
    * Document cryptographic standards and policies.
    * Document mandatory public disclosure requirements. For
     example, tracking how many data disclosure requests you
     received from law enforcement agencies, and how many did
     you fulfil.
    * Document data breach reporting procedures. This should
     include what to report, whom to report to and within
     what timelines.
    * Document intellectual property rights requirements.
    * Validate requirements through reviews with local legal
     experts and your own compliance teams. Seek
     clarifications from regulators and designated national
     competent authorities.
    * Additionally, consider documenting the potential
     economic impact of meeting regulations (cost of
     regulation). This guides yearly planning and budgeting.

3. **Build a comprehensive knowledge
   base:** Make compliance mappings searchable,
   accessible, and understandable to improve awareness and
   reusability.
   - Include descriptive text and guidance.
   - Make prior certifications and attestations readily
     available to the wider organization.
   - Use advanced analytics methods. For example, large
     language models (LLMs), retrieval-augmented generation
     (RAG) search, and knowledge graphs to make
     compliance-related literature more accessible.

4. **Conduct gap analysis**:
   Discover potential gaps in your compliance posture.
   - Conduct data protection impact analysis (DPIAs) where
     there is a high risk of non-compliance due to the
     location and sensitivity of the data involved.
   - A quick way to spot compliance issues would be to enable
     AWS Security Hub CSPM. Then, enable a
     [Security Hub standard](../../../securityhub/latest/userguide/standards-reference.md "../../../securityhub/latest/userguide/standards-reference.md") to automatically start collecting
     data about non-compliant resources. Compliance findings
     are displayed on the Security Hub CSPM
     [dashboard](../../../securityhub/latest/userguide/dashboard.md "../../../securityhub/latest/userguide/dashboard.md").

5. **Log and manage risks**:
   Maintain a risk register. Log and manage compliance-related
   risks that cannot be addressed by the current design.
   Document compensatory measures applied to partially or fully
   mitigate risks.
6. **Review compliance
   baselines**: Update baselines periodically to
   address emerging threats and regulatory changes. Re-assess
   compliance requirements per jurisdiction and industry. Stay
   tuned to updates coming from regulatory authorities.

## Resources

**Related best practices:**

- [OPS01-BP03
  Evaluate governance requirements](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_priorities_governance_reqs.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_priorities_governance_reqs.md")
- [OPS01-BP04
  Evaluate compliance requirements](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_priorities_compliance_reqs.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_priorities_compliance_reqs.md")
- [SEC02-BP01:
  Use strong identity foundation](../security-pillar/sec_identities_enforce_mechanisms.md "../security-pillar/sec_identities_enforce_mechanisms.md")

**Related documents:**

- [Implementing
  a compliance and reporting strategy for NIST SP 800-53
  Rev. 5](https://aws.amazon.com/blogs/security/implementing-a-compliance-and-reporting-strategy-for-nist-sp-800-53-rev-5/ "https://aws.amazon.com/blogs/security/implementing-a-compliance-and-reporting-strategy-for-nist-sp-800-53-rev-5/")
- [Scaling
  a governance, risk, and compliance program for the
  cloud](https://aws.amazon.com/blogs/security/scaling-a-governance-risk-and-compliance-program-for-the-cloud/ "https://aws.amazon.com/blogs/security/scaling-a-governance-risk-and-compliance-program-for-the-cloud/")
- [AWS Security Reference Architecture (SRA)](../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md "../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md")
- [AWS Risk and Compliance Whitepaper](../../../whitepapers/latest/aws-risk-and-compliance/welcome.md "../../../whitepapers/latest/aws-risk-and-compliance/welcome.md")
- [Exploring
  the new AWS European Sovereign Cloud: Sovereign Reference
  Framework](https://aws.amazon.com/blogs/security/exploring-the-new-aws-european-sovereign-cloud-sovereign-reference-framework/ "https://aws.amazon.com/blogs/security/exploring-the-new-aws-european-sovereign-cloud-sovereign-reference-framework/")
- [Architecting
  for HIPAA Security and Compliance on Amazon Web Services](../../../whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/welcome.md "../../../whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/welcome.md")
- [AWS Config Conformance Packs](../../../config/latest/developerguide/conformance-packs.md "../../../config/latest/developerguide/conformance-packs.md")
- [AWS Security Hub Compliance Standards](../../../securityhub/latest/userguide/standards-reference.md "../../../securityhub/latest/userguide/standards-reference.md")
- [AWS Artifact User Guide](../../../artifact/latest/ug/what-is-aws-artifact.md "../../../artifact/latest/ug/what-is-aws-artifact.md")
- [AWS Audit Manager User Guide](../../../audit-manager/latest/userguide/what-is.md "../../../audit-manager/latest/userguide/what-is.md")

**Related videos:**

- [Global
  Security & Compliance Acceleration Program](https://www.youtube.com/watch?v=BJWQ_DPbp1U "https://www.youtube.com/watch?v=BJWQ_DPbp1U")
- [Global
  Security & Compliance Acceleration (GSCA) Bundles](https://www.youtube.com/watch?v=W6jlDur1Yos "https://www.youtube.com/watch?v=W6jlDur1Yos")
- [AWS re:Inforce 2022 - Quantifying your compliance posture with
  conformance packs (GRC211)](https://www.youtube.com/watch?v=t3tCfEySDxI "https://www.youtube.com/watch?v=t3tCfEySDxI")
