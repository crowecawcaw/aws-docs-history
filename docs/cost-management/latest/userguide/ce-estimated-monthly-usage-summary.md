# Understanding your estimated

monthly usage summary

When you enable granular data in Cost Explorer, it increases the number of usage records
Cost Explorer needs to host for your organization. To ensure Cost Explorer can respond
to queries as quickly as possible, Cost Explorer limits the amount of granular data
stored for your organization.

###### Note

If you enable hourly granularity for both **EC2-Instances (Elastic Compute
Cloud - Compute) resource-level data** and **Cost and usage
data for all AWS services at hourly granularity (without resource-level
data)**, you will see a drop in the hourly usage records reported
against **Cost and usage**. This is because the EC2 hourly usage
records are moved and reported under **EC2-Instances**.

In Cost Management preferences, you can view the estimated usage records count for your
granular data preference selections and understand how close you are to the
Cost Explorer data limits. See "Understanding Cost Explorer data threshold
limits".

Hourly granularity in Cost Explorer is a paid feature and the cost depends on your hourly
usage records count. Understanding your estimated usage records count for hourly
granularity features can help you estimate the cost of these features before enabling
them. See "Estimating cost for Cost Explorer hourly granularity".

###### Note

The usage records displayed in Cost Management preferences are for your entire organization
and are estimates based on your average past usage. The actual usage records in any
given past, current, or future month might differ from these values. If you’re a new
AWS customer and haven’t used AWS for at least a month, we can’t estimate your
usage records due to insufficient data.

###### Topics

- [Understanding Cost Explorer data
  threshold limits](ce-data-threshold-limits.md "ce-data-threshold-limits.md")
- [Estimating cost for Cost Explorer hourly
  granularity](ce-hourly-granularity.md "ce-hourly-granularity.md")
