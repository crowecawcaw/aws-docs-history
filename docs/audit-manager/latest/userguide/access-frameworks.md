# Finding the available frameworks in AWS Audit Manager

You can find all available frameworks on the **Framework library** page
in the Audit Manager console.

You can also view all available frameworks using the Audit Manager API or the AWS Command Line Interface (AWS CLI).

## Prerequisites

Make sure your IAM identity has appropriate permissions to view frameworks in
AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

Audit Manager console

###### To view available frameworks on the Audit Manager console

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the left navigation pane, choose **Framework library**.
3. Choose the **Standard frameworks** tab or the **Custom
   frameworks** tab to browse the available standard and custom frameworks.

AWS CLI

###### To view available frameworks in the AWS CLI

To view frameworks in Audit Manager, use the [list-assessment-frameworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessment-frameworks.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessment-frameworks.html") command and specify a
`--framework-type`. Either, you can retrieve a list of standard frameworks.
Or, you can retrieve a list of custom frameworks.

```
aws auditmanager list-assessment-frameworks --framework-type Standard
```

```
aws auditmanager list-assessment-frameworks --framework-type Custom
```

Audit Manager API

###### To view available frameworks using the API

Use the [ListAssessmentFrameworks](../APIReference/API_ListAssessmentFrameworks.md "../APIReference/API_ListAssessmentFrameworks.md") operation and specify a [frameworkType](../APIReference/API_ListAssessmentFrameworks.md#auditmanager-ListAssessmentFrameworks-request-frameworkType "../APIReference/API_ListAssessmentFrameworks.md#auditmanager-ListAssessmentFrameworks-request-frameworkType"). Either, you can return a list of standard frameworks. Or,
you can return a list of custom frameworks.

For more information, choose either of the previous links to read more in the
_AWS Audit Manager API Reference_. This includes
information about how to use the `ListAssessmentFrameworks` operation and
parameters in one of the language-specific AWS SDKs.

## Next steps

When you're ready to explore the details of a framework, follow the steps in [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md"). This page will guide you
through the framework details and explain the information that you see there.

From the framework library page, you can also [create](custom-frameworks.md "custom-frameworks.md"), [edit](edit-custom-frameworks.md "edit-custom-frameworks.md"), [delete](delete-custom-framework.md "delete-custom-framework.md"), or
[share](share-custom-framework.md "share-custom-framework.md") a
custom framework.

## Additional resources

For solutions to framework issues in Audit Manager, see [Troubleshooting framework issues](framework-issues.md "framework-issues.md").
