

# Troubleshoot an access denied error in Amazon SQS
<a name="troubleshooting-access-denied"></a>

The following topics cover the most common causes of `AccessDenied` or `AccessDeniedException` errors on Amazon SQS API calls. For more information on how to troubleshoot these errors, see [How do I troubleshoot "AccessDenied" or "AccessDeniedException" errors on Amazon SQS API calls?](https://repost.aws/knowledge-center/sqs-accessdenied-errors) in the *AWS Knowledge Center Guide*.

**Error message examples:**

```
An error occurred (AccessDenied) when calling the SendMessage operation: Access to
        the resource https://sqs.us-east-1.amazonaws.com/ is denied.
```

**- or -**

```
An error occurred (KMS.AccessDeniedException) when calling the SendMessage
        operation: User: arn:aws:iam::xxxxx:user/xxxx is not authorized to perform:
        kms:GenerateDataKey on resource: arn:aws:kms:us-east-1:xxxx:key/xxxx with an explicit
        deny.
```

## Amazon SQS queue policy and IAM policy
<a name="sqs-queue-policy-iam-policy"></a>

To verify if the requester has proper permissions to perform an Amazon SQS operation, do the following:
+ Identify the IAM principal that’s making the Amazon SQS API call. If the IAM principal is from the same account, then either the Amazon SQS queue policy or the AWS Identity and Access Management (IAM) policy must include permissions to explicitly allow access for the action.
+ If the principal is an IAM entity:
  + You can identify your IAM user or role by checking the upper-right corner of the AWS Management Console, or by using the [`aws sts get-caller-identity`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/get-caller-identity.html) command.
  + Check the IAM policies that are related to the IAM user or role. You can use one of the following methods:
    + Test IAM policies with the [IAM Policy Simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html).
    + Review the different [IAM policy types](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policy-types).
  + If needed, edit your [IAM user policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html).
  + Check the queue policy and [edit](sqs-configure-add-permissions.md) if required.
+ If the principal is an AWS service, then the Amazon SQS queue policy must explicitly allow access.
+ If the principal is a cross-account principal, then both the Amazon SQS queue policy and the IAM policy must explicitly allow access.
+ If the policy uses a condition element, then check that the condition restricts access.

**Important**  
An explicit deny in either policy overrides an explicit allow. Here are some basic examples of [Amazon SQS policies](sqs-basic-examples-of-sqs-policies.md).

## AWS Key Management Service permissions
<a name="kms-permissions"></a>

If your Amazon SQS queue has [server-side encryption (SSE)](sqs-server-side-encryption.md) turned on with a customer managed AWS KMS key, then permissions must be granted to both producers and consumers. To confirm if a queue is encrypted, you can use the [`GetQueueAttributes`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html) API `KmsMasterKeyId` attribute, or from the queue console under **Encryption**.
+ Required [permissions for producers](sqs-key-management.md#send-to-encrypted-queue):

  ```
  {
  "Effect": "Allow",
  "Action": [
      "kms:Decrypt",
      "kms:GenerateDataKey"
  ],
  "Resource": "<Key ARN>"
  }
  ```
+ Required [permissions for consumers](sqs-key-management.md#receive-from-encrypted-queue):

  ```
  {
  "Effect": "Allow",
  "Action": [
      "kms:Decrypt"
  ],
  "Resource": "<Key ARN>"
  }
  ```
+ Required permissions for [cross-account access](sqs-key-management.md):

  ```
  {
  "Effect": "Allow",
  "Action": [         
      "kms:DescribeKey",
      "kms:Decrypt",
      "kms:ReEncrypt",
      "kms:GenerateDataKey"
  ],
  "Resource": "<Key ARN>"
  }
  ```

Choose one of the following options to enable encryption for an Amazon SQS queue:
+ [SSE-Amazon SQS](sqs-server-side-encryption.md) (Encryption key created and managed by the Amazon SQS service.)
+ [AWS managed default key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) (alias/aws/sqs)
+ [Customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk)

However, if you are using an AWS-managed [KMS key](sqs-key-management.md), you can't modify the default key policy. Therefore, to provide access to other services and cross-accounts, use customer managed key. Doing this allows you to edit the key policy.

## VPC endpoint policy
<a name="vpc-endpoint-policy"></a>

If you access [Amazon SQS through an Amazon Virtual Private Cloud (Amazon VPC) endpoint](sqs-internetwork-traffic-privacy.md#sqs-vpc-endpoints), the Amazon SQS VPC endpoint policy must allow access. You can create a policy for Amazon VPC endpoints for Amazon SQS, where you can specify the following:

1. The principal that can perform actions.

1. The actions that can be performed.

1. The resources on which actions can be performed.

In the following example, the VPC endpoint policy specifies that the IAM user {{MyUser}} is allowed to send messages to the Amazon SQS queue {{MyQueue}}. Other actions, IAM users, and Amazon SQS resources are denied access through the VPC endpoint.

```
{
   "Statement": [{
      "Action": ["sqs:SendMessage"],
      "Effect": "Allow",
      "Resource": "arn:aws:sqs:us-east-2:123456789012:{{MyQueue}}",
      "Principal": {
        "AWS": "arn:aws:iam:123456789012:user/{{MyUser}}"
      }
   }]
}
```

## Organization service control policy
<a name="organization-control-policy"></a>

If your AWS account belongs to an organization, AWS Organizations policies can block you from accessing your Amazon SQS queues. By default, AWS Organizations policies do not block any requests to Amazon SQS. However, make sure that your AWS Organizations policies haven’t been configured to block access to Amazon SQS queues. For instructions on how to check your AWS Organizations policies, see [Listing all policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_info-operations.html#list-all-pols-in-org) in the *AWS Organizations User Guide*.