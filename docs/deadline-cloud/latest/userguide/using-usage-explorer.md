

# Track usage and costs with the Deadline Cloud usage explorer
<a name="using-usage-explorer"></a>

With the Deadline Cloud usage explorer, you can see real-time metrics on the activity happening on each farm. You can look at the farm's costs by different variables, such as queue, fleet, job, license product, or instance types. Select various time frames to see usage during a specific period of time, and look at usage trends over the course of time. You can also see a detailed breakdown of selected data points, allowing for a closer look into metrics. Usage can be shown by time (minutes and hours) or by cost ($USD).

![The usage explorer showing filter controls, a donut chart of total cost, and a stacked bar chart of daily costs per queue.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/usage-explorer.png)


The following sections show you the steps for accessing and using the Deadline Cloud usage explorer.

**Topics**
+ [How the usage explorer and budgets estimate costs](#manage-costs-assumptions)
+ [Adjust usage explorer and budget estimates with the cost scale factor](#cost-scale-factor)
+ [Prerequisite](#usage-explorer-prereqs)
+ [Open the usage explorer](#access-usage-explorer)
+ [Use the usage explorer](#usage-explorer-use)

## How the usage explorer and budgets estimate costs
<a name="manage-costs-assumptions"></a>

The Deadline Cloud usage explorer and budget manager estimate job costs from available pricing and usage information. Use these estimates to compare usage and set budget thresholds.

### How cost estimates are calculated
<a name="cost-estimate-calculation"></a>

The usage explorer and budgets use the following basic calculation:

```
Cost per job =
    (CMF run time x CMF compute rate) +
    (SMF run time x SMF compute rate) +
    (License run time x license rate)
```
+ Run time is the sum of the time that all tasks in a job spend running.
+ Compute rate comes from [AWS Deadline Cloud pricing](https://aws.amazon.com/deadline-cloud/pricing/) for service-managed fleets. For customer-managed fleets, assume an estimated compute rate of USD 1.00 per worker hour.
+ License rate comes from the Deadline Cloud base license price and applies only to service-managed fleets. The estimate doesn't include additional pricing tiers. For more information, see [AWS Deadline Cloud pricing](https://aws.amazon.com/deadline-cloud/pricing/).

For information about costs that aren't included in these estimates, see [Understand estimated and actual costs for Deadline Cloud](cost-management.md).

## Adjust usage explorer and budget estimates with the cost scale factor
<a name="cost-scale-factor"></a>

The cost scale factor is a farm-level setting that applies a multiplier to calculated costs. Use it to align estimates with private pricing agreements, promotional credits, or internal cost allocation markups. The setting changes displayed estimates; it doesn't change the amount that AWS charges.

### Cost scale factor values
<a name="cost-scale-factor-values"></a>

The cost scale factor accepts values from 0 to 100:
+ **Values less than 1** represent discounts. For example, a value of 0.75 applies a 25 percent discount to displayed costs.
+ **Values greater than 1** represent premiums or markups. For example, a value of 1.5 applies a 50 percent markup.
+ **A value of 1** is the default and leaves displayed costs unchanged.

### Configure the cost scale factor
<a name="cost-scale-factor-configure"></a>

You can configure the cost scale factor when you create a farm or edit an existing farm.

**To configure the cost scale factor for an existing farm**

1. Open the [AWS Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home). In the navigation pane, choose **Farms and other resources**.

1. Select the farm that you want to modify.

1. Choose **Actions**, and then choose **Edit**.

1. For **Cost scale factor**, enter a value from 0 to 100.

1. Choose **Save changes**.

### Effects on cost tools
<a name="cost-scale-factor-effects"></a>

After you configure a cost scale factor, the value affects the cost tools in the following ways:
+ **Usage explorer** – New queries display cost data modified by the cost scale factor.
+ **New budgets** – Budgets created after the change use the new value for all cost calculations.
+ **Existing budgets** – Existing budgets use the new value for future calculations, but Deadline Cloud doesn't recalculate their accumulated cost history. To recalculate accumulated costs, delete and recreate the budget.

## Prerequisite
<a name="usage-explorer-prereqs"></a>

To use the Deadline Cloud usage explorer, you must have either `MANAGER` or `OWNER` farm permissions. For more information, see [How permissions work in Deadline Cloud](permissions-overview.md).

**Note**  
If your time zone doesn't align to a full hour, such as India Standard Time (UTC\+5:30), the usage explorer doesn't show usage metrics. To see metrics, set your time zone to a zone that aligns to a full hour.

## Open the usage explorer
<a name="access-usage-explorer"></a>

To open the Deadline Cloud usage explorer, use the following procedure.

1. Sign in to the AWS Management Console and open the Deadline Cloud [ console](https://us-west-2.console.aws.amazon.com/deadlinecloud/home).

1. To see all available farms, choose **View farms**. 

1. Locate the farm that you want to get information about, then choose **Manage jobs**. The Deadline Cloud monitor opens in a new tab.

1. In the Deadline Cloud monitor, from the left menu, select **Usage explorer**.

## Use the usage explorer
<a name="usage-explorer-use"></a>

From the usage explorer page, you can select specific parameters in which the data can be displayed. By default, you see total usage in time (hours and minutes) within the last 7 days. You can change these parameters, and the information displayed changes dynamically in accordance to the parameter settings.

You can group the results based on the queue, fleet, job, user, usage type, instance type, or license product. If you choose license product, costs are calculated for specific licenses. If you filter by fleet and group by usage type, you can see persistent volume cost associated with your fleets. For all other groups the time is calculated by adding up the time taken for each task to run.

You can filter results by queues or by fleets, but you cannot filter by both at the same time.

The usage explorer returns only 100 results based on the filter criteria that you set. The results are listed in descending order by the date created timestamp. If there are more than 100 results, you get an error message. You can refine your query to reduce the number of results:
+ Select a smaller time range
+ Select fewer queues or fleets
+ Select a different grouping, such as grouping by queue or fleet instead of job

**Topics**
+ [Use visual graphs to review data](#visual-graphs)
+ [View a breakdown of metrics](#breakdown)
+ [View approximate runtime of queues and fleets](#approximate-runtime)

### Use visual graphs to review data
<a name="visual-graphs"></a>

You can review data in a visual format to identify trends and potential areas that might need more analysis or attention. Usage explorer offers a pie chart that displays overall usage and cost with the option to group the totals into smaller subtotals. 

**Note**  
The chart *only* displays the top five results with other results combined in an "others" section. You can view all results in the breakdown section below the chart.

![A pie chart showing a breakdown of the time spent running jobs is three different queues in a farm.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/cost-explorer-graph.png)


### View a breakdown of metrics
<a name="breakdown"></a>

Beneath the pie chart, usage explorer offers a more detailed breakdown of specific metrics, which will change as parameters change. By default, five results display in the usage explorer. You can scroll through results using the pagination arrows in the breakdown section. 

Breakdown is minimized by default. To expand and display the results, select the **View all breakdown** arrow. To download the breakdown, choose **Download data**. 

### View approximate runtime of queues and fleets
<a name="approximate-runtime"></a>

You can also view the approximate runtime of your queues or fleets based on different intervals that you specify. The interval options are hourly, daily, weekly, and monthly. After you select an interval, the graph displays the approximate runtime of your queues or fleets. 

![A bar chart showing the approximate runtime of a queue or fleet using a daily interval.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/usage-explorer-approximate-runtime.png)
