# AwsVpcConfiguration

This structure specifies the VPC subnets and security groups for the task, and whether a
public IP address is to be used. This structure is relevant only for ECS tasks that use the
`awsvpc` network mode.

## Contents

**Subnets**

Specifies the subnets associated with the task. These subnets must all be in the same
VPC. You can specify as many as 16 subnets.

Type: Array of strings

Array Members: Minimum number of 0 items. Maximum number of 16 items.

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `subnet-[0-9a-z]*|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`

Required: Yes

**AssignPublicIp**

Specifies whether the task's elastic network interface receives a public IP address. You
can specify `ENABLED` only when `LaunchType` in
`EcsParameters` is set to `FARGATE`.

Type: String

Valid Values: `ENABLED | DISABLED`

Required: No

**SecurityGroups**

Specifies the security groups associated with the task. These security groups must all
be in the same VPC. You can specify as many as five security groups. If you do not specify
a security group, the default security group for the VPC is used.

Type: Array of strings

Array Members: Minimum number of 0 items. Maximum number of 5 items.

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `sg-[0-9a-zA-Z]*|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/AwsVpcConfiguration.md "../../../goto/SdkForCpp/pipes-2015-10-07/AwsVpcConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/AwsVpcConfiguration.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/AwsVpcConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/AwsVpcConfiguration.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/AwsVpcConfiguration.md")
