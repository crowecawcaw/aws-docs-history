# Deleting a custom framework in AWS Audit Manager

When you no longer need a custom framework, you can delete it from your Audit Manager environment.
This enables you to clean up your workspace and focus on the custom frameworks that are
relevant to your current tasks and priorities.

## Prerequisites

The following procedure assumes that you have previously created a custom
framework.

Make sure your IAM identity has appropriate permissions to delete a custom framework
in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

You can delete custom frameworks using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface
(AWS CLI).

###### Note

Deleting a custom framework doesn't affect any existing assessments that were created
from the framework before it was deleted.

Audit Manager console

###### To delete a custom framework on the Audit Manager console

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the left navigation pane, choose **Framework library** and
   then choose the **Custom frameworks** tab.
3. Select the framework that you want to delete, choose
   **Actions**, and then choose **Delete**.
   - Alternatively, you can open a custom framework and choose
     **Actions**, **Delete** at the top right of
     the framework summary page.

4. In the pop-up window, choose **Delete** to confirm deletion.

AWS CLI

###### To delete a custom framework in the AWS CLI

1. First, identify the custom framework that you want to delete. To do this, run
   the [list-assessment-frameworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessment-frameworks.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessment-frameworks.html") command and specify the
   `--framework-type` as `Custom`.

```
 aws auditmanager list-assessment-frameworks --framework-type Custom
```

The response returns a list of custom frameworks. Find the custom framework that
you want to delete, and take note of the framework ID. 2. Next, run the [delete-assessment-framework](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/delete-assessment-framework.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/delete-assessment-framework.html") command and specify the
`--framework-id` of the framework that you want to delete.

In the following example, replace the `placeholder
 text` with your own information.

```
aws auditmanager delete-assessment-framework --framework-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
```

Audit Manager API

###### To delete a custom framework using the API

1. Use the [ListAssessmentFrameworks](../APIReference/API_ListAssessmentFrameworks.md "../APIReference/API_ListAssessmentFrameworks.md") operation and specify the [frameworkType](../APIReference/API_ListAssessmentFrameworks.md#auditmanager-ListAssessmentFrameworks-request-frameworkType "../APIReference/API_ListAssessmentFrameworks.md#auditmanager-ListAssessmentFrameworks-request-frameworkType") as `Custom`. From the response, find the custom
   framework that you want to delete, and take note of the framework ID.
2. Use the [DeleteAssessmentFramework](../APIReference/API_DeleteAssessmentFramework.md "../APIReference/API_DeleteAssessmentFramework.md") operation to delete the framework. In the
   request, use the [frameworkId](../APIReference/API_DeleteAssessmentFramework.md#auditmanager-DeleteAssessmentFramework-request-frameworkId "../APIReference/API_DeleteAssessmentFramework.md#auditmanager-DeleteAssessmentFramework-request-frameworkId") parameter to specify the framework that you want to
   delete.

For more information about these API operations, choose any of the links in the
previous procedure to read more in the _AWS Audit Manager API
Reference_. This includes information about how to use these operations and
parameters in one of the language-specific AWS SDKs.

## Additional resources

For information about data retention in Audit Manager, see [Deletion of Audit Manager data](data-protection.md#data-deletion-and-retention "data-protection.md#data-deletion-and-retention").
