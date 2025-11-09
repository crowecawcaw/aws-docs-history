# View query results with the console

After your query finishes, you can view its results. The results of a query are
available for seven days after the query finishes. You can view results for the active
query on the **Query results** tab, or you can access results for all
recent queries on the **Results history** tab on the
**Lake** home page.

Query results can change from older runs of a query to newer ones, as later events in
the query period can be logged between queries.

When you save query results, the query results may display in the CloudTrail console before they
are viewable in the S3 bucket since CloudTrail delivers the query results after the query scan
completes. While most queries complete within a few minutes, depending on the size of
your event data store, it can take considerably longer for CloudTrail to deliver query results
to your S3 bucket. CloudTrail delivers the query results to the S3 bucket in compressed gzip
format.  On average, after the query scan completes you can expect a latency of 60 to 90
seconds for every GB of data delivered to the S3 bucket. For more information about
finding and downloading saved query results, see [Download saved query results](view-download-cloudtrail-lake-query-results.md "view-download-cloudtrail-lake-query-results.md").

###### Note

Queries that run for longer than one hour might time out. You can still get
partial results that were processed before the query timed out. CloudTrail does not
deliver partial query results to an S3 bucket. To avoid a time out, you can refine
your query to limit the amount of data scanned by specifying a narrower time
range.

###### To view query results

1. Choose the **Query results** tab on the query editor if it is not already selected. On the **Query results** tab for an active query, each row
   represents an event result that matched the query. Filter results by entering
   all or part of an event field value in the search bar.
   To copy an event, choose the event you want to copy and then choose **Copy**.
2. (Optional) Choose **Summarize results** to generate a natural language summary of the query results. The summary is provided in English. This option uses
   generative artificial intelligence (generative AI) to produce the summary. For more information about this option, see [Summarize query results in natural language](query-results-summary.md "query-results-summary.md").

You can provide feedback about the summary by choosing the thumbs up or thumbs down
button that appears below the generated summary.

###### Note

The query summarization feature is in preview release for
CloudTrail Lake and is subject to change. This feature is available in the following regions: Asia Pacific (Tokyo), US East (N. Virginia), and US West (Oregon). 3. On the **Command output** tab, view metadata about the query
that was run, such as the event data store ID, run time, number of results
scanned, and whether or not the query was successful. If you saved the query
results to an Amazon S3 bucket, the metadata also includes a link to the S3 bucket
containing the saved query results.
