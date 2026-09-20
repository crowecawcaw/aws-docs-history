

# DSREL02-BP01 Implement continuous third-party risk management (TPRM) processes
<a name="dsrel02-bp01"></a>

 In highly regulated industries, a structured third-party risk management (TPRM) process is essential to mitigate risks associated with third-party vendors and service providers. Vendors can introduce sovereignty risks through data processed in non-approved jurisdictions, operators accessing systems from foreign locations, or sub-processors that don't adhere to data residency requirements. 

 **Desired outcome:** 
+  Third-party vendor risks are identified, assessed, and mitigated throughout the vendor engagement lifecycle, with specific verification that vendors maintain data within approved jurisdictions and meet jurisdiction-specific compliance requirements. 

 **Common anti-patterns:** 
+  Conducting one-time vendor assessments without continuous monitoring, failing to adapt evaluations to evolving threats and regulations. 
+  Relying on manual tracking processes and lacking clear understanding of data flows and vendor dependencies. 
+  Using inconsistent security criteria across vendors and over-relying on vendor self-attestations without independent verification. 
+  Allowing unapproved technology usage and lacking proper incident response coordination with vendors. 

 **Benefits of establishing this best practice:** 
+  Continuous monitoring of vendor risk posture with automated alerting and proactive supply chain risk identification. 
+  Systematic evidence collection and documentation demonstrating adherence to industry regulations. 
+  Streamlined vendor onboarding and offboarding processes while maintaining security standards and cost optimization. 
+  Pre-established communication channels and procedures for coordinating security incidents and protecting operations. 
+  Enhanced confidence from auditors, regulators, and customers through demonstrated vendor risk management. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A continuous TPRM lifecycle process, integrated with existing risk management, procurement, and compliance functions, provides systematic oversight of vendor risks throughout the engagement lifecycle. For sovereign workloads, TPRM extends beyond standard security assessments to verify that vendors maintain data within approved jurisdictions, that operator access originates from approved locations, and that sub-processors don't introduce unmonitored cross-border data flows. 

 Regulations such as the [EU Digital Operational Resilience Act](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en) (EU DORA) include specific requirements for Information and Communication Technology (ICT) TPRM. AWS has been [designated as a Critical Third-Party Provider (CTPP)](https://aws.amazon.com/blogs/security/aws-designated-as-a-critical-third-party-provider-under-eus-dora-regulation/) by the European Supervisory Authorities (ESAs), meaning AWS is subject to a formal oversight process under DORA. For financial services customers using AWS, this designation means that there is now joint oversight by the European Banking Authority (EBA), the European Securities and Markets Authority (ESMA), and the European Insurance and Occupational Pensions Authority (EIOPA). While AWS recognizes the significance of this oversight, it doesn't change a financial entity's obligation to maintain its own TPRM processes, including contractual safeguards, exit strategies, and ongoing monitoring of its ICT third-party dependencies. 

 The depth of TPRM implementation scales with organizational complexity. Organizations with fewer vendors might manage assessments through structured questionnaires and periodic reviews, while larger enterprises with extensive vendor ecosystems benefit from automated risk scoring, continuous monitoring integrations, and dedicated TPRM tooling. Regardless of scale, apply the sovereignty-specific criteria (data residency verification, operator location, and cross-border data flows) to every vendor that handles regulated data. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish governance and ownership:** Assign clear ownership for third-party risk management. Define roles, responsibilities, escalation paths, and review cadences. 

1.  **Implement a sovereignty-aware assessment framework:** Develop vendor questionnaires, risk assessment templates, compliance checklists, and evidence collection processes. Consider using [governance, risk, and compliance (GRC) solutions](https://aws.amazon.com/marketplace/solutions/security/governance-risk-compliance/) available in AWS Marketplace for structured TPRM workflows. Common sovereignty-specific assessment criteria include: 
   +  **Data residency and cross-border transfers:** Where does the vendor store and process your data? Does data cross jurisdictional boundaries during processing, and do they use sub-processors in other jurisdictions? 
   +  **Operator location:** Are the vendor's operational support staff located in approved jurisdictions? What access do they have to your data? 
   +  **Jurisdiction-specific certifications:** Does the vendor hold certifications relevant to your jurisdiction (for example, C5 in Germany, SOC 2, and ISO 27001)? 
   +  **Data portability:** Does the vendor support data portability? Can you extract your data in standard formats if you need to change providers? 

1.  **Configure a vendor management database:** Track vendor profiles, risk scores, compliance status, contract details, and sovereignty-specific attributes (data residency, operator locations, and certifications). Schedule regular reviews and re-assessments aligned with vendor risk tiers. 

1.  **Set up automated monitoring for sovereignty drift:** Monitor the resources in your own accounts that connect to vendor services, and alert on changes that could route regulated data to a vendor outside approved boundaries. 
   +  Use [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) to detect drift in vendor-facing connectivity: changes to VPC endpoint (PrivateLink) configurations, VPC peering and Transit Gateway attachments, security group egress rules, and Amazon S3 cross-Region replication. Flag resources created outside approved Regions. 
   +  Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) rules on [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) management events (such as CreateVpcEndpoint, CreateVpcPeeringConnection, AuthorizeSecurityGroupEgress, and Route 53 Resolver rule changes) to alert when a new path to a vendor endpoint is created or modified. 
   +  Enable [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) and [Route 53 Resolver query logging](https://docs.aws.amazon.com/Route 53/latest/DeveloperGuide/resolver-query-logs.html) to record egress and DNS resolution to vendor endpoints, so you can confirm traffic matches the vendor's documented data-flow paths. 
   +  Aggregate these findings in [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) and route alerts through [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) so a reviewer can confirm the change keeps vendor data within approved jurisdictions. 

1.  **Establish contractual sovereignty safeguards:** Contractual controls complement technical controls by establishing obligations around data handling. Verify that vendor contracts address the following sovereignty-specific areas: 
   +  **Data residency clauses:** Approved jurisdictions for data storage and processing. 
   +  **Breach notification timelines:** Alignment with your regulatory notification requirements. 
   +  **Data portability and exit provisions:** Exit procedures, data formats, and associated charges. 
   +  **Sub-processor usage:** Sub-processor locations and purpose. 

1.  **Validate vendor data residency:** Verify that vendor data flows remain within approved jurisdictional boundaries. Where a vendor exposes its service through an endpoint service, use [AWS PrivateLink](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.html) to connect privately without traversing the public internet. Review the vendor's documentation on AWS Region usage and data flow architecture, and monitor network traffic to vendor endpoints to verify that data flows match documented paths. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC03-BP09 Share resources securely with a third party](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_share_securely_third_party.html) 
+  [SEC03-BP08 Share resources securely within your organization](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_share_securely.html) 
+  [OPS01-BP04 Evaluate compliance requirements](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_compliance_reqs.html) 

 **Related documents:** 
+  [Plan your AWS account governance structure](https://docs.aws.amazon.com/accounts/latest/reference/plan-acct-structure.html) 
+  [AWS designated as a critical third-party provider under EU's DORA regulation](https://aws.amazon.com/blogs/security/aws-designated-as-a-critical-third-party-provider-under-eus-dora-regulation/) 
+  [AWS User Guide to Financial Services Regulations and Guidelines in the EU](https://d1.awsstatic.com/whitepapers/compliance/AWS_User_Guide_to_Financial_Services_Regulations_and_Guidelines_in_the_EU.pdf) 
+  [Amazon Web Services' Approach to Operational Resilience in the Financial Sector & Beyond](https://d1.awsstatic.com/whitepapers/compliance/AWS_Operational_Resilience.pdf) 

 **Related videos:** 
+  [AWS re:Inforce 2024 - Automation in action: Strategies for risk mitigation (GRC301)](https://www.youtube.com/watch?v=gbo-Z01NTc8) 

 **Related examples:** 
+  [AWS Marketplace](https://aws.amazon.com/marketplace/) for discovering vendors with AWS security reviews and relevant certifications 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS Marketplace](https://aws.amazon.com/marketplace/) 
+  [AWS PrivateLink](https://aws.amazon.com/privatelink/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 