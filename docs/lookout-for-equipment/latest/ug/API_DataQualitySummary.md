

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# DataQualitySummary
<a name="API_DataQualitySummary"></a>

 DataQualitySummary gives aggregated statistics over all the sensors about a completed ingestion job. It primarily gives more information about statistics over different incorrect data like MissingCompleteSensorData, MissingSensorData, UnsupportedDateFormats, InsufficientSensorData, DuplicateTimeStamps. 

## Contents
<a name="API_DataQualitySummary_Contents"></a>

 ** DuplicateTimestamps **   <a name="LookoutForEquipment-Type-DataQualitySummary-DuplicateTimestamps"></a>
 Parameter that gives information about duplicate timestamps in the input data.   
Type: [DuplicateTimestamps](API_DuplicateTimestamps.md) object  
Required: Yes

 ** InsufficientSensorData **   <a name="LookoutForEquipment-Type-DataQualitySummary-InsufficientSensorData"></a>
 Parameter that gives information about insufficient data for sensors in the dataset. This includes information about those sensors that have complete data missing and those with a short date range.   
Type: [InsufficientSensorData](API_InsufficientSensorData.md) object  
Required: Yes

 ** InvalidSensorData **   <a name="LookoutForEquipment-Type-DataQualitySummary-InvalidSensorData"></a>
 Parameter that gives information about data that is invalid over all the sensors in the input data.   
Type: [InvalidSensorData](API_InvalidSensorData.md) object  
Required: Yes

 ** MissingSensorData **   <a name="LookoutForEquipment-Type-DataQualitySummary-MissingSensorData"></a>
 Parameter that gives information about data that is missing over all the sensors in the input data.   
Type: [MissingSensorData](API_MissingSensorData.md) object  
Required: Yes

 ** UnsupportedTimestamps **   <a name="LookoutForEquipment-Type-DataQualitySummary-UnsupportedTimestamps"></a>
 Parameter that gives information about unsupported timestamps in the input data.   
Type: [UnsupportedTimestamps](API_UnsupportedTimestamps.md) object  
Required: Yes

## See Also
<a name="API_DataQualitySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/DataQualitySummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/DataQualitySummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/DataQualitySummary) 