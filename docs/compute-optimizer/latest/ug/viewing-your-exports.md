# Viewing your export jobs

This section provides you with instructions on how to view the export jobs that you created in the last seven days.

## Prerequisites

The following procedures assumes that you have already completed the [Exporting your recommendations](exporting-your-recommendations.md "exporting-your-recommendations.md") procedure.

## Procedure

###### To view your export jobs

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **Exports** in the navigation pane.

The **Exports** page displays the recommendation export jobs that
were created in the last seven days.

Export jobs can have one of the following statuses.

    * **Queued** - The export job didn't start yet. You can
     have only one recommendations export job in progress for each resource type, and for
     each AWS Region.
    * **In progress** - The export job started but isn't
     complete. Export jobs can take anywhere from a few minutes to a few hours to complete.
     This depends on the number of recommendations and fields that the export job
     includes.
    * **Complete** - The export job is complete. A link to
     the export CSV file in the destination Amazon S3 bucket is displayed for each
     complete export job under the export destination column.
    * **Failed** - The export job failed to start or
     complete. The message that's displayed under the failure reason column for the export
     job provides additional information about why the export job failed. For example, the
     export might have failed because the
     destination
     Amazon S3 bucket didn't have the required permissions. After
     resolving the issue, try to export your recommendations again. For more information,
     see [Troubleshooting failed export jobs](troubleshooting-account-opt-in.md#troubleshooting-exports "troubleshooting-account-opt-in.md#troubleshooting-exports").

3. You can perform the following actions on the page:
   - Choose the export destination link for a completed job to access the destination
     S3 bucket. The export destination displays only for successful export
     jobs.
     A dash (-) displays for export jobs that are in progress or that
     failed.
   - Scroll right to view the failure reason for failed export jobs. Use the failure
     reason to determine why your export job isn't complete.

## Additional resources

- Troubleshooting — [Troubleshooting failed export jobs](troubleshooting-account-opt-in.md#troubleshooting-exports "troubleshooting-account-opt-in.md#troubleshooting-exports")
- [Exported files](exported-files.md "exported-files.md")
