# DSREL01-BP05 Establish independent localized operations

Organizations in highly regulated industries must establish
independent localized operations across different geographical
regions. This maintains adherence to data sovereignty requirements
and regulatory mandates specific to each jurisdiction.

Localized operations enable autonomous workload management within
specific regions. You can enforce local data residency requirements
and comply with regional regulations such as GDPR, HIPAA, or CCPA.
This approach assists in managing cross-border risks while
maintaining operational agility and meeting the needs of local users
and regulatory authorities.

**Desired outcome:** Organizations
maintain autonomous Regional operations with isolated data
processing, storage, and governance capabilities. Local regulations
and data residency requirements are met through Region-specific
compliance controls. Security standards and operational efficiency
remain consistent across each jurisdiction.

**Common anti-patterns:**

- Operating from a single central AWS Region without considering
  data sovereignty requirements, using shared resources across
  jurisdictions, and failing to properly segment networks and
  isolate regional operations.
- Implementing centralized, uniform compliance policies and IAM
  controls without accounting for local regulatory variations or
  region-specific requirements.
- Not implementing proper data classification and handling
  procedures based on local sensitivity requirements, storing
  regulated and non-regulated data in shared systems without
  proper separation.
- Using global edge services and CDNs without appropriate
  geo-restrictions, regional controls, and region-specific
  encryption controls.

**Benefits of establishing this best
practice:**

- Regulatory requirements are met through adherence to local data
  protection laws and industry-specific regulations while enabling
  Region-specific audit trails.
- Strengthens data sovereignty by maintaining complete control
  over data location and processing boundaries, minimizing
  exposure to cross-region breaches and legal penalties.
- Enhances operational resilience through independent regional
  operations that can continue functioning during disruptions
  without impacting other Regions.
- Improves performance and user experience by reducing latency
  through geographically distributed operations that keep data
  closer to users.
- Simplifies compliance reporting and auditing through clear
  regional separation and jurisdiction-specific documentation.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Establish independent localized operations through a strategic,
multi-phase approach. Start with a comprehensive regulatory
assessment to understand specific requirements for each localized
Region and operation. Document data residency mandates, processing
restrictions, and compliance frameworks specific to each local
jurisdiction.

Design your architecture with clear Regional boundaries. Use
separate AWS accounts and dedicated resources for each
jurisdiction. This provides complete operational, security, and
billing isolation.

Implement Region-specific governance policies and operational
procedures that align with local requirements. Maintain your
overall security posture and operational excellence across each
Region. Support your implementation with local teams who
understand both the technical and regulatory landscape of their
Region.

Consider data classification, data protection requirements, and
access controls carefully. These elements are crucial for
maintaining regulatory compliance while operating efficiently
across multiple jurisdictions.

Key implementation elements:

- Deploy workloads in AWS Regions aligned with regulatory
  requirements
- Use AWS Organizations to enforce Region-specific guardrails
- Implement data classification and encryption at rest and in
  transit

### Implementation steps

1. Develop a regulatory assessment framework for each target
   Region. Document data protection laws, processing
   requirements. Create a compliance matrix and engage legal
   and compliance teams for validation.
2. Configure
   [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/") with Region-specific and
   compliance-based OUs. Implement service control policies and
   [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/") to set up guardrails.
3. Implement a multi-account structure for each Region using
   [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/"). Create production, development, shared
   services, and security accounts per Region. Document the
   account hierarchy and relationships.
4. Define an encryption strategy within a Region. The strategy
   should include the type of encryption keys, secure key
   storage, key policies, access controls and key rotation. Use
   relevant AWS services such as
   [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") and
   [AWS CloudHSM](https://aws.amazon.com/cloudhsm/ "https://aws.amazon.com/cloudhsm/").
5. Design and configure network architecture for Regional
   segmentation. Use relevant AWS services such as
   [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/"),
   [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/") or
   [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/") to provide network segmentation, security
   controls and connectivity in each Region.

## Resources

**Related best practices:**

- [SEC09-BP02
  Enforce encryption in transit](../security-pillar/sec_protect_data_transit_encrypt.md "../security-pillar/sec_protect_data_transit_encrypt.md")
- [SEC08-BP02
  Enforce encryption at rest](../security-pillar/sec_protect_data_rest_encrypt.md "../security-pillar/sec_protect_data_rest_encrypt.md")
- [DRHCSEC03-BP01
  Implement controls that enhance your digital sovereignty
  governance posture](../data-residency-hybrid-cloud-services-lens/drhcsec03-bp01.md "../data-residency-hybrid-cloud-services-lens/drhcsec03-bp01.md")

**Related documents:**

- [AWS Organizations User Guide](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")
- [Data Residency with Hybrid Cloud Services Lens](../data-residency-hybrid-cloud-services-lens/data-residency-with-hybrid-cloud-services-lens.md "../data-residency-hybrid-cloud-services-lens/data-residency-with-hybrid-cloud-services-lens.md")

**Related videos:**

- [AWS re:Inforce 2025-Navigating sovereignty requirements:
  Architectures and solutions on AWS (DAP202)](https://www.youtube.com/watch?v=Eq0K0pxRjRk "https://www.youtube.com/watch?v=Eq0K0pxRjRk")

**Related services:**

- [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/")
- [AWS CloudHSM](https://aws.amazon.com/cloudhsm/ "https://aws.amazon.com/cloudhsm/")
- [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/")
- [AWS Resource Groups](https://aws.amazon.com/resource-groups/ "https://aws.amazon.com/resource-groups/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/")
