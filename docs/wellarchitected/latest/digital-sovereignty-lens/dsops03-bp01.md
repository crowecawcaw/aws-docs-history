

# DSOPS03-BP01 Plan and prepare for audits
<a name="dsops03-bp01"></a>

 Organizations face audits from multiple regulatory authorities with different evidence requirements, timelines, and scoping criteria, whether within a single jurisdiction or across several. Proactive audit planning and consistent tooling reduce disruption and provide confidence that evidence is complete, accessible, and stored within approved jurisdictions. 

 **Desired outcome:** 
+  Audit processes are streamlined and repeatable across jurisdictions. 
+  Evidence is collected continuously, stored in compliance with data residency requirements, and accessible to auditors on demand. 
+  Teams can respond to audit requests from multiple regulatory authorities without diverting significant engineering effort. 

 **Common anti-patterns:** 
+  Scrambling to gather documentation days before an audit, leading to incomplete or inaccurate evidence. 
+  Treating audits as solely an IT or security team responsibility rather than a cross-functional effort. 
+  Storing audit evidence in a Region without considering data localization or data residency requirements. 
+  No process exists to coordinate audits across multiple regulatory authorities in different jurisdictions. 

 **Benefits of establishing this best practice:** 
+  Scope of audit exercises is known in advance, leading to better planning and resource utilization. 
+  Well-documented audit practices demonstrate due diligence to regulators and can reduce scrutiny. 
+  Audits are conducted in a structured, automated, and repeatable manner across jurisdictions. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Organizations operating across jurisdictions face audits from multiple regulatory authorities, each with different evidence requirements, timelines, and scoping criteria. A single workload spanning two jurisdictions may face simultaneous audits from different authorities, each requiring evidence scoped to their jurisdiction. Without proactive planning, audit responses become reactive and engineering-intensive. 

 Continuous evidence collection captures compliance findings, configuration states, and access logs as they occur, so that evidence is already available when an audit is initiated. This reduces audit-time disruption compared to point-in-time collection, which retrospectively assembles documentation after an audit is announced. 

 Audit evidence itself is subject to data residency requirements. Logs, compliance reports, and configuration snapshots relating to a jurisdiction may need to remain within that jurisdiction. Centralizing evidence into a single Region for convenience may violate the same data residency controls the evidence is meant to demonstrate. Scope evidence storage by jurisdiction, and verify that cross-Region aggregation doesn't move protected data outside approved boundaries. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Conduct readiness assessments:** 
   +  Perform regular internal audits using the same criteria as external auditors. Include jurisdiction-specific criteria where audit requirements differ. 
   +  Run tabletop exercises simulating audit scenarios, including situations where multiple regulatory authorities audit simultaneously. 
   +  Practice evidence retrieval and presentation. 

1.  **Establish audit governance processes:** 
   +  Create an audit coordination group with representatives from key areas. Include jurisdiction-specific compliance expertise to address local audit requirements. 
   + Prepare regional teams to independently support audit exercises. 
   +  Designate an audit owner to oversee audits. Audit owners are typically governance, risk, and compliance (GRC) professionals, such as a compliance officer or a data protection officer. 
   +  Develop a communication plan for internal and external auditors. Include escalation paths to resolve conflicting requirements. 

1.  **Prepare audit artifacts:** Start building a searchable and readily accessible repository of frequently requested audit artifacts. Store artifacts in Regions that meet data residency requirements for audit evidence. You may need to consider the following items: 

    **Note:** The following list isn't exhaustive and doesn't include all the documentation that may be needed for audits. Consult your legal, compliance, and audit teams to determine the specific evidence requirements for your organization and jurisdictions. 
   +  Inventory of software and hardware assets. 
   +  Compliance catalogs and workbooks, security policies, data protection policies, and privacy policies. 
   +  Data protection impact assessment (DPIA) reports. 
   +  Risk registers. 
   +  Incident management plans. 
   +  Business continuity plans (BCPs) and disaster recovery (DR) plans. 
   +  Documentation related to software development lifecycle (SDLC) processes (for example, data handling procedures and change management processes). 
   +  Design documentation (for example, data flow diagrams, up-to-date network diagrams, and records of architecture decisions). 
   +  Documents related to previous security incidents, including root cause analysis (RCA) reports. 
   +  Contractual agreements with your technology providers. Agreements between AWS and AWS customers can be found in [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/managing-agreements.html). 
   +  Attestations and certifications currently held by your organization and your service providers. AWS certifications and attestations can be evidenced through [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/managing-agreements.html). 
   +  Audit trails and security-related logs. For example, AWS CloudTrail [Data and Management Event Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-events.html), [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), [AWS WAF Logs](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html), [Amazon EKS Audit Logs](https://docs.aws.amazon.com/eks/latest/best-practices/auditing-and-logging.html), and [Route 53 resolver query logs](https://docs.aws.amazon.com/Route 53/latest/DeveloperGuide/resolver-query-logs.html). 
   +  Records of training conducted on compliance-related topics. 
   +  Jurisdiction-specific artifacts. For example, evidence of data localization and data residency, operator access logs by Region, and jurisdiction-specific breach notification records. 

1.  **Provision jurisdiction-scoped auditor access:** Provision read-only auditor roles such as the AWS [ReadOnlyAccess managed policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ReadOnlyAccess.html), which allows auditors access to compliance-related services including [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) and [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html). Scope auditor roles by jurisdiction where access restrictions apply, for example by [adding condition elements](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/) to the IAM role's trust policy. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSOPS01-BP01 Organize compliance for multi-jurisdictional operations](dsops01-bp01.html) 
+  [DSOPS03-BP02 Automate evidence collection and reporting](dsops03-bp02.html) 
+  [OPS02-BP02 Processes and procedures have identified owners](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_proc_owners.html) 
+  [OPS02-BP03 Operations activities have identified owners responsible for their performance](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_activity_owners.html) 

 **Related documents:** 
+  [Visualizing AWS Config data using Amazon Athena and Quick](https://aws.amazon.com/blogs/mt/visualizing-aws-config-data-using-amazon-athena-and-amazon-quicksight/) 
+  [Prepare for an Audit in AWS Part 2 – General Best Practices](https://aws.amazon.com/blogs/mt/prepare-for-an-audit-in-aws-part-2-general-best-practices/) 
+  [How to use trust policies with IAM roles](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/) 

 **Related videos:** 
+  [AWS re:Inforce 2025 - Best practices for managing governance, risk, and compliance globally (GRC301)](https://www.youtube.com/watch?v=pCNIpnb9tvE) 

 **Related examples:** 
+  [Workshop: AWS Cloud – An Auditors Lens](https://catalog.us-east-1.prod.workshops.aws/workshops/be5ac274-af86-47ef-b3ae-efae7fad136c/en-US) 
+  [Workshop: AWS Config Resource Compliance Dashboard](https://catalog.workshops.aws/awscid/en-US/dashboards/additional/config-resource-compliance-dashboard/) 

 **Related services:** 
+  [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) 
+  [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) 
+  [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) 