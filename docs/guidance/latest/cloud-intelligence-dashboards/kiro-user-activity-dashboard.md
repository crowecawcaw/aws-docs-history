

# Kiro User Activity Dashboard
<a name="kiro-user-activity-dashboard"></a>

## Introduction
<a name="introduction"></a>

The Kiro User Activity Dashboard provides enterprise visibility into [Kiro](https://kiro.dev/) AI coding assistant usage across your AWS accounts. It tracks per-user credit consumption, model usage, overage risk, and the cost of licences nobody is using. Cloud financial management (FinOps) and engineering leaders can use this data to manage Kiro adoption at scale.

The dashboard answers two different questions from two different data sources. **How is Kiro being used?** comes from the Kiro user activity report: messages, credits, models, and client types, per user per day. **What are we paying for, and is it being used?** comes from your AWS Cost and Usage Report (CUR): which licences appear on each month’s bill, which of them consumed credits, and what the ones that did not have cost you. Because Kiro allocates and resets plan credits per calendar month, both halves are scoped by a single **Billing period** control.

Key capabilities include:
+ Licence-level subscription tracking: how many Kiro licences are billed in a month, how many were used, and how many sat idle
+ Idle licence reclaim reporting, with the cost attributable to the months a licence went unused
+ Credit consumption monitoring with tier-based utilization thresholds
+ Per-user and per-account usage breakdown across all Kiro-enabled regions
+ Model-level message tracking (Claude Opus, Sonnet, Haiku, and other models)
+ Subscription tier right-sizing recommendations (upgrade, downgrade, right-sized)
+ Overage detection and at-risk user identification (at or above 75% plan utilization)
+ Under-utilization detection (below 25% of plan), for conversations with team managers rather than direct action
+ New user adoption tracking

The following screenshot shows the Executive Summary tab of the Kiro User Activity Dashboard:

![The Kiro User Activity Dashboard Executive Summary tab showing Active Users](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/dashboards/kiro-executive-view.png)


## Demo Dashboard
<a name="demo-dashboard"></a>

Get more familiar with the Dashboard using the live, interactive demo dashboard following this [link](https://cid.workshops.aws.dev/demo?dashboard=kiro-user-activity&sheet=default).

The dashboard has five tabs:
+  **Executive Summary**:
  + Total Kiro Subscriptions, Active Kiro Licences, and Idle Kiro Licences KPIs (from CUR)
  + Total Messages, Credits Used, and Overage Credits KPIs (from the activity report)
  + Active Users by Client Type and Daily Active Users by Client Type
  + Credits by Subscription Tier
  + Messages by Model
+  **User Engagement**:
  + Users by Message Count, and Top 50 Users by Message Count colored by Model
  + User Summary pivot table with per-user monthly utilization and tier recommendations
  + Idle Kiro Licences table, listing reclaim candidates with licence tenure and idle cost
+  **Credit & Overage Tracking**:
  + Users at Risk KPI (at or above 75% plan utilization)
  + Users in Overage KPI
  + Users Below 25% of Plan KPI
  + Daily Credits Used vs Overage
  + Monthly Credits and Overage pivot table
+  **Model & Client Breakdown**:
  + Daily Messages by Model
  + Monthly Messages by Model and Client Type pivot table with user counts
+  **About**:
  + Dashboard version and release information
  + Legal notice

All tabs include shared filter controls for Billing period, AWS Account, User, Model, and Client Type.

**Important**  
The **Billing period** control scopes every widget on every tab, including the subscription KPIs and the Idle Kiro Licences table. Set it to a **whole calendar month**, and prefer a month that has closed.  
Kiro allocates and resets plan credits per calendar month, so a partial window understates plan utilization. It also under-reports subscriptions: Kiro subscription fee lines are dated either on the first of the billing month or spread daily through month end, and CUR delivery lag means the current month’s fee lines may not have arrived yet. A window that ends mid-month can therefore miss a licence’s billing rows entirely, and the licence drops out of the roster instead of being reported. The control defaults to the previous month for this reason, which is the most recent fully delivered bill.

## Architecture
<a name="architecture"></a>

The Kiro User Activity module uses a **pull-based** architecture. A central AWS Lambda function in the Data Collection account reads CSV reports from customer Kiro source buckets on a daily schedule. Customers only need to apply a bucket policy, because no AWS CloudFormation stack is deployed in their accounts.

The following diagram shows the pull-based data collection flow:

![The pull-based Kiro User Activity data collection flow from source S3 buckets through a central Lambda function to the Data Collection bucket](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/architecture/kiro-user-activity.png)


1. The Kiro service writes daily CSV user activity reports at 2 AM UTC to each customer’s designated S3 bucket, under the path `kiro/AWSLogs/<account-id>/KiroLogs/user_report/<region>/<year>/<month>/<day>/`.

1. A Lambda function (scheduled at 3 AM UTC) reconciles each source bucket against the central Data Collection bucket. It lists every Kiro report in the source and every file already imported to the destination. It then pulls only the reports that are missing. For each report it pivots the model-specific columns into normalized rows. It then writes Hive-partitioned output to the central Data Collection bucket, keyed by source account and region: `kiro-user-activity/account_id=<id>/region=<region>/year=<year>/month=<month>/day=<day>/`. The destination is the source of truth for what has already been collected. This gives the reconcile both checkpointing (transient failures self-heal on the next run) and backfill (any missing history is filled). It also scales to accounts that manage many source buckets.

1. An explicit AWS Glue table partitioned by `account_id`, `region`, `year`, `month`, and `day` makes the source account and region first-class query dimensions. This partitioning also prevents cross-account filename collisions. The Lambda registers each partition it writes through the AWS Glue API. Amazon Athena can then query the data without an AWS Glue crawler or `MSCK REPAIR TABLE`, and newly onboarded accounts and regions become queryable automatically.

1. Amazon Quick Suite ingests data from Amazon Athena (through a bounded two-year view over the table) into SPICE (Super-fast, Parallel, In-memory Calculation Engine) and applies calculated fields for utilization metrics, tier recommendations, and overage tracking.

The dashboard uses a **second** dataset, built from your existing AWS Cost and Usage Report rather than from the Kiro activity report. The activity report only contains users who did something, so it has no way to represent a subscribed-but-idle user. Subscription counts, the active and idle split, and all cost figures therefore come from CUR:

1. An Athena view over your CUR 2.0 table selects Kiro line items (`line_item_product_code = 'Kiro'`) for the last 18 months, at one row per billing line per subscriber. Subscription fee lines and credit-consumption lines are both retained, because the dashboard needs to distinguish them: the billing operation distinguishes them, not the pricing unit, because the same consumption arrives under two different pricing units. The view also joins the activity report per licence and month, so credit consumption that produces no billing record still registers as activity. It resolves a human-readable email from the same join, falling back to the raw Identity Center user ID for a subscriber who has never generated activity.

1. Quick Suite ingests that view into a second SPICE dataset. Both datasets expose a `usage_date` column under the same name, which is what allows the single **Billing period** control to scope both of them at once.

## Prerequisites
<a name="prerequisites"></a>

1. Deploy one or more of the foundational dashboards: [CUDOS, Cost Intelligence, or KPI Dashboard](cudos-cid-kpi.md). This deployment enables the required Amazon Athena and Amazon Quick Suite resources for this dashboard.

1.  [Deploy](data-collection-deployment.md) or [Update](data-collection-update.md) the Data Collection Stack with the **Kiro User Activity Data Collection Module** enabled (see [Step 1](#step-1-enable-the-kiro-user-activity-module-in-the-data-collection-stack)).

1.  **Kiro user activity reporting enabled** — Each source account must have Kiro user activity reporting enabled and writing CSV reports to an Amazon S3 bucket. This is configured in each account through the Kiro console.

1.  **An AWS Cost and Usage Report (CUR 2.0) data export**: required by the subscription and cost widgets, which read Kiro line items from CUR rather than from the activity report. The foundational dashboards in step 1 already set this up. If your organization’s Kiro subscriptions are billed in a payer account whose CUR you do not collect, those licences do not appear in the subscription KPIs or the Idle Kiro Licences table, although any activity they generate still appears in the usage widgets.

1.  **Amazon Quick Suite Enterprise Edition** — Required for SPICE datasets and calculated fields.

**Note**  
Unlike most Data Collection modules, the Kiro User Activity module is **pull-based** and does **not** require the Management Account Read Permissions stack or a Linked Account StackSet. The central collection Lambda reads directly from the source buckets you specify, and each source account grants access with a bucket policy (see [Step 2](#step-2-grant-read-access)).

**Important**  
This module currently supports source buckets that are unencrypted or encrypted with Amazon S3-managed keys (**SSE-S3**). Source buckets encrypted with an AWS KMS key (**SSE-KMS**) are **not** supported: the bucket policy in [Step 2](#step-2-grant-read-access) grants Amazon S3 read access only, so the collection Lambda cannot decrypt objects protected by a customer-managed KMS key and collection fails.  
If your Kiro source buckets use SSE-KMS, either change the bucket’s default encryption to SSE-S3 (or ensure the objects written under `kiro/*` use SSE-S3), or track KMS support through [Feedback and Support](#kiro-user-activity-dashboard-feedback-support).

## Deployment
<a name="deployment"></a>

Deployment consists of three steps: enabling the data collection module in the Data Collection Stack, granting read access from each source account, and deploying the Quick Suite dashboard.

### Step 1: Enable the Kiro User Activity Module in the Data Collection Stack
<a name="step-1-enable-the-kiro-user-activity-module-in-the-data-collection-stack"></a>

The Kiro User Activity module is part of the [Data Collection Stack](data-collection.md). Enable it when you deploy or update the stack in your **Data Collection** account.

1. Sign in to your **Data Collection** account and open the [AWS CloudFormation](https://console.aws.amazon.com/cloudformation) console.

1.  [Deploy](data-collection-deployment.md) the Data Collection Stack (first-time setup) or [Update](data-collection-update.md) your existing Data Collection Stack.

1. In the **Parameters** section, set the following values for the **Kiro User Activity Module Configuration**:


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th><th>Example</th></tr>
</thead>
<tbody>
  <tr><td> <b>Include Kiro User Activity Data Collection Module</b> </td><td>Set to <code>yes</code> to enable the module</td><td> <code>yes</code> </td></tr>
  <tr><td> <b>Kiro Source Bucket Names (comma-separated)</b> </td><td>Comma-separated list of S3 bucket names where Kiro writes user activity reports</td><td> <code>my-kiro-bucket-111111111111,my-kiro-bucket-222222222222</code> </td></tr>
</tbody>
</table>


1. Complete the stack deployment or update. After the stack reaches `CREATE_COMPLETE` or `UPDATE_COMPLETE`, AWS CloudFormation creates the Kiro collection Lambda function, Amazon EventBridge Scheduler schedule, and AWS Glue table.

1. In the AWS CloudFormation **Outputs** of the nested Kiro module stack, note the **LambdaRoleArn** value. You use this ARN in each source account’s bucket policy in [Step 2](#step-2-grant-read-access).

**Note**  
The collection Lambda runs daily at 3 AM UTC, after Kiro generates its reports at 2 AM UTC. On each run it reconciles every source bucket against what has already been imported and pulls any missing reports, regardless of date. This means the first run backfills all available history, and subsequent runs copy only new or previously-missed reports.

### Step 2: Grant Read Access
<a name="step-2-grant-read-access"></a>

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

**Tip**  
The exact bucket policy statements, pre-populated with your Lambda role ARN, are also provided in the `BucketPolicyExample` CloudFormation stack output.

**Important**  
When you specify a role ARN as a bucket policy `Principal`, Amazon S3 stores it internally as the role’s unique ID, not the ARN string. If you tear down and later re-enable the module (or otherwise delete and recreate the Lambda role), the new role has a **different** unique ID even though the ARN is unchanged. The existing bucket policy then still points at the deleted role, so the Lambda can no longer list or read the source bucket. Collection fails quietly — the run returns `total_files_copied: 0`, and any per-bucket access failures appear in the `errors` array of the Lambda response.  
If you re-deploy the module, re-apply the bucket policy in each source account so it re-resolves to the new role. Use the current `BucketPolicyExample` stack output as the source of truth.

### Step 3: Test the Lambda Collector
<a name="step-3-test-the-lambda-collector"></a>

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

**Note**  
The collector imports only reports that are not already present in the destination. On a first run it backfills everything available; on later runs `total_files_copied` is often 0 because there is nothing new to copy — this is expected and not an error.  
If a **first** run (or a run against a brand-new source bucket) reports `total_files_copied: 0`, verify the following:  
The bucket policy in the source account is applied, and — if you have re-deployed the module — that it points at the **current** Lambda role (see the IMPORTANT note in [Step 2](#step-2-grant-read-access)).
The **Kiro Source Bucket Names** parameter is correct.
The Kiro service has written reports to the source bucket under the expected `kiro/AWSLogs/<account-id>/KiroLogs/user_report/…​` path.
The collector reads the source account, region, and date from the **S3 object path** (`kiro/AWSLogs/<account-id>/KiroLogs/user_report/<region>/<year>/<month>/<day>/…​`) rather than from columns inside the CSV. Reports that do not match this path layout (for example the legacy `by_user_analytic` report) are skipped.

### Step 4: Verify Data in Athena
<a name="step-4-verify-data-in-athena"></a>

Run a test query to confirm data is accessible:

```
SELECT * FROM optimization_data.kiro_user_activity LIMIT 10;
```

### Step 5: Deploy the Quick Suite Dashboard
<a name="step-5-deploy-the-quick-suite-dashboard"></a>

**Example**  
 **Prerequisite**: To install this dashboard using CloudFormation, you need to install Foundational Dashboards CFN with version v4.0.0 or above as described [here](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard) 

1. Sign in to your **Data Collection** account. Choose the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation.

    [![Launch Stack button](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=Kiro-User-Activity-Dashboard&param_DashboardId=kiro-user-activity&param_RequiresDataCollection=yes) 

1. (Optional) Change the **Stack name** for your template.

1. Leave **Parameters** values as it is.

1. Review the configuration and choose **Create stack**.

1. The stack starts in **CREATE\_IN\_PROGRESS** status. When complete, the stack shows **CREATE\_COMPLETE**.

1. Check the stack output for dashboard URLs.
**Note**  
 **Troubleshooting:** If you see error "No export named cid-CidExecArn found" during stack deployment, make sure you have completed prerequisite steps.

1. Sign in to your **Data Collection** account.

1. Open a command-line interface with permissions to run API requests in your AWS account. We recommend [AWS CloudShell](https://console.aws.amazon.com/cloudshell).

1. In your command-line interface run the following command to download and install the CID CLI tool:

   ```
   pip3 install --upgrade cid-cmd
   ```

1. In your command-line interface run the following command to deploy the dashboard:

   ```
   cid-cmd deploy --dashboard-id kiro-user-activity
   ```

   Follow the instructions from the deployment wizard. For more information about command line options, see the [README](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/?tab=readme-ov-file#command-line-tool-cid-cmd) or run `cid-cmd --help`.

### Step 6: Trigger Initial SPICE Refresh
<a name="step-6-trigger-initial-spice-refresh"></a>

After deploying the dashboard, trigger a SPICE ingestion to load data:

```
cid-cmd refresh --dashboard-id kiro-user-activity
```

## Adding New Source Accounts
<a name="adding-new-source-accounts"></a>

To start collecting data from additional Kiro-enabled accounts:

1.  [Update](data-collection-update.md) the Data Collection Stack, adding the new bucket name(s) to the **Kiro Source Bucket Names** parameter.

1. Apply the bucket policy from [Step 2: Grant Read Access](#step-2-grant-read-access) in the new source account.

1. Invoke the Lambda manually, as described in [Step 3: Test the Lambda Collector](#step-3-test-the-lambda-collector), to verify the new source is discovered.

You do not need to redeploy the dashboard. New accounts automatically appear as filter values after the next SPICE refresh.

## Usage Guide
<a name="usage-guide"></a>

A typical review runs left to right. Set the **Billing period** to the month you are reviewing, read the Executive Summary to see whether the licence pool is the right size, use User Engagement to decide what to do about individual licences, and use Credit & Overage Tracking to spot people on the wrong tier. Model & Client Breakdown answers a separate question about which models and clients your developers actually work in.

**Example**  
This tab answers whether you are buying the right number of Kiro licences and whether they are being used. The first three KPIs come from billing data and count **licences**; the next three come from the activity report and count **usage**. They deliberately measure different populations and will not reconcile with each other, because CUR also covers accounts whose Kiro activity report you are not collecting.  
+  **Total Kiro Subscriptions**: licences that appear on the selected month’s bill. This is your licence pool for that month, and it is the denominator for everything else on the tab. A licence cancelled in a previous month simply has no fee line in the selected month and drops out on its own.
+  **Active Kiro Licences**: of those, the ones that consumed credits during the month. Someone was working in Kiro on this licence.
+  **Idle Kiro Licences**: the remainder, billed for the month but with no credit consumption in it. These are your reclaim candidates, and the count turns red when it is above zero. Active plus Idle always equals Total, so the three read as one sentence.
+  **Total Messages**, **Credits Used**, **Overage Credits**: volume for the month from the activity report. Overage Credits is consumption beyond the plan allocation, which is billed at a higher rate than in-plan credits.
+  **Active Users by Client Type**: distinct users who appear in the activity report, split across `KIRO_IDE`, `KIRO_CLI`, and `PLUGIN`. Use it to see which surfaces adoption is actually happening on.
+  **Daily Active Users by Client Type**: the same population broken down by day, which shows whether usage is steady or concentrated in bursts.
+  **Credits by Subscription Tier**: where consumption sits across Pro, ProPlus, ProMax, and Power. Read alongside the tier recommendations on the next tab.
+  **Messages by Model**: which models drive the most activity.
This tab is where you decide what to do about individual licences. The **User Summary** pivot handles people who are using Kiro, and the **Idle Kiro Licences** table handles the ones who are not.  
+  **Users by Message Count** and **Top 50 Users by Message Count**: identify your heaviest users and likely internal champions. The Top 50 chart colors each bar by model, so you can also see whose work depends on which model.
+  **User Summary**: one row per user per month, with total messages, credits used, plan credits, monthly utilization percentage, credits per message, and a tier recommendation of Upgrade Candidate, Downgrade Candidate, Review Overage Settings, or Right-Sized. Because plan credits reset monthly, select a single month for these figures to be meaningful.
+  **Idle Kiro Licences**: licences on the selected month’s bill that consumed no credits during it, which matches the Idle Kiro Licences KPI on the Executive Summary. Read it left to right as a case for or against reclaiming each licence:
  +  **Licence Since** and **Last Activity**: when the licence first appeared on a bill, and the last day any credits were consumed on it. Both are all-time and can fall outside the selected month. A blank Last Activity means the licence has never been used at all, which makes it the most reclaimable kind.
  +  **Months Active**: how long the person used Kiro before going quiet. This is the column that prevents over-reacting. Somebody productive for a year who has been quiet for two months, perhaps on parental leave or between projects, is a different case from a licence barely touched since it was bought.
  +  **Months Idle**: whole calendar months of no credit consumption, measured to the last day of the selected period.
  +  **Monthly Fee** and **Inactivity Cost**: what the licence costs per month, taken from what CUR actually charged rather than from a price list, and Months Idle multiplied by that fee. Inactivity Cost is cumulative across the whole idle stretch rather than for the selected month alone, so a licence idle since March shows six months of fees in a September review, not one.
This tab is about whether individual users are on the right plan. The three KPIs mark out the two ends of the utilization range, and the pivot shows who sits where.  
+  **Users at Risk**: users at or above 75% of their monthly plan credits. They are on course to exceed their plan.
+  **Users in Overage**: users who have already exceeded it and are consuming credits at the overage rate.
+  **Users Below 25% of Plan**: users who consumed less than a quarter of their allowance. Treat this list differently from the idle licences: low credit consumption is not the same as low productivity, since an experienced developer can be effective on very few credits. Share it with the relevant team managers to judge whether Kiro is landing, rather than acting on it directly.
+  **Daily Credits Used vs Overage**: daily burn rate with the overage portion stacked on top, which shows when in the month users cross their plan limit.
+  **Monthly Credits and Overage by User**: per-user detail behind the three KPIs, with plan credits, credits used, utilization percentage, overage credits, and the tier recommendation.
This tab describes how developers work rather than what it costs. Use it when choosing which models to make available, or when sizing the impact of a model deprecation.  
+  **Daily Messages by Model**: a stacked bar chart of model popularity over time.
+  **Monthly Messages by Model and Client Type**: message volumes and distinct user counts grouped by model, client type, and subscription tier.
This tab reports **messages**, not credits. The Kiro activity report writes a user’s daily credit total on a single one of that user’s model rows rather than splitting it per model, so credits cannot be attributed to an individual model from this data source. Any per-model credit figure would report which row happened to carry the total, not which model spent it.

### How licences are counted
<a name="how-licences-are-counted"></a>

One licence is **one subscriber within one AWS account**, identified by the IAM Identity Center user ID in the CUR line item resource ID, paired with the account that is billed for it.

This matters when the same person is subscribed in more than one account, which happens in organizations that run separate AWS accounts per team or per environment. That person holds two licences, is billed twice, and either licence can go idle and be reclaimed independently of the other. Counting distinct subscribers instead would collapse the two into one and hide the wasted spend, so the subscription KPIs count the pair and a single person can legitimately appear twice in the Idle Kiro Licences table under different accounts.

Grouping only by subscriber has the same effect inside the idle table: if a person works in one account and lets the licence in a second account sit unused, the active account’s last-activity date would mask the abandoned licence. All of the idle calculations are therefore evaluated per account and subscriber together.

## Calculated Fields Reference
<a name="calculated-fields-reference"></a>

### Activity dataset
<a name="activity-dataset"></a>

Fields derived from the Kiro user activity report, which is one row per user per day per model:


| Field | Logic | Purpose | 
| --- | --- | --- | 
|  `usage_date`  |  `parseDate({date}, "yyyy-MM-dd")`  | Date type for time-series, and the column the Billing period control filters on | 
|  `user`  | Email if available, cleaned userid otherwise | Human-readable display | 
|  `plan_credits`  | Pro=1000, ProPlus=2000, ProMax=5000, Power=10000, Free=50 | Plan allocation for the tier on that row | 
|  `plan_utilization_pct`  |  `credits_used / plan_credits`  | Per-day utilization (not used directly by the pivots; see `monthly_plan_utilization_pct`) | 
|  `in_overage_flag`  | 1 if overage\_credits > 0 | Overage counter | 
|  `credits_per_message`  |  `credits_used / total_messages`  | Efficiency metric | 
|  `is_new_user`  | 1 if new\_user = true | Adoption counter | 
|  `monthly_plan_credits`  | The highest plan allocation the licence held during the calendar month (analysis-level) | The month’s effective allowance, resolved to a single figure for a licence that changed tier mid-month | 
|  `monthly_tier`  | The tier matching `monthly_plan_credits`  | The tier label to group by for any monthly figure, so a licence that changed tier mid-month appears once | 
|  `monthly_plan_utilization_pct`  | Cumulative monthly credits per user / `monthly_plan_credits` (analysis-level, aggregated over the calendar month) | Monthly utilization, the basis for utilization %, at-risk, under-utilization, and tier recommendations | 
|  `monthly_overage_credits`  | Sum of a user’s overage credits over the calendar month (analysis-level) | Monthly overage total | 
|  `monthly_credits_per_message`  | Monthly credits summed, divided by monthly messages summed, per user | Efficiency metric at monthly grain. Averaging the per-row ratio instead understates it, because the activity report writes a user’s daily credit total on one model row only | 
|  `at_risk_flag`  | 1 if monthly utilization >= 75%, for a recognized tier | Risk threshold. Requires a known plan allocation, so an unrecognized tier is excluded rather than silently counted as 0% and dropped from the at-risk count | 
|  `underutilized_flag`  | 1 if monthly utilization < 25%, for a recognized tier | Under-utilization threshold. Requires a known plan allocation, so a tier the dashboard does not recognize is excluded rather than reported as unused | 
|  `tier_recommendation_monthly`  | No known plan allocation gives Unknown Tier; else any monthly overage gives Upgrade Candidate (or Review Overage Settings if already on Power, the top tier); else monthly utilization below 30% on a tier above Pro gives Downgrade Candidate; else Right-Sized | Tier optimization, evaluated on monthly rather than per-day usage | 

**Note**  
 `tier_key` and the tier spellings. The subscription tier is normalized once into a `tier_key` column, lowercased with underscores, hyphens and spaces removed, and every comparison matches on that rather than on the raw `Subscription_Tier` value.  
This is deliberate rather than defensive. Kiro spells the same tier differently depending on where you read it: the activity report writes `PRO_PLUS` and `PRO_MAX`, the CUR line item usage type uses `KiroEnterprise-ProPlus`, and the Kiro documentation gives `ProPlus` and `ProMax`. Matching any single spelling means the other two fall through to a zero plan allowance. Normalizing accepts all of them.  
A tier with no known allowance reports `Unknown Tier` and is excluded from the at-risk and under-utilization counts, rather than being reported as 0% utilized.

### Subscription dataset
<a name="subscription-dataset"></a>

Fields derived from CUR, evaluated per account and subscriber together. Except where noted, all of them are scoped to the selected **Billing period**:


| Field | Logic | Purpose | 
| --- | --- | --- | 
|  `subscription_key`  |  `account_id` and `resource_id` combined | The unit of licence counting. See [How licences are counted](#how-licences-are-counted)  | 
|  `period_total_cost`  | Every Kiro charge for the licence in the period, whatever the billing operation | Defines the roster: a licence with no charge in the month is not on that month’s bill. Deliberately unfiltered, so a charge under an unrecognized billing operation cannot remove the licence from the Total, Active and Idle counts | 
|  `period_subscription_cost`  | Subscription fee charges only | The basis for `monthly_fee`, kept separate from the roster above | 
|  `period_active_flag`  | 1 if the licence consumed credits in the period, according to the Kiro activity report **or** a billing record | Defines active. Credit consumption included in a subscription does not always produce a billing record, so billing alone cannot answer this | 
|  `inactive_in_period`  |  `period_total_cost > 0` and `period_active_flag = 0`  | The idle test, and the filter behind the Idle Kiro Licences KPI and table | 
|  `last_activity_date`  | Newest credit-consumption date for the licence, **all-time**, from the activity report or a billing record | Last Activity column. Not scoped to the period, so it can show later activity for a licence that was idle during the month under review | 
|  `first_billed_date`  | Oldest fee line date for the licence, **all-time**  | Licence Since column, and the starting point for a licence that has never consumed credits | 
|  `monthly_fee`  | Subscription cost divided by the number of distinct months billed in the period | What the licence costs per month, taken from actual charges so tier changes, discounts, and private pricing are all reflected without maintaining a price list | 
|  `months_idle`  | Whole calendar months from the last activity to the end of the selected period | Months Idle column, and the multiplier for Inactivity Cost | 
|  `months_active`  | Months licensed minus months idle | Months Active column: how long the person used Kiro before going quiet | 
|  `inactivity_cost`  |  `monthly_fee` multiplied by `months_idle`  | Inactivity Cost column: what the idle months have cost, cumulatively rather than for the selected month alone | 

**Note**  
Utilization, at-risk, under-utilization, and tier-recommendation logic all evaluate usage over the **calendar month**, because Kiro plan credits are allocated and reset per calendar month. The subscription and idle fields are scoped to the selected month for the same reason. Set the **Billing period** control to a full calendar month when reviewing any of these metrics.  
Two consequences are worth knowing when reading the idle table:  
 **Months Active and Licence Since are bounded by data retention.** The subscription view keeps 18 months of CUR, so a licence bought before that shows the oldest date available rather than its true start, and Months Active reads as a minimum rather than an exact tenure. Several licences sharing the same Licence Since date is the signal that you are at that boundary.
 **A licence that was idle in the month under review but has since been used again** reports the selected period as its idle span, not the true gap. The figure is a floor, and the Last Activity column shows the later date so the licence is not reclaimed by mistake.

## Update
<a name="update"></a>

When a new version of the dashboard template is released, update your dashboard by running the following command:

```
cid-cmd update --dashboard-id kiro-user-activity
```

## Teardown
<a name="teardown"></a>

To remove the Kiro User Activity module:

1. Delete the Quick Suite dashboard and dataset via the Quick Suite console or `cid-cmd delete --dashboard-id kiro-user-activity`.

1.  [Update](data-collection-update.md) the Data Collection Stack and set **Include Kiro User Activity Data Collection Module** back to `no`. This removes the collection Lambda, EventBridge Scheduler schedule, and Glue table.

1. (Optional) Remove the bucket policy statements from source accounts.

1. (Optional) Delete collected data from `s3://<dest-bucket>/kiro-user-activity/`.
**Note**  
If you migrated from an earlier, replication-based version of this module, the destination bucket might also contain a legacy `s3://<dest-bucket>/kiro/` prefix (the raw replication landing zone) and an AWS Glue crawler. These are not used by the current pull-based architecture. After confirming no Glue table still references the `kiro/` prefix, you can delete that data and remove the crawler.

## Authors
<a name="authors"></a>
+ Darius Seroka, Senior Technical Account Manager

## Contributors
<a name="contributors"></a>
+ Yuriy Prykhodko, Principal Technical Account Manager
+ Eric Christensen, Senior Technical Account Manager

## Feedback & Support
<a name="kiro-user-activity-dashboard-feedback-support"></a>

For feedback and support, see the [Feedback and Support](feedback-support.md) guide.

**Note**  
These dashboards and their content: (a) are for informational purposes only, (b) represent current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS content, products or services are provided "as is" without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers.