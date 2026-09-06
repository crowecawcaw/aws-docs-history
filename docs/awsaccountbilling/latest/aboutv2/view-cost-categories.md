

# Viewing cost categories
<a name="view-cost-categories"></a>

From the cost categories dashboard in AWS Billing and Cost Management, you can view comprehensive information about your category details and values by using details page. This section shows you how to navigate to the details page, understand values shown, and customize your view to show different cost types.

**Topics**
+ [Navigating to your cost category details page](#view-cost-categories-details-navigate)
+ [Understanding your cost category details page](#view-cost-categories-details)
+ [Your cost category month-to-date categorizations](#view-cost-categories-details-mtd)
+ [Change your cost type](#change-cost-type-for-cost-categories)

## Navigating to your cost category details page
<a name="view-cost-categories-details-navigate"></a>

You can choose any cost category name in the Billing and Cost Management console to open a details page. The details page is also shown when you add or edit a cost category.<a name="view-cost-categories-steps"></a>

**To view your cost category details page**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost categories**.

1. Under the **Cost category** column, choose a cost category name.

## Understanding your cost category details page
<a name="view-cost-categories-details"></a>

Your cost category details page breaks down your month-to-date cost allocations using the **Category details** and **Category values** sections.
+ Use the **month selector** on the top right of the page to change the month you're viewing. You can see a detailed breakdown of cost category value cost allocations within your cost category.
+ Under the **Category details** section, you can view your current [status](manage-cost-categories.md#cost-categories-stat), [default value](manage-cost-categories.md#cost-categories-default-value), value count, and your total month-to-date net amortized costs.
+ The graph under **Categorized costs** shows the allocation of cost category values in your monthly spend. Any uncategorized costs are shown as **Uncategorized**.

## Your cost category month-to-date categorizations
<a name="view-cost-categories-details-mtd"></a>

In the **Category values** section, you can see the month-to-date spend for each configured cost category value. The amounts that are shown are the net amortized costs.

To further explore your costs, open Cost Explorer by choosing **View in AWS Cost Explorer**.

## Change your cost type
<a name="change-cost-type-for-cost-categories"></a>

You can view your cost categories by using different cost types. You can choose the following options:
+ Unblended costs
+ Amortized costs
+ Blended costs
+ Net unblended costs
+ Net amortized costs

For more information about these cost types, see [Exploring your data using Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-exploring-data.html) in the *AWS Cost Management User Guide*.

**To change your cost category type**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost categories**.

1. Under the **Cost category** column, choose a cost category name. Currently, you can change the cost type for a cost category one at a time.

1. On the upper-right corner of the page, choose the preferences icon (![Gear icon on the Cost category console.](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/images/preferences-gear.png)).

1. In the **Cost category preferences** dialog box, choose how to aggregate your costs.

1. Choose **Confirm**. The page will refresh with the new cost type.