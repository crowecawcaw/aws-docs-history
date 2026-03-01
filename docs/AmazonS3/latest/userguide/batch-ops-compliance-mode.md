# Using S3 Batch Operations with S3 Object Lock retention compliance mode

The following example builds on the previous examples of creating a trust policy and
setting S3 Batch Operations and S3 Object Lock configuration permissions on your objects.
This example sets the retention mode to `COMPLIANCE` and the `retain
 until date` to January 1, 2025. This example creates a job that targets
objects in the manifest bucket and reports the results in the reports bucket that you
identified.

To use the following examples, replace the `user input
 placeholders` with your own information.

The following AWS CLI examples show how to use Batch Operations to apply
S3 Object Lock retention compliance mode across multiple objects.

###### Example— Set S3 Object Lock retention compliance mode across multiple objects

```
export AWS_PROFILE='`aws-user`'
export AWS_DEFAULT_REGION='`us-west-2`'
export ACCOUNT_ID=`123456789012`
export ROLE_ARN='arn:aws:iam::`123456789012`:role/`batch_operations-objectlock`'

read -d '' `OPERATION` <<EOF
{
  "S3PutObjectRetention": {
    "Retention": {
      "RetainUntilDate":"`2025-01-01T00:00:00`",
      "Mode":"COMPLIANCE"
    }
  }
}
EOF

read -d '' `MANIFEST` <<EOF
{
  "Spec": {
    "Format": "S3BatchOperations_CSV_20180820",
    "Fields": [
      "Bucket",
      "Key"
    ]
  },
  "Location": {
    "ObjectArn": "arn:aws:s3:::``amzn-s3-demo-manifest-bucket`/compliance-objects-manifest.csv`",
    "ETag": "`Your-manifest-ETag`"
  }
}
EOF

read -d '' `REPORT` <<EOF
{
  "Bucket": "arn:aws:s3:::`ReportBucket`",
  "Format": "Report_CSV_20180820",
  "Enabled": true,
  "Prefix": "``amzn-s3-demo-completion-report-bucket`/compliance-objects-batch-operations`",
  "ReportScope": "AllTasks"
}
EOF

aws \
    s3control create-job \
    --account-id "${`ACCOUNT_ID`}" \
    --manifest "${`MANIFEST`//$'\n'}" \
    --operation "${`OPERATION`//$'\n'/}" \
    --report "${`REPORT`//$'\n'}" \
    --priority 10 \
    --role-arn "${`ROLE_ARN`}" \
    --client-request-token "$(uuidgen)" \
    --region "${`AWS_DEFAULT_REGION`}" \
    --description "`Set compliance retain-until to 1 Jul 2030`";
```

###### Example— Extend the `COMPLIANCE` mode's `retain until date` to January 15, 2025

The following example extends the `COMPLIANCE` mode's
`retain until date` to January 15, 2025.

```
export AWS_PROFILE='`aws-user`'
export AWS_DEFAULT_REGION='`us-west-2`'
export ACCOUNT_ID=`123456789012`
export ROLE_ARN='arn:aws:iam::`123456789012`:role/`batch_operations-objectlock`'

read -d '' `OPERATION` <<EOF
{
  "S3PutObjectRetention": {
    "Retention": {
      "RetainUntilDate":"`2025-01-15T00:00:00`",
      "Mode":"COMPLIANCE"
    }
  }
}
EOF

read -d '' `MANIFEST` <<EOF
{
  "Spec": {
    "Format": "S3BatchOperations_CSV_20180820",
    "Fields": [
      "Bucket",
      "Key"
    ]
  },
  "Location": {
    "ObjectArn": "arn:aws:s3:::``amzn-s3-demo-manifest-bucket`/compliance-objects-manifest.csv`",
    "ETag": "`Your-manifest-ETag`"
  }
}
EOF

read -d '' `REPORT` <<EOF
{
  "Bucket": "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`",
  "Format": "Report_CSV_20180820",
  "Enabled": true,
  "Prefix": "`reports/compliance-objects-batch_operations`",
  "ReportScope": "AllTasks"
}
EOF

aws \
    s3control create-job \
    --account-id "${`ACCOUNT_ID`}" \
    --manifest "${`MANIFEST`//$'\n'}" \
    --operation "${`OPERATION`//$'\n'/}" \
    --report "${`REPORT`//$'\n'}" \
    --priority 10 \
    --role-arn "${`ROLE_ARN`}" \
    --client-request-token "$(uuidgen)" \
    --region "${`AWS_DEFAULT_REGION`}" \
    --description "`Extend compliance retention to 15 Jan 2025`";
```

The following AWS SDK for Java examples show how to use Batch Operations to apply
S3 Object Lock retention compliance mode across multiple objects, including setting the retention mode to COMPLIANCE with a retain until date and extending the COMPLIANCE mode retain until date.

For examples of how to use Batch Operations to apply S3 Object Lock retention compliance mode across multiple objects with the AWS SDK for Java, see [Use CreateJob with an AWS SDK or CLI](../API/s3-control_example_s3-control_CreateJob_section.md "../API/s3-control_example_s3-control_CreateJob_section.md") in the _Amazon S3 API Reference_.
