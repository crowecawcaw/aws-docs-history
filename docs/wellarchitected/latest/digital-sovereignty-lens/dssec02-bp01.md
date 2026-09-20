

# DSSEC02-BP01 Protect data through layered access controls within sovereign boundaries
<a name="dssec02-bp01"></a>

 Access control is one of the lens's five sovereignty design concerns: who can reach your data, from where, and under what authority. A single control layer leaves gaps, because network controls alone can't enforce identity rules and identity controls alone can't account for network paths. Layering network-centric and identity-centric controls, in proportion to data sensitivity and jurisdiction, keeps data within its sovereign boundary and blocks unauthorized access before it happens. 

 **Desired outcome:** 
+  Data remains accessible only to authorized users and services within its designated sovereign boundary, and unauthorized access is blocked before it occurs. 
+  Network-centric and identity-centric controls work together as layered preventive boundaries rather than relying on detection after access occurs. 
+  Operator access is constrained, and every access path is auditable, so you can demonstrate sovereign control to regulators. 

 **Common anti-patterns:** 
+  Zone of trust isn't known or not clearly established. 
+  Relying on a single layer of defense. For example, using only detective controls to detect violations, rather than applying preventive controls to stop violations in the first place. 
+  Not considering cross-service and intra-service data flows across AWS Regions. 

 **Benefits of establishing this best practice:** 
