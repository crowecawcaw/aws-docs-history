

# MultiMeasureMapping
<a name="API_MultiMeasureMapping"></a>

Maps multiple measures from the source event to the same Timestream for LiveAnalytics record.

For more information, see [Amazon Timestream for LiveAnalytics concepts](https://docs.aws.amazon.com/timestream/latest/developerguide/concepts.html) 

## Contents
<a name="API_MultiMeasureMapping_Contents"></a>

 ** MultiMeasureAttributeMappings **   <a name="eventbridge-Type-MultiMeasureMapping-MultiMeasureAttributeMappings"></a>
Mappings that represent multiple source event fields mapped to measures in the same Timestream for LiveAnalytics record.  
Type: Array of [MultiMeasureAttributeMapping](API_MultiMeasureAttributeMapping.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 256 items.  
Required: Yes

 ** MultiMeasureName **   <a name="eventbridge-Type-MultiMeasureMapping-MultiMeasureName"></a>
The name of the multiple measurements per record (multi-measure).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

## See Also
<a name="API_MultiMeasureMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/MultiMeasureMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/MultiMeasureMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/MultiMeasureMapping) 