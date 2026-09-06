

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Configuring your default export destination for evidence finder
<a name="settings-export-destination"></a>



When you run queries in evidence finder, you can export your search results into a comma-separated values (CSV) file. Use this setting to choose the default S3 bucket where Audit Manager saves your exported files.

## Prerequisites
<a name="settings-export-destination-prerequisites"></a>

Your S3 bucket must have the required permissions policy to allow CloudTrail to write the export files to it. More specifically, the bucket policy must include an `s3:PutObject` action and the bucket ARN, and list CloudTrail as the service principal. 
+ For an example permission policy that you can use, see [Resource-based policy examples for AWS Audit Manager](security_iam_resource-based-policy-examples.md). 
+ For instructions to attach this policy to your S3 bucket, see [Adding a bucket policy by using the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-bucket-policy.html). 
+ For more tips, see [configuration tips for your export destination](https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder-settings.html#settings-export-destination-tips) on this page. 

### Configuration tips for your export destination
<a name="settings-export-destination-tips"></a>

To ensure a successful file export, we recommend that you verify the following configurations for your export destination. 

**AWS Region**  
The AWS Region of your customer managed key (if you provided one) must match the Region of your assessment. For instructions on how to change your KMS key, see [Audit Manager data encryption settings](https://docs.aws.amazon.com/audit-manager/latest/userguide/general-settings.html#settings-KMS).

**Cross-account S3 buckets**  
Using a cross-account S3 bucket as your export destination isn't supported in the Audit Manager console. It's possible to specify a cross-account bucket using the AWS CLI or one of the AWS SDKs, but for simplicity, we recommend that you not do this. If you do choose to use a cross-account S3 bucket as your export destination, consider the following points.  
+ By default, S3 objects—such as CSV exports—are owned by the AWS account that uploads the object. You can use the [S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) setting to change this default behavior, so that any new objects that are written by accounts with the `bucket-owner-full-control` canned access control list (ACL) automatically become owned by the bucket owner.

  Although it's not a requirement, we recommend that you make the following changes to your cross-account bucket settings. Making these changes ensures that the bucket owner has full control of the exported files that you publish to their bucket.
  + [Set the object ownership of the S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html#enable-object-ownership) to *bucket owner preferred*, instead of the default * object writer* 
  + [Add a bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html#ensure-object-ownership) to ensure that objects uploaded to that bucket have the `bucket-owner-full-control` ACL
+ To allow Audit Manager to export files to a cross-account S3 bucket, you must add the following S3 bucket policy to your export destination bucket. Replace the {{placeholder text}} with your own information. The `Principal` element in this policy is the user or role that owns the assessment and exports the file. The `Resource` specifies the cross-account S3 bucket where the file is exported to.

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "Allow cross account file exports",
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

## Procedure
<a name="settings-export-destination-procedure"></a>

You can update this setting using the Audit Manager console, the AWS Command Line Interface (AWS CLI), or the Audit Manager API.

------
#### [ Audit Manager console ]

**To update your export destination settings on the Audit Manager console**

1. From the **Evidence finder** settings tab, go to the **Export destination** section.

1. Choose one of the following options:
   + If you want to remove the current S3 bucket, choose **Remove** to clear your settings.
   + If you want to save a default S3 bucket for the first time, proceed to step 3.

1. Specify the S3 bucket that you want to store your exported files in. 
   + Choose **Browse S3** to choose from a list of your buckets.
   + Alternatively, you can enter the bucket URI in this format: **s3://bucketname/prefix**
**Tip**  
To keep your destination bucket organized, you can create an optional folder for your CSV exports. To do so, append a slash (**/**) and a prefix to the value in the **Resource URI** box (for example, **/evidenceFinderCSVExports**). Audit Manager then includes this prefix when it adds the CSV file to the bucket, and Amazon S3 generates the path specified by the prefix. For more information about prefixes in Amazon S3, see [Organizing objects in the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) in the *Amazon Simple Storage Service* User Guide.

1. When you're done, choose **Save**.

For instructions on how to create an S3 bucket, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html) in the *Amazon S3 User Guide*.

------
#### [ AWS CLI ]

**To update your export destination settings in the AWS CLI**  
Run the [update-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-settings.html) command and use the `--default-export-destination` parameter to specify an S3 bucket.

In the following example, replace the {{placeholder text}} with your own information:

```
aws auditmanager update-settings --default-export-destination destinationType=S3,destination=amzn-s3-demo-destination-bucket
```

For instructions on how to create an S3 bucket, see [create-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html) in the *AWS CLI Command Reference*.

------
#### [ Audit Manager API ]

**To update your export destination settings using the API**  
Call the [UpdateSettings](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateSettings.html) operation and use the [defaultExportDestination](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateSettings.html#auditmanager-UpdateSettings-request-defaultAssessmentReportsDestination) parameter to specify an S3 bucket.

For instructions on how to create an S3 bucket, see [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html) in the *Amazon S3 API Reference*.

------