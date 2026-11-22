

# IAM permissions for queues

To work with a queue, an IAM principal needs permission for the queue actions, which use the `kinesis:` prefix. A policy identifies a queue by its ARN, which has the form `arn:aws:kinesis:{{region}}:{{account-id}}:queue/{{resource-id}}`. You can also share queue access with a principal in another AWS account by attaching a resource-based policy to the queue.

## Actions for queues
<a name="queues-iam-actions"></a>

Kinesis Data Streams provides additional actions for working with a queue. You can allow or deny the following actions in a policy, using the `kinesis:` prefix:
+ `kinesis:CreateQueue`
+ `kinesis:UpdateQueue`
+ `kinesis:DeleteQueue`
+ `kinesis:DescribeQueue`
+ `kinesis:ListQueues`
+ `kinesis:ReceiveQueueRecords`
+ `kinesis:AcknowledgeQueueRecords`
+ `kinesis:UpdateQueueRecordsVisibility`
+ `kinesis:ReceiveDeadLetterQueueRecords`
+ `kinesis:AcknowledgeDeadLetterQueueRecords`
+ `kinesis:UpdateDeadLetterQueueRecordsVisibility`
+ `kinesis:RestoreDeadLetterQueueRecords`
+ `kinesis:TagResource`
+ `kinesis:UntagResource`
+ `kinesis:ListTagsForResource`
+ `kinesis:PutResourcePolicy`
+ `kinesis:GetResourcePolicy`
+ `kinesis:DeleteResourcePolicy`
+ `kinesis:AssociateStreamsWithQueue`

**Note**  
If the stream uses server-side encryption, a queue consumer that calls `ReceiveQueueRecords` or `ReceiveDeadLetterQueueRecords` also needs `kms:Decrypt` permission on the stream's AWS KMS key. `CreateQueue` needs no AWS KMS permissions. For more information, see [Data protection in Amazon Kinesis Data Streams](server-side-encryption.md).

The tag and resource-based policy actions are the same actions you use for streams. When you use them with a queue, the resource is the queue ARN.

To create a queue, a principal needs two permissions: `kinesis:AssociateStreamsWithQueue` on the ARN of the stream, and `kinesis:CreateQueue` on `arn:aws:kinesis:{{region}}:{{account-id}}:queue/*`. `CreateQueue` emits both authorizations, so a principal cannot create a queue on a stream it does not have permission for.

`kinesis:AssociateStreamsWithQueue` has no matching API operation. It exists so that the stream can gate queue creation, and Kinesis Data Streams checks this permission against the ARN of the stream you are associating with the queue. `kinesis:CreateQueue` is granted on `queue/*` rather than on a specific queue, because the queue's resource ID does not exist until the queue is created.

A queue ARN carries the resource ID that Kinesis Data Streams generates, not the queue name, so a policy cannot identify a queue by its name.

## Share access with cross-account queue consumers
<a name="resource-based-policy-examples-queues"></a>

You can grant a principal in another AWS account access to consume records through a queue by attaching a resource-based policy. As with sharing a data stream, adding a cross-account principal to a resource-based policy is only part of establishing the trust relationship. When the principal and the resource are in separate AWS accounts, you must also use an identity-based policy to grant the principal access to the resource. For the general resource-based policy workflow, see [Share your data stream with another account](controlling-access.md#sharing-data-streams).

Attach the policy to the queue by calling `PutResourcePolicy` with the queue ARN. A stream's resource-based policy does not cover its queues. In a queue resource-based policy, you can allow the following actions:
+ `kinesis:ReceiveQueueRecords`, `kinesis:AcknowledgeQueueRecords`, and `kinesis:UpdateQueueRecordsVisibility`
+ `kinesis:ReceiveDeadLetterQueueRecords`, `kinesis:AcknowledgeDeadLetterQueueRecords`, `kinesis:UpdateDeadLetterQueueRecordsVisibility`, and `kinesis:RestoreDeadLetterQueueRecords`
+ `kinesis:DescribeQueue`

A queue resource-based policy that includes any other action is rejected. Every other queue operation stays with the account that owns the queue: creating, updating, deleting, listing, and tagging the queue, and managing its resource-based policy. A queue is always in the same account as its stream.

Queue policies follow the same restrictions as data stream and registered consumer policies. For the list, see [Policy limits](controlling-access.md#sharing-data-streams-validating).

If the stream uses server-side encryption, the cross-account principal also needs `kms:Decrypt` on the stream's AWS KMS key, granted in both the key policy and the principal's identity-based policy.

In the following example, account {{444455556666}} owns a stream and its queue, and the role {{QueueConsumer}} in account {{111122223333}} consumes records through the queue. The queue owner attaches the following policy to the queue:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCrossAccountQueueConsumer",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:role/{{QueueConsumer}}"
            },
            "Action": [
                "kinesis:ReceiveQueueRecords",
                "kinesis:AcknowledgeQueueRecords",
                "kinesis:UpdateQueueRecordsVisibility"
            ],
            "Resource": "arn:aws:kinesis:{{us-east-1}}:{{444455556666}}:queue/{{hbr0ptoeikgx8jfu1}}"
        }
    ]
}
```

The {{QueueConsumer}} role also needs an identity-based policy that allows the same actions on the queue:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kinesis:ReceiveQueueRecords",
                "kinesis:AcknowledgeQueueRecords",
                "kinesis:UpdateQueueRecordsVisibility"
            ],
            "Resource": "arn:aws:kinesis:{{us-east-1}}:{{444455556666}}:queue/{{hbr0ptoeikgx8jfu1}}"
        }
    ]
}
```