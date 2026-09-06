

# Data retention in the Connect Customer analytics data lake
<a name="data-lake-data-retention"></a>

The data lake retention system in Connect Customer maintains a rolling 25-month window of accessible data, with the cutoff date updating at 12 AM UTC. For example, if you access the data lake on September 1, 2025, at 03:00 AM UTC, Connect Customer will provide access to data from August 1, 2023, 12:00 AM UTC onwards, while any data before this cutoff date will not be accessible.

**Retaining data past the 25-month window**  
The 25-month window is fixed. You cannot change the retention period. To keep data for longer, such as to meet statutory retention requirements, copy the data to storage that you control before it ages out of the window.  
You access the data lake tables from your own account with AWS Lake Formation and . For more information, see [Access Connect Customer data lake](access-datalake.md). To retain data, run a scheduled query that writes each table to your own Amazon S3 bucket, for example with an `CREATE TABLE AS SELECT` (CTAS) query or an `UNLOAD` statement. You can then apply an Amazon S3 Lifecycle configuration to move the exported objects to a lower-cost storage class, such as Amazon S3 Glacier, and to expire them after your required retention period. For more information, see [Managing the lifecycle of objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) in the *Amazon S3 User Guide*.

Each data lake table uses a designated timestamp field for age calculations. The following table lists each the data lake table name and the name of their age timestamp column.


|  **Table name**  |  **Age timestamp column**  | 
| --- | --- | 
| agent\_queue\_statistic\_record | interval\_end\_time | 
| agent\_statistic\_record | interval\_end\_time | 
| contact\_evaluation\_record | evaluation\_submitted\_timestamp | 
| contact\_flow\_events | start\_timestamp | 
| contact\_lens\_conversational\_analytics | disconnect\_timestamp | 
| contact\_statistic\_record | disconnect\_timestamp | 
| contact\_record | disconnect\_timestamp | 
| staff\_shift\_activities | last\_updated\_timestamp | 
| staff\_shifts | last\_updated\_timestamp | 
| staff\_timeoffs | last\_updated\_timestamp | 
| staff\_timeoff\_intervals | last\_updated\_timestamp | 
| short\_term\_forecasts | creation\_timestamp | 
| long\_term\_forecasts | creation\_timestamp | 
| outbound\_campaign\_events | campaign\_event\_timestamp | 
| schedule\_metrics | last\_updated\_timestamp | 
| schedule\_goals | last\_updated\_timestamp | 
| bot\_conversations | bot\_conversation\_end\_timestamp | 
| bot\_intents | bot\_conversation\_end\_timestamp | 
| bot\_slots | bot\_conversation\_end\_timestamp | 
| intraday\_forecasts | creation\_timestamp | 