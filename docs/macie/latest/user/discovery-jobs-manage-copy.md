# Copying a sensitive data discovery

job

To quickly create a sensitive data discovery job that's similar to an existing job,
you can create a copy of the existing job. You can then edit the copy's settings, and
save the copy as a new job. This can be helpful for cases where you want to analyze
different sets of data in the same way, or the same set of data in different ways. It
can also be helpful if you want to adjust the configuration settings for an existing
job—cancel the existing job, copy it, and then adjust and save the copy as a new
job.

###### To copy a job

Follow these steps to copy a job by using the Amazon Macie console. To copy a job
programmatically, use the [DescribeClassificationJob](../APIReference/jobs-jobid.md "../APIReference/jobs-jobid.md") operation of the Amazon Macie API to retrieve
the configuration settings for the job that you want to copy. Then use the [CreateClassificationJob](../APIReference/jobs.md "../APIReference/jobs.md") operation to create a copy of the job.

1.  Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2.  In the navigation pane, choose **Jobs**. The
    **Jobs** page opens and displays the number of jobs in your
    inventory and a table of those jobs.
3.  In the **Jobs** table, select the checkbox for the job that
    you want to copy. To find the job more quickly, you can filter the table by
    using the filter options above the table. You can also sort the table in
    ascending or descending order by certain fields.
4.  On the **Actions** menu, choose **Copy to
    new**.
5.  Complete the steps on the console to review and adjust the settings for the
    copy of the job. For the **Refine the scope** step, consider
    choosing options that prevent the job from analyzing existing data in the same
    way again:

        * For a one-time job, use [object criteria](discovery-jobs-scope.md#discovery-jobs-scope-criteria "discovery-jobs-scope.md#discovery-jobs-scope-criteria") to include only those objects that were
         created or changed after a certain time. For example, if you're creating
         a copy of a job that you cancelled, add a **Last
         modified** condition that specifies the date and time when
         you cancelled the existing job.
        * For a periodic job, clear the **Include existing
         objects** checkbox. If you do this, the first run of the
         job analyzes only those objects that are created or changed after you
         create the job and before the job's first run. You can also use [object criteria](discovery-jobs-scope.md#discovery-jobs-scope-criteria "discovery-jobs-scope.md#discovery-jobs-scope-criteria") to
         exclude objects that were last modified before a certain date and
         time.

    For additional details about this and other steps, see [Creating a sensitive data discovery job](discovery-jobs-create.md "discovery-jobs-create.md").

6.  When you finish, choose **Submit** to save the copy as a new
    job.
    If you configured the job to run once, on a daily basis, or on the current day of the
    week or month, Macie starts running the job immediately after you save it. Otherwise,
    Macie prepares to run the job on the specified day of the week or month. To monitor the
    job, you can [check the status of the
    job](discovery-jobs-status-check.md "discovery-jobs-status-check.md").
