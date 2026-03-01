# Creating report plans using the AWS Backup console

There are two types of reports. One type is a **jobs report**, which
shows jobs finished in the last 24 hours and all active jobs. The second type of report is a
**compliance report**. Compliance reports can monitor resource levels or
the different controls that are in effect. When you create a report, you choose which type
of report to create.

Depending on your type of account, the console display may vary. Only management
accounts will see multi-account functionality.

Similar to a _backup plan_, you create a _report
plan_ to automate the creation of your reports and define their destination Amazon S3
bucket. A report plan requires that you have an S3 bucket to receive your reports. You can't
use a bucket from another account. For instructions on setting up a new S3 bucket, see
[Step 1: Create your
first S3 bucket](../../../AmazonS3/latest/userguide/GetStartedWithS3.md#creating-bucket "../../../AmazonS3/latest/userguide/GetStartedWithS3.md#creating-bucket") in the _Amazon Simple Storage Service User Guide_.

###### To create your report plan in the AWS Backup console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the left navigation pane, choose **Reports**.
3. Choose **Create report plan**.
4. Choose one of the report templates from the list.
5. Enter a unique **Report plan name**. The name must be between 1 and
   256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers
   (0-9), and underscores (\_).
6. (Optional) Enter a **Report plan description**.
7. _Compliance report templates for one account only_. Choose one or
   more frameworks on which to report. You can add a maximum 1,000 frameworks to a report
   plan.
   1. Choose your AWS Region.
   2. Choose a framework from that Region.
   3. Choose **Add framework**.

8. (Optional) To add tags to your report plan, choose **Add tags to the report
   plan**.
9. If you are using a management account, you can specify which accounts you want to
   include in this report plan. You can select **Only my account**, which
   will generate reports on just the account to which you’re currently logged in. Or, you
   can select **One or more accounts in my organization**
   (_available to management and delegated administrator
   accounts_).
10. (_If you are creating a compliance report for one Region only, skip this
    step_). You can select which Regions to include in your report. Click the
    drop down menu to show Regions available to you. Select _All available
    Regions_ or the Regions you prefer.
    1. The **Include new Regions when they are incorporated into Backup Audit
       Manager** check box will trigger new Regions to be included in your
       reports when they become available.

11. Choose the **File format** of your report. All reports can be
    exported in CSV format. Additionally, reports for a single Region can be exported
    in JSON format.
12. For **S3 bucket name**, choose a bucket from your account.
13. (Optional) Enter a bucket prefix.

AWS Backup delivers your _current account, current Region_ reports to
`s3://`amzn-s3-demo-bucket`/prefix/Backup/`accountID`/`Region`/year/month/day/report-name`.

AWS Backup delivers your _cross-account_ reports to
`s3://`amzn-s3-demo-bucket`/prefix/Backup/crossaccount/`Region`/year/month/day/report-name`

AWS Backup delivers your _cross-Region_ reports to
`s3://`amzn-s3-demo-bucket`/prefix/Backup/`accountID`/crossregion/year/month/day/report-name` 14. Choose **Create report plan**.
Next, you must allow your S3 bucket to receive reports from AWS Backup. After you create a
report plan, AWS Backup Audit Manager automatically generates an S3 bucket access policy for you
to apply.

If you encrypt your bucket using a customer managed KMS key, the KMS key policy must
meet the following requirements:

- The `Principal` attribute must include the Backup Audit Manager
  service-linked role [`AWSServiceRolePolicyForBackupReports`](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSServiceRolePolicyForBackupReports "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSServiceRolePolicyForBackupReports") ARN.

- The `Action` attribute must include `kms:GenerateDataKey` and
  `kms:Decrypt` at minimum.
  The policy [AWSServiceRolePolicyForBackupReports](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSServiceRolePolicyForBackupReports "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSServiceRolePolicyForBackupReports") has these permissions.

###### To view and apply this access policy to your S3 bucket

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the left navigation pane, choose **Reports**.
3. Under **Report plan name**, select a report plan by choosing its
   name.
4. Choose **Edit**.
5. Choose **View access policy for S3 bucket**. You can also use the
   policy at the end of this procedure.
6. Choose **Copy permissions**.
7. Choose **Edit bucket policy**. Note that until the backup report is
   created the first time, the service-linked role referred to in the S3 bucket policy will
   not yet exist, resulting in the error "Invalid principal".
8. Copy the permissions to the **Policy**.
   **Sample bucket policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "AWS":"arn:aws:iam::123456789012:role/aws-service-role/reports.backup.amazonaws.com/AWSServiceRoleForBackupReports"
 },
 "Action":"s3:PutObject",
 "Resource":[
 "arn:aws:s3:::BucketName/*"
 ],
 "Condition":{
 "StringEquals":{
 "s3:x-amz-acl":"bucket-owner-full-control"
 }
 }
 }
 ]
}`

```

If you use a custom AWS Key Management Service to encrypt your target S3 bucket that stores the reports,
include the following actions in your policy:

```

      "Action":[
        "kms:GenerateDataKey",
        "kms:Encrypt"
      ],
      "Resource":[
        "*"
      ],
```
