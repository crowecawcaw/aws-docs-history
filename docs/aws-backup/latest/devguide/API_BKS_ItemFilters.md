# ItemFilters

Item Filters represent all input item
properties specified when the search was
created.

Contains either EBSItemFilters or
S3ItemFilters

## Contents

**EBSItemFilters**

This array can contain CreationTimes,
FilePaths, LastModificationTimes, or Sizes objects.

Type: Array of [EBSItemFilter](API_BKS_EBSItemFilter.md "API_BKS_EBSItemFilter.md") objects

Array Members: Minimum number of 0 items. Maximum number of 10 items.

Required: No

**S3ItemFilters**

This array can contain CreationTimes, ETags,
ObjectKeys, Sizes, or VersionIds objects.

Type: Array of [S3ItemFilter](API_BKS_S3ItemFilter.md "API_BKS_S3ItemFilter.md") objects

Array Members: Minimum number of 0 items. Maximum number of 10 items.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backupsearch-2018-05-10/ItemFilters.md "../../../goto/SdkForCpp/backupsearch-2018-05-10/ItemFilters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backupsearch-2018-05-10/ItemFilters.md "../../../goto/SdkForJavaV2/backupsearch-2018-05-10/ItemFilters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backupsearch-2018-05-10/ItemFilters.md "../../../goto/SdkForRubyV3/backupsearch-2018-05-10/ItemFilters.md")
