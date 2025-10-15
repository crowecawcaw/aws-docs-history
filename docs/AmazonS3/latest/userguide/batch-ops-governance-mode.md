# Use S3 Batch Operations with S3 Object Lock
 retention governance mode

The following example builds on the previous example of creating a trust policy, and
 setting S3 Batch Operations and S3 Object Lock configuration permissions. This example
 shows how to apply S3 Object Lock retention governance with the `retain until
 date` of January 30, 2025, across multiple objects. It creates a Batch Operations
 job that uses the manifest bucket and reports the results in the reports bucket.

To use the following examples, replace the ``user input
 placeholders`` with your own information. 

The following AWS CLI examples show how to use Batch Operations to apply
 S3 Object Lock retention governance mode across multiple objects.

###### Example — Apply S3 Object Lock retention governance across multiple
 objects with the retain until date of January 30, 2025


```
export AWS_PROFILE='`aws-user`'
export AWS_DEFAULT_REGION='`us-west-2`'
export ACCOUNT_ID=`123456789012`
export ROLE_ARN='arn:aws:iam::`123456789012`:role/`batch_operations-objectlock`'

read -d '' `OPERATION` <<EOF
{
  "S3PutObjectRetention": {
    "Retention": {
      "RetainUntilDate":"`2025-01-30T00:00:00`",
      "Mode":"GOVERNANCE"
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
    "ObjectArn": "arn:aws:s3:::``amzn-s3-demo-manifest-bucket`/governance-objects-manifest.csv`",
    "ETag": "`Your-manifest-ETag`"
  }
}
EOF

read -d '' `REPORT` <<EOF
{
  "Bucket": "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`T",
  "Format": "Report_CSV_20180820",
  "Enabled": true,
  "Prefix": "`reports/governance-objects`",
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
    --description "`Put governance retention`";
```
###### Example — Bypass retention governance across multiple objects

The following example builds on the previous example of creating a trust
 policy, and setting S3 Batch Operations and S3 Object Lock configuration
 permissions. It shows how to bypass retention governance across multiple
 objects and creates a Batch Operations job that uses the manifest bucket and
 reports the results in the reports bucket.


```
export AWS_PROFILE='`aws-user`'

read -d '' bypass_governance_permissions <<EOF
{
    "Version": "2012-10-17"		 	 	 ,		 	 	 TCX5-2025-waiver;,
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:BypassGovernanceRetention"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
            ]
        }
    ]
}
EOF

aws iam put-role-policy --role-name `batch-operations-objectlock` --policy-name `bypass-governance-permissions` --policy-document "${`bypass_governance_permissions`}"

export AWS_PROFILE='`aws-user`'
export AWS_DEFAULT_REGION='`us-west-2`'
export ACCOUNT_ID=`123456789012`
export ROLE_ARN='arn:aws:iam::`123456789012`:role/`batch_operations-objectlock`'

read -d '' `OPERATION` <<EOF
{
  "S3PutObjectRetention": {
    "BypassGovernanceRetention": true,
    "Retention": {
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
    "ObjectArn": "arn:aws:s3:::``amzn-s3-demo-manifest-bucket`/governance-objects-manifest.csv`",
    "ETag": "`Your-manifest-ETag`"
  }
}
EOF

read -d '' REPORT <<EOF
{
  "Bucket": "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`",
  "Format": "Report_CSV_20180820",
  "Enabled": true,
  "Prefix": "`reports/batch_operations-governance`",
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
    --description "`Remove governance retention`";
```
The following AWS SDK for Java examples show how to apply S3 Object Lock retention
 governance with the `retain until date` set to January 30, 2025
 across multiple objects, including applying Object Lock retention governance across multiple
 objects with a retain until date and bypassing retention governance across multiple objects.

For examples of how to use Batch Operations with S3 Object Lock retention governance mode with the AWS SDK for Java, see [Use CreateJob with an AWS SDK or CLI](../API/s3-control_example_s3-control_CreateJob_section.md "../API/s3-control_example_s3-control_CreateJob_section.md") in the *Amazon S3 API Reference*.
