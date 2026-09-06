

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# PredictorEvent
<a name="API_PredictorEvent"></a>

Provides details about a predictor event, such as a retraining.

## Contents
<a name="API_PredictorEvent_Contents"></a>

 ** Datetime **   <a name="forecast-Type-PredictorEvent-Datetime"></a>
The timestamp for when the event occurred.  
Type: Timestamp  
Required: No

 ** Detail **   <a name="forecast-Type-PredictorEvent-Detail"></a>
The type of event. For example, `Retrain`. A retraining event denotes the timepoint when a predictor was retrained. Any monitor results from before the `Datetime` are from the previous predictor. Any new metrics are for the newly retrained predictor.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

## See Also
<a name="API_PredictorEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/PredictorEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/PredictorEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/PredictorEvent) 