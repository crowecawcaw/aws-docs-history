# Snapshot

Describes a directory snapshot.

## Contents

**DirectoryId**

The directory identifier.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**Name**

The descriptive name of the snapshot.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 128.

Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`

Required: No

**SnapshotId**

The snapshot identifier.

Type: String

Pattern: `^s-[0-9a-f]{10}$`

Required: No

**StartTime**

The date and time that the snapshot was taken.

Type: Timestamp

Required: No

**Status**

The snapshot status.

Type: String

Valid Values: `Creating | Completed | Failed`

Required: No

**Type**

The snapshot type.

Type: String

Valid Values: `Auto | Manual`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/Snapshot.md "../../../goto/SdkForCpp/ds-2015-04-16/Snapshot.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/Snapshot.md "../../../goto/SdkForJavaV2/ds-2015-04-16/Snapshot.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/Snapshot.md "../../../goto/SdkForRubyV3/ds-2015-04-16/Snapshot.md")
