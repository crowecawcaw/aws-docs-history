

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# InferenceEventSummary
<a name="API_InferenceEventSummary"></a>

Contains information about the specific inference event, including start and end time, diagnostics information, event duration and so on.

## Contents
<a name="API_InferenceEventSummary_Contents"></a>

 ** Diagnostics **   <a name="LookoutForEquipment-Type-InferenceEventSummary-Diagnostics"></a>
 An array which specifies the names and values of all sensors contributing to an inference event.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50000.  
Required: No

 ** EventDurationInSeconds **   <a name="LookoutForEquipment-Type-InferenceEventSummary-EventDurationInSeconds"></a>
 Indicates the size of an inference event in seconds.   
Type: Long  
Valid Range: Minimum value of 0.  
Required: No

 ** EventEndTime **   <a name="LookoutForEquipment-Type-InferenceEventSummary-EventEndTime"></a>
Indicates the ending time of an inference event.   
Type: Timestamp  
Required: No

 ** EventStartTime **   <a name="LookoutForEquipment-Type-InferenceEventSummary-EventStartTime"></a>
Indicates the starting time of an inference event.   
Type: Timestamp  
Required: No

 ** InferenceSchedulerArn **   <a name="LookoutForEquipment-Type-InferenceEventSummary-InferenceSchedulerArn"></a>
 The Amazon Resource Name (ARN) of the inference scheduler being used for the inference event.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:inference-scheduler\/.+`   
Required: No

 ** InferenceSchedulerName **   <a name="LookoutForEquipment-Type-InferenceEventSummary-InferenceSchedulerName"></a>
The name of the inference scheduler being used for the inference events.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: No

## See Also
<a name="API_InferenceEventSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceEventSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceEventSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceEventSummary) 