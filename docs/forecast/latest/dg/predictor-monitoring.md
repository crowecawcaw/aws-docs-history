Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Predictor Monitoring

###### Note

If you enable predictor monitoring, Amazon Forecast will store data from each of your forecasts for predictor
performance analysis, even after deleting forecast data. To delete this data, delete the monitoring resource.

Predictor monitoring allows you to see how your predictor's performance changes over time.
A variety of factors can cause performance changes, such as economic developments or changes in your customer's behavior.

For example, consider a forecasting scenario where the target is `sales` and
there are two related attributes: `price` and `color`. In the months after creating your first predictor,
certain colors might unexpectedly become more popular with your customers. This might drive up sales for items with this attribute. This new data could impact
your predictor's performance and the accuracy of the forecasts it generates.

With predictor monitoring enabled, Forecast analyzes your predictor's performance as you generate forecasts and import more data. Forecast compares the new data to the earlier forecasts
to detect any changes in performance.
You can view graphs of how different accuracy metrics have changed over time in the Forecast console. Or you can get monitoring results with the
[ListMonitorEvaluations](API_ListMonitorEvaluations.md "API_ListMonitorEvaluations.md")
operation.

Predictor monitoring can help decide if it is time to retrain your predictor. If performance is degrading, you might want to retrain the predictor on more
recent data. If you choose to retrain your predictor, the new
predictor will include the monitoring data from the previous one. You might also
use predictor monitoring to gather contextual data about your production environment, or to perform comparisons for different experiments.

Predictor monitoring is only available for AutoPredictors.
You can upgrade existing legacy predictors to AutoPredictor. See [Upgrading to AutoPredictor](howitworks-predictor.md#upgrading-autopredictor "howitworks-predictor.md#upgrading-autopredictor").

###### Topics

- [Predictor Monitoring Workflow](#predictor-monitoring-workflow "#predictor-monitoring-workflow")
- [Enabling Predictor
  Monitoring](enabling-predictor-monitoring.md "enabling-predictor-monitoring.md")
- [Viewing Monitoring Results](predictor-monitoring-results.md "predictor-monitoring-results.md")
- [Restrictions and Best
  Practices](#predictor-monitoring-best-practices "#predictor-monitoring-best-practices")

## Predictor Monitoring Workflow

To get predictor monitoring results, you must first use your predictor to generate a forecast and then import
more data. The monitoring workflow is as follows.

1.  Enable predictor monitoring for an auto predictor:
    - Create a new predictor with monitoring enabled. See [Enabling Predictor
      Monitoring for a New Predictor](enabling-predictor-monitoring.md#enabling-predictor-monitoring-new "enabling-predictor-monitoring.md#enabling-predictor-monitoring-new").
    - Or enable monitoring for an existing predictor. See [Enabling Predictor
      Monitoring for an Existing Predictor](enabling-predictor-monitoring.md#enabling-predictor-monitoring-existing "enabling-predictor-monitoring.md#enabling-predictor-monitoring-existing").

2.  Use the predictor to generate one or more forecasts.
3.  Import more data. For information about importing data into Forecast, see [Importing Datasets](howitworks-datasets-groups.md "howitworks-datasets-groups.md").
4.  View predictor monitoring results:

        * You can view results on the **Monitoring** tab for your predictor.
        * Or you can get monitoring results with the [ListMonitorEvaluations](API_ListMonitorEvaluations.md "API_ListMonitorEvaluations.md") operation.

    For more information, see [Viewing Monitoring Results](predictor-monitoring-results.md "predictor-monitoring-results.md").

## Restrictions and Best

Practices

Consider the following restrictions and best practices when working with predictor
monitoring.

- **Predictor monitoring is only available for auto predictors** – You cannot enable monitoring for
  legacy predictors that were created with AutoML or through manual selection. See
  [Upgrading to
  AutoPredictor](howitworks-predictor.md#upgrading-autopredictor "howitworks-predictor.md#upgrading-autopredictor").
- **Predictor monitoring is unique per auto predictor** – You can only
  create one monitor per auto predictor.
- **Predictor monitoring requires new data and generating
  forecasts** – As you import new data that is used to
  generate new forecasts, predictor monitoring results become available. If you
  are not importing new data or the newly imported data does not cover a full
  forecast horizon, you will not see monitoring results.
- **Predictor monitoring requires new forecasts** – You must
  continuously generate new forecasts to generate monitoring results. If you are not generating new forecasts,
  you will not see monitoring results.
- **Amazon Forecast will store data from each of your forecasts for
  predictor performance analysis** – Forecast stores these data
  even if you delete forecasts. To delete these data, delete the associated
  monitor.
- The [StopResource](API_StopResource.md "API_StopResource.md") operation will stop all current
  evaluations and all future evaluations.
- The avgWQL metric is available only when you generate forecasts for quantiles other than the mean.
- In-progress monitor evaluations are not shown in the [ListMonitorEvaluations](API_ListMonitorEvaluations.md "API_ListMonitorEvaluations.md") operation.
