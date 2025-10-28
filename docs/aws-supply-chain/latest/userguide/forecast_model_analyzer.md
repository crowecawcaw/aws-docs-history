# Forecast model analyzer

Forecast model analyzer is a self-service tool that you can use to execute forecast experiments on multiple forecast models (forecast period in past and future). Once executed, you can review the results of the different forecast models.
Using accuracy metrics and visual comparison between forecasts and actual demand, you can choose the required forecast model that suits your business data patterns. You can execute the forecast model analyzer at the same time the production demand plan is running without any interference between each other or vice-versa.

###### Note

Forecast model analyzer is an optional work flow. If you do not have multiple forecast models to compare, you can continue to use the default forecast model recommendations provided by AWS Supply Chain.

The forecast model analyzer supports two main evaluation scenarios:

- Back test scenario – You set the forecast start date in the past. In this scenario, forecasts are created and accuracy metrics are calculated and reported for forecast periods of overlap with actual demand periods.
- Forward forecast scenario – You do not set the forecast start date and there is no overlap between forecast and actual data. In this scenario, forecasts are created but since actual demand data is not available (for future periods), accuracy metrics are not calculated or reported.
  You can still verify how the demand is forecasted against recent trend and prior year(s) demand.
  Make sure the demand plan settings are configured before you execute the forecast model analyzer. The forecast model analyzer inherits the demand plan settings for _time interval_ and _hierarchy granularity_, while providing the flexibility to adjust the forecast horizon and optionally
  select the forecast start date.

You can choose to execute a back test or a forward forecast scenario. The default is forward forecast scenario where you do not specify a forecast start date and it is based on the last order date in the actual demand history. For more information, see [Create your first demand plan](onboarding.md "onboarding.md").
However, if you choose to run a back test scenario, you can override the forecast start date and select a date in the past for back testing purposes. When the selected forecast start date is later than the _outbound_order_line_ dataset end date, the default planning cycle last order date
in the actual demand history is used. When the selected forecast start date is before the _outbound_order_line_ start date or if the length of the demand history is insufficient, the forecast will fail and display an error. For more information, see [Prequisites before uploading your dataset](data_quality.md "data_quality.md").

It is recommended to select the first of the month for monthly intervals or Monday for weekly intervals. If you choose a different date, Demand Planning will automatically adjust to the nearest default date.
For example, if you selected Wednesday as the forecast start date, Demand Planning will select the next Monday as the forecast start date for weekly intervals. Similarly, selecting May 10th 2024 will result in June 1st 2024 as the planning cycle start date for monthly intervals.

###### Note

Make sure you have at least four times the historical demand data for the forecast period you enter.

After reviewing the model analyzer results, you can select or change the choice of forecast algorithm in the forecast analyzer tool. Alternatively, you can choose not to use model analyzer and proceed to directly
selecting or changing the choice of forecast algorithm to be used. AWS Supply Chain will pick the default forecast method for your dataset when the model analyzer is not used.

Forecast Model Analyzer produces forecasts and forecast metrics from across multiple models. The list of models included in [Forecast Algorithms](forecast-algorithims.md "forecast-algorithims.md").

## Viewing the forecast model analyzer details

To view the generated forecast model analyzer details, complete the following steps:

1. In the left navigation pane on the AWS Supply Chain dashboard, choose **Demand Planning** and then choose **Forecast Model Analyzer**.
2. Under **Forecast Model Analyzer**, you can view the meta data for each iteration of model analyzer including forecast summary that includes key metrics (such as the count of products, sites, channels and customers for which forecast were created),
   forecast scope such as time-interval, forecast horizon, forecast start date, the list of datasets used, forecast granularity, and input data used.
3. Under **Forecast(s) Vs. Actual Demand**, you can view a graph that displays the actual demand history, prior year demand, and the forecast to analyze trends and seasonality. You can adjust the **Viewing window start** and **Viewing window end** to review historical periods. Depending on the configured time-interval,

you can view the historical sales for 28 days, 52 weeks, 48 months, and 10 years. You can view and compare up to five forecast results simultaneously. 4. Under **Measures**, choose **Edit** to edit the selected forecast models. 5. Under **Model Overview and Selection**, the tables displays a summary of the forecast methods that were evaluated. In a back testing scenario, the table also displays aggregate forecast accuracy metrics such as, WAPE, Bias %, MAPE and sMAPE.
Additionally, you can choose **Select** to select the forecast model. The change will be applied during the subsequent forecast cycle. 6. Choose **Apply Selection to Demand Plan**.

You can view up to two forecast model analyzer results simultaneously. The most recent analyzer result remains fully interactive, allowing you to select and apply the preferred forecast method after careful evaluating
the products. This will be applied in the next forecast generation. The previous analyzer result is rendered as read-only. You can export both the results of the forecast method with actual demand history.
The exported data includes detailed information at the forecast period and granularity level, forecast by the P10/50/90 quantiles. For back test scenarios, the export will include actual demand data and corresponding
accuracy metrics.

You can modify the forecast selection method using the forecast model analyzer or under demand plan settings anytime. The changes will be applied during the subsequent forecast cycle.
The demand plan page will show meta data around the forecast method for current and the next forecast model.
