# AutoScaling

Specifies how the connector scales.

## Contents

**maxWorkerCount**

The maximum number of workers allocated to the connector.

Type: Integer

Required: Yes

**mcuCount**

The number of microcontroller units (MCUs) allocated to each connector worker. The valid
values are 1,2,4,8.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 8.

Required: Yes

**minWorkerCount**

The minimum number of workers allocated to the connector.

Type: Integer

Required: Yes

**scaleInPolicy**

The sacle-in policy for the connector.

Type: [ScaleInPolicy](API_ScaleInPolicy.md "API_ScaleInPolicy.md") object

Required: No

**scaleOutPolicy**

The sacle-out policy for the connector.

Type: [ScaleOutPolicy](API_ScaleOutPolicy.md "API_ScaleOutPolicy.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kafkaconnect-2021-09-14/AutoScaling.md "../../../goto/SdkForCpp/kafkaconnect-2021-09-14/AutoScaling.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/AutoScaling.md "../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/AutoScaling.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/AutoScaling.md "../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/AutoScaling.md")
