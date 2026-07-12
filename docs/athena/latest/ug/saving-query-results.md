# Download query results files using the Athena console

You can download the query results CSV file from the query pane immediately after you
run a query. You can also download query results from recent queries from the
**Recent queries** tab.

###### Note

Athena query result files are data files that contain information that can be
configured by individual users. Some programs that read and analyze this data can
potentially interpret some of the data as commands (CSV injection). For this reason,
when you import query results CSV data to a spreadsheet program, that program might
warn you about security concerns. To keep your system secure, you should always
choose to disable links or macros from downloaded query results.

###### To run a query and download the query results

1. Enter your query in the query editor and then choose
   **Run**.

When the query finishes running, the **Results** pane shows
the query results. 2. To download a CSV file of the query results, choose **Download
results** above the query results pane. Depending on your browser
and browser configuration, you may need to confirm the download.

![Saving query results to a .csv file in the Athena console.](images/getting-started-query-results-download-csv.png)

###### To download a query results file for an earlier query

1. Choose **Recent queries**.

![Choose Recent queries to view previous queries.](images/getting-started-recent-queries.png) 2. Use the search box to find the query, select the query, and then choose
**Download results**.

###### Note

You cannot use the **Download results** option to
retrieve query results that have been deleted manually, or retrieve query
results that have been deleted or moved to another location by Amazon S3 [lifecycle rules](../../../AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.md "../../../AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.md").

![Choose Recent queries to find and download previous query results.](images/querying-recent-queries-tab-download.png)
