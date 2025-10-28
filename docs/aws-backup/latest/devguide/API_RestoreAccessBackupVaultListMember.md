# RestoreAccessBackupVaultListMember

Contains information about a restore access backup vault.

## Contents

**ApprovalDate**

The date and time when the restore access backup vault was approved.

Type: Timestamp

Required: No

**CreationDate**

The date and time when the restore access backup vault was created.

Type: Timestamp

Required: No

**LatestRevokeRequest**

Information about the latest request to revoke access to this backup vault.

Type: [LatestRevokeRequest](API_LatestRevokeRequest.md "API_LatestRevokeRequest.md") object

Required: No

**RestoreAccessBackupVaultArn**

The ARN of the restore access backup vault.

Type: String

Required: No

**VaultState**

The current state of the restore access backup vault.

Type: String

Valid Values: `CREATING | AVAILABLE | FAILED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/RestoreAccessBackupVaultListMember.md "../../../goto/SdkForCpp/backup-2018-11-15/RestoreAccessBackupVaultListMember.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreAccessBackupVaultListMember.md "../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreAccessBackupVaultListMember.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreAccessBackupVaultListMember.md "../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreAccessBackupVaultListMember.md")
