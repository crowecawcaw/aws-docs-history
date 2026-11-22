

# Understand CloudWatch Omni pricing

This topic explains how ingestion, centralization, storage, and queries are charged when you use CloudWatch Omni, how the Omni query allowance is calculated and applied, how the free trial credit works, and how to review these charges on your bill. For list prices, see the [CloudWatch Omni pricing page](https://aws.amazon.com/cloudwatch/omni/pricing/).

## Omni pricing at a glance
<a name="omni-understand-pricing-at-a-glance"></a>

CloudWatch Omni works on the telemetry that you already send to CloudWatch. Ingestion and storage are charged at standard CloudWatch rates. Omni charges apply only to logs and traces queries that exceed your Omni query allowance, and to PromQL queries that run through the API or in alerts. Prices on this page are for US East (N. Virginia). For pricing in other Regions, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).


| Activity | What it is | How it is charged | 
| --- | --- | --- | 
| Ingestion | Logs, metrics, and spans that you send to CloudWatch from your applications, infrastructure, AWS services, and OpenTelemetry sources. Omni uses this telemetry as is, without re-instrumentation. | Standard CloudWatch ingestion rates | 
| Centralization | For cross-account and cross-Region observability, Omni recommends that you create CloudWatch centralization rules to copy telemetry from your source accounts and Regions into the account that hosts your space. See [Set up Omni for your organization](omni-set-up-omni-for-your-organization.md). | No ingestion charge for the first centralized copy in the destination account. Each additional copy is charged at $0.05 per GB. Storage and query charges apply separately, to every copy. | 
| Storage | Logs and spans retained in CloudWatch for the retention period that you set. Omni queries this data where it is stored and does not keep an additional copy. | Standard CloudWatch storage rates, based on retention | 
| Logs and traces queries | SQL queries that scan your logs and traces, from the Omni console, dashboards, alerts, the Omni agent, the API, coding agents, the AWS DevOps Agent, or the IDE extension in cloud mode. | No charge up to 5× your monthly log and span ingestion volume. Data scanned above the allowance is charged at $0.005 per GB. | 
| PromQL metrics queries | Prometheus Query Language (PromQL) queries on your metrics. | No charge in the Omni console. Queries through the API and in alerts are charged at $0.01 per million samples scanned. | 
| Dashboards, alerts, and the Omni agent | Shared views of your systems, notifications when a condition you define is met, and Omni's built-in AI assistant, which answers questions from your telemetry. | Included at no additional charge, within [service quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_limits.html#CloudWatch-Omni-quotas). The logs and traces queries that they run count toward your allowance, and PromQL alert queries are charged at $0.01 per million samples scanned. | 
| Agent evaluations | Scoring of your AI agents' responses with built-in or custom evaluators, continuously in production or on demand against a dataset. | Charged at [Amazon Bedrock AgentCore Evaluations rates](https://aws.amazon.com/bedrock/agentcore/pricing/) | 

## Ingestion and centralization
<a name="omni-understand-pricing-ingestion"></a>

Telemetry is charged when it is ingested into CloudWatch, at standard CloudWatch rates. Enabling Omni does not change these rates. Prices below are for US East (N. Virginia). For pricing in other Regions, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).


| Telemetry | Ingestion rate | 
| --- | --- | 
| Application and custom logs | $0.50 per GB | 
| OpenTelemetry metrics | $0.50 per GB ($0.08 per GB for Amazon EKS Container Insights) | 
| Vended logs (AWS service logs) | $0.50 to $0.05 per GB, tiered by volume | 
| Spans | $0.35 to $0.15 per GB, tiered by volume | 

Volume tiers for vended logs and spans apply per payer account, per Region, per month. Existing CloudWatch Free Tier allowances continue to apply.

### Centralization
<a name="omni-understand-pricing-centralization"></a>

Many organizations copy telemetry from multiple source accounts into one central account and use Omni in that account. The following table shows how centralized copies are charged.


