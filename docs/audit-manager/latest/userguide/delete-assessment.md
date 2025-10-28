# Deleting an assessment in AWS Audit Manager

When you no longer need an assessment, you can delete it from your Audit Manager environment. This
enables you to clean up your workspace and focus on the assessments that are relevant to your
current tasks and priorities.

###### Tip

If your goal is to reduce costs, consider [changing the
assessment status to inactive](change-assessment-status-to-inactive.md "change-assessment-status-to-inactive.md") instead of deleting it. This action stops evidence
collection, and places your assessment in a read-only state where you can review the evidence
that was previously collected. Inactive assessments don’t incur any charges.

## Prerequisites

The following procedure assumes that you have previously created an assessment.

Make sure your IAM identity has appropriate permissions to delete an assessment in
AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

You can delete assessments using the Audit Manager console, the Audit Manager API or the AWS Command Line Interface
(AWS CLI).

###### Warning

This action permanently deletes your assessment and all of the evidence that it collected.
You cannot recover this data. As a result, we recommend that you proceed with caution and make
sure that you want to delete your assessment.

Audit Manager console

###### To delete an assessment on the Audit Manager console

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Assessments**.
3. Select the assessment that you want to delete, and choose
   **Delete**.

AWS CLI

###### To delete an assessment in the AWS CLI

1. First, identify the assessment that you want to delete. To do this, run the [list-assessments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessments.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessments.html") command.

```
 aws auditmanager list-assessments
```

The response returns a list of assessments. Find the assessment that you want to
delete, and take note of the assessment ID. 2. Next, use the [delete-assessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/delete-assessment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/delete-assessment.html") command and specify the `--assessment-id` of the
assessment that you want to delete.

In the following example, replace the `placeholder text` with
your own information.

```
aws auditmanager delete-assessment --assessment-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
```

Audit Manager API

###### To delete an assessment using the API

1. Use the [ListAssessments](../APIReference/API_ListAssessments.md "../APIReference/API_ListAssessments.md")
   operation to find the assessment that you want to delete.

In the response, take note of the assessment ID. 2. Use the [DeleteAssessment](../APIReference/API_DeleteAssessment.md "../APIReference/API_DeleteAssessment.md")
operation and specify the [assessmentId](../APIReference/API_DeleteAssessment.md#auditmanager-DeleteAssessment-request-assessmentId "../APIReference/API_DeleteAssessment.md#auditmanager-DeleteAssessment-request-assessmentId") of the assessment that you want to delete.

For more information about these API operations, choose any of the previous links to
read more in the _AWS Audit Manager API Reference_. This includes
information about how to use these operations and parameters in one of the language-specific
AWS SDKs.

## Additional resources

For information about data retention in Audit Manager, see [Deletion of Audit Manager data](data-protection.md#data-deletion-and-retention "data-protection.md#data-deletion-and-retention").
