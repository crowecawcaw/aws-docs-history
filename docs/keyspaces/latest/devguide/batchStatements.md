# Use batch statements in Amazon Keyspaces

You can combine multiple `INSERT`, `UPDATE`, and
`DELETE` operations into a `BATCH` statement.
`LOGGED` batches are the default.

```
batch_statement ::=     BEGIN [ UNLOGGED ] BATCH
                        [ USING update_parameter( AND update_parameter)* ]
                        modification_statement ( ';' modification_statement )*
                        APPLY BATCH
modification_statement ::= insert_statement | update_statement | delete_statement
```

When you run a batch statement, the driver combines all statements in the batch into a single batch operation.

To decide which type of batch operation to use, you can consider the following guidelines.

Use logged batches when:

- You need atomic transaction guarantees.
- Slightly higher latencies are an acceptable trade-off.

Use unlogged batches when:

- You need to optimize single-partition operations.
- You want to reduce network overhead.
- You have high-throughput requirements.

For information about batch statement quotas, see [Quotas for Amazon Keyspaces (for Apache Cassandra)](quotas.md "quotas.md").

## Unlogged batches

With **unlogged batches**, Amazon Keyspaces processes multiple operations as a single request without
maintaining a batch log. With an unlogged batch operation, it's possible that some of the actions succeed while others fail. Unlogged batches
are useful when you want to:

- Optimize operations within a single partition.
- Reduce network traffic by grouping related requests.

The syntax for an unlogged batch is similar to that of a logged batch, with the addition of the `UNLOGGED` keyword.

```
BEGIN UNLOGGED BATCH
    INSERT INTO users (id, firstname, lastname) VALUES (1, 'John', 'Doe');
    INSERT INTO users (id, firstname, lastname) VALUES (2, 'Jane', 'Smith');
APPLY BATCH;
```

## Logged batches

A **logged** batch combines multiple write actions into a single atomic operation. When you run a logged batch:

- All actions either succeed together or fail together.
- The operation is synchronous and idempotent.
- You can write to multiple Amazon Keyspaces tables, as long as they are in the same AWS account and AWS Region.

Logged batches may have slightly higher latencies. For high-throughput applications, consider using unlogged batches.

There is no additional cost to use logged batches in Amazon Keyspaces. You pay only for the
writes that are part of your batch operations. Amazon Keyspaces performs two underlying writes
of every row in the batch: one to prepare the row for the batch and one to commit
the batch. When planning capacity for tables that use logged batches, remember that
each row in a batch requires twice the capacity of a standard write operation. For
example, if your application runs one logged batch per second with three 1KB rows,
you need to provision six write capacity units (WCUs) compared to only three WCUs
for individual writes or unlogged batches.

