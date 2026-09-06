

# AutoScalingDescription
<a name="API_AutoScalingDescription"></a>

Information about the auto scaling parameters for the connector.

## Contents
<a name="API_AutoScalingDescription_Contents"></a>

 ** maxAutoscalingTaskCount **   <a name="MSKC-Type-AutoScalingDescription-maxAutoscalingTaskCount"></a>
The maximum number of tasks allocated to the connector during autoscaling operations. Must be at least equal to maxWorkerCount.  
Type: Integer  
Required: No

 ** maxWorkerCount **   <a name="MSKC-Type-AutoScalingDescription-maxWorkerCount"></a>
The maximum number of workers allocated to the connector.  
Type: Integer  
Required: No

 ** mcuCount **   <a name="MSKC-Type-AutoScalingDescription-mcuCount"></a>
The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.  
Type: Integer  
Required: No

 ** minWorkerCount **   <a name="MSKC-Type-AutoScalingDescription-minWorkerCount"></a>
The minimum number of workers allocated to the connector.  
Type: Integer  
Required: No

 ** scaleInPolicy **   <a name="MSKC-Type-AutoScalingDescription-scaleInPolicy"></a>
The scale-in policy for the connector.  
Type: [ScaleInPolicyDescription](API_ScaleInPolicyDescription.md) object  
Required: No

 ** scaleOutPolicy **   <a name="MSKC-Type-AutoScalingDescription-scaleOutPolicy"></a>
The scale-out policy for the connector.  
Type: [ScaleOutPolicyDescription](API_ScaleOutPolicyDescription.md) object  
Required: No

## See Also
<a name="API_AutoScalingDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/AutoScalingDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/AutoScalingDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/AutoScalingDescription) 