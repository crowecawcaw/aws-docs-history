# Changing the status of an assessment control

in AWS Audit Manager

You can change the status of an assessment control within your active assessment. Updating a
control's status enables you to track its progress and indicate when you have reviewed it,
keeping your assessment organized and up-to-date.

## Prerequisites

The following procedure assumes that you have previously created an assessment, and its
current status is active.

Make sure your IAM identity has appropriate permissions to manage an assessment in
AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

You can update an assessment control status using the Audit Manager console, the Audit Manager API, or the
AWS Command Line Interface (AWS CLI).

###### Note

Changing a control status to _Reviewed_ is final. After
you set the status of a control to _Reviewed_, you can no
longer change the status of that control or revert to a previous status.

Audit Manager console

###### To change an assessment control status on the Audit Manager console

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Assessments**.
3. Choose the name of the assessment to open it.
4. From the assessment page, choose the **Controls** tab, scroll down to
   the **Control sets** table, and then choose the name of a control to open
   it.
5. Choose **Update control status** at the top right of the page, and
   then choose a status:

| Status           | Description                                                                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Under review** | Choose this status if you haven't reviewed the control yet.                                                                                 |
| **Reviewed**     | Choose this status if you have finished reviewing the evidence for this control,<br>and you want to continue collecting or adding evidence. |
| **Inactive**     | Choose this status if you want to stop collecting automated evidence for this<br>control.                                                   |

6. Choose **Update control status** to confirm your choice.

AWS CLI

###### To change an assessment control status in the AWS CLI

1. Run the [list-assessments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessments.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessments.html") command.

```
 aws auditmanager list-assessments
```

The response returns a list of assessments. Find the assessment that contains the
control that you want to update, and take note of the assessment ID. 2. Run the [get-assessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-assessment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-assessment.html") command and specify the assessment ID from step 1.

In the following example, replace the `placeholder text` with
your own information.

```
 aws auditmanager get-assessment --assessment-id `1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4e5f6g`
```

In the response, find the control that you want to update and take note of the control
ID and its control set ID. 3. Run the [update-assessment-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment-control.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment-control.html") command and specify the following parameters:

    * `--assessment-id` – The assessment that the control belongs
     to.
    * `--control-set-id` – The control set that the control belongs
     to.
    * `--control-id` – The control that you want to update.
    * `--control-status` – Set this value to `UNDER_REVIEW`,
     `REVIEWED`, or `INACTIVE`.

In the following example, replace the `placeholder text` with
your own information.

```
aws auditmanager update-assessment-control --assessment-id `1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4e5f6g` --control-set-id "`My control set`" --control-id `2b3c4d5e-2b3c-2b3c-2b3c-2b3c4d5f6g7h` --control-status `REVIEWED`
```

Audit Manager API

###### To change an assessment control status using the API

1. Use the [ListAssessments](../APIReference/API_ListAssessments.md "../APIReference/API_ListAssessments.md") operation.

In the response, find the assessment that contains the control that you want to
update, and take note of the assessment ID. 2. Use the [GetAssessment](../APIReference/API_GetAssessment.md "../APIReference/API_GetAssessment.md") operation and specify the assessment ID from
step 1.

In the response, find the control that you want to update and take note of the control
ID and its control set ID. 3. Use the [UpdateAssessmentControl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment-control.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment-control.html") operation and specify the following parameters:

    * `assessmentId` – The assessment that the control belongs
     to.
    * `controlSetId` – The control set that the control belongs
     to.
    * `controlId` –The control that you want to update.
    * `controlStatus` – Set this value to `UNDER_REVIEW`,
     `REVIEWED`, or `INACTIVE`.

For more information about these API operations, choose any of the links in the previous
procedure to read more in the _AWS Audit Manager API Reference_. This
includes information about how to use these operations and parameters in one of the
language-specific AWS SDKs.

## Next steps

When you're ready to change the status of the assessment, see [Changing the status of an assessment to
inactive in AWS Audit Manager](change-assessment-status-to-inactive.md "change-assessment-status-to-inactive.md").
