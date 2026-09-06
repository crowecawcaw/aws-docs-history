

# Forecasting with Cost Explorer
<a name="ce-forecast"></a>

You create a forecast by selecting a future time range for your report. For more information, see [Choosing time ranges for the data that you want to view](ce-modify.md#ce-timerange). The following section discusses the accuracy of the forecasts created by Cost Explorer and how to read them. 

A forecast is a prediction of how much you will use AWS services over the forecast time period that you selected. This forecast is based on your past usage. You can use a forecast to estimate your AWS bill and set alarms and budgets for based on predictions. Because forecasts are predictions, the forecasted billing amounts are estimated and might differ from your actual charges for each statement period. 

Like weather forecasts, billing forecasts can vary in accuracy. Different ranges of accuracy have different prediction intervals. The higher the prediction interval, the more likely the forecast has a wider range. For example, suppose that you have a budget set to 100 dollars for a given month. An 80% prediction interval might forecast your spend between 90 and 100, with a mean of 95. The range in the prediction band is dependent on your historical spend volatility, or fluctuations. The more consistent and predictable the historical spend, the narrower the prediction range in forecast spend.

Cost Explorer forecasts have a prediction interval of 80%. If AWS doesn't have enough data to forecast an 80% prediction interval, Cost Explorer doesn't provide a forecast. This is common for accounts that have less than one full billing cycle.

## Reading forecasts
<a name="reading-forecasts"></a>

How you read the Cost Explorer forecasts depends on the type of chart that you're using. Forecasts are available for both line charts and bar charts.

The 80% prediction interval appears differently on each type of chart:
+ Line charts represent the prediction interval as a set of lines that are on either side of your costs line.
+ Bar charts represent the prediction interval as two lines that are on either side of the top of your bar.

When forecasting costs, discounts are included by default.

**Note**  
If you want your forecasts to include non-recurring discounts such as refunds, we encourage you to use **Show net unblended costs**. For more information about different costs, see [Cost Explorer Advanced Options](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-advanced.html).

## Using forecasts with consolidated billing
<a name="budget-consolidated"></a>

If you use the consolidated billing feature in AWS Organizations, the forecasts are calculated with the data from all the accounts. If you add a new member account to an organization, forecasts don't include that new member account until the new spending patterns of the organization are analyzed. For more information about consolidated billing, see [Consolidated billing for AWS Organizations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html).

## Understanding your forecasts with AI explanations
<a name="forecasting-ce"></a>

Cost Explorer provides AI-powered explanations that help you understand the key drivers behind your forecast predictions. You can access forecast explanations by configuring a future date range in Cost Explorer and clicking **Analyze with Amazon Q**. Amazon Q Developer delivers detailed forecast explanations covering projected spending trajectories, service-level breakdowns, and the factors influencing your projections. You can ask follow-up questions to understand why specific services are projected to increase or decrease. For more information, see [Using Analyze with Amazon Q](ce-nlq.md#ce-nlq-analyze-with-q).

**Note**  
You can also ask questions about your forecasted costs using the suggested prompts or the **Ask question** button in Cost Explorer, powered by **Amazon Q Developer**. When viewing future dates, forecast related suggested prompts appear automatically. For more information, see [Asking questions about your costs using Amazon Q Developer](ce-nlq.md).