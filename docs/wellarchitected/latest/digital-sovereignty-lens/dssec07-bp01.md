# DSSEC07-BP01 Establish data sovereignty controls aligning with

regional data residency requirements

In highly regulated industries, you need to implement data sovereignty controls. These are
controls designed to meet requirements related to data residency, access restrictions, and
regulatory adherence. They assist in securing sensitive data while maintaining operational
efficiency.

Effective data sovereignty controls provide the foundation for regulatory adherence,
customer trust, and operational resilience in multi-jurisdictional environments.

**Desired outcome:** Sensitive data remains within designated
geographic boundaries through automated, verifiable controls. You maintain adherence to regional
data protection regulations and possess audit-ready evidence of data sovereignty measures.
Regulatory requirements are met while operational efficiency is preserved across jurisdictions.

**Common anti-patterns:**

- Relying solely on contractual agreements without technical enforcement mechanisms to
  enforce data residency.
- Implementing data residency controls as an afterthought rather than embedding them into
  the architecture from the beginning.
- Applying uniform data sovereignty controls across data types without considering
  sensitivity levels and regulatory requirements.
- Failing to implement monitoring and alerting for data sovereignty violations.

**Benefits of establishing this best practice:**

- Enhanced adherence assurance through automated enforcement of data residency
  requirements and detailed audit trails.
- Reduced compliance costs through automated controls that reduce manual oversight and
  reduce audit preparation time.
- Enhanced customer trust by demonstrating verifiable commitment to data sovereignty and
  privacy protection.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Begin by conducting a data classification and analysis exercise. Identify sensitive data
types and potential data sovereignty attributes. Implement a layered approach using AWS
services. Use services that provide built-in data residency controls, automated monitoring,
and audit capabilities. Deploy preventive controls to block unauthorized data movement,
detective controls to monitor compliance, and responsive controls to remediate violations
automatically. Choose appropriate AWS infrastructure options (for example, AWS Region,
AWS Outposts, Dedicated Local Zones) to further restrict data residency.

Key AWS services for data sovereignty implementation include AWS Control Tower for
organizational guardrails and AWS Config for compliance monitoring. Also use AWS CloudTrail for audit
logging and AWS Organizations for policy enforcement. Use AWS KMS with customer-managed keys in specific
Regions, Amazon S3 with bucket policies restricting cross-Region replication, and AWS IAM with
location-based conditions. These services establish effective data sovereignty controls.

### Implementation steps

