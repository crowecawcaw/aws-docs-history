

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Finding your assessments in AWS Audit Manager
<a name="access-assessments"></a>



After you create assessments in AWS Audit Manager, you can find them on the assessments page of the Audit Manager console. 

From this page, you can perform various actions on your assessments. For example, you can view assessment details, edit assessment configurations, or delete assessments that are no longer required. Additionally, the assessments page serves as a starting point for creating new assessments.

You can also view your assessments programmatically using the Audit Manager API or the AWS Command Line Interface (AWS CLI). 

## Prerequisites
<a name="access-assessments-prerequisites"></a>

The following procedure assumes that you have previously created at least one assessment. If you haven’t created an assessment yet, you won’t see any results when you follow these steps.

Make sure your IAM identity has appropriate permissions to view an assessment in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="access-assessments-procedure"></a>

You can view your assessments using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface (AWS CLI). 

------
#### [ Audit Manager console ]

**To view your assessments on the Audit Manager console**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the left navigation pane, choose **Assessments** to see a list of your assessments.

1. Choose any assessment name to view the details for that assessment.

------
#### [ AWS CLI ]

**To view your assessments (CLI)**  
To view assessments in Audit Manager, run the [list-assessments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessments.html) command. You can use the `--status` subcommand to view assessments that are active or inactive. 

```
aws auditmanager list-assessments --status ACTIVE
```

```
aws auditmanager list-assessments --status INACTIVE
```

------
#### [ Audit Manager API ]

**To view your assessments using the API**  
To view assessments in Audit Manager, use the [ListAssessments](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessments.html) operation. You can use the [status](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessments.html#auditmanager-ListAssessments-request-status) attribute to view assessments that are active or inactive. 

For more information, choose either of the previous links to read more in the *AWS Audit Manager API Reference*. This includes information about how to use the `ListAssessments` operation and parameters in one of the language-specific AWS SDKs.

------

## Next steps
<a name="access-assessments-next-steps"></a>

When you're ready to explore your assessment's contents, follow the steps in [Reviewing an assessment in AWS Audit Manager](review-assessment.md). This page will guide you through the assessment details and explain the information that you see there.

From the assessments page, you can also [edit an assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/edit-assessment.html), [delete an assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-assessment.html), or [create an assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-assessments.html). 

## Additional resources
<a name="access-assessments-additonal-resources"></a>

For solutions to assessment issues in Audit Manager, see [Troubleshooting assessment and evidence collection issues](evidence-collection-issues.md).