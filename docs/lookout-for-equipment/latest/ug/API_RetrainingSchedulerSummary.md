

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# RetrainingSchedulerSummary
<a name="API_RetrainingSchedulerSummary"></a>

Provides information about the specified retraining scheduler, including model name, status, start date, frequency, and lookback window. 

## Contents
<a name="API_RetrainingSchedulerSummary_Contents"></a>

 ** LookbackWindow **   <a name="LookoutForEquipment-Type-RetrainingSchedulerSummary-LookbackWindow"></a>
The number of past days of data used for retraining.  
Type: String  
Pattern: `^P180D$|^P360D$|^P540D$|^P720D$`   
Required: No

 ** ModelArn **   <a name="LookoutForEquipment-Type-RetrainingSchedulerSummary-ModelArn"></a>
The ARN of the model that the retraining scheduler is attached to.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/.+`   
Required: No

 ** ModelName **   <a name="LookoutForEquipment-Type-RetrainingSchedulerSummary-ModelName"></a>
The name of the model that the retraining scheduler is attached to.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: No

 ** RetrainingFrequency **   <a name="LookoutForEquipment-Type-RetrainingSchedulerSummary-RetrainingFrequency"></a>
The frequency at which the model retraining is set. This follows the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Durations) guidelines.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 10.  
Pattern: `^P(\dY)?(\d{1,2}M)?(\d{1,3}D)?$`   
Required: No

 ** RetrainingStartDate **   <a name="LookoutForEquipment-Type-RetrainingSchedulerSummary-RetrainingStartDate"></a>
The start date for the retraining scheduler. Lookout for Equipment truncates the time you provide to the nearest UTC day.  
Type: Timestamp  
Required: No

 ** Status **   <a name="LookoutForEquipment-Type-RetrainingSchedulerSummary-Status"></a>
The status of the retraining scheduler.   
Type: String  
Valid Values: `PENDING | RUNNING | STOPPING | STOPPED`   
Required: No

## See Also
<a name="API_RetrainingSchedulerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/RetrainingSchedulerSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/RetrainingSchedulerSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/RetrainingSchedulerSummary) 