# Understanding Amazon EMR WAL pricing and

metrics

| Core feature billing unit | Details                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| EMR-WAL-Read-GiB          | API calls to read data from your table are billed as<br>ReadRequestGiB. This includes Get and Scan operations.<br>Reads are charged based on the sizes of the read items. Amazon EMR bills<br>at a minimum of 1 byte. For example, if you read a 1234.12 bytes<br>item, you're charged for 1235 bytes. Reads are aggregated every hour<br>for billing and shown as GiBs.                                                                         |
| EMR-WAL-Write-GiB         | API calls to write data from your table are billed as<br>Write-GiB. This includes Put operations. Writes are charged<br>based on the sizes of the written items. Amazon EMR bills at a minimum of<br>1 byte. For example, if you write a 1234.12 bytes item, you're<br>charged for 1235 bytes. Writes are aggregated every hour for billing<br>and shown as GiBs.                                                                                |
| EMR-WAL-WALHours          | The number of WALs that you store on the service are billed as<br>`EMR-WAL-WALHours`. Amazon EMR creates one WAL per HBase<br>Region. For example, if you create 20 HBase tables including system<br>tables, and each table has two HBase Regions, then you use 28,800<br>WAL hours, calculated as:<br>`<br>20 tables<br>x  2 Regions per table<br>x  1 WAL per Region<br>x 30 days<br>x 24 hours<br>-----------<br>28,800 EMR-WAL-WALHours<br>` |

**Example `EMRWALCount`:**

![Line graph showing ResourceCount fluctuations over time, ranging from about 18.87 to 19.20.](images/wal-metric.png)
**Example `EMRWALWorkspaceCount`:**

![Graph showing ResourceCount fluctuations over time, ranging from 7.97 to 8.32.](images/wal-metric2.png)
