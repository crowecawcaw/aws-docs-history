# Checking the status of a sensitive data

discovery job

When you create a sensitive data discovery job, its initial status is **Active
(Running)** or **Active (Idle)**, depending on the job's
type and schedule. The job then passes through additional states, which you can monitor
as the job progresses.

###### Tip

In addition to monitoring the overall status of a job, you can monitor specific
events that occur as a job progresses. You can do this by using logging data that
Amazon Macie automatically publishes to Amazon CloudWatch Logs. The data in these logs provides a
record of changes to a job's status and details about any account- or bucket-level
errors that occur while a job runs. For more information, see [Monitoring jobs with
CloudWatch Logs](discovery-jobs-monitor-cw-logs.md "discovery-jobs-monitor-cw-logs.md").

###### To check the status of a job

Follow these steps to check the status of a job by using the Amazon Macie console. To
check a job's status programmatically, use the [DescribeClassificationJob](../APIReference/jobs-jobid.md "../APIReference/jobs-jobid.md") operation of the Amazon Macie API.

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **Jobs**. The
   **Jobs** page opens and displays the number of jobs in your
   inventory and a table of those jobs.
3. At the top of the page, choose refresh (
   ![The refresh button, which is a button that displays an empty blue circle with an arrow.](/images/macie/latest/user/images/btn-refresh-data.png)
   ) to retrieve the current
   status of each job.
4. In the **Jobs** table, locate the job whose status you want
   to check. To find the job more quickly, you can filter the table by using the
   filter options above the table. You can also sort the table in ascending or
   descending order by certain fields.
5. Refer to the **Status** field in the table. This field
   indicates the job's current status.
   A job's status can be one of the following.

**Active (Idle)**

For a periodic job, the previous run is complete and the next scheduled
run is pending. This value doesn't apply to one-time jobs.

**Active (Running)**

For a one-time job, the job is currently in progress. For a periodic job,
a scheduled run is in progress.

**Cancelled**

For any type of job, the job was stopped permanently (cancelled).

A job has this status if you explicitly cancelled it or, if it's a
one-time job, you paused the job and didn't resume it within 30 days. A job
can also have this status if you previously [suspended Macie](suspend-macie.md "suspend-macie.md") in the current AWS Region.

**Complete**

For a one-time job, the job ran successfully and is now complete. This
value doesn't apply to periodic jobs. Instead, the status of a periodic job
changes to **Active (Idle)** when each run completes
successfully.

**Paused (By Macie)**

For any type of job, the job was stopped temporarily (paused) by
Macie.

A job has this status if completion of the job or a job run would exceed
the monthly [sensitive data discovery
quota](macie-quotas.md "macie-quotas.md") for your account. When this happens, Macie automatically
pauses the job. Macie automatically resumes the job when the next calendar
month starts and the monthly quota is reset for your account, or you
increase the quota for your account.

If you’re the Macie administrator for an organization and you configured the job
to analyze data for member accounts, the job can also have this status if
completion of the job or a job run would exceed the monthly sensitive data
discovery quota for a member account.

If a job is running and the analysis of eligible objects reaches this
quota for a member account, the job stops analyzing objects that are owned
by the account. When the job finishes analyzing objects for all other
accounts that haven’t met the quota, Macie automatically pauses the job. If
it’s a one-time job, Macie automatically resumes the job when the next
calendar month starts or the quota is increased for all the affected
accounts, whichever occurs first. If it’s a periodic job, Macie
automatically resumes the job when the next run is scheduled to start or the
next calendar month starts, whichever occurs first. If a scheduled run
starts before the next calendar month starts or the quota is increased for
an affected account, the job doesn’t analyze objects that are owned by the
account.

**Paused (By user)**

For any type of job, the job was stopped temporarily (paused) by
you.

If you pause a one-time job and you don't resume it within 30 days, the
job expires and Macie cancels it. If you pause a periodic job while it's
actively running and you don't resume it within 30 days, the job's run
expires and Macie cancels the run. To check the expiration date for a paused
job or job run, choose the job's name in the table, and then refer to the
**Expires** field in the **Status
details** section of the details panel.

If a job is cancelled or paused, you can refer to the job's details to determine
whether the job started to run or, for a periodic job, ran at least once before it was
cancelled or paused. To do this, choose the job's name in the **Jobs**
table, and then refer to the details panel. In the panel, the **Number of
runs** field indicates the number of times that the job has run. The
**Last run time** field indicates the most recent date and time
when the job started to run.

Depending on the job’s current status, you can optionally pause, resume, or cancel the
job. For more information, see [Changing the status of a
job](discovery-jobs-status-change.md "discovery-jobs-status-change.md").
