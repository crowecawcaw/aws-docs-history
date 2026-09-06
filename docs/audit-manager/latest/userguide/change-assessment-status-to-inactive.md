

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Changing the status of an assessment to inactive in AWS Audit Manager
<a name="change-assessment-status-to-inactive"></a>



When you no longer need to collect evidence for an assessment, you can change the assessment status to *Inactive*. When the status of an assessment changes to inactive, the assessment stops collecting evidence. As a result, you no longer incur any charges for that assessment.

In addition to stopping evidence collection, Audit Manager makes the following changes to the controls that are within the inactive assessment:
+ All control sets change to *Reviewed* status.
+ All controls that are *Under review* change to *Reviewed* status.
+ Delegates for the inactive assessment can no longer view or edit its controls and control sets.

## Prerequisites
<a name="change-assessment-status-to-inactive-prerequisites"></a>

The following procedure assumes that you have previously created an assessment, and its current status is active.

Make sure your IAM identity has appropriate permissions to manage an assessment in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="change-assessment-status-to-inactive-procedure"></a>

You can update an assessment status using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface (AWS CLI).

**Warning**  
This action is irreversible. We recommend that you proceed with caution and make sure that you want to mark your assessment as inactive. When an assessment is inactive, you have read-only access to its contents. This means that you can still review previously collected evidence and generate assessment reports. However, you can’t edit the inactive assessment, add comments, or upload any manual evidence.

------
#### [ Audit Manager console ]

**To change an assessment status to inactive on the Audit Manager console**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the navigation pane, choose **Assessments**.

1. Choose the name of the assessment to open it.

1. On the upper-right corner of the page, choose **Update assessment status**, and then choose **Inactive**.

1. Choose **Update status** in the pop-up window to confirm that you want to change the status to inactive. 

The changes to the assessment and its controls take effect after approximately one minute.

------
#### [ AWS CLI ]

**To change an assessment status to inactive in the AWS CLI**

1. First, identify the assessment that you want to update. To do this, run the [list-assessments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessments.html) command.

   ```
    aws auditmanager list-assessments
   ```

   The response returns a list of assessments. Find the assessment that you want to deactivate, and take note of the assessment ID.

1. Next, run the [update-assessment-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment-status.html) command and specify the following parameters: 
   + `--assessment-id` – Use this parameter to specify the assessment that you want to deactivate.
   + `--status` – Set this value to `INACTIVE`.

   In the following example, replace the {{placeholder text}} with your own information.

   ```
   aws auditmanager update-assessment-status --assessment-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} --status INACTIVE
   ```

The changes to the assessment and its controls take effect after approximately one minute.

------
#### [ Audit Manager API ]

**To change an assessment status to inactive using the API**

1. Use the [ListAssessments](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessments.html) operation to find the assessment that you want to deactivate, and take note of the assessment ID.

1. Use the [UpdateAssessmentStatus](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentStatus.html) operation and specify the following parameters: 
   + [assessmentId](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentStatus.html#auditmanager-UpdateAssessmentStatus-request-assessmentId) – Use this parameter to specify the assessment that you want to deactivate.
   + [status](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentStatus.html#auditmanager-UpdateAssessmentStatus-request-status) – Set this value to `INACTIVE`.

The changes to the assessment and its controls take effect after approximately one minute.

For more information about these API operations, choose any of the links in the previous procedure to read more in the *AWS Audit Manager API Reference*. This includes information about how to use these operations and parameters in one of the language-specific AWS SDKs.

------

## Next steps
<a name="change-assessment-status-to-inactive-next-steps"></a>

When you're certain that you no longer need your inactive assessment, you can clean up your Audit Manager environment by deleting the assessment. For instructions, see [Deleting an assessment in AWS Audit Manager](delete-assessment.md).