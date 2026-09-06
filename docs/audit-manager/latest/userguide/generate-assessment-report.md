

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Preparing an assessment report in AWS Audit Manager
<a name="generate-assessment-report"></a>



After you've collected and reviewed the evidence for your assessment, you can generate an assessment report. An assessment report summarizes your assessment and provides links to an organized set of folders that contain the related evidence. 

## Key points
<a name="generate-assessment-report-key-points"></a>

Newly-collected evidence doesn't automatically appear in an assessment report. This means that you can control which evidence you want to include in the report. After you select the evidence that you want to include, you can generate the final assessment report to share with your auditors. 

When you generate an assessment report, it's placed into the S3 bucket that you chose as your assessment report destination. You can also download the assessment report from the download center in Audit Manager.

## Additional resources
<a name="generate-assessment-report-additional-resources"></a>

For more information about assessment reports and how to manage them, see the following resources.
+ [Adding evidence to an assessment report](generate-assessment-report-include-evidence.md)
+ [Removing evidence from an assessment report](generate-assessment-report-remove-evidence.md)
+ [Generating an assessment report](generate-assessment-report-generation-steps.md)
+ [Downloading an assessment report](https://docs.aws.amazon.com/audit-manager/latest/userguide/download-center.html#download-a-file)
+ [Navigating an assessment report and exploring its contents](https://docs.aws.amazon.com/audit-manager/latest/userguide/assessment-reports.html)
+ [Validating an assessment report](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ValidateAssessmentReportIntegrity.html)
+ [Deleting an assessment report](https://docs.aws.amazon.com/audit-manager/latest/userguide/download-center.html#delete-assessment-report-steps)
+ [Generating assessment reports from your evidence finder search results](https://docs.aws.amazon.com/audit-manager/latest/userguide/exporting-search-results-from-evidence-finder.html#generate-one-time-report-from-search-results)
+ [Configuring your default assessment report destination](settings-destination.md)
+ [Troubleshooting assessment report issues](assessment-report-issues.md)