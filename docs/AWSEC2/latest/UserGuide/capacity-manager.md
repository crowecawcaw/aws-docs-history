# EC2 Capacity Manager

Amazon EC2 Capacity Manager allows you to monitor, analyze, and manage your capacity usage across On-Demand Instances, Spot Instances, and Capacity Reservations
from a single location. Capacity Manager simplifies capacity tracking through a unified dashboard that aggregates your usage data with hourly refreshes and
optimization opportunities.

Designed for large enterprises and multi-account organizations, Capacity Manager eliminates manual data collection from multiple sources. The tool
provides deep insights across your AWS Regions. You can drill down into detailed capacity metrics and take immediate actions to optimize your cloud resources.

When you enable AWS Organizations integration, you can view and analyze capacity data across all member accounts in your organization from a single dashboard.
Without Organizations integration, Capacity Manager only monitors resources within the individual AWS account where it's enabled.

###### Note

- You can only enable Capacity Manager in one AWS Region per account.
- All costs displayed in Capacity Manager are estimated costs based on published On-Demand pricing. These estimates don't include discounts such as
  Savings Plans or Reserved Instances. Your actual costs may differ from these estimates.

## Key Features

- **Centralized dashboard:** View capacity usage across all accounts and regions with new data points refreshed every hour
- **Cross-account visibility:** Organization-level view for admin accounts
- **Data exports:** Export capacity data to Amazon S3
- **APIs:** Programmatic access to capacity metrics and data
- **Flexible analysis:** Dynamic date selector for exploring capacity usage across different time periods from the past 90 days
- **Comprehensive metrics and dimensions:** Access to more than 30 metrics across multiple measurement units (vCPUs, instances, estimated costs)
  with extensive filtering capabilities including Account ID, Region, Instance Family, Availability Zone, Instance Type, Platform, Tenancy, and reservation-specific dimensions
