

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# MonitorDataSource
<a name="API_MonitorDataSource"></a>

The source of the data the monitor used during the evaluation.

## Contents
<a name="API_MonitorDataSource_Contents"></a>

 ** DatasetImportJobArn **   <a name="forecast-Type-MonitorDataSource-DatasetImportJobArn"></a>
The Amazon Resource Name (ARN) of the dataset import job used to import the data that initiated the monitor evaluation.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: No

 ** ForecastArn **   <a name="forecast-Type-MonitorDataSource-ForecastArn"></a>
The Amazon Resource Name (ARN) of the forecast the monitor used during the evaluation.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: No

 ** PredictorArn **   <a name="forecast-Type-MonitorDataSource-PredictorArn"></a>
The Amazon Resource Name (ARN) of the predictor resource you are monitoring.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: No

## See Also
<a name="API_MonitorDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/MonitorDataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/MonitorDataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/MonitorDataSource) 