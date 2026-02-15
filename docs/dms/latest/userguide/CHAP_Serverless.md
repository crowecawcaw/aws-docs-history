# AWS DMS Serverless premigration.

AWS DMS Serverless includes pre-migration assessment capabilities that help identify
potential issues before starting your database migration. By running a pre-migration
assessment, you can detect and resolve configuration problems or compatibility issues
that might prevent successful serverless replication. For more information see [Individual assessments](CHAP_Tasks.AssessmentReport.md "CHAP_Tasks.AssessmentReport.md").

Unlike AWS DMS Standard, AWS DMS Serverless automatically stores pre-migration assessment
results in a system-managed Amazon S3 bucket, eliminating the need for you to specify a
custom bucket.

AWS DMS Serverless provides the following optional settings to support pre-migration
assessment:

- `**ResultLocationFolder**`: The folder
  within an Amazon S3 bucket where you want AWS DMS to store the results of this
  assessment run.
- `**ResultEncryptionMode**`: The
  supported values are `SSE_KMS` and `SSE_S3`. If these
  values are not provided, then the files are not encrypted at rest. For more
  information, see [Creating AWS KMS keys to encrypt Amazon S3 target
  objects](CHAP_Target.md#CHAP_Target.S3.KMSKeys "CHAP_Target.md#CHAP_Target.S3.KMSKeys").
- `**ResultKmsKeyArn**`: The ARN of a
  customer KMS encryption key that you specify when you set
  `ResultEncryptionMode` to `SSE_KMS`.
- `**IncludeOnly**`: A space-separated
  list of names for specific individual assessments that you want to include.
  These names come from the default list of individual assessments that AWS DMS
  supports for the associated migration.
- `**Exclude**`: A space-separated list
  of names for specific individual assessments that you want to exclude. These
  names come from the default list of individual assessments that AWS DMS supports
  for the associated migration.
- `**FailOnAssessmentFailure**`: A
  configurable setting you can set to `true` (the default setting) or
  `false`. Use this setting to to stop the replication from
  starting automatically if the assessment fails. This can help you evaluate the
  issue that is preventing the replication from running successfully.

## Using KMS key to encrypt files

To configure `SSE-KMS` for DMS Serverless premigration assessment with
a customer-managed key, add a policy statement that grants the DMS service-linked
role on your KMS key, enabling secure encryption and decryption of data during the
assessment process. You must configure the `kms:GenerateDataKey` and
`kms:Decrypt` permissions. See the example below:

```
{
      "Sid": "AccessForDMSServerlessPremigration",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<CustomerAccountId>:role/aws-service-role/dms.amazonaws.com/AWSServiceRoleForDMSServerless"
      },
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey*"
      ],
      "Resource": "*"
    }
```

## Limitations

Serverless premigrations has the following limitations:

- AWS DMS Serverless retains only the most recent pre-migration assessment
  results when you call the describe-replications API. While older assessment
  runs are removed from the immediate display, the corresponding result files
  remain accessible in the S3 results bucket.
- Custom S3 buckets cannot be chosen to store the assessment results.
- Transformations on remap schema, table, columns are not supported by
  preflight.
