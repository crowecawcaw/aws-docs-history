# Finding your assessments in AWS Audit Manager

After you create assessments in AWS Audit Manager, you can find them on the assessments page of the
Audit Manager console.

From this page, you can perform various actions on your assessments. For example, you can
view assessment details, edit assessment configurations, or delete assessments that are no longer
required. Additionally, the assessments page serves as a starting point for creating new
assessments.

You can also view your assessments programmatically using the Audit Manager API or the AWS Command Line Interface
(AWS CLI).

## Prerequisites

The following procedure assumes that you have previously created at least one assessment.
If you haven’t created an assessment yet, you won’t see any results when you follow these
steps.

Make sure your IAM identity has appropriate permissions to view an assessment in
AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

You can view your assessments using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface
(AWS CLI).

Audit Manager console

###### To view your assessments on the Audit Manager console

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the left navigation pane, choose **Assessments** to see a list of
   your assessments.
3. Choose any assessment name to view the details for that assessment.

AWS CLI

###### To view your assessments (CLI)

To view assessments in Audit Manager, run the [list-assessments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessments.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessments.html") command. You can use the `--status` subcommand to view
assessments that are active or inactive.

```
aws auditmanager list-assessments --status ACTIVE
```

```
aws auditmanager list-assessments --status INACTIVE
```

Audit Manager API

###### To view your assessments using the API

To view assessments in Audit Manager, use the [ListAssessments](../APIReference/API_ListAssessments.md "../APIReference/API_ListAssessments.md")
operation. You can use the [status](../APIReference/API_ListAssessments.md#auditmanager-ListAssessments-request-status "../APIReference/API_ListAssessments.md#auditmanager-ListAssessments-request-status") attribute to view assessments that are active or
inactive.

For more information, choose either of the previous links to read more in the _AWS Audit Manager API Reference_. This includes information about how to use
the `ListAssessments` operation and parameters in one of the language-specific
AWS SDKs.

## Next steps

When you're ready to explore your assessment's contents, follow the steps in [Reviewing an assessment in AWS Audit Manager](review-assessment.md "review-assessment.md"). This page will guide you
through the assessment details and explain the information that you see there.

From the assessments page, you can also [edit an assessment](edit-assessment.md "edit-assessment.md"), [delete an
assessment](delete-assessment.md "delete-assessment.md"), or [create an assessment](create-assessments.md "create-assessments.md").

## Additional resources

For solutions to assessment issues in Audit Manager, see [Troubleshooting assessment and evidence collection issues](evidence-collection-issues.md "evidence-collection-issues.md").
