

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Loading data in Amazon Redshift
<a name="t_Loading_data"></a>

There are several ways to load data into an Amazon Redshift database. One popular source of data to load are Amazon S3 files. The following table summarizes some of the methods to use with starting from an Amazon S3 source.


<table>
<thead>
  <tr><th>Method to use</th><th>Description</th><th>When method needed</th></tr>
</thead>
<tbody>
  <tr><td>COPY command</td><td>Runs a batch file ingestion to load data from your Amazon S3 files. This method leverages parallel processing capabilities of Amazon Redshift. For more information, see <a href="t_Loading_tables_with_the_COPY_command.md">Loading tables with the COPY command</a>.</td><td>Should be used when basic data loading requirements to initiate batch file ingestion manually is needed. This method is used mostly with custom and third-party file ingestion pipelines or one-time, or ad hoc, file ingestion workloads.</td></tr>
  <tr><td>COPY... CREATE JOB command (auto-copy)</td><td>Runs your COPY commands automatically when a new file is created on tracked Amazon S3 paths. For more information, see <a href="loading-data-copy-job.md">Create an S3 event integration to automatically copy files from Amazon S3 buckets</a>.</td><td>Should be used when a file ingestion pipeline needs to automatically ingest data when a new file is created on Amazon S3. Amazon Redshift keeps track of ingested files to prevent data duplication. This method requires configuration by Amazon S3 bucket owners.</td></tr>
  <tr><td>Load from data lake queries</td><td>Create external tables to run data lake queries on your Amazon S3 files and then run INSERT INTO command to load results from your data lake queries into local tables. For more information, see <a href="c-spectrum-external-tables.md">External tables for Redshift Spectrum</a>.</td><td>Should be used in any of the following scenarios: <ul><li>Loading from AWS Glue and open table formats (such as Apache Iceberg, Apache Hudi, or Delta Lake).</li><li>Source files need to be ingested partially (for example, needed for running a WHERE clause to ingest particular rows).</li><li>More flexibility needed to ingest particular columns (like running a SELECT command) or doing basic data transformation on the go (such as applying basic operations or calling UDFs on the values from the source file).</li></ul></td></tr>
  <tr><td colspan="3"><b>Other methods that you can consider</b></td></tr>
  <tr><td>Streaming ingestion </td><td>Streaming ingestion provides low-latency, high-speed ingestion of stream data from Amazon Kinesis Data Streams and Amazon Managed Streaming for Apache Kafka into an Amazon Redshift provisioned or Redshift Serverless materialized view. For more information, see <a href="materialized-view-streaming-ingestion-getting-started.md">Getting started with streaming ingestion from Amazon Kinesis Data Streams</a> and <a href="materialized-view-streaming-ingestion-getting-started-MSK.md">Getting started with streaming ingestion from Apache Kafka sources</a>.</td><td>Should be considered for use cases when data is first streamed into files on Amazon S3 and then loaded from Amazon S3. If keeping data on Amazon S3 is not needed, you can often consider streaming your data directly into Amazon Redshift. </td></tr>
  <tr><td>Running data lake queries</td><td>Running queries directly from a data lake table instead of ingesting contents of the table into a local table. For more information, see <a href="c-using-spectrum.md">Amazon Redshift Spectrum</a>.</td><td>Should be used when the use case doesn't require the performance of local table queries in Amazon Redshift.</td></tr>
  <tr><td>Batch loading using Amazon Redshift query editor v2</td><td>You can prepare and run your batch file ingestion workloads visually on Amazon Redshift query editor v2. For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-loading.html#query-editor-v2-loading-data">Loading data from S3</a> in the <i>Amazon Redshift Management Guide</i>.</td><td>Should be used when you want the query editor v2 to prepare COPY statements and you want a visual tool to simplify the COPY statement preparation process.</td></tr>
  <tr><td>Load data from a local file using Amazon Redshift query editor v2</td><td>You can directly upload files from your desktop into Amazon Redshift tables without the need for manually uploading your files into Amazon S3. For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-loading.html#query-editor-v2-loading-data-local">Loading data from a local file setup and workflow</a> in the <i>Amazon Redshift Management Guide</i>.</td><td>Should be used when you need to quickly load files from your local computer for one-time querying purposes. With this method, Amazon Redshift query editor v2 temporarily stores the file on a customer-owned Amazon S3 bucket and runs a copy command using this Amazon S3 path.</td></tr>
</tbody>
</table>


A COPY command is the most efficient way to load a table. You can also add data to your tables using INSERT commands, though it is much less efficient than using COPY. The COPY command is able to read from multiple data files or multiple data streams simultaneously. Amazon Redshift allocates the workload to the Amazon Redshift nodes and performs the load operations in parallel, including sorting the rows and distributing data across node slices.

**Note**  
Amazon Redshift Spectrum external tables are read-only. You can't COPY or INSERT to an external table.

To access data on other AWS resources, Amazon Redshift must have permission to access those resources and to perform the necessary actions to access the data. You can use AWS Identity and Access Management (IAM) to limit the access users have to Amazon Redshift resources and data.

After your initial data load, if you add, modify, or delete a significant amount of data, you should follow up by running a VACUUM command to reorganize your data and reclaim space after deletes. You should also run an ANALYZE command to update table statistics.

**Topics**
+ [Loading tables with the COPY command](t_Loading_tables_with_the_COPY_command.md)
+ [Create an S3 event integration to automatically copy files from Amazon S3 buckets](loading-data-copy-job.md)
+ [Loading tables with DML commands](t_Updating_tables_with_DML_commands.md)
+ [Performing a deep copy](performing-a-deep-copy.md)
+ [Analyzing tables](t_Analyzing_tables.md)
+ [Vacuuming tables](t_Reclaiming_storage_space202.md)
+ [Managing concurrent write operations](c_Concurrent_writes.md)
+ [Tutorial: Loading data from Amazon S3](tutorial-loading-data.md)