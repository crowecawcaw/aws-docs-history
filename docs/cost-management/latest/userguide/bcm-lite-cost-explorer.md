# Use Cost Explorer in the AWS Billing and Cost Management console

###### Warning

We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

The following information is about using Cost Explorer in the AWS Billing and Cost Management console when
you're using our [new AWS experience](../../../accounts/latest/reference/sign-in-new.md "../../../accounts/latest/reference/sign-in-new.md"). If you created your account
using [Sign up for AWS (advanced)](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md") or [activated advanced features](../../../accounts/latest/reference/activate-advanced-features.md "../../../accounts/latest/reference/activate-advanced-features.md"), see [Analyzing your costs and usage
with Cost Explorer](ce-what-is.md "ce-what-is.md").

You can view and analyze your costs and usage with Cost Explorer. You can view your costs
in three unique cost and usage graphs, and you can compare usage across a variety of
dimensions and forecast your future spending. Cost Explorer is also available
programmatically. For more information about the AWS Cost Explorer API, see the [AWS
Billing and Cost Management API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

## Forecasting your data for Cost Explorer with our new AWS experience

A forecast is a prediction of how much you will use AWS services over the forecast
time period that you selected. This forecast is based on your past usage. You can use a
forecast to estimate your AWS bill and set alarms and budgets for based on
predictions. Because forecasts are predictions, the forecasted billing amounts are
estimated and might differ from your actual charges for each statement period.

Like weather forecasts, billing forecasts can vary in accuracy. Different ranges of
accuracy have different prediction intervals. The higher the prediction interval, the
more likely the forecast has a wider range. For example, suppose that you have a budget
set to 100 dollars for a given month. An 80% prediction interval might forecast your
spend between 90 and 100, with a mean of 95. The range in the prediction band is
dependent on your historical spend volatility, or fluctuations. The more consistent and
predictable the historical spend, the narrower the prediction range in forecast
spend.

Cost Explorer forecasts have a prediction interval of 80%. If AWS doesn't have
enough data to forecast an 80% prediction interval, Cost Explorer doesn't provide a
forecast. This is common for accounts that have less than one full billing cycle.

## Considerations

When using Cost Explorer when you're using our new AWS experience, consider the
following:

- You can access your cost data using the Cost Explorer API. Each paginated API
  request results in a charge of $0.01. Because you're charged per paginated request,
 identify the exact dataset you want to access before submitting queries. If you're using
 an AI agent to access the Cost Explorer API, make sure it is aware of the $0.01
  charge.
- AWS prepares data for the current month, previous 13 months, and forecasts cost
  data for the next 12 months.
- It takes AWS about 24 hours to prepare your current month's data. It takes
  AWS a few more days to complete the preparation for your previous and forecasted
  data.
- You can only view Cost Explorer data for one project at a
  time.
- All costs reflect your usage up to the previous day.
- In the current billing period, the data depends on your upstream data from
  your billing applications, and some data might be updated later than 24
  hours.
- Data transfer costs are included in the services that they're associated
  with, such as Amazon EC2 or Amazon S3. They aren't represented as either a separate line item in
  the data table or a bar in the chart.
- If you choose any forecasted dates, your current date's cost and usage data
  shows as Forecast and won't include historical data.

Because you're using our new AWS experience, we provide a streamlined version of the Cost
Explorer console that helps you understand your costs and usage. Features that aren't
covered in the following documentation are not available for our new AWS experience
customers.

###### Topics

- [Access your cost data in the AWS Billing and Cost Management console](bcm-lite-ce-accessing-data.md "bcm-lite-ce-accessing-data.md")
- [Explore your data in the AWS Billing and Cost Management console](bcm-lite-ce-exploring-data.md "bcm-lite-ce-exploring-data.md")
- [Filter your data in the AWS Billing and Cost Management console](bcm-lite-ce-filter-data.md "bcm-lite-ce-filter-data.md")
- [Download the cost data CSV file in the AWS Billing and Cost Management console](bcm-lite-ce-download-csv.md "bcm-lite-ce-download-csv.md")
- [Ask questions about your costs using Amazon Q Developer in the AWS Billing and Cost Management console](bcm-lite-ce-amazon-q.md "bcm-lite-ce-amazon-q.md")
- [Cost comparisons in the AWS Billing and Cost Management console](bcm-lite-ce-cost-comparisons.md "bcm-lite-ce-cost-comparisons.md")
- [Troubleshoot Cost Explorer in the AWS Billing and Cost Management console](bcm-lite-ce-troubleshooting.md "bcm-lite-ce-troubleshooting.md")
