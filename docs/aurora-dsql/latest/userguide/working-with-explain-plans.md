# Working with Aurora DSQL EXPLAIN plans

Aurora DSQL uses a similar EXPLAIN plan structure to PostgreSQL,
but with key additions that reflect its distributed architecture and execution model.

In this documentation, we'll provide an overview of Aurora DSQL EXPLAIN plans, highlighting the
similarities and differences compared to PostgreSQL. We'll cover the various types of scan
operations available in Aurora DSQL and help you understand the cost of running your queries.

## PostgreSQL VS Aurora DSQL EXPLAIN plans

Aurora DSQL is built on top of the PostgreSQL database and shares most plan structures with PostgreSQL, but has key architectural diﬀerences that aﬀect query execution and optimization:

| Feature                | PostgreSQL                                    | Aurora DSQL                                                              |
| ---------------------- | --------------------------------------------- | ------------------------------------------------------------------------ |
| Data Storage           | Heap Storage                                  | No heap, all rows are indexed by a unique identifier                     |
| Primary Key            | Primary key index is separate from table data | Primary key index is the table with all extra columns as INCLUDE columns |
| Secondary Indexes      | Standard secondary indexes                    | Work the same as PostgreSQL, with ability to include non-key columns     |
| Filtering Capabilities | Index Condition, Heap Filter                  | Index Condition, Storage Filter, Query Processor Filter                  |
| Scan Types             | Sequential Scan, Index Scan, Index Only Scan  | Full Scan, Index Only Scan, Index Scan                                   |
| Query Execution        | Local to the Database                         | Distributed (compute and storage are separate)                           |

Aurora DSQL stores table data directly in primary key order rather than in a separate heap. Each
row is identified by a unique key, typically the primary key, which allows the database to optimize lookups more
efficiently. The architectural difference
explains why Aurora DSQL often uses Index Only Scans in cases where PostgreSQL might choose a
sequential scan.

Another key distinction is that Aurora DSQL separates compute from storage, enabling filters
to be applied earlier in the execution path to reduce data movement and improve
performance.

For more using EXPLAIN plans with PostgreSQL, see the [PostgreSQL EXPLAIN
documentation](https://www.postgresql.org/docs/current/using-explain.html "https://www.postgresql.org/docs/current/using-explain.html").

## Key elements in Aurora DSQL EXPLAIN plans

Aurora DSQL EXPLAIN plans provide detailed information about how queries are executed, including where filtering occurs and which columns are retrieved from storage. Understanding this output helps you optimize query performance.

Index Cond
Conditions used to navigate the index. Most efficient filtering that reduces data scanned. In Aurora DSQL, index conditions can be applied at multiple layers of the execution plan.

Projections
Columns retrieved from storage. Fewer projections mean better performance.

Storage Filter
Conditions applied at storage level. More efficient than query processor filters.

Query Processor Filter

Conditions applied at the query processor level. Requires transferring all data before
filtering, which results in higher data movement and processing overhead.

## Filters in Aurora DSQL

Aurora DSQL separates compute from storage, which means that the point where filters are applied during query execution has a significant impact on performance. Filters applied before large volumes of data are transferred reduce latency and improve efficiency. The earlier a filter is applied, the less data needs to be processed, moved, and scanned, resulting in faster queries.

Aurora DSQL can apply filters at multiple stages in the query path. Understanding these stages is key to interpreting query plans and optimizing performance.

| Level | Filter Type            | Description                                                                                                                                                                                                                                                                          |
| ----- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | Index Condition        | Applied while scanning the index. Limits how much data is read from storage and reduces<br>the data sent to the compute layer.                                                                                                                                                       |
| 2     | Storage Filter         | Applied after data is read from storage but before it’s sent to compute. An example here is a ﬁlter on an include column of an index. Reduces data transfer but not the amount read.                                                                                                 |
| 3     | Query Processor Filter | Applied after data reaches the compute layer. All data must be transferred first, which increases latency and cost. Currently, Aurora DSQL cannot perform all ﬁltering and projection operations on storage, so some queries might be forced to fall back to this type of filtering. |
