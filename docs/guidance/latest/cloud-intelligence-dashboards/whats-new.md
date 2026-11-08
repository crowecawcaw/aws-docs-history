

# What's new
<a name="whats-new"></a>

## Overview
<a name="overview"></a>

This page summarizes the most notable recent changes across the Cloud Intelligence Dashboards (CID) framework — new dashboards, major features, and tooling updates. For the complete, per-dashboard history, see the [changelogs](#whats-new-changelogs) at the bottom of this page.

## Stay up to date with the CID RSS feed
<a name="whats-new-rss"></a>

Subscribe to the RSS feed to get notified about new releases automatically: [cloud-intelligence-dashboards.rss](https://cid.workshops.aws.dev/feed/cloud-intelligence-dashboards.rss) 

## Recent highlights
<a name="whats-new-highlights"></a>

The highlights below cover notable releases from the past year, most recent first.

## DROID Dashboard v1.0.0: new dashboard for Amazon RDS and Amazon Aurora (November 3, 2026)
<a name="whats-new-droid-100"></a>

A new dashboard, Database Resilience, Operations, and Insights (DROID), gives you a single view of your Amazon RDS and Amazon Aurora fleet across accounts and Regions.
+  **Inventory** — instances and clusters by account, Region, engine, instance class, and processor (Graviton or x86), with filters for collection date, account, Region, engine, and tags.
+  **Version and maintenance** — current engine versions compared with the latest available, standard and extended support end dates, and pending maintenance actions.
+  **Security and resiliency** — encryption, Multi-AZ, deletion protection, storage autoscaling, and certificate expiration.
+  **Backup** — daily, 14-day, and 30-day backup coverage, and cluster snapshot analysis.
+  **Cost** — RDS spend by account, Region, engine, and instance type, and Aurora I/O-Optimized recommendations based on estimated savings.

Requires CUR 2.0 and CID Data Collection v3.14.11 or later with the Inventory, Reference, and RDS modules enabled.

See the [DROID Dashboard](droid-dashboard.md), or explore the [interactive demo dashboard](https://cid.workshops.aws.dev/demo?dashboard=droid).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-droid.md).

## Data Collection v3.14.11: RDS module and new price lists (November 3, 2026)
<a name="whats-new-data-collection-3-14-11"></a>
+  **RDS module** — a new module that collects Amazon RDS and Amazon Aurora pending maintenance actions and cluster snapshots across accounts, for the [DROID Dashboard](droid-dashboard.md). It requires the Inventory and Reference modules.
+  **Pricing** — new price lists for Database Savings Plans, Amazon Redshift, Amazon EKS, Amazon EMR, Amazon ECS, Amazon MSK, Amazon DocumentDB, Amazon MemoryDB, Amazon Neptune, and Amazon SageMaker AI.
+  **Fixes** — the `inventory_ec2_instances_data` table no longer fails every Athena query with `HIVE_SERDE_NOT_FOUND`, and the CUR crawler can create its CloudWatch log group.

See [Update the Data Collection framework](data-collection-update.md).

View the [release notes](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-data-collection/releases/tag/3.14.11).

## Data Exports v0.13.0: new CUR 2.0 columns (November 3, 2026)
<a name="whats-new-data-exports-0130"></a>
+  **CUR 2.0 table** — added the `net_*` columns and other columns, such as `line_item_net_unblended_cost`, `pricing_public_on_demand_rate`, `product_region_code`, and `product_sku`.
+  **Crawler logs** — the crawler role can create its log group by log group ARN, ahead of the CloudWatch Logs IAM change in April 2027.
+  **Secondary destination bucket** — fixed `SecondaryDestinationBucket`, which stopped receiving data in v0.11.0. If you use it, follow the upgrade note in the changelog.

See [Data Exports](data-exports.md).

View the [changelog](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-data-collection/blob/main/data-exports/CHANGELOG.md).

## Extended Support Cost Projection v5.3.0: Database Savings Plans coverage (November 2, 2026)
<a name="whats-new-extended-support-530"></a>
+  **Database Savings Plans coverage** — the RDS view now includes usage covered by Savings Plans, so RDS and Aurora resources in Extended Support that are covered by Database Savings Plans are no longer missing.
+  **More robust RDS view** — the view no longer fails when a line item has a non-numeric vCPU value. Such rows are kept, with no vCPU-based cost.
+  **New data preparation experience** — the RDS, EKS, OpenSearch, ElastiCache, and tagging datasets are migrated to the new Amazon Quick data preparation experience. Visuals and calculations are unchanged.

This update requires `cid-cmd` v4.4.12 or later. If you customized the datasets, make a copy before you update. Run the update with `--recursive`; without it, only the dashboard is updated and the datasets are not migrated: `cid-cmd update --dashboard-id extended-support-cost-projection --recursive`.

See the [Extended Support Cost Projection Dashboard](extended-support.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-extended-support-cost-projection.md).

## Graviton Savings Dashboard v3.0.6: Database Savings Plans support (October 27, 2026)
<a name="whats-new-graviton-savings-306"></a>
+  **Database Savings Plans** — RDS, OpenSearch, and ElastiCache recognize Database Savings Plan coverage and price covered usage at its effective rate, so covered Graviton resources are no longer missing from the scan or priced at On-Demand.
+  **Savings accuracy** — ElastiCache and OpenSearch **Current Unit Cost** and **Existing Savings %** now use amortized cost, and a new `graviton_unit_cost` column shows the per-unit Graviton rate.
+  **Fixes** — OpenSearch Gen7 (m7g and r7g) rows no longer show blank unit cost and savings, and cost is no longer double-counted for OpenSearch domains and ElastiCache clusters that report more than one engine version.

Requires the Database Savings Plans price list from the Data Collection pricing module (v3.14.11 or later). After you update Data Collection, run `cid-cmd update --dashboard-id graviton-savings --force --recursive`.

See the [Graviton Savings Dashboard](graviton-savings-dashboard.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-graviton-savings.md).

## Data Collection v3.14.10: Health Events Lambda timeout controls (October 20, 2026)
<a name="whats-new-data-collection-3-14-10"></a>

Update to fix Health Events data collection Lambda time out edge cases.
+  **Smaller default batch size** — the detail Step Function now sends 100 events to each Lambda invocation instead of 500. Set `EVENTS_PER_BATCH` on the Lambda to change this if you encounter Lambda timeout errors during data collection.
+  **Optional limit on affected resources per event** — for events with very large numbers of affected resources, where data collection might time out, `MAX_LIST_SIZE` limits the resources retrieved. By default there is no limit. Events and affected accounts are never dropped. A truncated event shows a `WARNING: Entity list truncated` resource on the dashboard, and you can see the full list in the AWS Health console.
+  **Easier debugging** — with `LOG_LEVEL=DEBUG`, the Lambda logs per-event progress, so you can find the event that times out.

See [Health Events Dashboard troubleshooting](health-events-dashboard.md#health-events-dashboard-lambda-timeout).

View the [release notes on the GitHub website](https://github.com/awslabs/cid-framework/releases).

## CUDOS Dashboard v5.10.0: Redshift RG migration, NAT gateway and DynamoDB backup optimization (October 23, 2026)
<a name="whats-new-cudos-5100"></a>
+  **Amazon Redshift RA3 to RG migration** — a new section on the **Databases** tab tracks adoption of Graviton-based RG instances and estimates the savings of migrating each RA3 cluster. Use the **Purchase Option** and **Incremental Snapshot Size** controls to adjust the estimate.
+  **NAT gateway optimization** — a new section on the **Data Transfer & Networking** tab highlights zonal NAT gateways that receive cross-AZ traffic and compares their current cost with a Regional NAT gateway, which improves resilience and can remove inter-AZ data transfer charges.
+  **DynamoDB backup optimization** — a new section on the **Amazon DynamoDB** tab finds native backups of deleted tables and older backups that are good candidates for cold storage, with estimated savings.
+  **Credits, refunds and discounts** — a new detailed view on the **Executive: Billing Summary** tab.
+  **More accurate usage categories** — usage type groups for databases, Amazon S3, Amazon CloudWatch, Amazon Cognito, AWS WAF, Amazon SageMaker AI, Amazon DynamoDB, Amazon MSK, Amazon EFS and Amazon FSx now cover newer usage types and use the names from the AWS pricing pages. Marketplace charges are split into *Marketplace Usage* and *Marketplace Fees*, and data transfer adds *Regional via Public IP* and *Cloud WAN Data Processed* types.

### See screenshots
<a name="collapsible-section-id-whats-new-cudos-5100"></a>

![Databases tab: Amazon Redshift RA3 to RG migration adoption tracking and potential savings](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/whats-new/cudos-5100-redshift-ra3-to-rg.png)


![Data Transfer and Networking tab: NAT gateways optimization opportunities with Regional NAT savings](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/whats-new/cudos-5100-nat-gateways.png)


![Amazon DynamoDB tab: DynamoDB backup optimization with native backup cost by age and backups to review](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/whats-new/cudos-5100-dynamodb-backups.png)


See the [CUDOS Dashboard](cudos-cid-kpi.md#foundational-cudos-dashboard).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md#cudos---5100).

## cid-cmd v4.4.18: sharing on update, plugin parameters, and CloudFormation fixes (October 9, 2026)
<a name="whats-new-cid-cmd-4418"></a>
+  **More reliable CloudFormation deployments** — dashboards deployed one after another no longer inherit each other’s parameters (such as the row-level security dataset), which could make a dashboard fail to create.
+  **Sharing on update** — `share-with-account yes|no` is now applied when updating a dashboard, so you can grant or revoke access for everyone in the account without recreating the dashboard.
+  **Plugin parameters** — the `cid-plugin.yml` template accepts any `cid-cmd` parameter as JSON (for example a row-level security dataset or resource tags), and unattended deployments use parameter defaults instead of failing.
+  **Fixes** — FOCUS `resource-tags` now produce valid views, dashboard updates skip filters on fields that are not yet in the datasets, and `--on-drift override` replaces views as documented.

To update, run `pip3 install --upgrade cid-cmd`. If you deploy with CloudFormation, update the `cid-cfn` stack to the latest template.

See [Share dashboards](share-dashboards.md).

View the [release notes](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/releases/tag/4.4.18).

## Graviton Savings Dashboard v3.0.5: Graviton5 support (October 2, 2026)
<a name="whats-new-graviton-savings-305"></a>
+  **Graviton5 support** (since v3.0.4) — Graviton5 is now a selectable generation (EC2 M9g/M9gd, C9g/C9gd, R9g/R9gd) across modernization mapping, pricing, and savings, with a new **Potential Graviton5 Base Savings** KPI and Graviton5 columns in the EC2 and Graviton Instance Mapping tables.
+  **More accurate GPU savings** (since v3.0.3) — NVIDIA and AMD GPU families without a Graviton equivalent are no longer mapped to g5g, so they no longer inflate On-Demand eligible savings.
+  **Realized savings in the view** — the EC2 realized Graviton savings figure is now calculated in the Athena view, like potential savings. Displayed numbers are unchanged.

See the [Graviton Savings Dashboard](graviton-savings-dashboard.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-graviton-savings.md).

## Kiro User Activity Dashboard v1.1.1: tier and idle-licence reporting fixes (September 25, 2026)
<a name="whats-new-kiro-user-activity-111"></a>

Update if you have users on Pro Plus or Pro Max, or licences that changed tier mid-month.
+  **Tier reporting for Pro Plus and Pro Max** — the report writes `PRO_PLUS` and `PRO_MAX`, which did not match the tier ladder, so Plan Credits and Plan Utilization read 0, the tier recommendation always read Downgrade Candidate, and Users at Risk under-counted those licences. Subscription Type also showed "monthly-subscription" rather than the tier, and an unrecognized tier now reports Unknown Tier.
+  **Licences in active use were reported idle** — with an Inactivity Cost and a blank Last Activity. Credits included in a subscription do not always produce a billing record, so activity is now read from the Kiro activity report.
+  **A licence that changed tier mid-month appeared twice** — once per tier, with contradictory recommendations. Tier, allowance, and utilization now resolve once per licence-month.

This release changes an Athena view, so update with `--recursive` and refresh SPICE for both datasets.

See the [Kiro User Activity Dashboard](kiro-user-activity-dashboard.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-kiro-user-activity.md).

## Media Services Insights Hub v2.2.2: AWS Elemental MediaConvert add-on analysis (September 18, 2026)
<a name="whats-new-media-services-222"></a>
+  **AWS Elemental MediaConvert** — refined analysis of MediaConvert add-ons.

See the [Media Services Insights Hub](media-services-insights.md).

View the [changelog](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-media-services-insights.md).

## Kiro User Activity Dashboard v1.1.0: licence-level subscription visibility (September 16, 2026)
<a name="whats-new-kiro-user-activity-110"></a>
+  **Licence-centric KPIs** — Total Active and Total Inactive Kiro Users become Active Kiro Licences and Idle Kiro Licences, counted per subscriber **and** account, so the same person subscribed in two accounts holds two independently reclaimable licences.
+  **Idle licence cost attribution** — the Idle Kiro Licences table gains licence tenure, months active, months idle, monthly fee, and the cost attributable to the idle months.
+  **Billing period control** — a single whole-month control scopes every widget on every tab, because Kiro allocates and resets plan credits per calendar month. "Inactive" means billed in the selected month with no credit consumption in it.
+  **New Users Below 25% of Plan KPI** — the low-utilization counterpart to the at-risk and overage KPIs.

See the [Kiro User Activity Dashboard](kiro-user-activity-dashboard.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-kiro-user-activity.md).

## CID Data Collection v3.14.8: refactored Service Quotas module (August 26, 2026)
<a name="whats-new-cid-data-collection-31408"></a>
+  **Native quota utilization API** — the Service Quotas module now retrieves quota values and usage from the Service Quotas utilization API, improving accuracy and reliability.
+  **Parallel regional processing** — quotas are collected across regions in parallel, significantly reducing collection time.
+  **All quotas collected** — rather than only those with applied quota changes, giving broader visibility into quota utilization.

See [CID Data Collection](data-collection.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-data-collection/releases/tag/3.14.8).

## cid-cmd v4.4.17: merge taxonomy fields and account mapping (August 14, 2026)
<a name="whats-new-cid-cmd-4417"></a>
+  **Merge taxonomy fields into a single dimension** (since v4.4.16) — combine several sources that represent the same business dimension (a resource tag, an IAM principal tag, an account tag, or an `account_map` column) into one dashboard filter and Group By field. The merged column takes the first non-empty value (COALESCE) and is applied as an Amazon Quick calculated field, with no Athena view changes. It is also a simple way to normalize inconsistent tag keys, such as `application` and `app`.
+  **Account mapping with `cid-cmd map` ** — build an enriched `account_map` Athena view without writing SQL, from AWS Organizations data (OU hierarchy levels, hierarchical tag inheritance, and account-name splitting), a CSV file (such as a CMDB export or spreadsheet), or both. Select which columns become taxonomy dimensions.

See [Add organizational taxonomy](add-org-taxonomy.md).

View the [GitHub releases](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/releases).

## Kiro User Activity Dashboard v1.0.0: new dashboard and data collection module (August 12, 2026)
<a name="whats-new-kiro-user-activity-100"></a>

A new dashboard that gives you visibility into Kiro adoption, usage, and credit consumption across your organization, helping you track engagement and manage subscription costs.
+  **Executive summary** — active users, messages, and credits (including overage), daily active users by client type, and a daily credit consumption trend.
+  **User engagement and overage tracking** — top users by message count, per-user daily activity, and a per-user overage table with plan credits, caps, and utilization percentages.
+  **Client type breakdown** — daily messages and metrics across IDE, CLI, and Plugin clients, with built-in credit allocations for the Free, Pro, Pro\+, and Power tiers.
+  **New data collection module** — the `kiro-user-activity` module in the CID Data Collection framework (v3.14.7) collects Kiro user activity data with support for cross-account collection.

See the [Kiro User Activity Dashboard](kiro-user-activity-dashboard.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-kiro-user-activity.md).

## CUDOS Dashboard v5.9.0: Amazon Bedrock token usage and prompt caching insights (August 12, 2026)
<a name="whats-new-cudos-590"></a>
+  **Amazon Bedrock token consumption** — new "Tokens Usage per Usage Type Group" visual to monitor how tokens are consumed.
+  **Prompt caching efficiency** — new "Tokens Cache Read and Cache Write Ratio" visual to track how effectively prompt caching is used.
+  **Cost per million tokens fix** — corrected the "Cost per Million Tokens" calculation to account for the change in pricing unit in the CUR.
+  **Total EBS fix** — the period-over-period visual now correctly compares the previous month against the current month.

See the [CUDOS Dashboard](cudos-cid-kpi.md#foundational-cudos-dashboard).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md#cudos---590).

## CID Data Collection v3.14.6: Identity Center module, new regions (July 23, 2026)
<a name="whats-new-data-collection-3146"></a>
+  **New IAM Identity Center module** — collects Identity Center users and groups, enabling user-attribute enrichment in dashboards.
+  **Two new supported regions** — Europe (Milan) `eu-south-1` and Europe (Zurich) `eu-central-2` are now available for deploying the Data Collection stack.
+  **WorkSpaces metrics improvements** — throttle handling with fallback, new metrics, and bug fixes for the EUC dashboard data collection.

See [CID Data Collection](data-collection.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-data-collection/releases/tag/3.14.6).

## cid-cmd v4.4.14: organizational taxonomy and `cid-cmd map` (June 4, 2026)
<a name="whats-new-cid-cmd-4414"></a>

The `cid-cmd map` command provides an interactive workflow to build an enriched `account_map` from AWS Organizations data, a CSV file, or both — with support for OU hierarchy levels, hierarchical tag inheritance, and account-name splitting. This is the tooling behind adding business units, cost centers, and teams to your dashboards as filters and Group By dimensions.

See [Add organizational taxonomy](add-org-taxonomy.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/releases/tag/4.4.14).

## Pricing Change Analysis Dashboard v1.0.0: new dashboard (June 3, 2026)
<a name="whats-new-pca-100"></a>

A new dashboard that helps you analyze the cost impact of AWS pricing changes.

See the [Pricing Change Analysis Dashboard](pricing-change-dashboard.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-pca.md).

## CUDOS Dashboard v5.8.1: Amazon Bedrock cost per million tokens (June 2, 2026)
<a name="whats-new-cudos-581"></a>

Switches Amazon Bedrock unit-cost visuals from cost per 1K tokens to cost per 1M tokens and adds "Cost per Million Tokens by Model (Top 5)" and "Spend per Resource" visuals.

See the [CUDOS Dashboard](cudos-cid-kpi.md#foundational-cudos-dashboard).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md#cudos---581).

## CUDOS Dashboard v5.8.0: faster refresh, AI/ML cost visibility, Database Savings Plans (May 22, 2026)
<a name="whats-new-cudos-580"></a>
+  **Up to 5x faster dataset refresh** with the new Amazon Quick data preparation experience.
+  **Amazon Bedrock cost per million tokens**, broken down by model and IAM Principal Tag.
+  **Database Savings Plans** support across DynamoDB, the Databases tab, and the RI/SP Summary.
+  **Kiro and AWS DevOps Agent** visuals, including tracking of idle Kiro users.
+  **Extended database coverage** — Keyspaces, DMS, Aurora DSQL, and Timestream.

See the [CUDOS Dashboard](cudos-cid-kpi.md#foundational-cudos-dashboard).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md#cudos---580).

## CID Data Exports v0.12.0: IAM Principal data support (May 22, 2026)
<a name="whats-new-data-exports-0120"></a>

Adds support for the CUR 2.0 `line_item_iam_principal` column and IAM Principal Tags, enabling cost attribution by **who** made an API call. New CUR 2.0 sources also include **User Attributes** from IAM Identity Center.

See [Resource-level cost allocation](add-org-taxonomy.md#add-org-taxonomy-resource-level-cost-allocation). Requires [Data export stack](data-exports.md) `v0.11.0` or later.

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-data-collection/blob/main/data-exports/CHANGELOG.md).

## Health Events Dashboard v3.0.0: Planned Lifecycle Events and new UI (April 27, 2026)
<a name="whats-new-hed-300"></a>

Adds new Health fields for Actionability and Personas, a significantly revised landing-page interface, and emphasis on reporting AWS Planned Lifecycle Events (PLEs) such as service version deprecations.

See the [Health Events Dashboard](health-events-dashboard.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-hed.md).

## Extended Support Cost Projection v5.2: taxonomy support and redesigned sheets (April 22, 2026)
<a name="whats-new-extended-support-52"></a>

The v5.1–v5.2 releases add taxonomy (tag-based) cost analysis and a refreshed experience across the RDS, EKS, OpenSearch, and ElastiCache sheets:
+  **Taxonomy (tagging) support** — analyze and filter Extended Support cost by tags and account-level taxonomy (such as OU columns) across all sheets.
+  **Redesigned sheets** — consolidated visuals with a **Group By** control to switch between Account, Engine Version, and selected tags.
+  **More reliable account names** — account-name resolution moved to dataset-level joins against `account_map` for RDS, EKS, OpenSearch, and ElastiCache.

See the [Extended Support Cost Projection Dashboard](extended-support.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-extended-support-cost-projection.md#extended-support-cost-projection---v520).

## FOCUS Dashboard v1.2.0: FOCUS 1.2 support (March 12, 2026)
<a name="whats-new-focus-120"></a>

Supports the [FOCUS 1.2 specification](https://focus.finops.org/#specification), with dynamic consolidation view generation and new Billing Summary visuals and Group By controls for the additional FOCUS columns.

See the [FOCUS Dashboard](focus-dashboard.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-focus.md#focus-dashboard-v120).

## AI Assistant with CID and Amazon Quick: new guidance (January 19, 2026)
<a name="whats-new-genai-assistant"></a>

New guidance for integrating Cloud Intelligence Dashboards with Amazon Quick agentic AI capabilities. Instead of navigating multiple dashboards, you can ask natural-language questions and get data-driven insights across FinOps, cost efficiency, security, performance, and operational excellence. You can also automate routine tasks with Amazon Quick Flows.

See [Generative AI Assistant with Cloud Intelligence Dashboards](generative-ai.md).

## CUDOS Dashboard v5.7.0: Security tab, unused commitments, Amazon Quick (November 25, 2025)
<a name="whats-new-cudos-570"></a>
+ New **AWS Shield and AWS WAF** section, including idle AWS WAF Web ACL tracking.
+ New **RI/SP Unused Commitment Insights** section.
+  **Amazon Quick** visuals with Reader Pro / Author Pro usage and cost.
+  **Executive: Trends** can now switch between Taxonomy fields, Service, Service Category, Payer, and Linked Account.

See the [CUDOS Dashboard](cudos-cid-kpi.md#foundational-cudos-dashboard).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md#cudos---570).

## Graviton Savings Dashboard v3.0.0: EC2 analysis and Graviton Mapping tab (November 24, 2025)
<a name="whats-new-graviton-300"></a>
+  **EC2 analysis improvements** — performance-based cost modeling with normalized instance hours (NIH) reduction, plus Graviton generation selection and savings analysis.
+ New **Graviton Mapping** tab for EC2 pricing reference and cross-generational mapping.
+  **Cost-allocation tag filtering** across the dashboard.

Later v3.0.x releases extend eligibility and modernization mapping across RDS, ElastiCache, and OpenSearch (including OpenSearch Optimized instance families).

See the [Graviton Savings Dashboard](graviton-savings-dashboard.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-graviton-savings.md#graviton-savings-dashboard-v300).

## SCAD Containers Cost Allocation Dashboard v4.0.0: Kubernetes labels and Data on EKS (October 31, 2025)
<a name="whats-new-scad-400"></a>
+ Add your **Kubernetes pod labels** to the Athena view and dashboard for use in visuals, filters, and Group By dimensions.
+ Common Kubernetes labels (`app`, `chart`, `release`, `version`, `component`, `type`, `created-by`) included by default in the new **Labels/Tags Explorer** sheet.
+ New **Data on EKS** sheet for cost allocation of Spark and Flink applications running on Amazon EKS.

See the [SCAD Containers Cost Allocation Dashboard](scad-containers-dashboard.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-scad-cca.md#scad-containers-cost-allocation-dashboard---v400).

## Media Services Insights Hub v1.0.0: new dashboard (September 22, 2025)
<a name="whats-new-msih-100"></a>

A new dashboard providing cost and usage insights for AWS Media Services, including AWS Elemental MediaLive (EML) reservation analysis.

See the [Media Services Insights Hub](media-services-insights.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-media-services-insights.md#media-services-insights-hub---v100).

## TAO Dashboard v4.0.0: automated data collection (September 5, 2025)
<a name="whats-new-tao-400"></a>

The Trusted Advisor Organizational (TAO) Dashboard now collects data through [CID Data Collection](data-collection.md) (v3.14.1 or later); manual data collection is no longer supported.

See the [Trusted Advisor Organizational (TAO) Dashboard](trusted-advisor-dashboard.md).

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-tao.md#tao-dashboard-v400).

## Changelogs by dashboard and component
<a name="whats-new-changelogs"></a>

For the complete release history of each dashboard, see its changelog on GitHub. All changelogs live in the [`changes/` directory](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/tree/main/changes).


| Dashboard / component | Changelog | 
| --- | --- | 
|  `cid-cmd` command-line tool |  [GitHub releases](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/releases)  | 
| CID Data Collection Framework |  [GitHub releases](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-data-collection/releases)  | 
| CID Data Exports |  [data-exports/CHANGELOG.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-data-collection/blob/main/data-exports/CHANGELOG.md)  | 
| CUDOS |  [CHANGELOG-cudos.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md)  | 
| Cost Intelligence Dashboard (CID) |  [CHANGELOG-cid.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cid.md)  | 
| KPI Dashboard |  [CHANGELOG-kpi.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-kpi.md)  | 
| FOCUS Dashboard |  [CHANGELOG-focus.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-focus.md)  | 
| Graviton Savings Dashboard |  [CHANGELOG-graviton-savings.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-graviton-savings.md)  | 
| Graviton Opportunities |  [CHANGELOG-graviton-opportunities.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-graviton-opportunities.md)  | 
| Extended Support Cost Projection |  [CHANGELOG-extended-support-cost-projection.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-extended-support-cost-projection.md)  | 
| Trends Dashboard |  [CHANGELOG-trends.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-trends.md)  | 
| End User Computing (EUC) |  [CHANGELOG-euc.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-euc.md)  | 
| Compute Optimizer Dashboard (COD) |  [CHANGELOG-cod.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cod.md)  | 
| CORA |  [CHANGELOG-cora.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cora.md)  | 
| Trusted Advisor Organizational (TAO) |  [CHANGELOG-tao.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-tao.md)  | 
| Cost Anomalies |  [CHANGELOG-aws-cost-anomalies.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-aws-cost-anomalies.md)  | 
| AWS Marketplace SPG |  [CHANGELOG-aws-marketplace-spg.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-aws-marketplace-spg.md)  | 
| Amazon Connect |  [CHANGELOG-amazon-connect.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-amazon-connect.md)  | 
| Media Services Insights |  [CHANGELOG-media-services-insights.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-media-services-insights.md)  | 
| SCAD Containers Cost Allocation |  [CHANGELOG-scad-cca.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-scad-cca.md)  | 
| Sustainability Proxy Metrics |  [CHANGELOG-sustainability-proxy-metrics.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-sustainability-proxy-metrics.md)  | 
| ResilienceVue |  [CHANGELOG-resiliencevue.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-resiliencevue.md)  | 
| Support Cases Radar |  [CHANGELOG-support-cases-radar.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-support-cases-radar.md)  | 
| Health Events Dashboard (HED) |  [CHANGELOG-hed.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-hed.md)  | 
| DROID Dashboard |  [CHANGELOG-droid.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-droid.md)  | 

## Feedback & Support
<a name="whats-new-feedback-support"></a>

Follow [Feedback & Support](feedback-support.md) guide