| Part of the setup | How it is charged | 
| --- | --- | 
| Ingestion in the source accounts | Charged once, at standard CloudWatch ingestion rates | 
| First centralized copy | No ingestion charge for the first centralized copy in the destination account | 
| Each additional copy, such as a backup in another Region | Charged at $0.05 per GB | 
| Storage and queries, for every copy | Charged separately from ingestion. Storage is charged for each copy based on its retention, and queries are charged in the account where they run. | 

Centralizing telemetry across Regions does not incur cross-Region data transfer charges.

![Accounts under one payer account. Source accounts 1, 2, and 3 ingest 10 TB, 8 TB, and 2 TB, at standard CloudWatch ingestion rates with storage charged per retention. Source account 1 runs queries that scan 10 TB, and source accounts 2 and 3 run no queries. A centralization rule copies the data to the central account that hosts the Omni space, with no charge for the first copy. The central account has no ingestion of its own, pays storage per retention, and runs queries that scan 90 TB. An additional copy to a backup in another Region is charged at $0.05 per GB, plus storage per retention. The Omni query allowance is (10 + 8 + 2) TB × 5 = 100 TB, pooled across all accounts under the payer account. It applies to queries in any account, including the central account, and centralized copies do not add to it. 10 TB plus 90 TB of queries equals 100 TB, so no query charges apply.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-pricing-hub-and-spoke.png)

Where each charge applies in a hub-and-spoke setup. Illustrative volumes.


For storage of centralized copies, see [Storage for centralized copies](#omni-understand-pricing-storage-centralized). For queries in a central account, see [Queries in a central account](#omni-understand-pricing-central-account).

## Storage
<a name="omni-understand-pricing-storage"></a>

Telemetry stored in CloudWatch is charged per GB-month of compressed data, based on the retention period that you set. Omni does not store an additional copy of your telemetry, so enabling Omni does not add storage charges. Prices below are for US East (N. Virginia). For pricing in other Regions, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).


| Storage tier | Rate per GB-month | When data is in this tier | 
| --- | --- | --- | 
| Standard (default) | $0.030 | Newly ingested, or accessed in the last 30 days | 
| Infrequent Access (Intelligent Tiering) | $0.018 | Not accessed for 30 days | 
| Archive Instant Access (Intelligent Tiering) | $0.006 | Not accessed for 90 days | 

Intelligent Tiering rates apply to accounts with Intelligent Tiering enabled. Storage for OpenTelemetry metrics is included in the metrics ingestion rate.

### Storage for centralized copies
<a name="omni-understand-pricing-storage-centralized"></a>

Storage charges apply to each copy, including the first centralized copy, based on the retention period that you set for it. To reduce storage charges, consider a shorter retention period in the source accounts when you query from the central account.

## Queries and the Omni query allowance
<a name="omni-understand-pricing-query-allowance"></a>

Each month, logs and traces queries can scan up to five times your eligible log and span ingestion volume at no charge. Data scanned above the allowance is charged at $0.005 per GB.

### What counts toward the allowance
<a name="omni-understand-pricing-eligible-ingestion"></a>


| Counts | Usage types on your bill | 
| --- | --- | 
| Application and custom logs, in any log class | DataProcessing-Bytes, DataProcessingIA-Bytes | 
| OpenTelemetry logs | DataProcessingOtel-Bytes, DataProcessingOtelIA-Bytes | 
| Vended logs delivered to CloudWatch Logs, including AWS WAF, Amazon CloudFront, and AWS Elemental MediaTailor logs | VendedLog-Bytes, VendedLogIA-Bytes, and their variants | 
| Spans | Application-Signals-Bytes | 

Vended logs count toward the allowance even when their ingestion is discounted under another service's offer, such as the AWS WAF logs included with WAF requests.

### What does not count
<a name="omni-understand-pricing-not-counted"></a>
+ **Metrics.** Metric ingestion does not count toward the allowance, and the allowance does not apply to PromQL queries.
+ **Centralized copies of logs.** Data counts once, when it is first ingested in the source account. Centralized copies are not counted as ingestion.
+ **Logs delivered to Amazon S3 or Amazon Data Firehose.** Only logs ingested into CloudWatch Logs count toward the allowance.

