

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Reviewing a framework in AWS Audit Manager
<a name="review-frameworks"></a>



You can review the details of a framework using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface (AWS CLI). 

## Prerequisites
<a name="review-frameworks-prerequisites"></a>

Make sure your IAM identity has appropriate permissions to view frameworks in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="review-frameworks-procedure"></a>

------
#### [ Audit Manager console ]

**To view framework details on the Audit Manager console**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the left navigation pane, choose **Framework library** to see a list of available frameworks. 

1. Choose the **Standard frameworks** tab or the **Custom frameworks** tab to browse the available frameworks.

1. Choose the name of the framework to open it.

1. Review the framework details using the following information as reference.

**Framework details section**  
This section provides an overview of the framework. In this section, you can review the following information:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/review-frameworks.html)
If you're viewing a custom framework, you can also see the following details:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/review-frameworks.html)

**Controls tab**  
This tab lists the controls in the framework, grouped by control set. On this tab, you can review the following information:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/review-frameworks.html)

**Tags tab**  
 This tab lists the tags that are associated with the framework. On this tab, you can review the following information:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/review-frameworks.html)

------
#### [ AWS CLI ]

**To view framework details in the AWS CLI**

1. To identify the framework that you want to review, run the [list-assessment-frameworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessment-frameworks.html) command and specify a `--framework-type`. Either, you can retrieve a list of standard frameworks. Or, you can retrieve a list of custom frameworks.

   In the following example, replace the {{placeholder text}} with either `Custom` or `Standard`.

   ```
    aws auditmanager list-assessment-frameworks --framework-type {{Custom/Standard}}
   ```

   The response returns a list of frameworks. Find the framework that you want to review, and take note of the framework ID and Amazon Resource Name (ARN).

1. To get the framework details, run the [get-assessment-framework](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-assessment-framework.html) command and specify the `--framework-id`.

   In the following example, replace the {{placeholder text}} with your own information.

   ```
   aws auditmanager get-assessment-framework --framework-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
   ```
**Tip**  
The framework details are returned in JSON format. To understand this data, see [get-assessment-framework Output](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-assessment-framework.html#output) in the *AWS CLI Command Reference*.

1. To see the tags for a framework, use the [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-tags-for-resource.html) command and specify the `--resource-arn` for the framework.

   In the following example, replace the {{placeholder text}} with your own information:

   ```
   aws auditmanager list-tags-for-resource --resource-arn arn:aws:auditmanager:{{us-east-1}}:{{111122223333}}:assessmentFramework/{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
   ```

   For more information about tags in Audit Manager, see [Tagging AWS Audit Manager resources](https://docs.aws.amazon.com/audit-manager/latest/userguide/tagging.html).

------
#### [ Audit Manager API ]

**To view framework details using the API**

1. To identify the framework that you want to review, use the [ListAssessmentFrameworks](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentFrameworks.html) operation and specify a [frameworkType](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentFrameworks.html#auditmanager-ListAssessmentFrameworks-request-frameworkType). Either, you can return a list of standard frameworks. Or, you can return a list of custom frameworks. 

   From the response, find the framework that you want to review and note the framework ID and Amazon Resource Name (ARN).

1. To get the framework details, use the [GetAssessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessmentFramework.html) operation. In the request, specify the [frameworkId](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessmentFramework.html#auditmanager-GetAssessmentFramework-request-frameworkId) that you got from step 1.
**Tip**  
The framework details are returned in JSON format. To understand this data, see [GetAssessmentFramework Response Elements](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessmentFramework.html#API_GetAssessmentFramework_ResponseElements) in the *AWS Audit Manager API Reference*.

1. To see tags for the framework, use the [ListTagsForResource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListTagsForResource.html) operation. In the request, specify the framework [resourceArn](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListTagsForResource.html#auditmanager-ListTagsForResource-request-resourceArn) that you got from step 1. 

For more information about tags in Audit Manager, see [Tagging AWS Audit Manager resources](https://docs.aws.amazon.com/audit-manager/latest/userguide/tagging.html). 

For more information about these API operations, choose any of the links in the previous procedure to read more in the *AWS Audit Manager API Reference*. This includes information about how to use these operations and parameters in one of the language-specific AWS SDKs.

------

## Next steps
<a name="review-frameworks-next-steps"></a>

From the framework details page, you can [ create an assessment from the framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-assessments.html) or [ make an editable copy of the framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-custom-frameworks-from-existing).

If you're reviewing a custom framework, you can also [edit](https://docs.aws.amazon.com/audit-manager/latest/userguide/edit-custom-frameworks.html), [delete](https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-custom-framework.html), or [share](https://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework.html) the framework.

## Additional resources
<a name="review-frameworks-additional-resources"></a>
+ [On my custom framework details page, I’m prompted to recreate my custom framework](framework-issues.md#recreate-framework-post-common-controls)
+ [I can’t make a copy of my custom framework](framework-issues.md#cannot-use-custom-framework)