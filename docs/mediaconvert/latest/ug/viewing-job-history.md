# Viewing your job history

You can view the recent history of MediaConvert jobs that you created with your AWS account in a
given AWS Region. After three months, the service automatically deletes the record of
a job.

The **Jobs** page shows jobs that are successfully completed, are canceled,
are being processed, are waiting in the queue, and that ended in error. You can filter
the job history list by the status and by the queue that the jobs were sent to. You can
also choose a specific job from the list to view the job's settings.

Console
To view your jobs using the MediaConvert console

1. Open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list "https://console.aws.amazon.com/mediaconvert/home#/jobs/list") page in
   the MediaConvert console.
2. Optionally, filter the list by status and queue by choosing from
   the dropdown lists.
3. To see details for a job, choose a **Job ID** to
   view its **Job summary** page.

CLI
The following `list-jobs` example lists up to twenty of your most recently
created jobs.

```
aws mediaconvert list-jobs
```

For more information about how to cancel a job using
the AWS CLI, see the [AWS CLI command reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-jobs.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-jobs.html").
