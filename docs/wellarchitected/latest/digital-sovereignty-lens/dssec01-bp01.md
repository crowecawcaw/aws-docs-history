

# DSSEC01-BP01 Establish secure foundations aligned with regulatory requirements
<a name="dssec01-bp01"></a>

 Sovereign workloads carry regulatory obligations that are best met when security and sovereignty controls are part of the foundation rather than added later. A foundation with automated guardrails for data residency, jurisdictional access, and continuous compliance monitoring means teams can deploy new workloads without rebuilding these controls each time. 

 **Desired outcome:** 
+  Security, compliance, and sovereignty controls are built into the architecture from initial deployment. 
+  Automated guardrails enforce data residency, jurisdictional access controls, and continuous compliance monitoring aligned to regulatory requirements. 

 **Common anti-patterns:** 
+  Implementing security controls as an afterthought rather than building them into the foundational architecture. 
+  Relying on manual processes instead of automated, policy-driven controls. 
+  Using improvised security configurations without standardized baselines or compliance frameworks. 
+  Implementing security controls that don't meet regulatory requirements or the full lifecycle of compliance and audit obligations. 

 **Benefits of establishing this best practice:** 
+  Accelerates deployment timelines by providing pre-configured security controls and compliance frameworks. 
+  Maintains consistent security posture across accounts and workloads through automated governance. 
+  Simplifies audit and compliance reporting through built-in monitoring and logging capabilities. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Organizations in highly regulated industries need to establish security foundations that demonstrate compliance starting with initial deployment. For sovereign workloads, this might mean going beyond commonly applied security baselines to include additional data protection, data privacy, data residency, and digital sovereignty controls from the outset. 

 The [AWS Security Reference Architecture (SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html) provides the architectural blueprint for implementing security controls across your infrastructure layers. 

 Consider using solution accelerators to set up foundational landing zone capabilities. The [Landing Zone Accelerator (LZA) on AWS](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/solution-overview.html) automates the deployment of additional security controls, compliance frameworks, and governance policies. LZA provides infrastructure as code templates that implement security best practices and regulatory requirements across your multi-account environment. 

 You can find additional partner-built Landing Zone Accelerator solutions from the [AWS Digital Sovereignty Marketplace](https://aws.amazon.com/marketplace/solutions/digital-sovereignty). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set up a landing zone and enable digital sovereignty controls:** Start with [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) to establish your multi-account foundation. Enable Control Tower in your management account to create organizational units (OUs), baseline security controls, and centralized logging as part of the [landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/planning-your-deployment.html) set up process. Structure your OUs to reflect jurisdictional boundaries (for example, separate OUs for EU and non-EU workloads). Then evaluate and apply additional controls from the [Digital Sovereignty group](https://docs.aws.amazon.com/controltower/latest/controlreference/digital-sovereignty-controls.html). Key control categories to consider: 
   +  Digital sovereignty [preventive](https://docs.aws.amazon.com/controltower/latest/controlreference/ds-preventive-controls.html) controls. 
   +  Data residency [controls](https://docs.aws.amazon.com/controltower/latest/controlreference/data-residency-controls.html). 

    For detailed guidance on selecting, configuring, and validating individual controls, including Region deny parameters, workload-level preventive controls, and detective controls, see [DSSEC07-BP01 Enhance your digital sovereignty governance posture](dssec07-bp01.html). 

1.  **Automate landing zone setup with Landing Zone Accelerators:** Consider using pre-built [Landing Zone Accelerator (LZA) on AWS](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/solution-overview.html) to automate deployment of your landing zones. The Landing Zone Accelerator on AWS solution deploys a foundational set of capabilities that is designed to follow AWS best practices and [multiple global compliance frameworks](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/support-for-regions-and-industries.html). Consult the LZA [Compliance Workbook](https://aws.amazon.com/blogs/security/introducing-the-landing-zone-accelerator-on-aws-universal-configuration-and-lza-compliance-workbook/) to discover how the provided configurations map to compliance requirements (FedRAMP, C5, and HIPAA). Review the [Landing Zone Accelerator (LZA) Universal Configuration](https://github.com/aws/lza-universal-configuration) repository on GitHub and adapt it to your organization's needs. For region-specific compliance requirements, review these regional landing zone implementations: 
   +  [Baseline Informatiebeveiliging Overheid (BIO) for the Dutch Public Sector](https://aws.amazon.com/contract-center/bio-for-the-dutch-public-sector/). 
   +  [Spain's National Security Framework (ENS)](https://aws.amazon.com/blogs/security/ccn-releases-guide-for-spains-ens-landing-zones-using-landing-zone-accelerator-on-aws/). 
   +  [Germany's Cloud Computing Compliance Criteria Catalogue (C5)](https://aws.amazon.com/blogs/security/introducing-new-regional-implementations-of-landing-zone-accelerator-on-aws-to-support-digital-sovereignty/). 

    Validate that these regional implementations also meet your organization's own security requirements. The LZA solution will not, by itself, make you compliant. It provides the foundational infrastructure from which additional complementary solutions can be integrated. 

1.  **Implement security best practices and patterns for sovereign workloads:** 
   +  Sovereign workloads require layered security controls across network, identity, data, and application layers. Implement network segmentation, [VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) isolation, and centralized egress controls. Follow the [perimeter security](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/perimeter-security.html) guidance in the AWS SRA for detailed patterns. 
   +  Establish data perimeters using identity-based, network-based, and resource-based controls to block unauthorized access and accidental data exposure. Follow [Data Perimeter on AWS](https://aws.amazon.com/identity/data-perimeters-on-aws/) for guidance. Implement [data perimeter policy examples](https://github.com/aws-samples/data-perimeter-policy-examples) using service control policies and resource policies. 
   +  For workloads processing personal data, refer to the [AWS Privacy Reference Architecture (AWS PRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/pra.html). Consider creating a dedicated personal data (PD) organizational unit with enhanced controls for collecting, storing, and processing personal data. See the [PRA organization account structure](https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/organization-account-structure.html) for details. 

1.  **Apply industry-specific best practices:** 
   +  Review and implement industry-specific guidance from AWS Well-Architected Lenses that address unique regulatory and security requirements for your sector: 
     +  [Healthcare Industry Lens](https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/healthcare-industry-lens.html) for HIPAA and healthcare data protection 
     +  [Financial Services Industry Lens](https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/financial-services-industry-lens.html) for financial regulations and data security 
     +  [Government Lens](https://docs.aws.amazon.com/wellarchitected/latest/government-lens/government-lens.html?did=wp_card&trk=wp_card) for public sector compliance requirements 
   +  For specialized use cases or additional implementation guidance, explore [Prescriptive Guides](https://aws.amazon.com/prescriptive-guidance/?achp_navlib3), [Reference Architectures](https://aws.amazon.com/architecture/reference-architecture-diagrams/?achp_navlib4), and [Solution Accelerators](https://aws.amazon.com/solutions/) on the [AWS Architecture Center](https://aws.amazon.com/architecture/) that provide detailed implementation patterns for specific scenarios. 

 For guidance on selecting appropriate sovereign solution options to meet data residency and sovereignty requirements, see [DSPERF01-BP01 Evaluate sovereign solutions using a data-driven approach](dsperf01-bp01.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC01-BP01 Separate workloads using accounts](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_multi_accounts.html) 
+  [SEC01-BP02 Secure account root user and its properties](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_aws_account.html) 
+  [SEC01-BP03 Identify and validate control objectives](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_control_objectives.html) 
+  [SEC01-BP04 Stay up to date with security threats and recommendations](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_updated_threats.html) 
+  [SEC01-BP06 Automate deployment of standard security controls](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_automate_security_controls.html) 
+  [SEC01-BP07 Identify threats and prioritize mitigations using a threat model](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_threat_model.html) 
+  [SEC03-BP05 Define permission guardrails for your organization](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define_guardrails.html) 
+  [SEC08-BP01 Implement secure key management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_key_mgmt.html) 

 **Related documents:** 
+  [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html) 
+  [Landing Zone Accelerator on AWS Implementation Guide](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/solution-overview.html) 
+  [AWS Control Tower User Guide](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) 
+  [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) 
+  [AWS Compliance Center](https://aws.amazon.com/compliance/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Building Sovereign Cloud Environments (COP409)](https://www.youtube.com/watch?v=zxvDiXPl6_Q) 
+  [AWS re:Invent 2025 - AWS Security Hub CSPM: Unifying & simplifying security operations at scale (SEC228)](https://www.youtube.com/watch?v=mYyBQYIeJzk) 
+  [AWS Security Reference Architecture: Visualize your security - NDC Security 2024](https://www.youtube.com/watch?v=jGxS-7s-0sE) 

 **Related examples:** 
+  [Landing Zone Accelerator Sample Configurations](https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/main/reference/sample-configurations) 
+  [AWS Security Reference Architecture GitHub Repository](https://github.com/aws-samples/aws-security-reference-architecture-examples) 
+  [AWS Well-Architected Labs - Security](https://wellarchitectedlabs.com/security/) 

 **Related services:** 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) 
+  [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) 
+  [AWS KMS](https://aws.amazon.com/kms/) 
+  [Amazon Macie](https://aws.amazon.com/macie/) 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 