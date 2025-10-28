AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Getting Started with AWS Data Pipeline

AWS Data Pipeline helps you sequence, schedule, run, and manage recurring data processing
workloads reliably and cost-effectively. This service makes it easy for you to design
extract-transform-load (ETL) activities using structured and unstructured data, both
on-premises and in the cloud, based on your business logic.

To use AWS Data Pipeline, you create a _pipeline definition_ that specifies the business logic
for your data processing. A typical pipeline definition consists of [activities](dp-concepts-activities.md "dp-concepts-activities.md")
that define the work to perform, and [data nodes](dp-concepts-datanodes.md "dp-concepts-datanodes.md") that define the location
and type of input and output data.

In this tutorial, you run a shell command script that counts the number of GET requests in
Apache web server logs. This pipeline runs every 15 minutes for an hour, and writes
output to Amazon S3 on each iteration.

###### Prerequisites

Before you begin, complete the tasks in [Setting up for AWS Data Pipeline](dp-get-setup.md "dp-get-setup.md").

###### Pipeline Objects

The pipeline uses the following objects:

[ShellCommandActivity](dp-object-shellcommandactivity.md "dp-object-shellcommandactivity.md")

Reads the input log file and counts the number of errors.

[S3DataNode](dp-object-s3datanode.md "dp-object-s3datanode.md") (input)

The S3 bucket that contains the input log file.

[S3DataNode](dp-object-s3datanode.md "dp-object-s3datanode.md") (output)

The S3 bucket for the output.

[Ec2Resource](dp-object-ec2resource.md "dp-object-ec2resource.md")

The compute resource that AWS Data Pipeline uses to perform the activity.

Note that if you have a large amount of log file data, you can configure
your pipeline to use an EMR cluster to process the files instead of an EC2 instance.

[Schedule](dp-object-schedule.md "dp-object-schedule.md")

Defines that the activity is performed every 15 minutes for an hour.

###### Tasks

- [Create the Pipeline](#dp-getting-started-create "#dp-getting-started-create")
- [Monitor the Running Pipeline](#dp-getting-started-monitor "#dp-getting-started-monitor")
- [View the Output](#dp-getting-started-output "#dp-getting-started-output")
- [Delete the Pipeline](#dp-getting-started-delete "#dp-getting-started-delete")

## Create the Pipeline

The quickest way to get started with AWS Data Pipeline is to use a pipeline definition called a _template_.

###### To create the pipeline

1. Open the AWS Data Pipeline console at [https://console.aws.amazon.com/datapipeline/](https://console.aws.amazon.com/datapipeline/ "https://console.aws.amazon.com/datapipeline/").
2. From the navigation bar, select a region. You can select any region that's available to you,
   regardless of your location. Many AWS resources are specific to a region, but AWS Data Pipeline enables
   you to use resources that are in a different region than the pipeline.
3. The first screen that you see depends on whether you've created a pipeline in the current region.
   1. If you haven't created a pipeline in this region, the console displays
      an introductory screen. Choose **Get started now**.
   2. If you've already created a pipeline in this region, the console
      displays a page that lists your pipelines for the region.
      Choose **Create new pipeline**.

4. In **Name**, enter a name for your pipeline.
5. (Optional) In **Description**, enter a description for your pipeline.
6. For **Source**, select **Build using a template**, and then
   select the following template: **Getting Started using ShellCommandActivity**.
7. Under the **Parameters** section, which opened when you selected the template,
   leave **S3 input folder** and **Shell command to run**
   with their default values. Click the folder icon next to **S3 output folder**,
   select one of your buckets or folders, and then click **Select**.
8. Under **Schedule**, leave the default values. When you activate the pipeline
   the pipeline runs start, and then continue every 15 minutes for an hour.

If you prefer, you can select **Run once on pipeline activation**
instead. 9. Under **Pipeline Configuration**, leave logging enabled.
Choose the folder icon under **S3 location for logs**,
select one of your buckets or folders, and then choose **Select**.

If you prefer, you can disable logging instead. 10. Under **Security/Access**, leave **IAM roles**
set to **Default**. 11. Click **Activate**.

If you prefer, you can choose **Edit in Architect** to modify this
pipeline. For example, you can add preconditions.

## Monitor the Running Pipeline

After you activate your pipeline, you are taken to the **Execution details**
page where you can monitor the progress of your pipeline.

###### To monitor the progress of your pipeline

1. Click **Update** or press F5 to update the status displayed.

###### Tip

If there are no runs listed, ensure that **Start (in UTC)** and
**End (in UTC)** cover the scheduled start and end of your pipeline,
and then click **Update**. 2. When the status of every object in your pipeline is `FINISHED`, your pipeline
has successfully completed the scheduled tasks. 3. If your pipeline doesn't complete successfully, check your pipeline settings
for issues. For more information about troubleshooting failed or incomplete instance
runs of your pipeline, see [Resolving Common Problems](dp-check-when-run-fails.md "dp-check-when-run-fails.md").

## View the Output

Open the Amazon S3 console and navigate to your bucket. If you ran your pipeline
every 15 minutes for an hour, you'll see four time-stamped subfolders.
Each subfolder contains output in a file named `output.txt`.
Because we ran the script on the same input file each time, the output files
are identical.

## Delete the Pipeline

To stop incurring charges, delete your pipeline. Deleting your pipeline deletes
the pipeline definition and all associated objects.

###### To delete your pipeline

1. On the **List Pipelines** page, select your pipeline.
2. Click **Actions**, and then choose **Delete**.
3. When prompted for confirmation, choose **Delete**.

If you are finished with the output from this tutorial, delete the output folders from your Amazon S3 bucket.
