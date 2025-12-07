# Creating and working with AWS Glue DataBrew recipe jobs

Use a DataBrew _recipe job_ to clean and normalize the data in a DataBrew
dataset and write the result to an output location of your choice. Running a recipe job
doesn't affect the dataset or the underlying source data. When a job runs, it connects
to the source data in a read-only fashion. The job output is written to an output
location that you define in Amazon S3, the AWS Glue Data Catalog, or a supported JDBC database.

Use the following procedure to create a DataBrew recipe job.

###### To create a recipe job

1. Sign in to the AWS Management Console and open the DataBrew console at
   [https://console.aws.amazon.com/databrew/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. Choose **JOBS** from the navigation pane, choose the
   **Recipe jobs** tab, and then choose **Create
   job**.
3. Enter a name for your job, and then choose **Create a
   recipe job**.
4. For **Job input**, enter details on the job that you want to create:
   the name of the dataset to be processed, and the recipe to use.

A recipe job uses a DataBrew recipe to transform a dataset. To use a recipe, make sure to
publish it first. 5. Configure your job output settings.

Provide a destination for your job output. If you don't have a DataBrew connection configured
for your output destination, configure it first on the **DATASETS** tab as
described in [Supported connections for data sources and outputs](supported-data-connection-sources.md "supported-data-connection-sources.md"). Choose one of the
following output destinations:

    * Amazon S3, with or without AWS Glue Data Catalog support
    * Amazon Redshift, with or without AWS Glue Data Catalog support
    * JDBC
    * Snowflake tables
    * Amazon RDS database tables with AWS Glue Data Catalog support. Amazon RDS database tables support the following
     database engines:




    	+ Amazon Aurora
    	+ MySQL
    	+ Oracle
    	+ PostgreSQL
    	+ Microsoft SQL Server
    * Amazon S3 with AWS Glue Data Catalog support.

For AWS Glue Data Catalog output based on AWS Lake Formation, DataBrew supports only
replacing existing files. In this approach, the files are replaced to
keep your existing Lake Formation permissions intact for your data access role.
Also, DataBrew gives precedence to the Amazon S3 location from the AWS Glue Data Catalog
table. Thus, you can't override the Amazon S3 location when creating a recipe
job.

In some cases, the Amazon S3 location in the job output differs from the Amazon S3 location in the Data
Catalog table. In these cases, DataBrew updates the job definition automatically
with the Amazon S3 location from the catalog table. It does this when you update or
start your existing jobs. 6. For Amazon S3 output destinations only, you have further choices:

    1. Choose one of the available data output formats for Amazon S3, optional
     compression, and an optional custom delimiter. Supported delimiters for
     output files are the same as those for input: comma, colon, semicolon,
     pipe, tab, caret, backslash, and space. For formatting details, see the
     following table.




    | **Format** | **File extension (uncompressed)** | **File extensions (compressed)** |
    | --- | --- | --- |
    | Comma-separated values | `.csv` | `.csv.snappy`, `.csv.gz`,<br>`.csv.lz4`, `csv.bz2`,<br>`.csv.deflate`, `csv.br` |
    | Tab-separated values | `.csv` | `.tsv.snappy`, `.tsv.gz`,<br>`.tsv.lz4`, `tsv.bz2`,<br>`.tsv.deflate`, `tsv.br` |
    | Apache Parquet | `.parquet` | `.parquet.snappy`, `.parquet.gz`,<br>`.parquet.lz4`, `.parquet.lzo`,<br>`.parquet.br` |
    | AWS Glue Parquet | Not supported | `.glue.parquet.snappy` |
    | Apache Avro | `.avro` | `.avro.snappy`, `.avro.gz`,<br>`.avro.lz4`, `.avro.bz2`,<br>`.avro.deflate`, `.avro.br` |
    | Apache ORC | `.orc` | `.orc.snappy`, `.orc.lzo`,<br>`.orc.zlib` |
    | XML | `.xml` | `.xml.snappy`, `.xml.gz`,<br>`.xml.lz4`, `.xml.bz2`,<br>`.xml.deflate`, `.xml.br` |
    | JSON (JSON Lines format only) | `.json` | `.json.snappy`, `.json.gz`,<br>`.json.lz4`, `json.bz2`,<br>`.json.deflate`, `.json.br` |
    | Tableau Hyper | Not supported | Not applicable |
    2. Choose whether to output a single file or multiple files. There are three
     options for file output with Amazon S3:




    	* **Autogenerate files (recommended)** – Has DataBrew determine the optimal
    	 number of output files.
    	* **Single file output** – Causes a single output file to be
    	 generated. This option might result in additional job execution
    	 time because post-processing is required.
    	* **Multiple file output** – Has you specify the number of files for
    	 your job output. Valid values are 2–999. Fewer files than you
    	 specify might be output if column partitioning is used or if the
    	 number of rows in the output is fewer than the number of files
    	 you specify.
    3. (Optional) Choose column partitioning for recipe job output.




    Column partitioning provides another way to partition your recipe job output into multiple
     files. Column partitioning can be used with new or existing Amazon S3 output or with new Data Catalog Amazon S3
     output. It cannot be used with existing Data Catalog Amazon S3 tables. The output files are based on the
     values of column names that you specify. If the column names you specify are unique, the resulting Amazon S3
     folder paths are based on the order of the column names.


    For an example of column partitioning, see [Example of column partitioning](#jobs.recipe-column-partition-example "#jobs.recipe-column-partition-example"), following.

7. (Optional) Choose **Enable encryption for job output** to encrypt the
   job output that DataBrew writes to your output location, and then choose the encryption
   method:
   - **Use SSE-S3 encryption** – The output is
     encrypted using server-side encryption with Amazon S3–managed encryption keys.
   - **Use AWS Key Management Service (AWS KMS)** – The output is encrypted
     using AWS KMS. To use this option, choose the Amazon Resource Name (ARN) of the AWS KMS key
     that you want to use. If you don't have an AWS KMS key, you can create one by choosing
     **Create an AWS KMS key**.

8. For **Access permissions**, choose an AWS Identity and Access Management (IAM) role that allows DataBrew to
   write to your output location. For a location owned by your AWS
   account, you can choose the `AwsGlueDataBrewDataAccessRole`
   service-managed role. Doing this allows DataBrew to access AWS resources that you
   own.
9. On the **Advanced job settings** pane, you can choose more options
   for how your job is to run:
   - **Maximum number of units** – DataBrew processes
     jobs using multiple compute nodes, running in parallel. The default
     number of nodes is 5. The maximum number of nodes is 149.
   - **Job timeout –** If a job takes more than the
     number of minutes that you set here to run, it fails with a timeout
     error. The default value is 2,880 minutes, or 48 hours.
   - **Number of retries** – If a job fails while
     running, DataBrew can try to run it again. By default, the job isn't
     retried.
   - **Enable Amazon CloudWatch Logs for job** – Allows DataBrew to publish
     diagnostic information to CloudWatch Logs. These logs can be useful for
     troubleshooting purposes, or for more details on how the job is
     processed.

10. For **Schedule jobs**, you can apply a DataBrew job schedule so that
    your job runs at a particular time, or on a recurring basis. For more
    information, see [Automating job runs with a schedule](#jobs.scheduling "#jobs.scheduling").
11. When the settings are as you want them, choose **Create
    job**. Or, if you want to run the job immediately, choose **Create and run job**.
    You can monitor your job's progress by checking its status while the job is
    running. When the job run is complete, the status changes to
    **Succeeded**. The job output is now available at your chosen
    output location.

DataBrew saves your job definition, so that you can run the same job later. To rerun a
job, choose **Jobs** from the navigation pane. Choose the job that you
want to work with, and then choose **Run job**.

## Example of column partitioning

As an example of column partitioning, assume that you specify three columns, each
row of which contains one of two possible values. The `Dept` column can
have the value `Admin` or
`Eng`.
The `Staff-type` column can have the value `Part-time` or
`Full-time`. The `Location` column can have the value
`Office1` or `Office2`. The Amazon S3 buckets for your job
output look something like the following.

```
s3://bucket/output-folder/Dept=Admin/Staff-type=Part-time/Area=Office1/jobId_timestamp_part0001.csv
s3://bucket/output-folder/Dept=Admin/Staff-type=Part-time/Location=Office2/jobId_timestamp_part0002.csv
s3://bucket/output-folder/Dept=Admin/Staff-type=Full-time/Location=Office1/jobId_timestamp_part0003.csv
s3://bucket/output-folder/Dept=Admin/Staff-type=Full-time/Location=Office2/jobId_timestamp_part0004.csv
s3://bucket/output-folder/Dept=Eng/Staff-type=Part-time/Location=Office1/jobId_timestamp_part0005.csv
s3://bucket/output-folder/Dept=Eng/Staff-type=Part-time/Location=Office2/jobId_timestamp_part0006.csv
s3://bucket/output-folder/Dept=Eng/Staff-type=Full-time/Location=Office1/jobId_timestamp_part0007.csv
s3://bucket/output-folder/Dept=Eng/Staff-type=Full-time/Location=Office2/jobId_timestamp_part0008.csv
```

## Automating job runs with a schedule

You can rerun DataBrew jobs at any time and also automate DataBrew job runs with a schedule.

###### To rerun a DataBrew job

1. Sign in to the AWS Management Console and open the DataBrew console
   at [https://console.aws.amazon.com/databrew/](https://console.aws.amazon.com/databrew/ "https://console.aws.amazon.com/databrew/").
2. On the navigation pane, choose **Jobs**. Choose the job that you want
   to run, and then choose **Run job**.

To run a DataBrew job at a particular time, or on a recurring basis, create a DataBrew job
schedule. You can then set up your job to run according to the schedule.

###### To create a DataBrew job schedule

1. On the DataBrew console's navigation pane, choose
   **Jobs**. Choose the **Schedules** tab,
   and choose **Add schedule**.
2. Enter a name for your schedule, and then choose a value for **Run
   frequency**:
   - **Recurring** – Choose how frequently that you want
     the job to run (for example, every 12 hours). Then choose which day or days to run the
     job on. Optionally, you can enter the time of day when the job runs.
   - **At a particular time** – Enter the time of day when you want the job
     to run. Then choose which day or days to run the job on.
   - **Enter CRON** – Define the job schedule by entering a valid cron
     expression. For more information, see [Working with cron expressions for recipe jobs](#jobs.cron "#jobs.cron").

3. When the settings are as you want them, choose
   **Save**.

###### To associate a job with a schedule

1. On the navigation pane, choose **Jobs**.
2. Choose the job that you want to work with, and then for **Actions**, choose **Edit.**.
3. On the **Schedule jobs** pane, choose **Associate
   schedule**. Choose the name of the schedule that you want to
   use.
4. When the settings are as you want them, choose
   **Save**.

## Working with cron expressions for recipe jobs

Cron expressions have six required fields, which are separated by white space. The
syntax is as follows.

```
`Minutes` `Hours` `Day-of-month` `Month` `Day-of-week` `Year`
```

In the preceding syntax, the following values and wildcards are used for the indicated
fields.

| **Fields**   | **Values**      | **Wildcards**         |
| ------------ | --------------- | --------------------- |
| Minutes      | 0–59            | ,<br>• \<br>• /       |
| Hours        | 0–23            | ,<br>• \<br>• /       |
| Day-of-month | 1–31            | ,<br>• \<br>• ? / L W |
| Month        | 1–12 or JAN-DEC | ,<br>• \<br>• /       |
| Day-of-week  | 1–7 or SUN-SAT  | ,<br>• \<br>• ? / L   |
| Year         | 1970–2199       | ,<br>• \<br>• /       |

Use these wildcards as follows:

- The **,** (comma) wildcard includes additional values. In
  the `Month` field, `JAN,FEB,MAR` includes January,
  February, and March.
- The **-** (en dash) wildcard specifies ranges. In the
  `Day` field, 1–15 includes days 1 through 15 of the
  specified month.
- The **\*** (asterisk) wildcard includes all values in the
  field. In the `Hours` field, **\*** includes
  every hour.
- The **/** (slash) wildcard specifies increments. In the
  `Minutes` field, you can enter `1/10` to
  specify every 10th minute, starting from the first minute of the hour (for
  example, the 11th, 21st, and 31st minute).
- The **?** (question mark) wildcard specifies one or another.
  For example, suppose that in the `Day-of-month` field you enter
  **7**. If you didn't care what day of the week the
  seventh was, you can then enter **?** in the
  `Day-of-week` field.
- The **L** wildcard in the `Day-of-month` or
  `Day-of-week` field specifies the last day of the month or
  week.
- The **W** wildcard in the `Day-of-month` field
  specifies a weekday. In the `Day-of-month` field, `3W`
  specifies the day closest to the third weekday of the month.

These fields and values have the following limitations:

- You can't specify the `Day-of-month` and `Day-of-week`
  fields in the same cron expression. If you specify a value in one of the fields,
  you must use a **?** (question mark) in the other.
- Cron expressions that lead to rates faster than 5 minutes aren't supported.

When creating a schedule, you can use the following sample cron strings.

| Minutes | Hours | Day of month | Month | Day of week | Year | Meaning                                                                        |
| ------- | ----- | ------------ | ----- | ----------- | ---- | ------------------------------------------------------------------------------ |
| 0       | 10    | \*           | \*    | ?           | \*   | Run at 10:00 AM (UTC) every day                                                |
| 15      | 12    | \*           | \*    | ?           | \*   | Run at 12:15 PM (UTC) every day                                                |
| 0       | 18    | ?            | \*    | MON-FRI     | \*   | Run at 6:00 PM (UTC) every Monday through Friday                               |
| 0       | 8     | 1            | \*    | ?           | \*   | Run at 8:00 AM (UTC) every first day of the month                              |
| 0/15    | \*    | \*           | \*    | ?           | \*   | Run every 15 minutes                                                           |
| 0/10    | \*    | ?            | \*    | MON-FRI     | \*   | Run every 10 minutes Monday through Friday                                     |
| 0/5     | 8–17  | ?            | \*    | MON-FRI     | \*   | Run every 5 minutes Monday through Friday between 8:00 AM and<br>5:55 PM (UTC) |

For example, you can use the following cron expression to run a job every day at 12:15
UTC.

```
15 12 * * ? *
```

## Deleting jobs and job schedules

If you no longer need a job or job schedule, you can delete it.

###### To delete a job

1. On the navigation pane, choose **Jobs**.
2. Choose the job that you want to delete, and then for
   **Actions**, choose **Delete.**.

###### To delete a job schedule

1. On the navigation pane, choose **Jobs**, and then choose the **Schedules** tab.
2. Choose the schedule that you want to delete, and then for
   **Actions**, choose **Delete.**.
