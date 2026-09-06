

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# LargeTimestampGaps
<a name="API_LargeTimestampGaps"></a>

 Entity that comprises information on large gaps between consecutive timestamps in data. 

## Contents
<a name="API_LargeTimestampGaps_Contents"></a>

 ** Status **   <a name="LookoutForEquipment-Type-LargeTimestampGaps-Status"></a>
 Indicates whether there is a potential data issue related to large gaps in timestamps.   
Type: String  
Valid Values: `POTENTIAL_ISSUE_DETECTED | NO_ISSUE_DETECTED`   
Required: Yes

 ** MaxTimestampGapInDays **   <a name="LookoutForEquipment-Type-LargeTimestampGaps-MaxTimestampGapInDays"></a>
 Indicates the size of the largest timestamp gap, in days.   
Type: Integer  
Required: No

 ** NumberOfLargeTimestampGaps **   <a name="LookoutForEquipment-Type-LargeTimestampGaps-NumberOfLargeTimestampGaps"></a>
 Indicates the number of large timestamp gaps, if there are any.   
Type: Integer  
Required: No

## See Also
<a name="API_LargeTimestampGaps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/LargeTimestampGaps) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/LargeTimestampGaps) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/LargeTimestampGaps) 