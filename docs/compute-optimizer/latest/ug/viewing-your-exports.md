

# Viewing your export jobs

This section shows you how to view the export jobs that you created in the last seven days.

## Prerequisites
<a name="viewing-your-exports-prerequisites"></a>

These steps assume that you already finished the [Exporting your recommendations](exporting-your-recommendations.md) procedure.

## Procedure
<a name="viewing-your-exports-procedure"></a>

**To view your export jobs**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Exports** in the navigation pane.

   The **Exports** page shows the export jobs that you created in the last seven days.

   An export job can have one of the following statuses.
   + **Queued** - The job has not started. You can run only one export job at a time for each resource type and each AWS Region.
   + **In progress** - The job started but is not done. A job can take a few minutes to a few hours. The time depends on how many recommendations and fields it includes.
   + **Complete** - The job is done. The export destination column shows a link to the Amazon S3 CSV file for the job.
   + **Failed** - The job did not start or finish. The failure reason column shows why. For example, a job can fail if your Amazon S3 bucket is missing the required permissions. Fix the issue, then export your recommendations again. For more information, see [Troubleshooting failed export jobs](troubleshooting-account-opt-in.md#troubleshooting-exports).

1. You can perform the following actions on the page:
   + Choose the export destination link for a finished job to open the Amazon S3 bucket. The link shows only for jobs that finished. A dash (-) shows for jobs that are in progress or that failed.
   + Scroll right to see the failure reason for a failed job. Use it to find out why the job is not done.

## Additional resources
<a name="viewing-your-exports-resources"></a>
+ Troubleshooting — [Troubleshooting failed export jobs](troubleshooting-account-opt-in.md#troubleshooting-exports)
+ [Exported files](exported-files.md)