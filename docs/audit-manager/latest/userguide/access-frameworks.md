

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Finding the available frameworks in AWS Audit Manager
<a name="access-frameworks"></a>



You can find all available frameworks on the **Framework library** page in the Audit Manager console. 

You can also view all available frameworks using the Audit Manager API or the AWS Command Line Interface (AWS CLI). 

## Prerequisites
<a name="access-frameworks-prerequisites"></a>

Make sure your IAM identity has appropriate permissions to view frameworks in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="access-frameworks-procedure"></a>

------
#### [ Audit Manager console ]

**To view available frameworks on the Audit Manager console**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the left navigation pane, choose **Framework library**. 

1. Choose the **Standard frameworks** tab or the **Custom frameworks** tab to browse the available standard and custom frameworks.

------
#### [ AWS CLI ]

**To view available frameworks in the AWS CLI**  
To view frameworks in Audit Manager, use the [list-assessment-frameworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessment-frameworks.html) command and specify a `--framework-type`. Either, you can retrieve a list of standard frameworks. Or, you can retrieve a list of custom frameworks.

```
aws auditmanager list-assessment-frameworks --framework-type Standard
```

```
aws auditmanager list-assessment-frameworks --framework-type Custom
```

------
#### [ Audit Manager API ]

**To view available frameworks using the API**  
Use the [ListAssessmentFrameworks](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentFrameworks.html) operation and specify a [frameworkType](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentFrameworks.html#auditmanager-ListAssessmentFrameworks-request-frameworkType). Either, you can return a list of standard frameworks. Or, you can return a list of custom frameworks.

For more information, choose either of the previous links to read more in the *AWS Audit Manager API Reference*. This includes information about how to use the `ListAssessmentFrameworks` operation and parameters in one of the language-specific AWS SDKs.

------

## Next steps
<a name="access-frameworks-next-steps"></a>

When you're ready to explore the details of a framework, follow the steps in [Reviewing a framework in AWS Audit Manager](review-frameworks.md). This page will guide you through the framework details and explain the information that you see there.

From the framework library page, you can also [create](https://docs.aws.amazon.com/audit-manager/latest/userguide/custom-frameworks.html), [edit](https://docs.aws.amazon.com/audit-manager/latest/userguide/edit-custom-frameworks.html), [delete](https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-custom-framework.html), or [share](https://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework.html) a custom framework.

## Additional resources
<a name="access-frameworks-additional-resources"></a>

For solutions to framework issues in Audit Manager, see [Troubleshooting framework issues](framework-issues.md). 