# Best practices for handling concurrent updates in DynamoDB

In distributed systems, multiple processes or users may attempt to modify the same data at
the same time. Without concurrency control, these concurrent writes can lead to lost updates,
inconsistent data, or race conditions. DynamoDB provides several mechanisms to help you manage
concurrent access and maintain data integrity.

###### Note

Individual write operations such as `UpdateItem` are atomic and always operate on
the most recent version of the item, regardless of concurrency. Locking strategies are needed
when your application must read an item and then write it back based on the read value (a
read-modify-write cycle), because another process could modify the item between the read and the
write.

There are two primary strategies for handling concurrent updates:

- **Optimistic locking** – Assumes conflicts are rare.
  It allows concurrent access and detects conflicts at write time using conditional writes. If a
  conflict is detected, the write fails and the application can retry.
- **Pessimistic locking** – Assumes conflicts are likely.
  It prevents concurrent access by acquiring exclusive access to a resource before modifying it.
  Other processes must wait until the lock is released.
  The following table summarizes the approaches available in DynamoDB:

| Approach                           | Mechanism                                     | Best for                                         |
| ---------------------------------- | --------------------------------------------- | ------------------------------------------------ |
| Optimistic locking                 | Version attribute + conditional writes        | Low contention, inexpensive retries              |
| Pessimistic locking (transactions) | `TransactWriteItems`                          | Multi-item atomicity, moderate contention        |
| Pessimistic locking (lock client)  | Dedicated lock table with lease and heartbeat | Long-running workflows, distributed coordination |

## Choosing a concurrency control strategy

Use the following guidelines to choose the right approach for your workload:

**Use optimistic locking** when:

- Conflicts are infrequent.
- Retrying a failed write is inexpensive.
- You are updating a single item at a time.

**Use transactions** when:

- You need to update multiple items atomically.
- You require all-or-nothing semantics across items or tables.
- You need to combine condition checks with writes in a single
  operation.

**Use the lock client** when:

- You need to coordinate access to external resources across distributed
  processes.
- The critical section is long-running and retrying on conflict is
  expensive.
- You need automatic lock expiry to handle process failures.

###### Note

If you use [DynamoDB global tables](GlobalTables.md "GlobalTables.md"), be aware that
global tables use a "last writer wins" reconciliation strategy for concurrent updates. Optimistic
locking with version numbers does not work as expected across Regions because a write in one
Region may overwrite a concurrent write in another Region without a version check. Design your
application to handle conflicts at the application level when using global tables.
