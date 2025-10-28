# Configuring server-side encryption for a queue

using the Amazon SQS console

To protect the data in a queue’s messages, Amazon SQS has server-side encryption (SSE) enabled
by default for all newly created queues. Amazon SQS integrates with the Amazon Web Services Key Management
Service (Amazon Web Services KMS) to manage [KMS keys](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys") for server-side encryption (SSE). For information about using SSE,
see [Encryption at rest in Amazon SQS](sqs-server-side-encryption.md "sqs-server-side-encryption.md").

The KMS key that you assign to your queue must have a key policy that includes
permissions for all principals that are authorized to use the queue. For information, see
[Key Management](sqs-key-management.md "sqs-key-management.md").

If you aren't the owner of the KMS key, or if you log in with an account that doesn't
have `kms:ListAliases` and `kms:DescribeKey` permissions, you won't be
able to view information about the KMS key on the Amazon SQS console. Ask the owner of the
KMS key to grant you these permissions. For more information, see [Key Management](sqs-key-management.md "sqs-key-management.md").

When you [create](creating-sqs-standard-queues.md#step-create-standard-queue "creating-sqs-standard-queues.md#step-create-standard-queue") or [edit](sqs-configure-edit-queue.md "sqs-configure-edit-queue.md") a queue, you can configure
SSE-KMS.

###### To configure SSE-KMS for an existing queue (console)

1. Open the Amazon SQS console at
   [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. In the navigation pane, choose **Queues**.
3. Choose a queue, and then choose **Edit**.
4. Expand **Encryption**.
5. For **Server-side encryption**, choose **Enabled**
   (default).

###### Note

With SSE enabled, anonymous `SendMessage` and
`ReceiveMessage` requests to the encrypted queue will be
rejected. Amazon SQS security best practises recommend against using anonymous
requests. If you wish to send anonymous requests to an Amazon SQS queue, make sure to
disable SSE. 6. Select **AWS Key Management Service key (SSE-KMS)**.

The console displays the **Description**, the
**Account**, and the **KMS key ARN** of the
KMS key. 7. Specify the KMS key ID for the queue. For more information, see [Key terms](sqs-server-side-encryption.md#sqs-sse-key-terms "sqs-server-side-encryption.md#sqs-sse-key-terms").

    1. Choose the **Choose a KMS key alias** option.
    2. The default key is the Amazon Web Services managed KMS key for Amazon SQS. To use this
     key, choose it from the **KMS key** list.
    3. To use a custom KMS key from your Amazon Web Services account, choose it from the
     **KMS key** list. For instructions on creating custom
     KMS keys, see [Creating
     Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the *Amazon Web Services Key Management Service Developer
     Guide*.
    4. To use a custom KMS key that is not in the list, or a custom KMS key
     from another Amazon Web Services account, choose **Enter the KMS key
     alias** and enter the KMS key Amazon Resource Name
     (ARN).

8. (Optional) For **Data key reuse period**, specify a value between
   1 minute and 24 hours. The default is 5 minutes. For more information, see [Understanding the
   data key reuse period](sqs-key-management.md#sqs-how-does-the-data-key-reuse-period-work "sqs-key-management.md#sqs-how-does-the-data-key-reuse-period-work").
9. When you finish configuring SSE-KMS, choose **Save**.
