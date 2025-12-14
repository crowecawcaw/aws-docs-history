# Reviewing a standard

control

You can review the details of a standard control by using the Audit Manager console, the Audit Manager
API, or the AWS Command Line Interface (AWS CLI).

## Prerequisites

Make sure your IAM identity has appropriate permissions to view controls in
AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

You can review the details of a standard control by using the Audit Manager console, the Audit Manager
API, or the AWS Command Line Interface (AWS CLI).

Audit Manager console

###### To view standard control details on the Audit Manager console

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Control library**.
3. Choose **Standard** to see the standard controls that are
   provided by AWS.
4. Choose any standard control name to view the details for that
   control.
5. Review the standard control details using the following information as
   reference.

**Overview section**

This section describes the standard control and lists the [data
source types](concepts.md#control-data-source "concepts.md#control-data-source") that it uses to collect evidence.

**Evidence sources tab**

This tab includes the following information:

| Name              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Core controls** | These are the core controls that collect evidence to support the<br>standard control.Each core control uses a predefined grouping of<br>data sources to collect evidence about an AWS service. These data<br>sources are managed for you by AWS, and are automatically updated<br>whenever regulations and standards change and new data sources are<br>identified. Choose any core control to see the underlying data<br>sources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Data sources**  | These are the other AWS managed data sources that collect<br>evidence to support the standard control.<br>• **Mapping** – The specific keyword<br>that's used to collect evidence.<br>+ If the type is _AWS Config_, the mapping is an AWS Config rule<br>(such as `SNS_ENCRYPTED_KMS`).<br>+ If the type is _AWS Security Hub CSPM_, the mapping is a Security Hub CSPM control<br>(such as `EC2.1`).<br>+ If the type is _AWS API<br>calls_, the mapping is an API call (such as<br>`kms_ListKeys`).<br>+ If the type is _AWS CloudTrail_, the mapping is a CloudTrail event (such as<br>`CreateAccessKey`).<br>• **Type** – The type of data source<br>that the evidence comes from.<br>+ If Audit Manager collects the evidence, the type can be _AWS Security Hub CSPM_, _AWS Config_, _AWS CloudTrail_, or _AWS API<br>calls_.<br>+ If you upload your own evidence, the type is _Manual_. A description indicates<br>if the required manual evidence is a *File upload<br>• or a *Text<br>response\*.<br>• **Frequency** – How often Audit Manager<br>collects evidence for an AWS API call data source. |

**Details tab**

This tab includes the following information:

| Name                    | Description                                                                   |
| ----------------------- | ----------------------------------------------------------------------------- |
| **Instructions**        | The directions that describe how to test and remediate the<br>control.        |
| **Testing information** | The recommended testing procedures.                                           |
| **Action plan**         | The recommended actions to take if you need to remediate the<br>control.      |
| **Tags**                | The tags that are associated with the control.                                |
| **Key**                 | The tag key (for example, a compliance standard, regulation, or<br>category). |
| **Value**               | The tag value.                                                                |

AWS CLI

###### To view standard control details in the AWS CLI

1. Follow the steps to [find a
   control](access-available-controls.md "access-available-controls.md"). Make sure to set the `--control-type` as
   `Standard`, and apply any optional filters as needed.

```
aws auditmanager list-controls --control-type Standard
```

2. In the response, identify the control that you want to review and take note of
   the control ID and Amazon Resource Name (ARN).
3. Run the [get-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-control.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-control.html") command and specify the `--control-id`. In the
   following example, replace the `placeholder text` with
   your own information.

```
aws auditmanager get-control --control-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
```

###### Tip

The control details are returned in JSON format. To help you understand this
data, see [get-control Output](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-control.html#output "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-control.html#output") in the _AWS CLI Command
Reference_ 4. To see tag details, run the [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-tags-for-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-tags-for-resource.html") command and specify the
`--resource-arn`. In the following example, replace the
`placeholder text` with your own information.

```
aws auditmanager list-tags-for-resource --resource-arn arn:aws:auditmanager:`us-east-1`:111122223333:control/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
```

Audit Manager API

###### To view standard control details using the API

1. Follow the steps to [find a
   control](access-available-controls.md "access-available-controls.md"). Make sure to set the [controlType](../APIReference/API_ListControls.md#auditmanager-ListControls-request-controlType "../APIReference/API_ListControls.md#auditmanager-ListControls-request-controlType") as `Standard`, and apply any optional filters as
   needed.
2. In the response, identify the control that you want to review and take note of
   the control ID and Amazon Resource Name (ARN).
3. Use the [GetControl](../APIReference/API_GetControl.md "../APIReference/API_GetControl.md")
   operation and specify the [controlId](../APIReference/API_GetControl.md#auditmanager-GetControl-request-controlId "../APIReference/API_GetControl.md#auditmanager-GetControl-request-controlId") that you noted in step 2.

###### Tip

The control details are returned in JSON format. To help you understand this
data, see [GetControl Response Elements](../APIReference/API_GetControl.md#API_GetControl_ResponseElements "../APIReference/API_GetControl.md#API_GetControl_ResponseElements") in the _AWS Audit Manager
API Reference_. 4. To see tag details, use the [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") operation and specify the
[resourceArn](../APIReference/API_ListTagsForResource.md#auditmanager-ListTagsForResource-request-resourceArn "../APIReference/API_ListTagsForResource.md#auditmanager-ListTagsForResource-request-resourceArn") that you noted in step 2.

For more information about these API operations, choose any of the links in this
procedure to read more in the _AWS Audit Manager API
Reference_. This includes information about how to use these operations
and parameters in one of the language-specific AWS SDKs.

## Next steps

You can add a standard control to any of your custom frameworks. For instructions, see
[Creating a custom framework in AWS Audit Manager](custom-frameworks.md "custom-frameworks.md").

You can also customize any standard control so that it meets your needs. For
instructions, see [Making an editable copy of a control in
AWS Audit Manager](customize-control-from-existing.md "customize-control-from-existing.md").

## Additional resources

- [Reviewing a common control](control-library-review-common-controls.md "control-library-review-common-controls.md")
- [Reviewing a core control](control-library-review-core-controls.md "control-library-review-core-controls.md")
- [Reviewing a custom control](control-library-review-custom-controls.md "control-library-review-custom-controls.md")
