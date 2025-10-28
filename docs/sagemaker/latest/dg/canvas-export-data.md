# Export data

Export data to apply the transforms from your data flow to the full imported dataset.
You can export any node in your data flow to the following locations:

- SageMaker Canvas dataset
- Amazon S3
  If you want to train models in Canvas, you can export your full, transformed
  dataset as a Canvas dataset. If you want to use your transformed data in machine
  learning workflows external to SageMaker Canvas, you can export your dataset to Amazon S3.

## Export to a Canvas

dataset

Use the following procedure to export a SageMaker Canvas dataset from a node in your data
flow.

###### To export a node in your flow as a SageMaker Canvas dataset

1. Navigate to your data flow.
2. Choose the ellipsis icon next to the node that you're exporting.
3. In the context menu, hover over **Export**, and then
   select **Export data to Canvas dataset**.
4. In the **Export to Canvas dataset** side panel, enter
   a **Dataset name** for the new dataset.
5. Leave the **Process entire dataset** option selected if
   you want SageMaker Canvas to process and save your full dataset. Turn this option off
   to only apply the transforms to the sample data you are working with in your
   data flow.
6. Choose **Export**.

You should now be able to go to the **Datasets** page of the
Canvas application and see your new dataset.

## Export to Amazon S3

When exporting your data to Amazon S3, you can scale to transform and process data of
any size. Canvas automatically processes your data locally if the application's
memory can handle the size of your dataset. If your dataset size exceeds the local
memory capacity of 5 GB, then Canvas initiates a remote job on your behalf to
provision additional compute resources and process the data more quickly. By
default, Canvas uses Amazon EMR Serverless to run these remote jobs. However, you
can manually configure Canvas to use either EMR Serverless or a SageMaker Processing
job with your own settings.

###### Note

When running an EMR Serverless job, by default the job inherits the IAM
role, KMS key settings, and tags of your Canvas application.

The following summarizes the options for remote jobs in Canvas:

- **EMR Serverless**: This is the default
  option that Canvas uses for remote jobs. EMR Serverless automatically
  provisions and scales compute resources to process your data so that you
  don't have to worry about choosing the right compute resources for your
  workload. For more information about EMR Serverless, see the [EMR Serverless User Guide](../../../emr/latest/EMR-Serverless-UserGuide/emr-serverless.md "../../../emr/latest/EMR-Serverless-UserGuide/emr-serverless.md").
- **SageMaker Processing**: SageMaker Processing jobs
  offer more advanced options and granular control over the compute resources
  used to process your data. For example, you can specify the type and count
  of the compute instances, configure the job in your own VPC and control
  network access, automate processing jobs, and more. For more information
  about automating processing jobs see [Create a schedule to automatically
  process new data](canvas-data-export-schedule-job.md "canvas-data-export-schedule-job.md"). For more general
  information about SageMaker Processing jobs, see [Data transformation
  workloads with SageMaker Processing](processing-job.md "processing-job.md").

The following file types are supported when exporting to Amazon S3:

- CSV
- Parquet

To get started, review the following prerequisites.

### Prerequisites for

EMR Serverless jobs

To create a remote job that uses EMR Serverless resources, you must have the
necessary permissions. You can grant permissions either through the
Amazon SageMaker AI domain or user profile settings, or you can manually configure your
user's AWS IAM role. For instructions on how to grant users permissions to
perform large data processing, see
[Grant Users Permissions to Use Large Data
across the ML Lifecycle](canvas-large-data-permissions.md "canvas-large-data-permissions.md").

If you don't want to configure these policies but still need to process large
datasets through Data Wrangler, you can alternatively use a SageMaker Processing job.

Use the following procedures to export your data to Amazon S3. To configure a
remote job, follow the optional advanced steps.

###### To export a node in your flow to Amazon S3

1. Navigate to your data flow.
2. Choose the ellipsis icon next to the node that you're exporting.
3. In the context menu, hover over **Export**, and then
   select **Export data to Amazon S3**.
4. In the **Export to Amazon S3** side panel, you can change the
   **Dataset name** for the new dataset.
5. For the **S3 location**, enter the Amazon S3 location to which
   you want to export the dataset. You can enter the S3 URI, alias, or ARN of
   the S3 location or S3 access point. For more information access points, see
   [Managing data access
   with Amazon S3 access points](../../../AmazonS3/latest/userguide/access-points.md "../../../AmazonS3/latest/userguide/access-points.md") in the _Amazon S3 User
   Guide_.
6. (Optional) For the **Advanced settings**, specify values
   for the following fields:
   1. **File type** – The file format of your
      exported data.
   2. **Delimiter** – The delimiter used to
      separate values in the file.
   3. **Compression** – The compression method
      used to reduce the file size.
   4. **Number of partitions** – The number of
      dataset files that Canvas writes as the output of the
      job.
   5. **Choose columns** – You can choose a
      subset of columns from the data to include in the partitions.

