

# Explore your data in the AWS Billing and Cost Management console
<a name="bcm-lite-ce-exploring-data"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

You can use Cost Explorer to explore your cost data for a project. The Cost dashboard gives you insights into your cost and usage overview, lets you [explore your costs with AI](bcm-lite-ce-amazon-q.md), and provides you with two visual tools to understand your cost. The following documentation explains how to use these two visual tools.

## Use the cost and usage graph to explore your data
<a name="bcm-lite-ce-cost-usage-graph"></a>

The first visual tool is the cost and usage graph (). This chart has three views to understand your cost data:
+ Bar charts
+ Stacked bar charts
+ Line graphs

You can set the style by choosing one of the views in the top corner of the chart.

You can also choose to view your cost data in time frequencies, or levels of granularity. The following levels of granularity are supported in Universal Coordinated Time (UTC):
+ **Monthly** – these are defined as calendar months.
+ **Daily** – these are defined as 12:00:00 to 11:59:59 PM.

You can use preconfigured time ranges or set custom time frames.

We also provide some relative auto-selected time ranges that are useful to understand your cost. If you choose any future times, your data will be forecasted. For more information, see [Forecasting your data for Cost Explorer with our new AWS experience](bcm-lite-cost-explorer.md#bcm-lite-ce-forecasting).

The cost and usage graph lets you filter your data to gain additional insights. For more information about supported filters and how to filter your data, see [Filter your data in the AWS Billing and Cost Management console](bcm-lite-ce-filter-data.md).

### Group your data to find cost patterns
<a name="bcm-lite-ce-group-data"></a>

To gain further insight into your data, you can group it in various dimensions. For instance, if you group your data by tags, you might see all resources tagged Prod have a higher cost compared to the rest of your resources. It might make sense for those resources to have a greater cost, and Cost Explorer can help you understand your costs. If you group your data, forecasting is not available.

## Use the Cost Explorer data table to explore your data
<a name="bcm-lite-ce-data-table-explore"></a>

The second visual tool is the cost and usage breakdown. This breakdown represents whatever view you've created for the cost and usage graph. This lets you directly read the costs figures without having to navigate on the chart. Data transfer costs are included in the services that they're associated with, such as Amazon EC2 or Amazon S3. They aren't represented as a separate line item on this table.

You can download the .csv file that contains the complete data set for your chart. For more information, see [Download the cost data CSV file in the AWS Billing and Cost Management console](bcm-lite-ce-download-csv.md).