# Reviewing your inventory of sensitive data

discovery jobs

On the Amazon Macie console, you can review a complete inventory of your sensitive data discovery jobs
in the current AWS Region. The inventory provides both summary information for all of
your jobs and details about individual jobs. Summary information includes: the current
status of each job; whether a job runs on a scheduled, periodic basis; and, whether a
job is configured to analyze objects in specific Amazon Simple Storage Service (Amazon S3) buckets or S3 buckets
that match runtime criteria. For individual jobs, you can also access details such as a
breakdown of the job's configuration settings. If a job has already run, the details
also provide direct access to sensitive data findings and other types of results that
the job produced.

###### To review your job inventory

Follow these steps to review your job inventory by using the Amazon Macie console. To
access your inventory programmatically, use the [ListClassificationJobs](../APIReference/jobs-list.md "../APIReference/jobs-list.md")
operation of the Amazon Macie API.

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **Jobs**. The
   **Jobs** page opens and displays the number of jobs in your
   inventory and a table of those jobs.
3. At the top of the page, optionally choose refresh (
   ![The refresh button, which is a button that displays an empty blue circle with an arrow.](/images/macie/latest/user/images/btn-refresh-data.png)
   ) to retrieve
   the current status of each job.
4. In the **Jobs** table, review summary information for your
   jobs:
   - **Job name** – The name of the job.
   - **Resources** – Whether the job is configured
     to analyze objects in specific S3 buckets or buckets that match runtime
     criteria. If you explicitly selected buckets for the job to analyze,
     this field indicates the number of buckets that you selected. If you
     configured the job to use runtime criteria, the value for this field is
     **Criteria based**.
   - **Job type** – Whether the job is configured
     to run once (**One time**) or on a scheduled, periodic
     basis (**Scheduled**).
   - **Status** – The current status of the job. To
     learn more about this value, see [Checking the status of a
     job](discovery-jobs-status-check.md "discovery-jobs-status-check.md").
   - **Created at** – When the job was
     created.

5. To analyze your inventory or find a specific job more quickly, do any of the
   following:
   - To sort the table by a specific field, choose the column heading for
     the field. To change the sort order, choose the column heading
     again.
   - To show only those jobs that have a specific value for a field, place
     your cursor in the filter box. In the menu that appears, choose the
     field to use for the filter, and enter the value for the filter. Then
     choose **Apply**.
   - To hide jobs that have a specific value for a field, place your cursor
     in the filter box. In the menu that appears, choose the field to use for
     the filter, and enter the value for the filter. Then choose
     **Apply**. In the filter box, choose the equals
     icon (
     ![The equals icon, which is a solid gray circle.](images/icon-operator-equals.png)
     ) for the filter. This changes the filter's
     operator from _equals_ to _not equals_
     (
     ![The not equals icon, which is an empty gray circle that has a backslash in it.](images/icon-operator-not-equals.png)
     ).
   - To remove a filter, choose the remove filter icon
     (
     ![The remove filter condition icon, which is a circle that has an X in it.](/images/macie/latest/user/images/icon-filter-remove.png)
     ) for the filter to remove.

6. To review additional settings and details for a particular job, choose the
   job's name. Then refer to the details panel. For information about these
   details, see [Reviewing configuration settings for
   a job](discovery-jobs-manage-settings.md "discovery-jobs-manage-settings.md").
