Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Receiving Job Status Notifications

You can have Amazon EventBridge or Amazon CloudWatch Events notify you with status updates for ongoing
Amazon Forecast resource jobs, such as creating predictors or forecasts. EventBridge and CloudWatch Events deliver a near real-time stream of system events
that describe changes in Amazon Web Services (AWS) resources. For example, you can set up an
event to notify you when a Forecast predictor finishes training.

Events are emitted on a best-effort basis. For more information about events, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md") or the [Amazon CloudWatch Events User Guide](../../../AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.md "../../../AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.md").

###### Note

We recommend using Amazon EventBridge to manage events. CloudWatch Events and EventBridge use the same API and
provide the same functionality, but EventBridge provides more features. Changes that you make
in either CloudWatch or EventBridge will appear in each console. For more information, see [Amazon EventBridge](../../../eventbridge/index.md "../../../eventbridge/index.md").

###### Topics

- [Monitoring Forecast Resource Jobs](#forecast-events "#forecast-events")
- [Creating an EventBridge Rule for Job Status Notifications](#create-rule-event-bridge "#create-rule-event-bridge")
- [Creating a CloudWatch Events Rule for Job Status Notifications](#create-rule-cloud-watch "#create-rule-cloud-watch")

## Monitoring Forecast Resource Jobs

An event indicates a change in your AWS environment, and a rule matches incoming
events and routes them to targets for processing. You can set up rules to match Forecast
events and route them to one or more target functions or streams. EventBridge and CloudWatch Events
detect events as they occur and invoke the target in the matching rule.

The following table lists the Forecast resource jobs and their status change events, which you can monitor.

| Resource Job                                                                                                          | Status Change Event Name                               | Status                                                    |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------- |
| [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md")                               | Forecast Dataset Import Job State Change               | ACTIVE, CREATE_IN_PROGRESS, CREATE_FAILED, CREATE_STOPPED |
| [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md")                                                    | Forecast Predictor Creation State Change               | ACTIVE, CREATE_IN_PROGRESS, CREATE_FAILED, CREATE_STOPPED |
| [CreateForecast](API_CreateForecast.md "API_CreateForecast.md")                                                       | Forecast Forecast Creation State Change                | ACTIVE, CREATE_IN_PROGRESS, CREATE_FAILED, CREATE_STOPPED |
| [CreateExplainability](API_CreateExplainability.md "API_CreateExplainability.md")                                     | Forecast Explainability Creation State Change          | ACTIVE, CREATE_IN_PROGRESS, CREATE_FAILED, CREATE_STOPPED |
| [CreatePredictorBacktestExportJob](API_CreatePredictorBacktestExportJob.md "API_CreatePredictorBacktestExportJob.md") | Forecast Predictor Backtest Export Job State Change    | ACTIVE, CREATE_IN_PROGRESS, CREATE_FAILED, CREATE_STOPPED |
| [CreateForecastExportJob](API_CreateForecastExportJob.md "API_CreateForecastExportJob.md")                            | Forecast Forecast Export Job State Change              | ACTIVE, CREATE_IN_PROGRESS, CREATE_FAILED, CREATE_STOPPED |
| [CreateExplainabilityExport](API_CreateExplainabilityExport.md "API_CreateExplainabilityExport.md")                   | Forecast Explainability Export Creation State Change   | ACTIVE, CREATE_IN_PROGRESS, CREATE_FAILED, CREATE_STOPPED |
| [CreateWhatIfAnalysis](API_CreateWhatIfAnalysis.md "API_CreateWhatIfAnalysis.md")                                     | Forecast What-if Analysis Creation State Change        | ACTIVE, CREATE_IN_PROGRESS, CREATE_FAILED, CREATE_STOPPED |
| [CreateWhatIfForecast](API_CreateWhatIfForecast.md "API_CreateWhatIfForecast.md")                                     | Forecast What-if Forecast Creation State Change        | ACTIVE, CREATE_IN_PROGRESS, CREATE_FAILED, CREATE_STOPPED |
| [CreateWhatIfForecastExport](API_CreateWhatIfForecastExport.md "API_CreateWhatIfForecastExport.md")                   | Forecast What-if Forecast Export Creation State Change | ACTIVE, CREATE_IN_PROGRESS, CREATE_FAILED, CREATE_STOPPED |
| [DeleteDataset](API_DeleteDataset.md "API_DeleteDataset.md")                                                          | Forecast Dataset Deletion State Change                 | DELETE_IN_PROGRESS, DELETE_FAILED                         |
| [DeleteDatasetImportJob](API_DeleteDatasetImportJob.md "API_DeleteDatasetImportJob.md")                               | Forecast Dataset Import Job Deletion State Change      | DELETE_IN_PROGRESS, DELETE_FAILED                         |
| [DeletePredictor](API_DeletePredictor.md "API_DeletePredictor.md")                                                    | Forecast Predictor Deletion State Change               | DELETE_IN_PROGRESS, DELETE_FAILED                         |
| [DeleteForecast](API_DeleteForecast.md "API_DeleteForecast.md")                                                       | Forecast Forecast Deletion State Change                | DELETE_IN_PROGRESS, DELETE_FAILED                         |
| [DeleteExplainability](API_DeleteExplainability.md "API_DeleteExplainability.md")                                     | Forecast Explainability Deletion State Change          | DELETE_IN_PROGRESS, DELETE_FAILED                         |
| [DeleteExplainabilityExport](API_DeleteExplainabilityExport.md "API_DeleteExplainabilityExport.md")                   | Forecast Explainability Export Deletion State Change   | DELETE_IN_PROGRESS, DELETE_FAILED                         |
| [DeleteWhatIfAnalysis](API_DeleteWhatIfAnalysis.md "API_DeleteWhatIfAnalysis.md")                                     | Forecast What-if Analysis Deletion State Change        | DELETE_IN_PROGRESS, DELETE_FAILED                         |
| [DeleteWhatIfForecast](API_DeleteWhatIfForecast.md "API_DeleteWhatIfForecast.md")                                     | Forecast What-if Forecast Deletion State Change        | DELETE_IN_PROGRESS, DELETE_FAILED                         |
| [DeleteWhatIfForecastExportJob](API_DeleteWhatIfForecastExport.md "API_DeleteWhatIfForecastExport.md")                | Forecast What-if Forecast Export Deletion State Change | DELETE_IN_PROGRESS, DELETE_FAILED                         |

Notifications contain information about the resource, including the Amazon Resource Name (ARN), job status, job duration (in minutes),
and, if the job failed, an error message. Delete event notifications don't include a `Duration` field.
The following is an example notification:

```
{
    "version": "0",
    "id": "017fcb6d-7ca3-ebf8-819e-3e0fa956ee17",
    "detail-type": "Forecast Dataset Import Job State Change",
    "source": "aws.forecast",
    "account": "000000000001",
    "time": "2021-02-19T05:45:51Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:forecast:us-west-2:000000000001:dataset/example_data"
    ],
    "detail": {
        "Arn": "arn:aws:forecast:us-west-2:000000000001:dataset/example_data",
        "Duration": 60,
        "Status": "ACTIVE",
    }
}
```

## Creating an EventBridge Rule for Job Status Notifications

To create an EventBridge rule to notify you of status changes for ongoing Forecast resource jobs, see
[Creating a rule for an AWS service](../../../eventbridge/latest/userguide/create-eventbridge-rule.md "../../../eventbridge/latest/userguide/create-eventbridge-rule.md")
in the _Amazon EventBridge User Guide_. In the procedure, for **Service name**, choose **Amazon Forecast**.
For **Event type**, choose the Forecast event to monitor. See [Monitoring Forecast Resource Jobs](#forecast-events "#forecast-events") for
the list of Forecast events.

## Creating a CloudWatch Events Rule for Job Status Notifications

To create an CloudWatch Events rule to notify you of status changes for ongoing Forecast resource jobs, see
[Creating a CloudWatch Events Rule That Triggers on an Event](../../../AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.md "../../../AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.md")
in the _Amazon CloudWatch User Guide_. In the procedure, for **Service name**, choose **Amazon Forecast**.
For **Event type**, choose the Forecast event to monitor. See [Monitoring Forecast Resource Jobs](#forecast-events "#forecast-events") for a list
of Forecast events.
