# Creating a job

To create a job, you specify your input settings, output settings, and any job-wide
settings. For a detailed step-by-step procedure, see [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md"). The following procedure is a high level overview
of how to create a job using the AWS Management Console.

When you create a job, you submit it to a queue for processing. Processing begins
automatically from your queues as resources allow. For information about resource
allocation, see [Processing multiple jobs in parallel](working-with-on-demand-queues.md#queue-resources "working-with-on-demand-queues.md#queue-resources") .

###### To create a job using the MediaConvert console

1. Open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list "https://console.aws.amazon.com/mediaconvert/home#/jobs/list") page in
   the MediaConvert console.
2. Choose **Create job**.
3. On the **Create job** page, provide transcode instructions
   and job settings. For more information, see [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").

Make sure that you select the same AWS Region for your job and your file storage. 4. Choose **Create**.
You can also create a job using a [Template](using-a-job-template.md "using-a-job-template.md"),
[Preset](using-a-preset-to-specify-a-job-output.md "using-a-preset-to-specify-a-job-output.md"), [duplicated job](create-new-job-from-completed-job.md "create-new-job-from-completed-job.md"), or [job settings JSON](exporting-and-importing-jobs.md "exporting-and-importing-jobs.md").
