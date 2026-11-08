

# Database Resilience, Operations, and Insights (DROID) Dashboard
<a name="droid-dashboard"></a>

## Introduction
<a name="introduction"></a>

The Database Resilience, Operations, and Insights (DROID) Dashboard provides comprehensive visibility into Amazon RDS and Amazon Aurora fleet health. It covers engine version status, end-of-support exposure, security and resiliency configuration, backup coverage, and cost. This dashboard combines AWS Cost and Usage Report (CUR) data with inventory and reference data collected by the Cloud Intelligence Dashboards Data Collection framework to deliver actionable insights for operating your database fleet across accounts and Regions.

The DROID Dashboard provides the following key capabilities:
+ Fleet inventory across accounts, Regions, engines, and instance classes, with Graviton adoption
+ Major and minor engine version compliance against the latest available versions
+ End-of-standard-support and Amazon RDS Extended Support exposure
+ Security and resiliency monitoring, including encryption, certificate validity, Multi-AZ, public accessibility, storage autoscaling, and Amazon CloudWatch Database Insights mode
+ Backup coverage and daily snapshot backup percentage for instances and Aurora clusters
+ Pending maintenance actions
+ Cost by account, Region, and engine, including Amazon RDS Extended Support charges and Amazon Aurora I/O-Optimized recommendations

The following screenshot shows the RDS Inventory tab on the DROID Dashboard, the fleet overview you open first. The KPI tiles across the top report total instances, accounts, Regions, database engines, and instance classes. The charts below break the fleet down by engine and by Region. A dynamic group-by control lets you re-pivot those charts by account, Region, engine, instance class, or processor type. Use this tab to see where your database fleet is concentrated before you drill into the other tabs.

![The RDS Inventory tab showing KPI tiles for total instances, accounts, Regions, database engines, and instance classes, with donut and bar charts of instance distribution by engine and Region.](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/dashboards/droid-inventory.png)


