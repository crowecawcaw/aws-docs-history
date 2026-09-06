

# Creating report plans using the AWS Backup console
<a name="create-report-plan-console"></a>

There are two types of reports. One type is a **jobs report**, which shows jobs finished in the last 24 hours and all active jobs. The second type of report is a **compliance report**. Compliance reports can monitor resource levels or the different controls that are in effect. When you create a report, you choose which type of report to create.

Depending on your type of account, the console display may vary. Only management accounts will see multi-account functionality.

Similar to a *backup plan*, you create a *report plan* to automate the creation of your reports and define their destination Amazon S3 bucket. A report plan requires that you have an S3 bucket to receive your reports. You can't use a bucket from another account. For instructions on setting up a new S3 bucket, see [Step 1: Create your first S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html#creating-bucket) in the *Amazon Simple Storage Service User Guide*.

**To create your report plan in the AWS Backup console**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the left navigation pane, choose **Reports**.

1. Choose **Create report plan**.

1. Choose one of the report templates from the list.

1. Enter a unique **Report plan name**. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (\_).

1. (Optional) Enter a **Report plan description**.

1. *Compliance report templates for one account only*. Choose one or more frameworks on which to report. You can add a maximum 1,000 frameworks to a report plan.

   1. Choose your AWS Region.

   1. Choose a framework from that Region.

   1. Choose **Add framework**.

1. (Optional) To add tags to your report plan, choose **Add tags to the report plan**.

1. If you are using a management account, you can specify which accounts you want to include in this report plan. You can select **Only my account**, which will generate reports on just the account to which you’re currently logged in. Or, you can select **One or more accounts in my organization** (*available to management and delegated administrator accounts*).

1. (*If you are creating a compliance report for one Region only, skip this step*). You can select which Regions to include in your report. Click the drop down menu to show Regions available to you. Select *All available Regions* or the Regions you prefer.

   1. The **Include new Regions when they are incorporated into Backup Audit Manager** check box will trigger new Regions to be included in your reports when they become available.

1. Choose the **File format** of your report. All reports can be exported in CSV format. Additionally, reports for a single Region can be exported in JSON format.

1. For **S3 bucket name**, choose a bucket from your account.

1. (Optional) Enter a bucket prefix.

   AWS Backup delivers your *current account, current Region* reports to `s3://{{amzn-s3-demo-bucket}}/prefix/Backup/{{accountID}}/{{Region}}/year/month/day/report-name`.

   AWS Backup delivers your *cross-account* reports to `s3://{{amzn-s3-demo-bucket}}/prefix/Backup/crossaccount/{{Region}}/year/month/day/report-name` 

   AWS Backup delivers your *cross-Region* reports to `s3://{{amzn-s3-demo-bucket}}/prefix/Backup/{{accountID}}/crossregion/year/month/day/report-name`

1. Choose **Create report plan**.

Next, you must allow your S3 bucket to receive reports from AWS Backup. After you create a report plan, AWS Backup Audit Manager automatically generates an S3 bucket access policy for you to apply.

If you encrypt your bucket using a customer managed KMS key, the KMS key policy must meet the following requirements:
+ The `Principal` attribute must include the Backup Audit Manager service-linked role [`AWSServiceRolePolicyForBackupReports`](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSServiceRolePolicyForBackupReports) ARN.
+ The `Action` attribute must include `kms:GenerateDataKey` at minimum.

 The policy [AWSServiceRolePolicyForBackupReports](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSServiceRolePolicyForBackupReports) has these permissions.

**To view and apply this access policy to your S3 bucket**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the left navigation pane, choose **Reports**.

1. Under **Report plan name**, select a report plan by choosing its name.

1. Choose **Edit**.

1. Choose **View access policy for S3 bucket**. You can also use the policy at the end of this procedure.

1. Choose **Copy permissions**.

1. Choose **Edit bucket policy**. Note that until the backup report is created the first time, the service-linked role referred to in the S3 bucket policy will not yet exist, resulting in the error "Invalid principal".

1. Copy the permissions to the **Policy**.

**Sample bucket policy**

------
#### [ JSON ]

****  

```
{
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
}
```

------

If you use a custom AWS Key Management Service to encrypt your target S3 bucket that stores the reports, include the following action in your policy:

```
      "Action":[
        "kms:GenerateDataKey"
      ],  
      "Resource":[
        "*"
      ],
```

## Using an S3 bucket encrypted with a cross-account KMS key
<a name="cross-account-kms-report-plan"></a>

If your S3 bucket (in Account A) is encrypted with a customer managed KMS key from a different account (Account B), complete the following additional steps to allow AWS Backup to deliver reports to the bucket.

**To configure a cross-account KMS key for Backup reports**

1. Add the S3 bucket policy as described in the preceding section.

1. Update the KMS key policy in Account B to grant permissions to the `AWSServiceRoleForBackupReports` service-linked role in Account A and to the IAM entity that creates the report plan:

   ```
   {
       "Version": "2012-10-17", 		 	 	 
       "Statement": [
           {
               "Sid": "Allow Backup Reports service-linked role to use the key",
               "Effect": "Allow",
               "Principal": {
                   "AWS": "arn:aws:iam::{{AccountA-ID}}:role/aws-service-role/reports.backup.amazonaws.com/AWSServiceRoleForBackupReports"
               },
               "Action": [
                   "kms:GenerateDataKey",
                   "kms:Encrypt"
               ],
               "Resource": "*"
           },
           {
               "Sid": "Allow IAM entity to create grants on the key",
               "Effect": "Allow",
               "Principal": {
                   "AWS": "arn:aws:iam::{{AccountA-ID}}:role/{{IAM-role-name}}"
               },
               "Action": "kms:CreateGrant",
               "Resource": "*"
           }
       ]
   }
   ```

   Replace {{AccountA-ID}} with the AWS account ID where the S3 bucket and AWS Backup report plan reside. Replace {{IAM-role-name}} with the IAM role you use to create the report plan.

1. From Account A, create a KMS grant for the service-linked role by running the following AWS CLI command with an IAM entity that has `kms:CreateGrant` permission on the key:

   ```
   aws kms create-grant \
       --key-id arn:aws:kms:{{region}}:{{AccountB-ID}}:key/{{key-id}} \
       --grantee-principal arn:aws:iam::{{AccountA-ID}}:role/aws-service-role/reports.backup.amazonaws.com/AWSServiceRoleForBackupReports \
       --operations GenerateDataKey
   ```

   Replace {{region}}, {{AccountB-ID}}, {{key-id}}, and {{AccountA-ID}} with your values.

1. Create your on-demand or scheduled report plan. Reports will be delivered to the S3 bucket encrypted with the cross-account KMS key.