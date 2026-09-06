

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# PredictorMonitorEvaluation
<a name="API_PredictorMonitorEvaluation"></a>

Describes the results of a monitor evaluation.

## Contents
<a name="API_PredictorMonitorEvaluation_Contents"></a>

 ** EvaluationState **   <a name="forecast-Type-PredictorMonitorEvaluation-EvaluationState"></a>
The status of the monitor evaluation. The state can be `SUCCESS` or `FAILURE`.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** EvaluationTime **   <a name="forecast-Type-PredictorMonitorEvaluation-EvaluationTime"></a>
The timestamp that indicates when the monitor evaluation was started.   
Type: Timestamp  
Required: No

 ** Message **   <a name="forecast-Type-PredictorMonitorEvaluation-Message"></a>
Information about any errors that may have occurred during the monitor evaluation.  
Type: String  
Required: No

 ** MetricResults **   <a name="forecast-Type-PredictorMonitorEvaluation-MetricResults"></a>
A list of metrics Forecast calculated when monitoring a predictor. You can compare the value for each metric in the list to the metric's value in the [Baseline](API_Baseline.md) to see how your predictor's performance is changing.  
Type: Array of [MetricResult](API_MetricResult.md) objects  
Required: No

 ** MonitorArn **   <a name="forecast-Type-PredictorMonitorEvaluation-MonitorArn"></a>
The Amazon Resource Name (ARN) of the monitor resource.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: No

 ** MonitorDataSource **   <a name="forecast-Type-PredictorMonitorEvaluation-MonitorDataSource"></a>
The source of the data the monitor resource used during the evaluation.  
Type: [MonitorDataSource](API_MonitorDataSource.md) object  
Required: No

 ** NumItemsEvaluated **   <a name="forecast-Type-PredictorMonitorEvaluation-NumItemsEvaluated"></a>
The number of items considered during the evaluation.  
Type: Long  
Required: No

 ** PredictorEvent **   <a name="forecast-Type-PredictorMonitorEvaluation-PredictorEvent"></a>
Provides details about a predictor event, such as a retraining.  
Type: [PredictorEvent](API_PredictorEvent.md) object  
Required: No

 ** ResourceArn **   <a name="forecast-Type-PredictorMonitorEvaluation-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource to monitor.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: No

 ** WindowEndDatetime **   <a name="forecast-Type-PredictorMonitorEvaluation-WindowEndDatetime"></a>
The timestamp that indicates the end of the window that is used for monitor evaluation.  
Type: Timestamp  
Required: No

 ** WindowStartDatetime **   <a name="forecast-Type-PredictorMonitorEvaluation-WindowStartDatetime"></a>
The timestamp that indicates the start of the window that is used for monitor evaluation.  
Type: Timestamp  
Required: No

## See Also
<a name="API_PredictorMonitorEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/PredictorMonitorEvaluation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/PredictorMonitorEvaluation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/PredictorMonitorEvaluation) 