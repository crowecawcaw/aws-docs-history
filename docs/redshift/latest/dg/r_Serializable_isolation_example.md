

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Concurrent write examples
<a name="r_Serializable_isolation_example"></a>

The following pseudo-code examples demonstrate how transactions either proceed or wait when they are run concurrently.

## Concurrent write examples with serializable isolation
<a name="r_Serializable_isolation_example-serializable"></a>

### Concurrent COPY operations into the same table with serializable isolation
<a name="r_Serializable_isolation_example-concurrent-copy-operations-into-the-same-table"></a>

Transaction 1 copies rows into the LISTING table: 

```
begin;
copy listing from ...;
end;
```

Transaction 2 starts concurrently in a separate session and attempts to copy more rows into the LISTING table. Transaction 2 must wait until transaction 1 releases the write lock on the LISTING table, then it can proceed. 

```
begin;
[waits]
copy listing from ;
end;
```

The same behavior would occur if one or both transactions contained an INSERT command instead of a COPY command.

### Concurrent DELETE operations from the same table with serializable isolation
<a name="r_Serializable_isolation_example-concurrent-delete-operations-from-the-same-table"></a>

Transaction 1 deletes rows from a table: 

```
begin;
delete from listing where ...;
end;
```

Transaction 2 starts concurrently and attempts to delete rows from the same table. It will succeed because it waits for transaction 1 to complete before attempting to delete rows.

```
begin
[waits]
delete from listing where ;
end;
```

The same behavior would occur if one or both transactions contained an UPDATE command to the same table instead of a DELETE command.

### Concurrent transactions with a mixture of read and write operations with serializable isolation
<a name="r_Serializable_isolation_example-concurrent-transactions"></a>

In this example, transaction 1 deletes rows from the USERS table, reloads the table, runs a COUNT(\*) query, and then ANALYZE, before committing: 

```
begin;
delete one row from USERS table;
copy ;
select count(*) from users;
analyze ;
end;
```

Meanwhile, transaction 2 starts. This transaction attempts to copy additional rows into the USERS table, analyze the table, and then run the same COUNT(\*) query as the first transaction:

```
begin;
[waits]
copy users from ...;
select count(*) from users;
analyze;
end;
```

The second transaction will succeed because it must wait for the first to complete. Its COUNT query will return the count based on the load it has completed.

## Concurrent write examples with snapshot isolation
<a name="r_Serializable_isolation_example-snapshot"></a>

### Concurrent COPY operations into the same table with snapshot isolation
<a name="r_Serializable_isolation_example-concurrent-copy-operations-into-the-same-table-snapshot"></a>

Transaction 1 copies rows into the LISTING table:

```
begin;
copy listing from ...;
end;
```

Transaction 2 starts concurrently in a separate session and attempts to copy more rows into the LISTING table. Transaction 2 can progress simultaneously until either transaction needs to write data to the target table `listing`, at which point they will run sequentially. 

```
begin; 
//When the COPY statement from T1 needs to write data to the table, the COPY statement from T2 waits.
copy listing from ...; 
end;
```

The same behavior would occur if one or both transactions contained an INSERT command instead of a COPY command.

### Concurrent DELETE operations from the same table with snapshot isolation
<a name="r_Serializable_isolation_example-concurrent-delete-operations-from-the-same-table-snapshot"></a>

Concurrent DELETE or UPDATE operations from the same table with snapshot isolation run the same as operations run with serializable isolation.

### Concurrent transactions with a mixture of read and write operations with snapshot isolation
<a name="r_Serializable_isolation_example-concurrent-transactions-snapshot"></a>

Concurrent transactions that are run with mixes of operations with snapshot isolation run the same as transactions with mixes of operations that are run with serializable isolation.