

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# TimeSeriesCondition
<a name="API_TimeSeriesCondition"></a>

Creates a subset of items within an attribute that are modified. For example, you can use this operation to create a subset of items that cost $5 or less. To do this, you specify `"AttributeName": "price"`, `"AttributeValue": "5"`, and `"Condition": "LESS_THAN"`. Pair this operation with the [Action](API_Action.md) operation within the [CreateWhatIfForecast:TimeSeriesTransformations](API_CreateWhatIfForecast.md#forecast-CreateWhatIfForecast-request-TimeSeriesTransformations) operation to define how the attribute is modified.

## Contents
<a name="API_TimeSeriesCondition_Contents"></a>

 ** AttributeName **   <a name="forecast-Type-TimeSeriesCondition-AttributeName"></a>
The item\_id, dimension name, IM name, or timestamp that you are modifying.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`   
Required: Yes

 ** AttributeValue **   <a name="forecast-Type-TimeSeriesCondition-AttributeValue"></a>
The value that is applied for the chosen `Condition`.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `.+`   
Required: Yes

 ** Condition **   <a name="forecast-Type-TimeSeriesCondition-Condition"></a>
The condition to apply. Valid values are `EQUALS`, `NOT_EQUALS`, `LESS_THAN` and `GREATER_THAN`.  
Type: String  
Valid Values: `EQUALS | NOT_EQUALS | LESS_THAN | GREATER_THAN`   
Required: Yes

## See Also
<a name="API_TimeSeriesCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/TimeSeriesCondition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/TimeSeriesCondition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/TimeSeriesCondition) 