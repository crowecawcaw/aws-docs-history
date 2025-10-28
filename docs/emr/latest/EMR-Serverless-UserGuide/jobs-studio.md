# Running jobs from the EMR Studio console

You can submit job runs to EMR Serverless applications and access the jobs from the
EMR Studio console. To create or navigate to your EMR Serverless application on the
EMR Studio console, follow the instructions in [Getting started
from the console](getting-started.md#gs-console "getting-started.md#gs-console").

## Submit a job

On the **Submit job** page, submit a job to an EMR Serverless
application as follows.

Spark

1. In the **Name** field, enter a name for your job run.
2. In the **Runtime role** field, enter the name of the IAM
   role that your EMR Serverless application can assume for the job run. To learn
   more about runtime roles, refer to [Job runtime roles for Amazon EMR Serverless](security-iam-runtime-role.md "security-iam-runtime-role.md").
3. In the **Script location** field, enter the Amazon S3 location for
   the script or JAR that you want to run. For Spark jobs, the script can be a Python
   (`.py`) file or a JAR (`.jar`) file.
4. If your script location is a JAR file, enter the class name that is the entry
   point for the job in the **Main class** field.
5. (Optional) Enter values for the remaining fields.
   - **Script arguments** — Enter any arguments that
     you want to pass to your main JAR or Python script. Your code reads these
     parameters. Separate each argument in the array by a comma.
   - **Spark properties** — Expand the Spark properties
     section and enter any Spark configuration parameters in this field.

   ###### Note

   If you specify Spark driver and executor sizes, take memory
   overhead into account. Specify memory overhead values in the properties
   `spark.driver.memoryOverhead` and
   `spark.executor.memoryOverhead`. Memory overhead has a default
   value of 10% of container memory, with a minimum of 384 MB. The executor
   memory and the memory overhead together can't exceed the worker memory. For
   example, the maximum `spark.executor.memory` on a 30 GB worker
   must be 27 GB.
   - **Job configuration** — Specify any job
     configuration in this field. You can use these job configurations to override
     the default configurations for applications.
   - **Additional settings** — Active or deactivate the
     AWS Glue Data Catalog as a metastore and modify application log settings. To learn more
     about metastore configurations, refer to [Metastore configuration for EMR Serverless](metastore-config.md "metastore-config.md"). To learn more about application logging
     options, refer to [Storing logs](logging.md "logging.md").
   - **Tags** — Assign custom tags to the
     application.

6. Choose **Submit job**.

Hive

1. In the **Name** field, enter a name for your job run.
2. In the **Runtime role** field, enter the name of the IAM
   role that your EMR Serverless application can assume for the job run.
3. In the **Script location** field, enter the Amazon S3 location for
   the script or JAR that you want to run. For Hive jobs, the script must be a Hive
   (`.sql`) file.
4. (Optional) Enter values for the remaining fields.
   - **Initialization script location** – Enter the
     location of the script that initializes tables before the Hive script
     runs.
   - **Hive properties** – Expand the Hive properties
     section and enter any Hive configuration parameters in this field.
   - **Job configuration** – Specify any job
     configuration. You can use these job configurations to override the default
     configurations for applications. For Hive jobs,
     `hive.exec.scratchdir` and
     `hive.metastore.warehouse.dir` are required properties in the
     `hive-site` configuration.

   ```
   {
       "applicationConfiguration": [
           {
               "classification": "hive-site",
               "configurations": [],
               "properties": {
                   "hive.exec.scratchdir": "s3://`DOC-EXAMPLE_BUCKET`/hive/scratch",
                   "hive.metastore.warehouse.dir": "s3://`DOC-EXAMPLE_BUCKET`/hive/warehouse"
               }
           }
       ],
       "monitoringConfiguration": {}
   }
   ```

   - **Additional settings** — Activate or deactivate
     the AWS Glue Data Catalog as a metastore and modify application log settings. To learn
     more about metastore configurations, refer to [Metastore configuration for EMR Serverless](metastore-config.md "metastore-config.md"). To learn more about application logging
     options, refer to [Storing logs](logging.md "logging.md").
   - **Tags** — Assign any custom tags to the
     application.

5. Choose **Submit job**.

## Access job runs

From the **Job runs** tab on an application’s
**Details** page, access job runs and perform the following actions
for job runs.

**Cancel job** — To cancel a job run that is in the
`RUNNING` state, choose this option. To learn more about job run transitions,
refer to [Job run states](job-states.md "job-states.md").

**Clone job** — To clone a previous job run and resubmit it,
choose this option.
