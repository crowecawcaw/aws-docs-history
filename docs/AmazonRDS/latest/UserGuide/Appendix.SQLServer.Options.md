# Support for Microsoft Distributed Transaction Coordinator in RDS for SQL Server

A _distributed transaction_ is a database transaction in
which two or more network hosts are involved. RDS for SQL Server supports distributed
transactions among hosts, where a single host can be one of the following:

- RDS for SQL Server DB instance
- On-premises SQL Server host
- Amazon EC2 host with SQL Server installed
- Any other EC2 host or RDS DB instance with a database engine that supports distributed
  transactions
  In RDS, starting with SQL Server 2012 (version 11.00.5058.0.v1 and later), all editions of RDS for SQL Server support distributed transactions.
  The support is provided using Microsoft Distributed Transaction Coordinator (MSDTC). For in-depth information about MSDTC, see
  [Distributed Transaction Coordinator](<https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms684146(v=vs.85)> "https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms684146(v=vs.85)") in the Microsoft documentation.

###### Contents

- [Limitations](Appendix.SQLServer.Options.md#Appendix.SQLServer.Options.MSDTC.Limitations "Appendix.SQLServer.Options.md#Appendix.SQLServer.Options.MSDTC.Limitations")
- [Enabling MSDTC](Appendix.SQLServer.Options.MSDTC.md "Appendix.SQLServer.Options.MSDTC.md")
  - [Creating the option group for MSDTC](Appendix.SQLServer.Options.MSDTC.md#Appendix.SQLServer.Options.MSDTC.OptionGroup "Appendix.SQLServer.Options.MSDTC.md#Appendix.SQLServer.Options.MSDTC.OptionGroup")
  - [Adding the MSDTC option to the option group](Appendix.SQLServer.Options.MSDTC.md#Appendix.SQLServer.Options.MSDTC.Add "Appendix.SQLServer.Options.MSDTC.md#Appendix.SQLServer.Options.MSDTC.Add")
  - [Creating the parameter group for MSDTC](Appendix.SQLServer.Options.MSDTC.md#MSDTC.CreateParamGroup "Appendix.SQLServer.Options.MSDTC.md#MSDTC.CreateParamGroup")
  - [Modifying the parameter for MSDTC](Appendix.SQLServer.Options.MSDTC.md#ModifyParam.MSDTC "Appendix.SQLServer.Options.MSDTC.md#ModifyParam.MSDTC")
  - [Associating the option group and parameter group with the DB instance](Appendix.SQLServer.Options.MSDTC.md#MSDTC.Apply "Appendix.SQLServer.Options.MSDTC.md#MSDTC.Apply")
  - [Modifying the MSDTC option](Appendix.SQLServer.Options.MSDTC.md#Appendix.SQLServer.Options.MSDTC.Modify "Appendix.SQLServer.Options.MSDTC.md#Appendix.SQLServer.Options.MSDTC.Modify")

- [Using transactions](Appendix.SQLServer.Options.md#Appendix.SQLServer.Options.MSDTC.Using "Appendix.SQLServer.Options.md#Appendix.SQLServer.Options.MSDTC.Using")
  - [Using distributed transactions](Appendix.SQLServer.Options.md#Appendix.SQLServer.Options.MSDTC.UsingXA "Appendix.SQLServer.Options.md#Appendix.SQLServer.Options.MSDTC.UsingXA")
  - [Using XA transactions](Appendix.SQLServer.Options.md#MSDTC.XA "Appendix.SQLServer.Options.md#MSDTC.XA")
  - [Using transaction tracing](Appendix.SQLServer.Options.md#MSDTC.Tracing "Appendix.SQLServer.Options.md#MSDTC.Tracing")

- [Disabling MSDTC](Appendix.SQLServer.Options.MSDTC.md "Appendix.SQLServer.Options.MSDTC.md")
- [Troubleshooting MSDTC for RDS for SQL Server](Appendix.SQLServer.Options.MSDTC.md "Appendix.SQLServer.Options.MSDTC.md")

## Limitations

The following limitations apply to using MSDTC on RDS for SQL Server:

- MSDTC isn't supported on instances using SQL Server Database Mirroring. For more
  information, see [Transactions - availability groups and database
  mirroring](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/transactions-always-on-availability-and-database-mirroring?view=sql-server-ver15#non-support-for-distributed-transactions "https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/transactions-always-on-availability-and-database-mirroring?view=sql-server-ver15#non-support-for-distributed-transactions").
- The `in-doubt xact resolution` parameter must be set to 1 or 2. For more information, see [Modifying the parameter for MSDTC](Appendix.SQLServer.Options.MSDTC.md#ModifyParam.MSDTC "Appendix.SQLServer.Options.MSDTC.md#ModifyParam.MSDTC").
- MSDTC requires all hosts participating in distributed transactions to be resolvable using their host names. RDS automatically
  maintains this functionality for domain-joined instances. However, for standalone instances make sure to configure the
  DNS server manually.
- Java Database Connectivity (JDBC) XA transactions are supported for SQL Server 2017 version 14.00.3223.3 and
  higher, and SQL Server 2019.
- Distributed transactions that depend on client dynamic link libraries (DLLs) on RDS
  instances aren't supported.
- Using custom XA dynamic link libraries isn't supported.

## Using transactions

### Using distributed transactions

In Amazon RDS for SQL Server, you run distributed transactions in the same way as distributed
transactions running on-premises:

- Using .NET framework `System.Transactions` promotable transactions, which
  optimizes distributed transactions by deferring their creation until
  they're needed.

In this case, promotion is automatic and doesn't require you to make any
intervention. If there's only one resource manager within the
transaction, no promotion is performed. For more information about implicit
transaction scopes, see [Implementing an implicit transaction using transaction scope](https://docs.microsoft.com/en-us/dotnet/framework/data/transactions/implementing-an-implicit-transaction-using-transaction-scope "https://docs.microsoft.com/en-us/dotnet/framework/data/transactions/implementing-an-implicit-transaction-using-transaction-scope") in
the Microsoft documentation.

Promotable transactions are supported with these .NET implementations:

    + Starting with ADO.NET 2.0, `System.Data.SqlClient` supports promotable
     transactions with SQL Server. For more information, see [System.Transactions integration with SQL Server](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/system-transactions-integration-with-sql-server "https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/system-transactions-integration-with-sql-server") in the
     Microsoft documentation.
    + ODP.NET supports `System.Transactions`. A local transaction is created for
     the first connection opened in the `TransactionsScope`
     scope to Oracle Database 11g release 1 (version 11.1) and later.
     When a second connection is opened, this transaction is
     automatically promoted to a distributed transaction. For more
     information about distributed transaction support in ODP.NET, see
     [Microsoft Distributed Transaction Coordinator
     integration](https://docs.oracle.com/en/database/oracle/oracle-data-access-components/18.3/ntmts/using-mts-with-oracledb.html "https://docs.oracle.com/en/database/oracle/oracle-data-access-components/18.3/ntmts/using-mts-with-oracledb.html") in the Microsoft documentation.

- Using the `BEGIN DISTRIBUTED TRANSACTION` statement. For more information, see
  [BEGIN DISTRIBUTED TRANSACTION (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/begin-distributed-transaction-transact-sql "https://docs.microsoft.com/en-us/sql/t-sql/language-elements/begin-distributed-transaction-transact-sql") in the Microsoft
  documentation.

### Using XA transactions

Starting from RDS for SQL Server 2017 version14.00.3223.3, you can control distributed transactions using JDBC. When you set the
`Enable XA` option setting to `true` in the `MSDTC` option, RDS automatically enables JDBC
transactions and grants the `SqlJDBCXAUser` role to the `guest` user. This allows executing distributed
transactions through JDBC. For more information, including a code example, see [Understanding XA transactions](https://docs.microsoft.com/en-us/sql/connect/jdbc/understanding-xa-transactions "https://docs.microsoft.com/en-us/sql/connect/jdbc/understanding-xa-transactions")
in the Microsoft documentation.

### Using transaction tracing

RDS supports controlling MSDTC transaction traces and downloading them from the RDS DB
instance for troubleshooting. You can control transaction tracing sessions by
running the following RDS stored procedure.

```
exec msdb.dbo.rds_msdtc_transaction_tracing '`trace_action`',
[@traceall='`0|1`'],
[@traceaborted='`0|1`'],
[@tracelong='`0|1`'];
```

The following parameter is required:

- `trace_action` – The tracing action. It can be
  `START`, `STOP`, or `STATUS`.

The following parameters are optional:

- `@traceall` – Set to 1 to trace all distributed transactions. The
  default is 0.
- `@traceaborted` – Set to 1 to trace canceled distributed transactions.
  The default is 0.
- `@tracelong` – Set to 1 to trace long-running distributed transactions.
  The default is 0.

###### Example of START tracing action

To start a new transaction tracing session, run the following example statement.

```
exec msdb.dbo.rds_msdtc_transaction_tracing 'START',
@traceall='`0`',
@traceaborted='`1`',
@tracelong='`1`';
```

###### Note

Only one transaction tracing session can be active at one time. If a new tracing session
`START` command is issued while a tracing session is active,
an error is returned and the active tracing session remains
unchanged.

###### Example of STOP tracing action

To stop a transaction tracing session, run the following statement.

```
exec msdb.dbo.rds_msdtc_transaction_tracing 'STOP'
```

This statement stops the active transaction tracing session and saves the transaction
trace data into the log directory on the RDS DB instance. The first row of the
output contains the overall result, and the following lines indicate details of
the operation.

The following is an example of a successful tracing session stop.

```
**OK: Trace session has been successfully stopped.**
Setting log file to: D:\rdsdbdata\MSDTC\Trace\dtctrace.log
Examining D:\rdsdbdata\MSDTC\Trace\msdtctr.mof for message formats,  8 found.
Searching for TMF files on path: (null)
Logfile D:\rdsdbdata\MSDTC\Trace\dtctrace.log:
 OS version    10.0.14393  (Currently running on 6.2.9200)
 Start Time    <timestamp>
 End Time      <timestamp>
 Timezone is   @tzres.dll,-932 (Bias is 0mins)
 BufferSize            16384 B
 Maximum File Size     10 MB
 Buffers  Written      Not set (Logger may not have been stopped).
 Logger Mode Settings (11000002) ( circular paged
 ProcessorCount         1
Processing completed   Buffers: 1, Events: 3, EventsLost: 0 :: Format Errors: 0, Unknowns: 3
Event traces dumped to **d:\rdsdbdata\Log\msdtc\_<`timestamp`>.log**
```

You can use the detailed information to query the name of the generated log file. For more
information about downloading log files from the RDS DB instance, see [Monitoring Amazon RDS log files](USER_LogAccess.md "USER_LogAccess.md").

The trace session logs remain on the instance for 35 days. Any older trace session logs are automatically deleted.

###### Example of STATUS tracing action

To trace the status of a transaction tracing session, run the following statement.

```
exec msdb.dbo.rds_msdtc_transaction_tracing 'STATUS'
```

This statement outputs the following as separate rows of the result set.

```
OK
SessionStatus: <`Started|Stopped`>
TraceAll: <`True|False`>
TraceAborted: <`True|False`>
TraceLongLived: <`True|False`>
```

The first line indicates the overall result of the operation: `OK` or
`ERROR` with details, if applicable. The subsequent lines
indicate details about the tracing session status:

- `SessionStatus` can be one of the following:
  - `Started` if a tracing session is running.
  - `Stopped` if no tracing session is running.

- The tracing session flags can be `True` or `False` depending on
  how they were set in the `START` command.
