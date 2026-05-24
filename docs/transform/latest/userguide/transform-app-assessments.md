# Migration assessments

AWS Transform assessments help you evaluate the cost, feasibility, and business value of
migrating on-premises infrastructure to AWS. Assessments provide automated right-sizing
recommendations, multi-scenario comparison, and interactive refinement through chat.

You can use migration assessments to:

- Get cost estimates for Amazon EC2, Amazon EBS, Amazon S3, and Amazon FSx
- Receive automated right-sizing recommendations
- Assess business value and sustainability impact
- Compare multiple migration scenarios side by side
- Refine assessments interactively through chat
- Generate executive presentations and detailed reports

## Prerequisites

Before you create a migration assessment, confirm that you have the following:

- An AWS Transform workspace
- Inventory data in a supported format, or you can use rough estimation
  through chat
- Appropriate permissions to create and run assessments

## How migration assessments work

Migration assessments follow a structured workflow that guides you from initial data
upload through final deliverable generation.

###### To complete a migration assessment

1. Create a migration assessment job in your AWS Transform workspace.
2. Upload your on-premises inventory data.
3. Review the discovery results that AWS Transform generates from your data.
4. Manage the inventory scope by excluding servers or adjusting groupings.
5. Configure your assessment scenario with pricing and infrastructure
   assumptions.
6. Run the assessment.
7. Review and refine the results through chat.

After you review results, you can create additional scenarios, compare scenarios, and
generate deliverables such as presentations and reports.

## Uploading inventory data

AWS Transform accepts inventory data from multiple sources. The following table lists the
supported data formats.

| Data source                         | Description                                                                                                             |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| AWS Transform Discovery Tool export | Automated server inventory discovered by the AWS Transform discovery<br>tool                                            |
| RVTools                             | Exports from VMware environments in ZIP/CSV or Excel format. Both<br>full exports and vInfo-only exports are supported. |
| CMDB data                           | Configuration management database exports                                                                               |
| Partner discovery tools             | Data from AWS partner discovery tools                                                                                   |
| Migration Evaluator                 | Quick Insights file from the Migration Evaluator console                                                                |
| MPA format                          | Migration Portfolio Assessment import file                                                                              |
| AWS Transform data template         | Microsoft Excel file created from the AWS Transform Assessment Data<br>template                                         |

AWS Transform automatically identifies the file format during ingestion. The ingestion
process validates your data, accepts partial data when some fields are missing, and
supports incremental uploads. You can upload additional files at any time to supplement
your inventory.

## Reviewing discovery results

After AWS Transform processes your inventory data, it generates a discovery summary. The
summary includes the following information:

- Server count by operating system
- Physical and virtual server breakdown
- SQL Server detection
- Storage summaries
- Data quality warnings

Review the discovery results to confirm that AWS Transform correctly identified your
infrastructure before you proceed with the assessment.

## Managing inventory scope

After you review the discovery results, you can refine the scope of your assessment.
Use the following actions to manage your inventory scope:

- Query inventory for specific servers or workloads
- Exclude servers from the assessment scope
- Review server groupings and application dependencies
- Identify SQL Server workloads for specialized assessment

## Configuring assessment scenarios

Before you run an assessment, configure the assumptions that AWS Transform uses to
generate recommendations. You can modify these assumptions at any time and run new
scenarios with different configurations.

The following table lists the available assumption categories.

| Assumption               | Description                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------ |
| Pricing model            | On-Demand or Reserved Instances                                                            |
| Target AWS Region        | The AWS Region where you plan to host migrated workloads                                   |
| Instance type exclusions | Amazon EC2 instance families or types to exclude from<br>recommendations                   |
| Amazon EBS configuration | Volume type and performance settings for storage                                           |
| SQL Server licensing     | License Included (LI) or Bring Your Own License (BYOL) options for<br>SQL Server workloads |

## Assessment capabilities

AWS Transform assessments cover multiple dimensions of your migration. The following
sections describe each assessment capability.

### Amazon EC2 right-sizing

AWS Transform analyzes your on-premises server specifications and recommends
appropriately sized Amazon EC2 instances. The recommendations account for CPU, memory,
and performance requirements.

### Amazon EBS storage

AWS Transform recommends Amazon EBS volume types and configurations based on your current
storage usage and performance requirements.

### Amazon FSx

AWS Transform evaluates file storage workloads and provides recommendations for
Amazon FSx migration, including cost estimates for supported Amazon FSx file system
types.

### Amazon EC2 SQL Server

