# RulesetItem

Contains metadata about the ruleset.

## Contents

###### Note

In the following list, the required parameters are described first.

**Name**

The name of the ruleset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**TargetArn**

The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is
associated with.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: Yes

**AccountId**

The ID of the AWS account that owns the ruleset.

Type: String

Length Constraints: Maximum length of 255.

Required: No

**CreateDate**

The date and time that the ruleset was created.

Type: Timestamp

Required: No

**CreatedBy**

The Amazon Resource Name (ARN) of the user who created the ruleset.

Type: String

Required: No

**Description**

The description of the ruleset.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

**LastModifiedBy**

The Amazon Resource Name (ARN) of the user who last modified the ruleset.

Type: String

Required: No

**LastModifiedDate**

The modification date and time of the ruleset.

Type: Timestamp

Required: No

**ResourceArn**

The Amazon Resource Name (ARN) for the ruleset.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: No

**RuleCount**

The number of rules that are defined in the ruleset.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**Tags**

Metadata tags that have been applied to the ruleset.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/RulesetItem.md "../../../goto/SdkForCpp/databrew-2017-07-25/RulesetItem.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/RulesetItem.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/RulesetItem.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/RulesetItem.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/RulesetItem.md")
