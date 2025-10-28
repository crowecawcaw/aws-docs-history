AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Copy CSV Data Between Amazon S3 Buckets Using AWS Data Pipeline

After you read [What is AWS Data Pipeline?](what-is-datapipeline.md "what-is-datapipeline.md")
and decide you want to use AWS Data Pipeline to automate the movement and transformation of your
data, it is time to get started with creating data pipelines. To help you make sense of how
AWS Data Pipeline works, let’s walk through a simple task.

This tutorial walks you through the process of creating a data pipeline to copy data from
one Amazon S3 bucket to another and then send an Amazon SNS notification after the copy activity
completes successfully. You use an EC2 instance managed by AWS Data Pipeline for this copy
activity.

###### Pipeline Objects

The pipeline uses the following objects:

[CopyActivity](dp-object-copyactivity.md "dp-object-copyactivity.md")

The activity that AWS Data Pipeline performs for this pipeline (copy CSV data from
one Amazon S3 bucket to another).

###### Important

There are limitations when using the CSV file format with
`CopyActivity` and `S3DataNode`. For more
information, see [CopyActivity](dp-object-copyactivity.md "dp-object-copyactivity.md").

[Schedule](dp-object-schedule.md "dp-object-schedule.md")

The start date, time, and the recurrence for this activity. You can optionally
specify the end date and time.

[Ec2Resource](dp-object-ec2resource.md "dp-object-ec2resource.md")

The resource (an EC2 instance) that AWS Data Pipeline uses to perform this activity.

[S3DataNode](dp-object-s3datanode.md "dp-object-s3datanode.md")

The input and output nodes (Amazon S3 buckets) for this pipeline.

[SnsAlarm](dp-object-snsalarm.md "dp-object-snsalarm.md")

The action AWS Data Pipeline must take when the specified conditions are met (send
Amazon SNS notifications to a topic after the task finishes successfully).

###### Contents

- [Before You Begin](dp-copydata-s3-prereq.md "dp-copydata-s3-prereq.md")
- [Copy CSV Data Using the Command Line](dp-get-started-copy-data-cli.md "dp-get-started-copy-data-cli.md")