### The allowance is shared across your organization
<a name="omni-understand-pricing-shared-allowance"></a>

The query allowance is calculated on the combined eligible ingestion of all accounts under your payer account, whether or not Omni is enabled in each account. If Omni is enabled in only one account, queries in that account can use the allowance from ingestion across all accounts under the payer account. The allowance resets at the start of each month, and unused allowance does not carry over.

On your bill, the allowance is applied first to queries in the accounts that generated the ingestion. Any remaining allowance is then applied to queries in other accounts under the same payer account.

### Queries in a central account
<a name="omni-understand-pricing-central-account"></a>

Omni queries are charged in the account where they run. Centralized copies do not add to the Omni query allowance. The Omni query allowance from ingestion in the source accounts applies to queries that run in any account under the same payer account, including the central account. For example, 28 TB of logs and spans ingested in the source accounts provides a 140 TB Omni query allowance.

**Note**  
**Example: one central account that only runs queries**  
Three workload accounts ingest 10 TB, 8 TB, and 2 TB of logs and spans in a month. The query allowance for the payer account is (10 \+ 8 \+ 2) × 5 = 100 TB. A central security account has no ingestion of its own and runs queries that scan 90 TB. Workload account 1 runs queries that scan 10 TB.  
The allowance is applied first to workload account 1, which generated 50 TB of allowance and scans 10 TB.
The remaining 90 TB of allowance is applied to the central account's 90 TB of queries.
No query charges apply.
If the central account scanned 120 TB instead, 30 TB would exceed the allowance and would be charged at 30,000 GB × $0.005 = $150.

### How queries are charged, by where they run
<a name="omni-understand-pricing-where-queries-run"></a>

Logs and traces queries are charged the same way wherever they run: they count toward your allowance, and data scanned above the allowance is charged at $0.005 per GB. PromQL charges depend on where the query runs.


<table>
<thead>
  <tr><th>Where the query runs</th><th>Logs and traces (SQL)</th><th>Metrics (PromQL)</th></tr>
</thead>
<tbody>
  <tr><td>Omni console</td><td>Allowance, then $0.005/GB</td><td>No charge</td></tr>
  <tr><td>Omni dashboards</td><td>No charge per dashboard. You pay only for the data its queries scan: allowance, then $0.005/GB.</td><td>No charge</td></tr>
  <tr><td>Omni alerts</td><td>No charge per alert. You pay only for the data its query scans: allowance, then $0.005/GB.</td><td>No charge per alert. Each evaluation is charged at $0.01 per million samples scanned.</td></tr>
  <tr><td>The Omni agent (built-in AI assistant)</td><td>Allowance, then $0.005/GB. Queries that the agent runs count toward scan volume.</td><td>No charge</td></tr>
  <tr><td>API, CLI, and SDKs</td><td>Allowance, then $0.005/GB</td><td>$0.01 per million samples</td></tr>
  <tr><td>Coding agents using Omni skills</td><td>Allowance, then $0.005/GB</td><td>$0.01 per million samples</td></tr>
  <tr><td>AWS DevOps Agent investigations</td><td>Allowance, then $0.005/GB</td><td>$0.01 per million samples</td></tr>
  <tr><td>IDE extension, local mode</td><td colspan="2">No CloudWatch charges apply. Traces are stored on your machine.</td></tr>
  <tr><td>IDE extension, cloud mode</td><td>Trace queries use your allowance, then $0.005/GB</td><td>Not applicable. The IDE extension does not run PromQL queries.</td></tr>
</tbody>
</table>


### Developing an agent in your IDE
<a name="omni-understand-pricing-ide"></a>

The CloudWatch Omni IDE extension has two modes. In local mode, traces from test runs are written to your project folder and are not sent to CloudWatch, so no CloudWatch charges apply. Model invocations that your agent makes during local testing are charged by your model provider. In cloud mode, the extension reads traces from your deployed agents, and those queries count toward your allowance the same as other logs and traces queries. Evaluations run from the IDE extension are charged at AgentCore Evaluations rates. See [Develop with the IDE extension](omni-develop-with-the-ide-extension.md).

