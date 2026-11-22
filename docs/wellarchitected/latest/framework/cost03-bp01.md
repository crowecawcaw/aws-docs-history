

# COST03-BP01 Track resources over their lifetime

 Track each resource from provisioning to retirement so you can retire it when its purpose ends. Consistent tracking makes cleanup a routine you can automate. 

 **Desired outcome:** 
+  You know the purpose, owner, environment, and expected end date of every resource in your workload. 
+  Your resource utilization is monitored, so idle and abandoned resources surface without manual investigation. 
+  You can identify which resources are ready for decommissioning from tracking data alone. 
+  Your temporary and programmatically created resources carry the same tracking as long-lived resources. 

 **Common anti-patterns:** 
+  Teams add resource tracking only to production and leave development and test resources untracked. 
+  Tagging conventions differ across resource types, so reports miss resources that use a different key. 
+  Resource metadata records what a resource is but not when to retire it. 
+  Monitoring covers manually created resources and ignores the resources that automation provisions. 
+  Ephemeral resources fall outside the tracking strategy and linger after their task finishes. 

 **Benefits of establishing this best practice:** 
+  Costs fall because resources that no longer serve a purpose are found and removed. 
+  Optimization opportunities become visible when utilization data is tied to each resource. 
+  Resource lifecycle policies are more reliably enforced when every resource carries lifecycle metadata. 
+  Cleanup and decommissioning become repeatable because tracking data drives them. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A test environment left running overnight, a snapshot taken before a risky change, and a load balancer stranded after a migration all keep billing until someone notices. The organization loses track of why a resource exists and whether anyone still needs it. Record that context when you create the resource, and keep it current through every lifecycle state, so retirement becomes a decision based on data. 

 A tracking record answers four questions about a resource: what it is for, who owns it, which environment it belongs to, and when to retire it. Most tagging strategies omit the last question, so resources linger. A purpose tag such as feature-X testing explains why the resource exists. A time-based tag with a lifespan or time-to-live value states when it becomes a candidate for removal. Without an expiration signal, every retirement decision needs investigation, and investigation rarely happens. 

 Resources do not share a single lifecycle. Long-lived resources such as production databases change slowly. Temporary resources such as test fixtures, build artifacts, and short-lived environments are created and abandoned quickly, and generate most untracked waste. Resources that automation creates are the hardest to see, because no person decided to make them or remembers they exist. A tracking strategy that covers only what people provision manually will miss the resources that scale, replicate, or clone themselves. 

 Resources depend on one another, so deleting a resource that another component still references can break a workload. Dependency mapping records those relationships, so you can retire a resource knowing nothing else relies on it. Tags are not applied consistently by default. Use tag governance to define required keys and flag resources that lack them. 

 Several AWS services support tracking across the lifecycle. [AWS Organizations tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) define required tag keys and values across accounts, and [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) reports resources that fall out of compliance. [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) measures utilization so idle resources become visible, and [AWS Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) consolidates recommendations to remove them. For retirement, [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) collect the resources that make up an application, based on tags or a CloudFormation stack. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) with [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) runs scheduled checks that act on expired lifecycle tags. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define mandatory lifecycle tags:** Establish a tag schema that captures environment, purpose, owner, and an expiration or time-to-live value for temporary resources. Add a project or initiative tag for context. Document the required keys and allowed values so every team applies them the same way, and treat this schema as a prerequisite for the tracking that follows. 

1.  **Enforce tagging with governance controls:** Apply [AWS Organizations tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) to standardize keys and values across accounts, and use [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) to detect resources missing required tags. Group related resources with [resource groups](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) so you can report on them together. 

1.  **Monitor resource utilization:** Configure [Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) for utilization and add [custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) for workload-specific signals. Review [AWS Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) recommendations to find idle resources, and check [AWS Trusted Advisor cost optimization checks](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html) for additional candidates. 

1.  **Track dependencies and configuration state:** Use [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) to see the resources that belong to each application and [AWS Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html) to track configuration. Enable [AWS CloudFormation drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/detect-drift-stack.html) so you know when deployed resources diverge from their definitions before you retire them. 

1.  **Automate detection of expired resources:** Schedule checks with [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) that invoke [AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) to find resources whose time-to-live tags have passed. For managed cleanup, pair the checks with [AWS Config remediation actions](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html), [Systems Manager Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html), and [Amazon S3 object lifecycle configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) for stored data. 

1.  **Report and notify on lifecycle events:** Set [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) for resource states and route [Amazon S3 Lifecycle event notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configure-notification.html) to the teams that own the affected resources. Build tracking dashboards so owners can see decommissioning candidates, using solutions such as the [Cloud Intelligence Dashboards](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/getting-started.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST03-BP02 Implement efficient resource lifecycle management](cost03-bp02.md) 
+  [COST03-BP03 Enforce data retention policies](cost03-bp03.md) 
+  [COST02-BP01 Implement granular resource tagging for workload cost allocation](cost02-bp01.md) 

 **Related documents:** 
+  [Building your tagging strategy](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/building-your-tagging-strategy.html) 
+  [Identifying opportunities with Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) 
+  [AWS Trusted Advisor cost optimization checks](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html) 
+  [Detecting unmanaged configuration changes in stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) 
+  [Publishing custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Manage resource lifecycle events at scale with AWS Health (SUP309)](https://www.youtube.com/watch?v=VoLLNL5j9NA) 

 **Related examples:** 
+  [Organizing AWS resources](https://repost.aws/knowledge-center/resource-groups) 

 **Related tools:** 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [Service Catalog](https://aws.amazon.com/servicecatalog/) 
+  [AWS Backup](https://aws.amazon.com/backup/) 
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) 

 **Related workshops:** 
+  [CFM Technical Implementation Playbooks (CFM TIPs): Service cost optimization playbooks](https://catalog.workshops.aws/awscff/) 