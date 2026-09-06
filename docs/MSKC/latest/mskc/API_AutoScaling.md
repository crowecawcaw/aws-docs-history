

# AutoScaling
<a name="API_AutoScaling"></a>

Specifies how the connector scales.

## Contents
<a name="API_AutoScaling_Contents"></a>

 ** maxWorkerCount **   <a name="MSKC-Type-AutoScaling-maxWorkerCount"></a>
The maximum number of workers allocated to the connector.  
Type: Integer  
Required: Yes

 ** mcuCount **   <a name="MSKC-Type-AutoScaling-mcuCount"></a>
The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 8.  
Required: Yes

 ** minWorkerCount **   <a name="MSKC-Type-AutoScaling-minWorkerCount"></a>
The minimum number of workers allocated to the connector.  
Type: Integer  
Required: Yes

 ** maxAutoscalingTaskCount **   <a name="MSKC-Type-AutoScaling-maxAutoscalingTaskCount"></a>
The maximum number of tasks allocated to the connector during autoscaling operations. Must be at least equal to maxWorkerCount.  
Type: Integer  
Required: No

 ** scaleInPolicy **   <a name="MSKC-Type-AutoScaling-scaleInPolicy"></a>
The scale-in policy for the connector.  
Type: [ScaleInPolicy](API_ScaleInPolicy.md) object  
Required: No

 ** scaleOutPolicy **   <a name="MSKC-Type-AutoScaling-scaleOutPolicy"></a>
The scale-out policy for the connector.  
Type: [ScaleOutPolicy](API_ScaleOutPolicy.md) object  
Required: No

## See Also
<a name="API_AutoScaling_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/AutoScaling) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/AutoScaling) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/AutoScaling) 