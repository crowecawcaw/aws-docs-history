# Job attachments in Deadline Cloud

With _job attachments_ you can transfer files back and forth between
your workstation and AWS Deadline Cloud. With job attachments, you don't need to manually set up an Amazon S3
bucket for your files. Instead, when you create a queue with the Deadline Cloud console, you choose the
bucket for your job attachments.

The first time that you submit a job to Deadline Cloud, all of the files for the job are transferred
to Deadline Cloud. For subsequent submissions, only the files that have changed are transferred, saving
both time and bandwidth.

After processing is complete, you can download the result from the job detail page, or by
using the Deadline Cloud CLI `deadline job download-output` command.

You can use the same S3 bucket for multiple queues. Set a different root prefix for each
queue to organize the attachments in the bucket.

When you create a queue with the console, you can either choose an existing AWS Identity and Access Management
(IAM) role or you can have the console create a new role. If the console creates the role, it
sets permissions to access the bucket that's specified for the queue. If you choose an existing
role, you must grant the role permissions to access the S3 bucket.

## Encryption for job attachment S3

buckets

Job attachment files are encrypted in your S3 bucket by default. This encryption helps secure your
information from unauthorized access. You don't need to do anything to have your files encrypted
with keys provided by Deadline Cloud. For more information, see [Amazon S3 now automatically encrypts all
new objects](../../../AmazonS3/latest/userguide/default-encryption-faq.md "../../../AmazonS3/latest/userguide/default-encryption-faq.md") in the _Amazon S3 User Guide_.

You can use your own customer managed AWS Key Management Service key to encrypt the S3 bucket that contains
your job attachments. To do so, you must modify the IAM role for the queue associated with the
bucket to allow access to the AWS KMS key.

###### To open the IAM policy editor for the queue role

1. Sign in to the AWS Management Console and open the Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home"). From the main page,
   in the **Get started** section, choose **View
   farms**.
2. From the list of farms, choose the farm that contains the queue to modify.
3. From the list of queues, choose the queue to modify.
4. In the **Queue details** section, choose the **Service
   role** to open the IAM console for the service role.

Next, complete the following procedure.

###### To update the role policy with permission for AWS KMS

1. From the list of **Permissions policies**, choose the policy for the
   role.
2. In the **Permissions defined in this policy** section, choose
   **Edit**.
3. Choose **Add new statement**.
4. Copy and paste the following policy into the editor. Change the
   `Region`,
   `accountID`, and
   `keyID` to your own values.

```
{
   "Effect": "Allow",
   "Action": [
       "kms:Decrypt",
       "kms:DescribeKey",
       "kms:GenerateDataKey"
   ],
   "Resource": [
       "arn:aws:kms:`us-east-1`:`111122223333`:key/`keyID`"
   ]
}
```

5. Choose **Next**.
6. Review the changes to the policy, and then when you're satisfied, choose **Save
   changes**.

## Replace job attachments bucket

You can replace your current job attachments bucket with a different job attachments bucket. You will find a button under the **Job Attachments** tab in the queue details. You can use it to either change the job attachments bucket or replace the root folder inside the same bucket to upload the job attachments.

###### To access job attachments settings

1. Go to **Queue details**, then locate the **Job Attachments** tab.
2. From the job attachments tab, there are 2 options:
   1. Change the job attachments bucket by doing the following:
      1. Select a new S3 bucket.
      2. Update the queue's service role policy to grant access to the new bucket.OR

   2. Change the root folder within an existing bucket by doing the following:
      1. Modify the root folder name.
      2. Update the resource ARN in the queue service role.

###### To update the service role

1. Navigate to your farm > queue > queue service role.
2. Choose **Edit in JSON**.
3. Locate the resource ARN (default root folder is **DeadlineCloud**):

```
  "arn:aws:s3:::<your-job-attachments-bucket-name>/DeadlineCloud/*"
]
```

4. Update the ARN with new bucket or folder:

```
 "arn:aws:s3:::<your-job-attachments-NEW-bucket-name>/NEW-ROOT-FOLDER-NAME/*"
]
```

5. Verify permissions after making these changes to ensure proper access.

## Managing job attachments in S3

buckets

Deadline Cloud stores the job attachment files required for your job in an S3 bucket. These files
accumulate over time, leading to increased Amazon S3 costs. To reduce costs, you can apply an S3
Lifecycle configuration to your S3 bucket. This configuration can automatically delete files in
the bucket. Because the S3 bucket is in your account, you can choose to modify or remove the S3
Lifecycle configuration at any time. For more information, see [Examples of S3 Lifecycle
configuration](../../../AmazonS3/latest/userguide/lifecycle-configuration-examples.md "../../../AmazonS3/latest/userguide/lifecycle-configuration-examples.md") in the _Amazon S3 User Guide_.

For a more granular S3 bucket management solution, you can set up your AWS account to
expire objects in an S3 bucket based on the last time that they were accessed. For more
information, see [Expiring Amazon S3 objects based on last accessed date to decrease costs](https://aws.amazon.com/blogs/architecture/expiring-amazon-s3-objects-based-on-last-accessed-date-to-decrease-costs/ "https://aws.amazon.com/blogs/architecture/expiring-amazon-s3-objects-based-on-last-accessed-date-to-decrease-costs/") on the AWS
Architecture Blog.
