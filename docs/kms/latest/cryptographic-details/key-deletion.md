# Deleting keys

Authorized users can use the [`ScheduleKeyDeletion`](../APIReference/API_ScheduleKeyDeletion.md "../APIReference/API_ScheduleKeyDeletion.md") API to schedule the deletion of a KMS key and
all associated HBKs. This is an inherently destructive operation, and you should exercise
caution when deleting keys from AWS KMS. AWS KMS enforces a minimal wait time of seven days when
deleting KMS keys. During the waiting period the key is placed in a disabled state with a
key state of **Pending Deletion**. All calls to use the key for cryptographic
operations will fail. ScheduleKeyDeletion takes the following arguments.

```
{
  "KeyId": "string",
  "PendingWindowInDays": number
}
```

**KeyId**

The unique identifier for the KMS key to delete. To specify this value, use the unique key ID or the key ARN of the KMS key.

**PendingWindowInDays**

(Optional) The waiting period, in number of days. This value is optional. The range is 7-30
days and the default value is 30 days. After the waiting period ends, AWS KMS deletes the
KMS key and all associated HBKs.
