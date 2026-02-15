# Using S3 Batch Operations to turn off

S3 Object Lock legal holds

The following example builds on the previous examples of creating a trust policy, and
setting S3 Batch Operations and S3 Object Lock configuration permissions. This example
shows how to disable Object Lock legal hold on objects using Batch Operations.

The example first updates the role to grant `s3:PutObjectLegalHold`
permissions, creates a Batch Operations job that turns off (removes) legal hold from the
objects identified in the manifest, and then reports on it.

To use the following examples, replace the `user input
 placeholders` with your own information.

The following AWS CLI examples show how to use Batch Operations to turn off
S3 Object Lock legal holds across multiple objects.

###### Example— Updates the role to grant `s3:PutObjectLegalHold`

permissions

```
export AWS_PROFILE='`aws-user`'

read -d '' `legal_hold_permissions` <<EOF
{
    "Version": "2012-10-17"		 	 	 ,		 	 	 TCX5-2025-waiver;,
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObjectLegalHold"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
            ]
        }
    ]

EOF

aws iam put-role-policy --role-name `batch_operations-objectlock` --policy-name `legal-hold-permissions` --policy-document "${`legal_hold_permissions`}"
```

###### Example— Turn off legal hold

The following example turns off legal hold.

```
export AWS_PROFILE='`aws-user`'
export AWS_DEFAULT_REGION='`us-west-2`'
export ACCOUNT_ID=`123456789012`
export ROLE_ARN='arn:aws:iam::`123456789012`:role/`batch_operations-objectlock`'

read -d '' `OPERATION` <<EOF
{
  "S3PutObjectLegalHold": {
    "LegalHold": {
      "Status":"OFF"
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
    "ObjectArn": "arn:aws:s3:::``amzn-s3-demo-manifest-bucket`/legalhold-object-manifest.csv`",
    "ETag": "`Your-manifest-ETag`"
  }
}
EOF

read -d '' `REPORT` <<EOF
{
  "Bucket": "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`",
  "Format": "Report_CSV_20180820",
  "Enabled": true,
  "Prefix": "`reports/legalhold-objects-batch_operations`",
  "ReportScope": "AllTasks"
}
EOF

aws \
    s3control create-job \
    --account-id "${`ACCOUNT_ID`}" \
    --manifest "${`MANIFEST`//$'\n'}" \
    --operation "${`OPERATION`//$'\n'/}" \
    --report "${`REPORT`//$'\n'}" \
    --priority `10` \
    --role-arn "${`ROLE_ARN`}" \
    --client-request-token "$(uuidgen)" \
    --region "${`AWS_DEFAULT_REGION`}" \
    --description "`Turn off legal hold`";
```

For examples of how to use S3 Batch Operations to turn off S3 Object Lock legal hold with the AWS SDK for Java, see [Use CreateJob with an AWS SDK or CLI](../API/s3-control_example_s3-control_CreateJob_section.md "../API/s3-control_example_s3-control_CreateJob_section.md") in the _Amazon S3 API Reference_.
