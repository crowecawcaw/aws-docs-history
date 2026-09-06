

# Step 2: Create an IAM role for AWS Glue
<a name="create-an-iam-role"></a>

You need to grant your IAM role permissions that AWS Glue can assume when calling other services on your behalf. This includes access to Amazon S3 for any sources, targets, scripts, and temporary directories that you use with AWS Glue. Permission is needed by crawlers, jobs, and development endpoints.

You provide those permissions by using AWS Identity and Access Management (IAM). Add a policy to the IAM role that you pass to AWS Glue.

****To create an IAM role within the job editor****

1. When you create a job in the AWS Glue console, locate the role section.

1. Choose **Create new role**.

1. An inline role creation form opens, allowing you to:
   + Specify **Role name**; for example, `AWSGlueServiceRoleDefault`.
   + The managed policy `AWSGlueServiceRole` is automatically selected.
   + Review the trust policy to assume the role.
   + Add optional tags for metadata.

1. Choose **Create role**.

1. The newly created role is automatically selected for your job.

Alternatively, you can use the IAM console to create the role:

****To create an IAM role for AWS Glue using the IAM console****

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, choose **Roles**.

1. Choose **Create role**.

1.  Choose **AWS service** as the trusted entity type. Then, for service or use case, find and choose **AWS Glue**. Choose **Next**. 

1. On the **Add permissions** page, choose the policies that contain the required permissions; for example, the AWS managed policy `AWSGlueServiceRole` for general AWS Glue permissions and the AWS managed policy **AmazonS3FullAccess** for access to Amazon S3 resources. Then choose **Next**.
**Note**  
Ensure that one of the policies in this role grants permissions to your Amazon S3 sources and targets. You might want to provide your own policy for access to specific Amazon S3 resources. Data sources require `s3:ListBucket` and `s3:GetObject` permissions. Data targets require `s3:ListBucket`, `s3:PutObject`, and `s3:DeleteObject` permissions. For more information about creating an Amazon S3 policy for your resources, see [Specifying Resources in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-arn-format.html). For an example Amazon S3 policy, see [ Writing IAM Policies: How to Grant Access to an Amazon S3 Bucket](https://aws.amazon.com/blogs/security/writing-iam-policies-how-to-grant-access-to-an-amazon-s3-bucket/).   
If you plan to access Amazon S3 sources and targets that are encrypted with SSE-KMS, attach a policy that allows AWS Glue crawlers, jobs, and development endpoints to decrypt the data. For more information, see [Protecting Data Using Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html).   
The following is an example.  

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "kms:Decrypt"
         ],
         "Resource": [
           "arn:aws:kms:*:{{111122223333}}:key/{{key-id}}"
         ]
       }
     ]
   }
   ```

1.  Name your role and add a description (optional), then review the trust policy and permissions. For **Role name**, enter a name for your role; for example, `AWSGlueServiceRoleDefault`. Create the role with the name prefixed with the string `AWSGlueServiceRole` to allow the role to be passed from console users to the service. AWS Glue provided policies expect IAM service roles to begin with `AWSGlueServiceRole`. Otherwise, you must add a policy to allow your users the `iam:PassRole` permission for IAM roles to match your naming convention. Choose **Create Role**.
**Note**  
When you create a notebook with a role, that role is then passed to interactive sessions so that the same role can be used in both places. As such, the `iam:PassRole` permission needs to be part of the role's policy.   
Create a new policy for your role using the following example. Replace the account number with your own and the role name.   

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "iam:PassRole",
         "Resource": "arn:aws:iam::090000000210:role/<role_name>"
       }
     ]
   }
   ```

1.  Add tags to your role (optional). Tags are key-value pairs that you can add to AWS resources to help identify, organize, or search for resources. Then, choose **Create role**. 