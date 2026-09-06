

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# SensorStatisticsSummary
<a name="API_SensorStatisticsSummary"></a>

 Summary of ingestion statistics like whether data exists, number of missing values, number of invalid values and so on related to the particular sensor. 

## Contents
<a name="API_SensorStatisticsSummary_Contents"></a>

 ** CategoricalValues **   <a name="LookoutForEquipment-Type-SensorStatisticsSummary-CategoricalValues"></a>
 Parameter that describes potential risk about whether data associated with the sensor is categorical.   
Type: [CategoricalValues](API_CategoricalValues.md) object  
Required: No

 ** ComponentName **   <a name="LookoutForEquipment-Type-SensorStatisticsSummary-ComponentName"></a>
 Name of the component to which the particular sensor belongs for which the statistics belong to.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._\-]{1,200}$`   
Required: No

 ** DataEndTime **   <a name="LookoutForEquipment-Type-SensorStatisticsSummary-DataEndTime"></a>
 Indicates the time reference to indicate the end of valid data associated with the sensor that the statistics belong to.   
Type: Timestamp  
Required: No

 ** DataExists **   <a name="LookoutForEquipment-Type-SensorStatisticsSummary-DataExists"></a>
 Parameter that indicates whether data exists for the sensor that the statistics belong to.   
Type: Boolean  
Required: No

 ** DataStartTime **   <a name="LookoutForEquipment-Type-SensorStatisticsSummary-DataStartTime"></a>
 Indicates the time reference to indicate the beginning of valid data associated with the sensor that the statistics belong to.   
Type: Timestamp  
Required: No

 ** DuplicateTimestamps **   <a name="LookoutForEquipment-Type-SensorStatisticsSummary-DuplicateTimestamps"></a>
 Parameter that describes the total number of duplicate timestamp records associated with the sensor that the statistics belong to.   
Type: [CountPercent](API_CountPercent.md) object  
Required: No

 ** InvalidDateEntries **   <a name="LookoutForEquipment-Type-SensorStatisticsSummary-InvalidDateEntries"></a>
 Parameter that describes the total number of invalid date entries associated with the sensor that the statistics belong to.   
Type: [CountPercent](API_CountPercent.md) object  
Required: No

 ** InvalidValues **   <a name="LookoutForEquipment-Type-SensorStatisticsSummary-InvalidValues"></a>
 Parameter that describes the total number of, and percentage of, values that are invalid for the sensor that the statistics belong to.   
Type: [CountPercent](API_CountPercent.md) object  
Required: No

 ** LargeTimestampGaps **   <a name="LookoutForEquipment-Type-SensorStatisticsSummary-LargeTimestampGaps"></a>
 Parameter that describes potential risk about whether data associated with the sensor contains one or more large gaps between consecutive timestamps.   
Type: [LargeTimestampGaps](API_LargeTimestampGaps.md) object  
Required: No

 ** MissingValues **   <a name="LookoutForEquipment-Type-SensorStatisticsSummary-MissingValues"></a>
 Parameter that describes the total number of, and percentage of, values that are missing for the sensor that the statistics belong to.   
Type: [CountPercent](API_CountPercent.md) object  
Required: No

 ** MonotonicValues **   <a name="LookoutForEquipment-Type-SensorStatisticsSummary-MonotonicValues"></a>
 Parameter that describes potential risk about whether data associated with the sensor is mostly monotonic.   
Type: [MonotonicValues](API_MonotonicValues.md) object  
Required: No

 ** MultipleOperatingModes **   <a name="LookoutForEquipment-Type-SensorStatisticsSummary-MultipleOperatingModes"></a>
 Parameter that describes potential risk about whether data associated with the sensor has more than one operating mode.   
Type: [MultipleOperatingModes](API_MultipleOperatingModes.md) object  
Required: No

 ** SensorName **   <a name="LookoutForEquipment-Type-SensorStatisticsSummary-SensorName"></a>
 Name of the sensor that the statistics belong to.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z:#$.\-_]{1,200}$`   
Required: No

## See Also
<a name="API_SensorStatisticsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/SensorStatisticsSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/SensorStatisticsSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/SensorStatisticsSummary) 