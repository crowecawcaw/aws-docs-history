

# DSSEC07-BP01 Enhance your digital sovereignty governance posture
<a name="dssec07-bp01"></a>

 In highly regulated industries, you might need to implement technical controls to enhance your digital sovereignty governance posture. This best practice assumes a secure landing zone with baseline security guardrails is already in place, and focuses on the sovereignty-specific governance controls layered on top of that foundation. 

 **Desired outcome:** 
+  Sovereign data remains within designated jurisdictions through automated, verifiable controls. 
+  Regulatory requirements are met while operational efficiency, access controls, and resiliency are preserved across jurisdictions. 

 **Common anti-patterns:** 
+  Relying solely on contractual agreements without technical enforcement mechanisms. 
+  Implementing digital sovereignty controls as an afterthought rather than embedding them into the architecture from the beginning. 
+  Applying uniform data protection and data privacy controls across data types without considering sensitivity levels and regulatory requirements. 
+  Failing to implement monitoring and alerting for digital sovereignty deviations. 

 **Benefits of establishing this best practice:** 
+  Enhanced adherence assurance through automated enforcement of digital sovereignty requirements and detailed audit trails. 
+  Reduced compliance costs through automated controls that lower manual oversight and audit preparation time. 
+  Enhanced customer trust by demonstrating verifiable digital sovereignty and privacy protection. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The introduction to this Lens establishes that a workload's sovereignty posture is the set of verifiable controls in effect, not contractual assertions alone. Contractual agreements and data processing addenda define obligations between parties, but they don't automatically enhance an organization's sovereignty posture. Organizations that complement contractual commitments with automated technical enforcement can provide verifiable, auditable assurance to regulators, customers, and internal stakeholders, reducing the cost and effort of compliance evidence gathering. 

 Data privacy legislation varies in how it addresses data residency. The European Union General Data Protection Regulation ([EU GDPR](https://eur-lex.europa.eu/eli/reg/2016/679)) doesn't mandate country-specific data residency but instead [outlines principles and conditions](https://eur-lex.europa.eu/eli/reg/2016/679#cpt_V) governing data transfers to a third country or to an international organization. Other regulators take more prescriptive approaches: the Reserve Bank of India ([RBI](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244&Mode=0)), for example, requires payment-related data to reside locally. Understanding these distinctions is the necessary starting point before selecting or deploying technical controls. 

 [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) provides the governance layer that translates sovereignty requirements into enforceable policy. It applies preventive, detective, and proactive controls at the Organizational Unit (OU) level, so you can codify data residency rules and access restrictions as organizational guardrails rather than one-off configurations. [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) continuously evaluates resource configurations against these governance rules, while [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) provides the audit trail needed to demonstrate enforcement to regulators. This governance model means you can tune the balance between strictness and operational flexibility per workload. Tighter preventive controls suit workloads where data sensitivity demands it, while lighter detective controls may be appropriate in development environments. AWS provides the governance mechanisms and the control catalog. Your responsibility is to determine which controls to activate, define their scope and parameters, and maintain policies that balance sovereignty requirements with operational needs. 

 Technical controls alone are not sufficient. Operational controls, such as mandatory security vetting of operational support staff, might serve to augment automated enforcement. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify your data residency requirements:** Determine which data privacy legislation and sector-specific regulations apply to each workload. Map data types to their permitted storage, processing, and permissible transfer locations. Consult privacy and legal experts, as data types may be subject to additional controls beyond general privacy legislation. See the EU list of [adequacy decisions](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en) as an example. 

1.  **Limit operations to within specific AWS Regions**: Establish secure landing zone AWS Control Tower and refine the controls to match your operating regions. AWS Control Tower offers two Region deny controls. One control, GRREGIONDENY, when activated, applies to the entire landing zone. Another control, CT.MULTISERVICE.PV.1, when activated, can apply to specific Organizational Units (OUs) that you specify. 
   +  GRREGIONDENY: Also known as Region deny control or landing zone Region deny control. This is [implemented using this Service Control Policy (SCP)](https://docs.aws.amazon.com/controltower/latest/controlreference/primary-region-deny-policy.html). When you enable the control, it applies to all registered, top-level OUs in your hierarchy, and it is inherited by OUs lower in the chain. 
   +  CT.MULTISERVICE.PV.1: Deny access to AWS based on the [requested AWS Region for an organizational unit](https://docs.aws.amazon.com/controltower/latest/controlreference/ou-region-deny.html). The CT.MULTISERVICE.PV.1 control is a configurable and parameterized SCP. You can select specific OUs to which it applies, and add one or more parameters, such as **AllowedRegions**, **ExemptedPrincipalArns**, and **ExemptedActions**. This example shows how to enable this control, with parameters, from the CLI. It activates a Region deny control on OU ou-zzxx-zzx0zzz2, restricting API actions to the us-east-1 and us-west-2 Regions only. The wildcard \* in the account ID position of the role ARN applies the exemption across all accounts in the OU without listing each account individually. The trailing /\* on the STS ARN matches any session name. When a principal assumes a role, AWS appends a session name to the ARN (for example, assumed-role/ReadOnly/username), and without the trailing wildcard, the exemption would not match active sessions. 

   ```
   # Enable Region deny control for an OU. Allow only us-east-1 and us-west-2. But also add exempted actions and principals.
   AWS controltower enable-control \
       --target-identifier arn:aws:organizations::012345678901:ou/o-EXAMPLE/ou-zzxx-zzx0zzz2 \
       --control-identifier arn:aws:controltower:us-east-1::control/EXAMPLE_NAME \
       --parameters '[{"key":"AllowedRegions","value":["us-east-1","us-west-2"]},{"key":"ExemptedPrincipalArns","value":["arn:aws:iam::*:role/ReadOnly","arn:aws:sts::*:assumed-role/ReadOnly/*"]},{"key":"ExemptedActions","value":["logs:DescribeLogGroups","logs:StartQuery","logs:GetQueryResults"]}]'
   ```

    Exemptions weaken security controls. Only exempt principals and actions after thorough security review. Document the business justification for each exemption. Review exemptions periodically and remove those no longer justified. Never exempt security-critical actions like iam:PutUserPolicy or kms:ScheduleKeyDeletion. 

1.  **Deploy digital sovereignty preventive controls aligned to individual workloads**: In addition to the Region deny control which acts at an OU (Organizational Unit) level, AWS Control Tower provides several digital sovereignty related preventive controls. These controls can be applied to protect [individual workloads](https://docs.aws.amazon.com/controltower/latest/controlreference/ds-preventive-controls.html). Consider enabling these controls to meet workload specific compliance requirements. For example, [CT.KMS.PV.6](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-kms-pv-6.html) requires that the AWS KMS customer-managed key is configured with a key material originating from an external key store (XKS) only. 

1.  **Deploy additional data residency controls**: Beyond data residency controls shown in Step 2, consider applying additional controls to block cross-region networking, VPC peering, Transit Gateway peering or VPN Connections. For more options, see [Data residency controls with preventive behavior](https://docs.aws.amazon.com/controltower/latest/controlreference/data-residency-preventive-controls.html). 

1.  **Deploy data residency detective controls**: Deploy controls to continuously monitor data residency compliance. See [Data residency controls with detective behavior](https://docs.aws.amazon.com/controltower/latest/controlreference/data-residency-detective-controls.html) for more options. See [Detect whether Amazon S3 settings to block public access are set as true for the account](https://docs.aws.amazon.com/controltower/latest/controlreference/data-residency-detective-controls.html#s3-account-level-public-access-blocks-periodic) to understand how such controls work. 

1.  **Validate deployed controls:** After enabling [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html) controls, validate effectiveness by attempting prohibited actions in a test account to verify they are blocked. Monitor control compliance using [Security Hub CSPM](https://aws.amazon.com/security-hub/) and integrate validation into your change management process so that controls are re-tested when architecture changes, new services are adopted, or regulatory requirements evolve. Automate compliance reporting to provide continuous assurance rather than point-in-time assessments. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSPERF01-BP01 Evaluate sovereign solutions using a data-driven approach](dsperf01-bp01.html) 
+  [SEC02-BP01 Use strong sign-in mechanisms](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_enforce_mechanisms.html) 
+  [SEC07-BP01 Understand your data classification scheme](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_identify_data.html) 
+  [SEC08-BP01 Implement secure key management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_key_mgmt.html) 
+  [SEC08-BP02 Enforce encryption at rest](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_encrypt.html) 
+  [OPS01-BP04 Evaluate compliance requirements](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_compliance_reqs.html) 

 **Related documents:** 
+  [Governance - Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/governance.html) 
+  [AWS Control Tower controls reference - Digital Sovereignty](https://docs.aws.amazon.com/controltower/latest/controlreference/ds-controls.html) 
+  [AWS Digital Sovereignty Pledge: Control without compromise](https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/) 
+  [AWS Control Tower Digital Sovereignty Controls](https://docs.aws.amazon.com/controltower/latest/controlreference/digital-sovereignty-controls.html) 
+  [Data residency controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/data-residency-controls.html) 
+  [AWS GDPR Center](https://aws.amazon.com/compliance/gdpr-center/) 
+  [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) 
+  [AWS Local Zones features and Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/?nc=sn&loc=2) 
+  [AWS Dedicated Local Zones features - See "Your choice of services"](https://aws.amazon.com/dedicatedlocalzones/features/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - AWS European Sovereign Cloud: From concept to reality (SEC201)](https://www.youtube.com/watch?v=L4rNxZJaCuc) 

 **Related services:** 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS KMS](https://aws.amazon.com/kms/) 
+  [AWS Organizations](https://aws.amazon.com/organizations/) 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 