1. **Understand your data residency needs**: Data privacy
   legislations such as European Union General Data Protection Regulation (EU GDPR) don't
   explicitly state requirements related to data residency or data export controls.
   However, many privacy legislations including EU GDPR, UK GDPR, and India's Digital
   Personal Data Protection Act, 2023 (DPDP), introduce a concept of adequacy. For example,
   under EU GDPR we have [Art 45 Transfers on
   the basis of an adequacy decision](https://gdpr-info.eu/art-45-gdpr/ "https://gdpr-info.eu/art-45-gdpr/"). It states that

A transfer of personal data to a third country or an international organisation may
take place where the Commission has decided that the third country, a territory or one
or more specified sectors within that third country, or the international organisation
in question ensures an adequate level of protection.

Based on these principles, the EU has established adequacy arrangements with the
UK, with the U.S (under the [EU-US Data
Privacy Framework](https://ec.europa.eu/commission/presscorner/detail/en/qanda_23_3752 "https://ec.europa.eu/commission/presscorner/detail/en/qanda_23_3752")) and with [Japan](https://ec.europa.eu/commission/presscorner/detail/en/ip_19_421 "https://ec.europa.eu/commission/presscorner/detail/en/ip_19_421").
In practical terms it means personal data can flow between these jurisdictions. But you
must consult privacy and legal experts before baselining your requirements. Primarily
because the type of data you may want to transfer could be subject to additional
sectoral controls.

For instance the Reserve Bank of India (RBI) has additional guidance requiring
payment-related data to be stored locally. As does the Telecom Regulatory Authority of
India (TRAI) for telecom related data. Furthermore, national competent authorities often
provide new clarifications and exemptions. For example, the UAE's Ministry of Health and
Prevention (MoHAP) issued [this clarification](https://uaephl.mohap.gov.ae/en/health-policies-and-legislations-advocacy/health-legislations?itemId=726efdef-580e-4817-bf5a-fbf8e53fddfc "https://uaephl.mohap.gov.ae/en/health-policies-and-legislations-advocacy/health-legislations?itemId=726efdef-580e-4817-bf5a-fbf8e53fddfc") regarding the transfer of healthcare data. 2. **Establish organizational level data residency controls**:
Deploy AWS Control Tower with digital sovereignty controls enabled to create secure,
compliant multi-account environments. Enable the following key controls:

    * CT.MULTISERVICE.PV.1 Region deny control to restrict operations to approved
     regions
    * Data residency detective controls to monitor public access and cross-region
     data movement
    * Encryption controls to provide data protection at rest and in transit
    * Here's an example of enabling CT.MULTISERVICE.PV.1:

```

# Enable region deny control for an OU. Allow only us-east-1 and us-west-2. But also add exempted actions and principals.
AWS controltower enable-control \
    --target-identifier arn:aws:organizations::01234567890:ou/o-EXAMPLE/ou-zzxx-zzx0zzz2 \
    --control-identifier arn:aws:controltower:us-east-1::control/EXAMPLE_NAME \
    --parameters '[{"key":"AllowedRegions","value":["us-east-1","us-west-2"]},{"key":"ExemptedPrincipalArns","value":["arn:aws:iam::*:role/ReadOnly","arn:aws:sts::*:assumed-role/ReadOnly/*"]},{"key":"ExemptedActions","value":["logs:DescribeLogGroups","logs:StartQuery","logs:GetQueryResults"]}]'

```

See [Region deny control
applied to the OU](../../../controltower/latest/controlreference/ou-region-deny.md "../../../controltower/latest/controlreference/ou-region-deny.md") in the AWS Control Tower documentation for more options. 3. **Deploy preventive controls aligned to individual
workloads**: In addition to the region deny control which acts at an OU
(Organizational Unit) level, Control Tower provides several digital sovereignty related
preventative controls. These controls can be applied to protect [individual
workloads](../../../controltower/latest/controlreference/ds-preventive-controls.md "../../../controltower/latest/controlreference/ds-preventive-controls.md"). Consider enabling these controls to meet workload specific
compliance requirements. For example, [CT.KMS.PV.6](../../../controltower/latest/controlreference/ct-kms-pv-6.md "../../../controltower/latest/controlreference/ct-kms-pv-6.md")
requires that the AWS KMS customer-managed key (CMK) is configured with a key material
originating from an external key store (XKS) only. 4. **Deploy additional data residency controls**: Beyond data
residency controls shown in Step 1, consider applying additional controls to block
cross-region networking, VPC peering, Transit Gateway peering or VPN Connections. For
more options, see [Data residency controls with preventive behavior](../../../controltower/latest/controlreference/data-residency-preventive-controls.md "../../../controltower/latest/controlreference/data-residency-preventive-controls.md"). 5. **Deploy data residency detective controls**: Deploy
controls to continuously monitor data sovereignty compliance. See [Data
residency controls with detective behavior](../../../controltower/latest/controlreference/data-residency-detective-controls.md "../../../controltower/latest/controlreference/data-residency-detective-controls.md") for more options. See [Detect whether Amazon S3 settings to block public access are set as true for the
account](../../../controltower/latest/controlreference/data-residency-detective-controls.md#s3-account-level-public-access-blocks-periodic "../../../controltower/latest/controlreference/data-residency-detective-controls.md#s3-account-level-public-access-blocks-periodic") to understand how such controls work. 6. **Implement key management restrictions**: AWS creates
and stores KMS keys in specific AWS Regions. You cannot use a KMS key from one Region
to encrypt or decrypt data in another Region. You can further restrict key usage to
specific accounts and principals, thus enabling workload level isolation. Using a
dedicated AWS Cloud HSM infrastructure or by using a dedicated external key store
(AWS KMS XKS), you can further:

    * Restrict where keys are stored
    * Where encryption/decryption operations occur

Additionally, with XKS, you even control the physical location and the provider of
the HSM devices enabling you to perform encryption/decryption operations outside of
AWS Cloud. 7. **Choose appropriate AWS Infrastructure**: The [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/") provides you several infrastructure solutions and options.
Those include:

    * [AWS Regions](../../../global-infrastructure/latest/regions/aws-regions.md "../../../global-infrastructure/latest/regions/aws-regions.md"):
     Standard multi-tenant cloud infrastructure.
    * [AWS GovCloud](https://aws.amazon.com/govcloud-us/ "https://aws.amazon.com/govcloud-us/"): Dedicated
     infrastructure for US government workloads.
    * [AWS European Sovereign Cloud](https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-announcing-a-new-independent-sovereign-cloud-in-europe/ "https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-announcing-a-new-independent-sovereign-cloud-in-europe/"): Infrastructure wholly located within the
     European Union (EU) and supported by EU residents only.
    * [AWS Dedicated Local
     Zones](https://aws.amazon.com/dedicatedlocalzones/ "https://aws.amazon.com/dedicatedlocalzones/"): Configurable infrastructure that aligns with your data isolation,
     in-country data residency, and digital sovereignty needs. Can be deployed to a
     location you choose.
    * [AWS
     Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/"): Run applications on AWS infrastructure closer to your end
     users and workloads.
    * [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/"): Run AWS infrastructure
     and services on-premises.

Develop selection criteria to choose one or a continuum of infrastructure options.
Consider the following factors:

    * Sensitivity and the type of the data you will be processing. How does the
     sensitivity or data type affect your residency requirements?
    * Sovereign or sectoral mandates. As discussed in Step 1, sovereign data privacy
     legislations or industry regulations may demand data to be located within specific
     jurisdictions.
    * The operational responsibilities you are willing to accept. For example, when
     you deploy AWS Outpost on your own managed infrastructure, you are responsible for
     aspects such as physical security, power supply among other things.
    * Citizenship, residency, and security vetting requirements for operators
     supporting your workloads.
    * Your technology requirements. AWS Regions, AWS GovCloud, and AWS European
     Sovereign Cloud offer the broadest range of AWS services. Local Zones, Dedicated
     Local Zone and AWS Outposts offer a different mix of AWS Services. See the resources
     section.
    * Security services and tooling required. Here's an [overview of security services and tooling](https://aws.amazon.com/blogs/security/overview-of-security-services-available-in-aws-dedicated-local-zones/ "https://aws.amazon.com/blogs/security/overview-of-security-services-available-in-aws-dedicated-local-zones/") available with Dedicated Local
     Zones.
    * Interoperability and portability requirements. Several AWS Services align
     with their open-source counterparts. Examples include Amazon OpenSearch Service, Amazon Managed
     Workflows for Apache Airflow (MWAA), Amazon Keyspaces (for Apache Cassandra) (for Apache Cassandra), and
     Amazon ElastiCache (Redis OSS). In addition, Dedicated Local Zones, Local Zones and Outposts offer
     Amazon Elastic Kubernetes Service. This allows you to deploy Kubernetes workloads across the continuum from
     AWS Regions to AWS Outposts.
    * Requirements related to survivability. AWS provides [different isolation boundaries](../../../whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.md"), such as Availability Zones, Regions,
     control planes, and data planes. Choose infrastructure aligning with your business
     continuity goals.
    * Performance requirements. Consider your compute, storage, and networking
     requirements.
    * Costs. [Pricing](https://aws.amazon.com/outposts/rack/pricing/ "https://aws.amazon.com/outposts/rack/pricing/") for
     AWS Outposts racks, is different from [pricing](https://aws.amazon.com/about-aws/global-infrastructure/localzones/pricing/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/pricing/") for
     AWS Local Zones. Use [AWS Pricing Calculator](https://calculator.aws/#/ "https://calculator.aws/#/") to
     understand what works best for you.
    * Flexibility. Factor in business growth and the infrastructure required to
     support this growth. How often will you need additional capacity? How long are you
     willing to wait for this capacity to come on-line?

## Resources

**Related best practices:**

- [SEC02-BP01 Use strong sign-in mechanisms](../security-pillar/sec_identities_enforce_mechanisms.md "../security-pillar/sec_identities_enforce_mechanisms.md")
- [SEC07-BP01 Understand your data classification scheme](../security-pillar/sec_data_classification_identify_data.md "../security-pillar/sec_data_classification_identify_data.md")
- [SEC08-BP01 Implement secure key management](../security-pillar/sec_protect_data_rest_key_mgmt.md "../security-pillar/sec_protect_data_rest_key_mgmt.md")
- [SEC08-BP02 Enforce encryption at rest](../security-pillar/sec_protect_data_rest_encrypt.md "../security-pillar/sec_protect_data_rest_encrypt.md")
- [OPS01-BP04 Evaluate compliance requirements](../operational-excellence-pillar/ops_priorities_compliance_reqs.md "../operational-excellence-pillar/ops_priorities_compliance_reqs.md")

**Related documents:**

- [AWS
  Digital Sovereignty Pledge: Control without compromise](https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/ "https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/")
- [AWS Control Tower Digital Sovereignty Controls](../../../controltower/latest/controlreference/digital-sovereignty-controls.md "../../../controltower/latest/controlreference/digital-sovereignty-controls.md")
- [Data residency
  controls in AWS Control Tower](../../../controltower/latest/controlreference/data-residency-controls.md "../../../controltower/latest/controlreference/data-residency-controls.md")
- [AWS GDPR Center](https://aws.amazon.com/compliance/gdpr-center/ "https://aws.amazon.com/compliance/gdpr-center/")
- [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/")
- [AWS Local
  Zones features and Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/?nc=sn&loc=2 "https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/?nc=sn&loc=2")
- [AWS Dedicated Local Zones
  features - See "Your choice of services"](https://aws.amazon.com/dedicatedlocalzones/features/ "https://aws.amazon.com/dedicatedlocalzones/features/")

**Related videos:**

- [AWS re:Invent 2025 - AWS
  European Sovereign Cloud: From concept to reality (SEC201)](https://www.youtube.com/watch?v=L4rNxZJaCuc "https://www.youtube.com/watch?v=L4rNxZJaCuc")

**Related services:**

- [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/")
