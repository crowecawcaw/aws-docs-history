# S3ItemFilter

This contains arrays of objects, which may include
ObjectKeys, Sizes, CreationTimes, VersionIds, and/or
Etags.

## Contents

**CreationTimes**

You can include 1 to 10 values.

If one value is included, the results will
return only items that match the value.

If more than one value is included, the
results will return all items that match any of the
values.

Type: Array of [TimeCondition](API_BKS_TimeCondition.md "API_BKS_TimeCondition.md") objects

Array Members: Minimum number of 1 item. Maximum number of 10 items.

Required: No

**ETags**

You can include 1 to 10 values.

If one value is included, the results will
return only items that match the value.

If more than one value is included, the
results will return all items that match any of the
values.

Type: Array of [StringCondition](API_BKS_StringCondition.md "API_BKS_StringCondition.md") objects

Array Members: Minimum number of 1 item. Maximum number of 10 items.

Required: No

**ObjectKeys**

You can include 1 to 10 values.

If one value is included, the results will
return only items that match the value.

If more than one value is included, the
results will return all items that match any of the
values.

Type: Array of [StringCondition](API_BKS_StringCondition.md "API_BKS_StringCondition.md") objects

Array Members: Minimum number of 1 item. Maximum number of 10 items.

Required: No

**Sizes**

You can include 1 to 10 values.

If one value is included, the results will
return only items that match the value.

If more than one value is included, the
results will return all items that match any of the
values.

Type: Array of [LongCondition](API_BKS_LongCondition.md "API_BKS_LongCondition.md") objects

Array Members: Minimum number of 1 item. Maximum number of 10 items.

Required: No

**VersionIds**

You can include 1 to 10 values.

If one value is included, the results will
return only items that match the value.

If more than one value is included, the
results will return all items that match any of the
values.

Type: Array of [StringCondition](API_BKS_StringCondition.md "API_BKS_StringCondition.md") objects

Array Members: Minimum number of 1 item. Maximum number of 10 items.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backupsearch-2018-05-10/S3ItemFilter.md "../../../goto/SdkForCpp/backupsearch-2018-05-10/S3ItemFilter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backupsearch-2018-05-10/S3ItemFilter.md "../../../goto/SdkForJavaV2/backupsearch-2018-05-10/S3ItemFilter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backupsearch-2018-05-10/S3ItemFilter.md "../../../goto/SdkForRubyV3/backupsearch-2018-05-10/S3ItemFilter.md")
