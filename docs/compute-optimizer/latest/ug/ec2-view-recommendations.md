# Accessing EC2 instance recommendations and details

You can use one of the following procedures to access either the **EC2 instances recommendations**
or the **EC2 instance details** pages in the AWS Console.

On the **EC2 instances recommendations** page you can view the recommendations for your current instances. On the
**EC2 instance details** page you can view the details of a specific instance and its recommendations.

## Procedures

###### To access the EC2 instances recommendations page

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **EC2 instances** in the navigation pane.

The recommendations page lists the specifications and finding classifications of your
current instances and the specifications of the recommended instances. The current instances
listed are from the AWS Region that is currently selected, in the selected account. 3. You can perform the following actions on the recommendations page:

    * View the price and performance impact of running your workload on AWS Graviton-based
     instances. To do this, choose **Graviton (aws-arm64)** in the **CPU
     architecture preference** dropdown list. Otherwise, the
     **Current** (default) option displays recommendations that are based on the
     same CPU vendor and architecture as the current instance.
    * Filter recommendations by AWS Regions, Findings, Finding reasons, or Inferred Workload
     Type. To do this, first select the **Filter by one or more properties** text
     box. Then, choose the property and a value in the dropdown list that
     appears.
    * Filter your recommendations by tags. To do this, first select the **Tag
     key** or **Tag value** text
     box. Then, enter the key or value that you want to filter your EC2
     instance recommendations by.


    For example, to find all the recommendations that have a tag with the key of
     `Owner` and the value of `TeamA`, specify `tag:Owner` for
     the filter name and `TeamA` for the filter value.
    * View recommendations for instances in another account. To do this, choose
     **Account**, and then select a different account ID.


    ###### Note

    If you're signed in to a management account of an organization and trusted access with
     Compute Optimizer is enabled, you can view recommendations for resources in other accounts. For more
     information, see [Accounts supported by Compute Optimizer](getting-started.md#supported-accounts "getting-started.md#supported-accounts") and
     [Trusted access for AWS Organizations](security-iam.md#trusted-service-access "security-iam.md#trusted-service-access").
    * Clear the selected filters. To do this, choose **Clear filters** next
     to the filter.
    * Access the **EC2 instance details** page for a specific instance. To do
     this, choose the finding classification listed next to the instance that you want to access.

###### To access the EC2 instance details page

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **EC2 instances** in the navigation pane.
3. Choose the finding classification listed next to the instance that you want to view
   detailed information for.

The details page lists up to three optimization recommendations for the instance that you
chose. The page lists the specifications of your current instance, the specifications and
performance risks of the recommended instances, and utilization metric graphs. 4. You can perform the following actions on the details page:

    * To view the price and performance impact of running your workload on AWS
     Graviton-based instances, choose **Graviton (aws-arm64)** in the
     **CPU architecture preference** dropdown. Otherwise, the
     **Current** (default) option displays recommendations that are based on the
     same CPU vendor and architecture as the current instance.
    * Activate the enhanced infrastructure metrics paid feature to extend the metrics analysis
     look-back period for the EC2 instance you're viewing up to three months (compared to the
     14-day default). For more information, see [Enhanced infrastructure metrics](enhanced-infrastructure-metrics.md "enhanced-infrastructure-metrics.md").
    * Choose a recommendation option to view the utilization comparison between your current
     instance and a recommended instance.


    The utilization metric graphs for your current instance are displayed at the bottom of
     the page. The solid blue line is the utilization of your current instance. The dotted orange
     line is the projected utilization of the selected recommended instance if you use that
     instance during the analyzed period. The dotted orange line is displayed in the CPU
     utilization and memory utilization graphs.
    * To change the time range of the graphs, choose **Time Range**, and then
     choose **Last 24 hours**, **Last 3 days**, **Last
     week**, or **Last 2 weeks**. If you activate the [enhanced infrastructure metrics recommendation
     preference](enhanced-infrastructure-metrics.md "enhanced-infrastructure-metrics.md"), you can also choose **Last 3 months**.


    Choosing a shorter time range displays the data points at a higher granularity, which
     provides a higher level of detail.
    * To change the statistic value of the graphs, choose **Statistics**, and
     then choose **Average** or **Maximum**.


    You can use this option to determine the typical instance utilization of your workload
     over time. To view the highest value observed during the specified period, change the
     selection to **Maximum**. This way, you can determine the peak instance
     usage of your workload over time.
