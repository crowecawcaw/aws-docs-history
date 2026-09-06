

# Understanding Amazon EMR WAL pricing and metrics
<a name="emr-hbase-wal-metrics"></a>


| Core feature billing unit | Details | 
| --- | --- | 
| EMR-WAL-Read-GiB | API calls to read data for your table are billed as ReadRequestGiB. In HBase, standard table read operations like Get and Scan do not involve Write-Ahead Logs (WALs). The EMR-WAL-Read-GiB charge is specifically related to operations that involve reading from WALs, such as:1. Restoring from EMR WALs in a new cluster.<br />2. Restoring from EMR WALs for a crashed Region Server (for example, WALs replay).<br />Reads are charged based on the sizes of the read items. Amazon EMR bills at a minimum of 1 byte. For example, if you read an item that is 1234.12 bytes, you are charged for 1235 bytes. Reads are aggregated every hour for billing and shown as GiBs. | 
| EMR-WAL-Write-GiB | API calls to write data for your table are billed as Write-GiB. This includes put operations, where data is written to EMR WAL. Writes are charged based on the sizes of the written items. Amazon EMR bills at a minimum of 1 byte. For example, if you write an item that is 1234.12 bytes, you are charged for 1235 bytes. Writes are aggregated every hour for billing and shown as GiBs. | 
| EMR-WAL-WALHours | The number of WALs that you store on the service are billed as `EMR-WAL-WALHours`. Amazon EMR creates one WAL per HBase Region. For example, if you create 20 HBase tables including system tables, and each table has two HBase Regions, then you use 28,800 WAL hours, calculated as:<pre>  20 tables <br />x  2 Regions per table <br />x  1 WAL per Region <br />x 30 days <br />x 24 hours <br />-----------<br />28,800 EMR-WAL-WALHours</pre> | 

**Example `EMRWALCount`:**

![Line graph showing ResourceCount fluctuations over time, ranging from about 18.87 to 19.20.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/wal-metric.png)


**Example `EMRWALWorkspaceCount`:**

![Graph showing ResourceCount fluctuations over time, ranging from 7.97 to 8.32.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/wal-metric2.png)
