

# FND06-BP03 Configure billing and cost management tools

 Configure cost management tools that provide organization-wide visibility, control, and optimization capabilities. With this foundation, central teams govern cloud spending, and business units have appropriate access to cost data and optimization tools. 

 **Desired outcome:** 
+  You have centralized cost monitoring, reporting, and optimization across the AWS Organization with clear visibility into cloud spending for all stakeholders. 
+  Your standardized cost management processes support real-time data-driven decisions. 

 **Common anti-patterns:** 
+  Lacking centralized governance of cost management capabilities. 
+  Not providing appropriate cost visibility to different stakeholder groups. 
+  Operating without automated cost monitoring and alerting. 
+  Managing costs reactively rather than proactively. 
+  Implementing tools without considering organizational structure. 

 **Benefits of establishing this best practice:** 
+  Improved financial governance and control with better cost visibility and allocation across the organization while supporting self-service cost management. 
+  Proactive cost optimization through automated monitoring and alerting. 
+  Standardized and automated cost optimization workflows. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A reliable cost management tooling framework must address the needs of different stakeholder groups while maintaining centralized control and governance. Collectively, these tools need to support organizing and tracking cost and usage data, improve control through consolidated billing and access permissions, improve financial planning with budgeting and forecasting, deliver proactive notifications and alerts, and surface resource and pricing optimizations to reduce overall costs. 

 Executive leaders need high-level trends and ROI metrics, finance teams need attribution and variance reports, and engineering teams need resource-level detail for optimization decisions. If any of these groups lack the tools they need, cost management either becomes a bottleneck or a blind spot. Central teams should establish the foundation and guardrails while business units manage their costs effectively within those boundaries. 

 Users need appropriate access to the tools that show their costs and usage. A well-designed [tagging strategy and taxonomy](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/building-your-tagging-strategy.html), a multi-account structure in [AWS Control Tower](https://aws.amazon.com/controltower/) and [AWS Organizations](https://aws.amazon.com/organizations/), and [AWS Cost Categories](https://aws.amazon.com/aws-cost-management/aws-cost-categories/) provide the baseline cost attribution that other tools rely on. Access controls enforce team permissions, and consolidated billing provides organization-wide visibility. Guardrails such as [SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [RCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html), [tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html), [IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html), and [budget alerts](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) prevent unintended cost behaviors (for example, resource creation in non-approved Regions or without required tags). 

 Configure notifications for budget threshold crossings and cost anomalies. Tailor reports to each audience with recommendations, goal tracking, and appropriate time granularity (hourly, daily, monthly). Make dashboards visible in high-traffic work areas. Route notifications about new optimization opportunities through [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), [Amazon SNS](https://aws.amazon.com/sns/), or [Amazon SES](https://aws.amazon.com/ses/). 

 Where internal skills or bandwidth fall short, [AWS Professional Services](https://aws.amazon.com/professional-services/) and [AWS Partners](https://aws.amazon.com/partners/) can help build or mature these capabilities. Third-party tools can also add value, though their pricing models deserve scrutiny. Tools that charge a percentage of your AWS bill, for example, need to deliver value that scales with that bill. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish consolidated billing and data collection:** Use [AWS Organizations](https://aws.amazon.com/organizations/) since it uses [consolidated billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html), which is the prerequisite for organization-wide cost visibility. Use [AWS Data Exports](https://aws.amazon.com/aws-cost-management/aws-data-exports/) (or AWS Cost and Usage Reports for existing implementations) to collect detailed billing data. 

1.  **Allow team-based access to tools:** Configure accounts and create groups with access to the required cost and usage reports using [AWS IAM](https://aws.amazon.com/iam/) to [control access](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-access.html) to tools such as [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/). Include representatives from all teams that own or manage applications. Control cost management data access with [Billing Views](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-view.html) through resource-based policies. 

1.  **Organize costs by tags and categories:** Tag resources with [cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) to organize costs across teams, business units, applications, environments, and projects. After you activate resource tags for cost allocation on the management payer account, these dimensions become available in reporting tools. Create [AWS Cost Categories](https://aws.amazon.com/aws-cost-management/aws-cost-categories/) based on tags, accounts, or services to map costs to business categories. 

1.  **Configure AWS Budgets:** [Configure AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) on all accounts for your workloads. Set budgets for overall account spend and for workloads using tags and cost categories. Configure [budget notifications](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-sns-policy.html) to alert when you exceed or are forecasted to exceed budgeted amounts. 

1.  **Configure AWS Cost Anomaly Detection:** Use [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) on accounts, core services, or cost categories to detect unusual spending. Receive alerts individually or in aggregated reports through email or [Amazon SNS](https://aws.amazon.com/sns/) topics to analyze root causes. 

1.  **Use cost analysis tools:** Configure [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to visualize cost data for analysis. Create workload dashboards that track overall spend, key usage metrics, and forecasts based on historical cost data. 

1.  **Use cost-saving analysis tools:** Review cost optimization recommendations in [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) and [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to identify savings opportunities: rightsizing, Savings Plans, reservations, and idle resource deletion. [Set up memory metrics on your EC2 instances](https://aws.amazon.com/blogs/mt/setup-memory-metrics-for-amazon-ec2-instances-using-aws-systems-manager/) to maximize the accuracy of Compute Optimizer recommendations. Compute Optimizer also provides recommendations for [AWS Lambda](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-lambda-recommendations.html) functions, [Amazon EBS](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ebs-recommendations.html) volumes, [Amazon ECS services on AWS Fargate](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ecs-recommendations.html), and [Auto Scaling groups](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-asg-recommendations.html), so consider [custom configurations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendation-preferences.html) based on your requirements. 

1.  **Configure advanced tools:** Create visuals to support interactive analysis and sharing of cost insights. [With AWS Data Exports](https://aws.amazon.com/aws-cost-management/aws-data-exports/), export data and use the [Cost and Usage Dashboard](https://aws.amazon.com/blogs/aws-cloud-financial-management/new-cost-and-usage-dashboard-powered-by-amazon-quicksight/) or [AWS Cloud Intelligence Dashboards](https://docs.aws.amazon.com/solutions/advanced-cloud-observability-with-cloud-intelligence-dashboards-on-aws/) for advanced visualization. Consider different dashboards for different personas, because manager dashboards differ from engineering dashboards. Implement advanced analysis capability using data exports with [Amazon Athena](https://docs.aws.amazon.com/athena/?id=docs_gateway) for custom queries. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND06-BP01 Configure detailed cost information sources](fnd06-bp01.md) 
+  [FND06-BP02 Standardize cost attribution categories](fnd06-bp02.md) 
+  [FND06-BP05 Establish organizational metrics to track optimization efforts](fnd06-bp05.md) 

 **Related documents:** 
+  [What is AWS Compute Optimizer?](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) 
+  [What is AWS Data Exports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) 
+  [Identifying opportunities with Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) 
+  [Analyzing your costs with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) 
+  [Understanding your costs using AWS Cost Explorer reports](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-reports.html) 
+  [Analyzing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) 
+  [Reporting your metrics with AWS Budgets Reports](https://docs.aws.amazon.com/cost-management/latest/userguide/reporting-cost-budget.html) 
+  [Organizing costs using AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html) 
+  [Detecting unusual spend with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) 
+  [What is AWS Trusted Advisor?](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - What's new with AWS cost optimization (COP204)](https://aws.amazon.com/video/watch/c95c911fb8c/) 
+  [AWS re:Invent 2024 - Best practices and new tools for cost reporting and estimation (COP218)](https://aws.amazon.com/video/watch/b3039b4fbeb/) 

 **Related examples:** 
+  [Cost and Usage Dashboard powered by QuickSight](https://aws.amazon.com/blogs/aws-cloud-financial-management/new-cost-and-usage-dashboard-powered-by-amazon-quicksight/) 