## The $1,000 free trial credit
<a name="omni-understand-pricing-free-trial-credit"></a>
+ A $1,000 credit is applied automatically when Omni is enabled, and is valid for 30 days.
+ The credit is applied to the account where Omni is enabled. If [credit sharing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/useconsolidatedbilling-credits.html) is turned on for your organization, the credit can apply to charges in other accounts under the same payer account.
+ The credit applies to OpenTelemetry log ingestion, OpenTelemetry metrics, and Application Signals spans. It does not apply to query charges or to other log ingestion.
+ Up to 10 accounts in an AWS Organization can receive the credit.
+ Not all accounts are eligible. Check eligibility in the CloudWatch console when you enable Omni.
+ After the credit is used or expires, standard rates apply and Omni remains enabled.

The trial credit and the query allowance are separate. The credit is a one-time offer that applies to ingestion. The allowance is an ongoing monthly benefit that applies to queries.

**Note**  
**Hub-and-spoke example.** Omni is enabled in a central monitoring account, and OpenTelemetry data is ingested in the source accounts. The credit is applied to the central account. With credit sharing turned on, the credit can apply to OpenTelemetry ingestion charges in the source accounts. Without credit sharing, the credit applies only to OpenTelemetry ingestion charges in the central account.

## How to review Omni charges on your bill
<a name="omni-understand-pricing-review-your-bill"></a>

### Omni usage types in Cost Explorer
<a name="omni-understand-pricing-usage-types"></a>

The following usage types show your Omni-related charges in AWS Cost Explorer and the AWS Cost and Usage Report. Each usage type begins with a Region code, for example `USE1-Omni-DataScanned-Bytes` for US East (N. Virginia).


