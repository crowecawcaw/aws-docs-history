# Accessing commercial software license recommendations and details

You can use one of the following procedures to access either the **Recommendations for commercial software licenses**
or the **License details** pages in the AWS Console.

On the **Recommendations for commercial software licenses** page you can view the recommendations for your current licenses. On the
**License details** page you can view the details of a specific license recommendation.

## Procedures

###### To access the commercial software license recommendations page

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **Licenses** in the navigation pane.
3. (Optional) You can also access the license recommendations from the EC2 instances page. To do this, first select
   the Filter by one or more properties. From the dropdown list that appears, choose the **Inferred workload
   type** property and then choose the **Inferred workload type = SQL Server value**.

###### Note

The current licenses listed are from the AWS Region that is currently selected, in the selected account. 4. You can perform the following actions on the recommendations for commercial software licenses page:

    * Filter recommendations by AWS Regions, Findings, or Finding reasons. To do this, first select the
     **Filter by one or more properties** text box. Then,
     choose the property and a value in the dropdown list that appears.
    * Filter your recommendations by tags. To do this, select the **Tag key** or
     **Tag value** text box. Then, enter the key or value you want to filter your
     licesne recommendations by.


    For example, to find all recommendations that have a tag with the key of `Owner` and the
     value of `TeamA`, specify `tag:Owner` for the filter name and `TeamA`
     for the filter value.
    * View recommendations for functions in another account. To do this, choose
     **Account**, and then select a different account ID.


    ###### Note

    If you're signed in to a management account of an organization and trusted access with
     Compute Optimizer is enabled, you can view recommendations for resources in other accounts. For more
     information, see [Accounts supported by Compute Optimizer](getting-started.md#supported-accounts "getting-started.md#supported-accounts") and
     [Trusted access for AWS Organizations](security-iam.md#trusted-service-access "security-iam.md#trusted-service-access").
    * Clear the selected filters. To do this, choose **Clear filters** next to the
     filter.

###### To access the commercial software license details page

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **Licenses** in the navigation pane.
3. Choose the **Instance ID** you want to view detailed information.
4. You can perform the following actions on the details page:
   - On the utilization graphs, you can hover over the graph to see exact values on specific
     dates over the analysis period.
   - To change the time range of the graphs, choose **Time Range**, and then
     choose **Last 24 hours**, **Last 3 days**, **Last
     week**, or **Last 2 weeks**.

   Choosing a shorter time range displays the data points at a higher granularity, which
   provides a higher level of detail.
   - To change the statistic value of the graphs, choose **Statistics**, and
     then choose **Average** or **Maximum**.
