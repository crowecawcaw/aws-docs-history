# IndexAction

This is an optional array within a BackupRule.

IndexAction consists of one ResourceTypes.

## Contents

**ResourceTypes**

0 or 1 index action will be accepted for each BackupRule.

Valid values:

- `EBS` for Amazon Elastic Block Store
- `S3` for Amazon Simple Storage Service (Amazon S3)

Type: Array of strings

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/IndexAction.md "../../../goto/SdkForCpp/backup-2018-11-15/IndexAction.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/IndexAction.md "../../../goto/SdkForJavaV2/backup-2018-11-15/IndexAction.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/IndexAction.md "../../../goto/SdkForRubyV3/backup-2018-11-15/IndexAction.md")
