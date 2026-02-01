# DSSEC04-BP02 Detect threats through comprehensive telemetry and

analysis

Effective threat detection capability needs comprehensive telemetry
from multiple sources, the ability to correlate and contextualize
data points, and centralized visibility of security events.

**Desired outcome:** Achieve
effective threat detection that identifies emerging threats and
supports adherence to regulatory standards through effective
monitoring and analysis.

**Common anti-patterns:**

- Incomplete telemetry leading to significant blind spots around
  critical assets.
- Fragmented security data points spread across multiple tools and
  databases. Security analysts struggle to correlate signals from
  multiple sources, and may fail to detect emerging threats.
- Failing to layer preventative security controls with detective
  and proactive measures. Detective controls are still required
  for detecting potential bypass of preventative and proactive
  controls.

**Benefits of establishing this best
practice:**

- Early detection of emerging threats allows you to isolate
  compromised systems and protect critical assets.
- Early detection supports regulatory adherence through systematic
  monitoring and documentation.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

1. Map compliance requirements to threat detection capabilities.
   In addition to mapping cybersecurity requirements to specific
   preventative or proactive controls, also detect threats that
   could compromise such controls.
2. Review the coverage, currency, and quality of telemetry
   involved in identifying malicious activities and emerging
   threats. Consider the following.
   - User and Entity Behavior Analytics (UEBA) for spotting
     anomalies.
   - Data loss prevention (DLP) to block unauthorized data
     transfers.
   - Security information and event management (SIEM) systems
     to correlate alerts and visualize attack paths.

3. Analyzing vast amounts of diverse telemetry data can be
   challenging. To identify emerging threats in a timely manner,
   consider the following:
   - Deploy automation to collect and store telemetry data.
   - Perform data analytics as part of your detection
     capability. Use extract, transform, and load (ETL)
     pipelines to standardize logs and trace formats. Use ETL
     queries to search across terabytes of data and use
     business intelligence or operational intelligence
     dashboards to visualize key metrics.
   - Use automation to handle the growing amount of data.
   - Integrate AI/ML and generative AI reasoning models to
     detect threats quickly from large datasets. AI/ML models
     and large language models (LLMs) are particularly useful
     for correlating logs and application traces. Evaluate
     these capabilities when choosing SIEM tools. However,
     always have a human in the loop to review findings, as the
     current generation of LLMs can only apply probabilistic
     methods to correlate information.

4. Perform regular reviews of the threat detection capabilities.
   The reviews should include:
   - Regulatory or compliance requirements
   - Extent of coverage
   - Detection metrics such as Mean Time to Detect (MTTD)
   - Accuracy of findings or alerts (for example, false
     positives versus actual findings) and the relevant
     configurations (for example, finding suppression rules,
     correlation rules)

### Implementation steps

