

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Changing the status of an assessment control in AWS Audit Manager
<a name="change-assessment-control-status"></a>

You can change the status of an assessment control within your active assessment. Updating a control's status enables you to track its progress and indicate when you have reviewed it, keeping your assessment organized and up-to-date. 

## Prerequisites
<a name="change-assessment-control-status-prerequisites"></a>

The following procedure assumes that you have previously created an assessment, and its current status is active.

Make sure your IAM identity has appropriate permissions to manage an assessment in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="change-assessment-control-status-procedure"></a>

You can update an assessment control status using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface (AWS CLI).

**Note**  
Changing a control status to *Reviewed* is final. After you set the status of a control to *Reviewed*, you can no longer change the status of that control or revert to a previous status. 

------
#### [ Audit Manager console ]

**To change an assessment control status on the Audit Manager console**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the navigation pane, choose **Assessments**.

1. Choose the name of the assessment to open it.

1. From the assessment page, choose the **Controls** tab, scroll down to the **Control sets** table, and then choose the name of a control to open it.

1. Choose **Update control status** at the top right of the page, and then choose a status:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/change-assessment-control-status.html)

1. Choose **Update control status** to confirm your choice.

------
#### [ AWS CLI ]

**To change an assessment control status in the AWS CLI**

1. Run the [list-assessments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessments.html) command.

   ```
    aws auditmanager list-assessments
   ```

   The response returns a list of assessments. Find the assessment that contains the control that you want to update, and take note of the assessment ID.

1. Run the [get-assessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-assessment.html) command and specify the assessment ID from step 1.

   In the following example, replace the {{placeholder text}} with your own information.

   ```
    aws auditmanager get-assessment --assessment-id {{1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4e5f6g}}
   ```

   In the response, find the control that you want to update and take note of the control ID and its control set ID.

1. Run the [update-assessment-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment-control.html) command and specify the following parameters: 
   + `--assessment-id` – The assessment that the control belongs to.
   + `--control-set-id` – The control set that the control belongs to.
   + `--control-id` – The control that you want to update.
   + `--control-status` – Set this value to `UNDER_REVIEW`, `REVIEWED`, or `INACTIVE`.

   In the following example, replace the {{placeholder text}} with your own information.

   ```
   aws auditmanager update-assessment-control --assessment-id {{1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4e5f6g}} --control-set-id "{{My control set}}" --control-id {{2b3c4d5e-2b3c-2b3c-2b3c-2b3c4d5f6g7h}} --control-status {{REVIEWED}}
   ```

------
#### [ Audit Manager API ]

**To change an assessment control status using the API**

1. Use the [ListAssessments](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessments.html) operation. 

   In the response, find the assessment that contains the control that you want to update, and take note of the assessment ID.

1. Use the [GetAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessment.html) operation and specify the assessment ID from step 1.

   In the response, find the control that you want to update and take note of the control ID and its control set ID.

1. Use the [UpdateAssessmentControl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment-control.html) operation and specify the following parameters: 
   + `[assessmentId](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentControl.html#auditmanager-UpdateAssessmentControl-request-assessmentId)` – The assessment that the control belongs to.
   + `[controlSetId](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentControl.html#auditmanager-UpdateAssessmentControl-request-controlSetId)` – The control set that the control belongs to.
   + `[controlId](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentControl.html#auditmanager-UpdateAssessmentControl-request-controlId)` –The control that you want to update.
   + `[controlStatus](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentControl.html#auditmanager-UpdateAssessmentControl-request-controlStatus)` – Set this value to `UNDER_REVIEW`, `REVIEWED`, or `INACTIVE`.

For more information about these API operations, choose any of the links in the previous procedure to read more in the *AWS Audit Manager API Reference*. This includes information about how to use these operations and parameters in one of the language-specific AWS SDKs.

------

## Next steps
<a name="change-assessment-control-status-next-steps"></a>

When you're ready to change the status of the assessment, see [Changing the status of an assessment to inactive in AWS Audit Manager](change-assessment-status-to-inactive.md).