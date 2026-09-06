

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Generating an assessment report
<a name="generate-assessment-report-generation-steps"></a>



When you're ready to generate your assessment report, follow these steps.

## Prerequisites
<a name="generate-assessment-report-generation-steps-prerequisite"></a>

Before you can generate an assessment report, you must add at least one piece of evidence to your assessment report. You can either add an entire evidence folder, or you can add individual evidence items from within a folder. 

To ensure that your assessment report is generated successfully, review our [Configuration tips for your assessment report destination](settings-destination.md#settings-assessment-report-destination-tips).

## Procedure
<a name="generate-assessment-report-generation-steps-procedure"></a>

**To generate an assessment report**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the left navigation pane, choose **Assessments**.

1. Choose the name of the assessment that you want to generate an assessment report for. 

1. Choose the **Assessment report selection** tab, and then choose **Generate assessment report**. 
**Tip**  
If **Generate assessment report** is greyed out, this means that no evidence was added to the assessment report yet.

1. In the pop-up window, provide a name and description for the assessment report, and review the assessment report details. 

1. Choose **Generate assessment report** and wait a few minutes while your assessment report is generated. 

1. Find and download your assessment report from the **Download center** page of the Audit Manager console.
   + Alternatively, you can go to your assessment report destination S3 bucket and download the assessment report from there. 

## Next steps
<a name="generate-assessment-report-generation-steps-next-steps"></a>

After you generate an assessment report, you can learn more about the following:
+ **Find and download your assessment report** – Learn how to download your assessment report [from the download center](https://docs.aws.amazon.com/audit-manager/latest/userguide/download-center.html#download-a-file) or [from Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html).
+ **Explore your assessment report** – Learn how to [navigate an assessment report and explore its contents](https://docs.aws.amazon.com/audit-manager/latest/userguide/assessment-reports.html).
+ **Validate your assessment report** – Learn how to use the [ValidateAssessmentReportIntegrity](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ValidateAssessmentReportIntegrity.html) API operation to validate your assessment report.
+ **Delete an unwanted assessment report** – Learn how to delete an unwanted report [from the download center](https://docs.aws.amazon.com/audit-manager/latest/userguide/download-center.html#delete-assessment-report-steps) or [from Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjects.html).
+ **Generate assessment reports from evidence finder** – Learn how to [generate assessment reports from your evidence finder search results](https://docs.aws.amazon.com/audit-manager/latest/userguide/viewing-search-results-in-evidence-finder.html#generate-one-time-report-from-search-results). 

## Additional resources
<a name="generate-assessment-report-generation-steps-additional-resources"></a>

To find answers to common questions and issues, see [Troubleshooting assessment report issues](assessment-report-issues.md) in the *Troubleshooting* section of this guide.