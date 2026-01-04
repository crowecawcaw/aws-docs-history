# Creating and working with AWS Glue DataBrew profile jobs

_Profile jobs_ run a series of evaluations on a
dataset and output the results to Amazon S3. The information that data profiling gathers
helps you understand your dataset and decide what kind of data preparation steps you
might want to run in your recipe jobs.

The simplest way to run a profile job is using the default DataBrew settings. You can
configure your profile job before running it so that it returns just the information
that you want.

Use the following procedure to create a DataBrew profile job.

###### To create a profile job

1. Sign in to the AWS Management Console and open the DataBrew console at [https://console.aws.amazon.com/databrew/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. Choose **JOBS** from the navigation pane, choose the
   **Profile jobs** tab, and then choose **Create
   job**.
3. Enter a name for your job, and then choose **Create a
   profile job**.
4. For **Job input**, provide the name of the
   dataset to be profiled.
5. (Optional) Configure the following on the **Data profile configurations**
   pane:
   - **Dataset level configurations** – Configure
     details of your profile job for all columns in your dataset.

   Optionally, you can turn on the ability to detect and count duplicate
   rows in the dataset. You can also choose **Enable
   correlations matrix** and select columns to see how closely
   the values in multiple columns are related. For details of the
   statistics that you can configure at the dataset level, see [Configurable statistics at the dataset
   level](profile.md#statistics.table01 "profile.md#statistics.table01").
   You can configure statistics on the DataBrew console, or using the DataBrew
   API or AWS SDKs.
   - **Column level configurations** – Using
     **Default profile configuration
     settings**, you can select the columns to include in your
     profile job. Use **Add configuration
     override** to select the columns for which to limit the
     number of statistics gathered, or override the default configuration of
     certain statistics. For details of the statistics that you can configure
     at the column level, see [Configurable statistics at the column
     level](profile.md#statistics.table02 "profile.md#statistics.table02"). You can configure statistics
     on the DataBrew console, or using the DataBrew API or AWS SDKs.

   Be sure that any configuration overrides that you specify apply to
   columns that you included in your profile job. If there are conflicts
   between different overrides that you configured for a column, the last
   conflicting override has priority.

6. (Optional) You can create **Data quality rules** and apply additional rulesets associated with this dataset or remove already applied ones.
   For more information on data quality validation, see [Validating data quality in AWS Glue DataBrew](profile.md "profile.md").
7. On the **Advanced job settings** pane, you can choose more options
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
   - **Enable Amazon CloudWatch Logs for job** –
     Allows DataBrew to publish diagnostic information to CloudWatch Logs. These logs can
     be useful for troubleshooting purposes, or for more details on how the
     job is processed.

8. For **Associated Schedule**, you can apply a DataBrew job schedule so that
   your job runs at a particular time, or on a recurring basis. For more
   information, see [Automating job runs with a schedule](jobs.md#jobs.scheduling "jobs.md#jobs.scheduling").
9. When the settings are as you want them, choose **Create
   job**. Or, if you want to run the job immediately, choose **Create and run job**.
