

# Choosing advanced options

You can customize how you view your data in Cost Explorer using **Advanced options** to include or exclude specific types of data. 

**To include or exclude data**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost Explorer**.

1. In the right pane, under **Advanced options**, under **Aggregate costs by**, choose between the following:
**Note**  
We added Billed cost, Public equivalent billed cost, Contracted cost, List cost, and Public on-demand cost as new cost metrics in November 2026. These metrics show values for November 2026 and later months.
   + **Actual Costs**
     + **Billed cost**: This cost metric reflects the cost serving as the basis for invoicing. This includes the impact of discounts, purchasing options and tiered pricing.
     + **Unblended costs**: This cost metric reflects the cost of the usage. When grouped by **Charge type**, unblended costs separate discounts into their own line items. This enables you to view the amount of each discount received.
     + **Net unblended costs**: This cost metric reflects the cost after discounts.
   + **Effective Costs**
     + **Net amortized costs**: This cost metric amortizes the upfront and monthly reservation fees while including discounts such as RI volume discounts.
     + **Amortized costs**: This cost metric reflects the effective cost of the upfront and monthly reservation fees spread across the billing period. By default, Cost Explorer shows the fees for Reserved Instances as a spike on the day that you're charged. However, if you choose to show costs as amortized costs, the costs are amortized over the billing period. This means that the costs are broken out into the effective daily rate. AWS estimates your amortized costs by combining your unblended costs with the amortized portion of your upfront and recurring reservation fees. For the daily view, Cost Explorer shows the unused portion of your upfront reservation fees and recurring RI charges on the first of the month.

       For example, suppose that Alejandro purchases a Partial Upfront `t2.micro` RI for a one-year term at $30 dollars upfront. The monthly fee is $2.48. Cost Explorer shows the costs for this RI as a spike on the first of the month. If Alejandro chooses **Amortized costs** for a 30-day month, the Cost Explorer chart shows a daily effective rate of $0.165. This is the EC2 effective rate multiplied by the number of hours in a day.

       Amortized costs aren't available for billing periods before 2018. If you want to see how much of your reservation was unused, group by purchase option.
     + **Blended costs**: This cost metric reflects the average cost of usage across the consolidated billing family. If you use the consolidated billing feature in AWS Organizations, you can view costs using *blended rates*. For more information, see [Blended Rates and Costs](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/con-bill-blended-rates.html#Blended_CB).
     + **Contracted cost**: This cost metric reflects the cost after applying contracted discounts and tier-based pricing while excluding commitment-based discounts.
   + **Reference Costs**
     + **List cost**: This cost metric reflects the cost based on the published on-demand prices for AWS services with tiered pricing but doesn't include commitment-based discounts.
     + **Public on-demand cost**: This cost metric reflects the cost based on public on-demand rate and in case of tiered pricing, it reflects the cost based on the highest tier. For products with subscriptions, it's the public price of the subscription.
     + **Public equivalent billed cost**: This cost metric reflects cost without contracted or private discounts, inclusive of the impacts of all reduced rate and purchasing options.

1. Under **Additional data settings**, select from the following:
   + **Show forecasted values**: Cost Explorer displays a forecast for how much AWS predicts you will spend over the forecast time period that you select, based on your past costs.
   + **Show only untagged resources**: By default, Cost Explorer includes costs both for resources that have cost allocation tags and for resources that don't have cost allocation tags. To find untagged resources that add to your costs, select **Show only untagged resources**. For more information about cost allocation tags, see [Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html).
   + **Show only uncategorized resources**: By default, Cost Explorer includes costs both for resources that are mapped to a cost category and for resources that aren’t mapped to a cost category. To find uncategorized resources that add to your costs, select **Show only uncategorized resources**. For more information about cost categories, see [Organizing costs using AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html).