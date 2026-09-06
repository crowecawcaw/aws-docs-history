

# Inspect a forecast in Amazon Connect Customer
<a name="inspect-forecast"></a>

You can inspect your forecasts before publishing them. You can do this in the online Connect Customer admin website, or [download the forecasts](download-forecasts.md) for offline analysis.

To help make it easier to inspect a forecast in the Connect Customer admin website, the forecast data is displayed in both a graph and a table. Use the controls on the report settings panel and calendar picker to adjust and filter the data for a more granular view. For example, you can:
+ Use the calendar to change the horizon. You can zoom into specific dates.
+ Choose 15 minute intervals if your date range is less than a week. With 15 minute intervals, you can see the exact contact pattern of the day.
+ Compare **Last computed forecast** and **Last published forecast** as shown in the following image.
+ Compare **Actuals** and forecasts to identify any abnormalities in either the line chart or the **Variance** chart. The Actuals data distinguishes between live data from Connect Customer and data supplied from historical uploads. Historical upload data is indicated by **Actuals Overrides** in the graph legend. **Actuals Prior Year** and **Actuals Prior Year Overrides** show data from the same date one year prior. The following image shows the forecast data displayed as graphs.  
![Forecast graph showing actuals data and actuals overrides from historical uploads.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-forecasting-inspect.png)

  Choose the **Override** setting to inspect the effect of any override you uploaded. The **Override** option is active only after an override has been uploaded. For more information, see [Edit a forecast](edit-forecast.md).
+ Filter by queues or channels to limit your forecast to one or more type.

## How average handle time is aggregated
<a name="forecast-aht-aggregation"></a>

The forecasted average handle time (AHT) for a given interval represents the expected time to handle a single contact during that interval. It indicates the average time, from start to finish, that a contact is connected with an agent.

When you view forecasted AHT aggregated across multiple intervals or queues (for example, daily or weekly totals), Connect Customer uses a weighted average rather than an arithmetic average. An arithmetic average is misleading because intervals or queues with higher forecasted contact volume contribute proportionally more to the aggregate forecasted AHT. For example, an interval forecasted to receive 100 contacts influences the aggregated forecasted AHT more than an interval forecasted to receive 2 contacts.

The aggregated forecasted AHT uses contact volume as the weight. The formula is: `Aggregated AHT = Sum(AHT × weight) / Sum(weight)`, where the weight is the total forecasted contact volume for each queue, channel, and interval.

A minimum weight of 1.0 applies to every interval or queue. Even if a queue or interval has a forecasted contact volume of zero, it still contributes to the aggregate forecasted AHT. This minimum weight ensures that every interval or queue in the forecast group is represented in the aggregated forecasted AHT. It also maintains mathematical validity when forecasted volume is zero. When all intervals have a forecasted volume of zero, each interval receives equal weight, so the aggregated AHT equals the arithmetic average of the individual AHT values.