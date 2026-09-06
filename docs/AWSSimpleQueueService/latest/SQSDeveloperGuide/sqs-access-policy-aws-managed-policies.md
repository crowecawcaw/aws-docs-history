

# Amazon SQS updates to AWS managed policies
<a name="sqs-access-policy-aws-managed-policies"></a>

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AmazonSQSFullAccess
<a name="security-iam-awsmanpol-AmazonSQSFullAccess"></a>

You can attach the `AmazonSQSFullAccess` policy to your Amazon SQS identities. This policy grants permissions that allow full access to Amazon SQS.

To view the permissions for this policy, see [AmazonSQSFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSQSFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonSQSReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonSQSReadOnlyAccess"></a>

You can attach the `AmazonSQSReadOnlyAccess` policy to your Amazon SQS identities. This policy grants permissions that allow read-only access to Amazon SQS.

To view the permissions for this policy, see [AmazonSQSReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSQSReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: SQSUnlockQueuePolicy
<a name="security-iam-awsmanpol-SQSUnlockQueuePolicy"></a>

If you incorrectly configured your queue policy for a member account to deny all users access to your Amazon SQS queue, you can use the `SQSUnlockQueuePolicy` AWS managed policy to unlock the queue.

For more information on how to remove a misconfigured queue policy that denies all principals from accessing an Amazon SQS queue, see [Perform a privileged task on an AWS Organizations member account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user-privileged-task.html) in the *IAM User Guide*.

## Amazon SQS updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Amazon SQS since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Amazon SQS [Document history](sqs-release-notes.md) page.


| Change | Description | Date | 
| --- | --- | --- | 
| [SQSUnlockQueuePolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-SQSUnlockQueuePolicy) | Amazon SQS added a new AWS-managed policy called `SQSUnlockQueuePolicy` to unlock a queue and remove a misconfigured queue policy that denies all principals from accessing an Amazon SQS queue. | November 15, 2024 | 
| [AmazonSQSReadOnlyAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonSQSReadOnlyAccess) | Amazon SQS added the [`ListQueueTags`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueueTags.html) action, which retrieves all tags associated with a specified Amazon SQS queue. It allows you to view the key-value pairs that have been assigned to the queue for organizational or metadata purposes. This action is associated with the `ListQueueTags` API operation. | June 20, 2024 | 
| [AmazonSQSReadOnlyAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonSQSReadOnlyAccess) | Amazon SQS added a new action that allows you to list the most recent message movement tasks (up to 10) under a specific source queue. This action is associated with the [`ListMessageMoveTasks`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListMessageMoveTasks.html) API operation. | June 9, 2023 | 