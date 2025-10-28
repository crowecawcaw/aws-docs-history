# Managing assessments in AWS Audit Manager

An Audit Manager assessment is based on a framework, which is a grouping of controls. Using a
framework as a starting point, you can create an assessment that collects evidence for the
controls in that framework. In your assessment, you can also define the scope of your audit. This
includes specifying the AWS accounts that you want to collect evidence for.

## Key points

You can create an assessment from any framework. Either, you can use a [standard
framework](framework-overviews.md "framework-overviews.md") that's provided by Audit Manager. Or, you can create an assessment from a [custom
framework](custom-frameworks.md "custom-frameworks.md") that you build yourself. Standard frameworks contain prebuilt control sets
that support a specific compliance standard or regulation. In contrast, custom frameworks contain
controls that you can customize and group according to your own requirements.

When you create an assessment, this starts the ongoing collection of evidence. When it's
time for an audit, you or a delegate can [review this evidence](review-evidence.md "review-evidence.md") and then
[add it to an assessment report](generate-assessment-report.md#generate-assessment-report-include-evidence "generate-assessment-report.md#generate-assessment-report-include-evidence").

###### Note

AWS Audit Manager assists in collecting evidence that's relevant for verifying compliance with
specific compliance standards and regulations. However, it doesn't assess your compliance
itself. The evidence that's collected through AWS Audit Manager therefore might not include all the
information about your AWS usage that's needed for audits. AWS Audit Manager isn't a substitute for
legal counsel or compliance experts.

## Additional resources

To create and manage assessments in Audit Manager, follow the procedures that are outlined
here.

- [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md")
- [Finding your assessments in AWS Audit Manager](access-assessments.md "access-assessments.md")
- [Reviewing an assessment in AWS Audit Manager](review-assessment.md "review-assessment.md")
  - [Reviewing assessment details in AWS Audit Manager](review-assessments.md "review-assessments.md")
  - [Reviewing an assessment control in AWS Audit Manager](review-controls.md "review-controls.md")
  - [Reviewing an evidence folder in
    AWS Audit Manager](review-evidence-folders-detail.md "review-evidence-folders-detail.md")
  - [Reviewing evidence in AWS Audit Manager](review-evidence.md "review-evidence.md")

- [Editing an assessment in AWS Audit Manager](edit-assessment.md "edit-assessment.md")
  - [Changing the status of an assessment control
    in AWS Audit Manager](change-assessment-control-status.md "change-assessment-control-status.md")
  - [Changing the status of an assessment to
    inactive in AWS Audit Manager](change-assessment-status-to-inactive.md "change-assessment-status-to-inactive.md")

- [Adding manual evidence in AWS Audit Manager](upload-evidence.md "upload-evidence.md")
  - [Importing manual evidence files from Amazon S3](import-from-s3.md "import-from-s3.md")
  - [Uploading manual evidence files from your browser](upload-from-computer.md "upload-from-computer.md")
  - [Entering free-form text responses as manual
    evidence](enter-text-response.md "enter-text-response.md")
  - [Supported file formats for manual
    evidence](supported-manual-evidence-files.md "supported-manual-evidence-files.md")

- [Preparing an assessment report in AWS Audit Manager](generate-assessment-report.md "generate-assessment-report.md")
  - [Adding evidence to an assessment
    report](generate-assessment-report-include-evidence.md "generate-assessment-report-include-evidence.md")
  - [Removing evidence from an
    assessment report](generate-assessment-report-remove-evidence.md "generate-assessment-report-remove-evidence.md")
  - [Generating an assessment
    report](generate-assessment-report-generation-steps.md "generate-assessment-report-generation-steps.md")
  - [Downloading an
    assessment report from the download center](download-center.md#download-a-file "download-center.md#download-a-file")
  - [Navigating an assessment report and exploring its contents](assessment-reports.md "assessment-reports.md")
  - [Validating an assessment report](../APIReference/API_ValidateAssessmentReportIntegrity.md "../APIReference/API_ValidateAssessmentReportIntegrity.md")
  - [Deleting an assessment report](download-center.md#delete-assessment-report-steps "download-center.md#delete-assessment-report-steps")
  - [Generating assessment reports from your evidence finder search results](https://amazonaws.com/audit-manager/latest/userguide/exporting-search-results-from-evidence-finder.html#generate-one-time-report-from-search-results "https://amazonaws.com/audit-manager/latest/userguide/exporting-search-results-from-evidence-finder.html#generate-one-time-report-from-search-results")

- [Deleting an assessment in AWS Audit Manager](delete-assessment.md "delete-assessment.md")
