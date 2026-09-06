

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# InferenceSchedulerSummary
<a name="API_InferenceSchedulerSummary"></a>

Contains information about the specific inference scheduler, including data delay offset, model name and ARN, status, and so on. 

## Contents
<a name="API_InferenceSchedulerSummary_Contents"></a>

 ** DataDelayOffsetInMinutes **   <a name="LookoutForEquipment-Type-InferenceSchedulerSummary-DataDelayOffsetInMinutes"></a>
A period of time (in minutes) by which inference on the data is delayed after the data starts. For instance, if an offset delay time of five minutes was selected, inference will not begin on the data until the first data measurement after the five minute mark. For example, if five minutes is selected, the inference scheduler will wake up at the configured frequency with the additional five minute delay time to check the customer S3 bucket. The customer can upload data at the same frequency and they don't need to stop and restart the scheduler when uploading new data.   
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 60.  
Required: No

 ** DataUploadFrequency **   <a name="LookoutForEquipment-Type-InferenceSchedulerSummary-DataUploadFrequency"></a>
How often data is uploaded to the source S3 bucket for the input data. This value is the length of time between data uploads. For instance, if you select 5 minutes, Amazon Lookout for Equipment will upload the real-time data to the source bucket once every 5 minutes. This frequency also determines how often Amazon Lookout for Equipment starts a scheduled inference on your data. In this example, it starts once every 5 minutes.   
Type: String  
Valid Values: `PT5M | PT10M | PT15M | PT30M | PT1H`   
Required: No

 ** InferenceSchedulerArn **   <a name="LookoutForEquipment-Type-InferenceSchedulerSummary-InferenceSchedulerArn"></a>
 The Amazon Resource Name (ARN) of the inference scheduler.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:inference-scheduler\/.+`   
Required: No

 ** InferenceSchedulerName **   <a name="LookoutForEquipment-Type-InferenceSchedulerSummary-InferenceSchedulerName"></a>
The name of the inference scheduler.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: No

 ** LatestInferenceResult **   <a name="LookoutForEquipment-Type-InferenceSchedulerSummary-LatestInferenceResult"></a>
Indicates whether the latest execution for the inference scheduler was Anomalous (anomalous events found) or Normal (no anomalous events found).  
Type: String  
Valid Values: `ANOMALOUS | NORMAL`   
Required: No

 ** ModelArn **   <a name="LookoutForEquipment-Type-InferenceSchedulerSummary-ModelArn"></a>
 The Amazon Resource Name (ARN) of the machine learning model used by the inference scheduler.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/.+`   
Required: No

 ** ModelName **   <a name="LookoutForEquipment-Type-InferenceSchedulerSummary-ModelName"></a>
The name of the machine learning model used for the inference scheduler.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: No

 ** Status **   <a name="LookoutForEquipment-Type-InferenceSchedulerSummary-Status"></a>
Indicates the status of the inference scheduler.   
Type: String  
Valid Values: `PENDING | RUNNING | STOPPING | STOPPED`   
Required: No

## See Also
<a name="API_InferenceSchedulerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceSchedulerSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceSchedulerSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceSchedulerSummary) 