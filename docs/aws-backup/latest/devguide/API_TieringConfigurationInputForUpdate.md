# TieringConfigurationInputForUpdate

This contains metadata about a tiering configuration for update operations.

## Contents

**BackupVaultName**

The name of the backup vault where the tiering configuration applies.
Use `*` to apply to all backup vaults.

Type: String

Pattern: `^(\*|[a-zA-Z0-9\-\_]{2,50})$`

Required: Yes

**ResourceSelection**

An array of resource selection objects that specify which resources
are included in the tiering configuration and their tiering settings.

Type: Array of [ResourceSelection](API_ResourceSelection.md "API_ResourceSelection.md") objects

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/TieringConfigurationInputForUpdate.md "../../../goto/SdkForCpp/backup-2018-11-15/TieringConfigurationInputForUpdate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/TieringConfigurationInputForUpdate.md "../../../goto/SdkForJavaV2/backup-2018-11-15/TieringConfigurationInputForUpdate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/TieringConfigurationInputForUpdate.md "../../../goto/SdkForRubyV3/backup-2018-11-15/TieringConfigurationInputForUpdate.md")
