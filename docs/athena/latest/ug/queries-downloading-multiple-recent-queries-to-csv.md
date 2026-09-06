

# Download multiple recent queries to a CSV file
<a name="queries-downloading-multiple-recent-queries-to-csv"></a>

You can use the **Recent queries** tab of the Athena console to export one or more recent queries to a CSV file in order to view them in tabular format. The downloaded file contains not the query results, but the SQL query string itself and other information about the query. Exported fields include the execution ID, query string contents, query start time, status, run time, amount of data scanned, query engine version used, and encryption method. You can export a maximum of 500 recent queries, or a filtered maximum of 500 queries using criteria that you enter in the search box.

**To export one or more recent queries to a CSV file**

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. Choose **Recent queries**.

1. (Optional) Use the search box to filter for the recent queries that you want to download.

1. Choose **Download CSV**.  
![Choose Download CSV.](http://docs.aws.amazon.com/athena/latest/ug/images/querying-recent-queries-csv.png)

1. At the file save prompt, choose **Save**. The default file name is `Recent Queries` followed by a timestamp (for example, `Recent Queries 2022-12-05T16 04 27.352-08 00.csv`)