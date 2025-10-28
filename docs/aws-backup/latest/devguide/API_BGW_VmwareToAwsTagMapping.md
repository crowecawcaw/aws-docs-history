# VmwareToAwsTagMapping

This displays the mapping of VMware tags to the
corresponding AWS tags.

## Contents

**AwsTagKey**

The key part of the AWS tag's key-value pair.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]+`

Required: Yes

**AwsTagValue**

The value part of the AWS tag's key-value pair.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 256.

Pattern: `[^\x00]*`

Required: Yes

**VmwareCategory**

The is the category of VMware.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 80.

Required: Yes

**VmwareTagName**

This is the user-defined name of a VMware tag.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 80.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-gateway-2021-01-01/VmwareToAwsTagMapping.md "../../../goto/SdkForCpp/backup-gateway-2021-01-01/VmwareToAwsTagMapping.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/VmwareToAwsTagMapping.md "../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/VmwareToAwsTagMapping.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/VmwareToAwsTagMapping.md "../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/VmwareToAwsTagMapping.md")
