# NetworkConfiguration

This structure specifies the network configuration for an Amazon ECS
task.

## Contents

**awsvpcConfiguration**

Use this structure to specify the VPC subnets and security groups for the task, and
whether a public IP address is to be used. This structure is relevant only for ECS tasks
that use the `awsvpc` network mode.

Type: [AwsVpcConfiguration](API_AwsVpcConfiguration.md "API_AwsVpcConfiguration.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/NetworkConfiguration.md "../../../goto/SdkForCpp/pipes-2015-10-07/NetworkConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/NetworkConfiguration.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/NetworkConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/NetworkConfiguration.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/NetworkConfiguration.md")
