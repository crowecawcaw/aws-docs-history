

# Organizing your data in Capacity Manager
<a name="capacity-manager-data-organization"></a>

Capacity Manager uses a combination of metrics, data points, dimensions, date ranges, and periods to organize your capacity data. This can help you analyze usage patterns and make informed decisions about your resources.

**Metrics and data points**

A metric is a time-ordered set of data points. For example, if you want to monitor your Spot usage in vCPUs, you would use the `SpotTotalUsageHrsVcpu` metric.

Every hour, the metric generates a timestamped data point with the Spot usage in vCPU hours. For example, if you used 100 vCPUs during the 10:00 AM hour, Capacity Manager creates a data point with a 10:00 AM timestamp and a value of 100.

For the full list of metrics that Capacity Manager analyzes, see [EC2 Capacity Manager metrics](cm-metrics-units.md).

**Dimensions**

Dimensions are name-value pairs that help you categorize and identify different aspects of a metric. For example, the name of one dimension in Capacity Manager is AccountID, where the value is the actual account ID. Capacity Manager provides dimensions to segment and group your data such as Instance Family, Reservation ARN, Reservation type, and Tenancy.

In addition to built-in dimensions, you can activate tag keys from your Amazon EC2 resources to use as custom dimensions. For example, if your instances are tagged with `environment` or `team`, you can activate those tag keys and then group and filter your capacity metrics by their values.

Capacity Manager also provides Capacity Manager-provided tags — such as EC2 Auto Scaling Group (`aws:autoscaling:groupName`), EKS cluster name (`aws:eks:cluster-name`), EKS Kubernetes node pool (`eks:kubernetes-node-pool-name`), and Karpenter node pool (`karpenter.sh/nodepool`) — that are available by default without counting toward your tag key limit.

For the full list of dimensions, see [EC2 Capacity Manager metrics](cm-metrics-units.md). For information about activating and managing tag dimensions, see [Managing monitored tag keys](managing-monitored-tag-keys.md).

**Date range and period**

The date range specifies how much time you want to analyze, from one hour to 90 days. The period determines how Capacity Manager aggregates your data across time and how many data points to return. For example, if your date range is one week and your period is 1 day, Capacity Manager returns 7 data points. Each data point represents one day of aggregated data. The period must be an interval of one hour and divide evenly into the date range.

**Topics**
+ [EC2 Capacity Manager metrics](cm-metrics-units.md)
+ [Grouping and filtering data](grouping-filtering-data.md)
+ [Managing monitored tag keys](managing-monitored-tag-keys.md)