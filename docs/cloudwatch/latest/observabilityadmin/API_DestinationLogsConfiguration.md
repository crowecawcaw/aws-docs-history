# DestinationLogsConfiguration

Configuration for centralization destination log groups, including encryption and backup
settings.

## Contents

**BackupConfiguration**

Configuration defining the backup region and an optional KMS key for the backup
destination.

Type: [LogsBackupConfiguration](API_LogsBackupConfiguration.md "API_LogsBackupConfiguration.md") object

Required: No

**LogGroupNameConfiguration**

Configuration that specifies a naming pattern for destination log groups created during centralization.
The pattern supports static text and dynamic variables that are replaced with source attributes
when log groups are created.

Type: [LogGroupNameConfiguration](API_LogGroupNameConfiguration.md "API_LogGroupNameConfiguration.md") object

Required: No

**LogsEncryptionConfiguration**

The encryption configuration for centralization destination log groups.

Type: [LogsEncryptionConfiguration](API_LogsEncryptionConfiguration.md "API_LogsEncryptionConfiguration.md") object

Required: No

**TagPropagationConfiguration**

Specifies the tag propagation configuration for this centralization rule. When present,
`LogGroupNameConfiguration` must use a `LogGroupNamePattern` that
contains `${source.logGroup}`, `${source.accountId}`, and
`${source.region}`.

Type: [TagPropagationConfiguration](API_TagPropagationConfiguration.md "API_TagPropagationConfiguration.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/DestinationLogsConfiguration.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/DestinationLogsConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/DestinationLogsConfiguration.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/DestinationLogsConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/DestinationLogsConfiguration.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/DestinationLogsConfiguration.md")
