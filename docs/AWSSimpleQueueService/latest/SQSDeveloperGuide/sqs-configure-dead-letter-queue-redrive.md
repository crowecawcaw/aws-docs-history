# Learn how to configure a

dead-letter queue redrive in Amazon SQS

Use dead-letter queue redrive to move unconsumed messages from a dead-letter queue to
another destination for processing. By default, dead-letter queue redrive moves messages
from a dead-letter queue to a source queue. However, you can also configure any other queue
as the redrive destination if both queues are the same type. For example, if the dead-letter
queue is a FIFO queue, the redrive destination queue must be a FIFO queue as well.
Additionally, you can configure the redrive velocity to set the rate at which Amazon SQS
moves messages.

###### Note

When a message is moved from a FIFO queue to a FIFO DLQ, the original message's
deduplication ID will be replaced with the original message's ID. This is to make sure
that the DLQ deduplication will not prevent storing of two independent messages that
happen to share a deduplication ID.

Dead-letter queues redrive messages in the order they are received, starting with the
oldest message. However, the destination queue ingests the redriven messages, as well as new
messages from other producers, according to the order in which it receives them. For
example, if a producer is sending messages to a source FIFO queue when simultaneously
receiving redriven messages from a dead letter queue, the redriven messages will interweave
with the new messages from the producer.

###### Note

The redrive task resets the retention period. All redriven messages are considered new
messages with a new `messageID` and `enqueueTime` are assigned to
redriven messages.

## Configuring a dead-letter

queue redrive for an existing standard queue using the Amazon SQS API

You can configure a dead-letter queue redrive using the
`StartMessageMoveTask`, `ListMessageMoveTasks`, and
`CancelMessageMoveTask` API actions:

| API action                                                                                                             | Description                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [`StartMessageMoveTask`](../APIReference/API_StartMessageMoveTask.md "../APIReference/API_StartMessageMoveTask.md")    | Starts an asynchronous task to move messages from a specified<br>source queue to a specified destination queue.            |
| [`ListMessageMoveTasks`](../APIReference/API_ListMessageMoveTasks.md "../APIReference/API_ListMessageMoveTasks.md")    | Gets the most recent message movement tasks (up to 10) under a<br>specific source queue.                                   |
| [`CancelMessageMoveTask`](../APIReference/API_CancelMessageMoveTask.md "../APIReference/API_CancelMessageMoveTask.md") | Cancels a specified message movement task. A message movement can<br>only be cancelled when the current status is RUNNING. |

## Configuring a

dead-letter queue redrive for an existing standard queue using the Amazon SQS
console

1. Open the Amazon SQS console at
   [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. In the navigation pane, choose **Queues**.
3. Choose the name of queue that you have configured as a [dead-letter queue](sqs-configure-dead-letter-queue.md "sqs-configure-dead-letter-queue.md").
4. Choose **Start DLQ redrive**.
5. Under **Redrive configuration**, for **Message
   destination**, do either of the following:
   - To redrive messages to their source queue, choose **Redrive to
     source queue(s)**.
   - To redrive messages to another queue, choose **Redrive to
     custom destination**. Then, enter the Amazon Resource Name
     (ARN) of an existing destination queue.

6. Under **Velocity control settings**, choose one of the
   following:
   - **System optimized** - Redrive dead-letter queue
     messages at the maximum number of messages per second.

   - **Custom max velocity** - Redrive dead-letter queue
     messages with a custom maximum rate of messages per second. The maximum
     allowed rate is 500 messages per second.
     - It is recommended to start with a small value for Custom max
       velocity and verify that the source queue doesn't get
       overwhelmed with messages. From there, gradually ramp-up the
       Custom max velocity value, continuing to monitor the state of
       the source queue.

7. When you finish configuring the dead-letter queue redrive, choose
   **Redrive messages**.

###### Important

Amazon SQS doesn't support filtering and modifying messages while redriving
them from the dead-letter queue.

A dead-letter queue redrive task can run a maximum of 36 hours. Amazon SQS
supports a maximum of 100 active redrive tasks per account. 8. If you want to cancel the message redrive task, on the
**Details** page for your queue, choose **Cancel
DLQ redrive**. When canceling an in progress message redrive, any
messages that have already been successfully moved to their move destination
queue will remain in the destination queue.

## Configuring queue

permissions for dead-letter queue redrive

You can give user access to specific dead-letter queue actions by adding permissions
to your policy. The minimum required permissions for a dead-letter queue redrive are as
follows:

| Minimum Permissions                      | Required API methods                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| To start a message redrive               | • Add the `sqs:StartMessageMoveTask`,<br>`sqs:ReceiveMessage`,<br>`sqs:DeleteMessage`, and<br>`sqs:GetQueueAttributes` of the dead-letter<br>queue. If either the dead-letter queue or the original<br>source queue are encrypted (also known as an [SSE](sqs-server-side-encryption.md "sqs-server-side-encryption.md") queue),<br>`kms:Decrypt` for any KMS key that has been<br>used to encrypt the messages is also required.<br>• Add the `sqs:SendMessage` of the destination<br>queue. If the destination queue is encrypted,<br>`kms:GenerateDataKey` and<br>`kms:Decrypt`are also required. |
| To cancel an in-progress message redrive | • Add the `sqs:CancelMessageMoveTask`,<br>`sqs:ReceiveMessage`,<br>`sqs:DeleteMessage`, and<br>`sqs:GetQueueAttributes` of the dead-letter<br>queue. If the dead-letter queue is encrypted (also known as<br>an [SSE](sqs-server-side-encryption.md "sqs-server-side-encryption.md")<br>queue), `kms:Decrypt` is also required.                                                                                                                                                                                                                                                                      |
| To show a message move status            | • Add the `sqs:ListMessageMoveTasks` and<br>`sqs:GetQueueAttributes` of the dead-letter<br>queue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

###### To configure permissions for an encrypted queue pair (a source queue with a

dead-letter queue)

