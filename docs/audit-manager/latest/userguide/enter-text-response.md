

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Entering free-form text responses as manual evidence
<a name="enter-text-response"></a>



You can provide additional context and supporting information for an assessment control by entering free-form text and saving that text as evidence. This allows you to manually document details that aren’t captured through automatic evidence collection. 

For example, you can use Audit Manager to create custom controls that represent questions in a vendor risk assessment questionnaire. In this case, the name of each control is a specific question that asks for information about your organization’s security and compliance posture. To record your response to a given vendor risk assessment question, you can enter a text response and save it as manual evidence for the control.

## Prerequisites
<a name="enter-text-response-prerequisites"></a>
+ When a control is *inactive*, you can't add manual evidence to that control. To add manual evidence, you must first [change the control status](https://docs.aws.amazon.com/audit-manager/latest/userguide/change-assessment-control-status.html) to either *under review* or *reviewed*.
+ Make sure your IAM identity has appropriate permissions to manage an assessment in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="enter-text-response-procedure"></a>

You can enter text responses using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface (AWS CLI).

------
#### [ AWS console ]

**Important**  
We strongly recommend that you never enter any sensitive or personally identifiable information (PII) as manual evidence. This includes, but is not limited to, Social Security numbers, addresses, phone numbers, or any other information that could be used to identify an individual. 

**To enter a text response on the Audit Manager console**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the left navigation pane, choose **Assessments** and then choose an assessment.

1. Choose the **Controls** tab, scroll down to **Control sets** and then choose a control. 

1. From the **Evidence folders** tab, choose **Add manual evidence**.

1. Choose **Enter text response**.

1. In the pop-up window that appears, enter your response in plain text format.

1. Choose **Confirm**.

------
#### [ AWS CLI ]

**Important**  
We strongly recommend that you never enter any sensitive or personally identifiable information (PII) as manual evidence. This includes, but is not limited to, Social Security numbers, addresses, phone numbers, or any other information that could be used to identify an individual. 

In the following procedure, replace the {{placeholder text}} with your own information.

**To enter a text response in the AWS CLI**

1. Run the `[list-assessments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessments.html)` command. 

   ```
   aws auditmanager list-assessments
   ```

   In the response, find the assessment that you want to upload evidence to and take note of the assessment ID.

1. Run the `[get-assessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-assessment.html)` command and specify the assessment ID from step one. 

   ```
   aws auditmanager get-assessment --assessment-id {{1a2b3c4d-5e6f-7g8h-9i0j-0k1l2m3n4o5p}}
   ```

   In the response, find the control set and control that you want to upload evidence to, and take note of their IDs.

1. Run the `[batch-import-evidence-to-assessment-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/batch-import-evidence-to-assessment-control.html)` command with the following parameters:
   + `--assessment-id` – Use the assessment ID from step one.
   + `--control-set-id` – Use the control set ID from step two.
   + `--control-id` – Use the control ID from step two.
   + `--manual-evidence` – Use `textResponse` as the manual evidence type and enter the text that you want to save as manual evidence.

   ```
   aws auditmanager batch-import-evidence-to-assessment-control --assessment-id {{1a2b3c4d-5e6f-7g8h-9i0j-0k1l2m3n4o5p}} --control-set-id {{ControlSet}} --control-id {{a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6}} --manual-evidence textResponse={{"enter text here"}}
   ```

------
#### [ Audit Manager API ]

**Important**  
We strongly recommend that you never enter any sensitive or personally identifiable information (PII) as manual evidence. This includes, but is not limited to, Social Security numbers, addresses, phone numbers, or any other information that could be used to identify an individual. 

**To enter a text response using the API**

1. Call the `[ListAssessments](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessments.html)` operation. In the response, find the assessment that you want to upload evidence to and take note of the assessment ID.

1. Call the `[GetAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessment.html)` operation and specify the `assessmentId` from step one. In the response, find the control set and control that you want to upload evidence to, and take note of their IDs.

1. Call the `[BatchImportEvidenceToAssessmentControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchImportEvidenceToAssessmentControl.html)` operation with the following parameters:
   + `[assessmentId](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchImportEvidenceToAssessmentControl.html#auditmanager-BatchImportEvidenceToAssessmentControl-request-assessmentId)` – Use the assessment ID from step one.
   + `[controlSetId](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchImportEvidenceToAssessmentControl.html#auditmanager-BatchImportEvidenceToAssessmentControl-request-controlSetId)` – Use the control set ID from step two.
   + `[controlId](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchImportEvidenceToAssessmentControl.html#auditmanager-BatchImportEvidenceToAssessmentControl-request-controlId)` – Use the control ID from step two.
   + `[manualEvidence](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchImportEvidenceToAssessmentControl.html#auditmanager-BatchImportEvidenceToAssessmentControl-request-manualEvidence)` – Use `textResponse` as the manual evidence type and enter the text that you want to save as manual evidence.

For more information, choose any of the links in the previous procedure to read more in the *AWS Audit Manager API Reference*. This includes information about how to use these operations and parameters in one of the language-specific AWS SDKs.

------

## Next steps
<a name="enter-text-response-next-steps"></a>

After you've collected and reviewed the evidence for your assessment, you can generate an assessment report. For more information, see [Preparing an assessment report in AWS Audit Manager](generate-assessment-report.md).