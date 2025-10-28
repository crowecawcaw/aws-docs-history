# Generating an assessment

report

When you're ready to generate your assessment report, follow these steps.

## Prerequisites

Before you can generate an assessment report, you must add at least one piece of evidence
to your assessment report. You can either add an entire evidence folder, or you can add
individual evidence items from within a folder.

To ensure that your assessment report is generated successfully, review our [Configuration tips
for your assessment report destination](settings-destination.md#settings-assessment-report-destination-tips "settings-destination.md#settings-assessment-report-destination-tips").

## Procedure

###### To generate an assessment report

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the left navigation pane, choose **Assessments**.
3. Choose the name of the assessment that you want to generate an assessment report for.
4. Choose the **Assessment report selection** tab, and then choose
   **Generate assessment report**.

###### Tip

If **Generate assessment report** is greyed out, this means that no
evidence was added to the assessment report yet. 5. In the pop-up window, provide a name and description for the assessment report, and
review the assessment report details. 6. Choose **Generate assessment report** and wait a few minutes while your
assessment report is generated. 7. Find and download your assessment report from the **Download center**
page of the Audit Manager console.

    * Alternatively, you can go to your assessment report destination S3 bucket and download
     the assessment report from there.

## Next

steps

After you generate an assessment report, you can learn more about the following:

- **Find and download your assessment report** – Learn
  how to download your assessment report [from the download
  center](download-center.md#download-a-file "download-center.md#download-a-file") or [from Amazon S3](../../../AmazonS3/latest/userguide/download-objects.md "../../../AmazonS3/latest/userguide/download-objects.md").
- **Explore your assessment report** – Learn how to
  [navigate an assessment report and explore its contents](assessment-reports.md "assessment-reports.md").
- **Validate your assessment report** – Learn how to
  use the [ValidateAssessmentReportIntegrity](../APIReference/API_ValidateAssessmentReportIntegrity.md "../APIReference/API_ValidateAssessmentReportIntegrity.md") API operation to validate your assessment
  report.
- **Delete an unwanted assessment report** – Learn how
  to delete an unwanted report [from the download center](download-center.md#delete-assessment-report-steps "download-center.md#delete-assessment-report-steps") or [from Amazon S3](../../../AmazonS3/latest/userguide/DeletingObjects.md "../../../AmazonS3/latest/userguide/DeletingObjects.md").
- **Generate assessment reports from evidence finder**
  – Learn how to [generate assessment reports from your evidence finder search results](viewing-search-results-in-evidence-finder.md#generate-one-time-report-from-search-results "viewing-search-results-in-evidence-finder.md#generate-one-time-report-from-search-results").

## Additional

resources

To find answers to common questions and issues, see [Troubleshooting assessment report
issues](assessment-report-issues.md "assessment-report-issues.md") in the _Troubleshooting_ section of this guide.
