

# FND06-BP06 Build strategies for commitment discounts and volume-based pricing

 Establish an organization-wide strategy for using cloud pricing models and commitment-based discounts across all accounts. Centralize management of commitment-based offerings to maximize cost savings while maintaining operational flexibility. Surface commitment and reservation recommendations at the organization level so purchasing decisions reflect consolidated usage. 

 **Desired outcome:** 
+  You have an optimized savings strategy through the use of commitment-based discounts. 
+  You have centralized management of pricing models across the organization. 
+  You maximize utilization of commitments and volume-based discounts. 
+  You have automated processes for commitment management and optimization. 

 **Common anti-patterns:** 
+  Over-committing to long-term discounts without considering flexibility needs and other workload optimization opportunities such as rightsizing, modernization, and waste reduction. 
+  Purchasing commitments at member account level when organization-focused purchases provide better savings. 
+  Failing to consider all available commitment options. 
+  Not reviewing and adjusting commitment strategies regularly. 
+  Using On-Demand pricing for predictable, long-running workloads. 
+  Lacking a centralized strategy for commitment purchases. 

 **Benefits of establishing this best practice:** 
+  Significant cost reduction through volume and commitment discounts, often 20–70 percent depending on commitment type and term length. 
+  Better alignment of costs with long-term business planning through predictable pricing. 
+  Reduced operational overhead through centralized management. 
+  Optimized utilization of commitments across the organization by sharing discounts across accounts and workloads where usage patterns complement each other. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Commitment-based pricing trades flexibility for cost savings. The discount sizes are significant (20–70 percent depending on the commitment type and term), but making the trade-off well requires analyzing usage patterns at the organization level. The management account gives you consolidated visibility across all member accounts. 

 Savings Plans offer flexibility across multiple services (Compute Savings Plans or Database Savings Plans), specific instance families (EC2 Instance Savings Plans), or specific services (SageMaker AI Savings Plans). Reserved Instances provide service-specific savings for services such as Amazon RDS, Amazon Redshift, Amazon ElastiCache, Amazon OpenSearch Service, Amazon DynamoDB, and Amazon MemoryDB. AWS Elemental reservations are available for Amazon MediaLive, Amazon MediaConvert, and Amazon MediaConnect. The Security Savings Bundle offers combined savings on Amazon CloudFront and AWS WAF. Volume-based and tiered pricing for services like Amazon S3 and AWS DataSync provides additional benefit when consolidated within an AWS Organization. 

 Figure 1 illustrates how a sample web application workload (built on services such as Amazon Route 53, AWS WAF, Amazon CloudFront, Amazon EC2, Amazon RDS, Elastic Load Balancing, Amazon S3, and Amazon EFS) maps to the commitment options available. <a name="fnd06-bp06-fig1"></a>

![Diagram showing a sample web application built on Amazon Route 53, AWS WAF, Amazon CloudFront, Amazon EC2, Amazon RDS, Elastic Load Balancing, Amazon S3, and Amazon EFS, with each service mapped to the Reserved Instance or Savings Plans commitment options available.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/ri-sp-services.png)

*Mapping a web application workload to Reserved Instance and Savings Plans commitments*


 For services that can benefit from both Reserved Instances and Savings Plans discounts, AWS applies Reserved Instances first. Within Savings Plans, EC2 Instance Savings Plans apply before Compute Savings Plans. This means the most restrictive (and therefore highest-discount) commitments are exhausted first before broader commitments cover the remaining usage. 

 [Commitment sharing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html) is turned on by default in AWS Organizations, so SPs and RIs purchased at the management account level apply across all member accounts. This maximizes utilization because a shared pool absorbs fluctuations across the organization better than fragmented per-account pools. Some organizations turn off sharing to improve cost accountability for individual teams, but this risks underutilization. If cost accountability is the driver, [AWS Billing and Cost Management Conductor](https://aws.amazon.com/aws-cost-management/aws-billing-conductor/) is usually a better answer, because it preserves the sharing benefit while supporting custom billing rates, credit and fee distribution, and per-team overhead allocation. 

 Purchasing commitments before rightsizing locks overprovisioned capacity into the commitment term. A safer order is to eliminate waste first (unused resources, idle instances), then rightsize compute, then evaluate [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) for fault-tolerant workloads, and only then commit to the stable baseline that remains. Spot covers variable, fault-tolerant workloads and commitments cover the predictable baseline, and both can run in parallel within the same optimization strategy. Partial commitments in the 50–70 percent range of baseline usage preserve flexibility for ongoing optimization and workload changes while still capturing meaningful discount. 

 Regular, smaller purchases adapt better than large infrequent ones. A monthly or quarterly rhythm lets the commitment portfolio evolve as usage patterns shift, reduces the financial risk of any single decision, and responds faster to new workloads or optimization gains that move the baseline. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish commitment management governance:** Define roles and responsibilities for commitment purchases across your organization. Consider enforcing commitment management policies that only allow relevant stakeholders to make final purchasing decisions. Implement approval workflows for different commitment types and amounts. 

1.  **Configure commitment sharing across accounts:** Turn on [RI and SP discount sharing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html) in your AWS Organization for broader benefit, unless your business requirements mean that individual teams need to purchase their own commitment discounts (which in some cases might be a budgeting or cost allocation requirement). If you're considering turning off the commitment sharing feature to improve cost accountability for internal teams, consider using [AWS Billing and Cost Management Conductor](https://aws.amazon.com/aws-cost-management/aws-billing-conductor/) instead. This provides customizable billing to meet complex business needs, so you can customize billing rates, distribute credits and fees, and share overhead costs and discounts at your discretion. Create processes for regular review and adjustment of commitments. 

1.  **Analyze usage patterns:** Configure [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) with hourly granularity to understand your baseline consumption. Use the [Savings Plans Purchase Analyzer](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-analyzer.html) for detailed planning. Review AWS Cost Explorer recommendations for both Savings Plans and Reserved Instances, examining projected savings, utilization rates, and payback periods. Consider implementing [AWS Cloud Intelligence Dashboards](https://docs.aws.amazon.com/solutions/advanced-cloud-observability-with-cloud-intelligence-dashboards-on-aws/) for advanced visualization of usage trends. 

1.  **Rightsize resources before purchasing commitments:** Evaluate rightsizing opportunities before committing to discounts to avoid locking in overprovisioned resources. Use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) recommendations as inputs to your commitment strategy. This step is critical, because purchasing commitments on top of oversized resources locks in waste for the commitment term. Address modernization roadmaps too: if workloads are moving to containers, serverless, or Graviton, commitments on the existing footprint might not pay back. 

1.  **Select your Savings Plans mix:** Start with [Compute Savings Plans](https://aws.amazon.com/savingsplans/compute-pricing/) and [Database Savings Plans](https://aws.amazon.com/savingsplans/database-pricing/) for maximum flexibility. Add [EC2 Instance Savings Plans](https://aws.amazon.com/savingsplans/compute-pricing/) where the instance family is stable but Region or OS might change. Mix one-year and three-year terms to balance discount depth with flexibility, and start with partial commitments (50–70 percent of baseline usage) to preserve flexibility for continued optimization and [Spot Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) adoption. 

1.  **Add Reserved Instances for deeper service-level discounts:** Add [service-specific Reserved Instances](https://docs.aws.amazon.com/cost-management/latest/userguide/ri-recommendations.html) for [Amazon RDS](https://aws.amazon.com/rds/), [Amazon Redshift](https://aws.amazon.com/redshift/), [Amazon ElastiCache](https://aws.amazon.com/elasticache/), [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/), [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), and [Amazon MemoryDB](https://aws.amazon.com/memorydb/) where usage is predictable. Evaluate the [Security Savings Bundle](https://aws.amazon.com/cloudfront/pricing/) for [Amazon CloudFront](https://aws.amazon.com/cloudfront/) and [AWS WAF](https://aws.amazon.com/waf/), and volume-based discount opportunities for services such as [Amazon S3](https://aws.amazon.com/s3/) and [AWS DataSync](https://aws.amazon.com/datasync/). 

1.  **Plan commitment purchase cadence:** Align purchases with business cycles, budgets, and cost optimization cycles. Implement regular, smaller purchases rather than large, infrequent commitments. This approach reduces risk by letting you adjust your commitment strategy as usage patterns evolve. 

1.  **Monitor commitment utilization and coverage:** Use [SP/RI utilization and coverage reports](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-monitoring.html) to track how your commitments are being used. Utilization measures how much of what you committed to is actually consumed. Consistently above 98 percent signals you can commit more. Sustained below 90 percent signals waste or workload shifts that need investigation. Coverage measures what percentage of eligible spend is protected by commitments, so low coverage points to opportunities for additional purchases. Tracking both together gives the complete picture of commitment effectiveness. Configure utilization alerts through [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) and set up automated reporting using [AWS Budget Reports](https://docs.aws.amazon.com/cost-management/latest/userguide/reporting-cost-budget.html). 

1.  **Establish commitment governance controls:** Restrict commitment purchase authorization to approved roles using [IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) for individual accounts or [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) for organization-wide enforcement. For specific Savings Plans and Reserved Instance purchase actions, see [Actions defined by AWS Savings Plans](https://docs.aws.amazon.com/service-authorization/latest/reference/). Tag resources to track how business units or teams benefit from shared commitments. Build internal chargeback mechanisms for advanced distribution of commitment benefits across the organization. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND06-BP01 Configure detailed cost information sources](fnd06-bp01.md) 
+  [FND06-BP03 Configure billing and cost management tools](fnd06-bp03.md) 
+  [FND06-BP04 Optimize software licensing and third-party agreements](fnd06-bp04.md) 
+  [FND06-BP05 Establish organizational metrics to track optimization efforts](fnd06-bp05.md) 

 **Related documents:** 
+  [Understanding your Savings Plans recommendations](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-recommendations.html) 
+  [Accessing Reserved Instance recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ri-recommendations.html) 
+  [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) 
+  [Services eligible for Savings Plans benefits](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-services.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Win-win: Maximize Amazon EC2 savings while improving performance (CMP214)](https://www.youtube.com/watch?v=UzibL6r9ChM) 

 **Related examples:** 
+  [What should you consider before purchasing Savings Plans?](https://repost.aws/knowledge-center/savings-plans-considerations) 
+  [AWS Savings Plans: How to Implement an Effective Chargeback Strategy](https://aws.amazon.com/blogs/aws-cloud-financial-management/aws-savings-plans-how-to-implement-an-effective-chargeback-strategy/) 