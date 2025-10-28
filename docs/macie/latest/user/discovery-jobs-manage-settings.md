# Reviewing the settings for a sensitive data

discovery job

On the Amazon Macie console, you can use the details panel on the **Jobs**
page to review configuration settings and other information about individual sensitive
data discovery jobs. For example, you can review a list of the Amazon Simple Storage Service (Amazon S3) buckets
that a job is configured to analyze. You can also determine which managed and custom
data identifiers a job is configured to use when analyzing objects in those
buckets.

Note that you can’t change any configuration settings for an existing job.
This helps ensure that you have an immutable history of sensitive data findings and discovery results for data privacy and protection audits or investigations that you perform.

If you want to change an existing job, you can [cancel the job](discovery-jobs-status-change.md "discovery-jobs-status-change.md"). Then [copy the job](discovery-jobs-manage-copy.md "discovery-jobs-manage-copy.md"), configure the copy to use
the settings that you want, and save the copy as a new job. If you do this, you should
also take steps to ensure that the new job doesn't analyze existing data in the same way
again. To do this, note the date and time when you cancel the existing job. Then
configure the scope of the new job to include only those objects that are created or
changed after you cancel the original job. For example, you can use [object criteria](discovery-jobs-scope.md#discovery-jobs-scope-criteria "discovery-jobs-scope.md#discovery-jobs-scope-criteria") to define an exclude
condition that specifies when you cancelled the original job.

###### To review the configuration settings for a job

Follow these steps to review a job's configuration settings by using the Amazon Macie
console. To review the settings programmatically, use the [DescribeClassificationJob](../APIReference/jobs-jobid.md "../APIReference/jobs-jobid.md") operation of the Amazon Macie API.

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **Jobs**. The
   **Jobs** page opens and displays the number of jobs in your
   inventory and a table of those jobs.
3. In the **Jobs** table, choose the name of the job whose
   settings you want to review. To find the job more quickly, you can filter the
   table by using the filter options above the table. You can also sort the table
   in ascending or descending order by certain fields.
   When you choose a job in the table, the details panel displays the job's configuration
   settings and other information about the job. Depending on the job's settings, the panel
   contains the following sections.

**General information**

This section provides general information about the job. For example, it
shows the Amazon Resource Name (ARN) of the job, when the job most recently
started to run, and the current status of the job. If you paused the job,
this section also indicates when you paused the job, and when the job or
latest job run expired or will expire if you don't resume it.

**Statistics**

This section shows processing statistics for the job. For example, it
specifies the number of times that the job has run, and the approximate
number of S3 objects that the job has yet to process during its current
run.

**Scope**

This section indicates how often the job runs. It also shows settings that
refine the job's scope—for example, the [sampling depth](discovery-jobs-scope.md#discovery-jobs-scope-sampling "discovery-jobs-scope.md#discovery-jobs-scope-sampling"), and any
[object criteria](discovery-jobs-scope.md#discovery-jobs-scope-criteria "discovery-jobs-scope.md#discovery-jobs-scope-criteria")
that include or exclude S3 objects from the analysis.

**S3 buckets**

This section appears in the panel if the job is configured to analyze
buckets that you explicitly selected when you created the job. It indicates
the number of AWS accounts that the job is configured to analyze data for.
It also indicates the number of buckets that the job is configured to
analyze and the names of those buckets (grouped by account).

To show the complete list of accounts and buckets in JSON format, choose
the number in the **Total buckets** field.

**S3 bucket criteria**

This section appears in the panel if the job uses runtime criteria to determine which
buckets to analyze. It lists the criteria that the job is configured to use.
To show the criteria in JSON format, choose **Details**.
Then choose the **Criteria** tab in the window that
appears.

To review a list of buckets that currently match the criteria, choose
**Details**. Then choose the **Matching
buckets** tab in the window that appears. Optionally choose
refresh (
![The refresh button, which is a button that displays an empty blue circle with an arrow.](images/btn-refresh-data.png)
) to retrieve the latest data. The tab lists up to 25
buckets that currently match the criteria.

###### Tip

If the job has already run, you can also determine whether any buckets
matched the criteria when the job ran and, if so, the names of those
buckets. To do this, review log events for the job: choose
**Show results** at the top of the panel, and then
choose **Show CloudWatch logs**. Macie opens the Amazon CloudWatch
console and displays a table of log events for the job. The events
include a `BUCKET_MATCHED_THE_CRITERIA` event for each bucket
that matched the criteria and was included in the job's analysis. For
more information, see [Monitoring jobs with
CloudWatch Logs](discovery-jobs-monitor-cw-logs.md "discovery-jobs-monitor-cw-logs.md").

**Custom data identifiers**

This section appears in the panel if the job is configured to use one or
more [custom data identifiers](custom-data-identifiers.md "custom-data-identifiers.md").
It specifies the names of those custom data identifiers.

**Allow lists**

This section appears in the panel if the job is configured to use one or
more [allow lists](allow-lists.md "allow-lists.md"). It specifies the names
of those lists. To review the settings and status of a list, choose the link
icon (
![The link icon, which is a blue box that has an arrow in it.](images/icon-view-resource-blue.png)
) next to the list's name.

**Managed data identifiers**

This section indicates which [managed data identifiers](managed-data-identifiers.md "managed-data-identifiers.md") the job is configured to use. This is
determined by the managed data identifier selection type for the job:

- **Recommended** – Use the managed data
  identifiers that are in the [recommended set](discovery-jobs-mdis-recommended.md "discovery-jobs-mdis-recommended.md")
  when the job runs.
- **Include selected** – Use only the
  managed data identifiers listed in the
  **Selections** section.
- **Include all** – Use all the managed data
  identifiers that are available when the job runs.
- **Exclude selected** – Use all the managed
  data identifiers that are available when the job runs, except the
  ones listed in the **Selections** section.
- **Exclude all** – Don't use any managed
  data identifiers. Use only the specified custom data
  identifiers.

To review these settings in JSON format, choose
**Details**.

**Tags**

This section appears in the panel if tags are assigned to the job. It
lists those tags. A *tag* is a label that you define and assign to certain types of AWS resources. Each tag consists of a required tag key and an optional tag value. To learn more, see [Tagging Macie resources](tagging-resources.md "tagging-resources.md").

To review and save the job's settings in JSON format, choose the unique identifier for
the job (**Job ID**) at the top of the panel. Then choose
**Download**.
