# Accessing EBS volumes recommendations and details

You can use one of the following procedures to access either the **EBS volumes recommendations**
or the **EBS volume details** pages in the AWS Console.

On the **EBS volumes recommendations** page you can view the recommendations for your current EBS volumes. On the
**EBS volume details** page you can view the details of a specific volume and its recommendations.

## Procedures

###### To access the EBS volume recommendations page

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **EBS volumes** in the navigation pane.

The recommendations page lists the specifications and finding classifications of your
volumes, along with the specifications of the recommended volumes. The current volumes listed
are from the AWS Region that is currently selected, in the selected account. 3. You can perform the following actions on the recommendations page:

    * Filter recommendations by AWS Regions, Findings, or Finding reasons. To do this, first select the
     **Filter by one or more properties** text box. Then,
     choose the property and a value in the drop-down list that appears.
    * Filter your recommendations by tags. To do this, select the **Tag key** or
     **Tag value** text box. Then, enter the key or value you want to filter your
     EBS volume recommendations by.


    For example, to find all recommendations that have a tag with the key of `Owner` and the
     value of `TeamA`, specify `tag:Owner` for the filter name and `TeamA`
     for the filter value.
    * View recommendations for volumes in another account. To do this, choose
     **Account**, and then select a different account ID.


    ###### Note

    If you're signed in to a management account of an organization and trusted access with
     Compute Optimizer is enabled, you can view recommendations for resources in other accounts. For more
     information, see [Accounts supported by Compute Optimizer](getting-started.md#supported-accounts "getting-started.md#supported-accounts") and
     [Trusted access for AWS Organizations](security-iam.md#trusted-service-access "security-iam.md#trusted-service-access").
    * Clear the selected filters. To do this, choose **Clear filters** next to the
     filter.
    * Access the **EBS volume details** page for a specific volume. To do this, choose
     the finding classification listed next to the desired volume.

When you're ready, use Amazon EBS Elastic Volumes to modify the configuration of your volumes.
For more information, see [Amazon EBS Elastic
Volumes](../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md "../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md") in the _Amazon Elastic Compute Cloud User Guide_.

###### To access the EBS volume details page

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **EBS volumes** in the navigation pane.
3. Choose the finding classification listed next to the volume for which you wish to view
   detailed information.

The details page lists up to three optimization recommendations for the volume that you
chose. It lists the specifications of your current volume, the specifications and performance
risks of the recommended volumes, and utilization metric graphs. 4. You can perform the following actions on the details page:

    * Choose a recommendation option to view the utilization comparison between your current
     volume and a recommended volume.


    The utilization metric graphs for your current volume are displayed at the bottom of the
     page.
    * To change the time range of the graphs, choose **Time Range**, and then
     choose **Last 24 hours**, **Last 3 days**, **Last
     week**, or **Last 2 weeks**.


    Choosing a shorter time range displays the data points at a higher granularity, which
     provides a higher level of detail.
    * To change the statistic value of the graphs, choose **Statistics**, and
     then choose **Average** or **Maximum**.


    You can use this option to determine the typical volume utilization of your workload
     over time. To view the highest value observed during the specified period, change the
     selection to **Maximum**. This allows you to determine the peak volume usage
     of your workload over time.

When you're ready, use Amazon EBS Elastic Volumes to modify the configuration of your volumes.
For more information, see [Amazon EBS Elastic
Volumes](../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md "../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md") in the _Amazon Elastic Compute Cloud User Guide_.
