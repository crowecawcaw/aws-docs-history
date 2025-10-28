# Use explicit transaction modes for reading and writing

When using transactions with Neptune and the Bolt driver, it is best to
explicitly set the access mode for both read and write transactions to the right
settings.

## Read-only transactions

For read-only transactions, if you don't pass in the appropriate access mode
configuration when building the session, the default isolation level is used,
which is mutation query isolation. As a result, it's important for read-only
transactions to set the access mode to `read` explicitly.

**Auto-commit read transaction example:**

```
SessionConfig sessionConfig = SessionConfig
  .builder()
  .withFetchSize(1000)
  .withDefaultAccessMode(AccessMode.READ)
  .build();
Session session = driver.session(sessionConfig);
try {
  `(Add your application code here)`
} catch (final Exception e) {
  throw e;
} finally {
  driver.close()
}
```

**Read transaction example:**

```
Driver driver = GraphDatabase.driver(url, auth, config);
SessionConfig sessionConfig = SessionConfig
  .builder()
  .withDefaultAccessMode(AccessMode.READ)
  .build();
driver.session(sessionConfig).readTransaction(
  new TransactionWork<List<String>>() {
    @Override
    public List<String> execute(org.neo4j.driver.Transaction tx) {
      `(Add your application code here)`
    }
  }
);
```

In both cases, [SNAPSHOT
isolation](transactions-isolation-levels.md "transactions-isolation-levels.md") is achieved using [Neptune
read-only transaction semantics](transactions-neptune.md#transactions-neptune-read-only "transactions-neptune.md#transactions-neptune-read-only").

Because read replicas only accept read-only queries, any query submitted
to a read replica runs under `SNAPSHOT` isolation semantics.

There are no dirty reads or non-repeatable reads for read-only transactions.

## Mutation transactions

For mutation queries, there are three different mechanisms to create a
write transaction, each of which is illustrated below:

**Implicit write transaction example:**

```
Driver driver = GraphDatabase.driver(url, auth, config);
SessionConfig sessionConfig = SessionConfig
  .builder()
  .withDefaultAccessMode(AccessMode.WRITE)
  .build();
driver.session(sessionConfig).writeTransaction(
  new TransactionWork<List<String>>() {
    @Override
    public List<String> execute(org.neo4j.driver.Transaction tx) {
      `(Add your application code here)`
    }
  }
);
```

**Auto-commit write transaction example:**

```
SessionConfig sessionConfig = SessionConfig
  .builder()
  .withFetchSize(1000)
  .withDefaultAccessMode(AccessMode.Write)
  .build();
Session session = driver.session(sessionConfig);
try {
  `(Add your application code here)`
} catch (final Exception e) {
    throw e;
} finally {
    driver.close()
}
```

**Explicit write transaction example:**

```
Driver driver = GraphDatabase.driver(url, auth, config);
SessionConfig sessionConfig = SessionConfig
  .builder()
  .withFetchSize(1000)
  .withDefaultAccessMode(AccessMode.WRITE)
  .build();
Transaction beginWriteTransaction = driver.session(sessionConfig).beginTransaction();
  `(Add your application code here)`
beginWriteTransaction.commit();
driver.close();
```

###### Isolation levels for write transactions

- Reads made as part of mutation queries are run under
  `READ COMMITTED` transaction isolation.
- There are no dirty reads for reads made as part of
  mutation queries.
- Records and ranges of records are locked when reading
  in a mutation query.
- When a range of the index has been read by a mutation
  transaction, there is a strong guarantee that this range will not
  be modified by any concurrent transactions until the end of the
  read.

Mutation queries are not thread safe.

For conflicts, see [Conflict Resolution Using Lock-Wait
Timeouts](transactions-neptune.md#transactions-neptune-conflicts "transactions-neptune.md#transactions-neptune-conflicts").

Mutation queries are not automatically retried in
case of failure.
