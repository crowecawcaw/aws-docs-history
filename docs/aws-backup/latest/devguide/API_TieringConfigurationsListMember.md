# TieringConfigurationsListMember

This contains metadata about a tiering configuration returned in a list.

## Contents

**BackupVaultName**

The name of the backup vault where the tiering configuration applies.
Use `*` to apply to all backup vaults.

Type: String

Pattern: `^(\*|[a-zA-Z0-9\-\_]{2,50})$`

Required: No

**CreationTime**

The date and time a tiering configuration was created, in Unix format
and Coordinated Universal Time (UTC). The value of `CreationTime`
is accurate to milliseconds. For example, the value 1516925490.087 represents
Friday, January 26, 2018 12:11:30.087AM.

Type: Timestamp

Required: No

**LastUpdatedTime**

The date and time a tiering configuration was updated, in Unix format
and Coordinated Universal Time (UTC). The value of `LastUpdatedTime`
is accurate to milliseconds. For example, the value 1516925490.087 represents
Friday, January 26, 2018 12:11:30.087AM.

Type: Timestamp

Required: No

**TieringConfigurationArn**

An Amazon Resource Name (ARN) that uniquely identifies the
tiering configuration.

Type: String

Required: No

**TieringConfigurationName**

The unique name of the tiering configuration.

Type: String

Pattern: `^[a-zA-Z0-9_]{1,200}$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/TieringConfigurationsListMember.md "../../../goto/SdkForCpp/backup-2018-11-15/TieringConfigurationsListMember.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/TieringConfigurationsListMember.md "../../../goto/SdkForJavaV2/backup-2018-11-15/TieringConfigurationsListMember.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/TieringConfigurationsListMember.md "../../../goto/SdkForRubyV3/backup-2018-11-15/TieringConfigurationsListMember.md")
