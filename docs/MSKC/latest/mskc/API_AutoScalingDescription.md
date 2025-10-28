# AutoScalingDescription

Information about the auto scaling parameters for the connector.

## Contents

**maxWorkerCount**

The maximum number of workers allocated to the connector.

Type: Integer

Required: No

**mcuCount**

The number of microcontroller units (MCUs) allocated to each connector worker. The valid
values are 1,2,4,8.

Type: Integer

Required: No

**minWorkerCount**

The minimum number of workers allocated to the connector.

Type: Integer

Required: No

**scaleInPolicy**

The sacle-in policy for the connector.

Type: [ScaleInPolicyDescription](API_ScaleInPolicyDescription.md "API_ScaleInPolicyDescription.md") object

Required: No

**scaleOutPolicy**

The sacle-out policy for the connector.>

Type: [ScaleOutPolicyDescription](API_ScaleOutPolicyDescription.md "API_ScaleOutPolicyDescription.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kafkaconnect-2021-09-14/AutoScalingDescription.md "../../../goto/SdkForCpp/kafkaconnect-2021-09-14/AutoScalingDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/AutoScalingDescription.md "../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/AutoScalingDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/AutoScalingDescription.md "../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/AutoScalingDescription.md")
