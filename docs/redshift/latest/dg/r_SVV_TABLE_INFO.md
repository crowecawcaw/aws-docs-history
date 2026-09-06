

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_TABLE\_INFO
<a name="r_SVV_TABLE_INFO"></a>

Shows summary information for tables and materialized views in the currently connected database. The view filters out system tables, and shows only user-defined tables and materialized views that contain at least 1 row of data. 

You can use the SVV\_TABLE\_INFO view to diagnose and address table design issues that can influence query performance. This includes issues with compression encoding, distribution keys, sort style, data distribution skew, table size, and statistics. The SVV\_TABLE\_INFO view doesn't return any information for empty tables.

The SVV\_TABLE\_INFO view summarizes information from the following system tables and catalog tables: 
+  [STV\_NODE\_STORAGE\_CAPACITY](r_STV_NODE_STORAGE_CAPACITY.md) 
+  [STV\_SLICES](r_STV_SLICES.md) 
+  [STV\_TBL\_PERM](r_STV_TBL_PERM.md) 
+  [PG\_ATTRIBUTE](https://www.postgresql.org/docs/8.0/static/catalog-pg-attribute.html) 
+  [PG\_CLASS](https://www.postgresql.org/docs/8.0/static/catalog-pg-class.html) 
+  [PG\_DATABASE](https://www.postgresql.org/docs/8.0/static/catalog-pg-database.html) 
+  [PG\_NAMESPACE](https://www.postgresql.org/docs/8.0/static/catalog-pg-namespace.html) 
+  [PG\_STATISTIC\_INDICATOR](r_PG_STATISTIC_INDICATOR.md) 

SVV\_TABLE\_INFO is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data). To permit a user to query the view, grant SELECT permission on SVV\_TABLE\_INFO to the user.

## Table columns
<a name="SVV_TABLE_INFO-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| database  | text  | Database name.  | 
| schema  | text  | Schema name.  | 
| table\_id  | oid  | Table ID.  | 
| table  | text  | Table name.  | 
| encoded  | text  | Value that indicates whether any column has compression encoding defined.  | 
| diststyle  | text  | Distribution style or distribution key column, if key distribution is defined. Possible values include EVEN, KEY(column), ALL, AUTO(ALL), AUTO(EVEN), and AUTO(KEY(column)). | 
| sortkey1  | text  | First column in the sort key, if a sort key is defined. Possible values include column, AUTO(SORTKEY), and AUTO(SORTKEY(column)). | 
| max\_varchar  | integer  | Size of the largest column that uses a VARCHAR data type.  | 
| sortkey1\_enc | character(32)  | Compression encoding of the first column in the sort key, if a sort key is defined. | 
| sortkey\_num  | integer | Number of columns defined as sort keys.  | 
| size | bigint | Size of the table, in 1-MB data blocks. | 
| pct\_used  | numeric(10,4)  | Percent of available space that is used by the table.  | 
| empty | bigint | For internal use. This column is no longer used and will be removed in a future release. | 
| unsorted | numeric(5,2) | Percent of unsorted rows in the table. | 
| stats\_off  | numeric(5,2) | Number that indicates how stale the table's statistics are; 0 is current, 100 is out of date. | 
| tbl\_rows | numeric(38,0) | Total number of rows in the table. This value includes rows marked for deletion, but not yet vacuumed. | 
| skew\_sortkey1  | numeric(19,2) | Ratio of the size of the largest non-sort key column to the size of the first column of the sort key, if a sort key is defined. Use this value to evaluate the effectiveness of the sort key.  | 
| skew\_rows | numeric(19,2) | Ratio of the number of rows in the slice with the most rows to the number of rows in the slice with the fewest rows.  | 
| estimated\_visible\_rows | numeric(38,0) | The estimated rows in the table. This value does not include rows marked for deletion. | 
| risk\_event | text | Risk information about a table. The field is separated into parts: <pre>{{risk_type}}|{{xid}}|{{timestamp}}</pre>+ The `risk_type`, where `1` indicates that a `COPY command with the EXPLICIT_IDS option` ran. Amazon Redshift no longer checks the uniqueness of IDENTITY columns in the table. For more information, see [EXPLICIT_IDS](copy-parameters-data-conversion.md#copy-explicit-ids).<br />+ The transaction ID, `xid`, that introduced the risk. <br />+ The `timestamp` when the COPY command ran.The following example shows the values in the field.<pre>1|1107|2019-06-22 07:16:11.292952</pre> | 
| vacuum\_sort\_benefit | numeric(12,2) | The estimated maximum percentage improvement of scan query performance when you run vacuum sort.  | 
| create\_time | timestamp without time zone | The timestamp for when the table was created. | 

## Sample queries
<a name="SVV_TABLE_INFO-sample-queries"></a>

The following example shows encoding, distribution style, sorting, and data skew for all user-defined tables in the database. Here, "table" must be enclosed in double quotation marks because it is a reserved word.

```
select "table", encoded, diststyle, sortkey1, skew_sortkey1, skew_rows
from svv_table_info
order by 1;

table          | encoded | diststyle       | sortkey1     | skew_sortkey1 | skew_rows
---------------+---------+-----------------+--------------+---------------+----------
category       | N       | EVEN            |              |               |          
date           | N       | ALL             | dateid       |          1.00 |          
event          | Y       | KEY(eventid)    | dateid       |          1.00 |      1.02
listing        | Y       | KEY(listid)     | dateid       |          1.00 |      1.01
sales          | Y       | KEY(listid)     | dateid       |          1.00 |      1.02
users          | Y       | KEY(userid)     | userid       |          1.00 |      1.01
venue          | N       | ALL             | venueid      |          1.00 |          
(7 rows)
```