To explore the dashboard with sample data, open the [interactive DROID demo dashboard](https://cid.workshops.aws.dev/demo?dashboard=droid).

The dashboard has five tabs:
+  **RDS Inventory**: Fleet overview with instance counts, engine and Region distribution, instance class breakdown, Graviton adoption, and a dynamic group-by control.
+  **RDS Version and Maintenance**: Major and minor version compliance, end-of-support status, and pending maintenance actions.
+  **RDS Security and Resiliency**: Encryption, certificate status, Multi-AZ, public accessibility, storage autoscaling, and Database Insights mode.
+  **RDS Snapshot Backup**: Daily backup coverage and backup percentage for instances and Aurora clusters.
+  **RDS Cost and Usage**: RDS and Aurora spend by account, Region, and engine, Extended Support cost, and Aurora I/O-Optimized recommendations.

The RDS Inventory, RDS Version and Maintenance, RDS Security and Resiliency, and RDS Snapshot Backup tabs share a Collection Date control so you can view the fleet as of a specific collection date. By default, the dashboard shows the latest collection date. To review an earlier snapshot, switch the date control to Selected and choose a collection date. The RDS Cost and Usage tab filters by billing period instead.

## Architecture
<a name="architecture"></a>

The DROID Dashboard reads data that the Data Collection framework writes to your Data Collection account. It performs all enrichment in Amazon Athena views and presents it in the dashboard under different categories for insights and actions.

The following diagram shows the data flow. The Inventory, Reference, and RDS data-collection modules write Amazon RDS and Amazon Aurora data to your Data Collection account. Amazon Athena views join and enrich that data. Amazon Quick then loads the result and presents it in the dashboard. The numbered steps after the diagram describe each stage.

![Data flow from an Amazon EventBridge schedule through AWS Step Functions and Lambda collectors that write Amazon RDS and Amazon Aurora data to Amazon S3, which AWS Glue catalogs, Amazon Athena enriches, and Amazon Quick presents in the dashboard.](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/architecture/droid.png)


1. An Amazon EventBridge schedule invokes the AWS Step Functions state machine for each deployed data-collection module.

1. The state machine runs an **Account Collector** Lambda function that assumes a read-only role in your management account and retrieves the list of linked accounts from the AWS Organizations API.

1. A Step Functions Map state runs a data-collection Lambda function for each linked account and Region.

1. In each linked account, the Lambda function assumes a read-only role and retrieves Amazon RDS and Amazon Aurora data (instances, clusters, snapshots, and pending maintenance actions) with the AWS SDK, then stores it in the Data Collection Amazon S3 bucket.

1. An AWS Glue crawler registers the data in the AWS Glue Data Catalog. Amazon Athena views then join and enrich it, deriving version compliance, end-of-support status, backup coverage, and tag values, with separate cost views that read CUR data and compute Amazon Aurora I/O-Optimized recommendations.

1. Amazon Quick ingests the Athena views into SPICE (Super-fast, Parallel, In-memory Calculation Engine) and presents the dashboard to your database, SRE, and FinOps teams.

## Prerequisites
<a name="prerequisites"></a>

1. Deploy one or more of the foundational dashboards: [CUDOS, Cost Intelligence, or KPI Dashboard](cudos-cid-kpi.md). This deployment enables the Amazon Athena, AWS Glue, and Quick resources and the CUR data that the RDS Cost and Usage tab uses.

1.  **Quick Enterprise Edition** is required for SPICE datasets and calculated fields.

## Deployment
<a name="deployment"></a>

Deployment has four parts: enable the required Data Collection modules, verify the data in Amazon Athena, deploy the dashboard, and verify the dashboard views.

### Step 1: Enable the required modules in the Data Collection Stack
<a name="step-1-enable-the-required-modules"></a>

Enable these modules when you deploy or update the Data Collection Stack (version 3.14.11 or later) in your **Data Collection** account.

1. Sign in to your **Data Collection** account and open the [AWS CloudFormation](https://console.aws.amazon.com/cloudformation) console.

1.  [Deploy](data-collection-deployment.md) the Data Collection Stack (first-time setup) or [Update](data-collection-update.md) your existing stack to version 3.14.11 or later. The **Include RDS Module** parameter is available from version 3.14.11.

1. In the **Parameters** section, set the following values:


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th><th>Example</th></tr>
</thead>
<tbody>
  <tr><td> <b>Include Inventory Collector Module</b> </td><td>Collects Amazon RDS instances, Amazon Aurora clusters, and snapshots</td><td> <code>yes</code> </td></tr>
  <tr><td> <b>Include Reference Module</b> </td><td>Provides engine version and end-of-support reference data</td><td> <code>yes</code> </td></tr>
  <tr><td> <b>Include RDS Module</b> </td><td>Collects pending maintenance actions and Aurora cluster snapshots</td><td> <code>yes</code> </td></tr>
</tbody>
</table>


1. Complete the stack deployment or update. Wait until the stack reaches `CREATE_COMPLETE` or `UPDATE_COMPLETE`.

**Note**  
The RDS module requires the Inventory and Reference modules. The Data Collection template enforces this at deploy time: the stack fails with a clear message if **Include RDS Module** is `yes` without them.  
Optional: enable the **Include Org Data Module** to show AWS Organizations account names. Without it, cid-cmd builds account names from CUR or a CSV file.

**Note**  
RDS data is collected on the standard Data Collection schedule, every 14 days by default.  
For a more current view, increase the RDS-related collection schedules:  
 `rate(7 days)`: fresher data at moderate cost.
 `rate(1 day)`: the freshest data and the most granular Collection Date history.
The **RDS Snapshot Backup** tab benefits most from daily collection (`rate(1 day)`): its daily backup coverage and 14-day and 30-day percentages are only meaningful with daily data points.  
More frequent collection increases AWS Glue crawler and SPICE refresh costs. For steps, see [Tailoring Data Collector schedules](tailor-data-collector.md).  
Allow one collection cycle of the Inventory, Reference, and RDS modules to complete after a fresh deployment before the dashboard is fully populated.

### Step 2: Verify data in Amazon Athena
<a name="step-2-verify-data-in-amazon-athena"></a>

Run a test query to confirm the base data is available.

```
SELECT COUNT(*) FROM optimization_data.inventory_rds_db_instances_data;
```

For an Aurora-only fleet whose clusters have no instances, also verify clusters:

```
SELECT COUNT(*) FROM optimization_data.inventory_rds_db_clusters_data;
```

### Step 3: Deploy the dashboard
<a name="step-3-deploy-the-dashboard"></a>

**Example**  
**Prerequisite**  
To install this dashboard using AWS CloudFormation, install the Foundational Dashboards template version v4.0.0 or above. For steps, see [Deploying dashboards in the global Region](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard).

1. Sign in to your **Data Collection** account.

1. Choose the following Launch Stack button. Choosing it opens the AWS CloudFormation console with a stack template pre-populated with the DROID Dashboard ID and data-collection settings.

    [![Launch Stack button that opens the pre-populated AWS CloudFormation stack creation page for the DROID Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=DROID-Dashboard&param_DashboardId=droid&param_RequiresDataCollection=yes) 

1. (Optional) Change the **Stack name**.

1. Leave the **Parameters** values as they are.

1. Review the configuration and choose **Create stack**.

1. Wait for the stack status to change from `CREATE_IN_PROGRESS` to `CREATE_COMPLETE`.

1. Check the stack output for dashboard URLs.
**Troubleshooting**  
If you see the error "No export named cid-CidExecArn found", confirm that you completed the [prerequisite steps](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard).

1. Sign in to your **Data Collection** account.

1. Open a command-line interface with permissions to run API requests. We recommend [AWS CloudShell](https://console.aws.amazon.com/cloudshell).

1. Install the CID command line tool:

   ```
   pip3 install --upgrade cid-cmd
   ```

1. Deploy the dashboard:

   ```
   cid-cmd deploy --dashboard-id droid
   ```

   Follow the deployment wizard. The wizard prompts you for the CUR database and table. For more information about command line options, see the [README](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/?tab=readme-ov-file#command-line-tool-cid-cmd) on the GitHub website or run `cid-cmd --help`.

### Step 4: Verify the dashboard views
<a name="step-4-verify-the-dashboard-views"></a>

After the dashboard deploys, confirm the enriched views return data. Run this in the Athena database where the dashboard created its views:

```
SELECT COUNT(*) FROM rds_inventory_view;
```

For the full list of views, see [Views reference](#views-reference).

## Usage guide
<a name="usage-guide"></a>

**Example**  
Start on the RDS Inventory tab for a fleet-wide overview of your Amazon RDS and Amazon Aurora estate: what you run, where, and on which engines and instance types. This tab provides:  
+ Headline KPIs: total instances, accounts, Regions, database engines, and instance classes
+ Instance distribution by account, Region, and engine to spot concentration and sprawl
+ Instance class breakdown and Graviton and processor-type adoption to surface modernization candidates
+ A daily instance-count trend to track fleet growth over time
+ A dynamic group-by control to pivot the breakdown by account, Region, engine, instance class, or processor type
+ A detailed inventory table you can filter, sort, and export for offline analysis
Use the RDS Version and Maintenance tab to keep engines current and stay ahead of end-of-support and maintenance events. This tab provides:  
+ Headline KPIs: total instances, instances on the latest major and minor versions, auto-minor-upgrade adoption, instances in Extended Support, and pending maintenance actions
+ Fleet percentage on the latest major and minor versions, shown as gauges
+ Per-instance comparison of the current version against the latest, N-1, and N-2 versions, color-coded for quick triage
+ Support status for each database: Standard Support, Extended Support, End of Standard Support, or End of Extended Support
+ End-of-standard-support and Amazon RDS Extended Support dates for each major version
+ Count of instances in Extended Support and the associated monthly charges
+ Auto minor version upgrade adoption
+ Pending maintenance actions per instance, with current, forced, and auto-apply dates
Review the security and resiliency posture of every database on the RDS Security and Resiliency tab. This tab provides:  
+ Headline KPIs: total instances, unencrypted instances, active certificates, Multi-AZ instances, publicly accessible instances, and Database Insights Advanced-mode instances
+ Storage encryption coverage, with a fleet encryption percentage and an unencrypted count
+ Certificate authority (CA) certificate status (Active or Expired) and a certificate-validity percentage
+ Multi-AZ adoption for high availability
+ Public accessibility exposure
+ Storage autoscaling enablement
+ Amazon CloudWatch Database Insights mode (Standard or Advanced)
+ A configuration summary with color-coded OK and attention indicators
Monitor backup and recovery readiness on the RDS Snapshot Backup tab. This tab provides:  
+ Headline KPIs: total instances, instances with automated backups disabled, instances without a recent backup, and average backup percentage
+ Daily backup coverage for both DB instances and Aurora clusters
+ Backup percentage over the last 14 and 30 days
+ Backup coverage broken down by account, Region, and engine
+ A snapshot backup history table for detailed review
Analyze Amazon RDS and Amazon Aurora spend and find savings on the RDS Cost and Usage tab. This tab provides:  
+ Headline KPIs: total RDS and Aurora spend, Aurora I/O-Optimized savings, and I/O-Optimized recommendation count
+ Amortized cost by account, Region, and engine, reflecting Reserved Instance and Savings Plans discounts
+ Month-over-month amortized cost trend
+ Amazon RDS Extended Support charges, so you can quantify the cost of lagging versions
+ Amazon Aurora I/O-Optimized recommendations per cluster, with I/O percentage and estimated monthly savings
+ Cost breakdown by usage type and instance
+ A cost dimension group-by control

## Views reference
<a name="views-reference"></a>

The dashboard creates the following Amazon Athena views, which you can query directly for custom reporting.


| View | Purpose | 
| --- | --- | 
|  `rds_inventory_view`  | Instance inventory with version compliance and end-of-support status | 
|  `rds_backup_view`  | Daily backup and snapshot coverage | 
|  `rds_maintenance_view`  | Pending maintenance actions | 
|  `rds_tags_view`  | Tag values for the tag filter | 
|  `rds_cost_summary_view`  | RDS and Aurora amortized cost from CUR | 
|  `rds_aurora_io_optimized_view`  | Amazon Aurora I/O-Optimized analysis from CUR | 

## Update
<a name="update"></a>

When a new version of the dashboard template is released, update your dashboard.

```
cid-cmd update --dashboard-id droid
```

## Teardown
<a name="teardown"></a>

To remove the DROID Dashboard and its data collection:

1. Delete the Quick dashboard and datasets with `cid-cmd delete --dashboard-id droid`, or use the Quick console.

1.  [Update](data-collection-update.md) the Data Collection Stack and the read-permissions StackSet, and set **Include RDS Module** back to `no` if no other dashboard uses it. This removes the maintenance and cluster-snapshot collectors, and removes `RDSModulePolicy` from the linked accounts.

1. (Optional) Delete the collected data from the Data Collection bucket.

## Authors
<a name="authors"></a>
+ Anish Kumar Gopal, Senior Technical Account Manager

## Contributors
<a name="contributors"></a>
+ Yuriy Prykhodko, Principal Technical Account Manager
+ Eric Christensen, Senior Technical Account Manager
+ Prashob Krishnan, Principal Technical Account Manager

## Feedback and support
<a name="droid-dashboard-feedback-support"></a>

For feedback and support, see the [Feedback and Support](feedback-support.md) guide.

**Note**  
These dashboards and their content: (a) are for informational purposes only, (b) represent current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS content, products or services are provided "as is" without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers.