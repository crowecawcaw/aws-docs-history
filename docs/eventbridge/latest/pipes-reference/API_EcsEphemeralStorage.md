# EcsEphemeralStorage

The amount of ephemeral storage to allocate for the task. This parameter is used to
expand the total amount of ephemeral storage available, beyond the default amount, for
tasks hosted on Fargate. For more information, see [Fargate task storage](../../../AmazonECS/latest/userguide/using_data_volumes.md "../../../AmazonECS/latest/userguide/using_data_volumes.md") in the _Amazon ECS User Guide
for Fargate_.

###### Note

This parameter is only supported for tasks hosted on Fargate using
Linux platform version `1.4.0` or later. This parameter is not supported for
Windows containers on Fargate.

## Contents

**sizeInGiB**

The total amount, in GiB, of ephemeral storage to set for the task. The minimum
supported value is `21` GiB and the maximum supported value is `200`
GiB.

Type: Integer

Valid Range: Minimum value of 21. Maximum value of 200.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/EcsEphemeralStorage.md "../../../goto/SdkForCpp/pipes-2015-10-07/EcsEphemeralStorage.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/EcsEphemeralStorage.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/EcsEphemeralStorage.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/EcsEphemeralStorage.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/EcsEphemeralStorage.md")
