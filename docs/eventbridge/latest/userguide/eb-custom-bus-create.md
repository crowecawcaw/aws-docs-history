

# Creating a bus
<a name="eb-custom-bus-create"></a>

You create a bus with `CreateEventBus`, for example `aws eventsv2 create-event-bus --name orders`. The name is the only required parameter. At creation you can also set a description, the number of days the bus retains events, the AWS KMS key that encrypts them, and tags. The call returns at once with the bus in the `CREATING` state; publish to the bus or create a subscriber on it once `DescribeEventBus` reports `ACTIVE`.

## Creating a bus with the AWS CLI
<a name="eb-custom-bus-create-cli"></a>

The following command creates a bus named `orders` that retains events for 30 days, encrypts them with your AWS KMS key, and carries one tag.

```
aws eventsv2 create-event-bus \
    --name orders \
    --description "Order events from the checkout service" \
    --storage-configuration RetentionPeriodInDays=30 \
    --encryption-configuration KmsKeyIdentifier=arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab \
    --tags team=orders
```

The following table lists what each parameter accepts.


| Parameter | What it accepts | 
| --- | --- | 
| --name | Required. 1 to 256 characters: letters, digits, periods, hyphens, and underscores, starting with a letter or digit. The name must be unique in your account in the Region; creating a second bus with the same name fails with ResourceAlreadyExistsException. | 
| --description | Up to 512 characters. | 
| --storage-configuration | RetentionPeriodInDays, from 1 to 365. Omit it and the bus retains events for 1 day. You can change the period later with UpdateEventBus. See [Choosing the retention period](#eb-custom-bus-create-retention). | 
| --encryption-configuration | KmsKeyIdentifier: a key ID, key ARN, alias name, or alias ARN of a AWS KMS customer managed key. Omit it and EventBridge encrypts events with an AWS owned key. For the key policy the key needs, see [Encrypting events on a Custom Event Bus](eb-custom-bus-encryption.md). | 
| --tags | A map of tag keys to values, for example team=orders,env=prod. For tag-based access control, see [Actions, resources, and condition keys for the Custom Event Bus](eb-custom-bus-access-actions.md). | 

The response returns the bus ARN, which every later call on the bus uses. The ARN ends in an identifier that EventBridge generates, so you cannot construct it from the name.

```
{
    "EventBusArn": "arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef",
    "Name": "orders",
    "Description": "Order events from the checkout service",
    "EncryptionConfiguration": {
        "KmsKeyIdentifier": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    },
    "StorageConfiguration": {
        "RetentionPeriodInDays": 30,
        "RetentionWindowStartTime": "2026-09-21T16:00:00+00:00"
    },
    "State": "CREATING",
    "CreationTime": "2026-09-21T16:00:00+00:00"
}
```

Describe the bus by its ARN until `State` is `ACTIVE`.

```
aws eventsv2 describe-event-bus \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef
```

To create a bus with CloudFormation instead, see [Creating Custom Event Bus resources with CloudFormation](eb-custom-bus-cloudformation.md). For the IAM actions that creating and describing a bus require, see [Actions, resources, and condition keys for the Custom Event Bus](eb-custom-bus-access-actions.md).

## Choosing the retention period
<a name="eb-custom-bus-create-retention"></a>

A bus retains every event that it accepts for the number of days in `StorageConfiguration.RetentionPeriodInDays`, from 1 to 365; omit it and the bus retains events for 1 day. Retention is what lets a subscriber start from a point in the past, pause and resume without losing events, and read events again after a failure. A longer period costs more storage. You can change the period later with `UpdateEventBus`.

```
aws eventsv2 create-event-bus \
    --name orders \
    --storage-configuration RetentionPeriodInDays=30
```

`DescribeEventBus` returns `RetentionWindowStartTime`, the earliest point that a subscriber can read from. To deliver retained events to a subscriber, see [Replaying retained events to a subscriber](eb-custom-bus-replay.md).

## Bus states and what each allows
<a name="eb-custom-bus-lifecycle-states"></a>

Creating, updating, and deleting a bus are asynchronous. Every state other than `ACTIVE` refuses some operations, and the three failed states carry a `StateReason` that tells you why. The following table lists the states a bus moves through and what you can do in each.


| State | How the bus gets there | What you can do | 
| --- | --- | --- | 
| CREATING | CreateEventBus returned and the bus is being set up. | Describe and wait. You cannot publish, update, or delete the bus, or create a subscriber or event source on it. | 
| ACTIVE | Creation or an update finished. | Everything: publish, create subscribers and event sources, update, share, delete. | 
| CREATE\_FAILED | Creation failed, which happens when EventBridge cannot use the AWS KMS key you named. | Delete the bus. Nothing else is accepted. Read StateReason, fix the key or its policy, and create the bus again. | 
| UPDATING | UpdateEventBus is changing the encryption configuration. Other updates do not pass through this state. | Publish and deliver as normal. You cannot update or delete the bus until it returns to ACTIVE. | 
| UPDATE\_FAILED | An encryption update failed, again because EventBridge could not use the key. | The bus keeps running with its previous configuration. Retry the update after you fix the cause, or delete the bus. | 
| DELETING | DeleteEventBus returned. | Wait. You cannot create a subscriber or event source on a bus that is being deleted. | 
| DELETE\_FAILED | Deletion found a subscriber or event source that is not revoked. | Delete the bus again after its subscribers and event sources are deleted or revoked. Nothing else is accepted. | 

## Deleting a bus that has subscribers
<a name="eb-custom-bus-lifecycle-delete"></a>

`DeleteEventBus` succeeds only when every subscriber and event source on the bus is deleted or revoked. A subscriber that another account created counts. You cannot delete that account's subscriber yourself, so either ask the owner to delete it or revoke it with `RevokeResource`; see [Revoking a subscriber or an event source](eb-custom-bus-access-revoke.md). If a subscriber is created between your check and the delete, the bus lands in `DELETE_FAILED`; deal with the new subscriber and delete again.

## Recovering from a failed key change
<a name="eb-custom-bus-lifecycle-key"></a>

Both failed states that a running bus can reach come from the AWS KMS key. When an update to a new key fails, retry `UpdateEventBus` after you fix the key's policy or grant. If the new key itself is unusable, the retry can name a different key, because EventBridge did not adopt the failed key. Do not disable, delete, or remove EventBridge's access to the previous key until `DescribeEventBus` shows the bus `ACTIVE` with the new key; a bus that loses its old key part-way through a change can only be repaired by restoring that key, or deleted. For the key permissions, see [Encrypting events on a Custom Event Bus](eb-custom-bus-encryption.md).