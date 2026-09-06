

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Managing assessments in AWS Audit Manager
<a name="assessments"></a>



An Audit Manager assessment is based on a framework, which is a grouping of controls. Using a framework as a starting point, you can create an assessment that collects evidence for the controls in that framework. In your assessment, you can also define the scope of your audit. This includes specifying the AWS accounts that you want to collect evidence for.

## Key points
<a name="assessments-key-points"></a>

You can create an assessment from any framework. Either, you can use a [standard framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-overviews.html) that's provided by Audit Manager. Or, you can create an assessment from a [custom framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/custom-frameworks.html) that you build yourself. Standard frameworks contain prebuilt control sets that support a specific compliance standard or regulation. In contrast, custom frameworks contain controls that you can customize and group according to your own requirements. 

When you create an assessment, this starts the ongoing collection of evidence. When it's time for an audit, you or a delegate can [review this evidence](https://docs.aws.amazon.com/audit-manager/latest/userguide/review-evidence.html) and then [add it to an assessment report](https://docs.aws.amazon.com/audit-manager/latest/userguide/generate-assessment-report.html#generate-assessment-report-include-evidence). 

**Note**  
AWS Audit Manager assists in collecting evidence that's relevant for verifying compliance with specific compliance standards and regulations. However, it doesn't assess your compliance itself. The evidence that's collected through AWS Audit Manager therefore might not include all the information about your AWS usage that's needed for audits. AWS Audit Manager isn't a substitute for legal counsel or compliance experts. 

## Additional resources
<a name="assessments-next-steps"></a>

To create and manage assessments in Audit Manager, follow the procedures that are outlined here.
+ [Creating an assessment in AWS Audit Manager](create-assessments.md)
+ [Finding your assessments in AWS Audit Manager](access-assessments.md)
+ [Reviewing an assessment in AWS Audit Manager](review-assessment.md)
  + [Reviewing assessment details in AWS Audit Manager](review-assessments.md)
  + [Reviewing an assessment control in AWS Audit Manager](review-controls.md)
  + [Reviewing an evidence folder in AWS Audit Manager](review-evidence-folders-detail.md)
  + [Reviewing evidence in AWS Audit Manager](review-evidence.md)
+ [Editing an assessment in AWS Audit Manager](edit-assessment.md)
  + [Changing the status of an assessment control in AWS Audit Manager](change-assessment-control-status.md)
  + [Changing the status of an assessment to inactive in AWS Audit Manager](change-assessment-status-to-inactive.md)
+ [Adding manual evidence in AWS Audit Manager](upload-evidence.md)
  + [Importing manual evidence files from Amazon S3](import-from-s3.md)
  + [Uploading manual evidence files from your browser](upload-from-computer.md)
  + [Entering free-form text responses as manual evidence](enter-text-response.md)
  + [Supported file formats for manual evidence](supported-manual-evidence-files.md)
+ [Preparing an assessment report in AWS Audit Manager](generate-assessment-report.md)
  + [Adding evidence to an assessment report](generate-assessment-report-include-evidence.md)
  + [Removing evidence from an assessment report](generate-assessment-report-remove-evidence.md)
  + [Generating an assessment report](generate-assessment-report-generation-steps.md)
  + [Downloading an assessment report from the download center](https://docs.aws.amazon.com/audit-manager/latest/userguide/download-center.html#download-a-file)
  + [Navigating an assessment report and exploring its contents](https://docs.aws.amazon.com/audit-manager/latest/userguide/assessment-reports.html)
  + [Validating an assessment report](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ValidateAssessmentReportIntegrity.html)
  + [Deleting an assessment report](https://docs.aws.amazon.com/audit-manager/latest/userguide/download-center.html#delete-assessment-report-steps)
  + [Generating assessment reports from your evidence finder search results](https://amazonaws.com/audit-manager/latest/userguide/exporting-search-results-from-evidence-finder.html#generate-one-time-report-from-search-results)
+ [Deleting an assessment in AWS Audit Manager](delete-assessment.md)