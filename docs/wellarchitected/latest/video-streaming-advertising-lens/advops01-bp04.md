

# ADVOPS01-BP04 Establish data governance and compliance operations
<a name="advops01-bp04"></a>

 Advertising data management requires governance and compliance procedures for Multi-Region environments, where regional privacy laws vary by jurisdiction. Procedures must cover application logs, managed connectivity service logs, and agentic AI agent traces. 

 **Desired outcome:** 
+  Data governance procedures cover all layers of the advertising stack, such as application logs, managed connectivity service logs (RTB Fabric), and agentic AI agent traces and reasoning chains. 
+  Retention policies, access controls, and compliance monitoring are defined per data type and jurisdiction (GDPR for EU data, CCPA for California data, and COPPA for child-directed content). 
+  Agent traces from agentic AI advertising workflows have documented retention policies that balance operational needs with data minimization principles. 

 **Common anti-patterns:** 
+  Treating managed connectivity service logs as equivalent to application logs without recognizing that they may contain partner identifiers and traffic management decisions subject to separate compliance requirements. 
+  Retaining agentic AI agent traces indefinitely without a defined retention policy, accumulating campaign data, audience information, and automated decisions without audit controls. 
+  Applying a single data retention policy to all advertising data regardless of jurisdiction, data type, or consent scope. 

 **Benefits of establishing this best practice:** 
+  Enables proactive identification of compliance gaps before they become enforcement actions. 
+  Supports multi-framework compliance (GDPR, CCPA, COPPA, IAB TCF, and TAG) from a single data governance architecture. 
+  Reduces audit preparation time by maintaining ongoing compliance evidence. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising data governance spans multiple regulatory frameworks, and a single bid request may contain data subject to multiple regulatory frameworks at once. Classify data at collection time, and enforce retention and access policies at the storage and processing layers. This design avoids per-request regulatory routing logic. 

 Agent traces contain both personal data and the reasoning behind automated bid or audience decisions. Privacy regulations require you to discard the personal data promptly. Some jurisdictions require you to keep the reasoning for audit. Separate the reasoning from the personal data it referenced, so the decision record survives without the identifiers that made it sensitive. 

 Connectivity-layer logs are another category without a clear owner. Network infrastructure produces them, which suggests the network team, but their contents are commercial, such as which partners sent what volume, and which requests were throttled or filtered. That data is competitively sensitive information about counterparties, with an exposure profile distinct from bid data. Because the infrastructure team treats them as operational and the advertising team might not know they exist, the logs accumulate without a retention period. Classify connectivity-layer logs as their own category, distinct from bid logs, to prevent this default. 

 Enforce residency at the account and permission layer. When you enforce residency in application logic, each service must implement the restriction separately. The control is only as strong as the newest service written by the team least aware of the requirement. A newly added service can violate the restriction without triggering an alert. At the account and permission layer, residency becomes a property of the environment, so the restriction applies regardless of what any individual service does. Account-level controls are coarser, though, so test them against real workflows first. They can block legitimate work with confusing permission errors rather than clear policy messages. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Classify advertising data by regulatory scope and retention requirement:** Create a data classification inventory covering each data type (bid requests, impression logs, user profiles, campaign configurations, agent traces, and connectivity logs). For each type, document: applicable regulations, maximum retention period, required access controls, encryption requirements, and the team responsible for enforcement. Use AWS Glue Data Catalog to register classifications as metadata tags on data assets. 

1.  **Define retention policies for agentic AI agent traces:** Establish separate retention policies for agent traces based on their content sensitivity. For traces containing targeting data and audience information, apply retention limits aligned with the underlying data's consent scope (typically 30–90 days). For traces used for model optimization and debugging, apply minimum retention for operational utility. Implement automated redaction of sensitive fields (audience identifiers, PII) from agent traces before long-term storage using AWS Glue ETL jobs. 

1.  **Establish data governance for managed connectivity service logs:** Define ownership for RTB Fabric or equivalent managed connectivity logs as a distinct data category. Document retention periods (typically 30 days for operational debugging, shorter for partner identifier data), access controls (limit access to network operations and security teams), and the review process for logs containing partner commercial data. Configure Amazon CloudWatch Logs delivery for connectivity logs with appropriate log group retention settings. 

1.  **Deploy ongoing compliance monitoring with AWS Config:** Create custom AWS Config rules that verify: encryption is enabled on all data stores containing advertising data, CloudTrail is active in all regions processing advertising data, S3 buckets with audience data have appropriate bucket policies, and data stores have lifecycle policies configured. Set Config rules to evaluate on configuration change and periodically. Route noncompliant findings to AWS Security Hub for centralized tracking. 

1.  **Implement IAM Permission Boundaries for regional data residency:** For advertising workloads processing EU viewer data, configure IAM Permission Boundaries with aws:RequestedRegion conditions that restrict principals from creating resources or accessing data outside designated regions. Apply Service Control Policies (SCPs) at the AWS Organizations level to enforce region restrictions for advertising accounts handling EU or California resident data. Test boundary enforcement by attempting to create a restricted resource from outside the allowed region. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Data Residency with Hybrid Cloud Services Lens](https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/data-residency-with-hybrid-cloud-services-lens.html) 
+  [Configuring RTB Fabric logs with Amazon CloudWatch Logs](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch-logs.html) 
+  [Amazon Bedrock Agent Tracing documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) 

 **Related services:** 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [Amazon Macie](https://aws.amazon.com/macie/) 