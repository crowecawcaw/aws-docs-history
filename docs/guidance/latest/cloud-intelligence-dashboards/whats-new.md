# What's new

## Overview

This page summarizes the most notable recent changes across the Cloud
Intelligence Dashboards (CID) framework — new dashboards, major features, and
tooling updates. For the complete, per-dashboard history, see the
[changelogs](#whats-new-changelogs "#whats-new-changelogs") at the bottom of this page.

## Stay up to date with the CID RSS feed

Subscribe to the RSS feed to get notified about new releases automatically:
[cloud-intelligence-dashboards.rss](https://cid.workshops.aws.dev/feed/cloud-intelligence-dashboards.rss "https://cid.workshops.aws.dev/feed/cloud-intelligence-dashboards.rss")

## Recent highlights

The highlights below cover notable releases from the past year, most recent
first.

## cid-cmd v4.4.14: organizational taxonomy and `cid-cmd map` (June 4, 2026)

The `cid-cmd map` command provides an interactive workflow to build an enriched
`account_map` from AWS Organizations data, a CSV file, or both — with support
for OU hierarchy levels, hierarchical tag inheritance, and account-name
splitting. This is the tooling behind adding business units, cost centers, and
teams to your dashboards as filters and Group By dimensions.

See [Add organizational taxonomy](add-org-taxonomy.md "add-org-taxonomy.md").

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/releases/tag/4.4.14 "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/releases/tag/4.4.14").

## Pricing Change Analysis Dashboard v1.0.0: new dashboard (June 3, 2026)

A new dashboard that helps you analyze the cost impact of AWS pricing changes.

See the [Pricing Change Analysis Dashboard](pricing-change-dashboard.md "pricing-change-dashboard.md").

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-pca.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-pca.md").

## CUDOS Dashboard v5.8.1: Amazon Bedrock cost per million tokens (June 2, 2026)

Switches Amazon Bedrock unit-cost visuals from cost per 1K tokens to cost per
1M tokens and adds "Cost per Million Tokens by Model (Top 5)" and "Spend per
Resource" visuals.

See the [CUDOS Dashboard](cudos-cid-kpi.md#foundational-cudos-dashboard "cudos-cid-kpi.md#foundational-cudos-dashboard").

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md#cudos---581 "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md#cudos---581").

## CUDOS Dashboard v5.8.0: faster refresh, AI/ML cost visibility, Database Savings Plans (May 22, 2026)

- **Up to 5x faster dataset refresh** with the new Amazon Quick data preparation
  experience.
- **Amazon Bedrock cost per million tokens**, broken down by model and IAM
  Principal Tag.
- **Database Savings Plans** support across DynamoDB, the Databases tab, and the
  RI/SP Summary.
- **Kiro and AWS DevOps Agent** visuals, including tracking of idle Kiro users.
- **Extended database coverage** — Keyspaces, DMS, Aurora DSQL, and Timestream.

See the [CUDOS Dashboard](cudos-cid-kpi.md#foundational-cudos-dashboard "cudos-cid-kpi.md#foundational-cudos-dashboard").

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md#cudos---580 "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md#cudos---580").

## CID Data Exports v0.12.0: IAM Principal data support (May 22, 2026)

Adds support for the CUR 2.0 `line_item_iam_principal` column and IAM Principal
Tags, enabling cost attribution by **who** made an API call. New CUR 2.0 sources
also include **User Attributes** from IAM Identity Center.

See [Resource-level cost
allocation](add-org-taxonomy.md#add-org-taxonomy-resource-level-cost-allocation "add-org-taxonomy.md#add-org-taxonomy-resource-level-cost-allocation"). Requires [Data export stack](data-exports.md "data-exports.md")
`v0.11.0` or later.

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-data-collection/blob/main/data-exports/CHANGELOG.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-data-collection/blob/main/data-exports/CHANGELOG.md").

## Health Events Dashboard v3.0.0: Planned Lifecycle Events and new UI (April 27, 2026)

Adds new Health fields for Actionability and Personas, a significantly revised
landing-page interface, and emphasis on reporting AWS Planned Lifecycle Events
(PLEs) such as service version deprecations.

See the [Health Events Dashboard](health-events-dashboard.md "health-events-dashboard.md").

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-hed.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-hed.md").

## Extended Support Cost Projection v5.2: taxonomy support and redesigned sheets (April 22, 2026)

The v5.1–v5.2 releases add taxonomy (tag-based) cost analysis and a refreshed
experience across the RDS, EKS, OpenSearch, and ElastiCache sheets:

- **Taxonomy (tagging) support** — analyze and filter Extended Support cost by
  tags and account-level taxonomy (such as OU columns) across all sheets.
- **Redesigned sheets** — consolidated visuals with a **Group By** control to switch
  between Account, Engine Version, and selected tags.
- **More reliable account names** — account-name resolution moved to dataset-level
  joins against `account_map` for RDS, EKS, OpenSearch, and ElastiCache.

See the [Extended Support Cost Projection Dashboard](extended-support.md "extended-support.md").

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-extended-support-cost-projection.md#extended-support-cost-projection---v520 "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-extended-support-cost-projection.md#extended-support-cost-projection---v520").

## FOCUS Dashboard v1.2.0: FOCUS 1.2 support (March 12, 2026)

Supports the
[FOCUS 1.2 specification](https://focus.finops.org/#specification "https://focus.finops.org/#specification"),
with dynamic consolidation view generation and new Billing Summary visuals and
Group By controls for the additional FOCUS columns.

See the [FOCUS Dashboard](focus-dashboard.md "focus-dashboard.md").

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-focus.md#focus-dashboard-v120 "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-focus.md#focus-dashboard-v120").

## AI Assistant with CID and Amazon Quick: new guidance (January 19, 2026)

New guidance for integrating Cloud Intelligence Dashboards with Amazon Quick
agentic AI capabilities. Instead of navigating multiple dashboards, you
can ask natural-language questions and get data-driven insights across FinOps,
cost efficiency, security, performance, and operational excellence. You can also
automate routine tasks with Amazon Quick Flows.

See [Generative AI Assistant with Cloud Intelligence
Dashboards](generative-ai.md "generative-ai.md").

## CUDOS Dashboard v5.7.0: Security tab, unused commitments, Amazon Quick (November 25, 2025)

- New **AWS Shield and AWS WAF** section, including idle AWS WAF Web ACL tracking.
- New **RI/SP Unused Commitment Insights** section.
- **Amazon Quick** visuals with Reader Pro / Author Pro usage and cost.
- **Executive: Trends** can now switch between Taxonomy fields, Service, Service
  Category, Payer, and Linked Account.

See the [CUDOS Dashboard](cudos-cid-kpi.md#foundational-cudos-dashboard "cudos-cid-kpi.md#foundational-cudos-dashboard").

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md#cudos---570 "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md#cudos---570").

## Graviton Savings Dashboard v3.0.0: EC2 analysis and Graviton Mapping tab (November 24, 2025)

- **EC2 analysis improvements** — performance-based cost modeling with normalized
  instance hours (NIH) reduction, plus Graviton generation selection and savings
  analysis.
- New **Graviton Mapping** tab for EC2 pricing reference and cross-generational
  mapping.
- **Cost-allocation tag filtering** across the dashboard.

Later v3.0.x releases extend eligibility and modernization mapping across RDS,
ElastiCache, and OpenSearch (including OpenSearch Optimized instance families).

See the [Graviton Savings Dashboard](graviton-savings-dashboard.md "graviton-savings-dashboard.md").

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-graviton-savings.md#graviton-savings-dashboard-v300 "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-graviton-savings.md#graviton-savings-dashboard-v300").

## SCAD Containers Cost Allocation Dashboard v4.0.0: Kubernetes labels and Data on EKS (October 31, 2025)

- Add your **Kubernetes pod labels** to the Athena view and dashboard for use in
  visuals, filters, and Group By dimensions.
- Common Kubernetes labels (`app`, `chart`, `release`, `version`, `component`,
  `type`, `created-by`) included by default in the new **Labels/Tags Explorer**
  sheet.
- New **Data on EKS** sheet for cost allocation of Spark and Flink applications
  running on Amazon EKS.

See the [SCAD Containers Cost Allocation Dashboard](scad-containers-dashboard.md "scad-containers-dashboard.md").

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-scad-cca.md#scad-containers-cost-allocation-dashboard---v400 "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-scad-cca.md#scad-containers-cost-allocation-dashboard---v400").

## Media Services Insights Hub v1.0.0: new dashboard (September 22, 2025)

A new dashboard providing cost and usage insights for AWS Media Services,
including AWS Elemental MediaLive (EML) reservation analysis.

See the [Media Services Insights Hub](media-services-insights.md "media-services-insights.md").

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-media-services-insights.md#media-services-insights-hub---v100 "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-media-services-insights.md#media-services-insights-hub---v100").

## TAO Dashboard v4.0.0: automated data collection (September 5, 2025)

The Trusted Advisor Organizational (TAO) Dashboard now collects data through
[CID Data Collection](data-collection.md "data-collection.md") (v3.14.1 or later); manual data
collection is no longer supported.

See the [Trusted Advisor Organizational (TAO)
Dashboard](trusted-advisor-dashboard.md "trusted-advisor-dashboard.md").

View the [changelog entry](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-tao.md#tao-dashboard-v400 "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-tao.md#tao-dashboard-v400").

## Changelogs by dashboard and component

For the complete release history of each dashboard, see its changelog on
GitHub. All changelogs live in the
[`changes/` directory](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/tree/main/changes "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/tree/main/changes").

| Dashboard / component                | Changelog                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cid-cmd` command-line tool          | [GitHub releases](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/releases "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/releases")                                                                                                                                             |
| CID Data Collection Framework        | [GitHub releases](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-data-collection/releases "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-data-collection/releases")                                                                                                                                 |
| CID Data Exports                     | [data-exports/CHANGELOG.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-data-collection/blob/main/data-exports/CHANGELOG.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-data-collection/blob/main/data-exports/CHANGELOG.md")                                                                 |
| CUDOS                                | [CHANGELOG-cudos.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cudos.md")                                                                                  |
| Cost Intelligence Dashboard (CID)    | [CHANGELOG-cid.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cid.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cid.md")                                                                                        |
| KPI Dashboard                        | [CHANGELOG-kpi.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-kpi.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-kpi.md")                                                                                        |
| FOCUS Dashboard                      | [CHANGELOG-focus.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-focus.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-focus.md")                                                                                  |
| Graviton Savings Dashboard           | [CHANGELOG-graviton-savings.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-graviton-savings.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-graviton-savings.md")                                                 |
| Graviton Opportunities               | [CHANGELOG-graviton-opportunities.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-graviton-opportunities.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-graviton-opportunities.md")                               |
| Extended Support Cost Projection     | [CHANGELOG-extended-support-cost-projection.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-extended-support-cost-projection.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-extended-support-cost-projection.md") |
| Trends Dashboard                     | [CHANGELOG-trends.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-trends.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-trends.md")                                                                               |
| End User Computing (EUC)             | [CHANGELOG-euc.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-euc.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-euc.md")                                                                                        |
| Compute Optimizer Dashboard (COD)    | [CHANGELOG-cod.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cod.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cod.md")                                                                                        |
| CORA                                 | [CHANGELOG-cora.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cora.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-cora.md")                                                                                     |
| Trusted Advisor Organizational (TAO) | [CHANGELOG-tao.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-tao.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-tao.md")                                                                                        |
| Cost Anomalies                       | [CHANGELOG-aws-cost-anomalies.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-aws-cost-anomalies.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-aws-cost-anomalies.md")                                           |
| AWS Marketplace SPG                  | [CHANGELOG-aws-marketplace-spg.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-aws-marketplace-spg.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-aws-marketplace-spg.md")                                        |
| Amazon Connect                       | [CHANGELOG-amazon-connect.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-amazon-connect.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-amazon-connect.md")                                                       |
| Media Services Insights              | [CHANGELOG-media-services-insights.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-media-services-insights.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-media-services-insights.md")                            |
| SCAD Containers Cost Allocation      | [CHANGELOG-scad-cca.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-scad-cca.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-scad-cca.md")                                                                         |
| Sustainability Proxy Metrics         | [CHANGELOG-sustainability-proxy-metrics.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-sustainability-proxy-metrics.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-sustainability-proxy-metrics.md")             |
| ResilienceVue                        | [CHANGELOG-resiliencevue.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-resiliencevue.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-resiliencevue.md")                                                          |
| Support Cases Radar                  | [CHANGELOG-support-cases-radar.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-support-cases-radar.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-support-cases-radar.md")                                        |
| Health Events Dashboard (HED)        | [CHANGELOG-hed.md](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-hed.md "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-hed.md")                                                                                        |

## Feedback & Support

Follow [Feedback & Support](feedback-support.md "feedback-support.md") guide
