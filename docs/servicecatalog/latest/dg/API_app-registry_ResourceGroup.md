# ResourceGroup

The information about the resource group integration.

## Contents

**arn**

The Amazon resource name (ARN) of the resource group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

Required: No

**errorMessage**

The error message that generates when the propagation process for the resource group fails.

Type: String

Required: No

**state**

The state of the propagation process for the resource group. The states includes:

`CREATING` if the resource group is in the process of being created.

`CREATE_COMPLETE` if the resource group was created successfully.

`CREATE_FAILED` if the resource group failed to be created.

`UPDATING` if the resource group is in the process of being updated.

`UPDATE_COMPLETE` if the resource group updated successfully.

`UPDATE_FAILED` if the resource group could not update successfully.

Type: String

Valid Values: `CREATING | CREATE_COMPLETE | CREATE_FAILED | UPDATING | UPDATE_COMPLETE | UPDATE_FAILED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ResourceGroup.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ResourceGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ResourceGroup.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ResourceGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ResourceGroup.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ResourceGroup.md")
