

# Migration assessments
<a name="transform-app-assessments"></a>

AWS Transform assessments help you evaluate the cost, feasibility, and business value of migrating on-premises infrastructure to AWS. Assessments provide automated right-sizing recommendations, multi-scenario comparison, and interactive refinement through chat.

You can use migration assessments to:
+ Get cost estimates for Amazon RDS for SQL Server, Amazon EC2, Amazon EBS, Amazon S3, and Amazon FSx
+ Receive automated right-sizing recommendations
+ Assess business value and sustainability impact
+ Compare multiple migration scenarios side by side
+ Refine assessments interactively through chat
+ Generate executive presentations and detailed reports

## Prerequisites
<a name="transform-app-assessments-prerequisites"></a>

Before you create a migration assessment, confirm that you have the following:
+ An AWS Transform workspace
+ Inventory data in a supported format, or you can use rough estimation through chat
+ Appropriate permissions to create and run assessments

## How migration assessments work
<a name="transform-app-assessments-how-it-works"></a>

Migration assessments follow a structured workflow that guides you from initial data upload through final deliverable generation.

**To complete a migration assessment**

1. Create a migration assessment job in your AWS Transform workspace.

1. Upload your on-premises inventory data.

1. Review the discovery results that AWS Transform generates from your data.

1. Manage the inventory scope by excluding servers or adjusting groupings.

1. Configure your assessment scenario with pricing and infrastructure assumptions.

1. Run the assessment.

1. Review and refine the results through chat.

After you review results, you can create additional scenarios, compare scenarios, and generate deliverables such as presentations and reports.

## Uploading inventory data
<a name="transform-app-assessments-upload-inventory"></a>

AWS Transform accepts inventory data from multiple sources. The following table lists the supported data formats.


| Data source | Description | 
| --- | --- | 
| AWS Transform Discovery Tool export | Automated server inventory discovered by the AWS Transform discovery tool | 
| RVTools | Exports from VMware environments in ZIP/CSV or Excel format. Both full exports and vInfo-only exports are supported. | 
| CMDB data | Configuration management database exports | 
| Partner discovery tools | Data from AWS partner discovery tools | 
| Migration Evaluator | Quick Insights file from the Migration Evaluator console | 
| MPA format | Migration Portfolio Assessment import file | 
| AWS Transform data template | Microsoft Excel file created from the AWS Transform Assessment Data template | 

AWS Transform automatically identifies the file format during ingestion. The ingestion process validates your data, accepts partial data when some fields are missing, and supports incremental uploads. You can upload additional files at any time to supplement your inventory.

## Reviewing discovery results
<a name="transform-app-assessments-review-discovery"></a>

After AWS Transform processes your inventory data, it generates a discovery summary. The summary includes the following information:
+ Server count by operating system
+ Physical and virtual server breakdown
+ SQL Server detection
+ Storage summaries
+ Data quality warnings

Review the discovery results to confirm that AWS Transform correctly identified your infrastructure before you proceed with the assessment.

## Managing inventory scope
<a name="transform-app-assessments-manage-scope"></a>

After you review the discovery results, you can refine the scope of your assessment. Use the following actions to manage your inventory scope:
+ Query inventory for specific servers or workloads
+ Exclude servers from the assessment scope
+ Review server groupings and application dependencies
+ Identify SQL Server workloads for specialized assessment

## Configuring assessment scenarios
<a name="transform-app-assessments-configure-scenarios"></a>

Before you run an assessment, configure the assumptions that AWS Transform uses to generate recommendations. You can modify these assumptions at any time and run new scenarios with different configurations.

The following table lists the available assumption categories.


| Assumption | Description | 
| --- | --- | 
| Pricing model | Database Savings Plans (for Amazon RDS for SQL Server), On-Demand, or Reserved Instances | 
| Target AWS Region | The AWS Region where you plan to host migrated workloads | 
| Instance type exclusions | Amazon EC2 instance families or types to exclude from recommendations | 
| Amazon EBS configuration | Volume type and performance settings for storage | 
| SQL Server licensing | Bring Your Own Media (BYOM) or License Included (LI) for Amazon RDS for SQL Server; License Included (LI) or Bring Your Own License (BYOL) for SQL Server on EC2 | 

