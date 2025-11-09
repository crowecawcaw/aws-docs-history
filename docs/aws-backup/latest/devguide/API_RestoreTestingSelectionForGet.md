# RestoreTestingSelectionForGet

This contains metadata about a restore testing selection.

## Contents

**CreationTime**

The date and time that a restore testing selection was created,
in Unix format and Coordinated Universal Time (UTC). The value of
`CreationTime` is accurate to milliseconds. For example,
the value 1516925490.087 represents Friday, January 26,
201812:11:30.087 AM.

Type: Timestamp

Required: Yes

**IamRoleArn**

The Amazon Resource Name (ARN) of the IAM role that
AWS Backup uses to create the target resource; for
example:`arn:aws:iam::123456789012:role/S3Access`.

Type: String

Required: Yes

**ProtectedResourceType**

The type of AWS resource included in a resource
testing selection;
for example, an Amazon EBS volume
or an Amazon RDS database.

Type: String

Required: Yes

**RestoreTestingPlanName**

The RestoreTestingPlanName is a unique string that is the name
of the restore testing plan.

Type: String

Required: Yes

**RestoreTestingSelectionName**

The unique name of the restore testing selection that
belongs to the related restore testing plan.

The name consists of only alphanumeric characters and underscores.
Maximum length is 50.

Type: String

Required: Yes

**CreatorRequestId**

This identifies the request and allows failed requests to
be retried without the risk of running the operation twice.
If the request includes a `CreatorRequestId` that
matches an existing backup plan, that plan is returned. This
parameter is optional.

If used, this parameter must contain 1 to 50 alphanumeric
or '-\_.' characters.

Type: String

Required: No

**ProtectedResourceArns**

You can include specific ARNs, such as
`ProtectedResourceArns: ["arn:aws:...", "arn:aws:..."]`
or you can include a wildcard: `ProtectedResourceArns: ["*"]`,
but not both.

Type: Array of strings

Required: No

**ProtectedResourceConditions**

In a resource testing selection, this parameter filters by
specific conditions such as `StringEquals` or
`StringNotEquals`.

Type: [ProtectedResourceConditions](API_ProtectedResourceConditions.md "API_ProtectedResourceConditions.md") object

Required: No

**RestoreMetadataOverrides**

You can override certain restore metadata keys by including the parameter
`RestoreMetadataOverrides` in the body of
`RestoreTestingSelection`. Key values are not case sensitive.

See the complete list of [restore testing
inferred metadata](restore-testing-inferred-metadata.md "restore-testing-inferred-metadata.md").

Type: String to string map

Required: No

**ValidationWindowHours**

This is amount of hours (1 to 168) available to run a validation script on the data. The
data will be deleted upon the completion of the validation script or the end of the
specified retention period, whichever comes first.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/RestoreTestingSelectionForGet.md "../../../goto/SdkForCpp/backup-2018-11-15/RestoreTestingSelectionForGet.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingSelectionForGet.md "../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingSelectionForGet.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingSelectionForGet.md "../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingSelectionForGet.md")
