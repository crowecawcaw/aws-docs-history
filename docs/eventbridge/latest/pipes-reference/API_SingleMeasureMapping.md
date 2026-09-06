

# SingleMeasureMapping
<a name="API_SingleMeasureMapping"></a>

Maps a single source data field to a single record in the specified Timestream for LiveAnalytics table.

For more information, see [Amazon Timestream for LiveAnalytics concepts](https://docs.aws.amazon.com/timestream/latest/developerguide/concepts.html) 

## Contents
<a name="API_SingleMeasureMapping_Contents"></a>

 ** MeasureName **   <a name="eventbridge-Type-SingleMeasureMapping-MeasureName"></a>
Target measure name for the measurement attribute in the Timestream table.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

 ** MeasureValue **   <a name="eventbridge-Type-SingleMeasureMapping-MeasureValue"></a>
Dynamic path of the source field to map to the measure in the record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

 ** MeasureValueType **   <a name="eventbridge-Type-SingleMeasureMapping-MeasureValueType"></a>
Data type of the source field.  
Type: String  
Valid Values: `DOUBLE | BIGINT | VARCHAR | BOOLEAN | TIMESTAMP`   
Required: Yes

## See Also
<a name="API_SingleMeasureMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/SingleMeasureMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/SingleMeasureMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/SingleMeasureMapping) 