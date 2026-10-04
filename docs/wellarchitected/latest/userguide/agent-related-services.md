

AWS Well-Architected Agent is in preview release and is subject to change.

# Related services
<a name="agent-related-services"></a>

AWS Well-Architected Agent integrates with the following AWS services:


| Service | Relationship | 
| --- | --- | 
| AWS Trusted Advisor | AWS WA Agent ingests Trusted Advisor findings as baseline signals. AWS WA Agent adds personalization, cross-pillar analysis, and automation-ready remediation on top of these findings. | 
| AWS Compute Optimizer | AWS WA Agent uses AWS Compute Optimizer rightsizing signals for Amazon EC2, Lambda, and Amazon RDS. AWS WA Agent contextualizes these within your business goals and application topology. | 
| AWS Security Hub CSPM | AWS WA Agent ingests Security Hub CSPM findings. AWS WA Agent adds goal-aligned prioritization and cross-pillar trade-off analysis. | 
| AWS Resilience Hub | AWS WA Agent uses resilience assessment data. AWS WA Agent incorporates your RTO/RPO targets and provides cross-pillar impact analysis. | 
| AWS Cost Optimization Hub | AWS WA Agent uses cost optimization signals. AWS WA Agent ranks cost recommendations against your stated business goals. | 
| AWS Cost Explorer | AWS WA Agent uses Cost Explorer data for accurate, resource-level cost attribution in cost optimization recommendations. Without Cost Explorer enabled, AWS WA Agent estimates costs from public AWS pricing. For more information about enabling Cost Explorer, see [Getting started with Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-getting-started.html). | 
| AWS Well-Architected Tool | AWS WA Agent launches within the AWS Well-Architected console. AWS WA Tool provides manual review workflows. AWS WA Agent provides automated, AI-powered analysis. Both can be used simultaneously. | 
| AWS Systems Manager | AWS WA Agent delivers remediation through SSM Runbooks for automated execution of recommendations. | 