AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Monitoring the import status from the

Snowball Edge

To monitor the status of your import job in the console, sign in to the
[AWS Snow Family Management Console](https://console.aws.amazon.com/snowfamily/home "https://console.aws.amazon.com/snowfamily/home") in the AWS Region where the job was created. Choose the job you want
to track from the table, or search for it by your chosen parameters in the search bar
above the table. After you select the job, detailed information appears for that job
within the table, including a bar that shows real-time status of your job.

###### Note

If we are unable to import data to our data centers from the Snow device due to
any issue with access permissions you have configured, we will attempt to notify you
and you will have 30 days from the date we provide the notification to resolve the
issue. If the issue is not resolved, we may cancel your Snowball Edge job and
delete data from the device.

After your device arrives at AWS, your job status
changes from **In transit to AWS** to **At
AWS**. On average, it takes a day for your data import
into Amazon S3 to begin. When it does, the status of your job changes to
**Importing**. It will take approximately the same amount of time
for AWS to import your data from the Snowball Edge as it did for you to move it to
the Snowball Edge. After your data is imported, the job status changes to
**Completed** status.

Now your first data import job into Amazon S3 using AWS Snowball Edge is complete. You can get a
report about the data transfer from the console. To access this report from the console,
select the job from the table, and expand it to reveal the job's detailed information.
Choose **Get report** to download your job completion report as a PDF
file. For more information, see [Getting your data transfer job completion report and
logs](report.md "report.md").

**Next:**
[Getting your data transfer job completion report and
logs](report.md "report.md")
