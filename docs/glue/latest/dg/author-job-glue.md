# Building visual ETL jobs

## Build visual ETL jobs with AWS Glue Studio

AWS Glue Studio provides a visual interface for creating, running, and monitoring Extract/Transform/Load (ETL) jobs in AWS Glue.
A job in AWS Glue consists of the business logic that performs extract, transform, and load
(ETL) work. With AWS Glue Studio, you can visually compose data
transformation workflows and seamlessly run them on AWS Glue's Apache Spark-based serverless ETL engine. You can create jobs that move and
transform data between various data stores and streams using a drag-and-drop interface without having to learn Spark or write code.

An AWS Glue job encapsulates a script that connects to your source data, processes it, and then
writes it out to your data target. Typically, a job runs extract, transform, and load (ETL) scripts. Jobs can
run scripts designed for Apache Spark and Ray runtime environments. Jobs can also run general-purpose Python
scripts (Python shell jobs.) AWS Glue triggers can start jobs based on a
schedule or event, or on demand. You can monitor job runs to understand runtime metrics such as completion
status, duration, and start time.

You can use scripts that AWS Glue generates or you can provide your own. With a source schema and
target location or schema, the AWS Glue Studio code generator can automatically create an Apache Spark API
(PySpark) script. You can use this script as a starting point and edit it to meet your goals.

AWS Glue can write output files in several data formats. Each job type may support different
output formats. For some data formats, common compression formats can be written.

### Managing AWS Glue Jobs in the AWS Console

To view existing jobs, sign in to the AWS Management Console and open the AWS Glue console at
[https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/"). Then choose the **Jobs** tab in AWS Glue. The
**Jobs** list displays the location of the script that is associated
with each job, when the job was last modified, and the current job bookmark option.

You can create jobs in the **ETL** section of the AWS Glue
console. While creating a new job, or after you have saved your job, you can use can AWS Glue Studio to modify
your ETL jobs. You can do this by editing the nodes in the visual editor or by editing the job
script in developer mode. You can also add and remove nodes in the visual editor to create more
complicated ETL jobs.

### Next steps for creating a job in AWS Glue Studio

You use the visual job editor to configure nodes for your job. Each node
represents an action, such as reading data from the source location or applying a transform to
the data. Each node you add to your job has properties that provide information about
either the data location or the transform.

The next steps for creating and managing your jobs are:

- [Starting visual ETL jobs in AWS Glue Studio](edit-nodes-chapter.md "edit-nodes-chapter.md")
- [View the job script](managing-jobs-chapter.md#view-job-script "managing-jobs-chapter.md#view-job-script")
- [Modify the job properties](managing-jobs-chapter.md#edit-jobs-properties "managing-jobs-chapter.md#edit-jobs-properties")
- [Save the job](managing-jobs-chapter.md#save-job "managing-jobs-chapter.md#save-job")
- [Start a job run](managing-jobs-chapter.md#start-jobs "managing-jobs-chapter.md#start-jobs")
- [View information for recent job runs](managing-jobs-chapter.md#view-job-run-details "managing-jobs-chapter.md#view-job-run-details")
- [Accessing the job monitoring
  dashboard](view-job-runs.md#monitoring-accessing-dashboard "view-job-runs.md#monitoring-accessing-dashboard")

## Build visual ETL flows with Amazon SageMaker

With an Amazon SageMaker Unified Studio workflow, you can set up and run a series of tasks in Amazon SageMaker Unified Studio.
Amazon SageMaker Unified Studio workflows use Apache Airflow to model data processing procedures and orchestrate your Amazon SageMaker Unified
Studio code artifacts. For more information, see
[Using workflows in Amazon SageMaker Unified Studio](../../../sagemaker-unified-studio/latest/userguide/workflow-orchestration.md "../../../sagemaker-unified-studio/latest/userguide/workflow-orchestration.md") .