Use the following steps to configure minimum permissions for a dead-letter queue
(DLQ) redrive:

1.  Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  In the navigation pane, select **Policies**.
3.  Create a new [**policy**](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") and add the following permissions. Attach the
    policy to the IAM [user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md") or [role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")
    that will perform the redrive operation.

        * Permissions for the DLQ (source queue):




        	+ `sqs:StartMessageMoveTask`
        	+ `sqs:CancelMessageMoveTask`
        	+ `sqs:ListMessageMoveTasks`
        	+ `sqs:ReceiveMessage`
        	+ `sqs:DeleteMessage`
        	+ `sqs:GetQueueAttributes`
        	+ `sqs:ListDeadLetterSourceQueues`
        	+ Specify the **Resource ARN** of
        	 the DLQ (source queue) (for example,
        	 "arn:aws:sqs:`<DLQ_region>`:`<DLQ_accountId>`:`<DLQ_name>`").
        * Permissions for destination queue:




        	+ `sqs:SendMessage`
        	+ Specify the `Resource ARN` of the destination queue
        	 (for example,
        	 "arn:aws:sqs:`<DestQueue_region>:<DestQueue_accountId>:<DestQueue_name>`").
        * Permissions for KMS keys:




        	+ `kms:Decrypt` (Needed to decrypt messages in the
        	 DLQ.)
        	+ `kms:GenerateDataKey` (Needed to encrypt messages
        	 in the destination queue.)




        		- `Resource` ARNs:




        			* The ARN of the KMS key used to encrypt
        			 messages in the **DLQ** (source queue) (for example,
        			 "arn:aws:kms:`<region>`:`<accountId>`:key/`<SourceQueueKeyId>`").
        			* The ARN of the KMS key used to encrypt
        			 messages in the **destination
        			 queue** (for example,
        			 "arn:aws:kms:`<region>`:`<accountId>`:key/`<DestinationQueueKeyId>`").

    Your access policy should resemble the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sqs:StartMessageMoveTask",
 "sqs:CancelMessageMoveTask",
 "sqs:ListMessageMoveTasks",
 "sqs:ReceiveMessage",
 "sqs:DeleteMessage",
 "sqs:GetQueueAttributes",
 "sqs:ListDeadLetterSourceQueues"
 ],
 "Resource": "arn:aws:sqs:us-west-1:123456789012:`<DLQ_name>`",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/QueueRole": "source"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "sqs:SendMessage",
 "Resource": "arn:aws:sqs:us-west-1:123456789012:`<DestQueue_name>`",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/QueueRole": "destination"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "arn:aws:kms:us-west-1:123456789012:key/`<SourceQueueKeyId>`",
 "arn:aws:kms:us-west-1:123456789012:key/`<DestQueueKeyId>`"
 ]
 }
 ]
}`

```

###### To configure permissions using a non-encrypted queue pair (a source queue with a

dead-letter queue)

Follow these steps to configure the minimum permissions required for handling a
standard, **unencrypted** dead-letter queue (DLQ).
Required minimum permissions are to _receive_,
_delete_ and _get_ attributes from the dead-letter queue, and _send_ attributes to the source queue.

