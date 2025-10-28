# SchemaExtensionInfo

Information about a schema extension.

## Contents

**Description**

A description of the schema extension.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 128.

Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`

Required: No

**DirectoryId**

The identifier of the directory to which the schema extension is applied.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**EndDateTime**

The date and time that the schema extension was completed.

Type: Timestamp

Required: No

**SchemaExtensionId**

The identifier of the schema extension.

Type: String

Pattern: `^e-[0-9a-f]{10}$`

Required: No

**SchemaExtensionStatus**

The current status of the schema extension.

Type: String

Valid Values: `Initializing | CreatingSnapshot | UpdatingSchema | Replicating | CancelInProgress | RollbackInProgress | Cancelled | Failed | Completed`

Required: No

**SchemaExtensionStatusReason**

The reason for the `SchemaExtensionStatus`.

Type: String

Required: No

**StartDateTime**

The date and time that the schema extension started being applied to the
directory.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/SchemaExtensionInfo.md "../../../goto/SdkForCpp/ds-2015-04-16/SchemaExtensionInfo.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/SchemaExtensionInfo.md "../../../goto/SdkForJavaV2/ds-2015-04-16/SchemaExtensionInfo.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/SchemaExtensionInfo.md "../../../goto/SdkForRubyV3/ds-2015-04-16/SchemaExtensionInfo.md")
