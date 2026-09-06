

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVL\_MV\_REFRESH\_STATUS
<a name="r_SVL_MV_REFRESH_STATUS"></a>

The SVL\_MV\_REFRESH\_STATUS view contains a row for the refresh activity of materialized views. 

For more information about materialized views, see [Materialized views in Amazon Redshift](materialized-view-overview.md).

SVL\_MV\_REFRESH\_STATUS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_MV\_REFRESH\_HISTORY](SYS_MV_REFRESH_HISTORY.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

## Table columns
<a name="r_SVL_MV_REFRESH_STATUS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| db\_name  | char(128)  | The database that contains the materialized view.  | 
| userid  | bigint  | The ID of the user who performed the refresh.  | 
| schema\_name  | char(128)  | The schema of the materialized view.  | 
| mv\_name  | char(128)  | The materialized view name.  | 
| xid  | bigint  | The transaction ID of the refresh.  | 
| starttime  | timestamp  | The start time of the refresh.  | 
| endtime  | timestamp  | The end time of the refresh.  | 
| status  | text  | The status of the refresh. Example values include the following: + *Refresh successfully updated MV incrementally*<br />If it's a materialized view for streaming, the message might have additional qualifiers regarding the number of records. These include the following: *Stream returned no new data* – There were no records retrieved. *All records received from the stream were skipped* – Records were retrieved, but due to errors all were skipped. *Some stream records were skipped* – Records were retrieved, but due to errors some were skipped.  <br />If there are no qualifiers, then at least one record was retrieved and all records are available in the materialized view. There is one remaining possible qualifier: <br />  *The stream may contain more data* – The refresh ended before Amazon Redshift determined that there were no further records to consume. The stream can be up to date, but it hasn't been confirmed by Amazon Redshift.  <br />+ *Refresh successfully recomputed MV from scratch*<br />+ *Refresh partially updated MV incrementally up to an active transaction*<br />+ *MV was already updated*<br />+  *Cascade automatic refresh skipped because materialized view <schema>.<name> was not refreshed.* <br />+  *Cascade refresh skipped because materialized view <schema>.<name> was not refreshed.* <br />+  *Cascade automatic refresh failed because materialized view <schema>.<name> was not refreshed.* <br />*Cascade refresh failed because materialized view <schema>.<name> was not refreshed.* <br />+ *Refresh failed. A base table column was renamed*<br />+ *Refresh failed. A base table column type was changed*<br />+ *Refresh failed. A base table was renamed*<br />+ *Refresh failed due to an internal error*<br />+ *Refresh failed. A base table column was dropped*<br />+ *Refresh failed. Schema of MV was renamed*<br />+ *Refresh failed. MV was not found*<br />+ *Auto refresh aborted due to excessive user workload*<br />+ *Refresh failed. Serializable isolation violation* | 
| refresh\_type | char(32) | The definition of the refresh type. Example values include Manual and Auto.  | 
| consumer\_account | char(12) | The AWS account ID of the consumer cluster that initiated the refresh. This field is populated when the refresh is initiated from a consumer cluster in a data sharing setup.  | 
| consumer\_region | char(32) | The AWS Region of the consumer cluster that initiated the refresh. This field is populated when the refresh is initiated from a consumer cluster in a data sharing setup.  | 
| consumer\_namespace | char(36) | The namespace identifier of the consumer cluster that initiated the refresh. This field is populated when the refresh is initiated from a consumer cluster in a data sharing setup.  | 

## Sample query
<a name="r_SVL_MV_REFRESH-sample-query"></a>

To view the refresh status of materialized views, run the following query. 

```
select * from svl_mv_refresh_status;
```

This query returns the following sample output: 

```
 db_name | userid |  schema   |  name   |  xid  |         starttime          |          endtime           |                        status                                                       |  refresh_type | consumer_account | consumer_region | consumer_namespace
---------+--------+-----------+---------+-------+----------------------------+----------------------------+-------------------------------------------------------------------------------------+---------------+------------------+-----------------+------------------------------------
 dev     |    169 | mv_schema | mv_test |  6640 | 2020-02-14 02:26:53.497935 | 2020-02-14 02:26:53.556156 | Refresh successfully recomputed MV from scratch                                     |  Manual       |                  |                 |
 dev     |    166 | mv_schema | mv_test |  6517 | 2020-02-14 02:26:39.287438 | 2020-02-14 02:26:39.349539 | Refresh successfully updated MV incrementally                                       |  Auto         |                  |                 |
 ext_db  |    162 | producer_schema | producer_mv |  6388 | 2020-02-14 02:26:27.863426 | 2020-02-14 02:26:27.918307 | Refresh successfully updated MV incrementally                                     |  Manual       | 0123456789       | us-east-1       | 623d8ff2-4391-4381-83d7-177caa6767af
 dev     |    161 | mv_schema | mv_test |  6323 | 2020-02-14 02:26:20.020717 | 2020-02-14 02:26:20.080002 | Refresh successfully updated MV incrementally                                       |  Auto         |                  |                 |
 dev     |    161 | mv_schema | mv_test |  6301 | 2020-02-14 02:26:05.796146 | 2020-02-14 02:26:07.853986 | Refresh successfully recomputed MV from scratch                                     |  Manual       |                  |                 |
 dev     |    153 | mv_schema | mv_test |  6024 | 2020-02-14 02:25:18.762335 | 2020-02-14 02:25:20.043462 | MV was already updated                                                              |  Manual       |                  |                 |
 dev     |    143 | mv_schema | mv_test |  5557 | 2020-02-14 02:24:23.100601 | 2020-02-14 02:24:23.100633 | MV was already updated                                                              |  Manual
 dev     |    141 | mv_schema | mv_test |  5447 | 2020-02-14 02:23:54.102837 | 2020-02-14 02:24:00.310166 | Refresh successfully updated MV incrementally                                       |  Auto
 dev     |      1 | mv_schema | mv_test |  5329 | 2020-02-14 02:22:26.328481 | 2020-02-14 02:22:28.369217 | Refresh successfully recomputed MV from scratch                                     |  Auto
 dev     |    138 | mv_schema | mv_test |  5290 | 2020-02-14 02:21:56.885093 | 2020-02-14 02:21:56.885098 | Refresh failed. MV was not found                                                    |  Manual
 dev     |    138 | mv_schema | mv_test |  5100 | 2020-02-14 02:20:33.123445 | 2020-02-14 02:20:33.123445 | Cascade refresh failed because materialized view mv_schema.child was not refreshed. |  Manual
 dev     |    138 | mv_schema | child   |  5100 | 2020-02-14 02:20:33.123445 | 2020-02-14 02:20:33.123445 | Refresh failed due to an internal error.                                            |  Manual
 dev     |    138 | mv_schema | mv_test |  5099 | 2020-02-14 02:10:23.492344 | 2020-02-14 02:10:23.492344 | Cascade refresh skipped because materialized view mv_schema.child was not refreshed.|  Manual
 dev     |    138 | mv_schema | child   |  5099 | 2020-02-14 02:10:23.492344 | 2020-02-14 02:10:23.492344 | Refresh failed due to an internal error.                                            |  Manual
```