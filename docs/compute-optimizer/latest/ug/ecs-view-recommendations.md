

# Accessing ECS service recommendations and details

Use one of the following procedures to open the **Recommendations for Amazon ECS services on Fargate** page or the **Amazon ECS service details** page in the AWS console.

The first page shows the recommendations for your current services. The second page shows the details for one service and its recommendations.

## Procedures
<a name="ecs-view-process"></a>

### Accessing ECS service recommendations page
<a name="ecs-viewing-recommendations-process"></a>

**To access the ECS service recommendations page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **ECS services on Fargate**.
**Note**  
The services listed are from the AWS Region that is now selected in the current account.

1. You can do the following on the recommendations page:
   + Filter recommendations by AWS Region, finding, or finding reason. To do this, choose the **Filter by one or more properties** box. Then choose the property and a value from the list.
   + Filter your recommendations by tags. To do this, choose the **Tag key** or **Tag value** box. Then enter the key or value to filter by.

     For example, to find all recommendations with a tag key of `Owner` and a value of `TeamA`, enter `tag:Owner` for the filter name and `TeamA` for the value.
   + View recommendations for services in another account. To do this, choose **Account**, then select a different account.
**Note**  
If you are signed in to a management account and trusted access with Compute Optimizer is turned on, you can view recommendations for resources in other accounts. For more information, see [Accounts supported by Compute Optimizer](getting-started.md#supported-accounts) and [Trusted access for AWS Organizations](security-iam.md#trusted-service-access).
   + Clear the selected filters. To do this, choose **Clear filters** next to the filter.

### Accessing ECS service details page
<a name="ecs-viewing-details"></a>

**To access the ECS service details page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **ECS services on Fargate**.

1. Select the service name you want to view detailed information for. Then, choose **View details**.

1. You can do the following on the details page:
   + On the graphs, hover over a point to see the exact value on a given date.
   + To change the time range, choose **Time Range**. Then choose **Last 24 hours**, **Last 3 days**, **Last week**, or **Last 2 weeks**.

     A shorter time range shows the data points in more detail.
   + To change the statistic, choose **Statistics**. Then choose **Average** or **Maximum**.

     Use this option to see the typical Amazon ECS service usage for your workload over time. To see the highest value in the period, choose **Maximum**. This shows the peak service usage over time.