1. Conduct threat modeling to systematically identify attack
   paths and threats using frameworks such as
   [STRIDE](https://owasp.org/www-community/Threat_Modeling_Process#stride "https://owasp.org/www-community/Threat_Modeling_Process#stride"),
   [PASTA](https://versprite.com/blog/what-is-pasta-threat-modeling/ "https://versprite.com/blog/what-is-pasta-threat-modeling/"),
   and [LINDDUN](https://linddun.org/ "https://linddun.org/").
   Evaluate frameworks such as
   [MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro "https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro")
   (Multi-Agent Environment, Security, Threat Risk, and
   Outcome) to address threats emerging from the widespread
   adoption of generative AI models, tools, and agentic
   frameworks.
   - Use external data such as domain-specific threat
     intelligence or security community publications (for
     example, OWASP, AWS
     [Security
     Bulletins](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/")) to improve precision.
   - Focus on actual adversary Tactics, Techniques, and
     Procedures (TTPs) rather than generic threats.

2. Map the output of threat modeling exercises to the detective
   controls and supporting telemetry data. Identify critical
   gaps and formulate remediation strategies. Consider other
   telemetry data produced by non-security sources such as
   system events or application logs. This data can provide
   insights or increase confidence when you correlate it with
   security logs.
3. Consider tools that support data analytic capabilities and
   add context to telemetry data, such as:
   - [Security
     Analytics for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/security-analytics.md "../../../opensearch-service/latest/developerguide/security-analytics.md") that
     analyzes security event logs from different sources.
   - [Amazon
     Security Lake](https://aws.amazon.com/security-lake/features/ "https://aws.amazon.com/security-lake/features/") that automatically centralizes
     security data from multiple sources.
   - [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") that enables you to prioritize
     critical security issues by correlating different
     security telemetry.

4. Detect emerging threats from compliance drift. See the AWS
   Prescriptive Guidance for implementing
   [detective
   controls](../../../prescriptive-guidance/latest/aws-security-controls/detective-controls.md "../../../prescriptive-guidance/latest/aws-security-controls/detective-controls.md") on AWS.
5. Review exposures and attack paths. AWS Security Hub
   [generates
   exposure findings](../../../securityhub/latest/userguide/exposure-findings-generate.md "../../../securityhub/latest/userguide/exposure-findings-generate.md") from sources such as EC2 instances,
   DynamoDB tables, IAM users, S3 buckets, Lambda functions,
   RDS database instances, and EKS clusters. Security Hub
   provides a visual graph of
   [potential
   attack paths](../../../securityhub/latest/userguide/potential-attack-path-graph.md "../../../securityhub/latest/userguide/potential-attack-path-graph.md"), showing how attackers can take control
   of your resources.

## Resources

**Related best practices:**

- [SEC01-BP07
  Identify threats and prioritize mitigations using a threat model](../security-pillar/sec_securely_operate_threat_model.md "../security-pillar/sec_securely_operate_threat_model.md")
- [SEC04-BP03
  Correlate and enrich security alerts](../security-pillar/sec_detect_investigate_events_security_alerts.md "../security-pillar/sec_detect_investigate_events_security_alerts.md")

**Related documents:**

- [Detective
  controls](../../../prescriptive-guidance/latest/aws-security-controls/detective-controls.md "../../../prescriptive-guidance/latest/aws-security-controls/detective-controls.md")
- [Threat
  Technique Catalog for AWS](https://aws-samples.github.io/threat-technique-catalog-for-aws/ "https://aws-samples.github.io/threat-technique-catalog-for-aws/")
- [Accelerate
  threat modeling with generative AI](https://aws.amazon.com/blogs/machine-learning/accelerate-threat-modeling-with-generative-ai/ "https://aws.amazon.com/blogs/machine-learning/accelerate-threat-modeling-with-generative-ai/")

**Related videos:**

- [AWS re:Invent 2025 - Testing GuardDuty's Runtime Detections:Hands-on with real world attack scenarios](https://www.youtube.com/watch?v=UyakYnhI0RE "https://www.youtube.com/watch?v=UyakYnhI0RE")
- [AWS re:Invent 2025 - Threat-Modeling-As-Code - Transforming Your Threat Statements into Attack Trees](https://www.youtube.com/watch?v=F5GU_d6Gfuc "https://www.youtube.com/watch?v=F5GU_d6Gfuc")
- [AWS re:Invent 2025 - Privacy-preserving AI primitives: Building blocks for regulated industries-ARC328](https://www.youtube.com/watch?v=vfkKJhllnx4 "https://www.youtube.com/watch?v=vfkKJhllnx4")
- [AWS re:Invent 2025 - Supercharge security investigations with custom detection & analytics (SEC350)](https://www.youtube.com/watch?v=E5p_WnP4pw8&list "https://www.youtube.com/watch?v=E5p_WnP4pw8&list")

**External publications:**

- [Threat Modeling: 12 Available Methods, N. Shevchenko, Carnegie Mellon University, Carnegie Mellon's Software Engineering Institute, December 3, 2018](https://www.sei.cmu.edu/blog/threat-modeling-12-available-methods/ "https://www.sei.cmu.edu/blog/threat-modeling-12-available-methods/")
- [MITRE
  ATT&CK Cloud Matrix](https://attack.mitre.org/matrices/enterprise/cloud/ "https://attack.mitre.org/matrices/enterprise/cloud/")
- [CISA

* Insider Threat Mitigation Guide](https://www.cisa.gov/resources-tools/resources/insider-threat-mitigation-guide "https://www.cisa.gov/resources-tools/resources/insider-threat-mitigation-guide")

- [Insider
  Threat Detection Study - NATO Cooperative Cyber Defence Centre of Excellence](https://ccdcoe.org/uploads/2018/10/Insider_Threat_Study_CCDCOE.pdf "https://ccdcoe.org/uploads/2018/10/Insider_Threat_Study_CCDCOE.pdf")
