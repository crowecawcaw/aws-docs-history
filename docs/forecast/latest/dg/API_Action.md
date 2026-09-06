

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# Action
<a name="API_Action"></a>

Defines the modifications that you are making to an attribute for a what-if forecast. For example, you can use this operation to create a what-if forecast that investigates a 10% off sale on all shoes. To do this, you specify `"AttributeName": "shoes"`, `"Operation": "MULTIPLY"`, and `"Value": "0.90"`. Pair this operation with the [TimeSeriesCondition](API_TimeSeriesCondition.md) operation within the [CreateWhatIfForecast:TimeSeriesTransformations](API_CreateWhatIfForecast.md#forecast-CreateWhatIfForecast-request-TimeSeriesTransformations) operation to define a subset of attribute items that are modified.

## Contents
<a name="API_Action_Contents"></a>

 ** AttributeName **   <a name="forecast-Type-Action-AttributeName"></a>
The related time series that you are modifying. This value is case insensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`   
Required: Yes

 ** Operation **   <a name="forecast-Type-Action-Operation"></a>
The operation that is applied to the provided attribute. Operations include:  
+  `ADD` - adds `Value` to all rows of `AttributeName`.
+  `SUBTRACT` - subtracts `Value` from all rows of `AttributeName`.
+  `MULTIPLY` - multiplies all rows of `AttributeName` by `Value`.
+  `DIVIDE` - divides all rows of `AttributeName` by `Value`.
Type: String  
Valid Values: `ADD | SUBTRACT | MULTIPLY | DIVIDE`   
Required: Yes

 ** Value **   <a name="forecast-Type-Action-Value"></a>
The value that is applied for the chosen `Operation`.  
Type: Double  
Required: Yes

## See Also
<a name="API_Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/Action) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/Action) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/Action) 