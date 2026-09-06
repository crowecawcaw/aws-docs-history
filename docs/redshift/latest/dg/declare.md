

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# DECLARE
<a name="declare"></a>

Defines a new cursor. Use a cursor to retrieve a few rows at a time from the result set of a larger query. 

When the first row of a cursor is fetched, the entire result set is materialized on the leader node, in memory or on disk, if needed. Because of the potential negative performance impact of using cursors with large result sets, we recommend using alternative approaches whenever possible. For more information, see [Performance considerations when using cursors](#declare-performance).

You must declare a cursor within a transaction block. Only one cursor at a time can be open per session. 

For more information, see [FETCH](fetch.md), [CLOSE](close.md).

## Syntax
<a name="declare-synopsis"></a>

```
DECLARE cursor_name CURSOR FOR query
```

## Parameters
<a name="declare-parameters"></a>

*cursor\_name*   
Name of the new cursor. 

 *query*   
A SELECT statement that populates the cursor.

## DECLARE CURSOR usage notes
<a name="declare-usage"></a>

If your client application uses an ODBC connection and your query creates a result set that is too large to fit in memory, you can stream the result set to your client application by using a cursor. When you use a cursor, the entire result set is materialized on the leader node, and then your client can fetch the results incrementally. 

**Note**  
To enable cursors in ODBC for Microsoft Windows, enable the **Use Declare/Fetch** option in the ODBC DSN you use for Amazon Redshift. We recommend setting the ODBC cache size, using the **Cache Size** field in the ODBC DSN options dialog, to 4,000 or greater on multi-node clusters to minimize round trips. On a single-node cluster, set Cache Size to 1,000.

Because of the potential negative performance impact of using cursors, we recommend using alternative approaches whenever possible. For more information, see [Performance considerations when using cursors](#declare-performance).

Amazon Redshift cursors are supported with the following limitations:
+ Only one cursor at a time can be open per session. 
+ Cursors must be used within a transaction (BEGIN … END). 
+ The maximum cumulative result set size for all cursors is constrained based on the cluster node type. This is a cluster-wide total that is shared across all cursors that are open at the same time; a single cursor can use only part of it, because some capacity is reserved so that multiple cursors can run concurrently. If you need larger result sets, you can resize to a larger node configuration.

  For more information, see [Cursor constraints](#declare-constraints). 

## Cursor constraints
<a name="declare-constraints"></a>

When the first row of a cursor is fetched, the entire result set is materialized on the leader node. If the result set doesn't fit in memory, it is written to disk as needed. To protect the integrity of the leader node, Amazon Redshift enforces constraints on the size of cursor result sets, based on the cluster's node type.

The value in the following table is a cluster-wide total, not a per-cursor limit. To make sure that multiple cursors can be open concurrently, a portion of this total capacity is reserved for concurrent use. As a result, a single cursor can't use the entire cumulative maximum on its own; the largest result set that one cursor can hold is less than the total shown in the table. An individual cursor can fail when its result set reaches this per-cursor boundary, even when the cluster's overall cursor capacity isn't fully used.

The following table shows the maximum cumulative result set size for each cluster node type. Maximum result set sizes are in megabytes.


| Node type | Maximum cumulative result set per cluster (MB) | 
| --- | --- | 
|  rg.12xlarge multiple nodes  | 7,200,000 | 
|  rg.4xlarge multiple nodes  | 1,600,000 | 
|  rg.xlarge multiple nodes  | 240,000 | 
|  rg.large multiple nodes  | 100,000 | 
|  rg.large single node  | 8,000 | 
|  ra3.16xlarge multiple nodes  | 14,400,000 | 
|  ra3.4xlarge multiple nodes  | 3,200,000 | 
|  ra3.xlplus multiple nodes  | 1,000,000 | 
|  ra3.xlplus single node  | 64,000 | 
|  ra3.large multiple nodes  | 240,000 | 
|  ra3.large single node  | 8,000 | 
| Amazon Redshift Serverless | 150,000 | 
|  dc2.8xlarge multiple nodes  | 3,200,000 | 
|  dc2.large multiple nodes  | 192,000 | 
|  dc2.large single node  | 8,000 | 

To view the active cursor configuration for a cluster, query the [STV\_CURSOR\_CONFIGURATION](r_STV_CURSOR_CONFIGURATION.md) system table as a superuser. To view the state of active cursors, query the [STV\_ACTIVE\_CURSORS](r_STV_ACTIVE_CURSORS.md) system table. Only the rows for a user's own cursors are visible to the user, but a superuser can view all cursors.

## Performance considerations when using cursors
<a name="declare-performance"></a>

Because cursors materialize the entire result set on the leader node before beginning to return results to the client, using cursors with very large result sets can have a negative impact on performance. We strongly recommend against using cursors with very large result sets. In some cases, such as when your application uses an ODBC connection, cursors might be the only feasible solution. If possible, we recommend using these alternatives:
+ Use [UNLOAD](r_UNLOAD.md) to export a large table. When you use UNLOAD, the compute nodes work in parallel to transfer the data directly to data files on Amazon Simple Storage Service. For more information, see [Unloading data in Amazon Redshift](c_unloading_data.md). 
+ Set the JDBC fetch size parameter in your client application. If you use a JDBC connection and you are encountering client-side out-of-memory errors, you can enable your client to retrieve result sets in smaller batches by setting the JDBC fetch size parameter. For more information, see [Setting the JDBC fetch size parameter](set-the-JDBC-fetch-size-parameter.md). 

RG nodes have smaller maximum cursor result set sizes compared to RA3 nodes of similar compute capacity. If your cursor workloads approach or exceed the limit for your RG node type, consider the following options:
+ **Optimize result set sizes.** Apply more selective query filters, reduce the number of columns retrieved, or implement application-level pagination to process results in smaller batches.
+ **Migrate to a larger RG node type.** A larger node type provides a higher cursor capacity. If your node count allows and workload performance is not impacted, you can reduce the number of nodes proportionally to maintain a comparable total cluster cost.

To determine the current size of your cursor's result set, query the SYS\_QUERY\_HISTORY view for the `returned_bytes` value associated with the first FETCH statement executed against the cursor. For more information, see [SYS\_QUERY\_HISTORY](https://docs.aws.amazon.com/redshift/latest/dg/SYS_QUERY_HISTORY.html).

## DECLARE CURSOR examples
<a name="declare-example"></a>

The following example declares a cursor named LOLLAPALOOZA to select sales information for the Lollapalooza event, and then fetches rows from the result set using the cursor:

```
-- Begin a transaction

begin;

-- Declare a cursor

declare lollapalooza cursor for
select eventname, starttime, pricepaid/qtysold as costperticket, qtysold
from sales, event
where sales.eventid = event.eventid
and eventname='Lollapalooza';

-- Fetch the first 5 rows in the cursor lollapalooza:

fetch forward 5 from lollapalooza;

  eventname   |      starttime      | costperticket | qtysold
--------------+---------------------+---------------+---------
 Lollapalooza | 2008-05-01 19:00:00 |   92.00000000 |       3
 Lollapalooza | 2008-11-15 15:00:00 |  222.00000000 |       2
 Lollapalooza | 2008-04-17 15:00:00 |  239.00000000 |       3
 Lollapalooza | 2008-04-17 15:00:00 |  239.00000000 |       4
 Lollapalooza | 2008-04-17 15:00:00 |  239.00000000 |       1
(5 rows)

-- Fetch the next row:

fetch next from lollapalooza;

  eventname   |      starttime      | costperticket | qtysold
--------------+---------------------+---------------+---------
 Lollapalooza | 2008-10-06 14:00:00 |  114.00000000 |       2

-- Close the cursor and end the transaction:

close lollapalooza;
commit;
```

The following example loops over a refcursor with all the results from a table:

```
CREATE TABLE tbl_1 (a int, b int);
INSERT INTO tbl_1 values (1, 2),(3, 4);

CREATE OR REPLACE PROCEDURE sp_cursor_loop() AS $$
DECLARE
    target record;
    curs1 cursor for select * from tbl_1;
BEGIN
    OPEN curs1;
    LOOP
        fetch curs1 into target;
        exit when not found;
        RAISE INFO 'a %', target.a;
    END LOOP;
    CLOSE curs1;
END;
$$ LANGUAGE plpgsql;

CALL sp_cursor_loop();
         
SELECT message 
   from svl_stored_proc_messages 
   where querytxt like 'CALL sp_cursor_loop()%';
         
  message
----------
      a 1
      a 3
```