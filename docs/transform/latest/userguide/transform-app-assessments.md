

# Migration assessments
<a name="transform-app-assessments"></a>

AWS Transform assessments help you evaluate the cost, feasibility, and business value of migrating on-premises infrastructure to AWS. Using agentic AI, AWS Transform generates a data-driven total cost of ownership (TCO) business case in minutes from a server inventory, finding the best-fit AWS services for your workloads and producing pricing options, licensing analysis, and actionable next steps. From there, you refine the business case through natural language chat—adding missing inventory, adjusting on-premises costs, modeling alternative AWS services, changing assumptions, and exploring what-if scenarios—without re-running the full assessment.

You can use migration assessments to:
+ Get cost estimates for compute, databases, storage, analytics, and end user computing workloads on AWS
+ Receive automated right-sizing recommendations
+ Assess business value and sustainability impact
+ Compare multiple migration scenarios side by side
+ Refine assessments interactively through chat
+ Generate executive presentations and detailed reports

Assessment results can also help you understand whether you qualify for AWS programs and incentives, such as the AWS Migration Acceleration Program (MAP).

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

AWS Transform accepts inventory data from a broad set of sources, so you can work with the data you already have rather than running a new collection. The following table lists the supported data formats.


| Data source | Description | 
| --- | --- | 
| AWS Transform Discovery Tool export | Automated server inventory discovered by the AWS Transform discovery tool | 
| RVTools | Exports from VMware environments in ZIP/CSV or Excel format. Both full exports and vInfo-only exports are supported. | 
| CMDB data | Configuration management database exports | 
| Migration Evaluator | Quick Insights file from the AWS Migration Evaluator console | 
| MPA format | AWS Migration Portfolio Assessment (MPA) import file | 
| NetApp Data Infrastructure Insights (DII) | Exports from NetApp Data Infrastructure Insights | 
| Partner discovery tools | Exports from AWS partner and third-party discovery tools, including ModelizeIT, Cloudamize, Matilda Cloud, and Device42 | 
| AWS Transform data template | Microsoft Excel file created from the AWS Transform Assessment Data template | 

AWS Transform automatically identifies the file format during ingestion. The ingestion process validates your data, accepts partial data when some fields are missing, and supports incremental uploads. You can upload additional files at any time to supplement your inventory.

## Reviewing discovery results
<a name="transform-app-assessments-review-discovery"></a>

After AWS Transform processes your inventory data, it generates a discovery summary. The summary includes the following information:
+ Server count by operating system
+ Physical and virtual server breakdown
+ SQL Server detection
+ Apache Kafka cluster detection
+ Storage summaries
+ Data quality warnings

Review the discovery results to confirm that AWS Transform correctly identified your infrastructure before you proceed with the assessment.

## Managing inventory scope
<a name="transform-app-assessments-manage-scope"></a>

After you review the discovery results, you can refine the scope of your assessment. Use the following actions to manage your inventory scope:
+ Query inventory for specific servers or workloads
+ Exclude servers from the assessment scope
+ Review server groupings and application dependencies
+ Identify SQL Server and Apache Kafka workloads for specialized assessment

## Configuring assessment scenarios
<a name="transform-app-assessments-configure-scenarios"></a>

Before you run an assessment, configure the assumptions that AWS Transform uses to generate recommendations. You can modify these assumptions at any time and run new scenarios with different configurations.

The following table lists the available assumption categories.


| Assumption | Description | 
| --- | --- | 
| Pricing model | On-Demand, Reserved Instances, or Savings Plans; Database Savings Plans for Amazon RDS for SQL Server | 
| Target AWS Region | The AWS Region where you plan to host migrated workloads | 
| Utilization and right-sizing | The performance tier and utilization assumptions used to right-size Amazon EC2 instances | 
| Processor architecture | Whether recommendations use x86, AWS Graviton, or either architecture | 
| Tenancy | Shared, dedicated, or mixed tenancy for Amazon EC2 instances | 
| Instance type exclusions | Amazon EC2 instance families or types to exclude from recommendations | 
| Amazon EBS configuration | Volume type and performance settings for storage | 
| SQL Server licensing | Bring Your Own Media (BYOM) or License Included (LI) for Amazon RDS for SQL Server; License Included (LI) or Bring Your Own License (BYOL) for SQL Server on EC2 | 

## Assessment capabilities
<a name="transform-app-assessments-capabilities"></a>

AWS Transform assessments cover the workload categories that matter most in a typical enterprise migration. The following topics describe each assessment capability in detail.
+ [Compute assessments](transform-app-assessments-compute.md)—best-fit, lowest-cost Amazon EC2 instance recommendations, including AWS Graviton, Dedicated Hosts, and multiple pricing models.
+ [Database assessments](transform-app-assessments-databases.md)—Microsoft SQL Server on Amazon RDS for SQL Server and on Amazon EC2, with licensing analysis and edition recommendations.
+ [Storage assessments](transform-app-assessments-storage.md)—block, object, and file storage across Amazon EBS, Amazon S3, and Amazon FSx for NetApp ONTAP.
+ [Analytics assessments](transform-app-assessments-analytics.md)—self-managed Apache Kafka clusters assessed for Amazon MSK Express.
+ [Business value assessments](transform-app-assessments-business-value.md)—quantified business value across the AWS Cloud Value Framework pillars.
+ [Additional cost components](transform-app-assessments-cost-components.md)—on-premises pricing, network, support, and end user computing cost components.

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
+ "How much would running 2000 large Linux servers with roughly 500 TB of SAN storage cost? About 300 run MySQL and about 100 run Oracle."

### Adding inventory through chat
<a name="transform-app-assessments-chat-add-inventory"></a>

You can provide inventory details directly through chat to supplement or replace uploaded files. When a server is missing from an export, you can add it in chat rather than regenerating and re-uploading the file.

Use prompts like the following:
+ "There is a server missing from my inventory. It is called prod-server5, it runs SQL Server Standard Edition on Windows, and has 128 CPU cores and 256 GB of RAM."
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
+ "Migrate servers svr1, svr2, and svr3 to Amazon Connect. Remove them from EC2 and add $10,000 a month in Amazon Connect costs."

## Comparing scenarios
<a name="transform-app-assessments-compare-scenarios"></a>

You can create multiple assessment scenarios with different assumptions and compare them to identify the optimal migration strategy.

### Creating scenarios
<a name="transform-app-assessments-compare-scenarios-create"></a>

Try prompts such as:
+ "Create a BYOM scenario for migrating SQL Server databases to RDS for SQL Server"
+ "Create a scenario with Database Savings Plans for RDS for SQL Server"
+ "Create a scenario with AWS Graviton instances where supported"
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
| PDF | Report document with sections for compute, storage, licensing, and cost comparisons | Customizable through chat | 

## Related topics
<a name="transform-app-assessments-related"></a>
+ [Getting started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html)
+ [Custom jobs](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-custom.html)
+ [Discovery tool](https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool.html)