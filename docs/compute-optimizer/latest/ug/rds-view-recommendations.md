# Accessing Aurora and RDS database recommendations and details

You can use one of the following procedures to access either the **Aurora and RDS database recommendations**
or the **Aurora and RDS database details** pages in the AWS Console.

On the **Aurora and RDS database recommendations** page you can view the recommendations for your RDS DB instances. On the
**Aurora and RDS database details** page you can view the details of a specific instance or storage and its recommendations.

## Procedures

###### To access the Aurora and RDS database recommendations page

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **Aurora and RDS databases** in the navigation pane.

###### Note

The current instances listed are from the AWS Region that is currently selected, in the selected account. 3. You can perform the following actions on the recommendations page:

    * View your instance or storage recommendations by choosing the **Instance** or
     **Storage** tab.
    * In the **Instance** tab only, you can view the price and performance impact
     of running your workload on AWS Graviton-based
     instances. To do this, choose **Graviton (aws-arm64)** in the **CPU
     architecture preference** dropdown list. Otherwise, the
     **Current** (default) option displays recommendations that are based on the
     same CPU vendor and architecture as the current RDS DB instance.
    * Filter instance or storage recommendations to one or mores AWS Regions. To do this, enter
     the name of the Region in the **Filter by one or more properties** text
     box, or choose one or more Regions in the drop-down list that appears.
    * Filter your instance or storage recommendations by tags. To do this, first select the **Tag
     key** or **Tag value** text
     box. Then, enter the key or value that you want to filter your RDS
     instance recommendations by.


    For example, to find all the recommendations that have a tag with the key of
     `Owner` and the value of `TeamA`, specify `tag:Owner` for
     the filter name and `TeamA` for the filter value.
    * View instance or storage recommendations in another account. To do this, choose
     **Account**, and then select a different account ID.


    ###### Note

    If you're signed in to a management account of an organization and trusted access with
     Compute Optimizer is enabled, you can view recommendations for resources in other accounts. For more
     information, see [Accounts supported by Compute Optimizer](getting-started.md#supported-accounts "getting-started.md#supported-accounts") and
     [Trusted access for AWS Organizations](security-iam.md#trusted-service-access "security-iam.md#trusted-service-access").
    * Clear the selected filters. To do this, choose **Clear filters** next
     to the filter.

###### To access the Aurora and RDS database details page

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **Aurora and RDS databases** in the navigation pane.
3. Choose the finding classification listed next to the RDS DB instance or storage volume that you want to view.
4. You can perform the following actions on the details page:
   - View your instance or storage recommendations by choosing the **Instance** or
     **Storage** tab.
   - In the **Instance** tab only, you can view the price
     and performance impact of running your workload on AWS
     Graviton-based instances, choose **Graviton (aws-arm64)** in the
     **CPU architecture preference** dropdown. Otherwise, the
     **Current** (default) option displays recommendations that are based on the
     same CPU vendor and architecture as the current RDS DB instance.
   - On the comparison graphs, you can hover over the graph to see exact values on specific
     dates over the analysis period.
   - To change the time range of the graphs, choose **Time Range**, and then
     choose **Last 24 hours**, **Last 3 days**, **Last
     week**, or **Last 2 weeks**.

   Choosing a shorter time range displays the data points at a higher granularity, which
   provides a higher level of detail.
   - To change the statistic value of the graphs, choose **Statistics**, and
     then choose **Average** or **Maximum**.

   You can use this option to determine the typical utilization of your workload
   over time. To view the highest value observed during the specified period, change the
   selection to **Maximum**. This way, you can determine the peak instance
   usage of your workload over time.
