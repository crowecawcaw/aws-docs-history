# View AWS Batch job logs in CloudWatch Logs

You can [configure your AWS Batch jobs](using_cloudwatch_logs.md#using_cloudwatch_logs.title "using_cloudwatch_logs.md#using_cloudwatch_logs.title") to send log information to Amazon CloudWatch Logs. This way, you can
view different logs from your jobs in one convenient location. For more information, see
[Using CloudWatch Logs with AWS Batch](using_cloudwatch_logs.md "using_cloudwatch_logs.md").

You can also use **Job logs** in the AWS Batch console to monitor or
troubleshoot an AWS Batch job.

1. Open the [AWS Batch console](https://console.aws.amazon.com/batch/home "https://console.aws.amazon.com/batch/home").
2. Choose **Jobs**. For more detailed information on sorting and filtering job in the job queue, see [View AWS Batch jobs in a job queue](view-jobs.md "view-jobs.md") and [Search for jobs in a job queue](searching-filtering-jobs.md "searching-filtering-jobs.md")
3. For **Job queue**, choose the job queue that you want.

###### Tip

If there are several jobs in the job queue, you can turn on
**Searching and filtering** to find a job faster. For more
information, see [Search AWS Batch for jobs in a job queue](searching-filtering-jobs.md "searching-filtering-jobs.md"). 4. For **Status**, choose the job status that you want. 5. Choose the job that you want and the **Details** page will open. 6. On the **Details** page, scroll down to **Log stream name** and choose the link. The link opens the Amazon CloudWatch Logs page for the job. 7. (Optional) If this is the first time you've viewed the logs you may be asked for authorization.

For **Authorization required**, enter `OK`,
and then choose **Authorize** to accept Amazon CloudWatch charges.

###### Note

To revoke your authorization for CloudWatch charges:

    1. In the left navigation pane, choose
     **Permissions**.
    2. For **Job logs**, choose
     **Edit**.
    3. Clear the **Authorize Batch to use CloudWatch** check
     box.
    4. Choose **Save changes**.
