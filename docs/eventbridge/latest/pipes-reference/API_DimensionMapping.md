

# DimensionMapping
<a name="API_DimensionMapping"></a>

Maps source data to a dimension in the target Timestream for LiveAnalytics table.

For more information, see [Amazon Timestream for LiveAnalytics concepts](https://docs.aws.amazon.com/timestream/latest/developerguide/concepts.html) 

## Contents
<a name="API_DimensionMapping_Contents"></a>

 ** DimensionName **   <a name="eventbridge-Type-DimensionMapping-DimensionName"></a>
The metadata attributes of the time series. For example, the name and Availability Zone of an Amazon EC2 instance or the name of the manufacturer of a wind turbine are dimensions.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** DimensionValue **   <a name="eventbridge-Type-DimensionMapping-DimensionValue"></a>
Dynamic path to the dimension value in the source event.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

 ** DimensionValueType **   <a name="eventbridge-Type-DimensionMapping-DimensionValueType"></a>
The data type of the dimension for the time-series data.  
Type: String  
Valid Values: `VARCHAR`   
Required: Yes

## See Also
<a name="API_DimensionMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/DimensionMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/DimensionMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/DimensionMapping) 