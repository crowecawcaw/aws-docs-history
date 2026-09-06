

# Configure IAM permissions
<a name="configure-iam-role-policy-credentials"></a>

Amazon Location Jobs requires an IAM execution role that grants the service permission to access your Amazon S3 buckets. When you run a job, Amazon Location assumes this role to read input files from your input bucket and write output results to your output bucket on your behalf. You provide these permissions by creating an IAM policy with the required Amazon S3 permissions and attaching it to an IAM role with a trust policy that allows the Amazon Location service to assume the role.

**Note**  
The Amazon S3 input and output buckets you create must exist in the same AWS Region where you plan to run your jobs. The IAM resources you create must be created in the same account.

## Step 1: Create an IAM policy
<a name="create-iam-policy-jobs"></a>

Create an IAM policy that grants the permissions required for Amazon Location jobs.

**To create an IAM policy for Amazon Location jobs**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/). 

1. In the navigation pane, choose **Policies**. 

1. Choose **Create policy**. 

1. Choose the **JSON** tab and enter the following policy document, replacing {{INPUT\_BUCKET\_NAME}} and {{OUTPUT\_BUCKET\_NAME}} with your bucket names:

   ```
   {
     "Version": "2012-10-17", 		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "s3:GetObject",
           "s3:ListBucket",
           "s3:GetObjectVersion",
           "s3:GetBucketVersioning"
         ],
         "Resource": [
           "arn:aws:s3:::{{INPUT_BUCKET_NAME}}",
           "arn:aws:s3:::{{INPUT_BUCKET_NAME}}/*"
         ]
       },
       {
         "Effect": "Allow",
         "Action": [
           "s3:PutObject",
           "s3:AbortMultipartUpload"
         ],
         "Resource": [
           "arn:aws:s3:::{{OUTPUT_BUCKET_NAME}}/*"
         ]
       }
     ]
   }
   ```

1. Choose **Next**. 

1. For **Policy name**, enter a descriptive name such as `{{LocationJobsS3AccessPolicy}}`. 

1. Choose **Create policy**. 

The following table describes the permissions granted by this policy:


| Permission | Description | 
| --- | --- | 
|  s3:GetObject  | Allows Amazon Location to read input files from your input bucket. | 
|  s3:ListBucket  | Allows Amazon Location to list files in your input bucket to identify all input files for processing. | 
|  s3:GetObjectVersion  | Allows Amazon Location to access specific versions of input files. Required because versioning must be enabled on your buckets. | 
|  s3:GetBucketVersioning  | Allows Amazon Location to verify that versioning is enabled on your input bucket. | 
|  s3:PutObject  | Allows Amazon Location to write output results to your output bucket. | 
|  s3:AbortMultipartUpload  | Allows Amazon Location to clean up failed multipart uploads when writing large output files. | 

**Note**  
This policy follows the principle of least privilege by granting only the permissions required for Amazon Location Jobs to function. The policy restricts read permissions to your input bucket and write permissions to your output bucket.

**To create an IAM policy using the AWS CLI**

1. Create a file named `location-jobs-policy.json` with the following content, replacing {{INPUT\_BUCKET\_NAME}} and {{OUTPUT\_BUCKET\_NAME}} with your bucket names:

   ```
   {
     "Version": "2012-10-17", 		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "s3:GetObject",
           "s3:ListBucket",
           "s3:GetObjectVersion",
           "s3:GetBucketVersioning"
         ],
         "Resource": [
           "arn:aws:s3:::{{INPUT_BUCKET_NAME}}",
           "arn:aws:s3:::{{INPUT_BUCKET_NAME}}/*"
         ]
       },
       {
         "Effect": "Allow",
         "Action": [
           "s3:PutObject",
           "s3:AbortMultipartUpload"
         ],
         "Resource": [
           "arn:aws:s3:::{{OUTPUT_BUCKET_NAME}}/*"
         ]
       }
     ]
   }
   ```

1. Create the policy:

   ```
   aws iam create-policy \
       --policy-name {{LocationJobsS3AccessPolicy}} \
       --policy-document file://location-jobs-policy.json
   ```

1. Note the policy ARN from the output. You need this ARN in the next step.

## Step 2: Create an execution role
<a name="create-execution-role-jobs"></a>

Create an IAM role that Amazon Location assumes to access your Amazon S3 buckets during job execution.

The trust policy allows the Amazon Location service (`geo.amazonaws.com`) to assume this role. This trust relationship is required for Amazon Location to access your Amazon S3 buckets during job execution.

**To create an execution role for Amazon Location jobs**

1. In the IAM console navigation pane, choose **Roles**. 

1. Choose **Create role**. 

1. For **Trusted entity type**, choose **Custom trust policy**. 

1. Enter the following trust policy, replacing {{ACCOUNT\_ID}} with your AWS account ID:

   ```
   {
     "Version": "2012-10-17", 		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Service": "geo.amazonaws.com"
         },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "{{ACCOUNT_ID}}"
           }
         }
       }
     ]
   }
   ```

1. Choose **Next**. 

1. Search for and select the policy you created in Step 1 (such as `{{LocationJobsS3AccessPolicy}}`). 

1. Choose **Next**. 

1. For **Role name**, enter a descriptive name such as `LocationServiceJobExecutionRole`. 

1. Choose **Create role**. 

**To create an execution role using the AWS CLI**

1. Create a file named `trust-policy.json` with the following content, replacing {{ACCOUNT\_ID}} with your AWS account ID:

   ```
   {
     "Version": "2012-10-17", 		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Service": "geo.amazonaws.com"
         },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "{{ACCOUNT_ID}}"
           }
         }
       }
     ]
   }
   ```

1. Create the role:

   ```
   aws iam create-role \
       --role-name LocationServiceJobExecutionRole \
       --assume-role-policy-document file://trust-policy.json
   ```

1. Attach the policy you created in Step 1 (replace {{ACCOUNT\_ID}} with your AWS account ID and {{LocationJobsS3AccessPolicy}} with your policy name if different):

   ```
   aws iam attach-role-policy \
       --role-name LocationServiceJobExecutionRole \
       --policy-arn arn:aws:iam::{{ACCOUNT_ID}}:policy/{{LocationJobsS3AccessPolicy}}
   ```

1. Get the role ARN:

   ```
   aws iam get-role \
       --role-name LocationServiceJobExecutionRole \
       --query 'Role.Arn' \
       --output text
   ```

1. Note the role ARN from the output. You need this ARN when starting jobs using the `ExecutionRoleArn` parameter.

After creating the role, note the role ARN. You need this ARN when starting jobs using the `ExecutionRoleArn` parameter. For more information, see [Prepare input data](preparing-input-data.md).

## Security best practices
<a name="iam-security-best-practices"></a>

Follow these security best practices when configuring IAM permissions for Amazon Location Jobs:
+  **Use specific bucket ARNs:** Replace the placeholder bucket names in the policy with your actual bucket names to restrict access to only the buckets you intend to use.
+  **Separate input and output buckets:** Use different buckets for input and output to maintain clear separation of read and write permissions.
+  **Enable Amazon S3 bucket versioning:** Versioning must be enabled on your buckets. This is required for Amazon Location Jobs to function properly.
+  **Use Amazon S3 bucket policies:** Add bucket policies to your Amazon S3 buckets for additional access control beyond IAM policies.
+  **Monitor role usage:** Use to monitor when and how the execution role is used by Amazon Location Jobs.