+  Maintain adherence to regional data sovereignty requirements. 
+  Developers can modify and extend application functionality without inadvertently exposing data. 
+  Improve transparency and visibility of data access controls leading to better auditability. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Access control measures designed to improve the sovereignty posture of your workload are driven by data localization mandates, data residency requirements, data sovereignty requirements, industry regulations (such as PCI DSS), and your organization-specific policies conforming to data privacy legislation. 

 The terms data localization, residency, and sovereignty might sound similar but have different implications. The following guidance doesn't provide formal definitions of the terms listed. They are based on what we have identified as the main themes by listening to our customers, partners, and regulators. Consult your legal and compliance teams to verify how each of these sets of requirements apply to the jurisdictions you operate in. It isn't uncommon to find different interpretations of these terms. 

 **Data Localization:** Implies you meet legal requirements stating data must be stored and processed within a specific geographic boundary. **Scenario**: A central bank mandates that all payment systems data must be stored on servers physically located within the country's jurisdiction. 

 **Data Residency:** Implies that you have knowledge of where your data is, and control where that data is stored and transferred to at all times. Unlike data localization, data residency is about knowing and controlling where your data lives, and understanding the legal basis for international data transfers, including adequacy decisions and standard contractual clauses (SCCs). **Scenario:** A European healthcare provider assesses their data residency requirements and chooses to store patient records in Frankfurt data centers for faster access, lower latency, while aligning with articles under [Chapter V](https://eur-lex.europa.eu/eli/reg/2016/679#cpt_V) of the EU GDPR. 

 **Data Sovereignty:** This is the [broadest concept](https://aws.amazon.com/what-is/data-sovereignty/). Implies data remains under the legal jurisdiction of the country where it is located, and the organization maintains control over that data, including who can access it and under what circumstances. It encompasses data residency and localization but adds requirements around operator access restrictions. It might also include requirements related to data portability so that data isn't locked in to a specific service provider. **Scenario:** A German financial institution needs to make sure that their customer data stored in Germany remains under German jurisdiction. Therefore, this goes beyond storing data in Germany (residency). It means maintaining sovereign control over that data. 

 For simplicity, you can think of data localization as a subset of data residency. Data residency as a subset of data sovereignty. You can meet data residency requirements without achieving data sovereignty (that is, your data is in the right place, but you don't have operator access restrictions in place). You can meet data localization requirements without achieving data sovereignty (your data never leaves the country, but you are locked-in to a specific service provider as it uses a closed data format). 

 Access control (who can access, what, and under what circumstances) spans all three aspects. 

 **What AWS provides to control operator access:** 
+  Many core AWS services, including [AWS KMS](https://aws.amazon.com/kms/), [Amazon EC2](https://aws.amazon.com/ec2/) (through the [AWS Nitro System](https://aws.amazon.com/ec2/nitro/)), [AWS Lambda](https://aws.amazon.com/lambda/), and [Amazon EKS](https://aws.amazon.com/eks/), are designed with [zero operator access](https://aws.amazon.com/trust-center/operator-access/). The [Nitro System](https://aws.amazon.com/blogs/security/aws-nitro-system-security-design-receives-high-marks-from-ncc-group/) and [Amazon EKS](https://aws.amazon.com/blogs/security/amazon-elastic-kubernetes-service-gets-independent-affirmation-of-its-zero-operator-access-design/) have each been independently validated by NCC Group, affirming that there is no mechanism for AWS operators to access customer content. 
+  AWS operator actions use secure interfaces with temporary short-lived credentials, FIPS-validated hardware security tokens. These secure operator interfaces permit only limited operations that don't disclose customer data, and enforce multi-person approval for sensitive operations with full traceability to the individual operator. For more information see [AWS Trust Center - Operator Access](https://aws.amazon.com/trust-center/operator-access/). 
+  The [AWS European Sovereign Cloud](https://aws.eu/) is operated by [EU residents (transitioning to EU citizens)](https://www.aboutamazon.eu/news/aws/aws-european-sovereign-cloud-to-be-operated-by-eu-citizens) located in the EU. AWS European Sovereign Cloud Staff are obligated under their terms of employment to follow EU and Member State law. The AWS European Sovereign Cloud [Addendum](https://aws.eu/esca/) that supplements the AWS [Customer Agreement](https://aws.amazon.com/agreement) provides more details. 
+  [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/), [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/), [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/), [AWS AI Factories](https://aws.amazon.com/ai/ai-factories/), and [AWS Outposts](https://aws.amazon.com/outposts/) each bring a range of deployment, and governance options, enabling customers to match their infrastructure deployment to their specific regulatory, latency, and data residency requirements. 

 These controls are part of the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/). AWS secures the infrastructure, and you configure controls over your own operators and users. 

### Implementation steps
<a name="implementation-steps"></a>

 Before attempting the following implementation steps, make sure you have read through and applied best practices listed under the AWS Well-Architected Security pillar under [Identity management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/identity-management.html) and [Permissions management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/permissions-management.html). 

1.  **Know where your data is**: Knowing where your data resides is a key requirement under data residency. Run discovery and data classification jobs to tag resources with sovereignty-specific data classification tags (such as data-classification:sovereign, data-classification:confidential) and create automated processes that verify tag compliance. See [DSSEC06-BP01 Classify data with sovereignty attributes](dssec06-bp01.html). 

1.  **Baseline your data sovereignty requirements**: After you understand where your data is, the next step is to baseline your data sovereignty requirements. They include (but are not limited to): 

   1.  Where can data be stored? - Think of jurisdictional boundaries, data stores, retention policies, and cross-border data transfers. 

   1.  Who can access it and under what circumstances? - Think of operator location, access routes, clearances required, physical security of the facility, and the certifications and attestations you will need. 

   1.  Which nation (or bloc of nations) has jurisdiction over your data? Think of data subject access requests (DSARs), data disclosure requests from law enforcement agencies, and breach reporting procedures in the jurisdictions you operate in. 

   1.  And are there any interoperability and portability requirements that need to be fulfilled? Think of alignment to standards-based protocols, storage formats, data formats, and open specifications that can assist in mitigating potential risks around business continuity. 

    After you understand your data residency and data sovereignty requirements, the next steps are to establish network-centric and identity-centric controls. 

1.  **Establish network-centric controls**: Set up centralized routing and inspection points to inspect, route, and filter [East-West](https://en.wikipedia.org/wiki/East-west_traffic) (VPC-to-VPC) and [North-South](https://en.wikipedia.org/wiki/North-south_traffic) (Internet egress) traffic. For sovereign workloads, centralized egress inspection is particularly important because it gives you a single point to detect and block unintended data flows before they leave your network. The whitepaper [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) lists several patterns that you can use. 

    This presentation [The Routing Loop - Centralized network traffic inspection: Key insights and lessons learned](https://www.youtube.com/watch?v=3tXQUZ-_ASs) compares several network topologies from the perspective of security, operational flexibility, and costs. For instance, while using a centralized "Inspection VPC" might be the right approach for VPC-to-VPC and Internet Egress traffic, the distributed model (AWS WAF, AWS Shield, and ALBs located in workload VPCs) offers greater operational flexibility for Internet Ingress traffic. 

    Along with ingress, egress, and VPC-to-VPC traffic routing and filtering, apply network segmentation with subnets and security groups. Security groups provide dynamic, software-defined network micro-perimeters for both north-south and east-west traffic. 

1.  **Add identity-centric controls**: Apply principles of least privilege on AWS [principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) and [resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html) using AWS Identity and Access Management [access policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html). Consider building [data perimeters](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_data-perimeters.html) that serve as always-on boundaries to help protect your data across a broad set of AWS accounts and resources. Establish your zone of trust and define it as narrowly as possible. Review trust boundaries regularly and remove unnecessary trust relationships. 

    A data perimeter is a set of preventive controls that verifies that only *trusted identities* are accessing *trusted resources* from *expected networks*. This is a foundational step designed to block untrusted entities from accessing sensitive data held within your accounts. The following three principles are central to this: 

   1.  **Only trusted identities**: Only *trusted identities* can access *my resources* and only *trusted identities* are allowed from *my networks*. 

   1.  **Only trusted resources**: *My principals* can only access *trusted resources* and that access from *my networks* only targets *trusted resources* (regardless of the principal involved). 

   1.  **Only expected networks**: Only *expected networks* can be the source of requests from *my principals* or to *my resources*. 

    Data perimeters are set up using [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) and [VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) to complement the network-centric controls you set up in Step 3 and add more defense in depth. For example, VPC endpoint policies allow you to enforce identity-centric rules at a logical network boundary. The blog post [Zero Trust architectures: An AWS perspective](https://aws.amazon.com/blogs/security/zero-trust-architectures-an-aws-perspective/) makes the case that the best security doesn't come from making a binary choice between identity-centric and network-centric tools, but rather by using both effectively in combination with each other. 

    For more detail on building data perimeters, see [Blog Post Series: Establishing a Data Perimeter on AWS](https://aws.amazon.com/identity/data-perimeters-blog-post-series/). 

1.  **Strengthen your digital sovereignty posture:** See [DSSEC07-BP01 Enhance your digital sovereignty governance posture](dssec07-bp01.html) for a list of additional measures including, specific AWS Control Tower preventive and detective controls dedicated to data residency and digital sovereignty. 

1.  **Implement logging and monitoring**: Prioritize preventive and proactive controls over detective controls, because it is more secure to block noncompliant access attempts before they occur rather than to detect such attempts after they occur. Apply detective controls to add in monitoring of compliance. 
   +  Implement [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and [Amazon CloudWatch](https://docs.aws.amazon.com/cloudwatch/) for logging and monitoring. 
   +  Implement [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) rules to detect noncompliant resources. Use [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) compliance standards to continuously assess your posture and generate compliance scores aligned with regulatory frameworks. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC03-BP01 Define access requirements](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define.html) 
+  [SEC03-BP02 Grant least privilege access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html) 
+  [SEC03-BP05 Define permission guardrails for your organization](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define_guardrails.html) 
+  [SEC08-BP04 Enforce access control](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_access_control.html) 
+  [SEC01-BP06 Automate testing and validation of security controls in pipelines](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_automate_security_controls.html) 
+  [SEC05-BP01 Create network layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_create_layers.html) 
+  [SEC05-BP02 Control traffic flow within your network layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_layered.html) 

 **Related documents:** 
+  [Identity and Access Management](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-security-perspective/identity-and-access-management.html) 
+  [Data Residency: AWS Policy Perspectives](https://d1.awsstatic.com/whitepapers/compliance/Data_Residency_Whitepaper.pdf) 
+  [Data Residency with Hybrid Cloud Services Lens - AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/data-residency-with-hybrid-cloud-services-lens.html) 
+  [Data Classification](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification.html) 
+  [Data security and risk management](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/data-security-and-risk-management.html) 
+  [Exploring the zero operator access design of Mantle - Next-generation inference engine for Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/exploring-the-zero-operator-access-design-of-mantle/) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Amazon S3 security and access control best practices](https://www.youtube.com/watch?v=vRmUI0VdsQw) 
+  [AWS re:Invent 2019 - Provable access control: Know who can access your AWS resources](https://www.youtube.com/watch?v=6DX7p-OirGU) 
+  [AWS re:Inforce 2022 - AWS Identity and Access Management (IAM) deep dive](https://www.youtube.com/watch?v=YMj33ToS8cI) 
+  [AWS re:Invent 2018: The Theory and Math Behind Data Privacy and Security Assurance](https://www.youtube.com/watch?v=F3JmBhTQmyY) 

 **Related services:** 
+  [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) 
+  [AWS Key Management Service (KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) 
+  [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) 