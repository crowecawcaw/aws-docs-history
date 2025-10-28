# Read consistency for write forwarding

You can control the degree of read consistency on a DB cluster. The read consistency
level determines how long the DB cluster waits before each read operation to ensure that some
or all changes are replicated from the writer. You can adjust the read consistency level to
make sure that all forwarded write operations from your session are visible in the DB cluster
before any subsequent queries. You can also use this setting to make sure that queries on the
DB cluster always see the most current updates from the writer. This setting also applies to
queries submitted by other sessions or other clusters. To specify this type of behavior for
your application, choose a value for the `aurora_replica_read_consistency` DB
parameter or DB cluster parameter.

###### Important

Always set the `aurora_replica_read_consistency` DB parameter or DB
cluster parameter when you want to forward writes. If you don't, then Aurora
doesn't forward writes. This parameter has an empty value by default, so choose a
specific value when you use this parameter. The `aurora_replica_read_consistency`
parameter only affects DB clusters or instances that have write forwarding enabled.

As you increase the consistency level, your application spends more time waiting for changes to be propagated between DB
instances. You can choose the balance between fast response time and making sure that changes made in other DB instances are
fully available before your queries run.

You can specify the following values for the `aurora_replica_read_consistency` parameter:

- `EVENTUAL` – Results of write operations in the same session aren't visible until the write
  operation is performed on the writer DB instance. The query doesn't wait for the updated results to be available.
  Thus it might retrieve the older data or the updated data, depending on the timing of the statements and the amount of
  replication lag. This is the same consistency as for Aurora MySQL DB clusters that don't use write forwarding.
- `SESSION` – All queries that use write forwarding see the results of all changes made in that
  session. The changes are visible regardless of whether the transaction is committed. If necessary, the query waits for
  the results of forwarded write operations to be replicated.
- `GLOBAL` – A session sees all committed changes across all sessions and instances in the DB cluster.
  Each query might wait for a period that varies depending on the amount of session lag. The query proceeds when the DB
  cluster is up-to-date with all committed data from the writer, as of the time that the query began.
  For information about the configuration parameters involved in write forwarding, see [Configuration parameters for write forwarding](aurora-mysql-write-forwarding.md#aurora-mysql-write-forwarding-params "aurora-mysql-write-forwarding.md#aurora-mysql-write-forwarding-params").

###### Note

You can also use `aurora_replica_read_consistency` as a session variable, for example:

```
mysql> set aurora_replica_read_consistency = 'session';
```

## Examples of using write forwarding

The following examples show the effects of the `aurora_replica_read_consistency` parameter on running
`INSERT` statements followed by `SELECT` statements. The results can differ, depending on the
value of `aurora_replica_read_consistency` and the timing of the statements.

To achieve higher consistency, you might wait briefly before issuing the `SELECT` statement. Or Aurora can
automatically wait until the results finish replicating before proceeding with `SELECT`.

For information on setting DB parameters, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

###### Example with `aurora_replica_read_consistency` set to `EVENTUAL`

Running an `INSERT` statement, immediately followed by a `SELECT` statement, returns a value for
`COUNT(*)` with the number of rows before the new row is inserted. Running the `SELECT` again
a short time later returns the updated row count. The `SELECT` statements don't wait.

````
mysql> select count(*) from t1;
+----------+
| count(*) | +----------+
|        5 | +----------+ 1 row in set (0.00 sec) mysql> insert into t1 values (6); select count(*) from t1; +----------+
| count(*) | +----------+
|        5 | +----------+ 1 row in set (0.00 sec) mysql> select count(*) from t1; +----------+
| count(*) | +----------+
|        6 | +----------+ 1 row in set (0.00 sec) ``` ###### Example with `aurora_replica_read_consistency` set to `SESSION` A `SELECT` statement immediately after an `INSERT` waits until the changes from the `INSERT` statement are visible. Subsequent `SELECT` statements don't wait. ``` mysql> select count(*) from t1; +----------+
| count(*) | +----------+
|        6 | +----------+ 1 row in set (0.01 sec) mysql> insert into t1 values (6); select count(*) from t1; select count(*) from t1; Query OK, 1 row affected (0.08 sec) +----------+
| count(*) | +----------+
|        7 | +----------+ 1 row in set (0.37 sec) +----------+
| count(*) | +----------+
|        7 | +----------+ 1 row in set (0.00 sec) ``` With the read consistency setting still set to `SESSION`, introducing a brief wait after performing an `INSERT` statement makes the updated row count available by the time the next `SELECT` statement runs. ``` mysql> insert into t1 values (6); select sleep(2); select count(*) from t1; Query OK, 1 row affected (0.07 sec) +----------+
| sleep(2) | +----------+
|        0 | +----------+ 1 row in set (2.01 sec) +----------+
| count(*) | +----------+
|        8 | +----------+ 1 row in set (0.00 sec) ``` ###### Example with `aurora_replica_read_consistency` set to `GLOBAL` Each `SELECT` statement waits for all data changes, as of the start time of the statement, to be visible before performing the query. The wait time for each `SELECT` statement varies, depending on the amount of replication lag. ``` mysql> select count(*) from t1; +----------+
| count(*) | +----------+
|        8 | +----------+ 1 row in set (0.75 sec) mysql> select count(*) from t1; +----------+
| count(*) | +----------+
|        8 | +----------+ 1 row in set (0.37 sec) mysql> select count(*) from t1; +----------+
| count(*) | +----------+
|        8 | +----------+ 1 row in set (0.66 sec) ```
````