## Assessment capabilities
<a name="transform-app-assessments-capabilities"></a>

AWS Transform assessments cover multiple dimensions of your migration. The following sections describe each assessment capability.

### Amazon EC2 right-sizing
<a name="transform-app-assessments-capabilities-ec2"></a>

AWS Transform analyzes your on-premises server specifications and recommends appropriately sized Amazon EC2 instances. The recommendations account for CPU, memory, and performance requirements.

### Amazon EBS storage
<a name="transform-app-assessments-capabilities-ebs"></a>

AWS Transform recommends Amazon EBS volume types and configurations based on your current storage usage and performance requirements.

### Amazon FSx
<a name="transform-app-assessments-capabilities-fsx"></a>

AWS Transform evaluates file storage workloads and provides recommendations for Amazon FSx migration, including cost estimates for supported Amazon FSx file system types.

### Amazon RDS for SQL Server
<a name="transform-app-assessments-capabilities-rds-sql"></a>

AWS Transform assesses the cost of migrating on-premises SQL Server databases to Amazon RDS for SQL Server. Using AI-powered agents, AWS Transform analyzes your on-premises SQL Server environment and delivers a complete migration business case in minutes, with compute and memory recommendations matched to your workload requirements so you avoid over-provisioning and only pay for what you need.

The RDS for SQL Server assessment includes the following capabilities:
+ Bring Your Own Media (BYOM) licensing, allowing you to use your existing SQL Server licenses
+ License Included (LI) licensing options
+ Cost optimization using Database Savings Plans, which offer up to 20% savings compared to On-Demand pricing
+ Eligibility assessment for the AWS Migration Acceleration Program (MAP), which provides credits and support to offset migration costs

You can start your RDS for SQL Server assessment with any supported data format, including RVTools exports, Configuration management database (CMDB) data, exports from the AWS Transform discovery tool, and other third-party discovery tools. Create what-if scenarios to compare multiple cost models with customized assumptions including region, resource utilization, and pricing terms.

Example prompts:
+ "Estimate the cost of migrating my SQL Server databases to RDS for SQL Server"
+ "Compare BYOM vs License Included pricing for RDS for SQL Server"
+ "Show me Database Savings Plans options for my RDS workloads"

### Amazon EC2 SQL Server
<a name="transform-app-assessments-capabilities-sql"></a>

AWS Transform assesses SQL Server workloads and provides recommendations for running SQL Server on Amazon EC2, including licensing analysis and dedicated host mappings.

### On-premises pricing
<a name="transform-app-assessments-capabilities-onprem-pricing"></a>

AWS Transform estimates your current on-premises costs to provide a baseline for comparison with AWS pricing. You can make overall cost adjustments through chat. On-premises cost adjustments are reflected in the PDF report and chat responses, but not in the PPTX export.

Example prompts:
+ "Update the on-premises server cost to $500 per server per month"
+ "Add $50,000 annual data center facility costs"

### Sustainability
<a name="transform-app-assessments-capabilities-sustainability"></a>

AWS Transform estimates the carbon footprint reduction that results from migrating to AWS. You can explore sustainability metrics through chat.

Try prompts such as:
+ "Show me the estimated carbon reduction for this migration"
+ "What is the energy efficiency improvement for my workloads on AWS?"

### Business value assessment
<a name="transform-app-assessments-capabilities-business-value"></a>

AWS Transform evaluates the broader business value of migration beyond infrastructure cost savings. The assessment covers staff productivity, resilience, and business agility.

Here are some example prompts:
+ "Estimate staff productivity gains from migrating to AWS"
+ "What resilience improvements can I expect after migration?"
+ "Show me the business agility benefits of this migration"

### Network costs
<a name="transform-app-assessments-capabilities-network"></a>

AWS Transform estimates network-related costs for your migration, including data transfer and connectivity requirements.

### Support costs
<a name="transform-app-assessments-capabilities-support"></a>

AWS Transform includes AWS Support plan costs in the assessment based on your selected support tier.