| Usage type | What it measures | How it is charged | 
| --- | --- | --- | 
| Omni-DataScanned-Bytes | Logs and traces data scanned by Omni queries, from any surface | Charged at $0.005 per GB above the query allowance. The allowance appears as Bundled Discount against this usage type. | 
| CW:PromQL:SamplesScanned | Samples scanned by PromQL queries that run through the API or in alerts | Charged at $0.01 per million samples. PromQL queries in the Omni console are not charged. | 
| CentralizedBytes (logs), CW:CentralizedBytes (metrics) | Telemetry copied by centralization rules | No ingestion charge for the first centralized copy in the destination account. Each additional copy is charged at $0.05 per GB. Storage and query charges apply separately, to every copy. | 
| DataProcessing-Bytes, VendedLog-Bytes, Application-Signals-Bytes, and their variants | Log and span ingestion | Standard CloudWatch ingestion rates. This ingestion sets your query allowance. For the full list, see [What counts toward the allowance](#omni-understand-pricing-eligible-ingestion). | 
| DataProcessingOtel-Bytes, DataProcessingOtelIA-Bytes, DataProcessingOtelEss-Bytes, CW:OTEL:Bytes, Application-Signals-Bytes | OpenTelemetry log, OpenTelemetry metric, and span ingestion | Standard CloudWatch ingestion rates. The free trial credit applies to these usage types and appears as Credit. | 
| XRay-Spans-Indexed | Spans indexed as X-Ray trace summaries | The first 1% of ingested spans is indexed at no charge. Indexing above that is charged per million trace summaries. | 

### Review your query allowance
<a name="omni-understand-pricing-review-allowance"></a>

To review your query allowance, complete the following steps:

1. Sign in to your **payer (management) account**. The allowance is shared across accounts, so a single linked account shows only part of the picture.

1. Open AWS Cost Explorer. Filter **Service** to CloudWatch and **Usage type** to the eligible usage types listed in [What counts toward the allowance](#omni-understand-pricing-eligible-ingestion).

1. Add up that ingestion for the month and multiply by five. The result is your allowance in GB.

1. Change the **Usage type** filter to `Omni-DataScanned-Bytes`, and group by **Linked account** and **Charge type**.

1. The allowance appears as **Bundled Discount**. Compare the total Bundled Discount across all accounts with your allowance.

### Example scenario: how the query allowance is applied across accounts
<a name="omni-understand-pricing-example-bill"></a>

The following example scenario uses the hub-and-spoke setup from [Queries in a central account](#omni-understand-pricing-central-account). It shows how the query allowance is applied to each account under the same payer account.


| Linked account | Eligible ingestion | Allowance generated | Data scanned | Query charge before allowance | Allowance applied | Net charge | 
| --- | --- | --- | --- | --- | --- | --- | 
| Source account 1 | 10 TB | 50 TB | 10,000 GB | $50.00 | −$50.00 | $0.00 | 
| Source account 2 | 8 TB | 40 TB | 0 GB | $0.00 | $0.00 | $0.00 | 
| Source account 3 | 2 TB | 10 TB | 0 GB | $0.00 | $0.00 | $0.00 | 
| Central account | 0 TB | 0 TB | 90,000 GB | $450.00 | −$450.00 | $0.00 | 
| Payer account total | 20 TB | 100 TB | 100,000 GB | $500.00 | −$500.00 | $0.00 | 

**Note**  
**How to read this example**  
The central account has no ingestion of its own, but −$450.00 of allowance is applied to its queries. Its queries use allowance generated by the source accounts.
Source account 1 generated 50 TB of allowance but had allowance applied only to the 10 TB that it scanned. The rest of its allowance was applied to the central account.
Source accounts 2 and 3 have no allowance applied because they ran no queries. Their allowance was applied to the central account.
To confirm that the full allowance was applied, compare the total allowance applied across all accounts with five times your total eligible ingestion.

Final charges are calculated when your monthly bill closes. During the month, Cost Explorer shows estimated charges, which might differ from your final bill. An individual linked account might appear to reach its allowance partway through the month, even when allowance remains at the payer account level.

### Review your trial credit
<a name="omni-understand-pricing-review-credit"></a>

In Cost Explorer, group by **Charge type** and look for **Credit** on the OpenTelemetry and Application Signals usage types.

### In the Cost and Usage Report
<a name="omni-understand-pricing-cur"></a>

Query scans appear as `Omni-DataScanned-Bytes` usage. The allowance appears as a bundled discount line item against that usage, and the trial credit appears as a credit line item.

## Managing query charges
<a name="omni-understand-pricing-manage-query-charges"></a>
+ **Run PromQL queries in the Omni console** when possible. PromQL queries in the console are not charged.
+ **Set dashboard refresh intervals to 5 minutes or longer.** Each refresh runs the dashboard queries again.
+ **Narrow the time range and filters of your queries.** Queries are charged for data scanned, not for rows returned.
+ **Use local mode in the IDE extension** while you build and test agents.
+ **Create an AWS Budgets alert** on the `Omni-DataScanned-Bytes` usage type to get notified when query charges exceed the allowance.
+ **Plan for agents and automation that query through the API.** Their logs and traces queries count toward the shared allowance, and their PromQL queries are charged.

## FAQs
<a name="omni-understand-pricing-faq"></a>

Is the allowance calculated per account?  
No. The allowance is calculated across all accounts under your payer account, and is applied first to the accounts that generated the ingestion.

Do I need to enable Omni in every account for its ingestion to count?  
No. Ingestion in all accounts under your payer account counts, whether or not Omni is enabled in each account.

Do centralized copies add to my allowance?  
No. Data counts once, when it is first ingested in the source account.

Does the allowance cover PromQL?  
No. The allowance applies to logs and traces queries. PromQL queries are not charged in the Omni console, and are charged through the API and in alerts.

Does the free trial credit apply to query charges?  
No. The credit applies only to OpenTelemetry and Application Signals ingestion.

Does unused allowance carry over?  
No. The allowance resets at the start of each month.

Why does one of my accounts show only a partial discount?  
The allowance is shared across all accounts under your payer account. Review the total from the payer account, using the closed monthly bill.

Can I see how much each query or each user scanned?  
Not after a query completes. Bytes scanned are available for a query while it runs, and total scan volume for each account is available on your bill.

Can I get custom or volume pricing?  
Yes. Contact your AWS account team.