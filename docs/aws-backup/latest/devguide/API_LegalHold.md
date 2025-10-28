# LegalHold

A legal hold is an administrative tool that helps prevent backups
from being deleted while under a hold. While the hold is in place,
backups under a hold cannot be deleted and lifecycle policies that
would alter the backup status (such as transition to cold storage) are
delayed until the legal hold is removed. A backup can have more than
one legal hold. Legal holds are applied to one or more backups
(also known as recovery points). These backups can be filtered by resource
types and by resource IDs.

## Contents

**CancellationDate**

The time when the legal hold was cancelled.

Type: Timestamp

Required: No

**CreationDate**

The time when the legal hold was created.

Type: Timestamp

Required: No

**Description**

The description of a legal hold.

Type: String

Required: No

**LegalHoldArn**

The Amazon Resource Name (ARN) of the legal hold; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Type: String

Required: No

**LegalHoldId**

The ID of the legal hold.

Type: String

Required: No

**Status**

The status of the legal hold.

Type: String

Valid Values: `CREATING | ACTIVE | CANCELING | CANCELED`

Required: No

**Title**

The title of a legal hold.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/LegalHold.md "../../../goto/SdkForCpp/backup-2018-11-15/LegalHold.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/LegalHold.md "../../../goto/SdkForJavaV2/backup-2018-11-15/LegalHold.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/LegalHold.md "../../../goto/SdkForRubyV3/backup-2018-11-15/LegalHold.md")
