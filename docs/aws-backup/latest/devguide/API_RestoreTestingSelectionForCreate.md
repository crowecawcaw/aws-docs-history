# RestoreTestingSelectionForCreate

This contains metadata about a specific restore testing selection.

ProtectedResourceType is required, such as Amazon EBS or
Amazon EC2.

This consists of `RestoreTestingSelectionName`,
`ProtectedResourceType`, and one of the following:

- `ProtectedResourceArns`
- `ProtectedResourceConditions`
  Each protected resource type can have one single value.

A restore testing selection can include a wildcard value ("\*") for
`ProtectedResourceArns` along with `ProtectedResourceConditions`.
Alternatively, you can include up to 30 specific protected resource ARNs in
`ProtectedResourceArns`.

`ProtectedResourceConditions` examples include as `StringEquals`
and `StringNotEquals`.

## Contents

**IamRoleArn**

The Amazon Resource Name (ARN) of the IAM role that
AWS Backup uses to create the target resource;
for example: `arn:aws:iam::123456789012:role/S3Access`.

Type: String

Required: Yes

**ProtectedResourceType**

The type of AWS resource included in a restore
testing selection; for example, an Amazon EBS volume or
an Amazon RDS database.

Supported resource types accepted include:

- `Aurora` for Amazon Aurora
- `DocumentDB` for Amazon DocumentDB (with MongoDB compatibility)
- `DynamoDB` for Amazon DynamoDB
- `EBS` for Amazon Elastic Block Store
- `EC2` for Amazon Elastic Compute Cloud
- `EFS` for Amazon Elastic File System
- `FSx` for Amazon FSx
- `Neptune` for Amazon Neptune
- `RDS` for Amazon Relational Database Service
- `S3` for Amazon S3

Type: String

Required: Yes

**RestoreTestingSelectionName**

The unique name of the restore testing selection
that belongs to the related restore testing plan.

Type: String

Required: Yes

**ProtectedResourceArns**

Each protected resource can be filtered by its specific ARNs, such as
`ProtectedResourceArns: ["arn:aws:...", "arn:aws:..."]`
or by a wildcard: `ProtectedResourceArns: ["*"]`,
but not both.

Type: Array of strings

Required: No

**ProtectedResourceConditions**

If you have included the wildcard in ProtectedResourceArns,
you can include resource conditions, such as
`ProtectedResourceConditions: { StringEquals: [{ key: "XXXX", 
 value: "YYYY" }]`.

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

This is amount of hours (0 to 168) available to run a validation script on the data. The
data will be deleted upon the completion of the validation script or the end of the
specified retention period, whichever comes first.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/RestoreTestingSelectionForCreate.md "../../../goto/SdkForCpp/backup-2018-11-15/RestoreTestingSelectionForCreate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingSelectionForCreate.md "../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingSelectionForCreate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingSelectionForCreate.md "../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingSelectionForCreate.md")
