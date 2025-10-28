# Getting started with EMR Serverless from the console

This section describes working with EMR Serverless, including creating an EMR Studio. It also describes how to submit job
runs and view logs.

###### Steps to complete

- [Step 1: Create an EMR Serverless
  application](#gs-application-console "#gs-application-console")
- [Step 2: Submit a job run or interactive
  workload](#gs-job-run-console "#gs-job-run-console")
- [Step 3: View application UI and logs](#gs-output-console "#gs-output-console")
- [Step 4: Clean up](#gs-cleanup-console "#gs-cleanup-console")

## Step 1: Create an EMR Serverless

application

Create a new application with EMR Serverless as follows.

1. Sign in to the AWS Management Console and open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. In the left navigation pane, choose **EMR Serverless** to navigate
   to the EMR Serverless landing page.
3. To create or manage EMR Serverless applications, you need the EMR Studio
   UI.
   - If you already have an EMR Studio in the AWS Region where you want to
     create an application, then select **Manage applications** to
     navigate to your EMR Studio, or select the studio that you want to use.
   - If you don't have an EMR Studio in the AWS Region where you want to create
     an application, choose **Get started** and then Choose
     **Create and launch Studio**. EMR Serverless creates a
     EMR Studio for you so that you can create and manage applications.

4. In the **Create studio** UI that opens in a new tab, enter the
   name, type, and release version for your application. If you only want to run batch
   jobs, select **Use default settings for batch jobs only**. For
   interactive workloads, select **Use default settings for interactive
   workloads**. You can also run batch jobs on interactive-enabled applications
   with this option. If you need to, you can change these settings later.

For more information, see [Create a
studio](../ManagementGuide/emr-studio-create-studio.md "../ManagementGuide/emr-studio-create-studio.md"). 5. Select **Create application** to create your first application.

Continue to the next section [Step 2: Submit a job run or interactive
workload](#gs-job-run-console "#gs-job-run-console") to submit a job run or interactive workload.

## Step 2: Submit a job run or interactive

workload

Spark job run
In this tutorial, we use a PySpark script to compute the number of occurrences of
unique words across multiple text files. A public, read-only S3 bucket stores both the
script and the dataset.

###### To run a Spark job

1. Upload the sample script `wordcount.py` into your new bucket with
   the following command.

```
aws s3 cp s3://us-east-1.elasticmapreduce/emr-containers/samples/wordcount/scripts/wordcount.py s3://`amzn-s3-demo-bucket`/scripts/
```

2. Completing [Step 1: Create an EMR Serverless
   application](#gs-application-console "#gs-application-console") takes you to the **Application
   details** page in EMR Studio. There, choose the **Submit
   job** option.
3. On the **Submit job** page, complete the following.
   - In the **Name** field, enter the name that you want to
     call your job run.
   - In the **Runtime role** field, enter the name of the role
     that you created in [Create a job runtime role](getting-started.md#gs-runtime-role "getting-started.md#gs-runtime-role").
   - In the **Script location** field, enter
     `s3://`amzn-s3-demo-bucket`/scripts/wordcount.py`
     as the S3 URI.
   - In the **Script arguments** field, enter
     `["s3://`amzn-s3-demo-bucket`/emr-serverless-spark/output"]`.
   - In the **Spark properties** section, choose
     **Edit as text** and enter the following
     configurations.

   ```
   --conf spark.executor.cores=1 --conf spark.executor.memory=4g --conf spark.driver.cores=1 --conf spark.driver.memory=4g --conf spark.executor.instances=1
   ```

4. To start the job run, choose **Submit job** .
5. In the **Job runs** tab, you should see your new job run with
   a **Running** status.

Hive job run
In this part of the tutorial, we create a table, insert a few records, and run a
count aggregation query. To run the Hive job, first create a file that contains all
Hive queries to run as part of single job, upload the file to S3, and specify this S3
path when starting the Hive job.

###### To run a Hive job

1. Create a file called `hive-query.ql` that contains all the queries
   that you want to run in your Hive job.

```
create database if not exists emrserverless;
use emrserverless;
create table if not exists test_table(id int);
drop table if exists Values__Tmp__Table__1;
insert into test_table values (1),(2),(2),(3),(3),(3);
select id, count(id) from test_table group by id order by id desc;
```

2. Upload `hive-query.ql` to your S3 bucket with the following
   command.

```
aws s3 cp hive-query.ql s3://`amzn-s3-demo-bucket`/emr-serverless-hive/query/hive-query.ql
```

3. Completing [Step 1: Create an EMR Serverless
   application](#gs-application-console "#gs-application-console") takes you to the **Application
   details** page in EMR Studio. There, choose the **Submit
   job** option.
4. On the **Submit job** page, complete the following.
   - In the **Name** field, enter the name that you want to
     call your job run.
   - In the **Runtime role** field, enter the name of the role
     that you created in [Create a job runtime role](getting-started.md#gs-runtime-role "getting-started.md#gs-runtime-role").
   - In the **Script location** field, enter
     `s3://`amzn-s3-demo-bucket`/emr-serverless-hive/query/hive-query.ql`
     as the S3 URI.
   - In the **Hive properties** section, choose **Edit
     as text**, and enter the following configurations.

   ```
   --hiveconf hive.log.explain.output=false
   ```

   - In the **Job configuration** section, choose
     **Edit as JSON**, and enter the following JSON.

   ```
   {
      "applicationConfiguration":
      [{
          "classification": "hive-site",
             "properties": {
                 "hive.exec.scratchdir": "s3://`amzn-s3-demo-bucket`/emr-serverless-hive/hive/scratch",
                 "hive.metastore.warehouse.dir": "s3://`amzn-s3-demo-bucket`/emr-serverless-hive/hive/warehouse",
                 "hive.driver.cores": "2",
                 "hive.driver.memory": "4g",
                 "hive.tez.container.size": "4096",
                 "hive.tez.cpu.vcores": "1"
              }
       }]
   }
   ```

5. To start the job run, choose **Submit job**.
6. In the **Job runs** tab, you should see your new job run with
   a **Running** status.

Interactive workload
With Amazon EMR 6.14.0 and higher, you can use notebooks that are hosted in
EMR Studio to run interactive workloads for Spark in EMR Serverless. For more
information including permissions and prerequisites, see [Run interactive workloads with EMR Serverless through
EMR Studio](interactive-workloads.md "interactive-workloads.md").

Once you've created your application and set up the required permissions, use the
following steps to run an interactive notebook with EMR Studio:

1. Navigate to the **Workspaces** tab in EMR Studio. If you
   still need to configure an Amazon S3 storage location and [EMR Studio
   service role](../ManagementGuide/emr-studio-service-role.md "../ManagementGuide/emr-studio-service-role.md"), select the **Configure studio** button in
   the banner at the top of the screen.
2. To access a notebook, select a Workspace or create a new Workspace. Use
   **Quick launch** to open your Workspace in a new tab.
3. Go to the newly opened tab. Select the **Compute** icon from
   the left navigation. Select EMR Serverless as the **Compute
   type**.
4. Select the interactive-enabled application that you created in the previous
   section.
5. In the **Runtime role** field, enter the name of the IAM
   role that your EMR Serverless application can assume for the job run. To learn
   more about runtime roles, see [Job
   runtime roles](security-iam-runtime-role.md "security-iam-runtime-role.md") in the _Amazon EMR Serverless User
   Guide_.
6. Select **Attach**. This may take up to a minute. The page
   will refresh when attached.
7. Pick a kernel and start a notebook. You can also browse example notebooks on
   EMR Serverless and copy them to your Workspace. To access the example notebooks,
   navigate to the **`{...}`** menu in the left
   navigation and browse through notebooks that have `serverless` in the
   notebook file name.
8. In the notebook, you can access the driver log link and a link to the Apache
   Spark UI, a real-time interface that provides metrics to monitor your job. For
   more information, see [Monitoring
   EMR Serverless applications and jobs](app-job-metrics.md "app-job-metrics.md") in the
   _Amazon EMR Serverless User Guide_.

When you attach an application to an Studio workspace, the application start
triggers automatically if it's not already running. You can also pre-start the
application and keep it ready before you attach it to the workspace.

## Step 3: View application UI and logs

To view the application UI, first identify the job run. An option for **Spark
UI** or **Hive Tez UI** is available in the first row of options
for that job run, based on the job type. Select the appropriate option.

If you chose the Spark UI, choose the **Executors** tab to view the
driver and executors logs. If you chose the Hive Tez UI, choose the **All
Tasks** tab to view the logs.

Once the job run status shows as **Success**, you can view the output
of the job in your S3 bucket.

## Step 4: Clean up

While the application you created should auto-stop after 15 minutes of inactivity, we
still recommend that you release resources that you don't intend to use again.

To delete the application, navigate to the **List applications** page.
Select the application that you created and choose **Actions → Stop** to
stop the application. After the application is in the `STOPPED` state, select the
same application and choose **Actions → Delete**.

For more examples of running Spark and Hive jobs, see [Using Spark configurations when you run EMR Serverless jobs](jobs-spark.md "jobs-spark.md") and [Using Hive configurations when you run EMR Serverless jobs](jobs-hive.md "jobs-hive.md").
