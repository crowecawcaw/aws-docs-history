

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_ANALYZE\_HISTORY
<a name="SYS_ANALYZE_HISTORY"></a>

Logs details for [ANALYZE](https://docs.aws.amazon.com/redshift/latest/dg/r_ANALYZE.html) operations.

SYS\_ANALYZE\_HISTORY is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SYS_ANALYZE_HISTORY-table-rows"></a>


| Column name | Data type | Description | 
| --- | --- | --- | 
| user\_id | integer | The ID of the user who generated the entry. | 
| transaction\_id | long | The transaction ID. | 
| database\_name | char(30) | The name of the database. | 
| table\_name | char(30) | The name of the table. | 
| table\_id | integer | The ID of the table. | 
| is\_automatic | char(1) | The value is true (t) if the operation included an Amazon Redshift ANALYZE operation by default. The value is false (f) if the ANALYZE command was run explicitly. | 
| status | char(15) | The result of the analyze command. Possible values are Full, Skipped, and PredicateColumn. | 
| start\_time | timestamp | The time in UTC of when the ANALYZE operation started running. | 
| end\_time | timestamp | The time in UTC of when the ANALYZE operation finished running. | 
| rows | double | The total number of rows in the table | 
| modified\_rows | double | The total number of rows that were modified since the last ANALYZE operation. | 
| analyze\_threshold\_percent | integer | The value of the analyze\_threshold\_percent parameter. | 
| last\_analyze\_time | timestamp | The time in UTC of when the table was previously analyzed. | 

## Sample queries
<a name="SYS_ANALYZE_HISTORY-sample-queries"></a>

```
 user_id | transaction_id | database_name | schema_name |      table_name     | table_id | is_automatic | Status |         start_time         |          end_time          | rows | modified_rows | analyze_threshold_percent |  last_analyze_time  
---------+----------------+---------------+-------------+---------------------+----------+--------------+--------+----------------------------+----------+-----------------+------+---------------+---------------------------+---------------------
     101 |           8006 |           dev |      public | test_table_562bf8dc |   110427 |            f |   Full | 2023-09-21 18:33:08.504646 | 2023-09-21 18:33:24.296498 |    5 |             5 |                         0 | 2000-01-01 00:00:00
```