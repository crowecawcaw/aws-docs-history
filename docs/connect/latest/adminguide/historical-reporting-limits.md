

# Historical metrics report limits in Connect Customer
<a name="historical-reporting-limits"></a>

Historical metrics reports have the following limits:

**Service quotas**
+ Historical metrics reports have service quotas, such as **Reports per instance** and **Scheduled reports per instance**. When service quotas are breached, the following error message is displayed: *Report cannot be saved*. For more information about these quotas, see [Connect Customer service quotas](amazon-connect-service-limits.md)

**Data only for active queues**
+ You can get data only for active queues. A queue is inactive if there are no contacts in the queue and no agents available.

**Query data for three days at a time, for the past 2 days**
+ When you create a report that uses 15 minute intervals, you can return data for three days at a time, for the past 35 days. For 30 minute intervals you can return data for only three days at a time, but the data is available based on the retention period of contact records. 

**The availability of historical metric data is based on the retention period of contact records**
+ Historical metrics are based contact records. For the current retention period for contact records, see [Connect Customer feature specifications](feature-limits.md).

**For daily and total intervals**
+ You can select up to 31 days in a single request.

**Cell limit**
+ Historical and scheduled reports limit the quantity of data returned according to the number of cells with data (and not total rows \* columns in the report). A cell missing data is rendered as "-" on the reporting page.
+ Historical reports are limited to 120k cells of data. If the cell limit is exceeded, the data is truncated.
+ Scheduled reports are limited to 200k cells of data. If the cell limit is exceeded, the report fails.