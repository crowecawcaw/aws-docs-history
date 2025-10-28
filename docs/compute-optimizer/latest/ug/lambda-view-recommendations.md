# Accessing Lambda function recommendations and details

You can use one of the following procedures to access either the **Lambda function recommendations**
or the **Lambda function details** pages in the AWS Console.

On the **Lambda function recommendations** page you can view the recommendations for your current functions. On the
**Lambda function details** page you can view the details of a specific function and its recommendations.

## Procedures

###### To access the Lambda function recommendations page

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **Lambda functions** in the navigation pane.

The recommendations page lists the specifications and finding classifications of your
functions, along with the specifications of the recommended functions. The current functions
listed are from the AWS Region that is currently selected, in the selected account. 3. You can perform the following actions on the recommendations page:

    * Filter recommendations by AWS Regions, Findings, or Finding reasons. To do this, first select the
     **Filter by one or more properties** text box. Then,
     choose the property and a value in the dropdown list that appears.
    * Filter your recommendations by tags. To do this, select the **Tag key** or
     **Tag value** text box. Then, enter the key or value you want to filter your
     Lambda function recommendations by.


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
    * Access the **Lambda function details** page for a specific function. To do this,
     choose the finding classification listed next to the function that you want to access.

Modify the configured memory of your Lambda function when you're ready. For more
information, see [Configuring Lambda function
memory](../../../lambda/latest/dg/configuration-memory.md "../../../lambda/latest/dg/configuration-memory.md") in the _AWS Lambda Developer Guide_.

###### To access the Lambda function details page

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **Lambda functions** in the navigation pane.
3. Choose the finding classification listed next to the function for which you wish to view
   detailed information.

The details page lists the top optimization recommendation for the function that you
chose. It lists the specifications of your current function, the recommended function
configuration, and utilization metric graphs. 4. You can perform the following actions on the details page:

    * Choose a recommendation option to view the utilization comparison between your current
     function and a recommended function.


    The utilization metric graphs for your current function are displayed at the bottom of
     the page.
    * To change the time range of the graphs, choose **Time Range**, and then
     choose **Last 24 hours**, **Last 3 days**, **Last
     week**, or **Last 2 weeks**.


    Choosing a shorter time range displays the data points at a higher granularity, which
     provides a higher level of detail.

Modify the configured memory of your Lambda function when you're ready. For more
information, see [Configuring Lambda function
memory](../../../lambda/latest/dg/configuration-memory.md "../../../lambda/latest/dg/configuration-memory.md") in the _AWS Lambda Developer Guide_.
