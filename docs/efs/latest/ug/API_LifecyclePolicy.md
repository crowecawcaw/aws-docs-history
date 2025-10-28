# LifecyclePolicy

Describes a policy used by lifecycle management that specifies when to transition files
into and out of storage classes. For more information, see [Managing file system
storage](lifecycle-management-efs.md "lifecycle-management-efs.md").

###### Note

When using the `put-lifecycle-configuration` CLI command or the
`PutLifecycleConfiguration` API action, Amazon EFS requires that each
`LifecyclePolicy` object have only a single transition. This means that in a
request body, `LifecyclePolicies` must be structured as an array of
`LifecyclePolicy` objects, one object for each transition. For more
information, see the request examples in [PutLifecycleConfiguration](API_PutLifecycleConfiguration.md "API_PutLifecycleConfiguration.md").

## Contents

**TransitionToArchive**

The number of days after files were last accessed in primary storage (the
Standard storage class) at which to move them to Archive
storage. Metadata operations such as listing the contents of a directory don't count as
file access events.

Type: String

Valid Values: `AFTER_1_DAY | AFTER_7_DAYS | AFTER_14_DAYS | AFTER_30_DAYS | AFTER_60_DAYS | AFTER_90_DAYS | AFTER_180_DAYS | AFTER_270_DAYS | AFTER_365_DAYS`

Required: No

**TransitionToIA**

The number of days after files were last accessed in primary storage (the
Standard storage class) at which to move them to Infrequent Access
(IA) storage. Metadata operations such as listing the contents of a directory
don't count as file access events.

Type: String

Valid Values: `AFTER_7_DAYS | AFTER_14_DAYS | AFTER_30_DAYS | AFTER_60_DAYS | AFTER_90_DAYS | AFTER_1_DAY | AFTER_180_DAYS | AFTER_270_DAYS | AFTER_365_DAYS`

Required: No

**TransitionToPrimaryStorageClass**

Whether to move files back to primary (Standard) storage after they are
accessed in IA or Archive storage. Metadata operations such as
listing the contents of a directory don't count as file access events.

Type: String

Valid Values: `AFTER_1_ACCESS`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/LifecyclePolicy.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/LifecyclePolicy.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/LifecyclePolicy.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/LifecyclePolicy.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/LifecyclePolicy.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/LifecyclePolicy.md")