AWS Transform assesses SQL Server workloads and provides recommendations for running
SQL Server on Amazon EC2, including licensing analysis and dedicated host mappings.

### On-premises pricing

AWS Transform estimates your current on-premises costs to provide a baseline for
comparison with AWS pricing. You can make overall cost adjustments through chat.
On-premises cost adjustments are reflected in the PDF report and chat responses, but
not in the PPTX export.

Example prompts:

- "Update the on-premises server cost to $500 per server per month"
- "Add $50,000 annual data center facility costs"

### Sustainability

AWS Transform estimates the carbon footprint reduction that results from migrating to
AWS. You can explore sustainability metrics through chat.

Try prompts such as:

- "Show me the estimated carbon reduction for this migration"
- "What is the energy efficiency improvement for my workloads on
  AWS?"

### Business value assessment

AWS Transform evaluates the broader business value of migration beyond infrastructure
cost savings. The assessment covers staff productivity, resilience, and business
agility.

Here are some example prompts:

- "Estimate staff productivity gains from migrating to AWS"
- "What resilience improvements can I expect after migration?"
- "Show me the business agility benefits of this migration"

### Network costs

AWS Transform estimates network-related costs for your migration, including data
transfer and connectivity requirements.

### Support costs

AWS Transform includes AWS Support plan costs in the assessment based on your
selected support tier.

### End user computing

AWS Transform assesses end user computing workloads and provides recommendations for
AWS end user computing services.

## Using chat-based assessments

You can interact with AWS Transform through chat to create and refine assessments. Chat
supports three modes of interaction.

You can iteratively refine your assessment by continuing the conversation. AWS Transform
maintains context across messages and updates the assessment results based on your
input.

### Rough estimation with limited data

You can get a rough cost estimate by describing your environment in chat without
uploading detailed inventory files. Rough estimation is a standalone feature and
cannot be combined with uploaded inventory data or data enrichment through
chat.

You can use prompts like these:

- "I have 200 Windows servers and 150 Linux servers, estimate my AWS
  costs"
- "Give me a rough estimate for migrating 500 VMs to AWS"
- "Estimate costs for 50 servers with an average of 8 CPUs and 32 GB
  RAM"

### Adding inventory through chat

You can provide inventory details directly through chat to supplement or replace
uploaded files.

Use prompts like the following:

- "Include a database server running Oracle on 4 CPUs with 128 GB
  RAM"
- "Add 20 web servers running Linux with 4 CPUs and 16 GB RAM"

### Modifying costs and adding services

You can adjust on-premises costs and add AWS services to your assessment through
chat.

Example prompts for on-premises adjustments:

- "Increase on-premises costs by 15% to account for upcoming hardware
  refresh"
- "Add $100,000 annual maintenance costs to the on-premises
  baseline"

You can also add rough cost estimates for AWS services that are not fully
supported by AWS Transform assessments. This provides a more complete analysis, but
these estimates are less accurate than the automated recommendations.

- "Add AWS Backup costs for all migrated servers"
- "Include Amazon CloudWatch monitoring costs in the estimate"
- "Add AWS Direct Connect costs for a 10 Gbps connection"

## Comparing scenarios

You can create multiple assessment scenarios with different assumptions and compare
them to identify the optimal migration strategy.

### Creating scenarios

Try prompts such as:

- "Create a scenario with all workloads in us-west-2"
- "Create a LI scenario for all SQL Server workloads"

### Running comparisons

Here are some example prompts:

- "Show me a cost comparison across all scenarios"
- "Which scenario has the lowest total cost of ownership?"

### What-if analysis

Model the impact of specific changes without creating a full new scenario.

Example prompts:

- "What if I exclude the 50 smallest servers from the migration?"
- "What if I only use storage optimized instances"
- "What is the impact of moving from gp3 to io2 volumes?"

## Generating deliverables

After you complete your assessment, you can generate deliverables in multiple formats.
The following table describes the available output formats.

| Format            | Description                                                                   | Customization             |
| ----------------- | ----------------------------------------------------------------------------- | ------------------------- |
| PPTX (PowerPoint) | Executive presentation with summary findings and<br>recommendations           | Fixed structure           |
| XLSX (Excel)      | Detailed data export with server-level recommendations and cost<br>breakdowns | Fixed structure           |
| PDF               | Report document                                                               | Customizable through chat |

## Related topics

- [Getting
  started](getting-started.md "getting-started.md")
- [Custom
  jobs](transform-app-custom.md "transform-app-custom.md")
- [Discovery
  tool](discovery-tool.md "discovery-tool.md")
