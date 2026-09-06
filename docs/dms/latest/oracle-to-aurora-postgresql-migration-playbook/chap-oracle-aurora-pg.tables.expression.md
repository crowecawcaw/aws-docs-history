

# Oracle function-based indexes and PostgreSQL expression indexes
<a name="chap-oracle-aurora-pg.tables.expression"></a>

With AWS DMS, you can create function-based indexes in Oracle databases and expression indexes in PostgreSQL databases to improve query performance. Function-based indexes in Oracle allow indexing on expressions or function results, while expression indexes in PostgreSQL index expressions based on one or more columns.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-4.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-4.png)  |  [Indexes](chap-oracle-aurora-pg.tools.actioncode.md#chap-oracle-aurora-pg.tools.actioncode.indexes)  | PostgreSQL doesn’t support functional indexes that aren’t single-column. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.tables.expression.ora"></a>

Function-based indexes allow functions to be used in the `WHERE` clause of queries on indexed columns. Function-based indexes store the output of a function applied on the values of a table column. The Oracle query optimizer only uses a function-based index when the function is used as part of a query.

Oracle updates the index for each DML to ensure that the value that returns from the function is correct.

 **Examples** 

Create a function-based index.

```
CREATE TABLE SYSTEM_EVENTS(
  EVENT_ID NUMERIC PRIMARY KEY,
  EVENT_CODE VARCHAR2(10) NOT NULL,
  EVENT_DESCIPTION VARCHAR2(200),
  EVENT_TIME TIMESTAMPNOT NULL);

CREATE INDEX EVNT_BY_DAY ON SYSTEM_EVENTS(
  EXTRACT(DAY FROM EVENT_TIME));
```

For more information, see [Indexes and Index-Organized Tables](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/indexes-and-index-organized-tables.html#GUID-797E49E6-2DCE-4FD4-8E4A-6E761F1383D1) and [CREATE INDEX](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-INDEX.html#GUID-1F89BBC0-825F-4215-AF71-7588E31D8BFE) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.tables.expression.pg"></a>

PostgreSQL supports expression indexes which are similar to function-based indexes in Oracle.

 **Examples** 

Create an expression index in PostgreSQL.

```
CREATE TABLE system_events(
  event_id NUMERIC PRIMARY KEY,
  event_code VARCHAR(21) NOT NULL,
  event_description VARCHAR(200),
  event_time TIMESTAMP NOT NULL);

CREATE INDEX event_by_day ON system_events(EXTRACT(DAY FROM event_time));
```

Insert records to the `system_events` table, gathering table statistics using the `ANALYZE` statement and verifying that the `EVNT_BY_DAY` expression index is being used for data access.

```
INSERT INTO system_events
  SELECT ID AS event_id,
    'EVNT-A'||ID+9||'-'||ID AS event_code,
    CASE WHEN mod(ID,2) = 0 THEN 'Warning' ELSE 'Critical' END AS event_desc,
    now() + INTERVAL '1 minute' * ID AS event_time
  FROM
  (SELECT generate_series(1,1000000) AS ID) A;
INSERT 0 1000000

ANALYZE SYSTEM_EVENTS;

EXPLAIN
  SELECT * FROM SYSTEM_EVENTS
  WHERE EXTRACT(DAY FROM EVENT_TIME) = '22';

QUERY PLAN
Bitmap Heap Scan on system_events (cost=729.08..10569.58 rows=33633 width=41)
Recheck Cond: (date_part('day'::text, event_time) = '22'::double precision)
-> Bitmap Index Scan on evnt_by_day (cost=0.00..720.67 rows=33633 width=0)
Index Cond: (date_part('day'::text, event_time) = '22'::double precision)
```

### Partial indexes
<a name="chap-oracle-aurora-pg.tables.expression.pg.partial"></a>

PostgreSQL also offers partial indexes, which are indexes that use a `WHERE` clause when created. The biggest benefit of using partial indexes is reduction of the overall subset of indexed data allowing users to index relevant table data only. You can use partial indexes to increase efficiency and reduce the size of the index.

 **Example** 

Create a PostgreSQL partial index.

```
CREATE TABLE SYSTEM_EVENTS(
  EVENT_ID NUMERIC PRIMARY KEY,
  EVENT_CODE VARCHAR(10) NOT NULL,
  EVENT_DESCIPTION VARCHAR(200),
  EVENT_TIME DATE NOT NULL);

CREATE INDEX IDX_TIME_CODE ON SYSTEM_EVENTS(EVENT_TIME)
  WHERE EVENT_CODE like '01-A%';
```

For more information, see [Building Indexes Concurrently](https://www.postgresql.org/docs/13/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY) in the *PostgreSQL documentation*.