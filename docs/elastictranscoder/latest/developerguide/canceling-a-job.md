End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Canceling an Elastic Transcoder Job

You can cancel a job that still has a status of **Submitted**, which
means that Elastic Transcoder hasn't started to transcode your file. The following procedure explains
how to cancel a job using the Elastic Transcoder console.

To cancel a job using the API, pause the corresponding pipeline so Elastic Transcoder doesn't start
processing the job, list jobs that have a status of **Submitted** to
get the applicable job ID, then cancel the job using the job ID to identify which job
you want to cancel. For more information, see:

- [Update Pipeline Status](update-pipeline-status.md "update-pipeline-status.md")
- [List Jobs by Status](list-jobs-by-status.md "list-jobs-by-status.md")
- [Cancel Job](cancel-job.md "cancel-job.md")

###### To cancel a job using the Elastic Transcoder console

1. Sign in to the AWS Management Console and open the Elastic Transcoder console at
   [https://console.aws.amazon.com/elastictranscoder/](https://console.aws.amazon.com/elastictranscoder/ "https://console.aws.amazon.com/elastictranscoder/").
2. In the navigation bar of the Elastic Transcoder console, select the region in which you want
   to cancel a job.
3. **Optional but recommended:** Pause the pipeline
   to which you submitted the job, so Elastic Transcoder doesn't begin to process the job. You
   can't cancel a job after Elastic Transcoder begins to process it.
   1. In the navigation (left) pane, click
      **Pipelines**.
   2. Select the check box next to the pipeline that you want to
      pause.
   3. Click **Pause**.

4. In the navigation pane of the console, click **Jobs**.
5. On the **Jobs** page, specify the following values:

**Search By**

Click **Status**.

**Job Status**

Select **Submitted**.

###### Note

You can only cancel a job that has a status of
**Submitted**.

For **Order** and **Number of Jobs**, enter
the applicable values. 6. Click **Search**. 7. In the search results, if you need to view more details about a job to
determine whether it's the one you want to cancel, click the
![Arrow to expand the settings for a preset.](images/magnifying-glass-icon.png)
icon next to the job. 8. To cancel a job, select the check box next to the job, and click
**Cancel**. 9. If you paused the pipeline in Step 3, reactivate it so it resumes processing
jobs.

    1. In the navigation pane, click **Pipelines**.
    2. Select the check box next to the pipeline that you want to
     reactivate.
    3. Click **Activate**.
