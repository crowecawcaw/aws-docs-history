

# EC2 Capacity Manager
<a name="capacity-manager"></a>

Amazon EC2 Capacity Manager helps you monitor, analyze, and manage your capacity usage across On-Demand Instances, Spot Instances, and Capacity Reservations from a single location. Capacity Manager simplifies capacity tracking through a unified dashboard that aggregates your usage data with hourly refreshes and optimization opportunities.

Designed for large enterprises and multi-account organizations, Capacity Manager eliminates manual data collection from multiple sources. The tool provides deep insights across your AWS Regions. You can drill down into detailed capacity metrics and take immediate actions to optimize your cloud resources.

When you enable AWS Organizations integration, you can view and analyze capacity data across all member accounts in your organization from a single dashboard. Without Organizations integration, Capacity Manager only monitors resources within the individual AWS account where it's enabled.

**Note**  
You can only enable Capacity Manager in one AWS Region per account.
All costs displayed in Capacity Manager are estimated costs based on published On-Demand pricing. These estimates don't include discounts such as Savings Plans or Reserved Instances. Your actual costs may differ from these estimates.

## Key Features
<a name="capacity-manager-key-features"></a>
+ **Dashboard** — Provides a high-level overview of all On-Demand Capacity Reservations, On-Demand and Spot usage, including key metrics to help improve your capacity posture.
+ **Cross-account and cross-region aggregation** — View capacity usage across all member accounts in your organization from a single dashboard. Capacity Manager aggregates data from all Regions in the partition into the single Region where you have enabled Capacity Manager, including tag data. For cross-account data, Capacity Manager also provides the account name as a dimension.
+ **Tag-based grouping and filtering** — Activate tag keys from your Amazon EC2 resources (for example, `environment` or `team`) to use as dimensions when grouping and filtering your capacity metrics. Capacity Manager-provided tags for EC2 Auto Scaling Groups, EKS cluster names, EKS Kubernetes node pools, and Karpenter node pools are included by default. For more information, see [Managing monitored tag keys](managing-monitored-tag-keys.md).
+ **Data exports** — Export capacity data to Amazon S3 in CSV or Parquet format for further analysis and custom reporting.
+ **APIs** — Query capacity metrics programmatically using `GetCapacityManagerMetricData` and `GetCapacityManagerMetricDimensions`.
+ **Date selector** — Analyze capacity data across date ranges from one hour to 90 days.
+ **30\+ metrics** — Track capacity across Capacity Reservations, On-Demand Instances, and Spot Instances with over 30 metrics.