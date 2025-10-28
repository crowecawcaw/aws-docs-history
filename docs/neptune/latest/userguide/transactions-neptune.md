# Transaction Isolation Levels in Neptune

Amazon Neptune implements different transaction isolation levels for read-only queries and
for mutation queries. SPARQL and Gremlin queries are classified as read-only or mutation based
on the following criteria:

- In SPARQL, there is a clear distinction between read queries
  (`SELECT`, `ASK`, `CONSTRUCT`, and `DESCRIBE`
  as defined in the [SPARQL 1.1 Query
  Language](https://www.w3.org/TR/sparql11-query/ "https://www.w3.org/TR/sparql11-query/") specification), and mutation queries (`INSERT` and
  `DELETE` as defined in the [SPARQL
  1.1 Update](https://www.w3.org/TR/sparql11-update/ "https://www.w3.org/TR/sparql11-update/") specification).

Note that Neptune treats multiple mutation queries submitted together (for example,
in a `POST` message, separated by semicolons) as a single transaction.
They are guaranteed either to succeed or fail as an atomic unit, and in the case of failure,
partial changes are rolled back.

- However, in Gremlin, Neptune classifies a query as a read-only query or a mutation query
  based on whether it contains any query-path steps such as `addE()`, `addV()`,
  `property()`, or `drop()` that manipulates data. If the query contains
  any such path step, it is classified and executed as a mutation query.
  It is also possible to use standing sessions in Gremlin. For more information, see [Gremlin script-based sessions](access-graph-gremlin-sessions.md "access-graph-gremlin-sessions.md").
  In these sessions, all queries, including read-only queries, are executed under the same
  isolation as mutation queries on the writer endpoint.

Using bolt read-write sessions in openCypher, all queries including read-only queries
are executed under the same isolation as mutation queries, on the writer endpoint.

###### Topics

- [Read-only query isolation in Neptune](#transactions-neptune-read-only "#transactions-neptune-read-only")
- [Mutation query isolation in Neptune](#transactions-neptune-mutation "#transactions-neptune-mutation")
- [Conflict Resolution Using Lock-Wait
  Timeouts](#transactions-neptune-conflicts "#transactions-neptune-conflicts")
- [Range locks and false conflicts](#transactions-neptune-false-conflicts "#transactions-neptune-false-conflicts")

## Read-only query isolation in Neptune

Neptune evaluates read-only queries under snapshot isolation semantics. This means that
a read-only query logically operates on a consistent snapshot of the database taken when query
evaluation begins. Neptune can then guarantee that none of the following phenomena will
happen:

- `Dirty reads` – Read-only queries in Neptune will never see
  uncommitted data from a concurrent transaction.
- `Non-repeatable reads` – A read-only transaction that reads the
  same data more than once will always get back the same values.
- `Phantom reads` – A read-only transaction will never read data that
  was added after the transaction began.

Because snapshot isolation is achieved using multiversion concurrency control (MVCC),
read-only queries have no need to lock data and therefore do not block mutation
queries.

Read replicas only accept read-only queries, so all queries against read replicas
execute under `SNAPSHOT` isolation semantics.

The only additional consideration when querying a read replica is that there can be a
small replication lag between the writer and read replicas. This means that an update made on
the writer might take a short time to be propagated to the read replica you are reading from.
The actual replication time depends on the write-load against the primary instance. Neptune
architecture supports low-latency replication and the replication lag is instrumented in an
Amazon CloudWatch metric.

Still, because of the `SNAPSHOT` isolation level, read queries always
see a consistent state of the database, even if it is not the most recent one.

In cases where you require a strong guarantee that a query observes the result of
a previous update, send the query to the writer endpoint itself rather than to a read
replica.

## Mutation query isolation in Neptune

Reads made as part of mutation queries are executed under `READ COMMITTED`
transaction isolation, which rules out the possibility of dirty reads. Going beyond the
usual guarantees provided for `READ COMMITTED` transaction isolation,
Neptune provides the strong guarantee that neither `NON-REPEATABLE` nor
`PHANTOM` reads can happen.

These strong guarantees are achieved by locking records and ranges of records when reading
data. This prevents concurrent transactions from making insertions or deletions in index
ranges after they have been read, thus guaranteeing repeatable reads.

###### Note

However, a concurrent mutation transaction `Tx2` could begin after the
start of mutation transaction `Tx1`, and could commit a change before
`Tx1` had locked data to read it. In that case, `Tx1` would
see `Tx2`'s change just as if `Tx2` had completed before
`Tx1` started. Because this only applies to committed changes, a `dirty
 read` could never occur.

To understand the locking mechanism that Neptune uses for mutation queries, it helps
first to understand the details of the Neptune [Graph Data Model](feature-overview-data-model.md "feature-overview-data-model.md") and [Indexing Strategy](feature-overview-storage-indexing.md "feature-overview-storage-indexing.md"). Neptune manages data using
three indexes, namely `SPOG`, `POGS`, and `GPSO`.

To achieve repeatable reads for the `READ COMMITTED` transaction level,
Neptune takes range locks in the index that is being used. For example, if a mutation query
reads all properties and outgoing edges of a vertex named `person1`, the node would
lock the entire range defined by the prefix `S=person1` in the `SPOG`
index before reading the data.

The same mechanism applies when using other indexes. For example, when a mutation
transaction looks up all the source-target vertex pairs for a given edge label using the
`POGS` index, the range for the edge label in the `P` position would
be locked. Any concurrent transaction, regardless of whether it was a read-only or mutation
query, could still perform reads within the locked range. However, any mutation involving
insertion or deletion of new records in the locked prefix range would require an exclusive
lock and would be prevented.

In other words, when a range of the index has been read by a mutation transaction, there
is a strong guarantee that this range will not be modified by any concurrent transactions
until the end of the reading transaction. This guarantees that no `non-repeatable
 reads` will occur.

## Conflict Resolution Using Lock-Wait

Timeouts

If a second transaction tries to modify a record in a range that a first transaction has
locked, Neptune detects the conflict immediately and blocks the second transaction.

If no dependency deadlock is detected, Neptune automatically applies a lock-wait timeout
mechanism, in which the blocked transaction waits for up to 60 seconds for the transaction
that holds the lock to finish and release the lock.

- If the lock-wait timeout expires before the lock is released,
  the blocked transaction is rolled back.
- If the lock is released within the lock-wait timeout, the second transaction is unblocked and
  can finish successfully without needing to retry.

However, if Neptune detects a dependency deadlock between the two
transactions, automatic reconciliation of the conflict is not possible.
In this case, Neptune immediately cancels and rolls back one of the two
transactions without initiating a lock-wait timeout. Neptune makes a
best effort to roll back the transaction that has the fewest records
inserted or deleted.

## Range locks and false conflicts

Neptune takes range locks using gap locks. A gap lock is a lock on a gap between
index records, or a lock on the gap before the first or after the last index record.

Neptune uses a so-called dictionary table to associate numeric ID values with
specific string literals. Here is a sample state of such a Neptune dictionary:
table:

| String        | ID     |
| ------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --- | ---------- | ---------- | ---------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| type          | 1      |
| default_graph | 2      |
| person_3      | 3      |
| person_1      | 5      |
| knows         | 6      |
| person_2      | 7      |
| age           | 8      |
| edge_1        | 9      |
| lives_in      | 10     |
| New York      | 11     |
| Person        | 12     |
| Place         | 13     |
| edge_2        | 14     | The strings above belong to a property-graph model, but the concepts apply equally to all RDF graph models as well. The corresponding state of the SPOG (Subject-Predicate-Object_Graph) index is shown below on the left. On the right, the corresponding strings are shown, to help understand what the index data means. |
| S (ID)        | P (ID) | O (ID)                                                                                                                                                                                                                                                                                                                      | G (ID) |     | S (string) | P (string) | O (string) | G (string)    |
| ---           | ---    | ---                                                                                                                                                                                                                                                                                                                         | ---    | --- | ---        | ---        | ---        | ---           |
| 3             | 1      | 12                                                                                                                                                                                                                                                                                                                          | 2      |     | person_3   | type       | Person     | default_graph |
| 5             | 1      | 12                                                                                                                                                                                                                                                                                                                          | 2      |     | person_1   | type       | Person     | default_graph |
| 5             | 6      | 3                                                                                                                                                                                                                                                                                                                           | 9      |     | person_1   | knows      | person_3   | edge_1        |
| 5             | 8      | 40                                                                                                                                                                                                                                                                                                                          | 2      |     | person_1   | age        | 40         | default_graph |
| 5             | 10     | 11                                                                                                                                                                                                                                                                                                                          | 14     |     | person_1   | lives_in   | New York   | edge_2        |
| 7             | 1      | 12                                                                                                                                                                                                                                                                                                                          | 2      |     | person_2   | type       | Person     | default_graph |
| 11            | 1      | 13                                                                                                                                                                                                                                                                                                                          | 2      |     | New York   | type       | Place      | default_graph | Now, if a mutation query reads all properties and outgoing edges of a vertex named `person_1`, the node would lock the entire range defined by the prefix `S=person_1` in the SPOG index before reading the data. The range lock would place gap locks on all matching records and the first record that is not a match. Matching records would be locked, and non-matching records would not be locked. Neptune would place the gap-locks as follows: <br>• `5 1 12 2` _(gap 1)_ <br>• `5 6 3 9` _(gap 2)_ <br>• `5 8 40 2` _(gap 3)_ <br>• `5 10 11 14` _(gap 4)_ <br>• `7 1 12 2` _(gap 5)_ This locks the following records: <br>• `5 1 12 2` <br>• `5 6 3 9` <br>• `5 8 40 2` <br>• `5 10 11 14` In this state, the following operations are legitimately blocked: <br>• Insertion of a new property or edge for `S=person_1`. A new property different from `type` or a new edge would have to go in either gap 2, gap 3, gap 4, or gap 5, all of which are locked. <br>• Deletion of any of the existing records. At the same time, a few concurrent operations would be blocked falsely (generating false conflicts): <br>• Any property or edge insertions for `S=person_3` are blocked because they would have to go in gap 1. <br>• Any new vertex insertion which gets assigned an ID between 3 and 5 would be blocked because it would have to go in gap 1. <br>• Any new vertex insertion which gets assigned an ID between 5 and 7 would be blocked because it would have to go in gap 5. Gap locks are not precise enough to lock the gap for one specific predicate (for example, to lock gap5 for predicate `S=5`). The range locks are only placed in the index where the read happens. In the case above, records are locked only in the SPOG index, not in POGS or GPSO. Reads for a query may be performed across all indexes depending on the access patterns, which can be listed using the `explain` APIs (for [Sparql](sparql-explain-examples.md "sparql-explain-examples.md") and for [Gremlin](gremlin-explain.md "gremlin-explain.md")). ###### Note Gap locks can also be taken for safe concurrent updates on underlying indexes, which can also lead to false conflicts. These gap locks are placed independent of isolation level or read operations performed by the transaction. False conflicts can happen not only when _concurrent_ transactions collide because of gap locks, but also in some cases when a transaction is being retried after any sort of failure. If the roll-back that was triggered by the failure is still in progress and the locks previously taken for the transaction have not yet been fully released, the retry will encounter a false conflict and fail. Under a high load, you might typically find that 3-4% of write queries fail because of false conflicts. For an external client, such false conflicts are hard to predict, and should be handled using [retries](transactions-exceptions.md "transactions-exceptions.md"). |
