# Kiro User Activity Dashboard

## Introduction

The Kiro User Activity Dashboard provides enterprise visibility into [Kiro](https://kiro.dev/ "https://kiro.dev/") AI coding assistant usage across your AWS accounts. It tracks per-user credit consumption, model usage, and overage risk. Cloud financial management (FinOps) and engineering leaders can use this data to manage Kiro adoption at scale.

Key capabilities include:

- Credit consumption monitoring with tier-based utilization thresholds
- Per-user and per-account usage breakdown across all Kiro-enabled regions
- Model-level message tracking (Claude Opus, Sonnet, Haiku, and other models)
- Subscription tier right-sizing recommendations (upgrade, downgrade, right-sized)
- Overage detection and at-risk user identification (at or above 75% plan utilization)
- New user adoption tracking

The following screenshot shows the Executive Summary tab of the Kiro User Activity Dashboard:

![The Kiro User Activity Dashboard Executive Summary tab showing Active Users](/images/guidance/latest/cloud-intelligence-dashboards/images/images/dashboards/kiro-executive-view.png)

## Demo Dashboard

Get more familiar with the Dashboard using the live, interactive demo
dashboard following this
[link](https://cid.workshops.aws.dev/demo?dashboard=kiro-user-activity&sheet=default "https://cid.workshops.aws.dev/demo?dashboard=kiro-user-activity&sheet=default").

The dashboard has five tabs:

- **Executive Summary**:

  - Active Users, Total Messages, Credits Used, Overage Credits, New Users KPIs
  - Daily Active Users by Client Type
  - Credits by Subscription Tier
  - Messages by Model
  - Daily Credits Consumed by Tier

- **User Engagement**:

  - Top 50 Users by Message Count colored by Model
  - Monthly User Summary pivot table with tier recommendations
  - Utilization percentage and credits per message metrics

- **Credit & Overage Tracking**:

  - Daily Credits Used vs Overage
  - Users at Risk KPI (at or above 75% plan utilization)
  - Users in Overage KPI
  - Monthly Credits and Overage pivot table

- **Model & Client Breakdown**:

  - Daily Messages by Model
  - Monthly Model and Client pivot table with user counts and efficiency metrics

- **About**:

  - Dashboard version and release information
  - Legal notice

All tabs include shared filter controls for lookback period, AWS Account, User, Model, and Client Type.

## Architecture

The Kiro User Activity module uses a **pull-based** architecture. A central AWS Lambda function in the Data Collection account reads CSV reports from customer Kiro source buckets on a daily schedule. Customers only need to apply a bucket policy, because no AWS CloudFormation stack is deployed in their accounts.

The following diagram shows the pull-based data collection flow:

![The pull-based Kiro User Activity data collection flow from source S3 buckets through a central Lambda function to the Data Collection bucket](images/images/architecture/kiro-user-activity.png)

1. The Kiro service writes daily CSV user activity reports at 2 AM UTC to each customer’s designated S3 bucket, under the path `kiro/AWSLogs/<account-id>/KiroLogs/user_report/<region>/<year>/<month>/<day>/`.
2. A Lambda function (scheduled at 3 AM UTC) reconciles each source bucket against the central Data Collection bucket. It lists every Kiro report in the source and every file already imported to the destination. It then pulls only the reports that are missing. For each report it pivots the model-specific columns into normalized rows. It then writes Hive-partitioned output to the central Data Collection bucket, keyed by source account and region: `kiro-user-activity/account_id=<id>/region=<region>/year=<year>/month=<month>/day=<day>/`. The destination is the source of truth for what has already been collected. This gives the reconcile both checkpointing (transient failures self-heal on the next run) and backfill (any missing history is filled). It also scales to accounts that manage many source buckets.
3. An explicit AWS Glue table partitioned by `account_id`, `region`, `year`, `month`, and `day` makes the source account and region first-class query dimensions. This partitioning also prevents cross-account filename collisions. The Lambda registers each partition it writes through the AWS Glue API. Amazon Athena can then query the data without an AWS Glue crawler or `MSCK REPAIR TABLE`, and newly onboarded accounts and regions become queryable automatically.
4. Amazon Quick Suite ingests data from Amazon Athena (through a bounded two-year view over the table) into SPICE (Super-fast, Parallel, In-memory Calculation Engine) and applies calculated fields for utilization metrics, tier recommendations, and overage tracking.

## Prerequisites

1. Deploy one or more of the foundational dashboards: [CUDOS, Cost Intelligence, or KPI Dashboard](cudos-cid-kpi.md "cudos-cid-kpi.md"). This deployment enables the required Amazon Athena and Amazon Quick Suite resources for this dashboard.
2. [Deploy](data-collection-deployment.md "data-collection-deployment.md") or [Update](data-collection-update.md "data-collection-update.md") the Data Collection Stack with the **Kiro User Activity Data Collection Module** enabled (see [Step 1](#step-1-enable-the-kiro-user-activity-module-in-the-data-collection-stack "#step-1-enable-the-kiro-user-activity-module-in-the-data-collection-stack")).
3. **Kiro user activity reporting enabled** — Each source account must have Kiro user activity reporting enabled and writing CSV reports to an Amazon S3 bucket. This is configured in each account through the Kiro console.
4. **Amazon Quick Suite Enterprise Edition** — Required for SPICE datasets and calculated fields.

###### Note

Unlike most Data Collection modules, the Kiro User Activity module is **pull-based** and does **not** require the Management Account Read Permissions stack or a Linked Account StackSet. The central collection Lambda reads directly from the source buckets you specify, and each source account grants access with a bucket policy (see [Step 2](#step-2-grant-read-access "#step-2-grant-read-access")).

###### Important

This module currently supports source buckets that are unencrypted or encrypted with Amazon S3-managed keys (**SSE-S3**). Source buckets encrypted with an AWS KMS key (**SSE-KMS**) are **not** supported: the bucket policy in [Step 2](#step-2-grant-read-access "#step-2-grant-read-access") grants Amazon S3 read access only, so the collection Lambda cannot decrypt objects protected by a customer-managed KMS key and collection fails.

If your Kiro source buckets use SSE-KMS, either change the bucket’s default encryption to SSE-S3 (or ensure the objects written under `kiro/*` use SSE-S3), or track KMS support through [Feedback and Support](#kiro-user-activity-dashboard-feedback-support "#kiro-user-activity-dashboard-feedback-support").

## Deployment

Deployment consists of three steps: enabling the data collection module in the Data Collection Stack, granting read access from each source account, and deploying the Quick Suite dashboard.

### Step 1: Enable the Kiro User Activity Module in the Data Collection Stack

The Kiro User Activity module is part of the [Data Collection Stack](data-collection.md "data-collection.md"). Enable it when you deploy or update the stack in your **Data Collection** account.

1. Sign in to your **Data Collection** account and open the [AWS CloudFormation](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation") console.
2. [Deploy](data-collection-deployment.md "data-collection-deployment.md") the Data Collection Stack (first-time setup) or [Update](data-collection-update.md "data-collection-update.md") your existing Data Collection Stack.
3. In the **Parameters** section, set the following values for the **Kiro User Activity Module Configuration**:

| Parameter                                             | Description                                                                     | Example                                                   |
| ----------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Include Kiro User Activity Data Collection Module** | Set to `yes` to enable the module                                               | `yes`                                                     |
| **Kiro Source Bucket Names (comma-separated)**        | Comma-separated list of S3 bucket names where Kiro writes user activity reports | `my-kiro-bucket-111111111111,my-kiro-bucket-222222222222` |

4. Complete the stack deployment or update. After the stack reaches `CREATE_COMPLETE` or `UPDATE_COMPLETE`, AWS CloudFormation creates the Kiro collection Lambda function, Amazon EventBridge Scheduler schedule, and AWS Glue table.
5. In the AWS CloudFormation **Outputs** of the nested Kiro module stack, note the **LambdaRoleArn** value. You use this ARN in each source account’s bucket policy in [Step 2](#step-2-grant-read-access "#step-2-grant-read-access").

###### Note

The collection Lambda runs daily at 3 AM UTC, after Kiro generates its reports at 2 AM UTC. On each run it reconciles every source bucket against what has already been imported and pulls any missing reports, regardless of date. This means the first run backfills all available history, and subsequent runs copy only new or previously-missed reports.

### Step 2: Grant Read Access

Apply the following in each source account that produces Kiro user activity reports. Each account must apply a bucket policy granting read access to the collection Lambda role from Step 1. **No CloudFormation stack is deployed in the source accounts** — a bucket policy is all that is required.

Add the following two statements to the S3 bucket policy on each Kiro source bucket. Access is scoped to the `kiro/*` prefix so the collection Lambda can read only the Kiro user activity reports, not the rest of the bucket:

```
{
  "Sid": "AllowCIDKiroDataCollectionRead",
  "Effect": "Allow",
  "Principal": {
    "AWS": "<LambdaRoleArn from Step 1 Outputs>"
  },
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::<kiro-source-bucket-name>/kiro/*"
},
{
  "Sid": "AllowCIDKiroDataCollectionList",
  "Effect": "Allow",
  "Principal": {
    "AWS": "<LambdaRoleArn from Step 1 Outputs>"
  },
  "Action": "s3:ListBucket",
  "Resource": "arn:aws:s3:::<kiro-source-bucket-name>",
  "Condition": {
    "StringLike": {
      "s3:prefix": "kiro/*"
    }
  }
}
```

###### Tip

The exact bucket policy statements, pre-populated with your Lambda role ARN, are also provided in the `BucketPolicyExample` CloudFormation stack output.

###### Important

When you specify a role ARN as a bucket policy `Principal`, Amazon S3 stores it internally as the role’s unique ID, not the ARN string. If you tear down and later re-enable the module (or otherwise delete and recreate the Lambda role), the new role has a **different** unique ID even though the ARN is unchanged. The existing bucket policy then still points at the deleted role, so the Lambda can no longer list or read the source bucket. Collection fails quietly — the run returns `total_files_copied: 0`, and any per-bucket access failures appear in the `errors` array of the Lambda response.

If you re-deploy the module, re-apply the bucket policy in each source account so it re-resolves to the new role. Use the current `BucketPolicyExample` stack output as the source of truth.

### Step 3: Test the Lambda Collector

Invoke the Lambda manually to verify data flows correctly:

```
aws lambda invoke \
  --region <region> \
  --function-name CID-DC-kiro-user-activity-Lambda \
  /tmp/kiro-output.json && cat /tmp/kiro-output.json
```

Expected response (a successful run returns `statusCode: 200`; `total_files_copied`, `total_rows_written`, and `partitions_registered` reflect how many reports were **missing** and therefore imported on this run — a run where everything is already collected returns zeros, which is normal):

```
{
  "statusCode": 200,
  "total_files_copied": 3,
  "total_rows_written": 45,
  "partitions_registered": 3,
  "errors": []
}
```

###### Note

The collector imports only reports that are not already present in the destination. On a first run it backfills everything available; on later runs `total_files_copied` is often 0 because there is nothing new to copy — this is expected and not an error.

If a **first** run (or a run against a brand-new source bucket) reports `total_files_copied: 0`, verify the following:

- The bucket policy in the source account is applied, and — if you have re-deployed the module — that it points at the **current** Lambda role (see the IMPORTANT note in [Step 2](#step-2-grant-read-access "#step-2-grant-read-access")).
- The **Kiro Source Bucket Names** parameter is correct.
- The Kiro service has written reports to the source bucket under the expected `kiro/AWSLogs/<account-id>/KiroLogs/user_report/…​` path.
  The collector reads the source account, region, and date from the **S3 object path** (`kiro/AWSLogs/<account-id>/KiroLogs/user_report/<region>/<year>/<month>/<day>/…​`) rather than from columns inside the CSV. Reports that do not match this path layout (for example the legacy `by_user_analytic` report) are skipped.

### Step 4: Verify Data in Athena

Run a test query to confirm data is accessible:

```
SELECT * FROM optimization_data.kiro_user_activity LIMIT 10;
```

### Step 5: Deploy the Quick Suite Dashboard

###### Example

CloudFormation

###### Note

**Prerequisite**: To install this dashboard using CloudFormation, you need to install Foundational Dashboards CFN with version v4.0.0 or above as described [here](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard "deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard")

1. Sign in to your **Data Collection** account. Choose the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation.

[![Launch Stack button](images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=Kiro-User-Activity-Dashboard&param_DashboardId=kiro-user-activity&param_RequiresDataCollection=yes "https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=Kiro-User-Activity-Dashboard&param_DashboardId=kiro-user-activity&param_RequiresDataCollection=yes") 2. (Optional) Change the **Stack name** for your template. 3. Leave **Parameters** values as it is. 4. Review the configuration and choose **Create stack**. 5. The stack starts in **CREATE\_IN\_PROGRESS** status. When complete, the stack shows **CREATE\_COMPLETE**. 6. Check the stack output for dashboard URLs.

###### Note

**Troubleshooting:** If you see error "No export named cid-CidExecArn found" during stack deployment, make sure you have completed prerequisite steps.

Command Line

1. Sign in to your **Data Collection** account.
2. Open a command-line interface with permissions to run API requests in your AWS account. We recommend [AWS CloudShell](https://console.aws.amazon.com/cloudshell "https://console.aws.amazon.com/cloudshell").
3. In your command-line interface run the following command to download and install the CID CLI tool:

```
pip3 install --upgrade cid-cmd
```

4. In your command-line interface run the following command to deploy the dashboard:

```
cid-cmd deploy --dashboard-id kiro-user-activity
```

Follow the instructions from the deployment wizard. For more information about command line options, see the [README](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/?tab=readme-ov-file#command-line-tool-cid-cmd "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/?tab=readme-ov-file#command-line-tool-cid-cmd") or run `cid-cmd --help`.

### Step 6: Trigger Initial SPICE Refresh

After deploying the dashboard, trigger a SPICE ingestion to load data:

```
cid-cmd refresh --dashboard-id kiro-user-activity
```

## Adding New Source Accounts

To start collecting data from additional Kiro-enabled accounts:

1. [Update](data-collection-update.md "data-collection-update.md") the Data Collection Stack, adding the new bucket name(s) to the **Kiro Source Bucket Names** parameter.
2. Apply the bucket policy from [Step 2: Grant Read Access](#step-2-grant-read-access "#step-2-grant-read-access") in the new source account.
3. Invoke the Lambda manually, as described in [Step 3: Test the Lambda Collector](#step-3-test-the-lambda-collector "#step-3-test-the-lambda-collector"), to verify the new source is discovered.

You do not need to redeploy the dashboard. New accounts automatically appear as filter values after the next SPICE refresh.

## Usage Guide

###### Example

Executive Summary
Start with the Executive Summary tab to get a high-level view of Kiro adoption and credit consumption:

- **Active Users KPI** — Distinct users with at least one message in the selected period
- **Credits Used KPI** — Total credits consumed in the selected lookback period
- **Overage Credits KPI** — Credits consumed beyond plan allocation
- **New Users KPI** — Users flagged as new by Kiro
- **Daily Active Users by Client Type** — Tracks adoption across Kiro client types (`KIRO_IDE`, `KIRO_CLI`, and `PLUGIN`)
- **Credits by Subscription Tier** — Shows consumption distribution across the Pro, ProPlus, ProMax, and Power tiers
- **Messages by Model** — Identifies which models drive the most activity

User Engagement
Drill into individual user behavior:

- **Top 50 Users** — Identifies power users and potential champions
- **Monthly User Summary** — Pivot table grouped by year, month, account, and user with key metrics:

  - Total messages, credits used, plan credits, monthly utilization %, credits per message
  - Tier recommendation (Upgrade Candidate, Downgrade Candidate, Review Overage Settings, or Right-Sized)

Credit & Overage Tracking
Monitor credit health and identify risk:

- **Users at Risk** — Count of users at or above 75% of their monthly plan credits
- **Users in Overage** — Count of users who have exceeded their plan allocation
- **Daily Credits vs Overage** — Visualizes daily burn rate against plan limits
- **Monthly Credits pivot** — Detailed per-user credit tracking with overage breakdown

Model & Client Breakdown
Understand AI model utilization patterns:

- **Daily Messages by Model** — Stacked bar chart showing model popularity over time
- **Monthly Model and Client pivot** — Groups data by model and client type with user counts, message volumes, and cost efficiency

## Calculated Fields Reference

The following calculated fields are created in the Quick Suite dataset:

| Field                          | Logic                                                                                                                                                                                             | Purpose                                                                                   |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `report_date`                  | `parseDate({date}, "yyyy-MM-dd")`                                                                                                                                                                 | Date type for time-series                                                                 |
| `user`                         | Email if available, cleaned userid otherwise                                                                                                                                                      | Human-readable display                                                                    |
| `plan_credits`                 | Pro=1000, ProPlus=2000, ProMax=5000, Power=10000, Free=50                                                                                                                                         | Monthly plan allocation                                                                   |
| `plan_utilization_pct`         | `credits_used / plan_credits`                                                                                                                                                                     | Per-day utilization (not used directly by the pivots; see `monthly_plan_utilization_pct`) |
| `in_overage_flag`              | 1 if overage\_credits > 0                                                                                                                                                                         | Overage counter                                                                           |
| `credits_per_message`          | `credits_used / total_messages`                                                                                                                                                                   | Efficiency metric                                                                         |
| `is_new_user`                  | 1 if new\_user = true                                                                                                                                                                             | Adoption counter                                                                          |
| `monthly_plan_utilization_pct` | Cumulative monthly credits per user / plan\_credits (analysis-level, aggregated over the calendar month)                                                                                          | Monthly utilization — the basis for utilization %, at-risk, and tier recommendations      |
| `monthly_overage_credits`      | Sum of a user’s overage credits over the calendar month (analysis-level)                                                                                                                          | Monthly overage total                                                                     |
| `at_risk_flag`                 | 1 if monthly utilization >= 75%                                                                                                                                                                   | Risk threshold                                                                            |
| `tier_recommendation_monthly`  | Any monthly overage → Upgrade Candidate (or Review Overage Settings if already on Power, the top tier); else monthly utilization <30% on a tier above Pro → Downgrade Candidate; else Right-Sized | Tier optimization (evaluated on monthly, not per-day, usage)                              |

###### Note

Utilization, at-risk, and tier-recommendation logic all evaluate usage over the **calendar month**, because Kiro plan credits are allocated and reset per calendar month. Set the dashboard’s lookback period to a full calendar month when reviewing these metrics.

## Update

When a new version of the dashboard template is released, update your dashboard by running the following command:

```
cid-cmd update --dashboard-id kiro-user-activity
```

## Teardown

To remove the Kiro User Activity module:

1. Delete the Quick Suite dashboard and dataset via the Quick Suite console or `cid-cmd delete --dashboard-id kiro-user-activity`.
2. [Update](data-collection-update.md "data-collection-update.md") the Data Collection Stack and set **Include Kiro User Activity Data Collection Module** back to `no`. This removes the collection Lambda, EventBridge Scheduler schedule, and Glue table.
3. (Optional) Remove the bucket policy statements from source accounts.
4. (Optional) Delete collected data from `s3://<dest-bucket>/kiro-user-activity/`.

###### Note

If you migrated from an earlier, replication-based version of this module, the destination bucket might also contain a legacy `s3://<dest-bucket>/kiro/` prefix (the raw replication landing zone) and an AWS Glue crawler. These are not used by the current pull-based architecture. After confirming no Glue table still references the `kiro/` prefix, you can delete that data and remove the crawler.

## Authors

- Darius Seroka, Senior Technical Account Manager

## Contributors

- Yuriy Prykhodko, Principal Technical Account Manager
- Eric Christensen, Senior Technical Account Manager

## Feedback & Support

For feedback and support, see the [Feedback and Support](feedback-support.md "feedback-support.md") guide.

###### Note

These dashboards and their content: (a) are for informational
purposes only, (b) represent current AWS product offerings and
practices, which are subject to change without notice, and (c) does not
create any commitments or assurances from AWS and its affiliates,
suppliers or licensors. AWS content, products or services are provided
"as is" without warranties, representations, or conditions of any
kind, whether express or implied. The responsibilities and liabilities
of AWS to its customers are controlled by AWS agreements, and this
document is not part of, nor does it modify, any agreement between AWS
and its customers.
