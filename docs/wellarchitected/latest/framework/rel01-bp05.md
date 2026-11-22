

# REL01-BP05 Automate quota management

 Manual quota tracking drifts out of date as a workload grows and spreads across accounts and Regions. Automate the monitoring of usage against quotas, and consider automating the increase requests. Automation keeps quota values aligned with real demand and removes the human delay between noticing a quota and acting on it. 

 **Desired outcome:** 
+  Quotas are configured to match the workload running in each account and Region, and stay aligned as demand changes. 
+  Automated monitoring tracks usage against quotas and alerts you before a quota is reached. 
+  New accounts inherit quota monitoring and baseline increases automatically when they are created. 
+  You track the status of increase requests across all accounts from one place. 

 **Common anti-patterns:** 
+  Teams do not adjust quotas to match workload requirements as they change. 
+  Teams track quotas and usage in tools that go stale, such as spreadsheets. 
+  Teams update quotas only on a periodic schedule rather than in response to usage. 
+  Teams have no operational process to review quotas and request increases when needed. 

 **Benefits of establishing this best practice:** 
+  Automated monitoring prevents errors caused by exceeding a resource quota. 
+  Quota mechanisms built in the primary Region can be reused when setting up a disaster recovery Region. 
+  New accounts are monitored from creation, so coverage keeps pace with organizational growth. 
+  Centralized request tracking shows where increases are pending or stalled across the organization. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 To keep quota data current, read current values and usage programmatically through the [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) console, the AWS CLI, or the SDKs. Integrate those APIs with a configuration management database or IT service management system to tie quota state into the tools your operations teams already use. 

 Automated increase requests remove the delay between an alert and an action, which is valuable for a business-critical workload. They also introduce risk. An automation that requests more capacity as usage rises can enter a feedback loop. Growth triggers an increase, which enables more growth, which triggers another increase. Test any auto-request automation carefully, and bound it so a runaway condition cannot escalate quotas without limits. For many workloads, automate the alert and the request preparation, but require human approval before submitting the request. 

 Approval time determines how far ahead you must act. Smaller increases are often approved automatically and take effect quickly. Larger requests are reviewed by Support and take longer, and submitting several large requests together extends the wait further. Automation does not remove this lead time, but it gives you time to absorb the wait. It detects the trend early and starts the request before the quota is reached. 

 A workload that spans many accounts and Regions is impractical to manage manually. The same automated monitoring, request templates, and dashboards apply to all accounts and Regions uniformly. Because the mechanism is reproducible, the quota setup you build for a primary Region becomes the setup for a disaster recovery Region, so automated quota management simplifies DR. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Automate quota monitoring and alerting:** Deploy automated monitoring that tracks usage against quotas and alerts as consumption approaches a quota. [Quota Monitor for AWS](https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/solution-overview.html) integrates with AWS Organizations and deploys through AWS CloudFormation StackSets, so new accounts are monitored automatically on creation. For monitoring design (thresholds, response processes), see [REL01-BP04 Monitor and manage quotas](rel01-bp04.md). 

1.  **Standardize quota setup for new accounts:** Use [Service Quotas request templates](https://docs.aws.amazon.com/servicequotas/latest/userguide/organization-templates.html) or [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) to apply baseline quota increases consistently when accounts are provisioned. 

1.  **Build cross-account, cross-Region dashboards:** Create dashboards of current quota usage across all accounts and Regions and reference them during planning. The [Cloud Intelligence Dashboards](https://catalog.workshops.aws/awscid/en-US) provide a Trusted Advisor organizational view to start from. 

1.  **Track increase requests centrally:** Maintain an organization-level view of every pending and completed increase request so no request is lost. Aggregating case data across accounts gives operators one place to check request status. 

1.  **Test automation with lower thresholds in non-production:** Validate alert generation and any auto-request automation by setting lower quota thresholds in non-production accounts. Do not run these tests in a production account. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL01-BP04 Monitor and manage quotas](rel01-bp04.md) 
+  [REL01-BP02 Manage service quotas across accounts and regions](rel01-bp02.md) 
+  [REL01-BP06 Verify that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover](rel01-bp06.md) 
+  [OPS06-BP02 Automate responses to events](ops06-bp02.md) 

 **Related documents:** 
+  [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) 
+  [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) 
+  [Using Service Quotas request templates](https://docs.aws.amazon.com/servicequotas/latest/userguide/organization-templates.html) 
+  [Monitor resource usage and send notifications when approaching quotas - Quota Monitor for AWS](https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/solution-overview.html) 
+  [AWS Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html) 
+  [A detailed overview of Trusted Advisor Organizational Dashboard](https://aws.amazon.com/blogs/mt/a-detailed-overview-of-trusted-advisor-organizational-dashboard/) 

 **Related videos:** 
+  [How do I manage my service quotas for my AWS services?](https://www.youtube.com/watch?v=Ddf5WG5I0Qo) 

 **Related examples:** 
+  [GitHub - aws-samples/case-insights-for-multi-accounts: AWS-CIMA (Consolidated Insights for Multi-Accounts) is a sample solution to provide single pane of glass of support cases for multiple accounts and multiple AWS Organizations](https://github.com/aws-samples/case-insights-for-multi-accounts) 
+  [Cloud Intelligence Dashboards](https://catalog.workshops.aws/awscid/en-US) 

 **Related tools:** 
+  [GitHub - aws-solutions/quota-monitor-for-aws: This solution leverages AWS Trusted Advisor and Service Quotas to monitor AWS resource usage and raise alerts.](https://github.com/aws-solutions/quota-monitor-for-aws) 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) 