### End user computing
<a name="transform-app-assessments-capabilities-euc"></a>

AWS Transform assesses end user computing workloads and provides recommendations for AWS end user computing services.

## Using chat-based assessments
<a name="transform-app-assessments-chat"></a>

You can interact with AWS Transform through chat to create and refine assessments. Chat supports three modes of interaction.

You can iteratively refine your assessment by continuing the conversation. AWS Transform maintains context across messages and updates the assessment results based on your input.

### Rough estimation with limited data
<a name="transform-app-assessments-chat-rough-estimation"></a>

You can get a rough cost estimate by describing your environment in chat without uploading detailed inventory files. Rough estimation is a standalone feature and cannot be combined with uploaded inventory data or data enrichment through chat.

You can use prompts like these:
+ "I have 200 Windows servers and 150 Linux servers, estimate my AWS costs"
+ "Give me a rough estimate for migrating 500 VMs to AWS"
+ "Estimate costs for 50 servers with an average of 8 CPUs and 32 GB RAM"

### Adding inventory through chat
<a name="transform-app-assessments-chat-add-inventory"></a>

You can provide inventory details directly through chat to supplement or replace uploaded files.

Use prompts like the following:
+ "Include a database server running Oracle on 4 CPUs with 128 GB RAM"
+ "Add 20 web servers running Linux with 4 CPUs and 16 GB RAM"

### Modifying costs and adding services
<a name="transform-app-assessments-chat-modify-costs"></a>

You can adjust on-premises costs and add AWS services to your assessment through chat.

Example prompts for on-premises adjustments:
+ "Increase on-premises costs by 15% to account for upcoming hardware refresh"
+ "Add $100,000 annual maintenance costs to the on-premises baseline"

You can also add rough cost estimates for AWS services that are not fully supported by AWS Transform assessments. This provides a more complete analysis, but these estimates are less accurate than the automated recommendations.
+ "Add AWS Backup costs for all migrated servers"
+ "Include Amazon CloudWatch monitoring costs in the estimate"
+ "Add AWS Direct Connect costs for a 10 Gbps connection"

## Comparing scenarios
<a name="transform-app-assessments-compare-scenarios"></a>

You can create multiple assessment scenarios with different assumptions and compare them to identify the optimal migration strategy.

### Creating scenarios
<a name="transform-app-assessments-compare-scenarios-create"></a>

Try prompts such as:
+ "Create a BYOM scenario for migrating SQL Server databases to RDS for SQL Server"
+ "Create a scenario with Database Savings Plans for RDS for SQL Server"
+ "Create a LI scenario for all SQL Server workloads on EC2"
+ "Create a scenario with all workloads in us-west-2"

### Running comparisons
<a name="transform-app-assessments-compare-scenarios-run"></a>

Here are some example prompts:
+ "Show me a cost comparison across all scenarios"
+ "Which scenario has the lowest total cost of ownership?"

### What-if analysis
<a name="transform-app-assessments-compare-scenarios-whatif"></a>

Model the impact of specific changes without creating a full new scenario.

Example prompts:
+ "What if I move my SQL Server workloads to RDS for SQL Server instead of EC2?"
+ "What is the cost difference between BYOM and License Included for RDS for SQL Server?"
+ "What if I exclude the 50 smallest servers from the migration?"
+ "What if I only use storage optimized instances?"
+ "What is the impact of moving from gp3 to io2 volumes?"

## Generating deliverables
<a name="transform-app-assessments-deliverables"></a>

After you complete your assessment, you can generate deliverables in multiple formats. The following table describes the available output formats.


| Format | Description | Customization | 
| --- | --- | --- | 
| PPTX (PowerPoint) | Executive presentation with summary findings and recommendations | Fixed structure | 
| XLSX (Excel) | Detailed data export with server-level recommendations and cost breakdowns | Fixed structure | 
| PDF | Report document | Customizable through chat | 

## Related topics
<a name="transform-app-assessments-related"></a>
+ [Getting started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html)
+ [Custom jobs](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-custom.html)
+ [Discovery tool](https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool.html)