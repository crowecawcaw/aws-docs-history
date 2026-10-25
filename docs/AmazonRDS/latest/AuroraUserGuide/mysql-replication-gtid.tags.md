

# Using GTID tags with an Aurora MySQL DB cluster
<a name="mysql-replication-gtid.tags"></a>

Starting with Aurora MySQL version 8.4.10, you can add a tag to the global transaction identifiers (GTIDs) of your transactions. Tags make it easier to identify and track groups of related transactions, such as the transactions from a specific application or batch job. A tagged GTID has the format `{{source_id}}:{{tag}}:{{transaction_id}}`, for example `ed102faf-eb00-11eb-8f20-0c5415bfaa1d:tag1:117`. Tagged and untagged GTIDs can exist together in the same DB cluster.

A tag name can be up to 32 characters long. It must start with a letter or underscore, and it can contain only letters, digits, and underscores. Tag names aren't case-sensitive, so `TAG1` and `tag1` are the same tag.

Before you start, enable binary logging, set `gtid_mode` and `enforce_gtid_consistency` to `ON` in your DB cluster parameter group. Your database user also needs the `TRANSACTION_GTID_TAG` privilege. To grant it, connect as your administrative user and run the following:

```
GRANT TRANSACTION_GTID_TAG ON *.* TO '{{user}}'@'{{host}}';
```

To tag transactions, set `gtid_next` to `AUTOMATIC:` followed by your tag name. For example, the following tags a transaction with `tag1` and then turns off tagging:

```
SET @@SESSION.gtid_next = 'AUTOMATIC:tag1';

START TRANSACTION;
-- your statements
COMMIT;

SET @@SESSION.gtid_next = 'AUTOMATIC';
```

The tag applies to every transaction in the session until you set `gtid_next` back to `AUTOMATIC` or to a different tag. If you use a connection pool, reset `gtid_next` to `AUTOMATIC` before you return the connection to the pool. You can't change `gtid_next` while a transaction is open.

To view your tagged transactions, query `gtid_executed`:

```
SELECT @@GLOBAL.gtid_executed;
```

Tagged transactions appear as a separate range after the untagged range, for example `3E11FA47-71CA-11E1-9E33-C80AA9429562:1-20:tag1:1-5`. Each tag has its own sequence of transaction numbers.