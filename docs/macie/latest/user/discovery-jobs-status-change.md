# Changing the status of a sensitive data

discovery job

After you create a sensitive data discovery job, you can pause it temporarily or
cancel it permanently. When you pause a job that's actively running, Amazon Macie
immediately begins to pause all processing tasks for the job. When you cancel a job
that's actively running, Macie immediately begins to stop all processing tasks for the
job. You can’t resume or restart a job after it’s cancelled.

If you pause a one-time job, you can resume it within 30 days. When you resume the
job, Macie immediately resumes processing from the point where you paused the job. Macie
doesn't restart the job from the beginning. If you don't resume a one-time job within 30
days of pausing it, the job expires and Macie cancels it.

If you pause a periodic job, you can resume it at any time. If you resume a periodic
job and the job was idle when you paused it, Macie resumes the job according to the
schedule and other configuration settings that you chose when you created the job. If
you resume a periodic job and the job was actively running when you paused it, how Macie
resumes the job depends on when you resume the job:

- If you resume the job within 30 days of pausing it, Macie immediately resumes
  the latest scheduled run from the point where you paused the job. Macie doesn't
  restart the run from the beginning.
- If you don't resume the job within 30 days of pausing it, the latest scheduled
  run expires and Macie cancels all remaining processing tasks for the run. When
  you subsequently resume the job, Macie resumes the job according to the schedule
  and other configuration settings that you chose when you created the job.
  To help you determine when a paused job or job run will expire, Macie adds an
  expiration date to the job’s details while the job is paused. In addition, we notify you
  approximately seven days before the job or job run will expire. We notify you again when
  the job or job run expires and is cancelled. To notify you, we send email to the address
  that's associated with your AWS account. We also create AWS Health events and
  Amazon CloudWatch Events for your account. To check the expiration date by using the console, choose
  the job’s name in the table on the **Jobs** page. Then refer to the
  **Expires** field in the **Status details**
  section of the details panel. To check the date programmatically, use the [DescribeClassificationJob](../APIReference/jobs-jobid.md "../APIReference/jobs-jobid.md") operation of the Amazon Macie API.

###### To pause, resume, or cancel a job

To pause, resume, or cancel a job by using the Amazon Macie console, follow these
steps. To do this programmatically, use the [UpdateClassificationJob](../APIReference/jobs-jobid.md "../APIReference/jobs-jobid.md")
operation of the Amazon Macie API.

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **Jobs**. The
   **Jobs** page opens and displays the number of jobs in your
   inventory and a table of those jobs.
3. At the top of the page, choose refresh (
   ![The refresh button, which is a button that displays an empty blue circle with an arrow.](/images/macie/latest/user/images/btn-refresh-data.png)
   ) to retrieve the current
   status of each job.
4. In the **Jobs** table, select the checkbox for the job that
   you want to pause, resume, or cancel. To find the job more quickly, you can
   filter the table by using the filter options above the table. You can also sort
   the table in ascending or descending order by certain fields.
5. On the **Actions** menu, do one of the following:
   - To pause the job temporarily, choose **Pause**. This
     option is available only if the job's current status is **Active
     (Idle)**, **Active (Running)**, or
     **Paused (By Macie)**.
   - To resume the job, choose **Resume**. This option is
     available only if the job's current status is **Paused (By
     user)**.
   - To cancel the job permanently, choose **Cancel**. If
     you choose this option, you can't subsequently resume or restart the
     job.
