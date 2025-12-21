# Accessing EC2 Auto Scaling group recommendations and details

You can use one of the following procedures to access either the **EC2 Auto Scaling groups recommendations**
or the **EC2 Auto Scaling group details** pages in the AWS Console.

On the **EC2 Auto Scaling groups recommendations** page you can view the recommendations for your current EC2 Auto Scaling groups. On the
**EC2 Auto Scaling group details** page you can view the details of a specific group and its recommendations.

## Procedures

###### To access the EC2 Auto Scaling group recommendations page

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **EC2 Auto Scaling groups** in the navigation pane.

The recommendations page lists the specifications and finding classifications of your EC2 Auto Scaling
groups, along with the specifications of the recommended groups. The current EC2 Auto Scaling groups listed
are from the AWS Region that is currently selected, in the selected account. 3. You can perform the following actions on the recommendations page:

    * View the price and performance impact of running your workload on AWS
     Graviton-based instances. To do this, choose **Graviton (aws-arm64)** in the
     **CPU architecture preference** dropdown list. Otherwise, the
     **Current** (default) option displays recommendations that are based on the
     same CPU vendor and architecture as the current instance.
    * Filter recommendations by AWS Regions, Findings, or Finding reasons. To do this, first select the
     **Filter by one or more properties** text box. Then, choose the property and a value
     in the dropdown list that appears.
    * View recommendations for instances in another account. To do this, choose
     **Account**, and then select a different account ID.


    ###### Note

    If you're signed in to a management account of an organization and trusted access with
     Compute Optimizer is enabled, you can view recommendations for resources in other accounts. For more
     information, see [Accounts supported by Compute Optimizer](getting-started.md#supported-accounts "getting-started.md#supported-accounts") and
     [Trusted access for AWS Organizations](security-iam.md#trusted-service-access "security-iam.md#trusted-service-access").
    * Clear the selected filters. To do this, choose **Clear filters** next to the
     filter.
    * Access the **EC2 Auto Scaling group details** page for a specific EC2 Auto Scaling group. To do this,
     choose the finding classification listed next to the desired group.

###### To access the EC2 Auto Scaling group details page

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **EC2 Auto Scaling groups** in the navigation pane.
3. To view the details of a recommendation, select an EC2 Auto Scaling group and choose **View details**.
   Or, choose the EC2 Auto Scaling group link.

The details page lists up to three optimization recommendations for the EC2 Auto Scaling group that
you chose. It lists the specifications of current instances in the EC2 Auto Scaling group, the
specifications and performance risks of the recommended instances, and utilization metric
graphs. 4. You can perform the following actions on the details page:

    * To view the price and performance impact of running your workload on AWS
     Graviton-based instances, choose **Graviton (aws-arm64)** in the
     **CPU architecture preference** dropdown. Otherwise, the
     **Current** (default) option displays recommendations that are based on the
     same CPU vendor and architecture as the current instance.
    * Activate the enhanced infrastructure metrics paid feature to extend the metrics analysis
     look-back period for the Auto Scaling group you're viewing up to three months (compared to the 14-day
     default). For more information, see [Enhanced infrastructure metrics](enhanced-infrastructure-metrics.md "enhanced-infrastructure-metrics.md").
    * The utilization metric graphs for your current instance are displayed at the bottom of
     the page. The solid blue line is the utilization of current instances in the Auto Scaling
     group.
    * To change the time range of the graphs, choose **Time Range**, and then
     choose **Last 24 hours**, **Last 3 days**, **Last
     week**, or **Last 2 weeks**. If you activate the [enhanced infrastructure metrics recommendation
     preference](enhanced-infrastructure-metrics.md "enhanced-infrastructure-metrics.md"), you can also choose **Last 3 months**.
     Choosing a shorter time range displays the data points at a higher granularity, which
     provides a higher level of detail.
