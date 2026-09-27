

# Permissions by scenario
<a name="eb-custom-bus-permissions"></a>

Each role in a Custom Event Bus deployment needs a small, specific set of grants. This page lists them by scenario so that you can copy the set for the role you are creating. For example, a producer's role needs `events:PutRawEvents` on the bus ARN and, if the bus uses a customer managed key, the key's policy must allow the `events.amazonaws.com` principal.


| Scenario | Who needs the grant | Grants | 
| --- | --- | --- | 
| Publish to a bus | The producer's identity | events:PutEvents or events:PutRawEvents on the bus ARN; events:DescribeEventBus to confirm the bus is ACTIVE | 
| Publish Avro or Protobuf with a schema registry | The role in PutRawEvents RoleArn | Read access to the schema in the registry: the Glue Schema Registry read actions for a Glue registry, or the secret and network access your Confluent registry requires. The role trusts events.amazonaws.com. See [Supported content types: JSON, Avro, Protobuf, and raw bytes](eb-custom-bus-open-formats.md) | 
| Publish to a bus in another account | The producer's identity, and the bus | The publish action in the producer's identity policy, and the same action granted to the producer's account by an AWS RAM share or the bus resource policy | 
| Create and manage subscribers | The subscriber owner's identity | events:CreateSubscriber on the bus and on arn:aws:events:{{region}}:{{account}}:subscriber/{{name}}/\*; iam:PassRole on the delivery role; events:DescribeSubscriber, events:UpdateSubscriber, events:DeleteSubscriber on the subscriber; events:TagResource if the create carries tags | 
| Deliver to a target | The delivery role | Trust for events.amazonaws.com; the target's action; sqs:SendMessage on the dead-letter queue; the target's key actions if the target is encrypted. See [The delivery role](eb-custom-bus-subscribers.md#eb-custom-bus-subscribers-role) | 
| Attach an event source | The event source owner's identity, the dead-letter queue, and the key | events:CreateEventSource on the bus and on the event source; a queue policy allowing events.amazonaws.com sqs:SendMessage on the dead-letter queue; if the bus is encrypted, the key policy allows events.amazonaws.com. See [Event sources for a Custom Event Bus](eb-custom-bus-event-sources.md) | 
| Administer a bus | The bus owner's identity | events:CreateEventBus, events:UpdateEventBus, events:DeleteEventBus, events:PutResourcePolicy, events:GetResourcePolicy, events:DeleteResourcePolicy, events:ListResourcePolicies, events:RevokeResource; ram:CreateResourceShare and related AWS RAM actions to share it | 
| Encrypt a bus with your own key | The key policy | The bus creator's identity needs kms:DescribeKey; that identity, every producer and subscriber owner, and the events.amazonaws.com principal need kms:Decrypt, kms:Encrypt, kms:GenerateDataKeyWithoutPlaintext, kms:ReEncryptFrom, and kms:ReEncryptTo, scoped to the bus with the aws:events:event-busv2:arn encryption context. See [Writing the key policy](eb-custom-bus-encryption.md#eb-custom-bus-encryption-key-policy) | 

For the full action list and condition keys, see [Actions, resources, and condition keys for the Custom Event Bus](eb-custom-bus-access-actions.md). For sharing, see [Sharing a Custom Event Bus with other accounts](eb-custom-bus-sharing.md).