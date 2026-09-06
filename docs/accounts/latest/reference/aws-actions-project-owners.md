

# AWS actions for project owners
<a name="aws-actions-project-owners"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

When you own your project, you have administrative control over your project. This includes tasks you can complete in [Use AWS Settings](use-aws-settings.md). You also have the ability to perform root-only actions. These actions can't be completed by your team members.

The current root-only actions you can perform are the following:
+ Edit or delete an S3 bucket policy that denies all principals. You might do this to unlock an S3 bucket with a misconfigured bucket policy.
+ Edit or delete an SQS resource-based policy that denies all principals. You might do this to unlock an SQS queue with a misconfigured resource-based policy.

**To perform a root-only action**

1. Login into your project and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the console, choose **Root access management**.

1. For privilege action, choose the privileged action you want to take in the member account.
   + Select **Delete Amazon S3 bucket policy** to remove a misconfigured bucket policy that denies all principals from accessing the Amazon S3 bucket.

     1. Enter the S3 URI, or choose **Browse S3** to select a name from the buckets in your project.

     1. Choose **Delete bucket policy**.

     1. Use the Amazon S3 console to correct the bucket policy after deleting the misconfigured policy. For more information, see [Adding a bucket policy by using the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-bucket-policy.html) in the *Amazon S3 User Guide*.
   + Select **Delete Amazon SQS policy** to delete a resource-based policy that denies all principals from accessing an Amazon SQS queue.

     1. Enter the queue name in **SQS queue name**.

     1. Choose **Delete SQS policy**.

     1. Use the Amazon SQS console to correct the queue policy after deleting the misconfigured policy. For more information, see [Configuring an access policy in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-add-permissions.html) in the *Amazon SQS Developer Guide*.