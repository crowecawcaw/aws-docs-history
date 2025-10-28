# Setting up Amazon SNS

topic encryption with encrypted Amazon SQS queue subscription

You can enable server-side encryption (SSE) for a topic to protect its data. To allow
Amazon SNS to send messages to encrypted Amazon SQS queues, the customer managed key associated with the Amazon SQS
queue must have a policy statement that grants Amazon SNS service-principal access to the AWS KMS
API actions `GenerateDataKey` and `Decrypt`. For more information
about using SSE, see [Securing Amazon SNS data with server-side
encryption](sns-server-side-encryption.md "sns-server-side-encryption.md").

This topic explains how to enable SSE for an Amazon SNS topic with an encrypted Amazon SQS queue
subscription using the AWS Management Console.

## Step 1: Create a custom KMS key

1. Sign in to the [AWS KMS console](https://console.aws.amazon.com/kms/ "https://console.aws.amazon.com/kms/")
   with a user that has at least the
   `AWSKeyManagementServicePowerUser` policy.
2. Choose **Create a key**.
3. To create a symmetric encryption KMS key, for **Key
   type** choose **Symmetric**.

For information about how to create an asymmetric KMS key in the AWS KMS
console, see [Creating asymmetric KMS keys (console)](../../../kms/latest/developerguide/asymm-create-key.md#create-asymmetric-keys-console "../../../kms/latest/developerguide/asymm-create-key.md#create-asymmetric-keys-console"). 4. In **Key usage**, the **Encrypt and
decrypt** option is selected for you.

For information about how to create KMS keys that generate and verify
MAC codes, see [Creating HMAC
KMS keys](../../../kms/latest/developerguide/hmac-create-key.md "../../../kms/latest/developerguide/hmac-create-key.md").

For information about the **Advanced options**, see
[Special-purpose
keys](../../../kms/latest/developerguide/key-types.md "../../../kms/latest/developerguide/key-types.md"). 5. Choose **Next**. 6. Type an alias for the KMS key. The alias name cannot begin with
`aws/`. The `aws/` prefix is
reserved by Amazon Web Services to represent AWS managed keys in your
account.

###### Note

Adding, deleting, or updating an alias can allow or deny permission to
the KMS key. For details, see [ABAC for AWS KMS](../../../kms/latest/developerguide/abac.md "../../../kms/latest/developerguide/abac.md") and
[Using
aliases to control access to KMS keys](../../../kms/latest/developerguide/concepts.md#hmac-key-concept "../../../kms/latest/developerguide/concepts.md#hmac-key-concept").

An alias is a display name that you can use to identify the KMS key. We
recommend that you choose an alias that indicates the type of data you plan
to protect or the application you plan to use with the KMS key.

Aliases are required when you create a KMS key in the AWS Management Console. They
are optional when you use the [CreateKey](../../../kms/latest/APIReference/API_CreateKey.md "../../../kms/latest/APIReference/API_CreateKey.md")
operation. 7. (Optional) Type a description for the KMS key.

You can add a description now or update it any time unless the [key
state](../../../kms/latest/developerguide/key-state.md "../../../kms/latest/developerguide/key-state.md") is `Pending Deletion` or `Pending Replica
 Deletion`. To add, change, or delete the description of an
existing customer managed key, [edit the
description](../../../kms/latest/developerguide/editing-keys.md "../../../kms/latest/developerguide/editing-keys.md") in the AWS Management Console or use the [UpdateKeyDescription](../../../kms/latest/APIReference/API_UpdateKeyDescription.md "../../../kms/latest/APIReference/API_UpdateKeyDescription.md") operation. 8. (Optional) Type a tag key and an optional tag value. To add more than one
tag to the KMS key, choose **Add tag**.

###### Note

Tagging or untagging a KMS key can allow or deny permission to the
KMS key. For details, see [ABAC for AWS KMS](../../../kms/latest/developerguide/abac.md "../../../kms/latest/developerguide/abac.md") and
[Using tags to
control access to KMS keys](../../../kms/latest/developerguide/tag-authorization.md "../../../kms/latest/developerguide/tag-authorization.md").

When you add tags to your AWS resources, AWS
generates a cost allocation report with usage and costs aggregated by tags.
Tags can also be used to control access to a KMS key. For information
about tagging KMS keys, see [Tagging keys](../../../kms/latest/developerguide/tagging-keys.md "../../../kms/latest/developerguide/tagging-keys.md")
and [ABAC for AWS KMS](../../../kms/latest/developerguide/abac.md "../../../kms/latest/developerguide/abac.md"). 9. Choose **Next**. 10. Select the IAM users and roles that can administer the KMS key.

###### Note

This key policy gives the AWS account full control of this
KMS key. It allows account administrators to use IAM policies to
give other principals permission to manage the KMS key. For details,
see [Default key
policy](../../../kms/latest/developerguide/key-policy-default.md "../../../kms/latest/developerguide/key-policy-default.md").

 

IAM best practices discourage the use of IAM users with long-term
credentials. Whenever possible, use IAM roles, which provide temporary
credentials. For details, see [Security best
practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the IAM User Guide. 11. (Optional) To prevent the selected IAM users and roles from deleting
this KMS key, in the **Key deletion** section at the
bottom of the page, clear the **Allow key administrators to delete
this key** check box. 12. Choose **Next**. 13. Select the IAM users and roles that can use the key in [cryptographic operations](../../../kms/latest/developerguide/concepts.md#cryptographic-operations "../../../kms/latest/developerguide/concepts.md#cryptographic-operations"). Choose
**Next**. 14. On the **Review and edit key policy** page, add the
following statement to the key policy, and then choose
**Finish**.

```
{
    "Sid": "Allow Amazon SNS to use this key",
    "Effect": "Allow",
    "Principal": {
        "Service": "sns.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey*"
    ],
    "Resource": "*"
}
```

Your new customer managed key appears in the list of keys.

[Show moreShow less](# "#")

## Step 2: Create an encrypted Amazon SNS topic

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. On the navigation panel, choose **Topics**.
3. Choose **Create topic**.
4. On the **Create new topic** page, for
   **Name**, enter a topic name (for example,
   `MyEncryptedTopic`) and then choose **Create
   topic**.
5. Expand the **Encryption** section and do the following:
   1. Choose **Enable server-side encryption**.
   2. Specify the customer managed key. For more information, see [Key terms](sns-server-side-encryption.md#sse-key-terms "sns-server-side-encryption.md#sse-key-terms").

   For each customer managed key type, the **Description**,
   **Account**, and customer managed key
   **ARN** are displayed.

   ###### Important

   If you aren't the owner of the customer managed key, or if you log in
   with an account that doesn't have the
   `kms:ListAliases` and `kms:DescribeKey`
   permissions, you won't be able to view information about the
   customer managed key on the Amazon SNS console.

   Ask the owner of the customer managed key to grant you these permissions.
   For more information, see the [AWS KMS API
   Permissions: Actions and Resources Reference](../../../kms/latest/developerguide/kms-api-permissions-reference.md "../../../kms/latest/developerguide/kms-api-permissions-reference.md") in the
   _AWS Key Management Service Developer Guide_. 3. For **customer managed key**, choose
   **MyCustomKey**
   [which you created earlier](#create-custom-cmk "#create-custom-cmk") and
   then choose **Enable server-side encryption**.

6. Choose **Save changes**.

SSE is enabled for your topic and the **MyTopic** page is
displayed.

The topic's **Encryption** status, AWS
**Account**, **customer managed key**, customer managed key
**ARN**, and **Description** are displayed
on the **Encryption** tab.

Your new encrypted topic appears in the list of topics.

## Step 3: Create and subscribe encrypted Amazon SQS

queues

1. Sign in to the [Amazon SQS
   console](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. Choose **Create New Queue**.
3. On the **Create New Queue** page, do the following:
   1. Enter a **Queue Name** (for example,
      `MyEncryptedQueue1`).
   2. Choose **Standard Queue**, and then choose
      **Configure Queue**.
   3. Choose **Use SSE**.
   4. For **AWS KMS key**, choose
      **MyCustomKey**
      [which you created earlier](#create-custom-cmk "#create-custom-cmk"), and
      then choose **Create Queue**.

4. Repeat the process to create a second queue (for example, named
   `MyEncryptedQueue2`).

Your new encrypted queues appear in the list of queues. 5. On the Amazon SQS console, choose `MyEncryptedQueue1` and
`MyEncryptedQueue2` and then choose **Queue
Actions**, **Subscribe Queues to SNS
Topic**. 6. In the **Subscribe to a Topic** dialog box, for
**Choose a Topic** select
**MyEncryptedTopic**, and then choose
**Subscribe**.

Your encrypted queues' subscriptions to your encrypted topic are displayed in
the **Topic Subscription Result** dialog box. 7. Choose **OK**.

## Step 4: Publish a message to your encrypted

topic

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. On the navigation panel, choose **Topics**.
3. From the list of topics, choose **MyEncryptedTopic** and then
   choose **Publish message**.
4. On the **Publish a message** page, do the following:
   1. (Optional) In the **Message details** section, enter
      the **Subject** (for example, `Testing message
publishing`).
   2. In the **Message body** section, enter the message
      body (for example, `My message body is encrypted at
rest.`).
   3. Choose **Publish message**.

Your message is published to your subscribed encrypted queues.

## Step 5: Verify message delivery

1. Sign in to the [Amazon SQS
   console](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. From the list of queues, choose **MyEncryptedQueue1** and
   then choose **Send and receive messages**.
3. On the **Send and receive messages in MyEncryptedQueue1**
   page, choose **Poll for messages**.

The message [that you sent
earlier](#publish-to-encrypted-topic "#publish-to-encrypted-topic") is displayed. 4. Choose **More Details** to view your message. 5. When you're finished, choose **Close**. 6. Repeat the process for **MyEncryptedQueue2**.
