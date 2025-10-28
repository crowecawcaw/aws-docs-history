# Organizing your data in Capacity Manager

Capacity Manager uses a combination of metrics, data points, dimensions, date ranges, and periods to organize your capacity data. This can help you analyze usage patterns and make informed
decisions about your resources.

**Metrics and data points**

A metric is a time-ordered set of data points. For example, if you want to monitor your Spot usage in vCPUs, you would
use the `SpotTotalUsageHrsVcpu` metric.

Every hour, the metric generates a timestamped data point with the Spot usage in vCPU hours. For example, if you used 100 vCPUs during the 10:00 AM hour,
Capacity Manager creates a data point with a 10:00 AM timestamp and a value of 100.

For the full list of metrics that Capacity Manager analyzes, see [EC2 Capacity Manager metrics](cm-metrics-units.md "cm-metrics-units.md").

**Dimensions**

Dimensions are name-value pairs that help you categorize and identify different aspects of a metric. For example, the name of one
dimension in Capacity Manager is AccountID, where the value is the actual account ID. Capacity Manager provides dimensions to segment
and group your data such as Instance Family, Reservation ARN, Reservation type, and Tenancy.

For the full list of dimensions, see [EC2 Capacity Manager metrics](cm-metrics-units.md "cm-metrics-units.md").

**Date range and period**

The date range specifies how much time you want to analyze, from one hour to 90 days.
The period determines how Capacity Manager aggregates your data across time and how many data points to return. For example,
if your date range is one week and your period is 1 day, Capacity Manager returns 7 data points. Each data point represents one day of aggregated data.
The period must be an interval of one hour and divide evenly into the date range.

###### Topics

- [EC2 Capacity Manager metrics](cm-metrics-units.md "cm-metrics-units.md")
- [Grouping and filtering data](grouping-filtering-data.md "grouping-filtering-data.md")
