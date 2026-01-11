# Oracle index-organized table and MySQL InnoDB clustered index

With AWS DMS, you can migrate databases that utilize Oracle index-organized tables and MySQL InnoDB clustered indexes.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                            | Key differences                                                                            |
| ------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Four star feature compatibility | Three star automation level        | [Indexes](chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.indexes "chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.indexes") | MySQL doesn’t support the index-organized tables. This is the default behavior for InnoDB. |

## Oracle usage

In Oracle, an index-organized table (IOT) object is a special type of index/table hybrid that physically controls how data is stored at the table and index level. When you create a common database table or a heap-organized table, the data is stored unsorted, as a heap. However, when you create an index-organized table, the actual table data is stored in a B-tree index structure sorted by the primary key of each row. Each leaf block in the index structure stores both the primary key and non-key columns.

IOTs provide performance improvements when accessing data using the primary key because table records are sorted or clustered using the primary key and physically co-located alongside the primary key.

### Example

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

## MySQL usage

MySQL doesn’t support index-organized tables. However it provides similar functionality using InnoDB, which is the Amazon Aurora default storage engine.

Each InnoDB table provides a special clustered index. When you create a `PRIMARY KEY` on a table, InnoDB automatically uses it as the clustered index. This behavior is similar to index-organized tables in Oracle.

The best practice is to specify a primary key for each MySQL table. If you do not specify a primary key, MySQL locates the first unique index where all key columns are specified as NOT NULL and uses it as the clustered index.

If a table layout doesn’t logically provide a column or multiple columns that are unique and not null, it is recommended to explicitly add an auto-incremented column to generate unique values.

###### Note

If no primary key or a suitable unique index can be found, InnoDB actually creates a hidden `GEN_CLUST_INDEX` clustered index with internally generated row ID values. These auto-generated row IDs are based on a 6-byte field that increases monotonically.

### Example

Create a new table with a simple primary key. Because the storage engine is InnoDB, the table is created as a clustered table sorting data based on the primary key itself.

```
CREATE TABLE SYSTEM_EVENTS (
  EVENT_ID INT PRIMARY KEY,
  EVENT_CODE VARCHAR(10) NOT NULL,
  EVENT_DESCIPTION VARCHAR(200),
  EVENT_TIME DATE NOT NULL);

INSERT INTO SYSTEM_EVENTS VALUES(9,'EVNT10','Critical',NOW());
INSERT INTO SYSTEM_EVENTS VALUES(1,'EVNT09','Warning',NOW());
INSERT INTO SYSTEM_EVENTS VALUES(7,'EVNT14','Critical',NOW());

SELECT * FROM SYSTEM_EVENTS;

event_id  event_code  event_desciption  event_time
1         EVNT-C1-09  Warning           2017-01-01
7         EVNT-E1-14  Critical          2017-01-01
9         EVNT-A1-10  Critical          2017-01-01
```

For more information, see [Clustered and Secondary Indexes](https://dev.mysql.com/doc/refman/5.7/en/innodb-index-types.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-index-types.html") in the _MySQL documentation_.
