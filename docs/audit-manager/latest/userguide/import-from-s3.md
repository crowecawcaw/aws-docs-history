

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Importing manual evidence files from Amazon S3
<a name="import-from-s3"></a>



You can manually import evidence files from an Amazon S3 bucket into your assessment. This enables you to supplement the automatically collected evidence with additional supporting materials.

## Prerequisites
<a name="import-from-s3-prerequisites"></a>
+ The maximum supported size for a single manual evidence file is 100 MB.
+ You must use one of the [Supported file formats for manual evidence](supported-manual-evidence-files.md).
+ Each AWS account can manually upload up to 100 evidence files to a control each day. Exceeding this daily quota causes any additional manual uploads to fail for that control. If you need to upload a large amount of manual evidence to a single control, upload your evidence in batches across several days.
+ When a control is *inactive*, you can't add manual evidence to that control. To add manual evidence, you must first [change the control status](https://docs.aws.amazon.com/audit-manager/latest/userguide/change-assessment-control-status.html) to either *under review* or *reviewed*.
+ Make sure your IAM identity has appropriate permissions to manage an assessment in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="import-from-s3-procedure"></a>

You can import a file using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface (AWS CLI).

------
#### [ AWS console ]

**Important**  
We strongly recommend that you never import any sensitive or personally identifiable information (PII) as manual evidence. This includes, but is not limited to, Social Security numbers, addresses, phone numbers, or any other information that could be used to identify an individual. 

**To import a file from S3 on the Audit Manager console**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the left navigation pane, choose **Assessments** and then choose an assessment.

1. Choose the **Controls** tab, scroll down to **Control sets** and then choose a control.

1. On the **Evidence folders** tab, choose **Add manual evidence**, and then choose **Import file from S3**.

1. On the next page, enter the S3 URI of the evidence. You can find the S3 URI by navigating to the object in the [Amazon S3 console](https://console.aws.amazon.com/s3/) and choosing **Copy S3 URI**. 

1. Choose **Upload**.

------
#### [ AWS CLI ]

**Important**  
We strongly recommend that you never import any sensitive or personally identifiable information (PII) as manual evidence. This includes, but is not limited to, Social Security numbers, addresses, phone numbers, or any other information that could be used to identify an individual. 

In the following procedure, replace the {{placeholder text}} with your own information.

**To import a file from S3 in the AWS CLI**

1. Run the `[list-assessments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessments.html)` command to see a list of your assessments. 

   ```
   aws auditmanager list-assessments
   ```

   In the response, find the assessment that you want to upload evidence to and take note of the assessment ID.

1. Run the `[get-assessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-assessment.html)` command and specify the assessment ID from step one.

   ```
   aws auditmanager get-assessment --assessment-id {{1a2b3c4d-5e6f-7g8h-9i0j-0k1l2m3n4o5p}}
   ```

   In the response, find the control set and the control that you want to upload evidence to, and take note of their IDs.

1. Run the `[batch-import-evidence-to-assessment-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/batch-import-evidence-to-assessment-control.html)` command with the following parameters:
   + `--assessment-id` – Use the assessment ID from step one.
   + `--control-set-id` – Use the control set ID from step two.
   + `--control-id` – Use the control ID from step two.
   + `--manual-evidence` – Use `s3ResourcePath` as the manual evidence type and specify the S3 URI of the evidence. You can find the S3 URI by navigating to the object in the [Amazon S3 console](https://console.aws.amazon.com/s3/) and choosing **Copy S3 URI**.

   ```
   aws auditmanager batch-import-evidence-to-assessment-control --assessment-id {{1a2b3c4d-5e6f-7g8h-9i0j-0k1l2m3n4o5p}} --control-set-id {{ControlSet}} --control-id {{a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6}} --manual-evidence s3ResourcePath={{s3://amzn-s3-demo-bucket/EXAMPLE-FILE.extension}}
   ```

------
#### [ Audit Manager API ]

**Important**  
We strongly recommend that you never import any sensitive or personally identifiable information (PII) as manual evidence. This includes, but is not limited to, Social Security numbers, addresses, phone numbers, or any other information that could be used to identify an individual. 

**To import a file from S3 using the API**

1. Call the `[ListAssessments](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessments.html)` operation to see a list of your assessments. In the response, find the assessment that you want to upload evidence to and take note of the assessment ID.

1. Call the `[GetAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessment.html)` operation and specify the assessment ID from step one. In the response, find the control set and the control that you want to upload evidence to, and take note of their IDs.

1. Call the `[BatchImportEvidenceToAssessmentControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchImportEvidenceToAssessmentControl.html)` operation with the following parameters:
   + `[assessmentId](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchImportEvidenceToAssessmentControl.html#auditmanager-BatchImportEvidenceToAssessmentControl-request-assessmentId)` – Use the assessment ID from step one.
   + `[controlSetId](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchImportEvidenceToAssessmentControl.html#auditmanager-BatchImportEvidenceToAssessmentControl-request-controlSetId)` – Use the control set ID from step two.
   + `[controlId](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchImportEvidenceToAssessmentControl.html#auditmanager-BatchImportEvidenceToAssessmentControl-request-controlId)` – Use the control ID from step two.
   + `[manualEvidence](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchImportEvidenceToAssessmentControl.html#auditmanager-BatchImportEvidenceToAssessmentControl-request-manualEvidence)` – Use `s3ResourcePath` as the manual evidence type and specify the S3 URI of the evidence. You can find the S3 URI by navigating to the object in the [Amazon S3 console](https://console.aws.amazon.com/s3/) and choosing **Copy S3 URI**.

For more information, choose any of the links in the previous procedure to read more in the *AWS Audit Manager API Reference*. This includes information about how to use these operations and parameters in one of the language-specific AWS SDKs.

------

## Next steps
<a name="import-from-s3-next-steps"></a>

After you've added and reviewed the evidence for your assessment, you can generate an assessment report. For more information, see [Preparing an assessment report in AWS Audit Manager](generate-assessment-report.md).

## Additional resources
<a name="import-from-s3-additional-resources"></a>

To learn which file formats you can use, see [Supported file formats for manual evidence](supported-manual-evidence-files.md).