

# Grouping and filtering data
<a name="grouping-filtering-data"></a>

Capacity Manager aggregates your metrics based on the dimensions and date period you choose. If no dimensions are chosen, Capacity Manager will aggregate the data and return one data point per period in the date range. You can group your data into smaller aggregations by adding dimensions, including tag dimensions from your Amazon EC2 resources.
+ **Grouping** — Break down your capacity data by dimensions such as Region, Instance Family, Account ID, or tag keys. You can group your metrics by multiple dimensions to break down your data further. For example, if you group by Region and Availability Zone, you get a data point for each Region and AZ combination where you have usage.
+ **Filtering** — Show only specific subsets of the dimensions you selected. For example, if you group by instance family, you will get data points for all families where you have usage. However, if you also filter by p5, you see only data points for the p5 instance family. You can also filter by tag values — for example, filter by `environment=prod` to see only production resources. To filter for resources that do not have a value for a selected tag, filter by an empty value.
+ **Metric units** — View results by different units like vCPUs, instances, or estimated costs. For example, after grouping by Region and filtering by a specific instance family, you can switch between total vCPUs used, number of instances running, or estimated costs.

## How to group and filter data in the console
<a name="grouping-filtering-process"></a>

**To group and filter data in Capacity Manager**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Capacity Manager**.

1. Choose the tab for the resource type you want to analyze: **Usage**, **Reservations**, or **Spot**.

1. In the **Date filter** section, choose a Date range, Time zone, and Interval.

1. In the **Dimension filter** section, choose a dimension from the *Select a dimension* dropdown. The dimension options differ for each resource type. For more information, see [EC2 Capacity Manager metrics](cm-metrics-units.md).

   To group by a tag dimension, choose the tag key from the dropdown (for example, `environment`). Only tag keys in `activated` status are available. For more information about activating tag keys, see [Managing monitored tag keys](managing-monitored-tag-keys.md).

   You can add multiple dimensions, including multiple tag dimensions, to create more granular groupings.

1. To filter by the dimension(s) you selected, choose a filter option from the *Filter by dimension* dropdown.

   For tag dimensions, the filter shows the tag values present in your data. To filter for resources without a value for the selected tag, choose the empty value option.

1. In the **Aggregations** section, choose a unit to view your results by vCPUs, Instances, or Estimated costs.

**Note**  
When you group by a tag dimension, resources that do not have a value for that tag are included in a separate group with an empty value. This ensures that totals account for all resources, not only tagged ones.