For information about pricing, see [Amazon Keyspaces (for Apache Cassandra) pricing](https://aws.amazon.com/keyspaces/pricing "https://aws.amazon.com/keyspaces/pricing").

### Best practices for batch operations

Consider the following recommended practices when using Amazon Keyspaces batch operations.

- Enable automatic scaling to ensure that you have sufficient throughput capacity for your tables to handle batch
  operations and the additional throughput requirements of logged batches.
- Use individual operations or unlogged batches when operations can run independently without affecting application correctness.
- Design your application to minimize concurrent updates to the same rows, as simultaneous batch operations can conflict and fail.
- For high-throughput bulk data ingestion without atomicity requirements, use individual write operations or unlogged batches.

### Consistency and concurrency

Amazon Keyspaces enforces the following consistency and concurrency rules for logged batches:

- All batch operations use `LOCAL_QUORUM` consistency level.
- Concurrent batches affecting different rows can execute simultaneously.
- Concurrent `INSERT`, `UPDATE`, or `DELETE` operations on
  rows involved in an ongoing batch fail with a conflict.

### Supported operators and conditions

Supported `WHERE` clause operators:

- Equality (=)

Unsupported operators:

- Range operators (>, <, >=, <=)
- `IN` operator
- `LIKE` operator
- `BETWEEN` operator

Not supported in logged batches:

- Multiple statements affecting the same row
- Counter operations
- Range deletes

### Failure conditions of logged batch statements

A logged batch operation may fail in any of the following cases:

- Condition expressions (like `IF NOT EXISTS` or `IF`) evaluate to false.
- One or more operations contain invalid parameters.
- The request conflicts with another batch operation running on the same rows.
- The table lacks sufficient provisioned capacity.
- A row exceeds the maximum size limit.
- The input data format is invalid.

### Batch statements and multi-Region replication

In multi-Region deployments:

- Source Region operations are synchronous and atomic.
- Destination Region operations are asynchronous.
- All batch operations are guaranteed to replicate, but may not maintain isolation during application.

### Monitor batch operations

You can monitor batch operations using Amazon CloudWatch metrics to track performance, errors, and
usage patterns. Amazon Keyspaces provides the following CloudWatch metrics for monitoring batch operations per table:

- `SuccessfulRequestCount` – Track successful batch operations.
- `Latency` – Measure batch operation performance.
- `ConsumedWriteCapacityUnits` – Monitor capacity consumption of batch
  operations.

For more information, see [Amazon Keyspaces metrics](metrics-dimensions.md#keyspaces-metrics-dimensions "metrics-dimensions.md#keyspaces-metrics-dimensions").

In addition to CloudWatch metrics, you can use AWS CloudTrail to log all Amazon Keyspaces API actions. Each API action in the batch is logged in
CloudTrail making it easier to track and audit batch operations in your Amazon Keyspaces tables.

### Batch operation examples

The following is an example of a basic logged batch statement.

```
BEGIN BATCH
    INSERT INTO users (id, firstname, lastname) VALUES (1, 'John', 'Doe');
    INSERT INTO users (id, firstname, lastname) VALUES (2, 'Jane', 'Smith');
APPLY BATCH;
```

This is an example of a batch that includes `INSERT`, `UPDATE`, and `DELETE` statements.

```
BEGIN BATCH
    INSERT INTO users (id, firstname, lastname) VALUES (1, 'John', 'Doe');
    UPDATE users SET firstname = 'Johnny' WHERE id = 2;
    DELETE FROM users WHERE id = 3;
APPLY BATCH;
```

This is an example of a batch using client-side timestamps.

```
BEGIN BATCH
    INSERT INTO users (id, firstname, lastname) VALUES (1, 'John', 'Stiles') USING TIMESTAMP 1669069624;
    INSERT INTO users (id, firstname, lastname) VALUES (2, 'Jane', 'Doe') USING TIMESTAMP 1669069624;
APPLY BATCH;

BEGIN BATCH
    UPDATE users USING TIMESTAMP 1669069624 SET firstname = 'Carlos' WHERE id = 1;
    UPDATE users USING TIMESTAMP 1669069624 SET firstname = 'Diego' WHERE id = 2;
APPLY BATCH;
```

This is an example of a conditional batch.

```
BEGIN BATCH
    INSERT INTO users (id, firstname, lastname) VALUES (1, 'Jane', 'Doe') IF NOT EXISTS;
    INSERT INTO users (id, firstname, lastname) VALUES (2, 'John', 'Doe') IF NOT EXISTS;
APPLY BATCH;


BEGIN BATCH
    UPDATE users SET lastname = 'Stiles' WHERE id = 1 IF lastname = 'Doe';
    UPDATE users SET lastname = 'Stiles' WHERE id = 2 IF lastname = 'Doe';
APPLY BATCH;
```

This is an example of a batch using Time to Live (TTL).

```
BEGIN BATCH
    INSERT INTO users (id, firstname, lastname) VALUES (1, 'John', 'Doe') USING TTL 3600;
    INSERT INTO users (id, firstname, lastname) VALUES (2, 'Jane', 'Smith') USING TTL 7200;
APPLY BATCH;
```

This is an example of a batch statement that updates multiple tables.

```
BEGIN BATCH
    INSERT INTO users (id, firstname) VALUES (1, 'John');
    INSERT INTO user_emails (user_id, email) VALUES (1, 'john@example.com');
APPLY BATCH;
```

This is an example of a batch operation using user-defined types (UDTs). The example
assumes that the UDT `address` exists.

```
BEGIN BATCH
    INSERT INTO users (id, firstname, address)
    VALUES (1, 'John', {street: '123 Main St', city: 'NYC', zip: '10001'});
    INSERT INTO users (id, firstname, address)
    VALUES (2, 'Jane', {street: '456 Oak Ave', city: 'LA', zip: '90210'});
APPLY BATCH;

BEGIN BATCH
    UPDATE users SET address.zip = '10002' WHERE id = 1;
    UPDATE users SET address.city = 'Boston' WHERE id = 2;
APPLY BATCH;
```
