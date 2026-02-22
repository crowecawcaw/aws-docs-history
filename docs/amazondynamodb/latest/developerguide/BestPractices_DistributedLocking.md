# Distributed locking with the DynamoDB Lock

Client

For applications that require traditional lock-acquire-release semantics, the DynamoDB Lock
Client is an open-source library that implements distributed locking using a DynamoDB table as the
lock store. This approach is useful when you need to coordinate access to an external resource
(such as an S3 object or a shared configuration) across multiple application instances.

The lock client is available as an open-source [Java library](https://github.com/awslabs/amazon-dynamodb-lock-client "https://github.com/awslabs/amazon-dynamodb-lock-client").

## How it works

The lock client uses a dedicated DynamoDB table to track locks. Each lock is represented as an
item with the following key attributes:

- A partition key that identifies the resource being locked.
- A lease duration that specifies how long the lock is valid. If the lock holder
  crashes or becomes unresponsive, the lock automatically expires after the lease
  duration.
- A heartbeat that the lock holder sends periodically to extend the lease. This
  prevents the lock from expiring while the holder is still actively processing.

The lock client uses conditional writes to ensure that only one process can acquire a lock
at a time. If a lock is already held, the caller can choose to wait and retry or fail
immediately.

## When to use the lock client

The lock client is a good fit when:

- You need to coordinate access to a shared resource across multiple application
  instances or microservices.
- The critical section is long-running (seconds to minutes) and retrying the
  entire operation on conflict would be expensive.
- You need automatic lock expiry to handle process failures
  gracefully.

Common examples include orchestrating distributed workflows, coordinating cron jobs across
multiple instances, and managing access to shared external resources.

## Tradeoffs

**Additional infrastructure**
Requires a dedicated DynamoDB table for lock management, with additional read and
write capacity for lock operations and heartbeats.

**Clock dependency**
Lock expiry relies on timestamps. Significant clock skew between clients can
cause unexpected behavior, particularly for short lease durations.

**Deadlock risk**
If your application acquires locks on multiple resources, you must acquire them
in a consistent order to avoid deadlocks. The lease duration provides a safety net by
automatically releasing locks from unresponsive holders.

## Implementation

The following example shows how to use the DynamoDB Lock Client to acquire and release a
lock:

```
import java.io.IOException;
import java.util.Optional;
import java.util.concurrent.TimeUnit;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;

final DynamoDbClient dynamoDB = DynamoDbClient.builder()
    .region(Region.US_WEST_2)
    .build();

final AmazonDynamoDBLockClient lockClient = new AmazonDynamoDBLockClient(
    AmazonDynamoDBLockClientOptions.builder(dynamoDB, "Locks")
        .withTimeUnit(TimeUnit.SECONDS)
        .withLeaseDuration(10L)
        .withHeartbeatPeriod(3L)
        .withCreateHeartbeatBackgroundThread(true)
        .build());

// Try to acquire a lock on a resource
final Optional<LockItem> lock =
    lockClient.tryAcquireLock(AcquireLockOptions.builder("my-shared-resource").build());

if (lock.isPresent()) {
    try {
        // Perform operations that require exclusive access
        processSharedResource();
    } finally {
        // Always release the lock when done
        lockClient.releaseLock(lock.get());
    }
} else {
    System.out.println("Failed to acquire lock.");
}

lockClient.close();
```

###### Important

Always release locks in a `finally` block to ensure locks are released even if
your processing logic throws an exception. Unreleased locks block other processes until the
lease expires.

You can also implement a simple locking mechanism without the lock client library by using
conditional writes directly. The following example uses `UpdateItem` with a condition
expression to acquire a lock, and `DeleteItem` to release it:

```
from datetime import datetime, timedelta
from boto3.dynamodb.conditions import Attr

def acquire_lock(table, resource_name, owner_id, ttl_seconds):
    """Attempt to acquire a lock. Returns True if successful."""
    expiry = (datetime.now() + timedelta(seconds=ttl_seconds)).isoformat()
    now = datetime.now().isoformat()
    try:
        table.update_item(
            Key={'LockID': resource_name},
            UpdateExpression='SET #owner = :owner, #expiry = :expiry',
            ConditionExpression=Attr('LockID').not_exists() | Attr('ExpiresAt').lt(now),
            ExpressionAttributeNames={'#owner': 'OwnerID', '#expiry': 'ExpiresAt'},
            ExpressionAttributeValues={':owner': owner_id, ':expiry': expiry}
        )
        return True
    except table.meta.client.exceptions.ConditionalCheckFailedException:
        return False

def release_lock(table, resource_name, owner_id):
    """Release a lock. Only succeeds if the caller is the lock owner."""
    try:
        table.delete_item(
            Key={'LockID': resource_name},
            ConditionExpression=Attr('OwnerID').eq(owner_id)
        )
        return True
    except table.meta.client.exceptions.ConditionalCheckFailedException:
        return False
```

This approach uses a condition expression to ensure that a lock can only be acquired if it
doesn't exist or has expired, and can only be released by the process that acquired it. Consider
enabling [Time to Live (TTL)](TTL.md "TTL.md") on the lock table to automatically clean
up expired lock items.
