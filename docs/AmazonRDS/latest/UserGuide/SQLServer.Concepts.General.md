# Microsoft SQL Server features on Amazon RDS

The supported SQL Server versions on Amazon RDS include the following features. In general, a version also includes features from the
previous versions, unless otherwise noted in the Microsoft documentation.

###### Topics

- [Microsoft SQL Server 2022 features](#SQLServer.Concepts.General.FeatureSupport.2022 "#SQLServer.Concepts.General.FeatureSupport.2022")
- [Microsoft SQL Server 2019 features](#SQLServer.Concepts.General.FeatureSupport.2019 "#SQLServer.Concepts.General.FeatureSupport.2019")
- [Microsoft SQL Server 2017 features](#SQLServer.Concepts.General.FeatureSupport.2017 "#SQLServer.Concepts.General.FeatureSupport.2017")
- [Microsoft SQL Server 2016 features](#SQLServer.Concepts.General.FeatureSupport.2016 "#SQLServer.Concepts.General.FeatureSupport.2016")
- [Microsoft SQL Server 2014 end of support on Amazon RDS](#SQLServer.Concepts.General.FeatureSupport.2014 "#SQLServer.Concepts.General.FeatureSupport.2014")
- [Microsoft SQL Server 2012 end of support on Amazon RDS](#SQLServer.Concepts.General.FeatureSupport.2012 "#SQLServer.Concepts.General.FeatureSupport.2012")
- [Microsoft SQL Server 2008 R2 end of support on Amazon RDS](#SQLServer.Concepts.General.FeatureSupport.2008 "#SQLServer.Concepts.General.FeatureSupport.2008")
- [Change data capture support for Microsoft SQL Server DB instances](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md")
- [Features not supported and features with limited support](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md")

## Microsoft SQL Server 2022 features

SQL Server 2022 includes many new features, such as the following:

- Parameter Sensitive Plan Optimization – allows multiple cached plans for a single parameterized statement,
  potentially reducing issues with parameter sniffing.
- SQL Server Ledger – provides the ability to cryptographically prove that your data hasn't been altered without authorization.
- Instant file initialization for transaction log file growth events – results in faster execution of log growth events up to 64MB,
  including for databases with TDE enabled.
- System page latch concurrency enhancements – reduces page latch contention while allocating and deallocating data pages and extents,
  providing significant performance enhancements to `tempdb` heavy workloads.

For the full list of SQL Server 2022 features, see [What's new in SQL Server 2022 (16.x)](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2022?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2022?view=sql-server-ver16") in the Microsoft
documentation.

For a list of unsupported features, see [Features not supported and features with limited support](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md").

## Microsoft SQL Server 2019 features

SQL Server 2019 includes many new features, such as the following:

- Accelerated database recovery (ADR) – Reduces crash recovery time after a restart or a
  long-running transaction rollback.
- Intelligent Query Processing (IQP):
  - Row mode memory grant feedback – Corrects excessive grants automatically, that
    would otherwise result in wasted memory and reduced
    concurrency.
  - Batch mode on rowstore – Enables batch mode execution for analytic
    workloads without requiring columnstore indexes.
  - Table variable deferred compilation – Improves plan quality and
    overall performance for queries that reference table
    variables.

- Intelligent performance:
  - `OPTIMIZE_FOR_SEQUENTIAL_KEY` index option – Improves throughput for
    high-concurrency inserts into indexes.
  - Improved indirect checkpoint scalability – Helps databases with
    heavy DML workloads.
  - Concurrent Page Free Space (PFS) updates – Enables handling as a shared latch
    rather than an exclusive latch.

- Monitoring improvements:
  - `WAIT_ON_SYNC_STATISTICS_REFRESH` wait type – Shows accumulated
    instance-level time spent on synchronous statistics refresh
    operations.
  - Database-scoped configurations – Include
    `LIGHTWEIGHT_QUERY_PROFILING` and
    `LAST_QUERY_PLAN_STATS`.
  - Dynamic management functions (DMFs) – Include
    `sys.dm_exec_query_plan_stats` and
    `sys.dm_db_page_info`.

- Verbose truncation warnings – The data truncation error message defaults to
  include table and column names and the truncated value.
- Resumable online index creation – In SQL Server 2017, only resumable online
  index rebuild is supported.

For the full list of SQL Server 2019 features, see [What's new in SQL Server 2019 (15.x)](https://docs.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-ver15 "https://docs.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-ver15") in the Microsoft
documentation.

For a list of unsupported features, see [Features not supported and features with limited support](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md").

## Microsoft SQL Server 2017 features

SQL Server 2017 includes many new features, such as the following:

- Adaptive query processing
- Automatic plan correction (an automatic tuning feature)
- GraphDB
- Resumable index rebuilds

For the full list of SQL Server 2017 features, see [What's new in SQL Server 2017](https://docs.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2017 "https://docs.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2017") in the Microsoft documentation.

For a list of unsupported features, see [Features not supported and features with limited support](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md").

## Microsoft SQL Server 2016 features

Amazon RDS supports the following features of SQL Server 2016:

- Always Encrypted
- JSON Support
- Operational Analytics
- Query Store
- Temporal Tables

For the full list of SQL Server 2016 features, see [What's new in SQL Server 2016](https://docs.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2016 "https://docs.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2016") in the Microsoft documentation.

## Microsoft SQL Server 2014 end of support on Amazon RDS

SQL Server 2014 has reached its end of support on Amazon RDS.

RDS is upgrading all existing DB instances that are still using SQL Server 2014 to
the latest minor version of SQL Server 2016. For more information, see [Version management in Amazon RDS](SQLServer.Concepts.General.md#SQLServer.Concepts.General.Version-Management "SQLServer.Concepts.General.md#SQLServer.Concepts.General.Version-Management").

## Microsoft SQL Server 2012 end of support on Amazon RDS

SQL Server 2012 has reached its end of support on Amazon RDS.

RDS is upgrading all existing DB instances that are still using SQL Server 2012 to the
latest minor version of SQL Server 2016. For more information, see [Version management in Amazon RDS](SQLServer.Concepts.General.md#SQLServer.Concepts.General.Version-Management "SQLServer.Concepts.General.md#SQLServer.Concepts.General.Version-Management").

## Microsoft SQL Server 2008 R2 end of support on Amazon RDS

SQL Server 2008 R2 has reached its end of support on Amazon RDS.

RDS is upgrading all existing DB instances that are still using SQL Server 2008 R2 to the
latest minor version of SQL Server 2012. For more information, see [Version management in Amazon RDS](SQLServer.Concepts.General.md#SQLServer.Concepts.General.Version-Management "SQLServer.Concepts.General.md#SQLServer.Concepts.General.Version-Management").
