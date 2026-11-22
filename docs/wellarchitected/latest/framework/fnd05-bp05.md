

# FND05-BP05 Maintain an auditable cloud inventory record

 An auditable inventory record captures what resources exist, how they are configured, and how they have changed over time. It emphasizes completeness, immutability of history, and alignment with evidence. A well-maintained, audit-ready inventory improves security investigations and forensic reconstruction. 

 **Desired outcome:** 
+  You have deployed automated discovery and cataloging tools that continuously identify and track all cloud resources, with a centralized inventory system that consolidates asset information across cloud providers and on-premises infrastructure. 
+  Your inventory captures detailed metadata for each asset (ownership, purpose, cost, security posture, and compliance status), along with a standardized tagging strategy that categorizes and organizes resources. 
+  You maintain a complete change history that records every resource modification, including who made the change and when it occurred. 
+  Your inventory system provides APIs and automation capabilities that integrate with other systems and support DevOps workflows, and it aligns with relevant compliance frameworks to speed up audits. 
+  You have implemented real-time monitoring and alerting for inventory changes, with cost and usage signals incorporated to help surface unexpected or unauthorized resource deployments during audits. 

 **Common anti-patterns:** 
+  Relying on manual inventory tracking that quickly becomes outdated in dynamic cloud environments. 
+  Lacking a centralized inventory system, leading to fragmented visibility across accounts and Regions. 
+  Not maintaining change history for resources, making audits and forensic investigations difficult. 
+  Failing to integrate cloud inventory with compliance frameworks and regulatory requirements. 
+  Not incorporating cost data into the inventory, missing a signal that can surface unexpected or unauthorized resource deployments during audits. 

 **Benefits of establishing this best practice:** 
+  A full view of all resources across accounts and Regions supports security oversight and surfaces shadow IT, unmanaged resources, and configuration drift that might indicate non-compliance. 
+  Accurate, audit-ready inventory simplifies compliance processes and regulatory audits through detailed, verifiable records. 
+  Change history tracking supports forensic investigations, change management, and root cause analysis. 
+  Automated discovery and cataloging reduce manual effort and improve inventory accuracy and completeness for audit evidence. 
+  The ability to answer what the environment looked like at a specific moment supports investigations, compliance reviews, and regulatory inquiries. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 In cloud environments, resources are provisioned, modified, and decommissioned continuously. Manual inventory tracking cannot keep pace with these changes, so auditable inventory must be automated. Continuous, automated discovery and immutable change history creates a foundation for security investigations, cost optimization, and strategic decision-making. 

 Capture the current state of your resources, detailed resource metadata, and a historical record for those resources. [AWS Config](https://aws.amazon.com/config/) provides a detailed inventory of AWS resources, tracks configuration changes with a complete timeline, and evaluates configurations against desired-state rules. Add [AWS Systems Manager Inventory](https://aws.amazon.com/systems-manager/) to capture OS-level metadata from managed instances. 

 [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) records the API activity behind each change, so you can see who changed a resource and how. [AWS Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/welcome.html) provides fast cross-account and cross-Region search so you can locate every occurrence of a resource during audits or incidents. [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) adds utilization metrics that show whether resources are being used. [Resource groups](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) and [Tag Editor](https://docs.aws.amazon.com/tag-editor/latest/userguide/) organize resources for management at scale. Inventory becomes a dynamic, queryable, analyzable dataset that supports a wide range of use cases. 

 Use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) and [AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) with a consistent tagging strategy to associate spend with applications, environments, or owners. For audits, cost signals can reveal unexpected deployments that indicate misconfiguration or unauthorized activity. 

 A common failure mode is treating inventory as a point-in-time snapshot rather than a continuous stream. For example, an organization that periodically exports resource lists to spreadsheets might find that their inventory is outdated as soon as they save the file. Automation is the only viable approach at cloud scale. 

**Important**  
 Establish clear ownership for inventory accuracy, define retention periods for historical data based on compliance requirements, and integrate inventory reviews into your regular operational cadence. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable automated asset discovery:** Implement solutions that continuously scan and catalog all resources across your cloud environments. [AWS Config](https://aws.amazon.com/config/) provides a detailed inventory of AWS resources and configurations. See [Setting Up AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html). Use [AWS Config aggregators](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html) to centralize configuration data across accounts and Regions into a single view. Turn on [AWS Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/getting-started.html) for fast cross-account, cross-Region search when investigators need to locate specific resources. For OS-level metadata, use [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html). 

1.  **Configure detailed logging and auditing:** Turn on full logging for all cloud services to capture resource lifecycle events, access attempts, and configuration changes. [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) records API activity. See [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html). Use [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_GettingStarted.html) to centrally store and analyze logs. Configure [AWS Config](https://aws.amazon.com/config/) to [track resource configuration changes](https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder.html) and detect non-compliant resources. 

1.  **Implement a standardized tagging strategy:** Use [resource tags](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) to categorize and organize resources by ownership, environment, cost center, and other relevant metadata. See [Tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html). Enforce required tags and permitted values across the organization using [tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) in AWS Organizations. 

1.  **Store infrastructure configurations in version control:** Track and manage changes to cloud configurations over time, enabling rollback and change auditing. Store [AWS CloudFormation](https://aws.amazon.com/cloudformation/) templates, [AWS CDK](https://aws.amazon.com/cdk/) code, and other IaC configurations in version control to maintain a complete history of infrastructure changes. Combine this with code review and branch protection so changes are auditable and reversible. 

1.  **Conduct regular inventory audits:** Perform periodic comparisons between your inventory system and actual cloud resources to identify discrepancies. Use [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) to continuously evaluate resource configurations against desired states, and [AWS Config advanced queries](https://docs.aws.amazon.com/config/latest/developerguide/querying-AWS-resources.html) to run SQL-like queries across your resource inventory for reconciliation reports. 

1.  **Implement change alerting:** Configure alert mechanisms for immediate notification of inventory changes, potential security issues, and compliance violations. Use [Amazon EventBridge](https://aws.amazon.com/eventbridge/) rules to monitor configuration changes and [Amazon SNS](https://aws.amazon.com/sns/) to notify relevant teams. See [Monitoring AWS Config with Amazon EventBridge](https://docs.aws.amazon.com/config/latest/developerguide/monitor-config-with-cloudwatchevents.html). 

1.  **Integrate cost and usage data:** Enrich inventory records with cost data so unexpected or unauthorized resource deployments are more visible during audits. Use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) and the [AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) together with a consistent tagging strategy to allocate spend to applications, environments, and owners. This creates a financial signal alongside configuration data that helps surface anomalies and supports lifecycle decisions. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND04-BP02 Establish an organization view of cloud inventory and dependencies](fnd04-bp02.md) 
+  [FND05-BP03 Configure audit logging of cloud operations](fnd05-bp03.md) 
+  [FND05-BP06 Remediate non-compliant resources](fnd05-bp06.md) 

 **Related documents:** 
+  [Establishing Your Cloud Foundation on AWS](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/welcome.html) 
+  [Tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) 
+  [Conformance Packs in AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) 
+  [AWS Config best practices](https://docs.aws.amazon.com/config/latest/developerguide/) 
+  [What is AWS Resource Explorer?](https://docs.aws.amazon.com/resource-explorer/latest/userguide/welcome.html) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Centralize your operations (COP320)](https://www.youtube.com/watch?v=9-RBjmhDdaM) 