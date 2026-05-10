# Inspect a forecast in Amazon Connect Customer

You can inspect your forecasts before publishing them. You can do this in the
online Connect Customer admin website, or [download the forecasts](download-forecasts.md "download-forecasts.md")
for offline analysis.

To help make it easier to inspect a forecast in the Connect Customer admin website, the forecast data is
displayed in both a graph and a table. Use the controls on the report settings panel
and calendar picker to adjust and filter the data for a more granular view. For
example, you can:

- Use the calendar to change the horizon. You can zoom into specific
  dates.
- Choose 15 minute intervals if your date range is less than a week. This
  enables you to see the exact contact pattern of the day.
- Compare **Last computed forecast** and **Last
  published forecast** as shown in the following image.
- Compare **Actuals** and forecasts to identify any
  abnormalities in either the line chart or the **Variance**
  chart. The Actuals data distinguishes between live data from Connect Customer and
  data supplied from historical uploads. Historical upload data is indicated
  by **Actuals Overrides** in the graph legend.
  **Actuals Prior Year** and
  **Actuals Prior Year Overrides** show data from
  the same date one year prior. The following image shows the forecast data displayed as
  graphs.

![Forecast graph showing actuals data and actuals overrides from historical uploads.](images/wfm-forecasting-inspect.png)

Choose the **Override** setting to inspect the effect of
any override you uploaded. The **Override** option is
active only after an override has been uploaded. For more information, see
[Edit a forecast](edit-forecast.md "edit-forecast.md").

- Filter by queues or channels to limit your forecast to one or more
  type.
