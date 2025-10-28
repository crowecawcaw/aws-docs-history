# LogsBackupConfiguration

Configuration for backing up centralized log data to a secondary region.

## Contents

**Region**

Logs specific backup destination region within the primary destination account to which
log data should be centralized.

Type: String

Length Constraints: Minimum length of 1.

Required: Yes

**KmsKeyArn**

KMS Key ARN belonging to the primary destination account and backup region, to encrypt
newly created central log groups in the backup destination.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/LogsBackupConfiguration.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/LogsBackupConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/LogsBackupConfiguration.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/LogsBackupConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/LogsBackupConfiguration.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/LogsBackupConfiguration.md")