7. Leave the **Process entire dataset** option selected if
   you want Canvas to apply your data flow transforms to your entire
   dataset and export the result. If you deselect this option, Canvas only
   applies the transforms to the sample of your dataset used in the interactive
   Data Wrangler data flow.

###### Note

If you only export a sample of your data, Canvas processes your
data in the application and doesn't create a remote job for you. 8. Leave the **Auto job configuration** option selected if
you want Canvas to automatically determine whether to run the job using
Canvas application memory or an EMR Serverless job. If you deselect
this option and manually configure your job, then you can choose to use
either an EMR Serverless or a SageMaker Processing job. For instructions on how
to configure an EMR Serverless or a SageMaker Processing job, see the section
after this procedure before you export your data. 9. Choose **Export**.

The following procedures show how to manually configure the remote job settings
for either EMR Serverless or SageMaker Processing when exporting your full dataset to
Amazon S3.

EMR Serverless
To configure an EMR Serverless job while exporting to Amazon S3, do the
following:

1. In the Export to Amazon S3 side panel, turn off the **Auto
   job configuration** option.
2. Select **EMR Serverless**.
3. For **Job name**, enter a name for your
   EMR Serverless job. The name can contain letters, numbers,
   hyphens, and underscores.
4. For **IAM role**, enter the user's IAM
   execution role. This role should have the required permissions
   to run EMR Serverless applications. For more information, see
   [Grant Users Permissions to Use Large Data
   across the ML Lifecycle](canvas-large-data-permissions.md "canvas-large-data-permissions.md").
5. (Optional) For **KMS key**, specify the key
   ID or ARN of an AWS KMS key to encrypt the job logs. If you
   don't enter a key, Canvas uses a default key for
   EMR Serverless.
6. (Optional) For **Monitoring configuration**,
   enter the name of an Amazon CloudWatch Logs log group to which you want to
   publish your logs.
7. (Optional) For **Tags**, add metadata tags to
   the EMR Serverless job consisting of key-value pairs. These
   tags can be used to categorize and search for jobs.
8. Choose **Export** to start the job.

SageMaker Processing
To configure a SageMaker Processing job while exporting to Amazon S3, do the
following:

1. In the **Export to Amazon S3** side panel, turn
   off the **Auto job configuration**
   option.
2. Select **SageMaker Processing**.
3. For **Job name**, enter a name for your SageMaker AI
   Processing job.
4. For **Instance type**, select the type of
   compute instance to run the processing job.
5. For **Instance count**, specify the number of
   compute instances to launch.
6. For **IAM role**, enter the user's IAM
   execution role. This role should have the required permissions
   for SageMaker AI to create and run processing jobs on your behalf. These
   permissions are granted if you have the [AmazonSageMakerFullAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md") policy attached to your
   IAM role.
7. For **Volume size**, enter the storage size
   in GB for the ML storage volume that is attached to each
   processing instance. Choose the size based on your expected
   input and output data size.
8. (Optional) For **Volume KMS key**, specify
   a KMS key to encrypt the storage volume. If you don't specify
   a key, the default Amazon EBS encryption key is used.
9. (Optional) For **KMS key**, specify a
   KMS key to encrypt input and output Amazon S3 data sources used by
   the processing job.
10. (Optional) For **Spark memory
    configuration**, do the following:
    1. Enter **Driver memory in MB** for the
       Spark driver node that handles job coordination and
       scheduling.
    2. Enter **Executor memory in MB** for
       the Spark executor nodes that run individual tasks in
       the job.

11. (Optional) For **Network configuration**, do
    the following:
    1. For **Subnet configuration**, enter
       the IDs of the VPC subnets for the processing instances
       to be launched in. By default, the job uses the settings
       of your default VPC.
    2. For **Security group configuration**,
       enter the IDs of the security groups to control inbound
       and outbound connectivity rules.
    3. Turn on the **Enable inter-container traffic
       encryption** option to encrypt network
       communication between processing containers during the
       job.

12. (Optional) For **Associate schedules**, you
    can choose create an Amazon EventBridge schedule to have the processing
    job run on recurring intervals. Choose **Create new
    schedule** and fill out the dialog box. For more
    information about filling out this section and running
    processing jobs on a schedule, see [Create a schedule to automatically
    process new data](canvas-data-export-schedule-job.md "canvas-data-export-schedule-job.md").
13. (Optional) Add **Tags** as key-value pairs so
    that you can categorize and search for processing jobs.
14. Choose **Export** to start the processing
    job.

After exporting your data, you should find the fully processed dataset in the
specified Amazon S3 location.