1.  Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  In the navigation pane, select **Policies**.
3.  Create a new [**policy**](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") and add the following permissions. Attach the
    policy to the IAM [user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md") or [role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")
    that will perform the redrive operation.

        * Permissions for the DLQ (source queue):




        	+ `sqs:StartMessageMoveTask`
        	+ `sqs:CancelMessageMoveTask`
        	+ `sqs:ListMessageMoveTasks`
        	+ `sqs:ReceiveMessage`
        	+ `sqs:DeleteMessage`
        	+ `sqs:ListDeadLetterSourceQueues`
        	+ Specify the **Resource ARN** of
        	 the DLQ (source queue) (for example,
        	 "arn:aws:sqs:`<DLQ_region>`:`<DLQ_accountId>`:`<DLQ_name>`").
        * Permissions for destination queue:




        	+ `sqs:SendMessage`
        	+ Specify the `Resource ARN` of the destination queue
        	 (for example,
        	 "arn:aws:sqs:`<DestQueue_region>:<DestQueue_accountId>:<DestQueue_name>`").

    Your access policy should resemble the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sqs:StartMessageMoveTask",
 "sqs:CancelMessageMoveTask",
 "sqs:ListMessageMoveTasks",
 "sqs:ReceiveMessage",
 "sqs:DeleteMessage",
 "sqs:GetQueueAttributes",
 "sqs:ListDeadLetterSourceQueues"
 ],
 "Resource": "arn:aws:sqs:us-west-1:111122223333:`<DLQ_name>`",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/QueueRole": "source"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "sqs:SendMessage",
 "Resource": "arn:aws:sqs:us-west-1:111122223333:`<DestQueue_name>`",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/QueueRole": "destination"
 }
 }
 }
 ]
}`

```

##

Using dead-letter queue redrive with VPC endpoint access control

When you restrict queue access to specific VPCs using the `aws:sourceVpc` condition,
you need to make an exception for AWS services to enable dead-letter queue (DLQ) redrive functionality.
This is because the Amazon SQS service operates outside your VPC when moving messages.

To allow DLQ redrive operations, add the `aws:CalledViaLast` condition to your queue policy.
This allows Amazon SQS to make API calls on your behalf while maintaining VPC restrictions for direct access.

To allow both VPC-restricted access and DLQ redrive:

1. Use the `aws:CalledViaLast` condition in your queue policy.
2. Apply the policy to both the source queue and the DLQ
3. Maintain VPC restrictions for direct access from other sources

Here is an example policy that implements these requirements:

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "SQSRedriveWithVpcRestriction",
 "Statement": [
 {
 "Sid": "DenyOutsideVPCUnlessAWSService_DestQueue",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "sqs:*",
 "Resource": "arn:aws:sqs:*:111122223333:DestQueue",
 "Condition": {
 "StringNotEquals": {
 "aws:SourceVpc": "vpc-1234567890abcdef0"
 },
 "StringNotEqualsIfExists": {
 "aws:CalledViaLast": "sqs.amazonaws.com"
 }
 }
 },
 {
 "Sid": "DenyOutsideVPCUnlessAWSService_DLQ",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "sqs:*",
 "Resource": "arn:aws:sqs:*:111122223333:Dlq",
 "Condition": {
 "StringNotEquals": {
 "aws:SourceVpc": "vpc-1234567890abcdef0"
 },
 "StringNotEqualsIfExists": {
 "aws:CalledViaLast": "sqs.amazonaws.com"
 }
 }
 }
 ]
}`

```

- Replace the placeholder values with your actual values
- This policy uses a "deny" statement with conditions, which is more secure than using "allow" statements
- The `StringNotEqualsIfExists` operator handles cases
  where the condition key might not be present in the request context.

Alternatively, you can use the `aws:ViaAWSService` condition key to allow service-based access
while maintaining VPC restrictions. This condition key indicates whether the request comes from an AWS service.
Here is an example policy that uses `aws:ViaAWSService` instead of `aws:CalledViaLast`:

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "SQSRedriveWithVpcRestriction",
 "Statement": [
 {
 "Sid": "DenyOutsideVPCUnlessAWSService_DestQueue",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "sqs:*",
 "Resource": "arn:aws:sqs:*:111122223333:DestQueue",
 "Condition": {
 "StringNotEquals": {
 "aws:SourceVpc": "vpc-1234567890abcdef0"
 },
 "BoolIfExists": {
 "aws:ViaAWSService": "false"
 }
 }
 },
 {
 "Sid": "DenyOutsideVPCUnlessAWSService_DLQ",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "sqs:*",
 "Resource": "arn:aws:sqs:*:111122223333:Dlq",
 "Condition": {
 "StringNotEquals": {
 "aws:SourceVpc": "vpc-1234567890abcdef0"
 },
 "BoolIfExists": {
 "aws:ViaAWSService": "false"
 }
 }
 }
 ]
}`

```

The BoolIfExists operator with `aws:ViaAWSService` condition ensures that requests are allowed
when they come from services while maintaining VPC restrictions for direct access.
This can be simpler to understand and maintain,
as it directly checks if the request is made by an AWS service rather than checking which service made the last call.

For more information on condition keys used in IAM and resource policies, see IAM JSON policy elements: Condition.
