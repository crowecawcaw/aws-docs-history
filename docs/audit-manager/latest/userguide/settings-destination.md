

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Configuring your default assessment report destination
<a name="settings-destination"></a>



When you generate an assessment report, Audit Manager publishes the report to the S3 bucket of your choice. This S3 bucket is referred to as an [](concepts.md#assessment-report-destination). You can choose the S3 bucket that Audit Manager stores your assessment reports in. 

## Prerequisites
<a name="settings-destination-prerequisites"></a>

### Configuration tips for your assessment report destination
<a name="settings-assessment-report-destination-tips"></a>

To ensure the successful generation of your assessment report, we recommend that you use the following configurations for your assessment report destination. 

**Same-Region buckets**  
We recommend that you use an S3 bucket that's in the same AWS Region as your assessment. When you use a same-Region bucket and assessment, your assessment report can include up to 22,000 evidence items. Conversely, when you use a cross-Region bucket and assessment, only 3,500 evidence items can be included.

**AWS Region**  
The AWS Region of your customer managed key (if you provided one) must match the Region of your assessment and your assessment report destination S3 bucket. For instructions on how to change the KMS key, see [Configuring your data encryption settings](settings-KMS.md). For a list of supported Audit Manager Regions, see [AWS Audit Manager endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/audit-manager.html) in the *Amazon Web Services General Reference*. 

**S3 bucket encryption**  
If your assessment report destination has a bucket policy that requires server-side encryption (SSE) using [SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html#require-sse-kms), then the KMS key used in that bucket policy must match the KMS key that you configured in your Audit Manager data encryption settings. If you haven't configured a KMS key in your Audit Manager settings, and your assessment report destination bucket policy requires SSE, ensure that the bucket policy allows [SSE-S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html). For instructions on how to configure the KMS key that's used for data encryption, see [Configuring your data encryption settings](settings-KMS.md).

**Cross-account S3 buckets**  
Using a cross-account S3 bucket as your assessment report destination isn't supported in the Audit Manager console. It's possible to specify a cross-account bucket as your assessment report destination by using the AWS CLI or one of the AWS SDKs, but for simplicity, we recommend that you not do this.   
For optimal security and performance, we recommend using an S3 bucket in the same AWS account and region as your assessment. 
If you do choose to use a cross-account S3 bucket as your assessment report destination, consider the following points.  
+ By default, S3 objects—such as assessment reports—are owned by the AWS account that uploads the object. You can use the [S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) setting to change this default behavior so that any new objects that are written by accounts with the `bucket-owner-full-control` canned access control list (ACL) automatically become owned by the bucket owner. 

  Although it's not a requirement, we recommend that you make the following changes to your cross-account bucket settings. Making these changes ensures that the bucket owner has full control of the assessment reports that you publish to their bucket.
  + [Set the object ownership of the S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html#enable-object-ownership) to *bucket owner preferred*, instead of the default * object writer* 
  + [Add a bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html#ensure-object-ownership) to ensure that objects uploaded to that bucket have the `bucket-owner-full-control` ACL
+ To allow Audit Manager to publish reports in a cross-account S3 bucket, you must add the following S3 bucket policy to your assessment report destination. Replace the {{placeholder text}} with your own information. The `Principal` element in this policy is the user or role that owns the assessment and creates the assessment report. The `Resource` specifies the cross-account S3 bucket where the report is published.

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "Allow cross account assessment report publishing",
              "Effect": "Allow",
              "Principal": {
                  "AWS": "arn:aws:iam::{{111122223333}}:user/{{AssessmentOwnerUserName}}"
              },
              "Action": [
                  "s3:ListBucket",
                  "s3:PutObject",
                  "s3:GetObject",
                  "s3:GetBucketLocation",
                  "s3:PutObjectAcl",
                  "s3:DeleteObject"
              ],
              "Resource": [
                  "arn:aws:s3:::{{CROSS-ACCOUNT-BUCKET}}",
                  "arn:aws:s3:::{{CROSS-ACCOUNT-BUCKET/*}}"
              ]
          }
      ]
  }
  ```

------

### Security best practices for your assessment report destination
<a name="settings-destination-security"></a>

Audit Manager publishes your assessment reports to the Amazon S3 bucket that you specify as your assessment report destination. Under the AWS Shared Responsibility Model, you are responsible for confirming that a trusted AWS account owns this bucket. For more information about your security responsibilities, see [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) on the AWS website.

To protect your assessment reports, we recommend that you implement one or more of the following controls.

**Restrict S3 actions to trusted accounts by using the `s3:ResourceAccount` condition key**  
Add an `s3:ResourceAccount` condition to the IAM policy attached to the identity that Audit Manager uses to publish assessment reports. This condition prevents the identity from writing to buckets owned by accounts other than those you specify. The condition applies regardless of the bucket's own access policy.  
For more information, see [Limit access to Amazon S3 buckets owned by specific AWS accounts](https://aws.amazon.com/blogs/storage/limit-access-to-amazon-s3-buckets-owned-by-specific-aws-accounts/).

**Restrict S3 actions to your organization by using SCPs**  
If you use , create a service control policy (SCP) that denies S3 actions on resources outside of your organization. The following example policy denies all S3 actions to resources outside your organization. The condition checks whether the `aws:ResourceOrgID` matches your organization ID.  

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyS3ActionsOutsideOrganization",
      "Effect": "Deny",
      "Action": "s3:*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:ResourceOrgID": "{{o-xxxxxxxxxx}}"
        }
      }
    }
  ]
}
```
Replace {{o-xxxxxxxxxx}} with your organization ID. For more information, see [aws:ResourceOrgID](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourceorgid) in the *IAM User Guide*.

**Use a customer managed KMS key for data encryption**  
When you configure Audit Manager to use a customer managed key for data encryption, Audit Manager encrypts assessment reports before writing them to Amazon S3. If a report is published to a bucket owned by an unauthorized party, the report contents remain encrypted. The contents are unreadable without access to your KMS key. For instructions, see [Configuring your data encryption settings](settings-KMS.md).

**Use S3 buckets in your account regional namespace**  
S3 buckets created in your account regional namespace include your AWS account ID and AWS Region in the bucket name. No other account can create these buckets or claim the bucket name. For more information, see [Account-level bucket namespaces](https://docs.aws.amazon.com/AmazonS3/latest/userguide/gpbucketnamespaces.html#account-regional-gp-buckets) in the *Amazon Simple Storage Service User Guide*.

## Procedure
<a name="settings-destination-procedure"></a>

You can update this setting using the Audit Manager console, the AWS Command Line Interface (AWS CLI), or the Audit Manager API.

------
#### [ Audit Manager console ]

**To update your default assessment report destination on the Audit Manager console**

1. From the **Assessment** settings tab, go to the **Assessment report destination** section.

1. To use an existing S3 bucket, select a bucket name from the dropdown menu.

1. To create a new S3 bucket, choose **Create new bucket**.

1. When you're done, choose **Save**.

------
#### [ AWS CLI ]

**To update your default assessment report destination in the AWS CLI**  
Run the [update-settings](https://docs.aws.amazon.com/cli/latest/reference/auditmanager/update-settings.html) command and use the `--default-assessment-reports-destination` parameter to specify an S3 bucket.

In the following example, replace the {{placeholder text}} with your own information:

```
aws auditmanager update-settings --default-assessment-reports-destination destinationType=S3,destination={{s3://amzn-s3-demo-destination-bucket}}
```

------
#### [ Audit Manager API ]

**To update your default assessment report destination using the API**  
Call the [UpdateSettings](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateSettings.html) operation and use the [defaultAssessmentReportsDestination](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateSettings.html#auditmanager-UpdateSettings-request-defaultAssessmentReportsDestination) parameter to specify an S3 bucket.

------

## Additional resources
<a name="settings-destination-additional-resources"></a>
+ [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)
+ [Assessment reports](assessment-reports.md)