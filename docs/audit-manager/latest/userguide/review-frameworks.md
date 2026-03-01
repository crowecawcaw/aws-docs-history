# Reviewing a framework in AWS Audit Manager

You can review the details of a framework using the Audit Manager console, the Audit Manager API, or the
AWS Command Line Interface (AWS CLI).

## Prerequisites

Make sure your IAM identity has appropriate permissions to view frameworks in AWS Audit Manager.
Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

Audit Manager console

###### To view framework details on the Audit Manager console

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the left navigation pane, choose **Framework library** to
   see a list of available frameworks.
3. Choose the **Standard frameworks** tab or the **Custom
   frameworks** tab to browse the available frameworks.
4. Choose the name of the framework to open it.
5. Review the framework details using the following information as
   reference.

**Framework details section**

This section provides an overview of the framework. In this section, you can
review the following information:

| Name                | Description                                                                       |
| ------------------- | --------------------------------------------------------------------------------- |
| **Description**     | A description of the framework, if one was provided.                              |
| **Framework type**  | Specifies whether the framework is a standard framework or a custom<br>framework. |
| **Compliance type** | The compliance standard or regulation that the framework supports.                |

If you're viewing a custom framework, you can also see the following
details:

| Name             | Description                                     |
| ---------------- | ----------------------------------------------- |
| **Created by**   | The account that created the custom framework.  |
| **Date created** | The date when the custom framework was created. |
| **Last updated** | The date when this framework was last edited.   |

**Controls tab**

This tab lists the controls in the framework, grouped by control set. On this
tab, you can review the following information:

| Name                                | Description                                                                                         |
| ----------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Controls grouped by control set** | Choose the tree view icon to see the controls that belong to each<br>control set.                   |
| **Type**                            | Specifies whether the control is a standard control or a custom<br>control.                         |
| **Data sources**                    | Specifies the data source where Audit Manager collects evidence from for<br>that framework control. |

**Tags tab**

This tab lists the tags that are associated with the framework. On this tab,
you can review the following information:

| Name      | Description                                                                   |
| --------- | ----------------------------------------------------------------------------- |
| **Key**   | The tag key (for example, a compliance standard, regulation, or<br>category). |
| **Value** | The tag value.                                                                |

AWS CLI

###### To view framework details in the AWS CLI

1. To identify the framework that you want to review, run the [list-assessment-frameworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessment-frameworks.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessment-frameworks.html") command and specify a
   `--framework-type`. Either, you can retrieve a list of standard
   frameworks. Or, you can retrieve a list of custom frameworks.

In the following example, replace the `placeholder
 text` with either `Custom` or
`Standard`.

```
 aws auditmanager list-assessment-frameworks --framework-type `Custom/Standard`
```

The response returns a list of frameworks. Find the framework that you want to
review, and take note of the framework ID and Amazon Resource Name (ARN). 2. To get the framework details, run the [get-assessment-framework](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-assessment-framework.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-assessment-framework.html") command and specify the
`--framework-id`.

In the following example, replace the `placeholder
 text` with your own information.

```
aws auditmanager get-assessment-framework --framework-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
```

###### Tip

The framework details are returned in JSON format. To understand this data, see
[get-assessment-framework Output](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-assessment-framework.html#output "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-assessment-framework.html#output") in the _AWS CLI
Command Reference_. 3. To see the tags for a framework, use the [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-tags-for-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-tags-for-resource.html") command and specify the
`--resource-arn` for the framework.

In the following example, replace the `placeholder
 text` with your own information:

```
aws auditmanager list-tags-for-resource --resource-arn arn:aws:auditmanager:`us-east-1`:`111122223333`:assessmentFramework/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
```

For more information about tags in Audit Manager, see [Tagging AWS Audit Manager
resources](tagging.md "tagging.md").

Audit Manager API

###### To view framework details using the API

1. To identify the framework that you want to review, use the [ListAssessmentFrameworks](../APIReference/API_ListAssessmentFrameworks.md "../APIReference/API_ListAssessmentFrameworks.md") operation and specify a [frameworkType](../APIReference/API_ListAssessmentFrameworks.md#auditmanager-ListAssessmentFrameworks-request-frameworkType "../APIReference/API_ListAssessmentFrameworks.md#auditmanager-ListAssessmentFrameworks-request-frameworkType"). Either, you can return a list of standard frameworks. Or,
   you can return a list of custom frameworks.

From the response, find the framework that you want to review and note the
framework ID and Amazon Resource Name (ARN). 2. To get the framework details, use the [GetAssessmentFramework](../APIReference/API_GetAssessmentFramework.md "../APIReference/API_GetAssessmentFramework.md") operation. In the request, specify the [frameworkId](../APIReference/API_GetAssessmentFramework.md#auditmanager-GetAssessmentFramework-request-frameworkId "../APIReference/API_GetAssessmentFramework.md#auditmanager-GetAssessmentFramework-request-frameworkId") that you got from step 1.

###### Tip

The framework details are returned in JSON format. To understand this data,
see [GetAssessmentFramework Response Elements](../APIReference/API_GetAssessmentFramework.md#API_GetAssessmentFramework_ResponseElements "../APIReference/API_GetAssessmentFramework.md#API_GetAssessmentFramework_ResponseElements") in the _AWS Audit Manager API Reference_. 3. To see tags for the framework, use the [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") operation. In the request, specify the framework
[resourceArn](../APIReference/API_ListTagsForResource.md#auditmanager-ListTagsForResource-request-resourceArn "../APIReference/API_ListTagsForResource.md#auditmanager-ListTagsForResource-request-resourceArn") that you got from step 1.

For more information about tags in Audit Manager, see [Tagging AWS Audit Manager resources](tagging.md "tagging.md").

For more information about these API operations, choose any of the links in the
previous procedure to read more in the _AWS Audit Manager API
Reference_. This includes information about how to use these operations and
parameters in one of the language-specific AWS SDKs.

## Next steps

From the framework details page, you can [create an assessment from
the framework](create-assessments.md "create-assessments.md") or [make an
editable copy of the framework](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md").

If you're reviewing a custom framework, you can also [edit](edit-custom-frameworks.md "edit-custom-frameworks.md"), [delete](delete-custom-framework.md "delete-custom-framework.md"), or [share](share-custom-framework.md "share-custom-framework.md") the framework.

## Additional resources

- [On my custom framework details page, I’m prompted to recreate my custom framework](framework-issues.md#recreate-framework-post-common-controls "framework-issues.md#recreate-framework-post-common-controls")
- [I can’t make a copy of my custom framework](framework-issues.md#cannot-use-custom-framework "framework-issues.md#cannot-use-custom-framework")
