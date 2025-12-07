# Oracle index-organized table and PostgreSQL cluster table

With AWS DMS, you can migrate data from Oracle index-organized tables and PostgreSQL cluster tables to target databases. An Oracle index-organized table stores data values in a B-tree index structure, providing excellent performance for queries involving primary key ranges. A PostgreSQL cluster table clusters related rows on disk by rewriting the table using an index, improving performance on queries that retrieve data from indexed columns.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                | Key differences                                                                       |
| ------------------------------ | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| Two star feature compatibility | No automation                      | [Indexes](chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.indexes "chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.indexes") | PostgreSQL doesn’t support index-organized tables, a partial workaround is available. |

## Oracle usage

In Oracle, an index-organized table (IOT) are a special type of index/table hybrid that physically controls how data is stored at the table and index level. When creating a common database table, or heap-organized table, the data is stored unsorted (as a heap). However, when creating an Index-organized table, the actual table data is stored in a B-tree index structure sorted by the primary key of each row. Each leaf block in the index structure stores both the primary key and non-key columns.

IOTs provide performance improvements when accessing data using the primary key because table records are sorted (clustered) using the primary key and physically co-located alongside the primary key.

**Examples**

Create an Oracle index-organized table storing ordered data based on the primary key.

```
CREATE TABLE SYSTEM_EVENTS (
  EVENT_ID NUMBER,
  EVENT_CODE VARCHAR2(10) NOT NULL,
  EVENT_DESCIPTION VARCHAR2(200),
  EVENT_TIME DATE NOT NULL,
  CONSTRAINT PK_EVENT_ID PRIMARY KEY(EVENT_ID))
  ORGANIZATION INDEX;

INSERT INTO SYSTEM_EVENTS VALUES(9, 'EVNT-A1-10', 'Critical', '01-JAN-2017');
INSERT INTO SYSTEM_EVENTS VALUES(1, 'EVNT-C1-09', 'Warning', '01-JAN-2017');
INSERT INTO SYSTEM_EVENTS VALUES(7, 'EVNT-E1-14', 'Critical', '01-JAN-2017');

SELECT * FROM SYSTEM_EVENTS;

EVENT_ID  EVENT_CODE  EVENT_DESCIPTION  EVENT_TIM
1         EVNT-C1-09  Warning           01-JAN-17
7         EVNT-E1-14  Critical          01-JAN-17
9         EVNT-A1-10  Critical          01-JAN-17
```

###### Note

The records are sorted in the reverse order from which they were inserted.

For more information, see [Indexes and Index-Organized Tables](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/indexes-and-index-organized-tables.html#GUID-797E49E6-2DCE-4FD4-8E4A-6E761F1383D1 "https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/indexes-and-index-organized-tables.html#GUID-797E49E6-2DCE-4FD4-8E4A-6E761F1383D1") in the _Oracle documentation_.

## PostgreSQL usage

PostgreSQL doesn’t support IOTs directly, but offers partially similar functionality using the `CLUSTER` feature. The PostgreSQL `CLUSTER` statement specifies table sorting based on an index already associated with the table. When using the PostgreSQL `CLUSTER` command, the data in the table is physically sorted based on the index, possibly using a primary key column.

###### Note

Unlike an Oracle Index-Organized Table which is defined during table creation and persists data sorting (the IOT will always remain sorted), the PostgreSQL `CLUSTER` doesn’t provide persistent sorting; it is a one-time operation. When the table is subsequently updated, the changes aren’t clustered/sorted.

You can use the `CLUSTER` statement to re-cluster the table.

**Examples**

```
CREATE TABLE SYSTEM_EVENTS (
  EVENT_ID NUMERIC,
  EVENT_CODE VARCHAR(10) NOT NULL,
  EVENT_DESCIPTION VARCHAR(200),
  EVENT_TIME DATE NOT NULL,
  CONSTRAINT PK_EVENT_ID PRIMARY KEY(EVENT_ID));

INSERT INTO SYSTEM_EVENTS VALUES(9, 'EV-A1-10', 'Critical', '01-JAN-2017');
INSERT INTO SYSTEM_EVENTS VALUES(1, 'EV-C1-09', 'Warning', '01-JAN-2017');
INSERT INTO SYSTEM_EVENTS VALUES(7, 'EV-E1-14', 'Critical', '01-JAN-2017');

CLUSTER SYSTEM_EVENTS USING PK_EVENT_ID;
SELECT * FROM SYSTEM_EVENTS;

event_id  event_code  event_desciption  event_time
1         EVNT-C1-09  Warning           2017-01-01
7         EVNT-E1-14  Critical          2017-01-01
9         EVNT-A1-10  Critical          2017-01-01

INSERT INTO SYSTEM_EVENTS VALUES(2, 'EV-E2-02', 'Warning', '01-JAN-2017');
SELECT * FROM SYSTEM_EVENTS;

event_id  event_code  event_desciption  event_time
1         EVNT-C1-09  Warning           2017-01-01
7         EVNT-E1-14  Critical          2017-01-01
9         EVNT-A1-10  Critical          2017-01-01
2         EVNT-E2-02  Warning           2017-01-01

CLUSTER SYSTEM_EVENTS USING PK_EVENT_ID; -- Run CLUSTER again to re-cluster
SELECT * FROM SYSTEM_EVENTS;

event_id  event_code  event_desciption  event_time
1         EVNT-C1-09  Warning           2017-01-01
2         EVNT-E2-02  Warning           2017-01-01
7         EVNT-E1-14  Critical          2017-01-01
9         EVNT-A1-10  Critical          2017-01-01
```

For more information, see [CLUSTER](https://www.postgresql.org/docs/13/sql-cluster.htm "https://www.postgresql.org/docs/13/sql-cluster.htm") and [Building Indexes Concurrently](https://www.postgresql.org/docs/13/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY "https://www.postgresql.org/docs/13/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY") in the _PostgreSQL documentation_.
