# AutoScalingUpdate

The updates to the auto scaling parameters for the connector.

## Contents

**maxWorkerCount**

The target maximum number of workers allocated to the connector.

Type: Integer

Required: Yes

**mcuCount**

The target number of microcontroller units (MCUs) allocated to each connector worker.
The valid values are 1,2,4,8.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 8.

Required: Yes

**minWorkerCount**

The target minimum number of workers allocated to the connector.

Type: Integer

Required: Yes

**scaleInPolicy**

The target scale-in policy for the connector.

Type: [ScaleInPolicyUpdate](API_ScaleInPolicyUpdate.md "API_ScaleInPolicyUpdate.md") object

Required: Yes

**scaleOutPolicy**

The target scale-out policy for the connector.

Type: [ScaleOutPolicyUpdate](API_ScaleOutPolicyUpdate.md "API_ScaleOutPolicyUpdate.md") object

Required: Yes

**maxAutoscalingTaskCount**

The maximum number of tasks allocated to the connector during autoscaling operations.
Must be at least equal to maxWorkerCount.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kafkaconnect-2021-09-14/AutoScalingUpdate.md "../../../goto/SdkForCpp/kafkaconnect-2021-09-14/AutoScalingUpdate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/AutoScalingUpdate.md "../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/AutoScalingUpdate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/AutoScalingUpdate.md "../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/AutoScalingUpdate.md")
