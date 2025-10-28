# Grouping and filtering data

Capacity Manager aggregates your metrics based on the dimensions and date period you choose. If no dimensions are chosen,
Capacity Manager will aggregate the data and return one data point per period in the date range. You can group your data into
smaller aggregations by adding dimensions.

- **Grouping** — Break down your capacity data by dimensions such as Region, Instance Family,
  or Account ID. You can group your metrics by multiple dimensions to break down your data further. For example, if you group
  by Region and Availability Zone, you get a data point for each Region and AZ combination where you have usage.
- **Filtering** — Show only specific subsets of the dimensions you selected. For example,
  if you group by instance family, you will get data points for all families where you have
  usage. However, if you also filter by p5, you see only data points for the p5 instance family.
- **Metric units** — View results by different units like vCPUs, instances, or estimated costs.
  For example, after grouping by Region and filtering by a specific instance family, you can view the data in different ways.
  Switch between total vCPUs used, number of instances running, or estimated costs.

## How to group and filter data in the console

###### To group and filter data in Capacity Manager

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Capacity Manager**.
3. Choose the tab for the resource type you want to analyze: **Usage**, **Reservations**,
   or **Spot**.
4. In the **Date filter** section, choose a Date range, Time zone, and Interval.
5. In the **Dimension filter** section, choose a dimension from the _Select a dimension_ dropdown.
6. Select the dimensions you want to group by from the dropdown. Note that the dimension options differ for each
   resource type. For more information, see [EC2 Capacity Manager metrics](cm-metrics-units.md "cm-metrics-units.md").

You can add multiple dimensions to create more granular groupings. 7. To filter by the dimension(s) you selected, choose a filter option from the _Filter by dimension_ dropdown. 8. In the **Aggregations** section, choose a unit to view your results by vCPUs, Instances, or Estimated costs.
