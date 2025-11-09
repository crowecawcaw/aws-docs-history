# RestoreTestingSelectionForList

This contains metadata about a restore testing selection.

## Contents

**CreationTime**

The date and time that a restore testing selection
was created, in Unix format and Coordinated Universal Time (UTC).
The value of `CreationTime` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday,
January 26,2018 12:11:30.087 AM.

Type: Timestamp

Required: Yes

**IamRoleArn**

The Amazon Resource Name (ARN) of the IAM role that
AWS Backup uses to create the target resource; for example:
`arn:aws:iam::123456789012:role/S3Access`.

Type: String

Required: Yes

**ProtectedResourceType**

The type of AWS resource included in a restore
testing selection; for example, an
Amazon EBS volume or an
Amazon RDS database.

Type: String

Required: Yes

**RestoreTestingPlanName**

Unique string that is the name of the restore testing plan.

The name cannot be changed after creation. The name must
consist of only alphanumeric characters and underscores.
Maximum length is 50.

Type: String

Required: Yes

**RestoreTestingSelectionName**

Unique name of a restore testing selection.

The name consists of only alphanumeric characters and underscores.
Maximum length is 50.

Type: String

Required: Yes

**ValidationWindowHours**

This value represents the time, in hours, data is retained after
a restore test so that optional validation can be completed.

Accepted value is an integer between
0 and 168 (the hourly equivalent of seven days).

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/RestoreTestingSelectionForList.md "../../../goto/SdkForCpp/backup-2018-11-15/RestoreTestingSelectionForList.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingSelectionForList.md "../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingSelectionForList.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingSelectionForList.md "../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingSelectionForList.md")
