

# Intraday forecast performance dashboard
<a name="intraday-forecast-performance-dashboard"></a>

The Intraday forecast performance dashboard provides forecasts for:
+ [Contact volume](metrics-definitions.md#contact-volume) and [Average handle time](metrics-definitions.md#average-handle-time) for queues that have a minimum of 2000 unique contacts per week per queue-channel for the last 4 weeks. This is evaluated every day for the trailing time period. 
+  [Average queue answer time](metrics-definitions.md#average-queue-answer-time) for queues that have 5000 unique contacts per month with the same evaluation timing.

**Topics**
+ [Enable access to the dashboard](#intraday-forecast-performance-dashboard-enable-access)
+ [Performance overview widget](#intraday-forecast-performance-dashboard-performance-overview)
+ [Comparison trend graphs](#intraday-forecast-comparison-trend-graphs)
+ [Comparison against short term forecasts](#intraday-forecast-comparison-shortterm)
+ [Daily projection widget](#intraday-forecast-daily-projection)

## Enable access to the dashboard
<a name="intraday-forecast-performance-dashboard-enable-access"></a>

Ensure users are assigned the appropriate **Analytics and Optimization** security profile permissions:
+ **Access metrics - Access permission** or the **Dashboard - Access permission**. For information about the difference in behavior, see [Assign permissions to view dashboards and reports in Connect Customer](dashboard-required-permissions.md). 
+ **Forecasting - View**. If you don't see this permission on the security profiles page, ask your Administrator to [enable forecasting, capacity planning, and scheduling](enable-forecasting-capacity-planning-scheduling.md) in the AWS console. 

## Performance overview widget
<a name="intraday-forecast-performance-dashboard-performance-overview"></a>

The **Intraday trailing performance overview** widget provides aggregated metrics based on your filters. Each metric in the widget is compared to your "compare to" benchmark time range filter. The widget displays the following metrics:
+ [Contact volume](metrics-definitions.md#contact-volume)
+ [Average handle time](metrics-definitions.md#average-handle-time)
+ [Average queue answer time](metrics-definitions.md#average-queue-answer-time)
+ [Effective staffing](metrics-definitions.md#effective-staffing)
+ [Abandonment rate](metrics-definitions.md#abandonment-rate)
+ [Service level](metrics-definitions.md#service-level)

The **Service level** metric uses a 60-second threshold by default. You can change the threshold for this widget, independently of the other widgets, to match your service level target.

The following image shows an example **Intraday trailing performance overview** widget: 

![The Intraday trailing performance overview widget showing six metrics compared to forecast.](https://docs.aws.amazon.com/connect/latest/adminguide/images/intraday-perf-overview-chart.png)


This widget shows the following information:
+ Contact volume during your time range selection was 3,921.
+ This is down 5% compared to the forecasted contact volume of 4,128.
+ The percentages are rounded up or down.
+ The colors that appear for the metrics indicate positive (green) or negative (red) compared to your benchmark. 

## Comparison trend graphs
<a name="intraday-forecast-comparison-trend-graphs"></a>

The Intraday performance dashboard displays the following trend graphs, which cover different metrics: 
+ [Contact volume](metrics-definitions.md#contact-volume)
+ [Average handle time](metrics-definitions.md#average-handle-time)
+ [Average queue answer time](metrics-definitions.md#average-queue-answer-time)
+ [Effective staffing](metrics-definitions.md#effective-staffing)
+ [Service level](metrics-definitions.md#service-level)

The **Service level** trend graph uses a 60-second threshold by default. To use a different threshold, edit the trend graph widget. Its threshold is independent of the threshold in the other widgets.

These graphs include the intraday forecast that projects up to 24 hours on a 15 minute interval based on:
+ The value of the respective metric.
+ The historical actuals from the current day.
+ The historical actuals from the same time in the past week.

These trend graphs provide data only for the next 24 hours and the past 24 hours. There is no option to change the time range. 

The following image shows an example of a **Contact volume** trend graph.

![The Contact volume trend graph.](https://docs.aws.amazon.com/connect/latest/adminguide/images/intraday-perf-trend-graph.png)


The following image shows an example of a **Service level** trend graph. It shows the trend of the actual service level up to the last update, and the intraday forecast service level after it. The legend labels include the threshold, such as **Service level 60 seconds** for the default threshold. If you choose a different threshold, the labels show that value.

![The Service level trend graph showing actual and forecast service level over 24 hours.](https://docs.aws.amazon.com/connect/latest/adminguide/images/intraday-service-level-trend-graph.png)


## Comparison against short term forecasts
<a name="intraday-forecast-comparison-shortterm"></a>

You can compare **Average handle time** and **Contact volume** against published short term forecasts. 

To select this option, choose the compare to button and select **Short-term published forecast**. This automatically picks up the published short term forecast for the time range selected. You can't select an unpublished forecast or a specific published forecast. 

For historical widgets, it compares against the same time range as the widget, while for the daily projection widget it compares against the entire day. 

This is the new default comparison for this dashboard. 

![The Short-term published forecast option.](https://docs.aws.amazon.com/connect/latest/adminguide/images/intraday-shortterm.png)


## Daily projection widget
<a name="intraday-forecast-daily-projection"></a>

The **Daily projection** widget provides a projection of how the day will end by combining historical metrics for the day so far with intraday forecasts for the remainder of the day. This is available for the following metrics: 
+ [Contact volume](metrics-definitions.md#contact-volume)
+ [Average handle time](metrics-definitions.md#average-handle-time)
+ [Average queue answer time](metrics-definitions.md#average-queue-answer-time)
+ [Effective staffing](metrics-definitions.md#effective-staffing)
+ [Service level](metrics-definitions.md#service-level)

The **Service level** metric uses a 60-second threshold by default. To use a different threshold, edit the **Daily projection** widget. Its threshold is independent of the threshold in the other widgets.

This widget only supports comparing against short term forecasts for **Contact volume** and **Average handle time**.

![The Daily projection widget showing projected values for five metrics.](https://docs.aws.amazon.com/connect/latest/adminguide/images/intraday-daily-projection.png)
