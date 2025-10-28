# CalculatedLifecycle

Contains `DeleteAt` and `MoveToColdStorageAt` timestamps, which
are used to specify a lifecycle for a recovery point.

The lifecycle defines when a protected resource is transitioned to cold storage and when
it expires. AWS Backup transitions and expires backups automatically according to
the lifecycle that you define.

Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
days. Therefore, the “retention” setting must be 90 days greater than the “transition to
cold after days” setting. The “transition to cold after days” setting cannot be changed
after a backup has been transitioned to cold.

Resource types that can transition to cold storage are listed in the [Feature availability
by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table. AWS Backup ignores this expression for other resource types.

## Contents

**DeleteAt**

A timestamp that specifies when to delete a recovery point.

Type: Timestamp

Required: No

**MoveToColdStorageAt**

A timestamp that specifies when to transition a recovery point to cold storage.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/CalculatedLifecycle.md "../../../goto/SdkForCpp/backup-2018-11-15/CalculatedLifecycle.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/CalculatedLifecycle.md "../../../goto/SdkForJavaV2/backup-2018-11-15/CalculatedLifecycle.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/CalculatedLifecycle.md "../../../goto/SdkForRubyV3/backup-2018-11-15/CalculatedLifecycle.md")
