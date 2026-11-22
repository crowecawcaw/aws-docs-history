

# FND06-BP04 Optimize software licensing and third-party agreements

 Establish organization-wide governance and processes for managing software licenses and third-party agreements. This includes centralizing license management, standardizing procurement processes, optimizing licensing costs, and using consolidated procurement channels for better commercial terms and billing. 

 **Desired outcome:** 
+  You have centralized and standardized governance for software procurement and license management. 
+  You have licensing costs aligned with actual usage and business value. 
+  You have a consolidated view of software spending and utilization. 
+  You maximize benefits from consolidated procurement channels. 

 **Common anti-patterns:** 
+  Inconsistent license management across different organizational units. 
+  Not using enterprise agreements or volume discounts. 
+  Selecting software based on team preferences without cost considerations. 
+  Missing opportunities to consolidate licenses across accounts. 
+  Managing licenses manually without centralized tooling. 
+  Lacking visibility into organization-wide software utilization. 

 **Benefits of establishing this best practice:** 
+  Reduced overall software and licensing costs by consolidating licenses, eliminating unused entitlements, and replacing commercial software with open-source alternatives where appropriate. 
+  Improved license compliance and risk management through centralized tracking of entitlements, renewal dates, and audit requirements that reduces the likelihood of true-up penalties. 
+  Improved ability to negotiate enterprise agreements because consolidated organization-wide usage data gives procurement teams the position to secure volume discounts and custom terms. 
+  Simplified billing and contributions to cloud spending commitments through consolidated procurement. 
+  Better alignment of software costs with business value by favoring licensing models that scale with usage or outcomes rather than with arbitrary metrics like CPU counts. 
+  Better visibility into software utilization patterns, which surfaces underused licenses and redundant tools so the organization can retire them or reallocate them where they deliver more value. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Effective management of software licensing and third-party agreements at an organizational level requires a complete approach that balances cost optimization with business needs. Evaluate [open-source alternatives](https://aws.amazon.com/what-is/open-source/) that can reduce licensing costs and still provide the required functionality. Where you must use licensed software, prefer licensing that scales with usage or business outcomes. Hardware-bound licenses, such as those tied to CPU count, can raise cost without raising throughput. For example, choosing an Amazon EC2 instance with Linux rather than Windows can reduce cost by 30 to 60 percent depending on instance type, because Windows adds per-hour licensing charges. 

 The value of licensed software needs to be measured against its total cost, including the effects of vendor pricing changes. When a vendor adjusts database licensing terms, the impact on overall workload efficiency can be substantial, and historical pricing announcements from vendors often reveal trends that inform longer-term decisions. Use the [AWS Pricing Calculator](https://calculator.aws/) to compare resource costs across licensing options, such as [Amazon RDS](https://aws.amazon.com/rds/) instances on different database engines. Use [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to review the costs of existing workloads under different licenses. For the license portfolio itself, [AWS License Manager](https://aws.amazon.com/license-manager/) tracks and manages licenses across accounts. 

 Use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to analyze historical utilization patterns and identify opportunities to right-size instances or migrate to different instance families, including Graviton-based instances. For software tied to instance specifications, such as CPU-based licensing, right-sizing reduces both licensing and infrastructure cost. 

 Use [AWS Marketplace](https://aws.amazon.com/marketplace/) as the preferred procurement channel for third-party software. Marketplace consolidates billing on the AWS invoice, offers enterprise pricing and terms, contributes to AWS spending commitments, simplifies procurement and deployment, standardizes terms and conditions, and integrates with license management tools. When evaluating third-party solutions, match the pricing structure to delivered value. For tools that charge a percentage of the AWS bill, confirm they provide value across all charged services. For managed services priced by resource size, confirm that managing larger resources requires more effort. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Standardize software procurement processes:** Establish organization-wide evaluation criteria that weigh open-source alternatives against commercial solutions. Create a standard process for negotiating private pricing and custom terms for [AWS Marketplace](https://aws.amazon.com/marketplace/) purchases, and define guidelines for enterprise agreement negotiations. Consider using [Service Catalog](https://aws.amazon.com/servicecatalog/) to curate a catalog of approved software options that teams can self-service from. Establish regular review cycles for license utilization and costs to catch underused or redundant licenses. 

1.  **Centralize license tracking and compliance:** Deploy [AWS License Manager](https://aws.amazon.com/license-manager/) to track and manage licenses across your organization, and integrate it with [AWS Organizations](https://aws.amazon.com/organizations/) for multi-account visibility. Build a detailed inventory of all commercial licenses, capturing terms, conditions, renewal dates, and audit requirements. Configure license rules to automate compliance checks, and use [AWS Systems Manager](https://aws.amazon.com/systems-manager/) to maintain an inventory of installed software on managed instances. For complex multi-vendor environments, consider supplementing with third-party license management tools. 

1.  **Review existing licenses for optimization opportunities:** Analyze current usage patterns with [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) and [AWS License Manager](https://aws.amazon.com/license-manager/) to identify consolidation opportunities and underutilized licenses. Evaluate whether open-source alternatives can replace commercial software for standard functionality. Review CPU-based licenses specifically for cost impact, because these scale with infrastructure rather than usage. Assess whether [AWS Marketplace](https://aws.amazon.com/marketplace/) license-included options (such as license-included [Amazon RDS](https://aws.amazon.com/rds/) engines) offer better economics than bring-your-own-license models. 

1.  **Adopt AWS Marketplace as the preferred procurement channel:** Implement [Private Marketplace](https://aws.amazon.com/marketplace/features/privatemarketplace) to control which software options are available to your teams. Negotiate [private contracts](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-private-offers.html) through AWS Marketplace to secure custom pricing and terms. Take advantage of flexible payment options including annual, multi-year, and pay-as-you-go models. Consider using AWS Marketplace [professional services](https://docs.aws.amazon.com/marketplace/latest/userguide/proserv-products.html) options when implementation support is needed. 

1.  **Configure financial tracking for software spending:** Set up [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) to support detailed license cost analysis. Create custom [AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html) to isolate software spending from infrastructure costs. Implement [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) with alerts for software license cost thresholds, and turn on [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) to flag unusual spending patterns. Track AWS Marketplace spending contributions to your AWS commitments to maximize discount benefits. 

1.  **Engage AWS OLA for license optimization:** Engage the [AWS Optimization and Licensing Assessment](https://aws.amazon.com/optimization-and-licensing-assessment/) (OLA) to obtain an expert evaluation of your licensing posture across vendors like Microsoft, Oracle, SAP, and VMware, identify right-sizing opportunities based on actual workload requirements, and receive strategies to convert or trade in existing licenses when migrating to AWS. Use the assessment output to make data-driven decisions about which licenses to maintain, convert, or retire, and to negotiate more favorable terms with software vendors. These assessments are typically offered at no additional cost for enterprise customers, and recommendations can reduce licensing costs by up to 30–60 percent. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND06-BP03 Configure billing and cost management tools](fnd06-bp03.md) 
+  [FND06-BP06 Build strategies for commitment discounts and volume-based pricing](fnd06-bp06.md) 

 **Related documents:** 
+  [Open Source at AWS](https://aws.amazon.com/opensource/) 
+  [AWS Open Source Blogs](https://aws.amazon.com/blogs/opensource/) 
+  [Getting started as a buyer using AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-getting-started.html) 
+  [Optimize costs for Microsoft workloads on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/introduction.html) 
+  [Oracle licensing considerations](https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/oracle-licensing-considerations.html) 
+  [Viewing commercial software license recommendations in AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-license-recommendations.html) 
+  [Get started with AWS License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/getting-started.html) 
+  [Enroll in the Enterprise Contract for AWS Marketplace Program](https://pages.awscloud.com/awsmp_ent_contracts.html) 

 **Related tools:** 
+  [AWS Optimization and Licensing Assessment](https://aws.amazon.com/optimization-and-licensing-assessment/) 
+  [Migration Evaluator](https://aws.amazon.com/migration-evaluator/) 

 **Related services:** 
+  [AWS License Manager](https://aws.amazon.com/license-manager/) 
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) 
+  [AWS Pricing Calculator](https://calculator.aws/) 