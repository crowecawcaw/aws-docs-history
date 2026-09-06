

# Actions, resources, and condition keys for Amazon Forecast
<a name="list_forecast"></a>

Amazon Forecast (service prefix: `forecast`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/forecast/latest/dg/api-reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/forecast/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/forecast/forecast.json) for this service.

**Topics**
+ [API operations defined by Amazon Forecast](#list_forecast-operations)
+ [Actions defined by Amazon Forecast](#list_forecast-actions-as-permissions)
+ [Permission-only actions for Amazon Forecast](#list_forecast-permission-only-actions)
+ [Resource types defined by Amazon Forecast](#list_forecast-resources-for-iam-policies)
+ [Condition keys for Amazon Forecast](#list_forecast-policy-keys)

## API operations defined by Amazon Forecast
<a name="list_forecast-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_forecast-actions-as-permissions).




- **   CreateAutoPredictor  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:CreateAutoPredictor](#list_forecast-action-CreateAutoPredictor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [forecast:TagResource](#list_forecast-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** forecast.amazonaws.com / **Access level:** Write

- **   CreateDataset  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:CreateDataset](#list_forecast-action-CreateDataset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [forecast:TagResource](#list_forecast-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** forecast.amazonaws.com / **Access level:** Write

- **   CreateDatasetGroup  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:CreateDatasetGroup](#list_forecast-action-CreateDatasetGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [forecast:TagResource](#list_forecast-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDatasetImportJob  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:CreateDatasetImportJob](#list_forecast-action-CreateDatasetImportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [forecast:TagResource](#list_forecast-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** forecast.amazonaws.com / **Access level:** Write

- **   CreateExplainability  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:CreateExplainability](#list_forecast-action-CreateExplainability)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [forecast:TagResource](#list_forecast-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateExplainabilityExport  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:CreateExplainabilityExport](#list_forecast-action-CreateExplainabilityExport)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [forecast:TagResource](#list_forecast-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** forecast.amazonaws.com / **Access level:** Write

- **   CreateForecast  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:CreateForecast](#list_forecast-action-CreateForecast)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [forecast:TagResource](#list_forecast-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateForecastExportJob  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:CreateForecastExportJob](#list_forecast-action-CreateForecastExportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [forecast:TagResource](#list_forecast-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** forecast.amazonaws.com / **Access level:** Write

- **   CreateMonitor  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:CreateMonitor](#list_forecast-action-CreateMonitor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [forecast:TagResource](#list_forecast-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePredictor  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:CreatePredictor](#list_forecast-action-CreatePredictor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [forecast:TagResource](#list_forecast-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** forecast.amazonaws.com / **Access level:** Write

- **   CreatePredictorBacktestExportJob  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:CreatePredictorBacktestExportJob](#list_forecast-action-CreatePredictorBacktestExportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [forecast:TagResource](#list_forecast-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** forecast.amazonaws.com / **Access level:** Write

- **   CreateWhatIfAnalysis  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:CreateWhatIfAnalysis](#list_forecast-action-CreateWhatIfAnalysis)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [forecast:TagResource](#list_forecast-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteDataset  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DeleteDataset](#list_forecast-action-DeleteDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDatasetGroup  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DeleteDatasetGroup](#list_forecast-action-DeleteDatasetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDatasetImportJob  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DeleteDatasetImportJob](#list_forecast-action-DeleteDatasetImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteExplainability  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DeleteExplainability](#list_forecast-action-DeleteExplainability) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteExplainabilityExport  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DeleteExplainabilityExport](#list_forecast-action-DeleteExplainabilityExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteForecast  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DeleteForecast](#list_forecast-action-DeleteForecast) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteForecastExportJob  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DeleteForecastExportJob](#list_forecast-action-DeleteForecastExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMonitor  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DeleteMonitor](#list_forecast-action-DeleteMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePredictor  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DeletePredictor](#list_forecast-action-DeletePredictor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePredictorBacktestExportJob  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DeletePredictorBacktestExportJob](#list_forecast-action-DeletePredictorBacktestExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourceTree  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DeleteResourceTree](#list_forecast-action-DeleteResourceTree) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWhatIfAnalysis  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DeleteWhatIfAnalysis](#list_forecast-action-DeleteWhatIfAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAutoPredictor  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DescribeAutoPredictor](#list_forecast-action-DescribeAutoPredictor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataset  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DescribeDataset](#list_forecast-action-DescribeDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDatasetGroup  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DescribeDatasetGroup](#list_forecast-action-DescribeDatasetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDatasetImportJob  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DescribeDatasetImportJob](#list_forecast-action-DescribeDatasetImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExplainability  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DescribeExplainability](#list_forecast-action-DescribeExplainability) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExplainabilityExport  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DescribeExplainabilityExport](#list_forecast-action-DescribeExplainabilityExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeForecast  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DescribeForecast](#list_forecast-action-DescribeForecast) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeForecastExportJob  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DescribeForecastExportJob](#list_forecast-action-DescribeForecastExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMonitor  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DescribeMonitor](#list_forecast-action-DescribeMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePredictor  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DescribePredictor](#list_forecast-action-DescribePredictor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePredictorBacktestExportJob  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DescribePredictorBacktestExportJob](#list_forecast-action-DescribePredictorBacktestExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWhatIfAnalysis  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DescribeWhatIfAnalysis](#list_forecast-action-DescribeWhatIfAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWhatIfForecast  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:DescribeWhatIfForecast](#list_forecast-action-DescribeWhatIfForecast) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccuracyMetrics  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:GetAccuracyMetrics](#list_forecast-action-GetAccuracyMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDatasetGroups  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListDatasetGroups](#list_forecast-action-ListDatasetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDatasetImportJobs  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListDatasetImportJobs](#list_forecast-action-ListDatasetImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDatasets  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListDatasets](#list_forecast-action-ListDatasets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListExplainabilities  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListExplainabilities](#list_forecast-action-ListExplainabilities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListExplainabilityExports  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListExplainabilityExports](#list_forecast-action-ListExplainabilityExports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListForecastExportJobs  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListForecastExportJobs](#list_forecast-action-ListForecastExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListForecasts  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListForecasts](#list_forecast-action-ListForecasts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListMonitorEvaluations  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListMonitorEvaluations](#list_forecast-action-ListMonitorEvaluations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListMonitors  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListMonitors](#list_forecast-action-ListMonitors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPredictorBacktestExportJobs  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListPredictorBacktestExportJobs](#list_forecast-action-ListPredictorBacktestExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPredictors  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListPredictors](#list_forecast-action-ListPredictors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListTagsForResource](#list_forecast-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWhatIfAnalyses  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListWhatIfAnalyses](#list_forecast-action-ListWhatIfAnalyses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWhatIfForecastExports  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListWhatIfForecastExports](#list_forecast-action-ListWhatIfForecastExports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWhatIfForecasts  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ListWhatIfForecasts](#list_forecast-action-ListWhatIfForecasts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ResumeResource  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:ResumeResource](#list_forecast-action-ResumeResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopResource  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:StopResource](#list_forecast-action-StopResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:TagResource](#list_forecast-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:UntagResource](#list_forecast-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDatasetGroup  **
  - **SDK client:** forecast
  - **IAM action:**  [forecast:UpdateDatasetGroup](#list_forecast-action-UpdateDatasetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   QueryForecast  **
  - **SDK client:** forecastquery
  - **IAM action:**  [forecast:QueryForecast](#list_forecast-action-QueryForecast) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   QueryWhatIfForecast  **
  - **SDK client:** forecastquery
  - **IAM action:**  [forecast:QueryWhatIfForecast](#list_forecast-action-QueryWhatIfForecast) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon Forecast
<a name="list_forecast-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateAutoPredictor](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateAutoPredictor.html)  **
  - **Description:** Grants permission to create an auto predictor
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html)  **
  - **Description:** Grants permission to create a dataset
  - **Resource types (\*required):** [dataset\*](#list_forecast-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html)  **
  - **Description:** Grants permission to create a dataset group
  - **Resource types (\*required):** [datasetGroup\*](#list_forecast-resource-datasetGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDatasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html)  **
  - **Description:** Grants permission to create a dataset import job
  - **Resource types (\*required):** [datasetImportJob\*](#list_forecast-resource-datasetImportJob)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [CreateExplainability](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateExplainability.html)  **
  - **Description:** Grants permission to create an explainability
  - **Resource types (\*required):** [forecast\*](#list_forecast-resource-forecast)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [CreateExplainabilityExport](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateExplainabilityExport.html)  **
  - **Description:** Grants permission to create an explainability export using an explainability resource
  - **Resource types (\*required):** [explainability\*](#list_forecast-resource-explainability)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [CreateForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateForecast.html)  **
  - **Description:** Grants permission to create a forecast
  - **Resource types (\*required):** [predictor\*](#list_forecast-resource-predictor)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [CreateForecastExportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateForecastExportJob.html)  **
  - **Description:** Grants permission to create a forecast export job using a forecast resource
  - **Resource types (\*required):** [forecast\*](#list_forecast-resource-forecast)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMonitor](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateMonitor.html)  **
  - **Description:** Grants permission to create an monitor using a Predictor resource
  - **Resource types (\*required):** [predictor\*](#list_forecast-resource-predictor)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePredictor](https://docs.aws.amazon.com/forecast/latest/dg/API_CreatePredictor.html)  **
  - **Description:** Grants permission to create a predictor
  - **Resource types (\*required):** [datasetGroup\*](#list_forecast-resource-datasetGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePredictorBacktestExportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreatePredictorBacktestExportJob.html)  **
  - **Description:** Grants permission to create a predictor backtest export job using a predictor
  - **Resource types (\*required):** [predictor\*](#list_forecast-resource-predictor)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWhatIfAnalysis](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfAnalysis.html)  **
  - **Description:** Grants permission to create a what-if analysis
  - **Resource types (\*required):** [forecast\*](#list_forecast-resource-forecast)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWhatIfForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfForecast.html)  **
  - **Description:** Grants permission to create a what-if forecast
  - **Resource types (\*required):** [whatIfAnalysis\*](#list_forecast-resource-whatIfAnalysis)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWhatIfForecastExport](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfForecastExport.html)  **
  - **Description:** Grants permission to create a what-if forecast export using what-if forecast resources
  - **Resource types (\*required):** [whatIfForecast\*](#list_forecast-resource-whatIfForecast)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteDataset.html)  **
  - **Description:** Grants permission to delete a dataset
  - **Resource types (\*required):** [dataset\*](#list_forecast-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteDatasetGroup.html)  **
  - **Description:** Grants permission to delete a dataset group
  - **Resource types (\*required):** [datasetGroup\*](#list_forecast-resource-datasetGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDatasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteDatasetImportJob.html)  **
  - **Description:** Grants permission to delete a dataset import job
  - **Resource types (\*required):** [datasetImportJob\*](#list_forecast-resource-datasetImportJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExplainability](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteExplainability.html)  **
  - **Description:** Grants permission to delete an explainability
  - **Resource types (\*required):** [explainability\*](#list_forecast-resource-explainability)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExplainabilityExport](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteExplainabilityExport.html)  **
  - **Description:** Grants permission to delete an explainability export
  - **Resource types (\*required):** [explainabilityExport\*](#list_forecast-resource-explainabilityExport)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteForecast.html)  **
  - **Description:** Grants permission to delete a forecast
  - **Resource types (\*required):** [forecast\*](#list_forecast-resource-forecast)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteForecastExportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteForecastExportJob.html)  **
  - **Description:** Grants permission to delete a forecast export job
  - **Resource types (\*required):** [forecastExport\*](#list_forecast-resource-forecastExport)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMonitor](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteMonitor.html)  **
  - **Description:** Grants permission to delete a monitor resource
  - **Resource types (\*required):** [monitor\*](#list_forecast-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePredictor](https://docs.aws.amazon.com/forecast/latest/dg/API_DeletePredictor.html)  **
  - **Description:** Grants permission to delete a predictor
  - **Resource types (\*required):** [predictor\*](#list_forecast-resource-predictor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePredictorBacktestExportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_DeletePredictorBacktestExportJob.html)  **
  - **Description:** Grants permission to delete a predictor backtest export job
  - **Resource types (\*required):** [predictorBacktestExportJob\*](#list_forecast-resource-predictorBacktestExportJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourceTree](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteResourceTree.html)  **
  - **Description:** Grants permission to delete a resource and its child resources
  - **Resource types (\*required):** [dataset\*](#list_forecast-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datasetGroup\*](#list_forecast-resource-datasetGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datasetImportJob\*](#list_forecast-resource-datasetImportJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [endpoint\*](#list_forecast-resource-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [explainability\*](#list_forecast-resource-explainability) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [explainabilityExport\*](#list_forecast-resource-explainabilityExport) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [forecast\*](#list_forecast-resource-forecast) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [forecastExport\*](#list_forecast-resource-forecastExport) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [monitor\*](#list_forecast-resource-monitor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [predictor\*](#list_forecast-resource-predictor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [predictorBacktestExportJob\*](#list_forecast-resource-predictorBacktestExportJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [whatIfAnalysis\*](#list_forecast-resource-whatIfAnalysis) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [whatIfForecast\*](#list_forecast-resource-whatIfForecast) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [whatIfForecastExport\*](#list_forecast-resource-whatIfForecastExport) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWhatIfAnalysis](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteWhatIfAnalysis.html)  **
  - **Description:** Grants permission to delete a what-if analysis
  - **Resource types (\*required):** [whatIfAnalysis\*](#list_forecast-resource-whatIfAnalysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWhatIfForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteWhatIfForecast.html)  **
  - **Description:** Grants permission to delete a what-if forecast
  - **Resource types (\*required):** [whatIfForecast\*](#list_forecast-resource-whatIfForecast)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWhatIfForecastExport](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteWhatIfForecastExport.html)  **
  - **Description:** Grants permission to delete a what-if forecast export
  - **Resource types (\*required):** [whatIfForecastExport\*](#list_forecast-resource-whatIfForecastExport)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAutoPredictor](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeAutoPredictor.html)  **
  - **Description:** Grants permission to describe an auto predictor
  - **Resource types (\*required):** [predictor\*](#list_forecast-resource-predictor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDataset.html)  **
  - **Description:** Grants permission to describe a dataset
  - **Resource types (\*required):** [dataset\*](#list_forecast-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetGroup.html)  **
  - **Description:** Grants permission to describe a dataset group
  - **Resource types (\*required):** [datasetGroup\*](#list_forecast-resource-datasetGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDatasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetImportJob.html)  **
  - **Description:** Grants permission to describe a dataset import job
  - **Resource types (\*required):** [datasetImportJob\*](#list_forecast-resource-datasetImportJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeExplainability](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeExplainability.html)  **
  - **Description:** Grants permission to describe an explainability
  - **Resource types (\*required):** [explainability\*](#list_forecast-resource-explainability)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeExplainabilityExport](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeExplainabilityExport.html)  **
  - **Description:** Grants permission to describe an explainability export
  - **Resource types (\*required):** [explainabilityExport\*](#list_forecast-resource-explainabilityExport)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeForecast.html)  **
  - **Description:** Grants permission to describe a forecast
  - **Resource types (\*required):** [forecast\*](#list_forecast-resource-forecast)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeForecastExportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeForecastExportJob.html)  **
  - **Description:** Grants permission to describe a forecast export job
  - **Resource types (\*required):** [forecastExport\*](#list_forecast-resource-forecastExport)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMonitor](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeMonitor.html)  **
  - **Description:** Grants permission to describe an monitor resource
  - **Resource types (\*required):** [monitor\*](#list_forecast-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePredictor](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribePredictor.html)  **
  - **Description:** Grants permission to describe a predictor
  - **Resource types (\*required):** [predictor\*](#list_forecast-resource-predictor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePredictorBacktestExportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribePredictorBacktestExportJob.html)  **
  - **Description:** Grants permission to describe a predictor backtest export job
  - **Resource types (\*required):** [predictorBacktestExportJob\*](#list_forecast-resource-predictorBacktestExportJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWhatIfAnalysis](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeWhatIfAnalysis.html)  **
  - **Description:** Grants permission to describe a what-if analysis
  - **Resource types (\*required):** [whatIfAnalysis\*](#list_forecast-resource-whatIfAnalysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWhatIfForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeWhatIfForecast.html)  **
  - **Description:** Grants permission to describe a what-if forecast
  - **Resource types (\*required):** [whatIfForecast\*](#list_forecast-resource-whatIfForecast)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWhatIfForecastExport](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeWhatIfForecastExport.html)  **
  - **Description:** Grants permission to describe a what-if forecast export
  - **Resource types (\*required):** [whatIfForecastExport\*](#list_forecast-resource-whatIfForecastExport)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAccuracyMetrics](https://docs.aws.amazon.com/forecast/latest/dg/API_GetAccuracyMetrics.html)  **
  - **Description:** Grants permission to get the Accuracy Metrics for a predictor
  - **Resource types (\*required):** [predictor\*](#list_forecast-resource-predictor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDatasetGroups](https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasetGroups.html)  **
  - **Description:** Grants permission to list all the dataset groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDatasetImportJobs](https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasetImportJobs.html)  **
  - **Description:** Grants permission to list all the dataset import jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDatasets](https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasets.html)  **
  - **Description:** Grants permission to list all the datasets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListExplainabilities](https://docs.aws.amazon.com/forecast/latest/dg/API_ListExplainabilities.html)  **
  - **Description:** Grants permission to list all the explainabilities
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListExplainabilityExports](https://docs.aws.amazon.com/forecast/latest/dg/API_ListExplainabilityExports.html)  **
  - **Description:** Grants permission to list all the explainability exports
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListForecastExportJobs](https://docs.aws.amazon.com/forecast/latest/dg/API_ListForecastExportJobs.html)  **
  - **Description:** Grants permission to list all the forecast export jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListForecasts](https://docs.aws.amazon.com/forecast/latest/dg/API_ListForecasts.html)  **
  - **Description:** Grants permission to list all the forecasts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListMonitorEvaluations](https://docs.aws.amazon.com/forecast/latest/dg/API_ListMonitorEvaluations.html)  **
  - **Description:** Grants permission to list all the monitor evaluation result for a monitor
  - **Resource types (\*required):** [monitor\*](#list_forecast-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListMonitors](https://docs.aws.amazon.com/forecast/latest/dg/API_ListMonitors.html)  **
  - **Description:** Grants permission to list all the monitor resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPredictorBacktestExportJobs](https://docs.aws.amazon.com/forecast/latest/dg/API_ListPredictorBacktestExportJobs.html)  **
  - **Description:** Grants permission to list all the predictor backtest export jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPredictors](https://docs.aws.amazon.com/forecast/latest/dg/API_ListPredictors.html)  **
  - **Description:** Grants permission to list all the predictors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/forecast/latest/dg/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for an Amazon Forecast resource
  - **Resource types (\*required):** [dataset](#list_forecast-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datasetGroup](#list_forecast-resource-datasetGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datasetImportJob](#list_forecast-resource-datasetImportJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [endpoint](#list_forecast-resource-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [explainability](#list_forecast-resource-explainability) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [explainabilityExport](#list_forecast-resource-explainabilityExport) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [forecast](#list_forecast-resource-forecast) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [forecastExport](#list_forecast-resource-forecastExport) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [monitor](#list_forecast-resource-monitor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [predictor](#list_forecast-resource-predictor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [predictorBacktestExportJob](#list_forecast-resource-predictorBacktestExportJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [whatIfAnalysis](#list_forecast-resource-whatIfAnalysis) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [whatIfForecast](#list_forecast-resource-whatIfForecast) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [whatIfForecastExport](#list_forecast-resource-whatIfForecastExport) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWhatIfAnalyses](https://docs.aws.amazon.com/forecast/latest/dg/API_ListWhatIfAnalyses.html)  **
  - **Description:** Grants permission to list all the what-if analyses
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListWhatIfForecastExports](https://docs.aws.amazon.com/forecast/latest/dg/API_ListWhatIfForecastExports.html)  **
  - **Description:** Grants permission to list all the what-if forecast exports
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListWhatIfForecasts](https://docs.aws.amazon.com/forecast/latest/dg/API_ListWhatIfForecasts.html)  **
  - **Description:** Grants permission to list all the what-if forecasts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [QueryForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_forecastquery_QueryForecast.html)  **
  - **Description:** Grants permission to retrieve a forecast for a single item
  - **Resource types (\*required):** [forecast\*](#list_forecast-resource-forecast)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [QueryWhatIfForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_forecastquery_QueryWhatIfForecast.html)  **
  - **Description:** Grants permission to retrieve a what-if forecast for a single item
  - **Resource types (\*required):** [whatIfForecast\*](#list_forecast-resource-whatIfForecast)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ResumeResource](https://docs.aws.amazon.com/forecast/latest/dg/API_ResumeResource.html)  **
  - **Description:** Grants permission to resume Amazon Forecast resource jobs
  - **Resource types (\*required):** [monitor\*](#list_forecast-resource-monitor)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [StopResource](https://docs.aws.amazon.com/forecast/latest/dg/API_StopResource.html)  **
  - **Description:** Grants permission to stop Amazon Forecast resource jobs
  - **Resource types (\*required):** [datasetImportJob\*](#list_forecast-resource-datasetImportJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [endpoint\*](#list_forecast-resource-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [explainability\*](#list_forecast-resource-explainability) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [explainabilityExport\*](#list_forecast-resource-explainabilityExport) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [forecast\*](#list_forecast-resource-forecast) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [forecastExport\*](#list_forecast-resource-forecastExport) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [monitor\*](#list_forecast-resource-monitor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [predictor\*](#list_forecast-resource-predictor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [predictorBacktestExportJob\*](#list_forecast-resource-predictorBacktestExportJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [whatIfAnalysis\*](#list_forecast-resource-whatIfAnalysis) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [whatIfForecast\*](#list_forecast-resource-whatIfForecast) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [whatIfForecastExport\*](#list_forecast-resource-whatIfForecastExport) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/forecast/latest/dg/API_TagResource.html)  **
  - **Description:** Grants permission to associate the specified tags to a resource
  - **Resource types (\*required):** [dataset](#list_forecast-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [datasetGroup](#list_forecast-resource-datasetGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [datasetImportJob](#list_forecast-resource-datasetImportJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [endpoint](#list_forecast-resource-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [explainability](#list_forecast-resource-explainability) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [explainabilityExport](#list_forecast-resource-explainabilityExport) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [forecast](#list_forecast-resource-forecast) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [forecastExport](#list_forecast-resource-forecastExport) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [monitor](#list_forecast-resource-monitor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [predictor](#list_forecast-resource-predictor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [predictorBacktestExportJob](#list_forecast-resource-predictorBacktestExportJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [whatIfAnalysis](#list_forecast-resource-whatIfAnalysis) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [whatIfForecast](#list_forecast-resource-whatIfForecast) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [whatIfForecastExport](#list_forecast-resource-whatIfForecastExport) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/forecast/latest/dg/API_UntagResource.html)  **
  - **Description:** Grants permission to delete the specified tags for a resource
  - **Resource types (\*required):** [dataset](#list_forecast-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [datasetGroup](#list_forecast-resource-datasetGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [datasetImportJob](#list_forecast-resource-datasetImportJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [endpoint](#list_forecast-resource-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [explainability](#list_forecast-resource-explainability) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [explainabilityExport](#list_forecast-resource-explainabilityExport) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [forecast](#list_forecast-resource-forecast) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [forecastExport](#list_forecast-resource-forecastExport) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [monitor](#list_forecast-resource-monitor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [predictor](#list_forecast-resource-predictor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [predictorBacktestExportJob](#list_forecast-resource-predictorBacktestExportJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [whatIfAnalysis](#list_forecast-resource-whatIfAnalysis) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [whatIfForecast](#list_forecast-resource-whatIfForecast) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Resource types (\*required):** [whatIfForecastExport](#list_forecast-resource-whatIfForecastExport) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_UpdateDatasetGroup.html)  **
  - **Description:** Grants permission to update a dataset group
  - **Resource types (\*required):** [dataset\*](#list_forecast-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datasetGroup\*](#list_forecast-resource-datasetGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Forecast
<a name="list_forecast-permission-only-actions"></a>

The following actions are defined by Amazon Forecast but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateForecastEndpoint](https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html)  **
  - **Description:** Grants permission to create an endpoint using a Predictor resource
  - **Resource types (\*required):** [predictor\*](#list_forecast-resource-predictor)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_forecast-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_forecast-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteForecastEndpoint](https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html)  **
  - **Description:** Grants permission to delete an endpoint resource
  - **Resource types (\*required):** [endpoint\*](#list_forecast-resource-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeForecastEndpoint](https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html)  **
  - **Description:** Grants permission to describe an endpoint resource
  - **Resource types (\*required):** [endpoint\*](#list_forecast-resource-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecentForecastContext](https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html)  **
  - **Description:** Grants permission to get the forecast context of a timeseries for an endpoint
  - **Resource types (\*required):** [endpoint\*](#list_forecast-resource-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeForecastEndpoint](https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html)  **
  - **Description:** Grants permission to invoke the endpoint to get forecast for a timeseries
  - **Resource types (\*required):** [endpoint\*](#list_forecast-resource-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Resource types defined by Amazon Forecast
<a name="list_forecast-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [algorithm](https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-choosing-recipes.html)  | arn:${Partition}:forecast:::algorithm/${ResourceId} |   | 
|  [dataset](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html)  | arn:${Partition}:forecast:${Region}:${Account}:dataset/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_) | 
|  [datasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html)  | arn:${Partition}:forecast:${Region}:${Account}:dataset-group/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_) | 
|  [datasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html)  | arn:${Partition}:forecast:${Region}:${Account}:dataset-import-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_) | 
|  [endpoint](https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html)  | arn:${Partition}:forecast:${Region}:${Account}:forecast-endpoint/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_) | 
|  [explainability](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateExplainability.html)  | arn:${Partition}:forecast:${Region}:${Account}:explainability/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_) | 
|  [explainabilityExport](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateExplainabilityExport.html)  | arn:${Partition}:forecast:${Region}:${Account}:explainability-export/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_) | 
|  [forecast](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateForecast.html)  | arn:${Partition}:forecast:${Region}:${Account}:forecast/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_) | 
|  [forecastExport](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateForecastExportJob.html)  | arn:${Partition}:forecast:${Region}:${Account}:forecast-export-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_) | 
|  [monitor](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateMonitor.html)  | arn:${Partition}:forecast:${Region}:${Account}:monitor/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_) | 
|  [predictor](https://docs.aws.amazon.com/forecast/latest/dg/API_CreatePredictor.html)  | arn:${Partition}:forecast:${Region}:${Account}:predictor/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_) | 
|  [predictorBacktestExportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreatePredictorBacktestExportJob.html)  | arn:${Partition}:forecast:${Region}:${Account}:predictor-backtest-export-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_) | 
|  [whatIfAnalysis](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfAnalysis.html)  | arn:${Partition}:forecast:${Region}:${Account}:what-if-analysis/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_) | 
|  [whatIfForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfForecast.html)  | arn:${Partition}:forecast:${Region}:${Account}:what-if-forecast/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_) | 
|  [whatIfForecastExport](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfForecastExport.html)  | arn:${Partition}:forecast:${Region}:${Account}:what-if-forecast-export/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_forecast-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Forecast
<a name="list_forecast-policy-keys"></a>

Amazon Forecast defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 