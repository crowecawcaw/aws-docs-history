# CUDOS, CID, KPI

## Feedback & Support

Follow [Feedback & Support](feedback-support.md "feedback-support.md") guide

## Introduction

In this section we provide a description of
[CUDOS Dashboard](#foundational-cudos-dashboard "#foundational-cudos-dashboard"), [Cost Intelligence Dashboard (CID)](#foundational-cid-dashboard "#foundational-cid-dashboard") and [KPI Dashboard](#foundational-kpi-dashboard "#foundational-kpi-dashboard")
which use data exclusively from the
[AWS
Cost and Usage Report.](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/ "https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/")

All these dashboards are based on the AWS Cost & Usage Report (CUR) that
contains the most comprehensive set of AWS cost and usage data
available, including additional metadata about AWS services, pricing,
Reserved Instances, and Savings Plans. The CUR itemizes usage at the
account or Organization level by product code, usage type and operation.
These costs can be further organized by enabling Cost Allocation tags
and Cost Categories.

These dashboards support both the newer **CUR 2.0** data export (recommended)
and the **legacy CUR**. We recommend CUR 2.0, which is delivered through
[AWS Data Exports](data-exports.md "data-exports.md") and provides additional columns and taxonomy
sources used across the dashboards.

![Recommended Deployment Architecture](images/basic_deployment_arch.png)

1. [AWS Data
   Exports](https://aws.amazon.com/aws-cost-management/aws-data-exports/ "https://aws.amazon.com/aws-cost-management/aws-data-exports/") delivers daily the Cost & Usage Report (CUR2) directly to an
   [Amazon S3 Bucket](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") in the Data Collection Account.
2. [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/") allows querying data
   directly from the S3 bucket using an [AWS
   Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/") table schema definition.
3. [Amazon Quick](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/") creates datasets
   from [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/"), refreshes daily and
   caches in
   [SPICE](../../../quicksight/latest/user/spice.md "../../../quicksight/latest/user/spice.md")(Super-fast,
   Parallel, In-memory Calculation Engine) for
   [Amazon Quick](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/")
4. User Teams (Executives, FinOps, Engineers) can access Cloud
   Intelligence Dashboards in [Amazon
   Quick](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/"). Access is secured through [AWS
   IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/"), IIC ([AWS IAM Identity
   Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/"), formerly SSO), and optional
   [Row
   Level Security](https://catalog.workshops.aws/awscid/en-US/customizations/row-level-security "https://catalog.workshops.aws/awscid/en-US/customizations/row-level-security").

If you do not have access to the Management account, you can also deploy
CID for a subset of Linked Accounts.

## CUDOS Dashboard

The CUDOS (Cost and Usage Dashboard Operations Solution) Dashboard is an
in-depth, granular, and recommendation-driven dashboard that helps you dive
deep into cost and usage and fine-tune efficiency. It provides high-level
executive summaries with the ability to drill down to resource-level
granularity, so executives, directors, FinOps practitioners, Product Owners,
and Engineering teams — across the CIO, CTO, and DevOps/IT organizations — can
act on auto-generated recommendations out of the box.

Built on fast Amazon Quick SPICE datasets, CUDOS organizes cost and usage
across dedicated tabs for Executive summaries, Compute, Databases, Storage,
AI/ML, Analytics, Security, Data Transfer, and more.

**Highlights of the CUDOS Dashboard:**

- **Executive summaries** — Track invoiced and amortized spend, month-over-month,
  weekly, and daily trends, and savings and discounts (SP, RI, Spot, Credits,
  Refunds), with grouping by FOCUS Service Categories.
- **Actionable recommendations and areas of focus** — Surface auto-generated cost
  optimization opportunities, such as top On-Demand instances and rightsizing
  candidates, that your teams can act on out of the box.
- **Idle resource tracking** — Identify and eliminate waste by surfacing idle
  resources across your environment, including idle Elastic Load Balancers
  (ELBs), NAT Gateways, VPC endpoints, Amazon Kinesis Data Streams, and idle Kiro
  users.
- **RI/SP commitment tracking** — Monitor Reserved Instance and Savings Plans
  coverage, utilization, and unused commitments across Amazon EC2, databases, and
  more.
- **Deep service coverage** — Dive into Compute, Databases (including DynamoDB
  elasticity and reservations), Amazon S3, Storage & Backup, Data Transfer &
  Networking, and Security (AWS Shield, WAF, Amazon Cognito, GuardDuty).
- **AI/ML cost visibility and optimization** — Analyze spend for Amazon Bedrock
  with cost-per-million-tokens tracking by model and IAM Principal Tag, alongside
  Amazon Q, SageMaker, and Kiro and AWS DevOps Agent usage — with insights to
  surface optimization opportunities such as idle Kiro users and high-cost
  models.
- **Resource-level granularity** — View resource-level detail such as hourly AWS
  Lambda costs and individual Amazon S3 bucket costs with advanced usage
  categorization (by operation and usage type group), for the last 30 days.
- **Built-in Taxonomy Explorer** — Group and filter cost and usage across tags and
  account-level mappings added through the [Add Organizational
  Taxonomy](add-org-taxonomy.md "add-org-taxonomy.md") capability.

### Demo Dashboard

Explore a [sample
CUDOS Dashboard](https://cid.workshops.aws.dev/demo?dashboard=cudos "https://cid.workshops.aws.dev/demo?dashboard=cudos")

![CUDOS Dashboard Screenshot](images/CUDOS_dashboard.png)

### Deploy

Follow [deployment guide](deployment-in-global-regions.md "deployment-in-global-regions.md")

### Learn more

- [What’s New in CUDOS
  versions 5.1 to 5.3](https://www.youtube.com/watch?v=3LuKzbFxuz8 "https://www.youtube.com/watch?v=3LuKzbFxuz8")
- [What’s new in CUDOS
  Dashboard v 4.77](https://www.youtube.com/watch?v=5IWAoKujOqo "https://www.youtube.com/watch?v=5IWAoKujOqo")
- [CUDOS
  Insights Learning Series on YouTube](https://www.youtube.com/watch?v=2N24ERSwPE4&list=PLevHThZeBjf85JyGgZGep0ib9eE-53A2T "https://www.youtube.com/watch?v=2N24ERSwPE4&list=PLevHThZeBjf85JyGgZGep0ib9eE-53A2T")

### Changelog

- [Changelog](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md")

### Authors

- Yuriy Prykhodko, AWS Principal Technical Account Manager
- Timur Tulyaganov, Ex-Amazonian

### Contributors

- Alee Whitman, Principal Solutions Architect
- Iakov Gan, Ex-Amazonian
- Judith Lehner, Senior Technical Account Manager
- Udi Dahan, Senior Technical Account Manager
- Mylen Rath, Senior Technical Account Manager
- Christopher Morris, Senior Technical Account Manager
- Xianshu Zeng, Senior FinOps Commercial Architect
- Oleksandr Moskalenko, Ex-Amazonian
- Natalia Cummings, Senior FinOps Commercial Architect
- Adam Richter, Senior Optimization Solutions Architect
- Sabith Venkitachalapathy, Senior Storage Specialist SA
- Brenno Passanha, Senior Technical Account Manager

## Cost Intelligence Dashboard (CID)

[Watch
10min video overview of CID dashboard](https://d3h9zoi3eqyz7s.cloudfront.net/Cost/Videos/DashboardCostIntelligence.mp4 "https://d3h9zoi3eqyz7s.cloudfront.net/Cost/Videos/DashboardCostIntelligence.mp4")

The Cost Intelligence Dashboard is a customizable and accessible
dashboard to help create the foundation of your own cost management and
optimization (FinOps) tool. Executives, directors, and other individuals
within the CFO’s line of business or who manage cloud financials for an
organization will find the Cloud Intelligence Dashboard easy to use and
relevant to their use cases. Little to no technical knowledge or
understanding of AWS Services is required. Out-of-the-box benefits of
the CID include (but are not limited to):

- Create chargeback or showback reports for internal business units,
  accounts, or cost centers.
- Track how Savings Plans (SP), Reserved Instances (RI), and Spot
  Instance usage has impacted your unit metrics such as your average
  hourly cost of Amazon EC2.
- Keep track of which accounts or internal business units receive
  savings and when RIs and SPs expire.

### Demo Dashboard

Explore a [sample Cost
Intelligence Dashboard](https://cid.workshops.aws.dev/demo?dashboard=cid "https://cid.workshops.aws.dev/demo?dashboard=cid")

### Deploy

Follow [deployment guide](deployment-in-global-regions.md "deployment-in-global-regions.md")

### Authors

- Alee Whitman, Principal Solutions Architect

### Contributors

- Aaron Edell, Head of Accelerators, AWS
- Aidin Khosrowshahi, AWS Sr. Technical Account Manager
- Yuriy Prykhodko, AWS Principal Technical Account Manager
- Arun Santhosh, Principal Specialist SA (Amazon Quick)
- Kareem Syed-Mohammed, Senior Product Manager - Technical (Amazon Quick)
- Timur Tulyaganov, Ex-Amazonian

## KPI Dashboard

The KPI and Modernization Dashboard helps your organization combine
DevOps and IT infrastructure with Finance and the C-Suite to grow more
efficiently and effectively on AWS. This dashboard lets you set and
track modernization and optimization goals such as percent OnDemand,
Spot adoption, and Graviton usage. By enabling every line of business to
create and track usage goals, and your cloud center of excellence to
make recommendations organization-wide, you can grow more efficiently
and innovate more quickly on AWS. Out-of-the-box benefits of the KPI
dashboard include (but are not limited to):

- Track percent on-demand across all your teams.
- See potential cost savings by meeting certain KPIs and goals for your
  organization.
- Quickly locate cost-optimization opportunities such as infrequently
  used S3 buckets, old EBS snapshots, and Graviton eligible instance
  usage.

### Demo Dashboard

Explore a [sample KPI
Dashboard](https://cid.workshops.aws.dev/demo?dashboard=kpi "https://cid.workshops.aws.dev/demo?dashboard=kpi")

### Deploy

Follow [deployment guide](deployment-in-global-regions.md "deployment-in-global-regions.md")

### Learn more

- [What’s new in KPI
  Dashboard](https://www.youtube.com/watch?v=1yDuYqNbcr4 "https://www.youtube.com/watch?v=1yDuYqNbcr4")

### Authors

- Alee Whitman, Principal Solutions Architect

### Contributors

- Aaron Edell, Head of Accelerators, AWS
- Alex Head, Sr. Manager, AWS OPTICS
- Georgios Rozakis, AWS Sr. Technical Account Manager
- Oleksandr Moskalenko, Ex-Amazonian
- Timur Tulyaganov, Ex-Amazonian
- Yash Bindlish, AWS Enterprise Support Manager
- Yuriy Prykhodko, AWS Principal Technical Account Manager
- Anjali Dhanerwal, AWS Senior Technical Account Manager

## Time to complete

If using automation steps, setup should take approximately 15-30 minutes
to complete. Please note that the first data refresh of Cost and Usage
Report may take 24 hours to arrive.

## Steps

- [Deployment in Global Regions](deployment-in-global-regions.md "deployment-in-global-regions.md")
- [Column Definitions](column-definitions.md "column-definitions.md")
- [Add Account Names ( Optional )](add-account-names.md "add-account-names.md")
- [Migration to CUR 2.0](migration-to-cur.md "migration-to-cur.md")
- [Deployment In China](deployment-in-china.md "deployment-in-china.md")

###### Note

These dashboards and their content: (a) are for informational purposes only, (b) represent current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS content, products or services are provided “as is” without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers.
