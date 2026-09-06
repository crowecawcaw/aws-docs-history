

# Create a snapshot
<a name="create-snapshot"></a>

Before you can create a snapshot, you must provide an Amazon S3 bucket with the necessary permissions. For information on creating a bucket, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html). Enable bucket versioning and server access logging. These settings can be enabled from the bucket's **Properties** tab after provisioning. 

**Note**  
This Amazon S3 bucket's lifecycle will not be managed within the product. You will need to manage the bucket lifecycle from the console.

**To add permissions to the bucket:**

1. Select the bucket you created from the **Buckets** list.

1. Select the **Permissions** tab. 

1. Under **Bucket policy**, choose **Edit**. 

1. Add the following statement to the bucket policy. Replace these values with your own: 
   + {{111122223333}} -> your AWS Account ID
   + {{{RES\_ENVIRONMENT\_NAME}}} -> your RES environment name
   + {{amzn-s3-demo-bucket}} -> your S3 bucket name
**Important**  
There are limited version strings supported by AWS. For more information, see [https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html).

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "Export-Snapshot-Policy",
               "Effect": "Allow",
               "Principal": {
                   "AWS": "arn:aws:iam::{{111122223333}}:role/{{{RES_ENVIRONMENT_NAME}}}-cluster-manager-role"
               },
               "Action": [
                   "s3:GetObject",
                   "s3:ListBucket",
                   "s3:AbortMultipartUpload",
                   "s3:PutObject",
                   "s3:PutObjectAcl"
               ],
               "Resource": [
                   "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                   "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
               ]
           },
           {
               "Sid": "AllowSSLRequestsOnly",
               "Action": "s3:*",
               "Effect": "Deny",
               "Resource": [
                   "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                   "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
               ],
               "Condition": {
                   "Bool": {
                       "aws:SecureTransport": "false"
                   }
               },
               "Principal": "*"
           }
       ]
   }
   ```

------

**To create the snapshot:**

1. Choose **Create Snapshot**. 

1. Enter the name of the Amazon S3 bucket you created. 

1. Enter the path where you would like the snapshot stored within the bucket. For example, **october2023/23**. 

1. Choose **Submit**.   
![Create a new snapshot](http://docs.aws.amazon.com/res/latest/ug/images/res-createsnapshot.png)

1. After five to ten minutes, choose **Refresh** on the Snapshots page to check the status. A snapshot will not be valid until the status changes from IN\_PROGRESS to COMPLETED.