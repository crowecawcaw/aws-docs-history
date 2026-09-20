

# DSSEC04-BP02 Detect sovereignty-specific threats through telemetry and analysis
<a name="dssec04-bp02"></a>

 Effective threat detection capability needs broad telemetry from multiple sources, the ability to correlate and contextualize data points, and centralized visibility of security events. 

 **Desired outcome:** 
+  Threat detection capabilities identify sovereignty-specific risks, including unauthorized cross-border data transfers, operator access violations, and jurisdictional compliance drift. 

 **Common anti-patterns:** 
+  Incomplete telemetry leading to significant blind spots around critical assets. 
+  Fragmented security data points spread across multiple tools and databases. Security analysts struggle to correlate signals from multiple sources, and may fail to detect emerging threats. 
+  Failing to layer preventive security controls with detective and proactive measures. Detective controls are still required for detecting potential bypass of preventive and proactive controls. 
+  Centralizing security telemetry across jurisdictions without considering data residency requirements. 

 **Benefits of establishing this best practice:** 
+  A sovereignty-specific threat taxonomy enables systematic identification of cross-border data risks and operator access violations relevant to your jurisdiction. 
+  Early detection of emerging threats means you can isolate compromised systems and protect critical assets. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Sovereignty-specific detection starts with knowing what to look for. A standard detection stack watches for malware, anomalous logins, and known attack patterns, but it has no concept of a jurisdictional boundary or a data localization mandate. Threat modeling supplies that context. By mapping each compliance requirement to the ways it could be violated, you produce a threat list unique to your jurisdiction: unauthorized cross-border transfers, resources created in noncompliant Regions, and operator access that breaks a localization rule. That list drives the rest of the detection design. 

 To detect the threats you modeled, review the coverage, currency, and quality of your telemetry. Consider User and Entity Behavior Analytics (UEBA) for spotting anomalies, data loss prevention (DLP) to block unauthorized data transfers, and security information and event management (SIEM) systems to correlate alerts and visualize attack paths. 

 Analyzing vast amounts of diverse telemetry data can be challenging. To identify emerging threats in a timely manner, deploy automation to collect and store telemetry data. Perform data analytics as part of your detection capability using extract, transform, and load (ETL) pipelines to standardize logs and trace formats. Integrate AI/ML and generative AI reasoning models to detect threats quickly from large datasets. AI/ML models and large language models (LLMs) are particularly useful for correlating logs and application traces. Use AI/ML to assist with triage, root cause analysis and prioritization, but be cautious when applying remediation based solely on model inferencing. 

 Perform regular reviews of the threat detection capabilities. The reviews should include regulatory or compliance requirements, extent of coverage, detection metrics such as Mean Time to Detect (MTTD), and accuracy of findings or alerts (for example, false positives compared to actual findings) and the relevant configurations (for example, finding suppression rules, correlation rules). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Apply standard threat modeling frameworks**: Conduct threat modeling to systematically identify attack paths and threats using frameworks such as [STRIDE](https://owasp.org/www-community/Threat_Modeling_Process#stride), [PASTA](https://versprite.com/blog/what-is-pasta-threat-modeling/), and [LINDDUN](https://linddun.org/). Evaluate frameworks such as [MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro) (Multi-Agent Environment, Security, Threat Risk, and Outcome) to address threats emerging from the widespread adoption of generative AI models, tools, and agentic frameworks. 
   +  Use external data such as domain-specific threat intelligence or security community publications (for example, OWASP, AWS [Security Bulletins](https://aws.amazon.com/security/security-bulletins/)) to improve precision. 
   +  Focus on actual adversary Tactics, Techniques, and Procedures (TTPs) rather than generic threats. 

1.  **Include sovereignty-specific threats in threat modeling**: Extend traditional threat modeling frameworks (STRIDE, PASTA, and LINDDUN) with sovereignty-specific threats. Here are a few examples for illustration purposes. Validate threats and mitigations for your specific context. Not all threats are mitigated with technical controls only. 
   +  Unauthorized Cross-Border Data Transfer (UCDT): 
     +  Threat: Data inadvertently replicated to foreign jurisdiction 
     +  Example: S3 bucket with cross-region replication to a foreign jurisdiction with which there is no existing [adequacy arrangement](https://aws.amazon.com/compliance/eu-data-protection/) 
     +  Mitigation: [Disallow cross region replication for Amazon S3 buckets](https://docs.aws.amazon.com/controltower/latest/controlreference/elective-preventive-controls.html#aws-gr_restrict_s3_cross_region_replication) 
   +  Jurisdictional Compliance Drift (JCD): 
     +  Threat: Resources created in noncompliant Regions 
     +  Example: Developer creates RDS instance in us-east-1 for EU workload 
     +  Mitigation: [Configure the Region deny control](https://docs.aws.amazon.com/controltower/latest/userguide/region-deny.html) in AWS Control Tower 
   +  Operator Access Violation (OAV): 
     +  Threat: Operator gains access to sensitive data 
     +  Example: A member of an operational support team located in a foreign jurisdiction is granted access to a sensitive data store in violation of an existing data localization mandate 
     +  Mitigation: [Establish permissions guardrails using data perimeters](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_data-perimeters.html), [Use conditions in IAM policies to further restrict access](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#use-policy-conditions) 
   +  Third-Party Sovereignty Risk (TPSR): 
     +  Threat: Third-party services process data outside jurisdiction 
     +  Example: SIEM vendor stores logs to a foreign data center 
     +  Mitigation: Analyze and baseline vendor documentation, certifications and attestations. Verify contractual agreements. Document net legal safeguards and residual risks. 

    An example sovereignty threat enumeration: 


<table>
<thead>
  <tr><th> Threat ID </th><th> Category </th><th> Description </th><th> Affected Assets </th><th> Likelihood </th><th> Impact </th><th> Mitigation </th><th> Owner </th></tr>
</thead>
<tbody>
  <tr><td> SOV-001 </td><td> UCDT </td><td> S3 replication to foreign jurisdiction </td><td> EU data </td><td> Medium </td><td> High </td><td> Block replication </td><td> Security </td></tr>
  <tr><td> SOV-002 </td><td> TPSR </td><td> Third-party services process data outside jurisdiction </td><td> EU data </td><td> Medium </td><td> High </td><td> Review agreements </td><td> Legal </td></tr>
</tbody>
</table>


1.  **Identify coverage gaps**: Map the output of threat modeling exercises to the detective controls and supporting telemetry data. Identify critical gaps and formulate remediation strategies. Consider other telemetry data produced by non-security sources such as system events or application logs. This data can provide insights or increase confidence when you correlate it with security logs. 

1.  **Augment telemetry data**: Consider tools that support data analytic capabilities and add context to telemetry data, such as: 
   +  [Security Analytics for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-analytics.html) that analyzes security event logs from different sources. 
   +  [Amazon Security Lake](https://aws.amazon.com/security-lake/features/) that automatically centralizes security data from multiple sources. 
   +  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) to prioritize critical security issues by correlating different security telemetry. 

1.  **Detect emerging threats from compliance drift**: See the AWS Prescriptive Guidance for implementing [detective controls](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/detective-controls.html) on AWS. 

1.  **Review exposures and attack paths**: AWS Security Hub CSPM [generates exposure findings](https://docs.aws.amazon.com/securityhub/latest/userguide/exposure-findings-generate.html) from sources such as EC2 instances, DynamoDB tables, IAM users, S3 buckets, Lambda functions, RDS database instances, and EKS clusters. Security Hub CSPM provides a visual graph of [potential attack paths](https://docs.aws.amazon.com/securityhub/latest/userguide/potential-attack-path-graph.html), showing how attackers can take control of your resources. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSSEC04-BP03 Establish comprehensive logging and monitoring of operator actions](dssec04-bp03.html) 
+  [SEC01-BP07 Identify threats and prioritize mitigations using a threat model](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_threat_model.html) 
+  [SEC01-BP04 Stay up to date with security threats and recommendations](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_updated_threats.html) 
+  [SEC04-BP01 Configure service and application logging](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_app_service_logging.html) 
+  [SEC04-BP03 Correlate and enrich security alerts](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_security_alerts.html) 
+  [SEC04-BP04 Initiate remediation for non-compliant resources](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_noncompliant_resources.html) 

 **Related documents:** 
+  [Detective controls](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/detective-controls.html) 
+  [Threat Technique Catalog for AWS](https://aws-samples.github.io/threat-technique-catalog-for-aws/) 
+  [Accelerate threat modeling with generative AI](https://aws.amazon.com/blogs/machine-learning/accelerate-threat-modeling-with-generative-ai/) 
+  [Threat Modeling: 12 Available Methods, N. Shevchenko, Carnegie Mellon University, Carnegie Mellon's Software Engineering Institute, December 3, 2018](https://www.sei.cmu.edu/blog/threat-modeling-12-available-methods/) 
+  [MITRE ATT&CK Cloud Matrix](https://attack.mitre.org/matrices/enterprise/cloud/) 
+  [CISA - Insider Threat Mitigation Guide](https://www.cisa.gov/resources-tools/resources/insider-threat-mitigation-guide) 
+  [Insider Threat Detection Study - NATO Cooperative Cyber Defence Centre of Excellence](https://ccdcoe.org/uploads/2018/10/Insider_Threat_Study_CCDCOE.pdf) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Testing GuardDuty's Runtime Detections: Hands-on with real world attack scenarios](https://www.youtube.com/watch?v=UyakYnhI0RE) 
+  [AWS re:Invent 2025 - Threat-Modeling-As-Code - Transforming Your Threat Statements into Attack Trees](https://www.youtube.com/watch?v=F5GU_d6Gfuc) 
+  [AWS re:Invent 2025 - Privacy-preserving AI primitives: Building blocks for regulated industries-ARC328](https://www.youtube.com/watch?v=vfkKJhllnx4) 
+  [AWS re:Invent 2025 - Supercharge security investigations with custom detection & analytics (SEC350)](https://www.youtube.com/watch?v=E5p_WnP4pw8&list) 

 **Related examples:** 
+  [AWS Well-Architected Labs - Security](https://wellarchitectedlabs.com/security/) 
+  [Amazon Security Lake samples](https://github.com/aws-samples/amazon-security-lake) 

 **Related services:** 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) 
+  [Amazon Security Lake](https://aws.amazon.com/security-lake/) 
+  [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Config](https://aws.amazon.com/config/) 