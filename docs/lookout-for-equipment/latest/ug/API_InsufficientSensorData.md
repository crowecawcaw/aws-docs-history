

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# InsufficientSensorData
<a name="API_InsufficientSensorData"></a>

 Entity that comprises aggregated information on sensors having insufficient data. 

## Contents
<a name="API_InsufficientSensorData_Contents"></a>

 ** MissingCompleteSensorData **   <a name="LookoutForEquipment-Type-InsufficientSensorData-MissingCompleteSensorData"></a>
 Parameter that describes the total number of sensors that have data completely missing for it.   
Type: [MissingCompleteSensorData](API_MissingCompleteSensorData.md) object  
Required: Yes

 ** SensorsWithShortDateRange **   <a name="LookoutForEquipment-Type-InsufficientSensorData-SensorsWithShortDateRange"></a>
 Parameter that describes the total number of sensors that have a short date range of less than 14 days of data overall.   
Type: [SensorsWithShortDateRange](API_SensorsWithShortDateRange.md) object  
Required: Yes

## See Also
<a name="API_InsufficientSensorData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/InsufficientSensorData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/InsufficientSensorData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/InsufficientSensorData) 